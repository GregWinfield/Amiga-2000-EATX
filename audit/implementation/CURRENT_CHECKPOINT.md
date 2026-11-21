# Scenario B+ motherboard recovery checkpoint

The verified batch is [cycle7-cia-bypass](cycle7-cia-bypass/README.md), with parent `f3ad936ed08df2c51a64f25bb1a8a2d3328dc0b6`. Resolve its artwork commit with `git log -1 --format=%H -- audit/implementation/cycle7-cia-bypass/verification.json`. The refilled board SHA-256 with LF line endings is `1a76c491b318db4e33af29a494ce1c57ef64e69b837551fae2cf58bf7b4986f1`.

| Current batch | Verified result |
|---|---|
| Converted positions | C301 |
| Physical packages | 196 THT, 358 SMD, 554 total, 35.4% THT |
| Conversion plan | 131 completed, 193 planned SMD, 114 deferred |
| ERC | 24 errors and 1182 warnings |
| Refilled DRC | 72 errors and 202 warnings |
| Schematic parity | 17 inherited warnings |
| Connectivity | Zero unrouted. All 3,603 schematic pins and 3,698 physical pad-net assignments match the control. |

[Object-level verification](cycle7-cia-bypass/verification.json) · [Native reports](cycle7-cia-bypass/kicad-reports.zip) · [Cycle 5 holds](cycle5/README.md) · [Current deferred register](cycle7/deferred.csv)

Fabrication approval remains withheld. Fabricator tolerances, connector fit and insertion, lead forming, populated clearances, RTC leakage and retention, reset behaviour, populated audio, and loaded signal and rail measurements remain open.

Final Cycle 7 artwork is `45aaed01bb321b46009c996124a4218e386e168b`. [Cycle report](cycle7/README.md) · [Cumulative CAD comparison](cycle7/cycle-check.json) · [Open holds](cycle7/deferred.csv). The separate PCB Explorer uses the engineering commit containing this comparison.
