# Scenario B+ motherboard recovery checkpoint

The verified artwork for this batch is the commit containing [resumed-isa-rn700/verification.json](resumed-isa-rn700/verification.json). Its parent design revision is `20b9c276e16dbb7e27d33c25b317cf29f7441263`. The preceding verified artwork is `20b9c276e16dbb7e27d33c25b317cf29f7441263`. Resolve the exact batch commit with `git log -1 --format=%H -- audit/implementation/resumed-isa-rn700/verification.json`. Board SHA-256 with LF line endings is `42ebe1c94fe0aa7064b8b21baaea730547b5937f7ee0d548349a6d9b3775998c`.

| Current batch | Result |
|---|---|
| Converted positions | C713, C714, C716, C717, C719, C720, C722 |
| KiCad layout status | Verified on implementation/scenario-b-plus |
| ERC | 24 inherited errors and 1182 warnings |
| Refilled DRC | 73 errors and 202 warnings |
| Schematic parity | 17 inherited warnings |
| Connectivity | Zero unrouted. 3603 schematic pins and 3698 physical pad-net records compared. Zero net differences. |
| Physical packages | 134 THT, 420 SMD, 554 total, 24.2% THT |
| Conversion plan | 69 converted positions, 216 planned SMD positions, 35 deferred |

The [deferral register](resumed-cycle/deferred.csv) includes the nine ZS1 resistors, R800, C224 and R109. The batch verification file records individual DRC objects, reference-plane changes, clearances and the fixed mechanical datums. Fabrication release and bench qualification are pending.

Next group: Keyboard supply and low-frequency indicator bypass.

After an interruption, inspect both worktrees and compare this batch with the GitHub branch before resuming.
