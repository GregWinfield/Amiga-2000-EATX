# Scenario B+ motherboard recovery checkpoint

The verified artwork for this batch is the commit containing [resumed-termination-capacitors/verification.json](resumed-termination-capacitors/verification.json). Its parent design revision is `f89074ea3d777a54c84b7281e9e6599ffa2f71f3`. The preceding verified artwork is `f89074ea3d777a54c84b7281e9e6599ffa2f71f3`. Resolve the exact batch commit with `git log -1 --format=%H -- audit/implementation/resumed-termination-capacitors/verification.json`. Board SHA-256 with LF line endings is `f3c40a6df5dd853bd085f0224c741d305029506f7a4808c1c6bf98eec0d59a63`.

| Current batch | Result |
|---|---|
| Converted positions | C664, C672, C711, C776, C789, C794 |
| KiCad layout status | Verified on implementation/scenario-b-plus |
| ERC | 24 inherited errors and 1182 warnings |
| Refilled DRC | 73 errors and 202 warnings |
| Schematic parity | 17 inherited warnings |
| Connectivity | Zero unrouted. 3603 schematic pins and 3698 physical pad-net records compared. Zero net differences. |
| Physical packages | 126 THT, 428 SMD, 554 total, 22.7% THT |
| Conversion plan | 61 converted positions, 224 planned SMD positions, 35 deferred |

The [deferral register](resumed-cycle/deferred.csv) includes the nine ZS1 resistors, R800, C224 and R109. The batch verification file records individual DRC objects, reference-plane changes, clearances and the fixed mechanical datums. Fabrication release and bench qualification are pending.

Next group: Q302 indicator driver and the passive ISA RC branches.

After an interruption, inspect both worktrees and compare this batch with the GitHub branch before resuming.
