# Cycle 5 motherboard implementation

Verified KiCad artwork is `7994c796b09d900ef0457c6b4a7c6ea9d2400fad`. The Cycle 4 engineering checkpoint was `a5552f5` with artwork `9f42a84`. The documented batches and counts below come from comparing the actual boards, schematic netlists and installed BOM.

| Measure | Cycle 4 | Cycle 5 |
|---|---:|---:|
| THT packages | 157 | 165 |
| SMD packages | 397 | 389 |
| Installed packages | 554 | 554 |
| THT share | 28.3% | 29.8% |
| Completed positions | 92 | 100 |
| Planned SMD positions | 193 | 185 |
| Engineering holds within plan | 52 | 95 |

| Verified artwork | Positions | Evidence |
|---|---|---|
| `141e05e4de` | R202, R206, R213 | [Batch report](../cycle5-audio-bias/README.md) |
| `c9fb54d094` | R914 | [Batch report](../cycle5-keyboard-feed/README.md) |
| `bdf143a118` | C811, R806 | [Batch report](../cycle5-rtc-and-grant/README.md) |
| `8c3a92d877` | XU1 | [Batch report](../cycle5-reset-supervisor/README.md) |
| `7994c796b0` | R232 | [Batch report](../cycle5-filter-resistor/README.md) |

The refill and ERC controls reproduced the inherited 73 DRC errors, 202 DRC warnings, 24 ERC errors, 1,182 ERC warnings and 17 schematic parity warnings. C811's new ground spoke arrangement resolved its inherited thermal error. The final board has 72 DRC errors and 202 warnings. The other totals match the control. The batch comparisons record individual diagnostic descriptions and affected objects. KiCad changed which examples it displayed for inherited library mismatches and which wire anchors it reported for equivalent ERC messages.

The cumulative comparison matched 3,603 schematic pin assignments, 3,698 physical pad-net records, all eleven mounting centres, five Zorro connector padstacks, the connector datums, board outline and four-layer stack. Final unrouted count is zero. Via population went from 1209 to 1208. Check each batch for the local plane and thermal results. [Full reconciliation](cycle-check.json)

### Recovery after the Windows reboot

The live implementation worktree and GitHub both pointed to `bdf143a` when inspected. Three earlier Cycle 5 batches were already committed and their report archives were readable. The installed board had 163 THT and 391 SMD packages. The latest completed batch at that point was C811 and R806. The implementation had one untracked trial-comparison report and no pending CAD edits. The dashboard at `3c17b11` had a pending change to read Cycle 5 classifications. Both changes were preserved.

The saved XU1 trial contained native reports. The R232 trial contained ERC and a netlist but lacked a completed DRC or mechanical comparison. No running KiCad verification process remained. The interrupted process's exit status could not be recovered. Fresh isolated runs reproduced the XU1 result and exposed a dangling branch at the old R232 pad. Replacing that branch preserved the C231 connection. Each recovered batch was then independently verified and pushed.

### Positions retained

All 52 earlier holds remain. The additional 43 comprise the 32 audited SOICs, C311, C704, C705, R500 and seven ISA termination capacitors. Across the register, 16 are category A (mechanical), 68 category B (copper), 10 category C (electrical), 0 category D (procurement), and 1 category E (physical validation). A category records the first release condition. Secondary issues are in the individual notes. A procurement category count of zero still leaves supplier confirmation outstanding for the parts selected for layout. [Deferred positions and reopening conditions](deferred.csv)

The serial shunt trial produced an isolated bottom ground island. The ISA decoupler trials produced a dangling +12 V trace and changes to reference copper under C791/C793. The _EXRAM pull-up trial crossed its supply trace. For seven 1 nF ISA terminations, individually routed outside positions added 11.86–15.61 mm on the socket side. Between-socket searches constrained the added branch to 7 mm and the private RC connection to 25 mm. No placement survived those bounds. Critical processor, Paula, Denise and CIA supply bypasses retain their local SMD connections. [Isolated trial coordinates, diagnostics and copper samples](trial-comparisons.json)

The 32 narrow DIP trials found no placement clearing every land. Two serial devices have exact manufacturer package equivalents. The other 30 original shopping-list entries specify families only. [Device comparisons](dip-review.md) · [Per-position screening](dip-screen.csv)

A follow-up two-layer routing screen checked alternate existing plated contacts without adding vias. Its best isolated C231 placements lengthened the private filter branch from 1.003 to 14.303 mm. At R205 the gate branch grew from 1.902 to 11.974 mm. Neither change was adopted. The same local search found no candidates for C234 or C244. These are bounded placement results. A paired filter redesign with closer copper access and a populated noise and response comparison remains an avenue for later work.

### Validation before manufacture

Confirm the finished-hole and registration tolerances with the chosen fabricator and verify socket retention, card insertion and removal, component lead forming and nearby tool access on samples. Measure RTC battery current and changeover retention, keyboard startup surge and temperature, and bus-grant and reset signals with representative loads. The earlier connector and termination coupon qualifications remain open. [RTC budget](rtc-reservoir.md) · [Connector qualification](../../../coupon/CONNECTOR_RESOLUTION.md)

The next bounded analogue trial should address the left/right filter capacitor branches around C231 and C241 using their actual op-amp terminals. Preserve the existing gain/feedback geometry and probe both channels. The 175-package milestone is 10 verified positions away.
