# Expansion supply reservoirs

C416 and C419 retain 220 µF from +5 V to ground. Panasonic EEU-FR1C221 is a 16 V, ±20%, 105 °C aluminium electrolytic, 6.3 × 11.2 mm with 2.5 mm pitch. The published 100 kHz limits are 455 mA ripple and 0.130 Ω impedance. C412 retains 47 µF between ground on pin 1 and −5 V on pin 2. EEU-FR1E470 is rated 25 V, ±20%, 280 mA and 0.300 Ω at 100 kHz, with a 5 × 11 mm body and 2 mm pitch. Both parts have a 5,000 hour rated endurance and a two-minute leakage limit of 0.01CV or 3 µA, whichever is larger. [Panasonic FR series tables and drawings](https://industrial.panasonic.com/cdbs/www-data/pdf/RDF0000/ast-ind-152839.pdf)

All original supply straps, vias and nearby route references remain intact. Both leads of each capacitor have explicit 0.70 mm front copper. The auxiliary rail areas and all inner plane contour counts match the control. The original local high-frequency bypasses remain in place. As a sensitivity, 20 nH of added inductance contributes 0.013 Ω at 100 kHz. Measure loaded-slot ripple and rail steps because Jason's BOM does not identify the original cans' impedance.

Allow 13.2 mm above the board for the larger can with length tolerance and 0.5 mm seating allowance. The nominal 15.5 mm Zorro connector height gives a 2.3 mm difference. The closest courtyard gap is 1.182 mm from C419 to CN604. Check card insertion, component overhang, vent space and actual connector height using a populated assembly. [TE housing dimensions](https://www.te.com/en/product-5645235-3.html)

DRC objects match the control. KiCad selected alternate anchors for some pre-existing schematic bus and net-name diagnostics. Their electrical messages and multiplicities match. Comparing the schematics with only footprint fields elided gives identical files. Both electrical pin maps match. [Pin assignments](conversion.csv) · [Route lengths](routing.csv) · [Verification](verification.json) · [Native reports](kicad-reports.zip)

