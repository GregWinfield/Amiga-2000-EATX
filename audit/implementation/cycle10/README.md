# Cycle 10 engineering checkpoint

The final KiCad artwork has 225 through-hole packages and 329 SMD packages. The eight new positions include the parallel-port power resistor, keyboard and audio filtering, four supply bypasses and the right audio-output shunt. The final artwork is `edccfc4fbe53fcb0d5d7e9be5bf3d8b0e50b467d`. [Opening CAD baseline](opening.json) · [Cumulative object comparison](cycle-check.json)

| Metric | Cycle 9 | Cycle 10 | Change |
|---|---:|---:|---:|
| Installed THT | 217 | 225 | +8 |
| Installed SMD | 337 | 329 | -8 |
| Installed total | 554 | 554 | 0 |
| THT share | 39.2% | 40.6% | +1.4 percentage points |
| Completed conversions | 152 | 160 | +8 |
| Planned positions still SMD | 201 | 202 | +1 |
| Active deferrals | 135 | 137 | +2 |

| Verified batch | Conversions | Artwork |
|---|---|---|
| [cycle10-port-passives](../cycle10-port-passives/README.md) | C261, C306, R310 | [`175d9b9a`](https://github.com/GregWinfield/Amiga-2000-EATX/commit/175d9b9ad1b8b7d6264b4b0577b2a43907e048ed) |
| [cycle10-supply-returns](../cycle10-supply-returns/README.md) | C203, C205, C300, C409 | [`537eb078`](https://github.com/GregWinfield/Amiga-2000-EATX/commit/537eb0786b8328e717337d61f00f51bd89f1a3b1) |
| [cycle10-audio-shunt](../cycle10-audio-shunt/README.md) | R234 | [`edccfc4f`](https://github.com/GregWinfield/Amiga-2000-EATX/commit/edccfc4fbe53fcb0d5d7e9be5bf3d8b0e50b467d) |

The installed population includes 65 original THT packages. Of the remaining SMD packages, 202 are planned, 89 are intentionally retained and 38 have unresolved dispositions. Active deferrals are a subset of the planned positions. CAD-verified conversions still require validation on a populated board. This cycle resolved R234, R310 and added C220, C504, RN204A1, R500-12. All previous reasons are available in the Cycle 9 register and the resolved rows link to the accepted design. [Classification changes](classification-changes.csv) · [Active register](deferred.csv) · [Resolutions](resolved.csv) · [Historical register](../cycle9/deferred.csv)

### Priority outcomes

- **R310.** The sourced 47 Ω ±5%, 1 W Vishay PR01 fits upright on 5.08 mm centres, preserving both 0.4572 mm exits. The conservative grounded-pin bound is 0.617 W. The batch record specifies the derating assumption, lead form and enclosure temperature measurements. The schematic, PCB value field and installed BOM identify the 1 W part.
- **C501.** The relocated 5.00 mm radial and locally oriented ground relief provided three connected front paths, four inner paths and three bottom paths. Supply-pad distance to U501.14 reduced from 4.34 to 4.04 mm. The original EATX shopping item 17 specifies 100 nF ceramic in 1206. It omits voltage, tolerance, dielectric and ordering code. Its previous exact-electrical-equivalence hold therefore remains active, with the ground-layout blocker cleared on this trial.
- **C600.** Moving the ground entry and retaining a dedicated connection to the original ground root produced three front ground paths and four inner paths. Only one bottom path connected to the outer pour. The positive terminal also moved from 16.14 to 19.23 mm from U600.20. The installed part remains SMD.
- **R233 and R243.** An isolated three-component trial shifted C234 by 0.50 mm and fitted both 1 kΩ resistors horizontally on 5.08 mm centres in the rear audio corridor. R233 intersected D401's inner copper and bottom BLUE/composite-sync routes. R243 intersected FLTRIGHT on the bottom. Enlarging the original audio vias also failed the clearance screen. Both holds remain active. The accepted local arrangement uses C306's plated ground for R234. The left audio channel, connector and hybrid positions retain their geometry.

[Ranked queue](candidate-queue.csv) · [Trial placements, omissions, native findings and measured returns](trials.json)

### Electrical, mechanical and sourcing evidence

All 3,603 schematic pin assignments and 3,698 physical pad-net assignments match across the cycle. There are zero opens. ERC retains 24 errors and 1,182 warnings. DRC now has 71 errors and 202 warnings, with 17 parity warnings. The single cleared error is C205's original front-ground thermal. The other differences are explicitly reconciled library or ERC witnesses. Board edges, four-layer stack, 11 mounting centres, five Zorro sockets, external connector datums and all 1,206 discrete vias match. The five Zorro +5 V refill triangles have identical native areas and vertices. [CAM comparison](cam-check.json)

The batch records include individual manufacturer order codes, lead geometry, temperatures, sourcing status, physical clearances, local copper lengths and post-refill reference checks. C306's selected C315C101J5G5TA had zero stock at DigiKey. The same-footprint C315C101F5G5TA is a sourceable alternative with the same 100 pF nominal, 50 V rating, C0G dielectric and 2.54 mm lead spacing, and a tighter ±1% tolerance. The installed BOM identifies the original selection. [Alternate manufacturer drawing](https://search.kemet.com/component-documentation/download/specsheet/C315C101F5G5TA) ? [Alternate distributor listing](https://www.digikey.com/en/products/detail/kemet/C315C101F5G5TA/6562358) The Cycle 9 Vishay MBA0204 RF variant retains its existing sourcing status. The remaining production holds include drill and registration tolerances, annular rings, card and connector fit, R232 lead access, C811 leakage and backup retention, XU1 reset, audio response, rail transients and loaded DRAM, video, Zorro, E7M, XCLK and _C4 waveforms. Also measure temperature under a grounded parallel port and inspect C261/C260 and C306/R234 solder access.

### Cycle 11 candidates

1. C501 has a demonstrated ground layout. Establish the fitted dielectric, voltage and tolerance or an approved original specification, then compare the local rail impedance and transient at U501.14.
2. C504 requires a different ground entry with two connected bottom paths close to U504. C600 needs a receiver-side landing that also shortens its feed.
3. Reopen R233/R243 only with a route around the measured inner and bottom copper conflicts. C220 likewise needs a layout that preserves Vref reference coverage. Preserve the qualified audio ground arrangement during those trials.
