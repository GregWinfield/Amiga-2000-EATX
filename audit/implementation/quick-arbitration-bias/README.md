# Processor and Buster arbitration bias

The same-version control is `dcd1418`. Each part retains its resistance, reference designator and both numbered nets. The exact original resistor tolerance and power grade are unspecified in the EATX shopping list. The selected metal-film parts are ±1%, ±50 ppm/K. MRS25 is rated 0.6 W at 70 °C in its specified mounting configuration, MRS16 is rated 0.4 W. At 5 V a 330 Ω resistor dissipates 75.8 mW, a 1 kΩ resistor 25 mW, a 4.7 kΩ resistor 5.32 mW, a 10 kΩ resistor 2.5 mW and a 47 kΩ resistor 0.53 mW. R306 would dissipate 62.5 mW at 25 V across 10 kΩ. [Vishay dimensions, ratings and order codes](https://www.vishay.com/docs/28724/mrs16m25.pdf) · [Baseline shopping list](../../../BOM/A2000EATX-REV31-ShoppingList.csv)

| Reference | Electrical function | Axial part | Nearest front courtyard |
|---|---|---|---|
| R114 | 330 Ω XRDY pull-up. Its original feed contacts the surface-mount land mid-trace. | MRS16000C3300FCT00 | 1.580 mm to R500 |
| R807 | Buster _CBR arbitration pull-up. | MRS16000C4701FCT00 | 0.807 mm to U800 |

The standard DIN0207 land pattern has 10.16 mm pitch, 1.60 mm lands and 0.80 mm bores. The compact DIN0204 pattern has 5.08 mm pitch, 1.40 mm lands and 0.70 mm bores. MRS25 and MRS16 maximum bodies are 6.5 × 2.5 and 3.6 × 1.6 mm respectively, with nominal lead diameters of 0.6 and 0.5 mm. Confirm supplier finished-hole and lead tolerances, actual seated height, card fit as applicable and underside trim. The compact geometry permits shorter signal taps or avoids an adjacent part. [Exact part, placement and pin maps](conversion.csv)

- **ERC** 24 errors, 1182 warnings. 3 newly listed and 3 previously listed item signatures.
- **DRC** 73 errors, 202 warnings. 1 newly listed and 1 previously listed item signatures.
- **Schematic parity** 0 errors, 17 warnings. 0 newly listed and 0 previously listed item signatures.
- **Unrouted** 0 errors, 0 warnings. 0 newly listed and 0 previously listed item signatures.

The object-level comparison records each change in the bounded library-warning list and each inherited ERC item whose representative changed. New physical violations and opens are zero. The full schematic pin and physical pad-net mappings compare equal. All 1,211 vias and every pre-existing track remain intact. The added copper is on F.Cu. All 54 fixed datums, the board edges and four-layer stack match the control. [Raw KiCad reports and XML](kicad-reports.zip) · [Routing lengths by net](routing.csv) · [Geometry, plane and item-level checks](verification.json)

The new front traces were sampled over In1 at intervals of 0.05 mm or less. The verification file gives total route length, length without immediate GND copper and the subset outside a 1.3 mm radius of any new barrel. The underside checks compare nearby original routes against the refilled In2 region. Plane clearance around the new barrels is included.

R500 retains its reference on the service silkscreen. Its 4.7 kΩ value moved to F.Fab to clear the R114 lead and body legend. The XRDY and _CBR taps add 4.104 and 1.189 mm respectively. All additional signal copper outside the 1.3 mm lead neighbourhood lies above In1 ground. Both new positive leads have four measured spokes into In2 +5 V. Inspect their spoke connections and test XRDY and _CBR with an accelerator and expansion cards under load.

Installed population is 90 through-hole and 464 SMD. Fabrication and physical validation remain open.
