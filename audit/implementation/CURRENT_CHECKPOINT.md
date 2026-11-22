# Scenario B+ motherboard recovery checkpoint

The verified batch is [cycle8-clock-series](cycle8-clock-series/README.md), with parent `7f3343a7f2fa5293fb9fc29bb7a398af6d57bff3`. Resolve its artwork commit with `git log -1 --format=%H -- audit/implementation/cycle8-clock-series/verification.json`. The refilled board SHA-256 with LF line endings is `c30e609e3eb8f0cb9af823ecec771d8915bd6700fb126928cd8ade977c9b4989`.

| Current batch | Verified result |
|---|---|
| Converted positions | R212, R905 |
| Physical packages | 206 THT, 348 SMD, 554 total, 37.2% THT |
| Conversion plan | 141 completed, 192 planned SMD, 114 deferred |
| ERC | 24 errors and 1182 warnings |
| Refilled DRC | 72 errors and 202 warnings |
| Schematic parity | 17 inherited warnings |
| Connectivity | Zero unrouted. All 3,603 schematic pins and 3,698 physical pad-net assignments match the control. |

[Object-level verification](cycle8-clock-series/verification.json) · [Native reports](cycle8-clock-series/kicad-reports.zip) · [Cycle 5 holds](cycle5/README.md) · [Current deferred register](cycle7/deferred.csv)

Fabrication approval remains withheld. Fabricator tolerances, connector fit and insertion, lead forming, populated clearances, RTC leakage and retention, reset behaviour, populated audio, and loaded signal and rail measurements remain open.
