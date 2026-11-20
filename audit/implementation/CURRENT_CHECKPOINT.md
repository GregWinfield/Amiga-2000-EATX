# Scenario B+ motherboard recovery checkpoint

The verified artwork for this batch is the commit containing [cycle4-expansion-bulk/verification.json](cycle4-expansion-bulk/verification.json). Its parent design revision is `cf2aa43da10fb7900f95da6026e5a89b967bf970`. The preceding verified artwork is `cf2aa43da10fb7900f95da6026e5a89b967bf970`. Resolve the exact batch commit with `git log -1 --format=%H -- audit/implementation/cycle4-expansion-bulk/verification.json`. Board SHA-256 with LF line endings is `9bb85ce6dfbcff218dc30c8a365ca7c9c23700d065ab8d95fd3685341c1c2461`.

| Current batch | Result |
|---|---|
| Converted positions | C412, C416, C419 |
| KiCad layout status | Verified on implementation/scenario-b-plus |
| ERC | 24 inherited errors and 1182 warnings |
| Refilled DRC | 73 errors and 202 warnings |
| Schematic parity | 17 inherited warnings |
| Connectivity | Zero unrouted. 3603 schematic pins and 3698 physical pad-net records compared. Zero net differences. |
| Physical packages | 150 THT, 404 SMD, 554 total, 27.1% THT |
| Conversion plan | 85 converted positions, 200 planned SMD positions, 41 deferred |

The [deferral register](cycle4/deferred.csv) includes the nine ZS1 resistors, R800, C224 and R109. The batch verification file records individual DRC objects, reference-plane changes, clearances and the fixed mechanical datums. Fabrication release and bench qualification are pending.

Next group: Verify the ISA bypass and termination pair and the shared bus-error pull-up.

After an interruption, inspect both worktrees and compare this batch with the GitHub branch before resuming.
