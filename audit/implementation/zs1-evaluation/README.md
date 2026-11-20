# ZS1 auxiliary rail review

**Retain the nine discrete 1 kΩ returns.** The routed trial places a 4610X-101-102LF at (120.700, 224.435) mm on the capacitor side of CN604. All nine private RC paths reach their assigned pins, and pin 1 returns to ground. The final KiCad comparison against fa32310 has the same 275 DRC findings, zero opens and the same 17 parity findings. The 0.30 mm gap, 0.28 mm spokes and 45° spoke angle connect the common to the adjacent ground copper. The isolated board and schematic can be reconstructed by applying the two patches in the archive to fa32310. [Candidate patches, raw reports and lane samples](review.zip)

The ten plated holes cut across three auxiliary rails. Scanning the filled In2 artwork vertically at 0.025 mm increments and sweeping x = 119.20–122.20 mm in 0.05 mm increments gives the following minimum **aggregate copper widths** within each rail band. Separate strips are summed. These values do not measure resistance or establish a current rating.

| In2 rail | Baseline | Trial |
|---|---:|---:|
| −5 V | 3.050 mm | 0.525 mm |
| +12 V | 7.550 mm | 1.400 mm |
| −12 V | 5.825 mm | 1.300 mm |

An earlier y = 225.480 mm layout changed the adjacent rail under three bottom-layer signals. The revised escapes restore their original rails. Thirteen B.Cu nets were compared at 0.02 mm intervals. Five samples on _OWN still lost their immediate −5 V reference at the drill row. The strip already beneath _COPCFG was an inter-rail gap before the change. The electrical hold reflects the narrowed power conductors and return path, independent of the DRC result.

A horizontal 25.35 mm body cannot fit in the 10.232 mm courtyard gap between CN605 and CN604. Moving it north of the socket ends would put its pin row at or above y = 214.883 mm. C626 alone would then need at least 36.025 mm of private route before any lateral jog or obstacles. A longitudinal move farther north continues to cross the rail bands until the complete pin row clears them. Review a quantified rail bypass or a different bank location with loaded-slot current and receiver measurements before revisiting this placement. [Bourns dimensional drawing](https://bourns.com/docs/Product-Datasheets/4600x.pdf)
