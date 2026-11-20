# Scenario B+ motherboard recovery checkpoint

The verified artwork for this batch is the commit containing [cycle4-audio-resistors/verification.json](cycle4-audio-resistors/verification.json). Its parent design revision is `824dd94bc5a3831dc0179351796cb21e939ca677`. The preceding verified artwork is `e59e244e798712bfd0d617a8f9a7dc695bc016b4`. Resolve the exact batch commit with `git log -1 --format=%H -- audit/implementation/cycle4-audio-resistors/verification.json`. Board SHA-256 with LF line endings is `211f32e72ebc6863d2cac1485d4bb1827e81f810210feb97f265f905953f3e20`.

| Current batch | Result |
|---|---|
| Converted positions | R207, R210, R230, R242 |
| KiCad layout status | Verified on implementation/scenario-b-plus |
| ERC | 24 inherited errors and 1182 warnings |
| Refilled DRC | 73 errors and 202 warnings |
| Schematic parity | 17 inherited warnings |
| Connectivity | Zero unrouted. 3603 schematic pins and 3698 physical pad-net records compared. Zero net differences. |
| Physical packages | 141 THT, 413 SMD, 554 total, 25.5% THT |
| Conversion plan | 76 converted positions, 209 planned SMD positions, 41 deferred |

The [deferral register](cycle4/deferred.csv) includes the nine ZS1 resistors, R800, C224 and R109. The batch verification file records individual DRC objects, reference-plane changes, clearances and the fixed mechanical datums. Fabrication release and bench qualification are pending.

Next group: Verify the staggered ISA termination row and radial reservoir candidates.

After an interruption, inspect both worktrees and compare this batch with the GitHub branch before resuming.
