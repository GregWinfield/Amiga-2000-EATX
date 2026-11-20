# Processor bus override pull-up

R115 remains a 330 Ω pull-up from _OVR to +5 V. The MRS16 mounts on the front. The 6.724 mm signal connection on the back starts at an existing _OVR via. The supply uses the resistor barrel and the In2 plane. The old three-segment front branch ended at U102 pin 29, and its separate supply spur ended at R500 pin 1. Those four traces are retired. Every original bus trunk, via and unrelated track remains intact. No sampled preserved front or back route changes reference. The 6.724 mm added branch is shorter than the retired signal branch. At 7 ps/mm it has a one-way flight time of about 47 ps. Check the _OVR edge and overshoot with representative bus loading.

The old R917 _DTACK location was evaluated alongside R115. Reusing its closest signal via from the back left the via connected on only one layer. The alternate front escape did not produce a clear local axial installation. R917 keeps its accepted copper and original package. C905 keeps a visible service reference at its new position. The value of C421 is on F.Fab.

[Installed positions and pin mapping](conversion.csv) · [Net lengths](routing.csv) · [Verification and fixed datums](verification.json) · [Native KiCad reports and netlists](kicad-reports.zip)
At 0.025 mm sample spacing, all 2.279 mm of added route lacking immediate In2 +5 V lies within 1.3 mm of the source via or new lead. [Endpoint samples](terminal-reference.json)
