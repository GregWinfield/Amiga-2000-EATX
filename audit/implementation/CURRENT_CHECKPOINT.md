# Scenario B+ motherboard recovery checkpoint

The verified batch is [cycle6-dram-address](cycle6-dram-address/README.md), with parent `437e65f5d49f968b8105561f606b151c39dcf69c`. Resolve its artwork commit with `git log -1 --format=%H -- audit/implementation/cycle6-dram-address/verification.json`. The refilled board SHA-256 with LF line endings is `79e0665a9b1cbec4da0e0a3da11c562c8660955bafe7e3297bdc1db6f1ba9225`.

| Current batch | Verified result |
|---|---|
| Converted positions | R500-1, R500-2, R500-4, R500-6, R500-7, R500-8, R500-9 |
| Physical packages | 177 THT, 377 SMD, 554 total, 31.9% THT |
| Conversion plan | 112 completed, 185 planned SMD, 95 deferred |
| ERC | 24 errors and 1182 warnings |
| Refilled DRC | 72 errors and 202 warnings |
| Schematic parity | 17 inherited warnings |
| Connectivity | Zero unrouted. All 3,603 schematic pins and 3,698 physical pad-net assignments match the control. |

[Object-level verification](cycle6-dram-address/verification.json) · [Native reports](cycle6-dram-address/kicad-reports.zip) · [Cycle 5 holds](cycle5/README.md) · [Current deferred register](cycle5/deferred.csv)

Fabrication approval remains withheld. Fabricator tolerances, connector fit and insertion, lead forming, populated clearances, RTC leakage and retention, reset behaviour, populated audio, and loaded signal and rail measurements remain open.
