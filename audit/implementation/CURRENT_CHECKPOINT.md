# Scenario B+ motherboard recovery checkpoint

The verified artwork for this batch is the commit containing [cycle5-reset-supervisor/verification.json](cycle5-reset-supervisor/verification.json). Its parent design revision is `bdf143a11889399fc2d9234dd2f6c76a53bde5ea`. The preceding verified artwork is `bdf143a11889399fc2d9234dd2f6c76a53bde5ea`. Resolve the exact batch commit with `git log -1 --format=%H -- audit/implementation/cycle5-reset-supervisor/verification.json`. Board SHA-256 with LF line endings is `3ad8f38597b7d69623a1e6c4ac5499965dd7f945f9d73eb10c9baf365a1ffc30`.

| Current batch | Result |
|---|---|
| Converted positions | XU1 |
| KiCad layout status | Verified on implementation/scenario-b-plus |
| ERC | 24 inherited errors and 1182 warnings |
| Refilled DRC | 72 errors and 202 warnings |
| Schematic parity | 17 inherited warnings |
| Connectivity | Zero unrouted. 3603 schematic pins and 3698 physical pad-net records compared. Zero net differences. |
| Physical packages | 164 THT, 390 SMD, 554 total, 29.6% THT |
| Conversion plan | 99 converted positions, 186 planned SMD positions, 95 deferred |

The [deferral register](cycle5/deferred.csv) includes the nine ZS1 resistors, R800, C224 and R109. The batch verification file records individual DRC objects, reference-plane changes, clearances and the fixed mechanical datums. Fabrication release and bench qualification are pending.

Next group: R232 audio filter resistor.

After an interruption, inspect both worktrees and compare this batch with the GitHub branch before resuming.
