# Scenario B+ motherboard recovery checkpoint

The verified batch is [cycle9-u106-bypass](cycle9-u106-bypass/README.md), with parent `86c4389de1073096d07b83f1b93c32d912b4771a`. Resolve its artwork commit with `git log -1 --format=%H -- audit/implementation/cycle9-u106-bypass/verification.json`. The refilled board SHA-256 with LF line endings is `e88049ffc635b9747d8fb0360c8264341dd5f63c6f54103a5c146d2f002d32e5`.

| Current batch | Verified result |
|---|---|
| Converted positions | C106 |
| Physical packages | 217 THT, 337 SMD, 554 total, 39.2% THT |
| Conversion plan | 152 completed, 201 planned SMD, 135 deferred |
| ERC | 24 errors and 1182 warnings |
| Refilled DRC | 72 errors and 202 warnings |
| Schematic parity | 17 inherited warnings |
| Connectivity | Zero unrouted. All 3,603 schematic pins and 3,698 physical pad-net assignments match the control. |

[Object-level verification](cycle9-u106-bypass/verification.json) · [Native reports](cycle9-u106-bypass/kicad-reports.zip) · [Cycle 5 holds](cycle5/README.md) · [Current deferred register](cycle9/deferred.csv)

Fabrication approval remains withheld. Fabricator tolerances, connector fit and insertion, lead forming, populated clearances, RTC leakage and retention, reset behaviour, populated audio, and loaded signal and rail measurements remain open.

Final Cycle 9 artwork is `bc28fab5ba558fc3a84b73baacfcd21978d78ab5`. [Cycle report](cycle9/README.md) · [Cumulative CAD comparison](cycle9/cycle-check.json) · [Open holds](cycle9/deferred.csv). The separate PCB Explorer uses the engineering commit containing this comparison.
