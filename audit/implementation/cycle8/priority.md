# Priority component decisions

All four positions retain their installed SMD packages. Their original Cycle 7 rows and trials remain in the register. The shopping list specifies ceramic type, package and nominal value for the capacitors. It omits manufacturer code, tolerance, voltage rating and dielectric class. The KEMET candidates below are design comparisons. Exact fitted-specification equivalence remains open. [Native trial findings and layout searches](trial-comparisons.json)

| Position | New approach | Measured outcome and requirement to reopen |
|---|---|---|
| C401, 10 nF +5 V distribution bypass | Used the existing plated +5 V point R308.1 and a 0.7 mm feed. Rotated the radial package to a separate ground landing at (241.39359, 172.296774) mm. Evaluated C315C103K5R5TA, 10 nF, 50 V, ±10%, X7R. | Copper sections on the ground pad gave two front spokes, four on In1.Cu and one on the bottom. Find a different ground entry with two effective outer spokes per face. |
| C407, 10 nF +12 V bypass | Searched at D400.2, U304.14 and the existing +12 V via at (328.46109, 95.43610) mm. Tested 2.54 and 5.08 mm pitches, including C322C103K5R5TA, 10 nF, 50 V, ±10%, X7R. | Neither pitch returned a complete land, body, feed and signal-reference arrangement. At the original positive and ground centres, the bottom PPD7 and PPD6 track edges are only 0.900 and 0.809 mm away, respectively. F3.2 is approximately 27.3 mm away and already has C322 at its feed. Seek a local pair of taps outside the parallel-port channel. Spokes and solder access require a viable placement first. |
| C915, 100 nF TBASE shunt | Preserved pin 1 TBASE and pin 2 GND. Checked receiver-side taps at CN207.14, J300.2 and U300.19. Refilled a different orientation with a 3.610 mm bottom ground connection to the original via. Candidate C315C104K5R5TA is 50 V, ±10%, X7R. | The ground trace crosses the existing _XCLKEN trace. Copper sampling found one effective thermal sector on each outer face and four on In1.Cu. A suitable placement must clear _XCLKEN and join connected ground copper with at least two manufactured spokes per intended outer thermal. Verify loaded TBASE behaviour. |
| D401, negative accessory-rail rectifier | Schematic and artwork specify Diodes S1MWF-7. The shopping list specifies RS1MWF-7DICT-ND. Pin 1 is cathode to −12 V. Pin 2 is anode toward EMI334.2 and connector CN305.35. Evaluated Vishay UF4007-E3/73 for the previously screened DO-41 position. | Electrical equivalence remains unresolved. Read the fitted marking, establish port load and reverse-event waveform, and qualify forward drop and junction temperature. The preliminary 7.62 mm placement would need a fresh all-layer refill, formed-body and connector access checks after part selection. |

### D401 device comparison

| Datasheet characteristic | S1MWF | RS1MWF | UF4007 |
|---|---:|---:|---:|
| Repetitive peak reverse voltage | 1,000 V | 1,000 V | 1,000 V |
| Average rectified current in specified fixture | 1 A | 1 A | 1 A |
| Non-repetitive 8.3 ms surge | 30 A | 30 A | 30 A |
| Maximum forward drop at 1 A | 1.1 V | 1.3 V | 1.7 V |
| Maximum reverse recovery | 3 µs | 500 ns | 75 ns |
| Typical capacitance, 4 V and 1 MHz | 7 pF | 8 pF | 17 pF |
| Typical junction-to-ambient thermal resistance in datasheet fixture | 56 °C/W | 65 °C/W | 60 °C/W |

The two Diodes parts specify 1 A at terminal temperatures of 100 °C and 88 °C respectively, and a 150 °C maximum junction temperature. Vishay's 1 A rating uses 9.5 mm lead length at an ambient temperature of 55 °C. The axial device's lower recovery time comes with different forward drop, capacitance and thermal mounting conditions. Confirm these against the fitted circuit. [Diodes S1MWF](https://www.diodes.com/datasheet/download/S1MWF.pdf) · [Diodes RS1MWF](https://www.diodes.com/datasheet/download/RS1MWF.pdf) · [Vishay UF4007](https://www.vishay.com/docs/88755/uf4001.pdf)
