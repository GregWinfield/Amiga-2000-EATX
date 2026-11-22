# Scenario B+ motherboard recovery checkpoint

The verified batch is [cycle8-audio-bus-bypass](cycle8-audio-bus-bypass/README.md), with parent `d3948fb823c27d4726baa38c30fa6d89097b32b8`. Resolve its artwork commit with `git log -1 --format=%H -- audit/implementation/cycle8-audio-bus-bypass/verification.json`. The refilled board SHA-256 with LF line endings is `ec51f0eb43b7092d66ab392f98cc3e6b7f8376f5815866f76e165df5a6a8dafb`.

| Current batch | Verified result |
|---|---|
| Converted positions | C318, C502, C602, C604 |
| Physical packages | 204 THT, 350 SMD, 554 total, 36.8% THT |
| Conversion plan | 139 completed, 192 planned SMD, 114 deferred |
| ERC | 24 errors and 1182 warnings |
| Refilled DRC | 72 errors and 202 warnings |
| Schematic parity | 17 inherited warnings |
| Connectivity | Zero unrouted. All 3,603 schematic pins and 3,698 physical pad-net assignments match the control. |

[Object-level verification](cycle8-audio-bus-bypass/verification.json) · [Native reports](cycle8-audio-bus-bypass/kicad-reports.zip) · [Cycle 5 holds](cycle5/README.md) · [Current deferred register](cycle7/deferred.csv)

Fabrication approval remains withheld. Fabricator tolerances, connector fit and insertion, lead forming, populated clearances, RTC leakage and retention, reset behaviour, populated audio, and loaded signal and rail measurements remain open.
