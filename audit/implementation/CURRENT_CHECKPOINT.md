# Scenario B+ motherboard recovery checkpoint

The verified artwork for this batch is the commit containing [resumed-keyboard-audio/verification.json](resumed-keyboard-audio/verification.json). Its parent design revision is `a19d0fe3e6320ccc1e356e4cfb0e5bcd88279638`. The preceding verified artwork is `a19d0fe3e6320ccc1e356e4cfb0e5bcd88279638`. Resolve the exact batch commit with `git log -1 --format=%H -- audit/implementation/resumed-keyboard-audio/verification.json`. Board SHA-256 with LF line endings is `4064e873cb7fec96ffca449f78a071adf802b0c0df12e70adb37df332979c3f8`.

| Current batch | Result |
|---|---|
| Converted positions | C912, R204 |
| KiCad layout status | Verified on implementation/scenario-b-plus |
| ERC | 24 inherited errors and 1182 warnings |
| Refilled DRC | 73 errors and 202 warnings |
| Schematic parity | 17 inherited warnings |
| Connectivity | Zero unrouted. 3603 schematic pins and 3698 physical pad-net records compared. Zero net differences. |
| Physical packages | 136 THT, 418 SMD, 554 total, 24.5% THT |
| Conversion plan | 71 converted positions, 214 planned SMD positions, 36 deferred |

The [deferral register](resumed-cycle/deferred.csv) includes the nine ZS1 resistors, R800, C224 and R109. The batch verification file records individual DRC objects, reference-plane changes, clearances and the fixed mechanical datums. Fabrication release and bench qualification are pending.

Next group: Check the separate ATX soft-power transistor and serial-port filter trials.

After an interruption, inspect both worktrees and compare this batch with the GitHub branch before resuming.
