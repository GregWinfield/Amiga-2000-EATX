"""Join KiCad package identities to the audited Scenario B+ construction register.

All bounds and origins use KiCad board coordinates in millimetres. A physical
package and an electrical branch have different identities in this project.
"""
import csv
import json
import math
import re
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from zipfile import ZipFile

PLAN = "audit/component-plan.csv"
TARGET = "audit/rev62/bplus-components.csv"
CROSSWALK = "audit/rev62/termination-crosswalk.csv"
FOOTPRINTS = "audit/rev62/reference-footprints.csv"
NETWORKS = "audit/rev62/historical-networks.csv"
SIPS = "SIP_NETWORK_AUDIT.csv"
HISTORY = "ORIGINAL_A2000_REV62_COMPARISON.md"
CIRCUITS = "COMMODORE_COMPONENT_COMPARISON.md"
DESIGN = "SCENARIO_B_PLUS_DESIGN.md"
IMPLEMENTATION = "SCENARIO_B_PLUS_IMPLEMENTATION.md"
VERIFICATION = "audit/implementation/slots/verification.json"
RAW = "audit/implementation/slots/kicad-reports.zip"
BASE_NETLIST = "audit/baseline/schematic.xml"
MISSING = "Not documented"
STATUS = ("converted", "original", "planned", "retained", "unresolved")
CATEGORIES = ("Resistors", "Resistor networks", "Capacitors", "Diodes", "Transistors",
              "Logic ICs", "Connectors", "Other")
EXCLUDED = {"Graphic", "Mounting hole", "Copper jumper"}


def table(root, name, required):
    with (root / name).open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        missing = set(required.split()) - set(reader.fieldnames or ())
        if missing:
            raise ValueError(f"{name} missing columns: {sorted(missing)}")
        rows = list(reader)
    if not rows or any(None in r or None in r.values() for r in rows):
        raise ValueError(f"{name} contains missing or malformed rows")
    return rows


def index(rows, key, source):
    result = {}
    for row in rows:
        value = row[key]
        if not value or value in result:
            raise ValueError(f"{source}: missing or duplicate {key} {value!r}")
        result[value] = row
    return result


def doc_table(root, path, header):
    """Read the existing report table, retaining the engineering author's wording."""
    content = (root / path).read_text(encoding="utf-8-sig").splitlines()
    start = next((i for i, line in enumerate(content) if line.startswith("| " + header + " |")), None)
    if start is None:
        raise ValueError(f"{path}: expected table headed {header!r}")
    rows = []
    size = len(content[start].strip("|").split("|"))
    for line in content[start + 2:]:
        if not line.startswith("|"):
            break
        row = [cell.strip() for cell in line.strip("|").split("|")]
        if len(row) != size:
            raise ValueError(f"{path}: malformed table row {line!r}")
        rows.append(row)
    if not rows:
        raise ValueError(f"{path}: empty table {header!r}")
    return rows


def plain(text):
    return re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text).replace("**", "").replace(chr(96), "")


