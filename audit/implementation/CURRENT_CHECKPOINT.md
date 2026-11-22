# Scenario B+ motherboard recovery checkpoint

The verified batch is [cycle10-supply-returns](cycle10-supply-returns/README.md), with parent `175d9b9ad1b8b7d6264b4b0577b2a43907e048ed`. Resolve its artwork commit with `git log -1 --format=%H -- audit/implementation/cycle10-supply-returns/verification.json`. The refilled board SHA-256 with LF line endings is `8e2076fac3c30c55be1135bc8adf5f4ab92d3e8ce9ec8a71558e42f3aa451f21`.

| Current batch | Verified result |
|---|---|
| Converted positions | C409, C300, C203, C205 |
| Physical packages | 224 THT, 330 SMD, 554 total, 40.4% THT |
| Conversion plan | 159 completed, 199 planned SMD, 134 deferred |
| ERC | 24 errors and 1182 warnings |
| Refilled DRC | 71 errors and 202 warnings |
| Schematic parity | 17 inherited warnings |
| Connectivity | Zero unrouted. All 3,603 schematic pins and 3,698 physical pad-net assignments match the control. |

[Object-level verification](cycle10-supply-returns/verification.json) · [Native reports](cycle10-supply-returns/kicad-reports.zip) · [Cycle 5 holds](cycle5/README.md) · [Current deferred register](cycle10/deferred.csv)

Fabrication approval remains withheld. Fabricator tolerances, connector fit and insertion, lead forming, populated clearances, RTC leakage and retention, reset behaviour, populated audio, and loaded signal and rail measurements remain open.
