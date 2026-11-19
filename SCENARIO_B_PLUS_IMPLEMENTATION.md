# Scenario B+ development review

Greg selected the Commodore-authentic construction direction at `dee224d91d5750c5a60abf4027df23123f4dec46` and provisionally approved the revised TE geometry on 20 November 2026. This branch contains the initial motherboard implementation and the three checked termination fixtures. Fabrication, electrical acceptance and a merge require subsequent decisions. [Connector engineering resolution](coupon/CONNECTOR_RESOLUTION.md) · [Coupon manufacturing readiness and equipment](coupon/FABRICATION_READINESS.md) · [Historical and population baseline](SCENARIO_B_PLUS_DESIGN.md)

## RTC battery feed

R803 is the 470 Ω resistor between BT800 positive and the D800 pin-one node on the Buster/RTC sheet. The initial section replaces the 1206 package with a DIN0207 horizontal axial, 6.3 × 2.5 mm body, 10.16 mm pitch. Pin 1 is at (274.35, 360.20) mm and pin 2 at (284.51, 360.20) mm. The physical centre is (279.43, 360.20), displaced (+3.40, +0.80) mm from the planning envelope. This placement clears the existing copper and RTC package. One 0.65 mm land / 0.30 mm drill via at (279.63, 359.40) carries the D800-side branch to B.Cu. Both extensions use 0.25 mm copper. U801's *value legend* moved (−3.0, −4.5) mm to clear R803, with the RTC itself at its original location. The schematic instance now specifies the axial footprint.

![RTC axial routing detail and motherboard 3D view](audit/implementation/axial/rtc-review.png)

The KiCad 10.0.8 comparison used a separate copy of the accepted board, rewritten with the same KiCad version and a fresh zone fill. Use KiCad 10 for the development motherboard and its layer-specific socket padstacks. The RTC change preserves 3,631 schematic pin assignments on 858 nets and all 3,726 physical pad-net records, including the grounded shell lands. All eleven mounts, every connector datum, the four outline segments, stackup and every footprint origin except R803 match. KiCad reports zero unrouted items, the same 17 schematic-field parity findings, 24 inherited ERC errors and 1,182 inherited warnings. Fresh fills give 82 thermal findings on both boards. The 199 reported library discrepancies exchanged R803 for C623. C623's pads and source footprint are unchanged by this functional section. The verification file lists the item-level differences and the raw reports support independent comparison. [Comparison and mechanical register](audit/implementation/axial/verification.json) · [Raw control and RTC reports](audit/implementation/axial/kicad-reports.zip)

## Five Zorro sockets and their power feeds

CN601–CN605 now use the local TE 5645235-3 footprint in both the schematic and board. Every one of the 500 leads moved 0.115 mm toward its own fixed card centre. Longitudinal coordinates, pin numbering, bracket pitch and housing origins match the accepted board. All 500 pads have 1.02 mm finished holes, 1.53 mm outer lands and 1.80 mm inner lands. The five existing ZORRO legends moved 1.20 mm clear of the longer TE silk outline. The project retains Jason Beer's mechanical outline, all eleven mounts and the original four-layer stack. [Motherboard KiCad project](2000EATX-KiCAD-R31/2000ATX.kicad_pro) · [Actual connector footprint](2000EATX-KiCAD-R31/Amiga-KiCad/AmigaFootprints.pretty/TE_5645235-3_Zorro.kicad_mod)

![Actual inner copper at CN605 and KiCad 3D view of the development motherboard](audit/implementation/slots/motherboard-review.png)

The 133.60 × 9.35 mm nominal body projection clears the existing front-side component envelopes at all five slots. The tightest projected clearance is 0.8695 mm at C417/CN602 and C419/CN604. CN605 has a nominal 1.675 mm body-to-left-outline margin. Body tolerances, mating-card/bracket alignment, board bow and underside hardware need first-article inspection. [Mechanical clearance register](audit/implementation/slots/body-clearance.csv)

The outer routing uses 0.25 mm signal tracks with local 0.20 mm escapes where the larger lands restrict the channel. Board minimum width and clearance remain 0.20 mm. The total newly routed at 0.20 mm is 2,167.8 mm across the five-slot group. The largest absolute change in total copper length on a signal net is 0.353 mm on `BA19`. Per-net totals include branches. Compare receiver waveforms and timing to R3.1 under real Zorro loading. [Net-by-net length and neckdown inventory](audit/implementation/slots/routed-lengths.csv)

The −5 V, +12 V and −12 V feeds stay on In2.Cu with their original 0.381, 0.700 and 0.381 mm track widths. The traces enter continuous rail pours before the first socket row. The new −5 V and −12 V bands widen toward lower Y and +12 V toward higher Y. A local indentation in the +12 V pour maintains the +5 V via connection at (158.03969, 236.61750) mm between CN602 and CN603. The auxiliary-rail fills use 0.20 mm pad clearance and 0.20 mm minimum copper width. In1 GND and In2 +5 V each have a same-net local fill at every socket with these dimensions, preserving copper between adjacent 1.80 mm capture lands. Relative auxiliary-rail priority remains −5 V, +12 V, −12 V, then +5 V.