def verification(root, provenance):
    evidence = provenance["evidenceFile"]
    archive_path = evidence.rsplit("/", 1)[0] + "/kicad-reports.zip"
    report = json.loads((root / evidence).read_text(encoding="utf-8-sig"))
    with ZipFile(root / archive_path) as archive:
        if "reports" in report:
            pcb = json.loads(archive.read("evaluated-drc.json"))
            erc = json.loads(archive.read("evaluated-erc.json"))
            ctrl = json.loads(archive.read("baseline-drc.json"))
            netlist = ET.fromstring(archive.read("evaluated.xml"))
            checks = report["reports"]
            for group, key in (("violations", "violations"), ("schematic_parity", "schematic_parity"),
                               ("unconnected_items", "unconnected_items")):
                for side, document in (("before", ctrl), ("after", pcb)):
                    actual = Counter(item["severity"] for item in document[group])
                    if actual != Counter(checks[key][side]):
                        raise ValueError(f"{evidence}: {group} {side} counts differ from raw report")
            pins = sum(len(net.findall("node")) for net in netlist.findall("./nets/net"))
            if pins != report["schematic_pin_assignments"][1]:
                raise ValueError(f"{evidence}: netlist pin count differs from report")
            fixed = report["fixed_datums"]
            report = {
                "drc": Counter(item["type"] for item in pcb["violations"]),
                "same_tool_control_drc": Counter(item["type"] for item in ctrl["violations"]),
                "erc": checks["erc"]["after"], "unrouted": len(pcb["unconnected_items"]),
                "parity_findings": len(pcb["schematic_parity"]), "nets": len(netlist.findall("./nets/net")),
                "pad_net_changes": report["expanded_differences"], "schematic_pin_assignments": pins,
                "edge_geometry_changed": not report["physical_stackup_and_edges_equal"],
                "stackup_changed": not report["physical_stackup_and_edges_equal"],
                "fixed_mounts": [r for r in fixed if re.fullmatch(r"H\d+", r)],
                "all_five_TE_socket_padstacks_checked": all(f"CN60{i}" in fixed for i in range(1, 6)),
                "changed_pad_geometry_per_ref": report["changed_shared_footprints"] + report["added"],
                "drc_item_deltas": {key: [{"description": row[2], "items": [i[0] for i in row[3]]}
                                           for row in checks["violations"][key]] for key in ("appeared", "absent")}
            }
        else:
            pcb = json.loads(archive.read("slots-pcb.json"))
            erc = json.loads(archive.read("slots-sch.json"))
            ctrl = json.loads(archive.read("control-pcb.json"))
    drc = Counter(v["type"] for v in pcb["violations"])
    errors = Counter(v["severity"] for v in pcb["violations"])
    erc_counts = Counter(v["severity"] for sheet in erc["sheets"] for v in sheet["violations"])
    if (drc != Counter(report["drc"]) or erc_counts != Counter(report["erc"])
            or len(pcb["unconnected_items"]) != report["unrouted"]
            or len(pcb["schematic_parity"]) != report["parity_findings"]
            or Counter(v["type"] for v in ctrl["violations"]) != Counter(report["same_tool_control_drc"])):
        raise ValueError(f"{evidence}: counts differ from the raw {archive_path} archive")
    risks = [{"risk": title, "consequence": plain(effect), "action": plain(action)}
             for title, effect, action in doc_table(root, IMPLEMENTATION, "Risk")]
    return {**report, "currentEvidence": provenance["verified"],
            "resultDate": pcb["date"], "tool": pcb["kicad_version"],
            "drcErrors": errors["error"], "drcWarnings": errors["warning"],
            "controlDrcErrors": sum(v["severity"] == "error" for v in ctrl["violations"]),
            "controlDrcWarnings": sum(v["severity"] == "warning" for v in ctrl["violations"]),
            "risks": risks, "sources": [evidence, archive_path, IMPLEMENTATION,
                                       "coupon/CONNECTOR_RESOLUTION.md", "coupon/FABRICATION_READINESS.md"]}


def footprint_category(ref, fp, plan, sips):
    if ref in sips:
        return "Resistor networks"
    if ref.startswith("CN") or fp["id"].startswith(("Connector_PinHeader", "Connector_Molex")):
        return "Connectors"
    return plan.get("category") or "Other"


def population(mounts):
    counts = Counter(mounts)
    total = sum(counts.values())
    return {"tht": counts["THT"], "smd": counts["SMD"], "total": total,
            "unknown": total - counts["THT"] - counts["SMD"],
            "percent": round(100 * counts["THT"] / total, 1) if total else 0}


def changes(before, after):
    if not before:
        return ["added"]
    if not after:
        return ["removed"]
    if len(before) > 1:
        return ["consolidated", "footprint"]
    a = before[0]
    differences = []
    for field, tag in (("ref", "renamed"), ("id", "footprint"), ("xy", "moved"),
                       ("side", "side"), ("value", "value"), ("signature", "pads")):
        if a[field] != after[field]:
            differences.append(tag)
    if not math.isclose((a["angle"] - after["angle"] + 180) % 360, 180, abs_tol=1e-5):
        differences.append("rotated")
    return differences


