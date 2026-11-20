# R914 keyboard supply feed

The +5 V keyboard feed retains 1 Ω ahead of FB301. PR01000101008FA500 is the through-hole 1%, 1 W PR01 already qualified for layout on the board’s 1 Ω supplies. The source BOM specifies 0.5 W and identifies no fuse function. Keep the original load limit. At 0.5 A the part drops 0.5 V and dissipates 0.25 W. The new 0.70 mm traces add 5.223 mm in total, approximately 3.7 mΩ at 35 µm copper and 20 °C. The In1 reference gap extending beyond the immediate pad neighbourhood is 0.875 mm on the DC supply connection. Other existing traces retain their sampled reference.

C912 (470 µF) and C259 (100 pF) sit downstream of the bead on the keyboard connector supply. At 5.25 V, +20% capacitance and ±1% resistance, ideal turn-on gives 27.9 W peak and an equal-energy pulse width of 0.285 ms, within the PR01 low-duty startup screen used for R200. Accessory inrush, repeated insertion, short-circuit supply limiting and enclosure temperature still need measurement. [Manufacturer pulse curves](https://www.vishay.com/docs/28729/pr010203.pdf) · [Existing feed qualification](../accelerated-rail-feeds/README.md)

The horizontal 10.16 mm footprint clears CN300 by 1.061 mm and C259 by 0.130 mm between courtyards. C259’s two legend fields moved. H3 has a circular 4.00 mm radius courtyard with a 0.05 mm stroke. Allowing 4.05 mm radially leaves 0.086 mm to the resistor courtyard corner. The actual 1.60 mm land clears that envelope by about 0.85 mm. Check the assembled keyboard plug, screw, washer and driver with the intended chassis before release.

[Part and pin map](conversion.csv) · [Routing](routing.csv) · [KiCad verification](verification.json)