Fifteen auxiliary-power pins (8, 10 and 20 per socket) have direct zone connections. Eight ground contacts also have direct zone connections after the larger pads left a single thermal spoke on an external layer. They are CN601.3/.4/.91, CN603.3/.4, CN604.2/.4 and CN605.99. Verify solder fill and rework with the actual thermal load of the populated motherboard. The existing CN605.5 +5 V relief still requires review.

| In2 rail | Minimum drawn pour metal across the five odd rows, revised | Minimum across the five even rows, revised |
|---|---:|---:|
| -5V | 0.678 mm | 2.879 mm |
| +12V | 1.017 mm | 3.013 mm |
| -12V | 1.017 mm | 3.218 mm |

Each section sums the filled In2 copper intersections along Y at one X station. This check excludes explicit tracks, barrel copper and other layers and samples the two pin columns of each slot. It does not establish current rating, temperature rise or the narrowest section between sampled stations. Verify far-slot DC drop, temperature, plane-current distribution, ground bounce and return-path inductance under representative loading. [All 30 sampled sections against R3.1](audit/implementation/slots/rail-sections.csv)

The socket group has zero unrouted items, copper clearance errors and track-width errors. The full motherboard still reports 73 thermal findings, the same 17 schematic-field parity findings as the control and the inherited ERC counts. Every physical pad retains its original net. The item-level report identifies even those thermal and library discrepancies whose total changed because of refill or package replacement. [Verification and mechanical comparison](audit/implementation/slots/verification.json) · [Raw full-board ERC/DRC reports](audit/implementation/slots/kicad-reports.zip)

## Component conversion and verification sequence

| Function | Physical change | Decision or test before release |
|---|---|---|
| RTC battery feed | One populated 1206 location becomes one 470 Ω DIN0207 axial. No change in component count or value. | Verify the fitted body's clearance to the RTC and tray, inspect both solder joints and measure RTC standby voltage and retention using the approved battery configuration. |
| Zorro socket | Five fixed card planes, 500 solder tails. All five revised footprints are placed and rerouted. The comparison quantifies the per-contact changes. | Gauge a genuine TE sample and populated first article, qualify ring and barrel process, inspect negative-rail and +12 V cross-sections and loaded voltage drop. |
| Grounded termination banks | Target 44 independent resistor elements in six SIPs, plus R604 and R605 as individual returns. The three coupons implement the SMD, SIP and axial alternatives. | Retain independent capacitor junctions. Validate matrix, common-ground bounce, crossings and margin before promoting a bank to a qualified assembly. |
| Remaining through-hole groups | 342/546 physical through-hole packages is the design target. The initial implementation stages only the recorded groups. | Use one commit per functional section. Export netlist, compare every pad and fixed datum, refill and review ERC/DRC after each. Preserve timing-critical damping, bypass and power functions until their own geometry and checks support conversion. |

## Electrical and mechanical risk register

| Risk | Consequence | Evidence required / owner |
|---|---|---|
| TE manufacturing limits | Socket insertion damage, split barrel or annular breakout | Fabricator to confirm all coupled process conditions in writing. Assembly engineer to gauge the actual connector and inspect a panel witness. |
| Fixed EATX fit | Five assembled sockets may bind cards or foul bracket/tray despite nominal alignment | Mechanical reviewer to gauge end stations, local bow, card plane, bracket and underside clearance with real hardware. |
| Expansion power and return continuity | Larger inner annuli restrict the auxiliary rails. New escapes can increase discontinuity or narrow return paths. | PCB reviewer to inspect both plane layers and current path. Verify four-wire resistance, droop and temperature at loaded near/far slots and under simultaneous switching. |
| R803 axial body | Solder tails or the body can foul tray hardware or hinder RTC service | Check lead form, body height, underside trim, extraction and standby operation. |
| Zorro termination performance | SIP common impedance changes overshoot, crosstalk and valid strobe window | Bench owner to measure all three variants under matched conditions and then measure actual receiver pins in a loaded machine. Await the separate SDS1104X-U test-plan revision for instrument-specific limits. |
| Inherited ERC and PCB findings | Apparent improvements in counts can mask a new fault | Preserve original report, compare matching KiCad-version refills and classify each local difference. Keep inherited circuitry corrections in separately approved commits. |
| Further historical packages | DIP substitution, radial lead inductance, thermal limits and audio JFET pinouts can affect system timing or analogue response | Check actual data sheets, pad maps, bypass loop and clearance by function. Keep the approved EATX electrical choices and compare measured performance. |

The branch carries layout approval. Authorising coupon manufacture, accepting a completed electrical test, ordering a motherboard prototype, releasing production plots and merging are separate decisions. [Bench worksheet](coupon/MEASUREMENT_PLAN.md) · [Per-reference construction target](audit/rev62/bplus-components.csv)
