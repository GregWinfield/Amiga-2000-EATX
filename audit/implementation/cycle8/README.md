# Cycle 8 motherboard conversion

Three published artwork batches converted ten positions and brought the board to **206 through-hole packages**. Every installed footprint in the assembly BOM was counted directly in both the Cycle 7 and Cycle 8 boards. The final artwork is `ce6eb1bf04c4958ade17b9757210480bca72c8a9`. [Opening evidence](opening.json) · [Final cumulative comparison](cycle-check.json)

| Metric | Starting | Final | Change |
|---|---:|---:|---:|
| Installed THT | 196 | 206 | +10 |
| Installed SMD | 358 | 348 | −10 |
| Total installed | 554 | 554 | 0 |
| THT share | 35.4% | 37.2% | +1.8 percentage points |
| Completed conversions | 131 | 141 | +10 |
| Planned positions still SMD | 193 | 196 | +3 |
| Active deferrals within the plan | 114 | 125 | +11 |

| Published batch | Converted positions | THT after batch |
|---|---|---:|
| [Zorro E7M damping and interface supplies](../cycle8-interface-supplies/README.md) · [d3948fb](https://github.com/GregWinfield/Amiga-2000-EATX/commit/d3948fb823c27d4726baa38c30fa6d89097b32b8) | RN907B1, C901, C206, C605 | 200 |
| [Audio coupling and peripheral bus bypass](../cycle8-audio-bus-bypass/README.md) · [7f3343a](https://github.com/GregWinfield/Amiga-2000-EATX/commit/7f3343a7f2fa5293fb9fc29bb7a398af6d57bff3) | C318, C502, C602, C604 | 204 |
| [XCLK and Buster/video clock damping](../cycle8-clock-series/README.md) · [ce6eb1b](https://github.com/GregWinfield/Amiga-2000-EATX/commit/ce6eb1bf04c4958ade17b9757210480bca72c8a9) | R212, R905 | 206 |

### Accounting and trials

65 original THT plus 141 converted THT account for 206. The 348 SMD consist of 196 planned, 114 intentionally retained and 38 with unresolved disposition. Of the 196 planned, 125 have active deferrals and 71 have no register hold. Hardware qualification is a separate attribute. All ten new conversions have passed CAD checks and await assembled-board qualification.

C318 was already planned. The other nine successful conversions came from previously retained SMD. C105, C501, C600 and R500-13 moved from retained into the plan with a hold. New holds also apply to seven positions already planned: C225, Q202, Q300, Q301, R310, C9103 and C9105. All 114 preceding entries and their original evidence are preserved. The four priority-component investigations confirmed their existing holds. [Line-by-line classification changes](classification-changes.csv) · [Active register and reopening conditions](deferred.csv) · [Priority components](priority.md)

The bounded placement screens cover 133 distinct references across 195 combinations of reference and search method. Each result gives the number of candidate geometries and, where available, its leading layout. The separate native trial records identify placements that reached refill, the introduced findings and the reference-copper changes. A grid result alone does not qualify an installed package. This distinction matters particularly for R310, where seven 7.62 mm layouts cleared the screen. A matching 47 Ω short-pitch MBB0207IC4709FCT00 is listed as non-stocked with a discontinuation notice, and the normal 10.16 mm horizontal outline produced no qualifying local layout. [Search and refill results](trial-comparisons.json) · [Vishay family specifications](https://www.vishay.com/docs/28766/mbxsma.pdf) · [Short-pitch part listing](https://au.mouser.com/en/ProductDetail/Vishay-BC-Components/MBB0207IC4709FCT00)

### Electrical and mechanical verification

KiCad 10.0.8 reported 24 ERC errors and 1,182 warnings, 72 refilled DRC errors and 202 warnings, 17 schematic-parity warnings and zero unrouted connections. Each batch archives its native reports, XML nets and object-level differences. Cumulatively the ERC comparison paired seven changed diagnostic witnesses by rule, severity and message. Seven DRC library-footprint warning witnesses changed on each side. Parity and unconnected-item differences were empty. No new short, dangling conductor or loss of pin-to-net connectivity was accepted.

All 3,603 schematic pin assignments and 3,698 physical pad assignments match. All 1,207 vias, the board outline and stack, 11 mounting centres, five Zorro socket positions and padstacks, and fixed connector datums were preserved. Each accepted batch records its own route changes, local reference sections, plane contacts, mechanical envelopes and nearest courtyard distances. C502/C602/C604 each have two connected ground spokes on each outer face and four on the inner ground plane. [Cumulative electrical and mechanical data](cycle-check.json) · [Milestone thermal measurements](milestone-ground-spokes.json)

### Manufacturing qualification and Cycle 9

The protected +5 V socket pours retain five rounding slivers. Both internal plot precisions reproduce them. Removing them with local keepouts cut measurable socket-row copper. Fabricator CAM inspection and sign-off remain required at all five sockets. [Precise geometry, test correction and CAM acceptance criteria](cam.md)

Fabrication approval remains withheld. Carry forward drill tolerance, annular ring and registration, external connector fit and Zorro card insertion, R232 and R500 formed-lead fit and rework, C675/R606 clearance, C811 RTC leakage and retention, XU1 reset behaviour, audio response, supply transients and loaded DRAM/video/Zorro measurements. Cycle 8 adds C318 lead forming from 2.00 to 5.00 mm, can height and port clearance, C901/C223 solder access, seating beside U502/U602/U604, and XCLK, _C4 and E7M edge measurements. Confirm audio leakage and polarity, +VID noise and local supply bounce under representative loads. No production artwork release is authorised.

For Cycle 9, first qualify a compact 47 Ω power resistor at R310 with verified mounting and hot-load characteristics. Revisit C501 and C600 from a different IC-side return with demonstrably connected bottom copper. For Q202/Q300/Q301, try a spread-lead pinout after establishing all three terminals, signal clearances and body access. C225 needs a supply/ground pair clear of the mouse tracks. D401 and the standby timing capacitors need fitted-device or bench evidence before another footprint trial.
