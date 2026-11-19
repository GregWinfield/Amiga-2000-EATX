"""Recreate edge-sensitivity.csv using NumPy and the per-branch placement study."""
import csv
from pathlib import Path

import numpy as np


DIRECTORY = Path(__file__).resolve().parent
DT_NS = 0.025
SAMPLES = 262144
TIME_NS = np.arange(SAMPLES) * DT_NS
OMEGA = 2 * np.pi * np.fft.rfftfreq(SAMPLES, DT_NS)
CORNERS = [
    # Label, 10-90% rise time (ns), driver resistance (ohms),
    # effective load at the slot (pF), line impedance (ohms).
    ("fast/light", 2, 25, 15, 70),
    ("slow/heavy", 8, 50, 80, 70),
    ("fast/heavy", 2, 25, 80, 70),
    ("lower impedance", 2, 25, 15, 55),
    ("higher impedance", 2, 25, 15, 95),
]


def proposed_lengths(row):
    slot_to_cap = float(row["baseline_slot_route_mm"]) + float(row["tap_extension_L1_mm"])
    return slot_to_cap, float(row["new_private_L1_mm"])


def simulate(lengths, lead_nh, rise_ns, source_ohms, load_pf, line_ohms):
    # Use ns, nF and nH throughout. The 1 nF capacitor opens the stub at DC.
    omega = OMEGA[1:]

    def input_impedance(load, length_mm):
        phase_term = 1j * np.tan(omega * length_mm / 160.0)
        return line_ohms * (load + line_ohms * phase_term) / (line_ohms + load * phase_term)

    slot_to_cap, cap_to_resistor = lengths
    far_section = input_impedance(1000, cap_to_resistor)
    series_rc = far_section + 1 / (1j * omega * 1.0) + 1j * omega * lead_nh
    node_admittance = 1 / input_impedance(series_rc, slot_to_cap) + 1j * omega * load_pf / 1000
    trunk_phase = omega * 150.0 / 160.0
    cosine, jsine = np.cos(trunk_phase), 1j * np.sin(trunk_phase)
    denominator = cosine + jsine * line_ohms * node_admittance
    denominator += source_ohms * (jsine / line_ohms + cosine * node_admittance)
    transfer = np.r_[1.0, 1 / denominator]
    full_ramp_ns = rise_ns / 0.8
    up = np.clip((TIME_NS - 50) / full_ramp_ns, 0, 1)
    down = np.clip((TIME_NS - 2050) / full_ramp_ns, 0, 1)
    source_spectrum = np.fft.rfft(5 * (up - down))
    output = np.fft.irfft(source_spectrum * transfer, n=SAMPLES)
    return output[(TIME_NS >= 50) & (TIME_NS < 150)]


def main():
    with (DIRECTORY / "termination-paths.csv").open() as source:
        paths = list(csv.DictReader(source))
    studies = [("CN605", "B SIP"), ("CN605", "C compact"), ("CN702", "B SIP"), ("CN601", "C compact")]
    results = []
    for slot, design in studies:
        branches = [p for p in paths if p["nearest_slot_pad"].startswith(slot) and p["scenario"] == design]
        sample = max(branches, key=lambda row: sum(proposed_lengths(row)))
        lengths = {"A stored": (float(sample["baseline_slot_route_mm"]), float(sample["baseline_private_route_mm"]))}
        for row in paths:
            if row["capacitor"] == sample["capacitor"] and row["scenario"] in ("B SIP", "C compact", "C axial"):
                lengths[row["scenario"]] = proposed_lengths(row)
        for corner, rise, rs, cl, z0 in CORNERS:
            for variant, distances in lengths.items():
                lead_nh = 2 if variant == "A stored" else 10
                waveform = simulate(distances, lead_nh, rise, rs, cl, z0)
                outside = np.flatnonzero(abs(waveform - 5) > 0.25)
                settling = (outside[-1] + 1) * DT_NS if len(outside) else 0
                results.append(dict(
                    slot=slot, ref=sample["capacitor"], signal=sample["signal"], corner=corner, variant=variant,
                    slot_to_cap_mm=round(distances[0], 3), cap_to_resistor_mm=round(distances[1], 3),
                    peak_V=round(float(waveform.max()), 3), settle_5pct_ns=round(settling, 3),
                    crossings_at_2V=int(np.count_nonzero(np.diff(waveform > 2.0))),
                ))
    with (DIRECTORY / "edge-sensitivity.csv").open("w", newline="") as destination:
        writer = csv.DictWriter(destination, fieldnames=results[0], lineterminator="\n")
        writer.writeheader()
        writer.writerows(results)


if __name__ == "__main__":
    main()
