# Scenario B+ motherboard recovery checkpoint

The verified artwork for this batch is the commit containing [cycle4-expansion-signals/verification.json](cycle4-expansion-signals/verification.json). Its parent design revision is `faa923d6ae9b8179169be0f8341b7df7d45d9783`. The preceding verified artwork is `faa923d6ae9b8179169be0f8341b7df7d45d9783`. Resolve the exact batch commit with `git log -1 --format=%H -- audit/implementation/cycle4-expansion-signals/verification.json`. Board SHA-256 with LF line endings is `52fd6b9ed309efcdd4dbc95416366b3f3e8041aa75956f401681d1d67379f424`.

| Current batch | Result |
|---|---|
| Converted positions | C700, C746, C748, R111 |
| KiCad layout status | Verified on implementation/scenario-b-plus |
| ERC | 24 inherited errors and 1182 warnings |
| Refilled DRC | 73 errors and 202 warnings |
| Schematic parity | 17 inherited warnings |
| Connectivity | Zero unrouted. 3603 schematic pins and 3698 physical pad-net records compared. Zero net differences. |
| Physical packages | 154 THT, 400 SMD, 554 total, 27.8% THT |
| Conversion plan | 89 converted positions, 196 planned SMD positions, 41 deferred |

The [deferral register](cycle4/deferred.csv) includes the nine ZS1 resistors, R800, C224 and R109. The batch verification file records individual DRC objects, reference-plane changes, clearances and the fixed mechanical datums. Fabrication release and bench qualification are pending.

Next group: Verify remaining expansion reservoirs against the combined refilled board and complete the audio filter trial.

After an interruption, inspect both worktrees and compare this batch with the GitHub branch before resuming.
