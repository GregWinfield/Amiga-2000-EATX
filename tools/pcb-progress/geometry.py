"""Read a saved KiCad board and plot inspection artwork in absolute, top-view mm.

Use KiCad 10's pcbnew Python bindings and matching kicad-cli. The input is never
saved, and kicad-cli works on a private copy to protect the user's project state.
"""
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
from xml.etree import ElementTree as ET

import pcbnew as pcb


COPPER = (pcb.F_Cu, pcb.In1_Cu, pcb.In2_Cu, pcb.B_Cu)
PLOTS = {
    "outline": ("Edge.Cuts", "#8bc3a0"),
    "front": ("F.Cu", "#629371"),
    "back": ("B.Cu", "#54899d"),
    "inner1": ("In1.Cu", "#a07892"),
    "inner2": ("In2.Cu", "#a79a60"),
    "silkF": ("F.Silkscreen", "#dbe7d7"),
    "silkB": ("B.Silkscreen", "#9dbea6"),
    "fab": ("F.Fab", "#abc2aa"),
    "fabB": ("B.Fab", "#8da48b"),
}
PAD_TYPES = {pcb.PAD_ATTRIB_PTH: "PTH", pcb.PAD_ATTRIB_NPTH: "NPTH",
             pcb.PAD_ATTRIB_SMD: "SMD", pcb.PAD_ATTRIB_CONN: "Contact"}
SVG = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG)
ET.register_namespace("xlink", "http://www.w3.org/1999/xlink")


def mm(value):
    return value / pcb.PCB_IU_PER_MM


def xy(point):
    return [mm(point.x), mm(point.y)]


def bounds(box):
    return [mm(box.GetX()), mm(box.GetY()), mm(box.GetWidth()), mm(box.GetHeight())]


def number(value):
    return f"{value:.6f}".rstrip("0").rstrip(".") or "0"


def coords(point):
    return " ".join(number(v) for v in xy(point))


def polygon_path(shape):
    """Use all contours and holes with SVG evenodd filling."""
    parts = []
    for i in range(shape.OutlineCount()):
        rings = [shape.COutline(i)] + [shape.CHole(i, j) for j in range(shape.HoleCount(i))]
        for ring in rings:
            points = ring.CPoints()
            if len(points) >= 3:
                parts.append("M" + " ".join(coords(p) for p in points) + "Z")
    return "".join(parts)


def signature(data):
    return hashlib.sha256(json.dumps(data, separators=(",", ":"), ensure_ascii=False)
                          .encode("utf-8")).hexdigest()


def land_definition(pad, layer):
    kind = pad.GetShape(layer)
    result = [kind, xy(pad.GetSize(layer)), xy(pad.GetOffset(layer))]
    if kind == pcb.PAD_SHAPE_TRAPEZOID:
        result.append(xy(pad.GetDelta(layer)))
    if kind in (pcb.PAD_SHAPE_ROUNDRECT, pcb.PAD_SHAPE_CHAMFERED_RECT):
        result.append(pad.GetRoundRectRadiusRatio(layer))
    if kind == pcb.PAD_SHAPE_CHAMFERED_RECT:
        result.extend([pad.GetChamferPositions(layer), pad.GetChamferRectRatio(layer)])
    if kind == pcb.PAD_SHAPE_CUSTOM:
        # KiCad gives custom copper in its pad-local frame.
        result.append(polygon_path(pad.GetCustomShapeAsPolygon(layer)))
    return result


def hole_svg(item):
    hole = item.GetEffectiveHoleShape()
    width = mm(hole.GetWidth())
    start, end = hole.GetStart(), hole.GetEnd()
    if start == end:
        x, y = xy(start)
        return f'<circle cx="{number(x)}" cy="{number(y)}" r="{number(width / 2)}"/>'
    return (f'<path d="M{coords(start)}L{coords(end)}" stroke="black" '
            f'stroke-width="{number(width)}" stroke-linecap="round"/>')


