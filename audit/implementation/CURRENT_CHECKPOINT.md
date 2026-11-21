# Scenario B+ motherboard recovery checkpoint

The verified artwork for this batch is the commit containing [cycle5-filter-resistor/verification.json](cycle5-filter-resistor/verification.json). Its parent design revision is `8c3a92d877cedc2a585fa53270c3035e00a930b8`. The preceding verified artwork is `8c3a92d877cedc2a585fa53270c3035e00a930b8`. Resolve the exact batch commit with `git log -1 --format=%H -- audit/implementation/cycle5-filter-resistor/verification.json`. Board SHA-256 with LF line endings is `60941ba2003f0ec8a2a6d713c8cf37cc3bfade16caf995e248f046751c49a934`.

| Current batch | Result |
|---|---|
| Converted positions | R232 |
| KiCad layout status | Verified on implementation/scenario-b-plus |
| ERC | 24 inherited errors and 1182 warnings |
| Refilled DRC | 72 errors and 202 warnings |
| Schematic parity | 17 inherited warnings |
| Connectivity | Zero unrouted. 3603 schematic pins and 3698 physical pad-net records compared. Zero net differences. |
| Physical packages | 165 THT, 389 SMD, 554 total, 29.8% THT |
| Conversion plan | 100 converted positions, 185 planned SMD positions, 95 deferred |

The [deferral register](cycle5/deferred.csv) includes the nine ZS1 resistors, R800, C224 and R109. The batch verification file records individual DRC objects, reference-plane changes, clearances and the fixed mechanical datums. Fabrication release and bench qualification are pending.

Final Cycle 5 artwork is `7994c796b09d900ef0457c6b4a7c6ea9d2400fad`. [Cycle report](cycle5/README.md) · [CAD reconciliation](cycle5/cycle-check.json) · [Engineering holds](cycle5/deferred.csv). The next trial is the paired audio filter assessment. After an interruption, compare the published heads and inspect both worktrees before resuming.
