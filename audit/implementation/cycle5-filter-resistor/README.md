# R232 audio filter resistor

R232 now uses a Vishay MRS16000C1002FCT00 upright 10 kΩ, 1% axial resistor on 2.54 mm pitch. Pin 1 remains on the Q201 source node and pin 2 on the private C231 filter junction. The closest courtyard is C231 at 0.130 mm. Allow 7 mm for the formed part and verify body, return-lead and soldering access with a populated sample. [Vishay MRS16 dimensions and ratings](https://www.vishay.com/docs/28724/mrs16m25.pdf)

The recovered placement left 2.4384 mm of original SMD copper ending beyond the new connection. The final trial replaced that spur from the existing branch point to the new plated land. Total copper grew by 0.004 mm on the C231 net and 0.143 mm on the Q201 source net. Both connections stay on the front layer. No via was added or retired. The refill changed local reference copper under two segments of the same Q201 node. The comparison found no changed bottom-layer references or plane island counts.

The refilled board has zero unrouted connections. Object-level ERC, DRC, schematic parity, pad-net and mechanical comparisons found no new electrical or mechanical error. Measure channel response and noise on first assembly.

[Part and pin mapping](conversion.csv) · [Copper lengths](routing.csv) · [Object-level checks](verification.json) · [Native KiCad reports](kicad-reports.zip)
