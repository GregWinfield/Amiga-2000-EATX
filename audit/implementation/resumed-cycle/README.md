# Resumed through-hole conversion cycle

Six verified motherboard batches converted 22 positions. Nineteen are radial capacitors, two are TO-92 transistors and one is an axial resistor. Each artwork commit was pushed and its branch tip checked on GitHub. The cycle began with the accepted register at `d87943f` and artwork at `4f8d886`. [Independent KiCad reconciliation and full commit IDs](cycle-check.json)

| Published artwork | Group | Positions |
|---|---|---:|
| `f89074e` | [Video reservoirs and audio coupling](../resumed-av-capacitors/README.md) | 5 |
| `7341f06` | [Zorro and ISA termination capacitors](../resumed-termination-capacitors/README.md) | 6 |
| `20b9c27` | [Front-panel indicator driver](../resumed-indicator-driver/README.md) | 1 |
| `a19d0fe` | [Seven ISA RN700 branches](../resumed-isa-rn700/README.md) | 7 |
| `43bfbff` | [Keyboard supply and audio filter control](../resumed-keyboard-audio/README.md) | 2 |
| `e59e244` | [ATX soft-power switch](../resumed-atx-driver/README.md) | 1 |

| Physical package or disposition | Before | After |
|---|---:|---:|
| Through-hole | 115 | 137 |
| Surface-mount | 439 | 417 |
| Physical packages | 554 | 554 |
| Through-hole share | 20.8% | 24.7% |
| Completed conversion positions | 50 | 72 |
| Planned SMD positions | 235 | 213 |
| Deferred subset | 34 | 39 |

KiCad 10.0.8 reopened the start and end artworks. Both have the same 3,698 numbered and unnumbered physical pad-net records, 3,603 schematic pin assignments, board outline, copper stack and fixed connector and mounting geometry. All six refilled comparisons ended with zero opens, 73 errors and 202 warnings in DRC, 17 schematic-parity warnings and 24 errors and 1,182 warnings in ERC. The error and warning object differences are recorded per batch, including the representative footprint-library warnings displaced when SMD parts were removed. Two dedicated transistor supply or return vias were retired. No via was added.

Five new holds account for the increase. C619's trial narrowed +12 V copper. C919 lost a required ground spoke on the top or bottom layer depending on placement. C312 missed front-copper clearance at PSTROBE, and C315 and C316 lost required ground thermals. The short routes in the C316 follow-up screen had at most one fully clear spoke direction on one outer layer. Holds remain in the planned population. [Register and reopening conditions](deferred.csv) · [Port-filter trial with object-level differences](port-filter-trial.json)

A local DIP screen used 7.62 mm row spacing, 2.54 mm pin pitch and cardinal orientations in 40.64 mm windows around the candidate devices. No supported 8-, 14-, 16- or 20-pin geometry survived the conservative land and neighbouring-body checks with existing copper fixed. D9100 and R500 also lacked a short placement at the alternative same-net anchors evaluated. The shortest surviving R806 trial required a 24.98 mm branch to the _CBG bus-grant pull-up. These screens justify moving to a grouped placement trial. They do not establish electrical equivalence or impose additional formal holds. The prior ZS1, R800, C224 and R109 decisions remain in force.

The next group is the standalone standby timing cluster, especially D9100, R9101 and C9104, around the verified Q9100. Map the common nodes and establish the reset interval, leakage budget and timing-capacitor return before relocating the group. Supplier acceptance of finished holes and registration, seated-body and card fit, and representative electrical measurements remain release conditions. The selected low-leakage audio capacitor also requires traceable stock or qualification of a current replacement.