def physical_groups(target, current, crosswalk):
    """Activate an explicit package mapping only when its source packages retire."""
    membership = defaultdict(list)
    for ref, item in target.items():
        membership[item["physical_package"]].append(ref)
    by_target = defaultdict(list)
    for row in crosswalk:
        by_target[row["bplus_element"].split(".")[0]].append(row)
    mapped, groups = {}, []
    for dest, members in membership.items():
        if members == [dest]:
            continue
        present = [ref for ref in members if ref != dest and ref in current]
        implemented = dest in current and not present
        if dest in current and present:
            raise ValueError(f"Conflicting active mapping {members} -> {dest}: {present} also placed")
        branches = by_target[dest]
        if len(members) > 1 and {r["eatx_element"].split(".")[0] for r in branches} != set(members):
            raise ValueError(f"{CROSSWALK}: incomplete electrical branch mapping for {dest}")
        if implemented:
            physical = current[dest]
            if physical["mount"] != "THT" and any(target[r]["construction"] == "SIP element" for r in members):
                raise ValueError(f"Implemented SIP mapping {dest} has unexpected mount {physical['mount']}")
            terminals = {(pad["number"], pad["net"]) for pad in physical["pads"]}
            for branch in branches:
                _, pin = branch["bplus_element"].split(".")
                if (pin, branch["eatx_private"]) not in terminals or ("1", branch["return_net"]) not in terminals:
                    raise ValueError(f"{dest}.{pin} disagrees with the accepted private junction or return")
            mapped[dest] = members
        groups.append({"ref": dest, "members": members, "branches": branches,
                       "implemented": implemented, "source": TARGET})
    return mapped, groups, membership


def historical_data(root):
    recon = index(table(root, FOOTPRINTS, "reconstructed_reference reconstructed_library_footprint"),
                  "reconstructed_reference", FOOTPRINTS)
    networks = index(table(root, NETWORKS, "historical_ref topology rev60_parts_list_or_note"),
                     "historical_ref", NETWORKS)
    parts = {r[0].split(",")[0]: r for r in doc_table(root, CIRCUITS, "Circuit/function")}
    return recon, networks, parts


def history_for(ref, component_branches, sip, sources, history_data, sheet, nets):
    recon, networks, circuits = history_data
    entries = []
    seen = set()
    for branch in component_branches:
        cap = ref == branch["eatx_cap"]
        historical = branch["historical_cap"] if cap else branch["historical_element"].split(".")[0]
        if historical in seen:
            continue
        seen.add(historical)
        form = ("Axial multilayer ceramic" if cap else
                "Grounded through-hole SIP" if historical.startswith("RP") else "Individual axial resistor")
        entries.append({"ref": historical, "package": form,
                        "function": f"Series termination capacitor on {branch['historical_signal']}" if cap else
                                    f"Grounded return on {branch['historical_signal']}",
                        "evidence": "Factory 312721 sheets 6–7 and Rev 6.0 parts list; contact crosswalk from the Rev 6.2 reconstruction.",
                        "source": CROSSWALK})
    if ref == "C789":
        entries.append({"ref": "C789", "package": "Axial multilayer ceramic", "function": "ISA D15 termination",
                        "evidence": "The annotated redraw reports a C788 legend and a route to _MASTER on Rev 6 copper. EATX terminates D15 at CN702.C18. Donor-wide applicability is unverified.", "source": HISTORY})
    if sip:
        h = sip["historical_function_lookup"]
        if h in networks and h not in seen:
            entries.append({"ref": h, "package": "Resistor network • " + networks[h]["topology"],
                            "function": networks[h]["bplus_disposition"],
                            "evidence": "SIP audit functional lookup. Pin topology is indexed from the reconstruction.",
                            "source": NETWORKS})
    # The report identifies these circuit-level roles; same designators alone do not establish equivalence.
    circuit = None
    if ref in {"U802", "U804", "U800", "U100", "U102"}:
        circuit = "Bus ownership"
    elif sheet in {"Clocks and Gary", "Agnus Multi Adapter"}:
        circuit = "Clocks and Agnus"
    elif ref in {"Q200", "Q201", "U204", "R230", "R240", "R234", "R244", "U200"}:
        circuit = "Audio"
    elif sheet == "Memory and Kickstart":
        circuit = "Memory and ROM"
    elif ref in {"BT800", "D800", "R803", "U801", "U899", "Y800"}:
        circuit = "RTC and battery"
    elif sheet == "Power":
        circuit = "Power supply"
    if circuit:
        heading, factory, eatx, _, _ = circuits[circuit]
        entries.append({"ref": "Circuit comparison", "package": MISSING, "function": plain(factory),
                        "evidence": f"{heading}. EATX: {plain(eatx)}", "source": CIRCUITS})
    # Only show the reconstruction's body alongside a documented, specifically identified same-ref role.
    documented_roles = {"U100": "68000 processor", "U101": "Agnus", "U102": "Gary", "U200": "Paula",
                        "U204": "Audio filter amplifier", "U800": "Buster", "U802": "Address decoder",
                        "U804": "Interrupt encoder", "U540": "Memory bus buffer", "U541": "Memory bus buffer"}
    if ref in {"Q200", "Q201", "R230", "R240", "R234", "R244", *documented_roles} and ref in recon:
        entries.append({"ref": ref, "package": recon[ref]["reconstructed_library_footprint"],
                        "function": documented_roles.get(ref, "Audio filter"),
                        "evidence": "Role documented in the circuit comparison. Package is from the rhaamo reconstruction.",
                        "source": FOOTPRINTS})
    if entries:
        sources.update([HISTORY, *(e["source"] for e in entries)])
    return entries


