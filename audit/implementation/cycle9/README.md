# Cycle 9 physical conversion

The final refilled KiCad motherboard contains 217 through-hole packages. The 220-package target remains 3 short. The bounded pass covered 30 ranked candidates, then checked additional 7 MHz dampers and the U607 supply bypass. The conversions include 10 positions previously classified as retained. The source artwork is `bc28fab5ba558fc3a84b73baacfcd21978d78ab5`. [Candidate queue](candidate-queue.csv) · [Classification changes](classification-changes.csv)

| Metric | Opening | Final | Change |
|---|---:|---:|---:|
| Installed THT | 206 | 217 | +11 |
| Installed SMD | 348 | 337 | -11 |
| Total installed | 554 | 554 | 0 |
| THT share | 37.2% | 39.2% | +2.0 percentage points |
| Completed conversions | 141 | 152 | +11 |
| Planned positions still SMD | 196 | 201 | +5 |
| Active deferrals | 125 | 135 | +10 |

| Verified batch and evidence | Converted positions | Artwork commit |
|---|---|---|
| [cycle9-logic-supplies](../cycle9-logic-supplies/README.md) | C103, C109, C500, C541, C603 | [`8e2f71ff`](https://github.com/GregWinfield/Amiga-2000-EATX/commit/8e2f71ff229e2fa5b11b86319002953aad4f86c6) |
| [cycle9-audio-clock-buffer](../cycle9-audio-clock-buffer/README.md) | C540, C805, R302, RN907A1, RN907C1 | [`86c4389d`](https://github.com/GregWinfield/Amiga-2000-EATX/commit/86c4389de1073096d07b83f1b93c32d912b4771a) |
| [cycle9-u106-bypass](../cycle9-u106-bypass/README.md) | C106 | [`bc28fab5`](https://github.com/GregWinfield/Amiga-2000-EATX/commit/bc28fab5ba558fc3a84b73baacfcd21978d78ab5) |

The supply bypasses use KEMET C315 and C322 X7R ceramics. C500 uses 220 nF and the others use 100 nF. The recorded ±10%, 50 V ordering codes had distributor listings with stock. R302 uses the sourced Vishay MRS16 1 kΩ metal-film resistor. RN907A1 and RN907C1 use the specified non-helical Vishay MBA0204 47 Ω RF family. Exact stock for that RF variant remains open. Batch records give each ordering code, body, lead dimensions, temperature ratings, distributor status and installed footprint.

R310 remains SMD. With a printer grounding parallel-port pin 14, the conservative dissipation bound is 0.617 W. The compact 0.5 W part fits, while the 1 W candidate lacks a verified mounting and copper exit. C501 retained only one effective bottom ground connection. C600's new ground stitch still fed an isolated bottom island. All 125 earlier holds are preserved. New deferrals are C102, C104, C108, C601, C607, C802, R205, R233, R243, RN204D1. Each row records what would justify reopening it. [Priority calculations](priorities.md) · [Deferral register](deferred.csv) · [Trial geometry and native findings](trials.json)

Across the entire cycle, the 3,603 schematic pin assignments and 3,698 physical pad-net assignments match. The board has zero unrouted connections. ERC retains 24 errors and 1,182 warnings, DRC 72 errors and 202 warnings, with 17 parity warnings. The cumulative object comparison records footprint-library witness changes and equivalent ERC witnesses. Every batch includes the underlying native reports. All 11 mounting centres, the five Zorro padstacks, external connector datums, board edge and four-layer construction match. C540's plated supply pad replaces the via at its original centre. The other 1,206 vias survive. [Opening comparison](opening.json) · [Cumulative verification](cycle-check.json)

All accepted supply pads have verified connections into the refilled planes. R302 shortens the coupling trace by 14.482 mm. The 7 MHz trunk retains its centreline. Its two added source branches are 0.306 and 0.892 mm. The routed 7M output shortens by 2.254 mm and V7M lengthens by 1.396 mm. The batch evidence records actual returns, thermals, new lengths, neighbouring courtyards and assembly access.

### Physical validation and Cycle 10

The same five +5 V triangles remain at the Zorro sockets, with matching native areas and vertices. Fabrication remains on hold for CAM acceptance, drill and annular-ring tolerances, connector and card fit, populated lead and body clearance, R232 formed-lead access, C811 RTC leakage and retention, and XU1 reset response. Measure populated audio, rail transients, loaded DRAM, video, Zorro, E7M, XCLK and _C4 edges. Include the changed 7M/V7M branches and check U805/R802 soldering access and C500 ROM clearance. [Native copper comparison](cam-check.json)

For Cycle 10, prioritise R310 if a short-pitch power part or measured hot grounded-port load resolves the rating. C501 and C600 require a different ground landing that reaches connected copper on both faces. R233 and R243 warrant another trial if a limited audio-component relocation opens both terminal routes. Preserve the existing SMD positions until those conditions are met.
