# Floppy motor and reset control axials

KiCad 10.0.8 control `cfa3c41`. All listed references retain their original two numbered electrical connections and nominal resistance.

| Reference | Function | Axial order code | Closest front courtyard |
|---|---|---|---|
| R309 | GARY MTRON to Q301 base through 4.7 kΩ. This branch controls the floppy motor driver. | MRS25000C4701FCT00 | 0.260 mm to R802 |
| R602 | 1 kΩ pull-up on the _BRST reset distribution. | MRS25000C1001FCT00 | 0.284 mm to R305 |

Vishay specifies ±1% and ±50 ppm/K for these metal-film parts. MRS25 is DIN0207, 0.6 W at 70 °C, with a 6.5 × 2.5 mm maximum body and a nominal 0.6 mm lead. MRS16 is DIN0204, 0.4 W at 70 °C, with a 3.6 × 1.6 mm maximum body and a nominal 0.5 mm lead. The installed footprints use 10.16/5.08 mm pitch, 1.60/1.40 mm lands and 0.80/0.70 mm finished holes respectively. The source shopping list gives the 1206 values without an individual manufacturer, tolerance or power specification. At a nominal 5 V across a 1 kΩ, 4.7 kΩ, 10 kΩ or 47 kΩ part, the respective upper dissipation estimates are 25, 5.32, 2.50 and 0.53 mW. Series input positions require checking their actual interface voltage. Verify lead and hole tolerances, barrel fill, formed height and underside trim on a witness. [Manufacturer data](https://www.vishay.com/docs/28724/mrs16m25.pdf) · [Baseline shopping list](../../../BOM/A2000EATX-REV31-ShoppingList.csv)

- **ERC** 24 errors, 1182 warnings. Object-level comparison: 4 newly listed, 4 previously listed. Raw details identify the items on each side.
- **DRC** 73 errors, 202 warnings. Object-level comparison: 2 newly listed, 2 previously listed. Raw details identify the items on each side.
- **Schematic parity** 0 errors, 17 warnings. Object-level comparison: 0 newly listed, 0 previously listed. Raw details identify the items on each side.
- **Unrouted** 0 errors, 0 warnings. Object-level comparison: 0 newly listed, 0 previously listed. Raw details identify the items on each side.

The DRC list is bounded. Any newly listed library mismatch pertains to a pre-existing footprint; each difference is identified in the object report. The ERC differences, if present, retain the same issue categories and messages. No new short, clearance violation or open is accepted. The schematic pin and physical pad-net maps compare equal. All existing signal segments and 1211 vias retain their complete native geometry. New trace segments use F.Cu. All 54 protected connector and mounting datums, the EATX perimeter and stack compare equal.

Native polygon sampling checks the In2 reference of original underside tracks near the new drills and the In1 reference under nearby original front tracks. Front changes at a signal or bias lead are local plane clearances around its plated barrel. The per-reference record lists affected nets, sample counts and supply/ground spoke directions. Check those nodes and assembly clearance on hardware. See [per-net lengths](routing.csv), [position and package manifest](conversion.csv), [object and plane comparison](verification.json) and [native control and evaluated reports](kicad-reports.zip).

R309 adds 7.500 mm on the motor-control branch. The original driver and fan-out copper remain in place. The added _BRST branch is 0.583 mm. The four In2 copper spokes at R602 connect the new supply lead. Inspect motor switching and reset assertion/release with the drive fitted.

Physical population after this batch: 79 THT, 475 SMD. Hardware validation and fabrication acceptance remain open.
