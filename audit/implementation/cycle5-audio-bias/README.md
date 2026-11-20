# Audio input and transistor bias

R202 and R206 use 10 kΩ MRS16 metal-film resistors. R213 uses the 2.7 kΩ part from the same 1% family. The 2.54 mm upright footprints keep both original copper taps on each resistor. The longest added lead trace is 1.54 mm. Allow 7 mm above the board for each formed resistor and verify the return lead and body fit inside the courtyard. R206 has 0.071 mm between its assembly courtyard and R241’s. Check the formed pair on the first assembly. [Manufacturer dimensions and ratings](https://www.vishay.com/docs/28724/mrs16m25.pdf)

At R213 the +AV barrel removes a small patch of In2 reference under two segments of its own analogue supply. The front-layer changes at R206 and R213 occur on the associated transistor and supply connections. Every added trace regains its reference outside the 1.3 mm pad neighbourhood. No bus reference, auxiliary polygon, plane island count or via changed. Check channel gain, noise and DC bias on the populated board.

[Part and pin mapping](conversion.csv) · [Copper lengths](routing.csv) · [Object-level checks](verification.json) · [KiCad reports](kicad-reports.zip)
