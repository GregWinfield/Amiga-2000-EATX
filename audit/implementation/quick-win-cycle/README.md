# Quick-win through-hole conversion cycle

Thirteen original 1206 resistors now occupy thirteen axial positions. Three use Vishay MRS25 DIN0207, ten use the shorter MRS16 DIN0204. All five installed Zorro SIPs and their 35 original termination elements were preserved. Each batch was checked against its immediate predecessor. [Installed motherboard BOM](../../../BOM/SCENARIO_B_PLUS.csv) · [Component dispositions](../../rev62/bplus-components.csv)

| Physical metric | At cfa3c41 | Final | Change |
|---|---:|---:|---:|
| Through-hole packages | 77 | 90 | +13 |
| SMD packages | 477 | 464 | −13 |
| All physical packages | 554 | 554 | 0 |
| Actual through-hole share | 13.9% | 16.2% | +2.3 percentage points |
| Completed conversions, current physical packages | 12 | 25 | +13 |
| Planned conversion positions still fitted as SMD | 273 | 260 | −13 |
| Explicitly deferred original positions in this cycle register | 10 | 17 | +7 |

The 17 named holds are a subset of the 260 planned positions. The Explorer separately reports 165 intentionally retained SMD and 39 unresolved packages. The Scenario B+ target remains 62.6%. Many-to-one SIPs count once in physical totals.

| Verified engineering batch | References | Board commit |
|---|---|---|
| [Floppy motor and reset](../quick-floppy-control/README.md) | R309, R602 | [fe26dc8](https://github.com/GregWinfield/Amiga-2000-EATX/commit/fe26dc8b2c3adca2a36639215f6b56e5c3e37ad3) |
| [Control inputs and expansion reset](../quick-control-pullups/README.md) | R104, R211, R216, R600, R603, R916 | [0bf288c](https://github.com/GregWinfield/Amiga-2000-EATX/commit/0bf288c0ec3793affafd786d3f2f244ff6d40927) |
| [Interface bias, comparator reset and mux select](../quick-interface-bias/README.md) | R306, R805, R900 | [dcd1418](https://github.com/GregWinfield/Amiga-2000-EATX/commit/dcd141847216d17ecb3d0886b4f91c9017f18d6a) |
| [Processor and Buster arbitration](../quick-arbitration-bias/README.md) | R114, R807 | [c743078](https://github.com/GregWinfield/Amiga-2000-EATX/commit/c7430783e094187a7635601305cc3c0b3ee3f4e3) |

## Selection and deferrals

The initial screen tested space for horizontal axial bodies, plated lands on both outer layers, board edges and local front-copper escapes. The first two-part pilot established the schematic, copper and evidence workflow. Later groups reused it with the approved compact axial construction where the larger body or longer tap was disadvantageous. A geometrically clear landing became GREEN only after routing, zone refill and full-board comparison.

- **GREEN, implemented.** The thirteen positions above retain their original pins and values. Three batches added short surface connections. R114 and R807 use direct In2 supply connections in the fourth batch.
- **AMBER, review individually.** R601 and R312 would lengthen taps on DOE and _INT2. D300 and R305 need a joint placement review around Q300 and R602. C813 and C814 require a defined leakage and reset timing envelope. The 1 Ω supply-feed positions R200 and R215 also merit a separate current and trace-width review before selection.
- **RED, hold.** ZS1, C224 and the rejected R800 position have specific power, impedance or geometry blockers. ZS1 remains nine discrete returns. Individual axial replacements remain a future isolated trial only.
- **GREY, retained SMD.** Driver-side damping at R105/R106 and the series elements at R212/R904/R905 retain their short connections. The active termination capacitors also retain their accepted placement in this cycle.

The [deferred register](deferred.csv) enumerates each held physical position and the evidence needed to reopen it. Other amber candidates remain in the general plan.

## Verification and manufacturing limits

KiCad 10.0.8 retains 24 ERC errors and 1,182 warnings, 73 DRC errors and 202 warnings, and 17 schematic-parity warnings. Each batch has zero opens and zero newly introduced layout-rule violations. Raw lists, including moved ERC representatives and library warnings entering or leaving the bounded display, are archived beside each board report. The 3,603 schematic pin assignments and 3,698 physical pad-net records match. [Whole-cycle independent comparison](cycle-check.json). The 304.8 × 330.2 mm outline, four-layer stack, all 11 mounting locations, all five socket centres and the complete set of 54 fixed datums match. Every original track segment and all 1,211 vias survived this cycle.

Zone refill and local centreline comparisons were run for each batch. Excluding R800 restored the auxiliary rail area and the original number of +5 V contours. The additional signal branches had GND beneath all sampled front-copper centres outside the 1.3 mm barrel neighbourhood. Some new +5 V branches pass over pre-existing plane clearances, including 1.598 mm outside that neighbourhood in the first batch. [Lengths with and without immediate In1 ground](front-reference.csv). These remain subject to bench validation. R306 has a nominal 0.080 mm courtyard gap to R305. Fit the SMD part before the axial and check rework access. R916 must leave J900 accessible. Check the reset ramp, motor switching, Q300 input, mux selection and loaded arbitration/reset signalling. Physical TE connector fit, fabricator-specific plating/registration/finished-hole guarantees, card insertion and loaded electrical qualification remain open. Fabrication is on hold.

## Next batch

Review the 4.7 kΩ Agnus configuration pull-ups R101 and R109 together. Their jumper functions are straightforward and avoid changing the clock circuitry. R109 is mounted on the underside. Use the existing jumper connection as the placement anchor and compare both board faces before committing a front-mounted pair. [Agnus component plan](../../component-plan.csv)
