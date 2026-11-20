# Scenario B+ motherboard recovery checkpoint

Last verified motherboard artwork is `e59e244e798712bfd0d617a8f9a7dc695bc016b4`. Its checks are in [resumed-atx-driver/verification.json](resumed-atx-driver/verification.json). Its parent design revision is `43bfbff1aef021d672cfd4c4ee53f2b41a9ad863`. The preceding verified artwork is `43bfbff1aef021d672cfd4c4ee53f2b41a9ad863`. Resolve the exact batch commit with `git log -1 --format=%H -- audit/implementation/resumed-atx-driver/verification.json`. Board SHA-256 with LF line endings is `0c257142780149644597b7cecd219b8b0c7fc68d0f110cf9aba36260f1d87cfd`.

| Current batch | Result |
|---|---|
| Converted positions | Q9100 |
| KiCad layout status | Verified on implementation/scenario-b-plus |
| ERC | 24 inherited errors and 1182 warnings |
| Refilled DRC | 73 errors and 202 warnings |
| Schematic parity | 17 inherited warnings |
| Connectivity | Zero unrouted. 3603 schematic pins and 3698 physical pad-net records compared. Zero net differences. |
| Physical packages | 137 THT, 417 SMD, 554 total, 24.7% THT |
| Conversion plan | 72 converted positions, 213 planned SMD positions, 39 deferred |

The [deferral register](resumed-cycle/deferred.csv) includes the nine ZS1 resistors, R800, C224 and R109. The batch verification file records individual DRC objects, reference-plane changes, clearances and the fixed mechanical datums. Fabrication release and bench qualification are pending.

Next group: Trial the standby timing cluster as a group, with the verified layout of the power switch as the fixed boundary.

After an interruption, inspect both worktrees and compare this batch with the GitHub branch before resuming.

The cycle closed with 22 new through-hole positions across six published artwork commits. C619, C919, C312, C315 and C316 joined the hold register. [Published batch history, comparison and next group](resumed-cycle/README.md) | [Independent end-to-end check](resumed-cycle/cycle-check.json)
