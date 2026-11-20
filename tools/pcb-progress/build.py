"""Build the offline board review from two committed KiCad engineering snapshots."""
import argparse
import csv
import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[2]
PROJECT = "2000EATX-KiCAD-R31"
BOARD = PROJECT + "/2000ATX.kicad_pcb"
BASELINE = "dfde4574396919e9cc51f5079ef054e4de3b9a07"
VERIFIED = "06815e2"
INPUTS = [PROJECT, "audit", "SIP_NETWORK_AUDIT.csv", "SCENARIO_B_PLUS_DESIGN.md",
          "SCENARIO_B_PLUS_IMPLEMENTATION.md", "ORIGINAL_A2000_REV62_COMPARISON.md",
          "COMMODORE_COMPONENT_COMPARISON.md", "coupon/CONNECTOR_RESOLUTION.md",
          "coupon/FABRICATION_READINESS.md", "coupon/MEASUREMENT_PLAN.md"]


def git(*args):
    return subprocess.check_output(["git", "-C", str(ROOT), *args], text=True, encoding="utf-8").strip()


def kicad_python():
    try:
        import pcbnew
        return pcbnew
    except ImportError as exc:
        install = Path(os.environ.get("ProgramFiles", "C:/Program Files")) / "KiCad/10.0/bin/python.exe"
        interpreters = [os.environ.get("KICAD_PYTHON"), str(install), "/usr/bin/python3"]
        for py in filter(None, interpreters):
            if Path(py).is_file() and Path(py).resolve() != Path(sys.executable).resolve():
                if subprocess.run([py, "-c", "import pcbnew"], capture_output=True).returncode == 0:
                    raise SystemExit(subprocess.call([py, *sys.argv]))
        raise RuntimeError("Install KiCad 10 with pcbnew, or set KICAD_PYTHON to its Python interpreter.") from exc


def snapshot(commit, dest, paths):
    archive = dest.with_suffix(".zip")
    subprocess.run(["git", "-C", str(ROOT), "-c", "core.autocrlf=false", "archive", "--format=zip", "-o", str(archive),
                    commit, "--", *paths], check=True)
    with ZipFile(archive) as z:
        z.extractall(dest)


def dump(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":"), allow_nan=False) + "\n",
                    encoding="utf-8")


def validate(board, directory):
    if len(board["bounds"]) != 4 or min(board["bounds"][2:]) <= 0:
        raise ValueError("Invalid Edge.Cuts bounds")
    refs = [f["ref"] for f in board["footprints"]]
    if not refs or len(set(refs)) != len(refs):
        raise ValueError("Missing or duplicate CAD reference in board")
    for key, filename in board["layers"].items():
        if not (directory / filename).is_file():
            raise ValueError(f"Missing {key} asset {filename}")


def static_report(folder, data, provenance):
    folder.mkdir()
    rows = data["components"]
    fields = ["ref", "value", "category", "status", "proposedPackage", "proposedFootprint",
              "implemented", "electrical", "mechanical", "fabrication", "physical"]
    with (folder / "components.csv").open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fields, extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    dump(folder / "summary.json", {"source": provenance, "stats": data["stats"],
                                   "verification": data["verification"], "warnings": data["warnings"]})


def build(args):
    pcbnew = kicad_python()
    from geometry import extract
    from manifest import build as manifest
    selected = git("rev-parse", "--verify", args.source + "^{commit}")
    original = git("rev-parse", "--verify", args.baseline + "^{commit}")
    if args.source == "HEAD" and git("status", "--porcelain", "--", *INPUTS):
        raise ValueError("Uncommitted engineering inputs. Commit them or select an explicit committed --source.")
    commit = git("log", "-1", "--format=%H", selected, "--", *INPUTS)
    active = git("branch", "--show-current")
    branch = args.source if args.source != "HEAD" else active or "detached"
    design_branch = "implementation/scenario-b-plus"
    design_refs = [design_branch, "refs/remotes/origin/" + design_branch]
    if branch in {"feature/interactive-pcb-dashboard", "HEAD", "detached"} and any(
        subprocess.run(["git", "-C", str(ROOT), "merge-base", "--is-ancestor", commit, ref],
                       capture_output=True).returncode == 0 for ref in design_refs
    ):
        branch = design_branch
    with tempfile.TemporaryDirectory(prefix="a2000-dashboard-") as temp:
        temp = Path(temp)
        source, base, data = temp / "current", temp / "original", temp / "data"
        snapshot(commit, source, INPUTS)
        snapshot(original, base, [PROJECT])
        results = json.loads((source / "audit/implementation/slots/verification.json").read_text())
        tested = results.get("source_commit", VERIFIED)
        checked = subprocess.run(["git", "-C", str(ROOT), "diff", "--quiet", tested, commit, "--",
                                  PROJECT], check=False)
        if checked.returncode not in (0, 1):
            raise ValueError(f"Cannot resolve verification snapshot {tested}")
        date = datetime.fromtimestamp(int(os.environ.get("SOURCE_DATE_EPOCH", datetime.now().timestamp())),
                                      timezone.utc).replace(microsecond=0).isoformat()
        p = {"schema": 1, "branch": branch, "commit": commit, "baselineCommit": original,
             "boardCommit": git("log", "-1", "--format=%H", commit, "--", BOARD),
             "verified": checked.returncode == 0, "verifiedCommit": git("rev-parse", tested),
             "kicad": str(pcbnew.GetBuildVersion()), "generated": date,
             "boardFile": BOARD, "boardSHA256": hashlib.sha256((source / BOARD).read_bytes()).hexdigest()}
        boards = {}
        for side, src in [("original", base), ("current", source)]:
            out = data / side
            out.mkdir(parents=True)
            print(f"Exporting {side} KiCad geometry", flush=True)
            boards[side] = extract(src / BOARD, out)
            validate(boards[side], out)
            dump(out / "board.json", boards[side])
        details = manifest(source, boards["original"], boards["current"], p)
        details["provenance"] = p
        dump(data / "manifest.json", details)
        report = temp / "report"
        static_report(report, details, p)
        # Only publish a complete validated export. Keep unrelated existing report files.
        for src, dst in [(data, ROOT / "dashboard/data"), (report, ROOT / "reports/pcb-progress")]:
            shutil.copytree(src, dst, dirs_exist_ok=True)
        print(f"Built {len(details['components'])} inspection records from {commit}.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", default="HEAD", help="Committed engineering revision")
    parser.add_argument("--baseline", default=BASELINE, help="Jason Beer's original EATX revision")
    try:
        build(parser.parse_args())
    except (OSError, ValueError, KeyError, RuntimeError, subprocess.CalledProcessError) as error:
        sys.exit(f"Dashboard build failed: {error}")
