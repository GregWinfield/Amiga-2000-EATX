# CPU, memory and bus supply bypasses

Five actual radial capacitors bring the installed count to 211 THT and 343 SMD. C103 and C109 serve CPU-side logic, C541 the 74AHCT244 memory buffer, C500 the Kickstart ROM and C603 the 74HCT245 bus buffer. The existing +5 V and GND pin assignments are preserved.

| Capacitor | Nominal | Supply land to associated device before / after | Nearest top courtyard |
|---|---:|---:|---:|
| C103 | 100 nF | 6.02 / 6.19 mm | 1.561 mm to U103 |
| C109 | 100 nF | 4.22 / 4.08 mm | 1.141 mm to U109 |
| C541 | 100 nF | 15.37 / 15.80 mm | 0.298 mm to U541 |
| C500 | 220 nF | 3.98 / 5.41 mm | 0.628 mm to R500-8 |
| C603 | 100 nF | 6.20 / 6.30 mm | 1.028 mm to U605 |

C500 exchanges 3.949 mm of narrow positive feed and 2.969 mm of ground lead for direct plated connections to both inner planes. C603 uses the same arrangement at the original distribution junction. C103, C109 and C541 retain local copper to the original supply and ground entries. Each new pad pair has two effective ground thermal paths on each outer face, four on In1.Cu and four into the inner supply. Continuous radial sections from 0.78 through 1.38 mm were measured after refill. All 36 changed outer ground contours have identified contacts. C109 and C603 have local changes to reference beneath their own supply or ground copper. Sampled adjacent signals preserve their reference. All newly routed copper retains its adjacent reference outside the immediate plated terminals. [Thermal paths](spokes.json) · [Ground contacts](ground-contacts.json) · [Changed routes](route-return.json)

The selected KEMET GoldMax parts are C315C104K5R5TA and C315C224K5R5TA. Both are radial X7R multilayer ceramics, ±10%, 50 V, −55 to +125 °C, with a 3.81 × 2.54 mm maximum body and 2.54 mm pitch. The board reserves a 0.80 mm drilled hole for the nominal 0.51 mm lead (0.61 mm maximum). Maximum seated height is 4.66 mm for 100 nF and 6.85 mm for 220 nF. Both ordering codes had distributor stock at review. The original shopping list specifies nominal ceramic values without an ordering code, voltage rating, dielectric or tolerance. These are documented Scenario B+ part selections. [100 nF manufacturer drawing](https://search.kemet.com/component-documentation/download/specsheet/C315C104K5R5TA) · [220 nF manufacturer drawing](https://search.kemet.com/component-documentation/download/specsheet/C315C224K5R5TA) · [100 nF sourcing](https://www.digikey.com/en/products/detail/kemet/C315C104K5R5TA/12701330) · [220 nF sourcing](https://www.digikey.com/en/products/detail/kemet/C315C224K5R5TA/14681404)

Seat these parts low, verify U541 solder access and check the populated C500 height against the ROM service envelope. Measure droop at the CPU transceiver, memory buffer, ROM and bus buffer during active switching. The KiCad comparison covers all schematic pins, physical pads, protected mechanical data and via objects. The 24 ERC errors, 1,182 ERC warnings, 72 DRC errors, 202 DRC warnings and 17 parity warnings reconcile to the inherited findings. There are zero opens. [Object comparison and package map](verification.json) · [Native reports](kicad-reports.zip)
