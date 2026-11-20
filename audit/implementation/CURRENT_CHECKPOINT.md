# Scenario B+ motherboard recovery checkpoint

The verified artwork for this batch is the commit containing [cycle5-audio-bias/verification.json](cycle5-audio-bias/verification.json). Its parent design revision is `a5552f5480a750f33415dabb2c4002c3b66b9242`. The preceding verified artwork is `9f42a84b01259dd6c112fab168786e06c2e8e8ea`. Resolve the exact batch commit with `git log -1 --format=%H -- audit/implementation/cycle5-audio-bias/verification.json`. Board SHA-256 with LF line endings is `f4cbbcdfab5afadf50a207eb4fee2075a6cbb81134c2fc1408e93bc0e3ffd14d`.

| Current batch | Result |
|---|---|
| Converted positions | R202, R206, R213 |
| KiCad layout status | Verified on implementation/scenario-b-plus |
| ERC | 24 inherited errors and 1182 warnings |
| Refilled DRC | 73 errors and 202 warnings |
| Schematic parity | 17 inherited warnings |
| Connectivity | Zero unrouted. 3603 schematic pins and 3698 physical pad-net records compared. Zero net differences. |
| Physical packages | 160 THT, 394 SMD, 554 total, 28.9% THT |
| Conversion plan | 95 converted positions, 190 planned SMD positions, 52 deferred |

The [deferral register](cycle5/deferred.csv) includes the nine ZS1 resistors, R800, C224 and R109. The batch verification file records individual DRC objects, reference-plane changes, clearances and the fixed mechanical datums. Fabrication release and bench qualification are pending.

Next group: RTC reservoir and interface pull-up.

After an interruption, inspect both worktrees and compare this batch with the GitHub branch before resuming.
