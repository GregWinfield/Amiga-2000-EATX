# Scenario B+ motherboard recovery checkpoint

The verified artwork for this batch is the commit containing [cycle4-audio-filter/verification.json](cycle4-audio-filter/verification.json). Its parent design revision is `512318fa852343f8a57f2011ad02786bbeb48717`. The preceding verified artwork is `512318fa852343f8a57f2011ad02786bbeb48717`. Resolve the exact batch commit with `git log -1 --format=%H -- audit/implementation/cycle4-audio-filter/verification.json`. Board SHA-256 with LF line endings is `858bb48c87e077e4a65bc501629a8bc433eb83d48cb7b2e3cb48e9b4c62a1185`.

| Current batch | Result |
|---|---|
| Converted positions | C232, R231 |
| KiCad layout status | Verified on implementation/scenario-b-plus |
| ERC | 24 inherited errors and 1182 warnings |
| Refilled DRC | 73 errors and 202 warnings |
| Schematic parity | 17 inherited warnings |
| Connectivity | Zero unrouted. 3603 schematic pins and 3698 physical pad-net records compared. Zero net differences. |
| Physical packages | 157 THT, 397 SMD, 554 total, 28.3% THT |
| Conversion plan | 92 converted positions, 193 planned SMD positions, 52 deferred |

The [deferral register](cycle4/deferred.csv) includes the nine ZS1 resistors, R800, C224 and R109. The batch verification file records individual DRC objects, reference-plane changes, clearances and the fixed mechanical datums. Fabrication release and bench qualification are pending.

Final cycle 4 verified KiCad artwork is `9f42a84b01259dd6c112fab168786e06c2e8e8ea`. [Cycle report](cycle4/README.md) · [Reconciliation](cycle4/cycle-check.json) · [Engineering holds](cycle4/deferred.csv). The next independent trial is the C811 RTC reservoir. After an interruption, compare both branch tips with GitHub before resuming.