def collect(board):
    rows, pad_paths, via_shapes = [], [], []
    drills = {layer: [] for layer in COPPER}
    all_holes, pad_holes, via_holes = [], [], []
    for fp in board.GetFootprints():
        pads, definitions, types = [], [], set()
        for pad in fp.Pads():
            kind = PAD_TYPES[pad.GetAttribute()]
            types.add(kind)
            drill = xy(pad.GetDrillSize())
            name = str(pad.GetNumber())
            layers = [layer for layer in COPPER if pad.IsOnLayer(layer)]
            pads.append(dict(number=name, net=str(pad.GetNetname()), xy=xy(pad.GetPosition()),
                             mount=kind, drill=drill, function=str(pad.GetPinFunction())))
            definitions.append([name, kind, xy(pad.GetFPRelativePosition()),
                                round(pad.GetFPRelativeOrientation().AsDegrees() % 360, 6),
                                drill, pad.GetDrillShape(),
                                [(layer, land_definition(pad, layer)) for layer in layers]])
            # The overlay shows each pad once, including bottom-only SMD pads.
            surface = next((l for l in (pcb.F_Cu, pcb.B_Cu) if l in layers), None)
            if surface is not None and kind != "NPTH":
                shape = pad.GetEffectivePolygon(surface, pcb.ERROR_INSIDE)
                pad_paths.append(polygon_path(shape))
            if drill[0] > 0 and drill[1] > 0:
                hole = hole_svg(pad)
                pad_holes.append(hole)
                all_holes.append(hole)
                for layer in COPPER:  # both PTH and NPTH penetrate the board
                    drills[layer].append(hole)

        # Include the field locations separately so legend-only changes do not
        # masquerade as physical package changes.
        legends = [[field.GetText(), xy(field.GetFPRelativePosition()), field.GetLayerName(),
                    field.IsVisible(), xy(field.GetTextSize()), field.GetTextAngleDegrees() % 360]
                   for field in (fp.Reference(), fp.Value())]
        mount = "THT" if "PTH" in types else "SMD" if "SMD" in types else "Other"
        rows.append(dict(ref=str(fp.GetReference()), value=str(fp.GetValue()),
                         id=str(fp.GetFPIDAsString()), mount=mount,
                         xy=xy(fp.GetPosition()), bounds=bounds(fp.GetBoundingBox(False, False)),
                         angle=fp.GetOrientationDegrees(), side=board.GetLayerName(fp.GetLayer()),
                         sheet=str(fp.GetSheetname()), description=str(fp.GetLibDescription()),
                         nets=sorted({p["net"] for p in pads if p["net"]}),
                         pads=sorted(pads, key=lambda p: (p["number"], p["xy"])),
                         signature=signature(sorted(definitions)), legendSignature=signature(legends)))

    for track in board.GetTracks():
        if not isinstance(track, pcb.PCB_VIA):
            continue
        layer = next((l for l in COPPER if track.IsOnLayer(l)), None)
        if layer is None:
            raise ValueError("Via has no enabled copper layer")
        x, y = xy(track.GetPosition())
        via_shapes.append(f'<circle cx="{number(x)}" cy="{number(y)}" '
                          f'r="{number(mm(track.GetWidth(layer)) / 2)}"/>')
        hole = hole_svg(track)
        via_holes.append(hole)
        if track.IsOnLayer(pcb.F_Cu) and track.IsOnLayer(pcb.B_Cu):
            all_holes.append(hole)
        for layer in COPPER:
            if track.IsOnLayer(layer):
                drills[layer].append(hole)
    pad_graphics = "".join(f'<path d="{p}" fill-rule="evenodd"/>' for p in sorted(pad_paths) if p)
    return (sorted(rows, key=lambda row: row["ref"]), pad_graphics, "".join(sorted(via_shapes)),
            drills, all_holes, pad_holes, via_holes)


def svg_document(box, content, holes=()):
    x, y, w, h = map(number, box)
    if holes:
        # A true transparent knockout. Other visible layers remain visible
        # through it. Use absolute user coordinates for both mask and content.
        rect = f'x="{x}" y="{y}" width="{w}" height="{h}"'
        content = (f'<defs><mask id="drills" maskUnits="userSpaceOnUse" {rect}>'
                   f'<rect {rect} fill="white"/><g fill="black">{"".join(sorted(holes))}</g>'
                   f'</mask></defs><g mask="url(#drills)">{content}</g>')
    return f'<svg xmlns="{SVG}" viewBox="{x} {y} {w} {h}">{content}</svg>\n'


def plot_program():
    name = "kicad-cli.exe" if os.name == "nt" else "kicad-cli"
    paths = (os.environ.get("KICAD_CLI"), Path(sys.executable).with_name(name),
             shutil.which(name))
    for path in paths:
        if path and Path(path).is_file():
            return str(path)
    raise FileNotFoundError("Install KiCad 10 and set KICAD_CLI to its kicad-cli executable")


