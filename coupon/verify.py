"""Verify coupon copper against its schematic and the audited EATX terminations.

Run with KiCad 10's Python interpreter. kicad-cli must be beside that interpreter
or on PATH. Running this check produces reports only in a temporary directory.
"""
import csv
import heapq
import math
from collections import defaultdict
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET

import pcbnew as pcb

ROOT = Path(__file__).resolve().parent
SIGNALS = ["BD14", "BD13", "BD12", "BD11", "BD0", "BD1", "BD2", "BD3", "BD4"]



def xy(point):
    return point.x, point.y


def path_mm(board, first, last):
    """Length between pad centres on these single-layer branches and trunks."""
    assert first.GetNetname() == last.GetNetname()
    graph = defaultdict(list)
    for track in board.GetTracks():
        if track.GetNetname() != first.GetNetname():
            continue
        if isinstance(track, pcb.PCB_VIA):
            continue
        a = (*xy(track.GetStart()), track.GetLayer())
        b = (*xy(track.GetEnd()), track.GetLayer())
        graph[a].append((b, track.GetLength()))
        graph[b].append((a, track.GetLength()))
    ends = []
    for pad in (first, last):
        key = (*xy(pad.GetPosition()), -1)
        ends.append(key)
        for vertex in list(graph):
            x, y, layer = vertex
            if layer < 0 or not pad.IsOnLayer(layer):
                continue
            if pad.HitTest(pcb.VECTOR2I(x, y)):
                delta = math.dist(key[:2], vertex[:2])
                graph[key].append((vertex, delta))
                graph[vertex].append((key, delta))
    queue = [(0, ends[0])]
    visited = set()
    while queue:
        distance, vertex = heapq.heappop(queue)
        if vertex == ends[1]:
            return distance / 1e6
        if vertex in visited:
            continue
        visited.add(vertex)
        for other, length in graph[vertex]:
            if other not in visited:
                heapq.heappush(queue, (distance + length, other))
    raise ValueError(f"No copper path on {first.GetNetname()}")


def check(design, baseline, cli, tmp):
    stem = ROOT / design / f"Zorro-{design}"
    sch, layout = stem.with_suffix(".kicad_sch"), stem.with_suffix(".kicad_pcb")
    xml = tmp / "pins.xml"
    for args in [
        ["sch", "erc", "--exit-code-violations", "-o", tmp / "erc.rpt", sch],
        ["pcb", "drc", "--schematic-parity", "--exit-code-violations", "-o", tmp / "drc.rpt", layout],
        ["sch", "export", "netlist", "--format", "kicadxml", "-o", xml, sch],
    ]:
        subprocess.run([cli, *args], check=True)
    board = pcb.LoadBoard(str(layout))
    assert board.GetCopperLayerCount() == 4
    footprints = {f.GetReference(): f for f in board.GetFootprints()}
    pads = {(r, p.GetNumber()): p for r, f in footprints.items() for p in f.Pads() if p.GetNumber()}
    assert all(p.GetDrillSize().x == 1020000 for p in footprints["J2"].Pads())
    expected = {(node.get("ref"), node.get("pin")): net.get("name")
                for net in ET.parse(xml).findall("./nets/net") for node in net.findall("node")}
    assert {key: pad.GetNetname() for key, pad in pads.items()} == expected
    results = []
    for lane, signal in enumerate(SIGNALS, 1):
        src = pads["J1", str(2 * lane)]
        historical = baseline[signal]
        socket = pads["J2", historical["nearest_slot_pad"].split(".")[1]]
        cap = f"C{lane}"
        rpin = ("RN1", str(lane + 1)) if design == "B" else (f"R{lane}", "2")
        private = "RC_" + signal
        assert expected[rpin] == expected[cap, "1"] == private
        assert sum(net == private for net in expected.values()) == 2
        assert expected[rpin[0], "1"] == "GND"
        assert src.GetNetname() == socket.GetNetname() == expected[cap, "2"] == signal
        assert expected[f"CL{lane}", "1"] == expected[f"TP{lane}", "1"] == signal
        assert expected[f"CL{lane}", "2"] == expected[f"TP{lane+10}", "1"] == "GND"
        tap = path_mm(board, socket, pads[cap, "2"])
        junction = path_mm(board, pads[cap, "1"], pads[rpin])
        if design == "A":
            for length, field in [(tap, "baseline_slot_route_mm"), (junction, "baseline_private_route_mm")]:
                assert abs(length - float(historical[field])) < 0.001
        results.append((design, lane, signal, path_mm(board, src, socket), tap, junction))
    return results


def main():
    with (ROOT.parent / "audit/layout/termination-paths.csv").open() as f:
        baseline = {r["signal"]: r for r in csv.DictReader(f)
                    if r["scenario"] == "B SIP" and r["nearest_slot_pad"].startswith("CN605.")}
    cli = shutil.which("kicad-cli") or str(Path(sys.executable).with_name("kicad-cli.exe"))
    with tempfile.TemporaryDirectory() as folder:
        results = [row for design in "ABC" for row in check(design, baseline, cli, Path(folder))]
    with (ROOT / "lanes.csv").open() as f:
        records = {(r["design"], int(r["lane"])): r for r in csv.DictReader(f)}
    for design, lane, signal, trunk, tap, junction in results:
        row = records[design, lane]
        assert row["signal"] == signal
        for actual, key in [(trunk, "trunk_mm"), (tap, "tap_to_cap_mm"), (junction, "private_mm")]:
            assert abs(actual - float(row[key])) < 0.001
    print("Verified all 27 routed lanes, pin maps, design checks and published lengths.")


if __name__ == "__main__":
    main()
