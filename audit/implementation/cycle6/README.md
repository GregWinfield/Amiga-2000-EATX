# Cycle 6 motherboard implementation

The refilled motherboard at `65f3b2f` has **182 through-hole packages**. Four independently verified and pushed batches converted 17 positions. The second batch crossed the 175-package milestone.

| Metric | Starting | Final | Change |
|---|---:|---:|---:|
| Installed THT packages | 165 | 182 | +17 |
| Installed SMD packages | 389 | 372 | −17 |
| Installed packages | 554 | 554 | 0 |
| THT share | 29.8% | 32.9% | +3.1 percentage points |
| Completed conversions | 100 | 117 | +17 |
| Planned positions still SMD | 185 | 184 | −1 |
| Deferred positions within plan | 95 | 100 | +5 |

C815 was in the starting conversion plan. Sixteen conversions came from reassessing retained positions. The installed BOM and construction manifest identify each exact part. Five new holds are a subset of the 184 planned SMD positions. All 95 prior register entries were carried forward verbatim.

| Artwork | Functional group | Converted positions |
|---|---|---|
| `437e65f` | [Video-slot series damping](../cycle6-video-series/README.md) | RN201A1, RN201B1, RN201C1, RN201D1, RN203E1 |
| `170bea5` | [DRAM address damping](../cycle6-dram-address/README.md) | R500-1, R500-2, R500-4, R500-6, R500-7, R500-8, R500-9 |
| `18cbdda` | [Mouse and Zorro interfaces](../cycle6-peripheral-interfaces/README.md) | RN204C1, R904, R606 |
| `65f3b2f` | [Comparator and Zorro capacitors](../cycle6-radial-shunts/README.md) | C815, C675 |

The video and memory substitutions use non-helical RF resistors mounted horizontally. All 24 affected video and address route ends became shorter. C675 keeps its dedicated slot-side RC branch. C815 moved to the comparator divider after a placement near the original pads failed its ground-spoke and D15-reference checks.

## Electrical and mechanical verification

The opening control reproduced the Cycle 5 board hash and mechanical extract at artwork `7994c79`, engineering checkpoint `8a8b814`, and Explorer revision `abd81dc`. Each batch contains both native DRC and ERC reports, the schematic XML netlists, local plane samples, routed lengths, CAD dimensions and the board hash. The cumulative comparison reconciles the four Git objects, the installed BOM and the final CAD. [Opening control](baseline.json) · [Cumulative verification](cycle-check.json)

| KiCad 10.0.8 check | Starting | Final |
|---|---:|---:|
| ERC errors / warnings | 24 / 1,182 | 24 / 1,182 |
| Refilled DRC errors / warnings | 72 / 202 | 72 / 202 |
| Schematic parity warnings | 17 | 17 |
| Unrouted connections | 0 | 0 |
| Schematic pin assignments | 3,603 | 3,603 |
| Physical pad-net records | 3,698 | 3,698 |
| Vias | 1,208 | 1,208 |

The pin and pad net assignments match individually. Cumulative object differences are limited to representative inherited library mismatches and alternate wire anchors for equivalent ERC findings. The four-layer stack, EATX outline, all eleven mounting centres, connector datums and five Zorro socket padstacks match the starting board. The tighter DRAM row has a minimum 0.0666 mm courtyard gap. The C675–R606 gap is 0.1208 mm. New outer ground contours in the capacitor batch have individually identified plated ground contacts.

## New deferrals and next candidates

| Position | Result of the bounded reassessment |
|---|---|
| C310 | The local shunt and short receiver/connector taps had no radial site passing the body, land and nearby copper screen. |
| C313 | The routed serial shunt changed the reference below PSTROBE and _IORST. Its signal lead also crossed 0.800 mm outside adjacent ground beyond the terminal neighbourhood. |
| C314 | The local candidate lengthened its signal lead by 2.346 mm and ground lead by 4.939 mm. The screened short alternatives failed copper clearance. |
| C702 | The −5 V slot bypass had no qualifying local two-hole placement. The closest ground via has 0.990 mm to an adjacent copper edge. |
| C703 | The −12 V slot bypass had no qualifying local two-hole placement. Copper on the underside comes within 0.858 mm of the nearby ground via centre. |

The final peripheral screen found a short candidate at **C260** on the connector side of the keyboard-clock ferrite. Its signal lead would shorten by 0.067 mm and its return trace would grow by 1.015 mm. Before a native trial, compare the original and candidate 100 pF impedances across the ferrite's operating band and check the assembled port response. **R500-3** is the next memory-row candidate if a different pin escape preserves the DRAB2 driver's approach and the clearance to R500-2 and R500-6. Keep the remaining strobes and clock damping positions in their present layout. [Trial coordinates and diagnostics](trial-comparisons.json) · [Register and reopening conditions](deferred.csv)

## Physical qualification

Fabrication release remains on hold. Obtain fabricator-specific drill, annular-ring and registration limits. Check connector fit, card insertion and extraction, card overhang, formed leads and rework access with populated hardware. Measure the DRAM and video receiver margins, loaded Zorro grant and DOE waveforms, comparator reference and reset transients, and slot rails. Retain the Cycle 5 requirements for R232 lead forming, C811 RTC leakage and retention, XU1 reset behaviour, populated audio noise and filter response, and the remaining connector and power qualifications. [Inherited qualifications](../cycle5/README.md) · [Current checkpoint](../CURRENT_CHECKPOINT.md)
