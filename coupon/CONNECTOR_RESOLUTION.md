# TE 5645235-3 socket footprint

**Disposition.** Greg approved this geometry provisionally for Scenario B+ layout on 20 November 2026. The production datum is the centre of the mating card. The review covers the -3 solder-tail socket in Jason Beer's shopping list. Supplier process acceptance and a physical fit test are outstanding. [Shopping list](../BOM/A2000EATX-REV31-ShoppingList.csv) · [TE part record](https://www.te.com/en/product-5645235-3.html)

## Drawing interpretation

TE customer drawing C-5645235 revision C1 gives 50 contacts per row for the -3, 2.54 mm longitudinal pitch, 124.46 mm first-to-last span and 4.85 mm across the solder tails. The body is 133.60 ±0.25 mm long. The symmetric reference footprint uses a 9.35 mm body width. Pins 3–6, 49–52 and 95–98 have formed retention features. These twelve posts are electrical terminals and occupy their own numbered plated holes alongside the other 88 straight tails. All 100 receive the same finished diameter. The formed-post detail dimensions describe the terminal profile. There are zero separate retention drills. Inspect the bag label, drawing revision, pin-one end, retention groups and all fifty stations of a sample before use. [TE customer drawing C1, sheet 1, -3 row](https://www.te.com/commerce/DocumentDelivery/DDEController?Action=srchrtrv&DocFormat=pdf&DocLang=English&DocNm=5645235&DocType=Customer+Drawing&PartCntxt=5645235-3)

TE application specification 114-13018 revision C, §3.6 and figure 2, distinguishes the plated bore from the manufacturing tool. Its through-hole column calls for 1.15 ±0.03 mm before plating, 1.02 ±0.08 mm finished, and 0.026–0.076 mm copper per barrel wall. Nominal outer pad width is 1.02 + 0.51 = 1.53 mm. Specify the finish in the same column and check all three dimensions together. Excellon conveys the 1.02 mm **finished** target. CAM selects and documents the compensated tool. [TE application specification, figure 2](https://www.te.com/commerce/DocumentDelivery/DDEController?Action=srchrtrv&DocFormat=pdf&DocLang=English&DocNm=114-13018&DocType=Specification+Or+Standard&PartCntxt=5645235-3)

## Pad and drill budget

All dimensions are mm. The layout contract assumes maximum diametric copper undersize of 0.040 and maximum combined hole-to-land centre displacement of 0.060 **radial** on each layer. These are procurement conditions. Residual ring = (nominal land width − diametric undersize − maximum hole diameter) / 2 − displacement. Use finished bore on the two external faces and preplate bore on inner capture lands. Roundrect pin one uses its minimum width. These are worst-case bounds within the stated process.

| Variant | Outer / inner land | Hole used outside / inside | Minimum outside | Minimum inside |
|---|---:|---:|---:|---:|
| R3.1, standard +0.13 mm finished tolerance | 1.31 / 1.31 | 0.93 / unknown | 0.110 | Actual production tool required |
| Earlier coupon with precision finish | 1.31 / 1.31 | 1.07 / 1.18 | 0.040 | −0.015 |
| Uniform TE nominal outer land on all layers | 1.53 / 1.53 | 1.07 / 1.18 | 0.150 | 0.095 |
| Approved coupon padstack | 1.53 / 1.80 | 1.07 / 1.18 | **0.150** | **0.230** |

Project residual-ring acceptance is ≥0.125 external and ≥0.150 internal, continuous around the whole barrel. Under the quote conditions the margins are 0.025 and 0.080 respectively. At TE's absolute finished maximum of 1.10 the calculated outer residual falls to 0.135. Production's nominal 0.80 finished diameter is already 0.14 below TE's minimum. The old 1.31/1.02 padstack can break out internally.

With 2.54 mm pitch, the nominal longitudinal clear copper corridor is 1.01 mm outside and 0.74 mm inside. One 0.25 mm track plus two 0.20 mm clearances fits either corridor. Two such tracks with three 0.20 mm clearances require 1.10 mm. Stagger or move the escape, change routing layer after checking the return path, or relocate unrelated vias. Preserve rail cross-section and qualify any new return discontinuity. A compromised annulus is grounds to redesign the escape.

## Fixed EATX geometry

The preceding footprint had 5.08 mm row spacing. Move the odd and even rows 0.115 mm toward their common centre, preserving connector station Y, body centre, card plane and bracket pitch. On the coupons the two X rows are 204.71469 and 209.56469 mm, with station one Y = 56.53290. On the motherboard all five first stations have Y = 221.53290 mm. Preserve the measured CN604–605 pitch of 20.42160 mm alongside the other three 20.32000 mm pitches.

| R3.1 socket | Fixed X centre | Pins flagged for escape review | Pad-to-foreign-track/via interactions under 0.20 mm |
|---|---:|---:|---:|
| CN601 | 188.52129 | 73 | 101 |
| CN602 | 168.20129 | 75 | 78 |
| CN603 | 147.88129 | 74 | 88 |
| CN604 | 127.56129 | 74 | 76 |
| CN605 | 107.13969 | 60 | 125 |

The screen places candidate copper at all 500 new pad centres and measures distance to each foreign segment or via on its layer, accounting for width. It uses the circumscribing radius for the front of pad one, which can overcount near its corners. Counts can include multiple segments at one pin. At CN605.7 the inner capture land overlaps the −5 V trace by 0.045 mm. At CN605.9 it overlaps +12 V by 0.045 mm. These circular-land examples establish a real production routing conflict. The screen excludes pours, foreign footprint lands, mask, courtyard and enclosure, which require separate checks. The coupons have their own reworked escapes. [Per-interaction PCB coordinates and nets](checks/motherboard-slot-escape.csv) · [Accepted motherboard pad map](../audit/baseline/pcb-pads.csv)

## Process requirement for a JLCPCB quotation

Request a four-layer, 1.6 mm nominal, ENIG build with the 100 circular J2 holes flagged for the precision ±0.05 mm finished-hole process (0.97–1.07). The public standard PTH tolerance of +0.13/−0.08 permits 1.15 mm. JLCPCB lists precision capability for selected ENIG multilayer holes and requires identification in the fabrication remarks. Its advertised average hole copper of 18 µm and hole-position tolerance alone do not establish TE barrel minimum or relative registration. A ±0.075 mm limit on each Cartesian axis would permit 0.106 mm radial displacement. [JLCPCB rigid board capabilities](https://jlcpcb.com/capabilities/pcb-capabilities)

Require written CAM concurrence on finished-hole range, TE tool and barrel limits, ENIG finish to figure 2, ≤0.040 mm land undersize, ≤0.060 mm radial combined registration, drawing hole pattern, **all 100 capture lands on both inner layers**, and the residual rings above. Obtain proposed stack, mask/annular rules, actual board thickness over the mounting area, local flatness, tool table, registration target data and representative lot microsections. Have the supplier identify any feature it cannot guarantee. If these conditions exceed its process, qualify another process or revise the stack/lands and reroute before fabrication approval. An accepted quote, inspection evidence and physical sample are still open. [Fabrication readiness and first article](FABRICATION_READINESS.md)
