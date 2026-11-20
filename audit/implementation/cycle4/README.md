# Scenario B+ through-hole conversion, cycle 4

20 more motherboard positions are through-hole. The accepted starting engineering commit was `824dd94bc5a3831dc0179351796cb21e939ca677`. Its PCB matched `e59e244e798712bfd0d617a8f9a7dc695bc016b4`. A clean recovery check reconciled the motherboard and dashboard worktrees with GitHub. Native KiCad 10.0.8 reproduced the inherited ERC, refilled DRC and parity baseline before placement work. The final verified artwork is `9f42a84b01259dd6c112fab168786e06c2e8e8ea`. Each accepted batch has a separate pushed checkpoint.

| Verified batch | Converted references | Count |
|---|---|---:|
| [`40db66d`](../cycle4-audio-resistors/README.md) | R207, R210, R230, R242 | 4 |
| [`cf2aa43`](../cycle4-isa-termination/README.md) | C726, C780, C782, C784, C786, C787 | 6 |
| [`faa923d`](../cycle4-expansion-bulk/README.md) | C412, C416, C419 | 3 |
| [`23396e0`](../cycle4-expansion-signals/README.md) | C700, C746, C748, R111 | 4 |
| [`512318f`](../cycle4-zorro-reservoir/README.md) | C418 | 1 |
| [`9f42a84`](../cycle4-audio-filter/README.md) | C232, R231 | 2 |

| Measure | Start | End |
|---|---:|---:|
| Through-hole packages | 137 | 157 |
| Surface-mount packages | 417 | 397 |
| Total physical packages | 554 | 554 |
| Actual through-hole share | 24.7% | 28.3% |
| Completed conversion positions | 72 | 92 |
| Planned positions still SMD | 213 | 193 |
| Deferred within plan | 39 | 52 |

The proposed 62.6% construction share uses the plan's grouped package count. Current population uses the physical BOM. The final CAD comparison matched 3,698 PCB pad-net records, 3,603 schematic assignments, the 304.8 × 330.2 mm outline, all 11 mounting centres, the five fixed Zorro socket padstacks, the four-layer stack, external connector positions and all 1,209 original vias. Each batch has its own refilled raw DRC, ERC, XML netlist and local return-plane comparison. The final DRC has 73 errors and 202 warnings, ERC has 24 errors and 1,182 warnings, and schematic parity has 17 warnings. Opens and new shorts are zero. The raw comparisons document KiCad's changing representative objects for inherited library and bus diagnostics.

## Engineering holds and remaining validation

The 39 existing holds remain in force. The new entries are C400, C408, C415, C417, C701, C750, C762, C764, C766, C768, C9104, D9100, R311. The [deferral register](deferred.csv) records the reason and evidence required for each. D9100 and C9104 remain SMD. R9101 is already axial. The [standby analysis](standby.md) covers both timing directions, leakage and the failed local escape. The [audio part comparison](audio-capacitor.md) replaces the obsolete engineering BOM selection at three already-converted positions.

| Engineering risk | Evidence or release condition |
|---|---|
| Dense ISA termination rows | A six-position trial put C750 against the retained C746 and two RN703 capacitor sites against C760. The short socket leaf and original SMD pads overlapped new copper. Coordinated routing verified the two RN702 positions in the batch table. A search with the four RN703 radials fixed found no local THT or relocated SMD route for C760 within the branch length budget. Keep the remaining row intact pending a different row arrangement. |
| Expansion reservoirs and card geometry | The [four-reservoir comparison](rejected-four-reservoirs.json) left only one In1.Cu spoke at CN602 pads 3 and 4. Check actual card overhang, service access, vent space and loaded rail ripple at every accepted can. Sample the connector and obtain a fabricator-specific drill, registration and annular-ring commitment. |
| ISA reset, bus error and termination | Probe loaded receiver waveforms, overshoot and rail bounce, including the C700 and R111 reference interruptions quantified in the batch comparison. Validate the three coupons with representative expansion loads. |
| Audio and standby | Measure filter response and channel balance, coupling-capacitor bias and leakage, startup transients and cold/hot soft-power timing. Confirm exact Rubycon lifecycle before production. |
| Discrete and DIP candidates | The diode trial and prior package/pin-escape screens leave the existing active devices in place. U9101 shares the unresolved standby thresholds and timing interface. Q301 and U203 require explicit pin escape and verified placement before conversion. |

The next recommended trial is the 4.7 ?F RTC reservoir C811 on CLKVCC. The five-millimetre radial placement screen found explicit supply and ground traces of about 0.05 and 1.55 mm at its shortest site. Establish a standby leakage budget from the backup source, RTC and steering diodes, select the exact capacitor and run a native placement, thermal and backup-current comparison. The 175-package milestone remains open. Fabrication, release files and hardware orders remain on hold.

[Independent cycle comparison](cycle-check.json) · [Current engineering BOM](../../../BOM/SCENARIO_B_PLUS.csv) · [Construction manifest](../../rev62/bplus-components.csv)
