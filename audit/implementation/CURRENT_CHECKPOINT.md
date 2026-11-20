# Scenario B+ motherboard recovery checkpoint

The verified artwork for this batch is the commit containing [resumed-av-capacitors/verification.json](resumed-av-capacitors/verification.json). Its parent design revision is `d87943fa82f870917cb144d933bf0163d22cdfb4`. The preceding verified artwork is `4f8d88683aea83586f66474429128974cd439b6f`. Resolve the exact batch commit with `git log -1 --format=%H -- audit/implementation/resumed-av-capacitors/verification.json`. Board SHA-256 with LF line endings is `c02253420a958d4cb61ce843464e29e466662fc7cd46a8a9eb24a2d12cfb2650`.

| Current batch | Result |
|---|---|
| Converted positions | C214, C226, C233, C243, C317 |
| KiCad layout status | Verified on implementation/scenario-b-plus |
| ERC | 24 inherited errors and 1182 warnings |
| Refilled DRC | 73 errors and 202 warnings |
| Schematic parity | 17 inherited warnings |
| Connectivity | Zero unrouted. 3603 schematic pins and 3698 physical pad-net records compared. Zero net differences. |
| Physical packages | 120 THT, 434 SMD, 554 total, 21.7% THT |
| Conversion plan | 55 converted positions, 230 planned SMD positions, 34 deferred |

The [deferral register](resumed-cycle/deferred.csv) includes the nine ZS1 resistors, R800, C224 and R109. The batch verification file records individual DRC objects, reference-plane changes, clearances and the fixed mechanical datums. Fabrication release and bench qualification are pending.

Next group: ISA termination branches and Q302 indicator driver.

After an interruption, inspect both worktrees and compare this batch with the GitHub branch before resuming.
