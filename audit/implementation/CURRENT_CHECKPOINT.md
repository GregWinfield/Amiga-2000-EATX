# Scenario B+ motherboard recovery checkpoint

The verified batch is [cycle8-interface-supplies](cycle8-interface-supplies/README.md), with parent `cffff5ad5a1a3b1068d821a9ab1d117d2292ace1`. Resolve its artwork commit with `git log -1 --format=%H -- audit/implementation/cycle8-interface-supplies/verification.json`. The refilled board SHA-256 with LF line endings is `6dab3a5ba5370310900bd197f010d3f98519f8fe5326a85d5f8981884ecd9c8f`.

| Current batch | Verified result |
|---|---|
| Converted positions | RN907B1, C901, C206, C605 |
| Physical packages | 200 THT, 354 SMD, 554 total, 36.1% THT |
| Conversion plan | 135 completed, 193 planned SMD, 114 deferred |
| ERC | 24 errors and 1182 warnings |
| Refilled DRC | 72 errors and 202 warnings |
| Schematic parity | 17 inherited warnings |
| Connectivity | Zero unrouted. All 3,603 schematic pins and 3,698 physical pad-net assignments match the control. |

[Object-level verification](cycle8-interface-supplies/verification.json) · [Native reports](cycle8-interface-supplies/kicad-reports.zip) · [Cycle 5 holds](cycle5/README.md) · [Current deferred register](cycle7/deferred.csv)

Fabrication approval remains withheld. Fabricator tolerances, connector fit and insertion, lead forming, populated clearances, RTC leakage and retention, reset behaviour, populated audio, and loaded signal and rail measurements remain open.