def native_plots(board_file, destination, box, drills):
    """Plot saved copper fills and graphic strokes natively, without refilling."""
    with tempfile.TemporaryDirectory(prefix="pcb-dashboard-plot-") as td:
        scratch = Path(td)
        local = scratch / board_file.name
        shutil.copyfile(board_file, local)
        project = board_file.with_suffix(".kicad_pro")
        if project.is_file():
            shutil.copyfile(project, local.with_suffix(".kicad_pro"))
        plot_dir = scratch / "plots"
        process = subprocess.run([plot_program(), "pcb", "export", "svg", "--mode-multi",
                                  "--page-size-mode", "1", "--scale", "1", "--black-and-white",
                                  "--drill-shape-opt", "0", "--exclude-drawing-sheet",
                                  "--layers", ",".join(layer for layer, _ in PLOTS.values()),
                                  "-o", str(plot_dir), str(local)], capture_output=True, text=True,
                                 encoding="utf-8", errors="replace")
        if process.returncode:
            raise RuntimeError("KiCad SVG plot failed:\n" + process.stdout + process.stderr)
        paths = {}
        copper_by_key = dict(front=pcb.F_Cu, back=pcb.B_Cu, inner1=pcb.In1_Cu, inner2=pcb.In2_Cu)
        for key, (layer, tint) in PLOTS.items():
            filename = f"{local.stem}-{layer.replace('.', '_')}.svg"
            root = ET.parse(plot_dir / filename).getroot()
            # Page-mode 1 and scale 1 preserve KiCad's physical mm coordinates:
            # no fit-to-page origin shift, board-wide rotation, or back-side mirroring.
            view = list(map(float, root.attrib["viewBox"].split()))
            if (view[:2] != [0, 0] or not root.attrib["width"].endswith("mm")
                    or abs(float(root.attrib["width"][:-2]) - view[2]) > 0.0001):
                raise ValueError(f"Unexpected native SVG coordinate system for {layer}")
            graphics = [node for node in root if node.tag.rsplit("}", 1)[-1] not in ("title", "desc")]
            content = "".join(ET.tostring(node, encoding="unicode") for node in graphics)
            content = re.sub(r"(fill|stroke):#[0-9A-Fa-f]{6}", lambda m: m[1] + ":" + tint, content)
            content = re.sub(r"[ \t]+\n", "\n", content)
            holes = drills[copper_by_key[key]] if key in copper_by_key else ()
            (destination / f"{key}.svg").write_text(svg_document(box, content, holes),
                                                      encoding="utf-8", newline="\n")
            paths[key] = key + ".svg"
        return paths


def extract(pcb_path, output_directory):
    """Export artwork and selectable footprint data; all geometry is top-view mm."""
    board_file = Path(pcb_path).resolve(strict=True)
    dest = Path(output_directory)
    dest.mkdir(parents=True, exist_ok=True)
    board = pcb.LoadBoard(str(board_file))
    if not board or board.GetCopperLayerCount() != 4:
        raise ValueError(f"Expected a four-copper-layer KiCad PCB in {board_file}")
    silhouette = pcb.SHAPE_POLY_SET()
    if not board.GetBoardPolygonOutlines(silhouette, False) or silhouette.OutlineCount() < 1:
        raise ValueError(f"Could not read a closed Edge.Cuts outline from {board_file}")
    box = bounds(silhouette.BBox())  # centreline boundary, excluding the edge pen width
    rows, pads, vias, drills, all_holes, pad_holes, via_holes = collect(board)
    if not rows or not any(row["pads"] for row in rows):
        raise ValueError(f"Missing PCB footprints or pads in {board_file}")
    layers = native_plots(board_file, dest, box, drills)
    substrate = f'<path fill="#22563c" fill-rule="evenodd" d="{polygon_path(silhouette)}"/>'
    for key, graphics, holes in [("substrate", substrate, all_holes),
                                 ("pads", f'<g fill="#d9bf78">{pads}</g>', pad_holes),
                                 ("vias", f'<g fill="#a88e56">{vias}</g>', via_holes)]:
        (dest / f"{key}.svg").write_text(svg_document(box, graphics, holes), encoding="utf-8",
                                         newline="\n")
        layers[key] = key + ".svg"
    with board_file.open(encoding="utf-8-sig") as source:
        header = source.read(2048)
    version = re.search(r"\(version\s+(\d+)\)", header)
    if not version:
        raise ValueError(f"Missing KiCad PCB file version in {board_file}")
    return dict(bounds=box, footprints=rows, layers=layers, kicadVersion=pcb.Version(),
                pcbFileFormat=version[1], titleBlock=dict(title=board.GetTitleBlock().GetTitle(),
                revision=board.GetTitleBlock().GetRevision(), date=board.GetTitleBlock().GetDate()),
                padCount=sum(len(row["pads"]) for row in rows), viaCount=len(via_holes))
