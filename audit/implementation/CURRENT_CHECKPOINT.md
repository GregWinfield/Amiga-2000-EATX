# Scenario B+ motherboard recovery checkpoint

The verified artwork for this batch is the commit containing [resumed-indicator-driver/verification.json](resumed-indicator-driver/verification.json). Its parent design revision is `7341f06a1f78edc0c7abaddc5530d2c53936680f`. The preceding verified artwork is `7341f06a1f78edc0c7abaddc5530d2c53936680f`. Resolve the exact batch commit with `git log -1 --format=%H -- audit/implementation/resumed-indicator-driver/verification.json`. Board SHA-256 with LF line endings is `dc0f9a763f75102807dc1cfa48f9cefe9bbb4106d2e9e7a1f656230c5afe7a11`.

| Current batch | Result |
|---|---|
| Converted positions | Q302 |
| KiCad layout status | Verified on implementation/scenario-b-plus |
| ERC | 24 inherited errors and 1182 warnings |
| Refilled DRC | 73 errors and 202 warnings |
| Schematic parity | 17 inherited warnings |
| Connectivity | Zero unrouted. 3603 schematic pins and 3698 physical pad-net records compared. Zero net differences. |
| Physical packages | 127 THT, 427 SMD, 554 total, 22.9% THT |
| Conversion plan | 62 converted positions, 223 planned SMD positions, 35 deferred |

The [deferral register](resumed-cycle/deferred.csv) includes the nine ZS1 resistors, R800, C224 and R109. The batch verification file records individual DRC objects, reference-plane changes, clearances and the fixed mechanical datums. Fabrication release and bench qualification are pending.

Next group: ISA connector-side capacitor fanout.

After an interruption, inspect both worktrees and compare this batch with the GitHub branch before resuming.