def regions_for(components, current):
    specs = [
        ("zorro", "Zorro II expansion", "Zorro_Expansion schematic sheet", lambda r: r["sheet"] == "Zorro_Expansion"),
        ("isa", "ISA expansion", "ISA schematic sheet", lambda r: r["sheet"] == "ISA"),
        ("cpu", "CPU and custom chipset", "CPU, Agnus, Gary, Paula, Denise and Buster packages identified in the schematic and circuit comparison",
         lambda r: r["ref"] in {"U100", "U101", "U102", "U200", "U201", "U800"}),
        ("memory", "Memory circuitry", "Memory and Kickstart schematic sheet", lambda r: r["sheet"] == "Memory and Kickstart"),
        ("decode", "Address decoding and control", "Gary, Buster, U802 decoder and U804 interrupt encoder identified in the bus-ownership comparison",
         lambda r: r["ref"] in {"U102", "U800", "U802", "U804"}),
        ("clock", "Clock circuitry", "Clocks and Gary schematic sheet", lambda r: r["sheet"] == "Clocks and Gary"),
        ("audio", "Audio circuitry", "Named audio/filter references in the component comparison and Paula-sheet nets AUD*, FLT* or Vref",
         lambda r: r["ref"] in {"Q200", "Q201", "U204", "R230", "R240", "R234", "R244", "CN205"}
         or (r["sheet"] == "Paula" and any(n.rsplit("/", 1)[-1].upper().startswith(("AUD", "FLT", "VREF")) for n in r["nets"]))),
        ("rtc", "RTC and battery", "RTC assembly options, crystal and battery-feed components in the Buster/RTC sheet and implementation report",
         lambda r: r["ref"] in {"BT800", "D800", "R803", "U801", "U899", "Y800"}),
        ("power", "Power regulation and filtering", "Power schematic sheet", lambda r: r["sheet"] == "Power"),
    ]
    regions = []
    for key, name, basis, select in specs:
        refs = [r["ref"] for r in components if r["currentRefs"] and r["status"] != "excluded" and select(r)]
        boxes = [current[ref]["bounds"] for ref in refs]
        bounds = None
        if boxes:
            x, y = min(b[0] for b in boxes), min(b[1] for b in boxes)
            bounds = [x, y, max(b[0] + b[2] for b in boxes) - x, max(b[1] + b[3] for b in boxes) - y]
        regions.append({"id": key, "name": name, "refs": refs, "bounds": bounds, "basis": basis})
    return regions



