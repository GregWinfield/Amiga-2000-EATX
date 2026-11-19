"""Check the socket lands and drill hits in the three KiCad review archives."""
from pathlib import Path
import re
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parent / "fabrication-review"
# KiCad writes the copper in mm (4.6) and metric Excellon hits at 0.001 mm.
CENTRES = {(207139690 + offset, -(56532900 + station * 2540000))
           for station in range(50) for offset in (-2425000, 2425000)}


def read_copper(data, width):
    assert "%FSLAX46Y46*%" in data and "%MOMM*%" in data
    apertures = {}
    seen = set()
    for line in data.splitlines():
        definition = re.fullmatch(r"%ADD(\d+)(C|RoundRect),([^*]+)\*%", line)
        if definition:
            code, kind, params = definition.groups()
            vals = list(map(float, params.split("X")))
            if kind == "C":
                apertures[code] = (vals[0], vals[0])
            elif vals[-1] == 0:
                # KiCad axis-aligned RoundRect macro, four corner centres + radius.
                apertures[code] = tuple(max(v) - min(v) + 2 * vals[0]
                                       for v in (vals[1:9:2], vals[2:9:2]))
        select = re.fullmatch(r"D(\d+)\*", line)
        if select:
            current = select[1]
        flash = re.fullmatch(r"X(-?\d+)Y(-?\d+)D03\*", line)
        if flash:
            pt = (int(flash[1]), int(flash[2]))
            if pt in CENTRES:
                assert all(abs(w - width) < 0.00001 for w in apertures[current]), pt
                seen.add(pt)
    assert seen == CENTRES, CENTRES - seen


def read_drill(data):
    assert "METRIC" in data and "absolute / metric / decimal" in data
    tool, = re.findall(r"^(T\d+)C1\.020$", data, re.M)
    block = re.search("^" + tool + r"\n((?:X[^\n]+\n)+)", data, re.M)[1]
    hits = sorted((round(float(x) * 1000), round(float(y) * 1000))
                  for x, y in re.findall(r"X(-?[\d.]+)Y(-?[\d.]+)", block))
    assert hits == sorted((round(x / 1000), round(y / 1000)) for x, y in CENTRES)


if __name__ == "__main__":
    for design in "ABC":
        with ZipFile(ROOT / f"Zorro-{design}-review.zip") as archive:
            assert archive.testzip() is None
            for suffix, diameter in [(".gtl", 1.53), (".g1", 1.80), (".g2", 1.80), (".gbl", 1.53)]:
                name, = [f for f in archive.namelist() if f.endswith(suffix)]
                read_copper(archive.read(name).decode(), diameter)
            read_drill(archive.read(f"Zorro-{design}.drl").decode().replace("\r\n", "\n"))
        print(f"{design}: 100 socket pads on each of four copper layers and 100 matching 1.02 mm holes.")
