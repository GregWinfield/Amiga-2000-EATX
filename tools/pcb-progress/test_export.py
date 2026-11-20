"""Validate the published snapshots and the package mapping rules (standard library)."""
import csv
from collections import Counter
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
import xml.etree.ElementTree as XML

import manifest

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "dashboard/data"


def read(name):
    return json.loads((DATA / name).read_text(encoding="utf-8"))


class ExportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = read("manifest.json")
        cls.o = read("original/board.json")
        cls.c = read("current/board.json")

    def test_asset_coordinates(self):
        for side, board in [("original", self.o), ("current", self.c)]:
            self.assertEqual(len({f["ref"] for f in board["footprints"]}), len(board["footprints"]))
            self.assertEqual(sum(len(f["pads"]) for f in board["footprints"]), board["padCount"])
            for filename in board["layers"].values():
                svg = XML.parse(DATA / side / filename).getroot()
                self.assertEqual(list(map(float, svg.attrib["viewBox"].split())), board["bounds"])
        self.assertEqual(self.o["bounds"], [100.78969, 53.8675, 304.8, 330.2])
        if self.m["provenance"]["verified"]:
            self.assertEqual(self.o["bounds"], self.c["bounds"])

    def test_source_and_pad_coordinates(self):
        p = self.m["provenance"]
        source = subprocess.check_output(["git", "-C", str(ROOT), "show", p["commit"] + ":" + p["boardFile"]])
        self.assertEqual(hashlib.sha256(source).hexdigest(), p["boardSHA256"])
        with (ROOT / "audit/baseline/pcb-pads.csv").open(encoding="utf-8-sig") as f:
            rows = list(csv.DictReader(f))
        expected = Counter((r["reference"], r["pad"], r["net"], round(float(r["x_mm"]), 4),
                            round(float(r["y_mm"]), 4)) for r in rows)
        def pads(board):
            return Counter((f["ref"], p["number"], p["net"], round(p["xy"][0], 4), round(p["xy"][1], 4))
                           for f in board["footprints"] for p in f["pads"])
        self.assertEqual(expected, pads(self.o))
        if p["boardCommit"].startswith("06815e2"):
            original = {f["ref"]: f for f in self.o["footprints"]}
            for f in self.c["footprints"]:
                if f["ref"] != "R803":
                    self.assertEqual(f["xy"], original[f["ref"]]["xy"])
                if f["ref"] in {"CN601", "CN602", "CN603", "CN604", "CN605"}:
                    old = {p["number"]: p for p in original[f["ref"]]["pads"]}
                    for p in f["pads"]:
                        q = old[p["number"]]
                        self.assertEqual(p["xy"][1], q["xy"][1])
                        self.assertAlmostEqual(abs(p["xy"][0]-q["xy"][0]), .115, places=6)
                        self.assertEqual(p["drill"], [1.02, 1.02])

    def test_population_and_mappings(self):
        s = self.m["stats"]
        rows = self.m["components"]
        actual = [r for r in rows if r["currentRefs"] and r["status"] != "excluded"]
        self.assertEqual(Counter(r["status"] for r in actual), Counter(s["status"]))
        self.assertEqual(len(actual), s["current"]["total"])
        self.assertEqual(sum(r["currentMount"] == "THT" for r in actual), s["current"]["tht"])
        for g in self.m["groups"]:
            self.assertEqual(set(g["members"]), {b["eatx_element"].split(".")[0] for b in g["branches"]})
        if self.m["provenance"]["boardCommit"].startswith("06815e2"):
            self.assertEqual([r["ref"] for r in rows if r["status"] == "converted"], ["R803"])
            self.assertEqual([s[k]["tht"] for k in ("original","current","target")], [65,66,342])
            self.assertEqual(s["target"]["total"], 546)
            self.assertEqual(sum(len(g["branches"]) for g in self.m["groups"]), 44)
            self.assertTrue(all(not g["implemented"] for g in self.m["groups"]))
        for r in self.m["regions"]:
            self.assertTrue(r["refs"] and r["bounds"], r["name"])

    def test_active_and_invalid_sip_mapping(self):
        group = self.m["groups"][0]
        members = group["members"]
        target = {r: {"physical_package": group["ref"], "construction": "SIP element"} for r in members}
        pins = [{"number": b["bplus_element"].split(".")[1], "net": b["eatx_private"]} for b in group["branches"]]
        pins.append({"number": "1", "net": group["branches"][0]["return_net"]})
        placed = {group["ref"]: {"mount": "THT", "pads": pins}}
        mapping, groups, _ = manifest.physical_groups(target, placed, group["branches"])
        self.assertEqual(mapping[group["ref"]], members)
        self.assertTrue(groups[0]["implemented"])
        pins.pop()
        with self.assertRaises(ValueError):
            manifest.physical_groups(target, placed, group["branches"])

    def test_missing_input_is_explicit(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(FileNotFoundError):
                manifest.table(Path(directory), "missing.csv", "reference")
            (Path(directory) / "input.csv").write_text("wrong\nx\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "missing columns"):
                manifest.table(Path(directory), "input.csv", "reference")


if __name__ == "__main__":
    unittest.main()
