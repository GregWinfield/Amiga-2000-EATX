# Accelerated through-hole conversion cycle

25 physical SMD positions now use through-hole packages in 8 verified board commits. Results compare the accepted 5f8ea56 artwork with 4f8d886. The BOM includes optional design positions, including RX1. The count describes the design, not a populated or tested assembly.

| Metric | Before | After | Change |
|---|---:|---:|---:|
| THT packages | 90 | 115 | +25 |
| SMD packages | 464 | 439 | -25 |
| Physical packages | 554 | 554 | +0 |
| THT percentage | 16.2% | 20.8% | +4.6 pp |
| Completed THT conversions | 25 | 50 | +25 |
| Planned SMD positions remaining | 260 | 235 | -25 |
| Deferred positions | 17 | 34 | +17 |

| Verified board change | Physical references |
|---|---|
| [agnus control](../accelerated-agnus-control/README.md) · [7022dd4](https://github.com/GregWinfield/Amiga-2000-EATX/commit/7022dd4381328b921ffe88ff6a9fb12f3a5aa095) | R301, R101, R1000, R217, R601 |
| [peripheral bias](../accelerated-peripheral-bias/README.md) · [2cfdc40](https://github.com/GregWinfield/Amiga-2000-EATX/commit/2cfdc40326653fea0d0eb77c249ba3db21cea054) | R305, R214, R300, R902, R308 |
| [audio video](../accelerated-audio-video/README.md) · [8ead2ed](https://github.com/GregWinfield/Amiga-2000-EATX/commit/8ead2ede22b1dffe11899915b240001a8d7119af) | R240, R241, R209, R244, R203 |
| [standby clock](../accelerated-standby-clock/README.md) · [3eff23e](https://github.com/GregWinfield/Amiga-2000-EATX/commit/3eff23eee0aaa54b662c0c36752a6ea0cd50b2bd) | RX1, R9101 |
| [paula inputs](../accelerated-paula-inputs/README.md) · [092917a](https://github.com/GregWinfield/Amiga-2000-EATX/commit/092917a8687a28c2f19f1d8202d5a8835675d8ae) | C211, C212 |
| [rail feeds](../accelerated-rail-feeds/README.md) · [cb9422f](https://github.com/GregWinfield/Amiga-2000-EATX/commit/cb9422f845797438f975d9bfe7054ada63c37e9c) | R208, R200, R215 |
| [analogue filters](../accelerated-analogue-filters/README.md) · [6b6d8db](https://github.com/GregWinfield/Amiga-2000-EATX/commit/6b6d8db97651ae5d0f287a1b67b88559d68ce3c9) | C222, C223 |
| [override bias](../accelerated-override-bias/README.md) · [4f8d886](https://github.com/GregWinfield/Amiga-2000-EATX/commit/4f8d88683aea83586f66474429128974cd439b6f) | R115 |

KiCad 10.0.8 copper refill, ERC, DRC with schematic parity, and independent physical and schematic comparisons ran for each accepted group. The final board retains 73 DRC errors and 202 warnings, 24 ERC errors and 1,182 warnings, and 17 schematic-parity warnings. Zero opens or new shorts were introduced. All 3,603 schematic pin assignments and 3,698 PCB pad-net records agree. The 304.8 × 330.2 mm outline, 11 mounting centres, five Zorro sockets, all fixed electrical/mechanical datums, all 1,211 vias, four-layer stack and auxiliary rail copper areas match the starting board. Only 9 superseded track segments were retired. Each batch archives native outputs and item-level differences, including unchanged footprints entering KiCad's bounded library-warning display.

R305/R306 now have a 0.404 mm courtyard gap and a centred maximum-body gap of 0.994 mm. The limiting adjacent courtyard at R305 is D300 at 0.042 mm. Physical lead forming, socket access at R101, can height, polarities, TE connector fit and loaded supply/signal behaviour remain open. Production fabrication remains on hold.

The 34 named deferrals are a subset of the remaining planned positions. R305 and R601 cleared their previous holds. The screened inventory also includes first-pass package-fit candidates. A free body envelope does not establish pin escape, compatible transistor pinout or logic timing. Future candidates with open body space include Q301 and U203. Use the actual lead ordering and native pad-to-net mapping before any footprint change.

[Independent cycle comparison](cycle-check.json) · [Current deferrals](deferred.csv) · [Candidate screen](candidate-screen.csv) · [Installed BOM](../../../BOM/SCENARIO_B_PLUS.csv) · [Component manifest](../../rev62/bplus-components.csv)
