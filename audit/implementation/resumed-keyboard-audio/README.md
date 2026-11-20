# Keyboard supply and audio filter control

C912 retains 470 µF downstream of FB301 and the 1 Ω R914 keyboard supply feed. The Panasonic EEU-FR1C471 is a 16 V, ±20%, 105 °C radial part. Pin 1 connects to C259 and pin 2 to ground. The 0.70 mm supply and return additions measure 3.02 and 1.43 mm. The local 100 pF C259 and the original ferrite remain. The nominal RC time constant is 470 µs. The closest adjacent courtyard is 1.35 mm away. Allow 14 mm seated height plus vent clearance. Check keyboard load-step droop, inrush and actual enclosure clearance on hardware. [Part dimensions, impedance and ripple assessment](../resumed-av-capacitors/README.md)

R204 retains 470 kΩ between the filter-control driver Q202 and the Q200 gate. The 5.08 mm pitch MRS16 fits between C223 and Q200, with respectively 0.120 and 0.157 mm between the courtyard boundaries. The larger 10.16 mm pitch did not fit the local route search. The 2.185 mm gate leaf replaces 5.632 mm. The driver-side leaf grows by 10.091 mm. Even an extra 5 pF on that side would be 0.05% of the fitted 10 nF C204. Maximum dissipation at 12 V across 470 kΩ is 0.31 mW. Keep the area around the high-impedance gate clean and check filter switching transients in both audio channels. [Vishay MRS16 dimensions and ratings](https://www.vishay.com/docs/28724/mrs16m25.pdf)

No existing bottom trace changed reference in the sampled regions. The affected original front copper is the C912 ground return adjacent to its own new ground barrel. All auxiliary power-zone areas and inner contour counts matched. The largest ground-reference gap on new copper beyond 1.3 mm from either new part was under 0.92 mm. C663 became the representative library-mismatch warning after the inherited R204 mismatch cleared. The C663 footprint is unchanged.

C919 remains surface-mount. Separate placements lost the required two-spoke ground connection on opposite outer copper layers. [Deferral register](../resumed-cycle/deferred.csv)

[Installed parts](conversion.csv) · [Trace lengths](routing.csv) · [Verification](verification.json) · [Native KiCad reports](kicad-reports.zip)
