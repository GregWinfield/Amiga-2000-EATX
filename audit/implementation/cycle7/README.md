# Cycle 7 motherboard implementation

Five independently refilled and verified batches converted 14 positions. The motherboard has **196 installed through-hole packages**, 4 short of the 200-package milestone. Further screened placements require changes to their signal references, power feeds, thermal reliefs or component qualification.

| Metric | Starting | Final | Change |
|---|---:|---:|---:|
| Installed THT packages | 182 | 196 | +14 |
| Installed SMD packages | 372 | 358 | -14 |
| Installed packages | 554 | 554 | 0 |
| THT share | 32.9% | 35.4% | +2.5 percentage points |
| Completed conversions | 117 | 131 | +14 |
| Planned positions still SMD | 184 | 193 | +9 |
| Deferred positions within plan | 100 | 114 | +14 |

Four converted positions came from the opening plan. Ten came from reassessing retained SMD. Thirteen retained positions entered the conditional plan as new deferrals, and C201 was already planned. The 100 prior register entries carry forward verbatim. [Installed BOM](../../../BOM/SCENARIO_B_PLUS.csv) · [Construction manifest](../../rev62/bplus-components.csv) · [Complete hold register](deferred.csv)

| Artwork commit | Function | Installed positions |
|---|---|---|
| [2ec535d](https://github.com/GregWinfield/Amiga-2000-EATX/commit/2ec535d0646bc2c908e51e1788c58fc758633767) | [68000 handshakes and DRAM addressing](../cycle7-processor-address/README.md) | R105, R106, R500-3 |
| [1607fd2](https://github.com/GregWinfield/Amiga-2000-EATX/commit/1607fd2d9332e7e1bf5fab27ff892ae6e6202ff1) | [CPU and game-port supply, peripheral reset](../cycle7-cpu-port-reset/README.md) | C100, C218, C916 |
| [77b4f62](https://github.com/GregWinfield/Amiga-2000-EATX/commit/77b4f6256d1aabe01e0441c5887a7b9c37ae9c95) | [DRAM addressing, mouse, audio, RTC and −5 V](../cycle7-memory-mouse-filters/README.md) | C244, C413, C812, R500-10, RN204B1 |
| [f3ad936](https://github.com/GregWinfield/Amiga-2000-EATX/commit/f3ad936ed08df2c51a64f25bb1a8a2d3328dc0b6) | [Audio rail and peripheral address logic](../cycle7-audio-logic-supply/README.md) | C200, C302 |
| [45aaed0](https://github.com/GregWinfield/Amiga-2000-EATX/commit/45aaed01bb321b46009c996124a4218e386e168b) | [8520 CIA bypass](../cycle7-cia-bypass/README.md) | C301 |

## Electrical and mechanical qualification

R500-3 uses a direct U540.14 exit and the original DRAB2 load tap. It retains 47 Ω and shortens the driver and load copper by 1.345 and 1.787 mm. The closest centred maximum-body gap to R500-2 is 0.653 mm. C260 remains the original 100 pF SMD keyboard-clock shunt. The original ordering codes for the capacitor and FB302 remain unknown. The C0G radial candidate clears the layout screen, but its estimated resonance and edge-band impedance depend strongly on the formed leads. [R500-3 engineering](../cycle7-processor-address/README.md) · [C260 impedance and supply evidence](keyboard.md)

The twelve Cycle 6 video and DRAM series resistors preserve the original nominal 47 Ω. Original tolerance and manufacturer are unspecified. The selected parts are ±1% non-helically trimmed RF film. All 24 routed ends shortened, with no new dangling copper. Centred maximum-body clearance is 0.652 mm at R500-6 / R500-5 using a representative maximum 1206, and 2.383 mm at C675 / R606. Ordinary manual assembly appears feasible with underside access and controlled lead forming. Check the purchased bodies, lead dressing and socket access on a sample. [Twelve individual route comparisons](cycle6-damping.csv) · [Physical envelope and signal review](cycle6-review.md)

Native KiCad 10.0.8 reports 24 ERC errors and 1,182 warnings, 72 DRC errors and 202 warnings, 17 schematic-parity warnings and zero unrouted connections. The expanded comparisons identify sampled library-footprint warnings and electrically equivalent ERC message witnesses separately. Across the cycle, ten library-mismatch witnesses entered the report and ten left. Five ERC witnesses changed on each side with matching diagnostic type, severity and description. The other findings retain their identities. The archived reports list each witness. All 3,603 schematic pin and 3,698 physical pad assignments agree. The outline, four-layer stack, all 11 mounting centres, external connectors and five Zorro socket positions and padstacks agree. Of 1,208 opening vias, C302 pin 2 replaces one supply via at the original centre. All 1,207 others remain. [Cumulative object and diagnostic comparison](cycle-check.json) · [Opening audit](opening.json)

## Additional holds and Cycle 8

- C201, C401, C800, C906 and C915 need different ground entries. The C800 trial starved existing U800 socket thermals. C915 failed on opposite outer layers at two distinct taps.
- C101, C407, C606, C803 and C900 need drill sites clear of existing bus, reset, parallel or analog-supply references. C110 needs a topology that preserves the shared positive trunk and improves its already short bypass loop.
- D401 needs the S1MWF-7 versus RS1MWF-7 documentation conflict resolved before a 7.62 mm axial placement can advance. R500-5 needs a new driver exit and a formed-body clearance check. C260 needs impedance and clock-edge evidence. [Native trial findings and coordinates](trial-comparisons.json) · [Reopening conditions by reference](deferred.csv)

Prioritise a new ground entry at C401's broad supply trunk, a parallel-port-side +12 V tap at C407 clear of PPD7 and a receiver-side C915 placement with two outer thermal spokes on both sides. Resolve D401's fitted part and duty before selecting the replacement. A coordinated R500-5 row trial follows measurement of the populated R500-6 neighbour. The original DIP-logic, C231/C241, serial and ISA holds remain active.

## Manufacturing release

Fabrication approval remains withheld. Confirm drill and annular-ring tolerances and copper registration with the fabricator. Include the sub-nanometre-wide positive-plane refill artifact in CAM inspection. Check the C100 socket, C244 connector overhang, C812 and R232 access, axial bends, Zorro card insertion and underside soldering on an assembled sample. Measure C811/C812 RTC leakage and retention, XU1 and peripheral reset, audio response and supply noise, loaded CPU and CIA rails, mouse thresholds, DRAM, video and Zorro timing. Review the U302 supply-pin transient after its plated bypass substitution. The published checks cover CAD and selected part specifications. Populated measurements remain open.
