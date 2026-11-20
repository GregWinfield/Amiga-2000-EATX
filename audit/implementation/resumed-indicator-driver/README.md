# Q302 front-panel indicator driver

The installed part is onsemi 2N3906G, the straight-lead bulk TO-92. Q302 switches the 5 V indicator supply. R902 supplies base drive through 4.7 kΩ, and R307 limits collector current through 68 Ω. At 5 V, even a shorted external load draws at most 74 mA through R307. The maximum possible transistor collector dissipation on that load line is 92 mW. Base drive is approximately 0.9 mA with a low input. The MMBT3906 and 2N3906 have the same 40 V and 200 mA limits, minimum gain of 100 at 10 mA and 60 at 50 mA under the specified gain-test conditions, 4.5 pF maximum output capacitance and 225 ns maximum storage time at the stated switching test point. The operating load and base drive determine actual saturation. The indicator path has no system clock or arbitration timing requirement. Check the loaded indicator voltage and brightness on hardware. [Original SOT-23 data](https://www.onsemi.com/pdf/datasheet/mmbt3906lt1-d.pdf) · [Installed TO-92 data and package drawing](https://www.onsemi.com/pdf/datasheet/2n3906-d.pdf)

| Physical lead, onsemi Style 1 | Schematic and PCB pad | Verified net |
|---|---|---|
| 1, emitter | 2 | +5V |
| 2, base | 1 | Net-(Q302-B) |
| 3, collector | 3 | Net-(Q302-C) |

Fit the flat face to the outline and form the centre base lead to the staggered hole. All three lands are round. The manufacturer gives maximum lead dimensions of 0.533 × 0.50 mm, a 0.731 mm diagonal. A 0.90 mm finished hole at −0.075 mm leaves 0.094 mm diametral allowance. The 1.45 mm land gives 0.275 mm nominal annular ring, or 0.1625 mm with +0.075 mm finished-hole tolerance and 0.075 mm centre offset. These are fabrication capability requirements for the layout. The 5.33 × 4.19 mm maximum package body has a dedicated courtyard and 4.53 mm to the next courtyard. Allow 5.20 mm body height plus the actual lead-form standoff and verify the formed sample before fabrication.

The emitter barrel connects directly to In2 +5 V with three sampled thermal spokes. The former 2.881 mm emitter spur and its dedicated +5 V via were retired. Every other via and pre-existing track is identical. Base and collector extensions are 9.10 and 6.53 mm on F.Cu. All added copper has nearby ground except at the device antipads. Sampled preserved traces on both sides retain their original reference. Auxiliary rail areas and all inner contour counts match the control.

[Installed component](conversion.csv) · [Net lengths](routing.csv) · [Physical and electrical verification](verification.json) · [Raw KiCad reports](kicad-reports.zip)
