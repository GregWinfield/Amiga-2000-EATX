# Scenario B+ motherboard recovery checkpoint

The verified artwork for this batch is the commit containing [cycle5-rtc-and-grant/verification.json](cycle5-rtc-and-grant/verification.json). Its parent design revision is `c9fb54d0946b6f75a7347fba236c8f40bcac2986`. The preceding verified artwork is `c9fb54d0946b6f75a7347fba236c8f40bcac2986`. Resolve the exact batch commit with `git log -1 --format=%H -- audit/implementation/cycle5-rtc-and-grant/verification.json`. Board SHA-256 with LF line endings is `3bb4259c868d34e4475bc5626fd74f358d10e9d655ddf4e77a0e737cafbf9cf5`.

| Current batch | Result |
|---|---|
| Converted positions | C811, R806 |
| KiCad layout status | Verified on implementation/scenario-b-plus |
| ERC | 24 inherited errors and 1182 warnings |
| Refilled DRC | 72 errors and 202 warnings |
| Schematic parity | 17 inherited warnings |
| Connectivity | Zero unrouted. 3603 schematic pins and 3698 physical pad-net records compared. Zero net differences. |
| Physical packages | 163 THT, 391 SMD, 554 total, 29.4% THT |
| Conversion plan | 98 converted positions, 187 planned SMD positions, 95 deferred |

The [deferral register](cycle5/deferred.csv) includes the nine ZS1 resistors, R800, C224 and R109. The batch verification file records individual DRC objects, reference-plane changes, clearances and the fixed mechanical datums. Fabrication release and bench qualification are pending.

Next group: reset supervisor.

After an interruption, inspect both worktrees and compare this batch with the GitHub branch before resuming.
