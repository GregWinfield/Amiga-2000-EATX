# Scenario B+ motherboard recovery checkpoint

The verified artwork for this batch is the commit containing [cycle4-isa-termination/verification.json](cycle4-isa-termination/verification.json). Its parent design revision is `40db66db9284a099003aca705bb249b1ef4dbd72`. The preceding verified artwork is `40db66db9284a099003aca705bb249b1ef4dbd72`. Resolve the exact batch commit with `git log -1 --format=%H -- audit/implementation/cycle4-isa-termination/verification.json`. Board SHA-256 with LF line endings is `0878da49af046e73c3a0101db302aa9e84da4a4126804c9f36f741cd27aa3b4c`.

| Current batch | Result |
|---|---|
| Converted positions | C726, C780, C782, C784, C786, C787 |
| KiCad layout status | Verified on implementation/scenario-b-plus |
| ERC | 24 inherited errors and 1182 warnings |
| Refilled DRC | 73 errors and 202 warnings |
| Schematic parity | 17 inherited warnings |
| Connectivity | Zero unrouted. 3603 schematic pins and 3698 physical pad-net records compared. Zero net differences. |
| Physical packages | 147 THT, 407 SMD, 554 total, 26.5% THT |
| Conversion plan | 82 converted positions, 203 planned SMD positions, 41 deferred |

The [deferral register](cycle4/deferred.csv) includes the nine ZS1 resistors, R800, C224 and R109. The batch verification file records individual DRC objects, reference-plane changes, clearances and the fixed mechanical datums. Fabrication release and bench qualification are pending.

Next group: Evaluate conventional expansion bulk capacitors with original supply straps intact.

After an interruption, inspect both worktrees and compare this batch with the GitHub branch before resuming.
