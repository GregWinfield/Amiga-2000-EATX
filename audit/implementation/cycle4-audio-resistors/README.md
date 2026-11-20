# Audio supply, reference and filter resistors

Four through-hole resistors fit on the component side using upright axial mounting at 2.54 mm pitch. Horizontal DIN0207 and DIN0204 patterns did not leave room for the same short connections. Body axes and the formed return leads are separated by the standard footprint. R210 uses the larger DIN0207. R230 and R242 use DIN0204. R207 uses the pulse-rated 10 Ω MBA0204 already specified for the opposite analogue supply feed. [Supply feed qualification](../accelerated-rail-feeds/README.md) · [MRS16 and MRS25](https://www.vishay.com/docs/28724/mrs16m25.pdf)

| Ref | Function | Nearest courtyard gap |
|---|---|---:|
| R207 | +12 V to +AV, 10 Ω, 0.4572 mm copper on both leads | 0.248 mm |
| R210 | 1.2 kΩ audio reference divider | 0.315 mm |
| R230 | 360 Ω right-channel signal path | 0.148 mm |
| R242 | 10 kΩ left-channel filter branch | 0.227 mm |

The net-length change on every analogue signal is below 0.82 mm. R230's two holes affect the immediately adjacent reference on its own Paula RIGHT input connection. The other sampled bottom routes retain their original reference. The front reference differences at R210 and R230 occur on their own signal and return nets. No inner contour split or auxiliary rail loss was found. The only DRC object substitutions were unchanged capacitors becoming the reported library-mismatch examples as four inherited resistor mismatches cleared.

Allow 10 mm above R210 and 7 mm above the three compact parts for the formed lead and standoff. Confirm the formed sample stays in its courtyard, the insulation clearance to the folded lead, and the operating temperature of R207 at the intended rail load. Short excess lead length and a supported bend are important at these placements. The original filters, thresholds and polarity are preserved. The two filter resistors remain within the existing 1% part grade. Confirm channel balance and the audio-reference startup transient on a populated board.

[Installed part numbers and pin maps](conversion.csv) · [Measured copper lengths](routing.csv) · [KiCad comparison](verification.json) · [Raw reports](kicad-reports.zip)