def build(root, original, current, provenance):
    """Return one record per current physical identity plus any removed identity."""
    old = index(original["footprints"], "ref", "original PCB")
    new = index(current["footprints"], "ref", "current PCB")
    audit = index(table(root, PLAN, "reference sheet mount category existing_footprint"), "reference", PLAN)
    target = index(table(root, TARGET, "eatx_reference physical_package authenticity construction proposed_footprint basis_or_release_condition"),
                   "eatx_reference", TARGET)
    hold_register = next((f"audit/implementation/{cycle}/deferred.csv"
                          for cycle in ("cycle8", "cycle7", "cycle6", "cycle5", "cycle4", "resumed-cycle", "accelerated-cycle", "quick-win-cycle")
                          if (root / "audit/implementation" / cycle / "deferred.csv").is_file()), None)
    holds = index(table(root, hold_register, "reference reason_for_hold"), "reference", hold_register) if hold_register else {}
    crosswalk = table(root, CROSSWALK, "eatx_cap eatx_element eatx_private eatx_signal eatx_contact historical_cap historical_element bplus_element return_net")
    index(crosswalk, "eatx_cap", CROSSWALK)
    sips = index(table(root, SIPS, "reference topology historical_function_lookup"), "reference", SIPS)
    history_data = historical_data(root)
    coverage = {r for r, p in audit.items() if p["mount"] not in EXCLUDED}
    if set(old) != set(audit) or coverage != set(target):
        raise ValueError(f"Baseline references disagree with {PLAN} or {TARGET}; reconcile the input snapshot")
    for ref in coverage:
        if audit[ref]["mount"] != old[ref]["mount"] or audit[ref]["existing_footprint"] != old[ref]["id"]:
            raise ValueError(f"{PLAN}: {ref} package or mount disagrees with the original KiCad PCB")
        if (target[ref]["construction"] not in {"THT", "SIP element", "SMD"}
                or target[ref]["authenticity"] not in {"A", "B", "C", "D", "E"}):
            raise ValueError(f"{TARGET}: invalid disposition for {ref}")
    evidence = provenance["verified"]
    report = verification(root, provenance)
    warnings = [] if evidence else ["Stored verification applies to an earlier design. Rerun electrical and mechanical checks for this snapshot."]
    original_symbols = {}
    for comp in ET.parse(root / BASE_NETLIST).findall("./components/comp"):
        symbol = comp.find("libsource")
        if symbol is not None:
            original_symbols[comp.attrib["ref"]] = symbol.get("description", "")
    mapped, groups, membership = physical_groups(target, new, crosswalk)
    consumed = {source for sources in mapped.values() for source in sources}
    old_only = set(old) - set(new) - consumed
    by_ref = defaultdict(list)
    for row in crosswalk:
        for field in ["eatx_cap", "eatx_element", "bplus_element"]:
            ref = row[field].split(".")[0]
            if row not in by_ref[ref]:
                by_ref[ref].append(row)
    group_by_member = {m: group for group in groups for m in group["members"]}
    comps = []
    breakdown = {name: {"name": name, "original": 0, "current": 0, "currentTht": 0, "planned": 0, "converted": 0, "target": 0}
                 for name in CATEGORIES}
    for ref in coverage:
        category = footprint_category(ref, old[ref], audit[ref], sips)
        breakdown[category]["original"] += 1
    for dest, members in membership.items():
        category = footprint_category(dest, old[members[0]], audit[members[0]], sips)
        if len(members) > 1 and any(target[r]["construction"] == "SIP element" for r in members):
            category = "Resistor networks"
        breakdown[category]["target"] += 1
    for ref in sorted(set(new) | old_only):
        after = new.get(ref)
        old_refs = mapped.get(ref, [ref] if ref in old else [])
        before = [old[r] for r in old_refs]
        fp = after or before[0]
        source_ref = old_refs[0] if old_refs else ref
        base_row = audit.get(source_ref, {})
        item = target.get(source_ref, {})
        proposal = item.get("physical_package")
        group = group_by_member.get(source_ref)
        branch_rows = group["branches"] if group else by_ref[ref]
        category = footprint_category(ref, fp, base_row, sips)
        tags = changes(before, after)
        if (before and after and before[0].get("legendSignature") != after.get("legendSignature")
                and not tags):
            tags.append("legend")
        sources = {PLAN} if base_row else set()
        if item:
            sources.add(TARGET)
        actual = after["mount"] if after else None
        if base_row.get("mount") in EXCLUDED:
            status = "excluded"
        elif not after:
            status = "removed"
        elif actual == "THT" and before and all(p["mount"] == "SMD" for p in before):
            status = "converted"
        elif actual == "THT" and before and all(p["mount"] == "THT" for p in before):
            status = "original"
        elif item.get("construction") in {"THT", "SIP element"} and actual == "SMD":
            status = "planned"
        elif item.get("authenticity") in {"C", "D"} and actual == "SMD":
            status = "retained"
        else:
            status = "unresolved"
        if after and status != "excluded":
            cat = breakdown[category]
            cat["current"] += 1
            cat["currentTht"] += int(actual == "THT")
            if status in {"planned", "converted"}:
                cat[status] += 1
        if after and not base_row:
            warnings.append(f"{ref}: present in current PCB; original identity and disposition are undocumented.")
        notes = item.get("basis_or_release_condition") or base_row.get("rationale_and_checks") or MISSING
        if ref in holds:
            hold = holds[ref]
            notes += " Engineering hold: " + hold["reason_for_hold"]
            if hold.get("category"):
                names = {"A": "mechanical placement", "B": "copper geometry", "C": "electrical substitution",
                         "D": "procurement", "E": "physical validation"}
                notes += f" Hold category {hold['category']} ({names[hold['category']]})."
            sources.add(hold_register)
        if item.get("authenticity") == "D" and status != "converted":
            notes = "Optional conversion trial. " + notes
        if item.get("authenticity") == "E":
            notes = "Unresolved engineering disposition. " + notes
        physically_implemented = bool(tags) and tags != ["removed"]
        implemented = ("Changed in current PCB" if physically_implemented else
                       "Removed from current PCB" if not after else
                       "Planned conversion" if status == "planned" else "Original layout retained")
        if ref in holds:
            implemented = "Deferred conversion"
        if not evidence or not after or status == "excluded":
            electrical = MISSING if status == "excluded" or not after else "Awaiting checks on this source revision"
            mechanical = electrical
        else:
            electrical = ("Board pad-net assignment compared; inherited findings remain"
                          if not report["pad_net_changes"] else "See board pad-net difference report")
            mechanical = ("Projected footprint and board datums checked" if ref in report["changed_pad_geometry_per_ref"]
                          else "Footprint origin compared with baseline")
            sources.add(provenance["evidenceFile"])
        if ref in report["changed_pad_geometry_per_ref"]:
            sources.add(IMPLEMENTATION)
        if re.fullmatch(r"CN60[1-5]", ref):
            sources.add("coupon/CONNECTOR_RESOLUTION.md")
            if evidence:
                notes += " Revised TE geometry has provisional layout approval. Supplier acceptance and physical fit remain open."
        if sips.get(ref) or group:
            sources.add(SIPS)
        if branch_rows:
            sources.add(CROSSWALK)
        sheet = (fp.get("sheet") or base_row.get("sheet") or "").strip("/") or MISSING
        sources.add("2000EATX-KiCAD-R31/2000ATX.kicad_pcb")
        desc = (original_symbols.get(source_ref) if before and after and before[0]["value"] == after["value"] else None)
        if desc:
            sources.add(BASE_NETLIST)
        risks = [risk["risk"] for risk in report["risks"] if
                 (ref == "R803" and "R803" in risk["risk"])
                 or (re.fullmatch(r"CN60[1-5]", ref) and risk["risk"] in {"TE manufacturing limits", "Fixed EATX fit", "Expansion power and return continuity"})
                 or (branch_rows and risk["risk"] == "Zorro termination performance" and
                     any(b["eatx_contact"].startswith(("CN601.", "CN605.")) for b in branch_rows))]
        historical = history_for(ref, branch_rows if not group or group["implemented"] else by_ref[ref],
                                 sips.get(ref), sources, history_data, sheet, fp["nets"])
        comps.append({"ref": ref, "value": fp["value"], "status": status, "category": category, "sheet": sheet,
                      "description": desc or fp.get("description") or MISSING,
                      "originalRefs": old_refs, "currentRefs": [ref] if after else [],
                      "originalMount": ", ".join(sorted({p["mount"] for p in before})) or MISSING,
                      "currentMount": actual or MISSING,
                      "originalFootprint": ", ".join(sorted({p["id"] for p in before})) or MISSING,
                      "currentFootprint": after["id"] if after else MISSING,
                      "proposedFootprint": item.get("proposed_footprint") or MISSING,
                      "proposedPackage": proposal or MISSING, "group": group["ref"] if group else None,
                      "grade": item.get("authenticity"), "implemented": implemented, "electrical": electrical,
                      "mechanical": mechanical, "fabrication": "Awaiting manufacturing approval" if after else MISSING,
                      "physical": MISSING, "nets": fp["nets"], "change": tags, "notes": notes,
                      "history": historical, "sources": sorted(sources), "branches": branch_rows, "risks": risks})
    current_population = [r for r in comps if r["currentRefs"] and r["status"] != "excluded"]
    stats = {"original": population(old[r]["mount"] for r in coverage),
             "current": population(r["currentMount"] for r in current_population),
             "target": population("THT" if target[members[0]]["construction"] in {"THT", "SIP element"} else "SMD"
                                  for members in membership.values()),
             "status": {status: sum(r["status"] == status for r in current_population) for status in STATUS},
             "categories": list(breakdown.values()), "excluded": sum(r["status"] == "excluded" and bool(r["currentRefs"]) for r in comps)}
    if sum(stats["status"].values()) != stats["current"]["total"]:
        raise ValueError("Current package counts do not reconcile with the component manifest")
    planned = {row["ref"] for row in current_population if row["status"] == "planned"}
    if holds.keys() - planned:
        raise ValueError(f"{hold_register}: held references outside the current plan: {sorted(holds.keys() - planned)}")
    if hold_register:
        stats["deferred"] = len(holds)
    return {"components": comps, "stats": stats, "groups": groups, "regions": regions_for(comps, new),
            "verification": report, "warnings": warnings, "provenance": provenance}
