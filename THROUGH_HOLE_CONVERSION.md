# Amiga 2000 EATX through-hole conversion review

**Review decision, 20 November 2026.** Start with the radial bulk capacitors, selected axial resistors and small-signal devices. Of 584 component positions, 65 already use through-hole pads. The review identifies 151 further candidates. Even if every candidate passes, the board reaches **216/584 through-hole positions (37.0%)**. A majority would require qualifying at least 77 additional positions. The principal constraint is the pair of dense termination banks alongside the expansion slots. The design evidence supports a mixed-technology motherboard at this stage.

Phases 1 and 2 are ready for review. The baseline is GregWinfield/Amiga-2000-EATX `main` at `dfde4574396919e9cc51f5079ef054e4de3b9a07`, also the author’s upstream revision when checked. The working branch is `feature/through-hole-conversion`. This packet contains analysis and proposed substitutions. Schematic, layout, libraries, rules, shopping list and fabrication artwork remain at the baseline revision. [Pinned project](https://github.com/GregWinfield/Amiga-2000-EATX/tree/dfde4574396919e9cc51f5079ef054e4de3b9a07)

## Inventory and proposed disposition

Counts use component positions, including mutually exclusive assembly options. Of 614 board footprints, 17 are etched configuration jumpers, 11 are mounting holes and two are graphics. Those 30 do not count toward assembly technology. The 65 leaded positions include the 25 SIP networks and the through-hole socket for the PLCC Agnus. The case supplies the power LED. There is no motherboard SMD LED or SMD external connector to replace.

| Category | Original SMD | Converted to THT | Proposed THT | Retained SMD in plan | Reason |
|---|---:|---:|---:|---:|---|
| Resistors | 152 | 0 | 63 | 89 | Axial bias, pull-up and audio resistors are candidates. Preserve bus terminations, damping and confined back-side sites. |
| Capacitors | 293 | 0 | 52 | 241 | Trial 31 radial electrolytics and 21 ceramics. Retain feedthroughs, termination banks and sensitive bypass or timing loops. |
| Diodes | 7 | 0 | 1 | 6 | D300 has an axial counterpart. Other sites involve rectifier identification, battery leakage or underside clearance. |
| Transistors | 7 | 0 | 4 | 3 | Four BJTs have TO-92 candidates. Keep the paired audio JFETs and underside ATX driver. |
| Logic ICs | 33 | 0 | 26 | 7 | Same-family DIPs are available for review. Clock selection, SRAM timing and back-side standby logic constrain seven sites. |
| Other | 27 | 0 | 5 | 22 | Trial the audio op amp, comparator, two serial interfaces and reset supervisor. Retain SRAM, RTC option, fuses, ferrites, regulator and frequency references. |
| **Total** | **519** | **0** | **151** | **368** | Each of the 519 SMD positions has its own disposition and rationale. |

The component register is the **planning BOM**, with one row per board reference, original value, sheet, board face, position, existing footprint, proposed library footprint, candidate specification, pin mapping and electrical checks. Filter `decision` for the proposed substitutions or retained SMD list. The pad register supplies the exact nets where the rationale refers to a signal or supply. [Component register](audit/component-plan.csv) · [PCB pad register](audit/baseline/pcb-pads.csv)

## Phase 1 — source and connectivity baseline

The motherboard is `2000EATX-KiCAD-R31/2000ATX`, revision **3.1**, dated 2 June 2024. The hierarchy has a root and 13 child sheets. The PCB format is 20240108 and schematic format is 20231120. Both identify generator 8.0. The released Gerber header identifies **Pcbnew 8.0.2-8.0.2-0~ubuntu23.10.1**. The exact schematic-writer patch is not recorded in its header. This audit used **KiCad 10.0.8**. Future deltas should use the same checker, library versions and options, or establish a second baseline before comparison.

The project includes a local footprint library, Amiga and rescue symbol libraries, upstream shopping CSV, interactive BOM, schematic PDF, Gerbers and drills, mechanical STLs, datasheets, assembly notes and user guide. Three separate TICK accessory board designs are outside the motherboard population. The motherboard uses the settings in its project file and has no project-specific .kicad_dru file. The bundled 2000ATX.xml identifies the older R12 schematic and Eeschema 5.1.6. The comparison here uses a fresh hierarchical export. [Design files](2000EATX-KiCAD-R31) · [Released BOM](BOM) · [Fabrication package](Gerber) · [Assembly notes](AssemblyNotes.md)

| Connectivity check | Baseline observation |
|---|---|
| Schematic | 612 referenced items, 858 named nets and 3,631 reference/pin-to-net assignments. |
| PCB | 3,726 physical pads, including repeated pad numbers. All 3,631 assignments match the PCB net name on the corresponding reference and pad. |
| Extra PCB pads | 20 distinct reference/pad keys have no assigned board net. Four extra keys represent 14 GND shell or mounting lands numbered 0 on CN200, CN202, CN300 and CN305. Preserve these contacts explicitly. |
| Routing | 7,340 front, 6,207 back, 58 In1 and 135 In2 trace objects, plus 1,212 vias. Zero unconnected items reported by DRC. |
| Future comparison | Compare physical terminal function, net membership and connector pad locations. For a verified package remap such as a 3904, compare B/E/C by function and document the intentional pad-number change. |

The full schematic export and per-pad table permit independent comparisons of connector pins, memory byte lanes, enables, interrupt lines, DMA and power. The XML source filename is project-relative for portability. A net-name match establishes agreement between these two files. Timing, symbol pin semantics and the accuracy of the original circuit require independent evidence. [Schematic netlist](audit/baseline/schematic.xml) · [PCB pads and coordinates](audit/baseline/pcb-pads.csv)

### Baseline ERC and DRC

| Check | Errors | Warnings | Observations |
|---|---:|---:|---|
| Schematic ERC | 24 | 1,182 | Eight pin-type conflicts, seven inputs without a driver and nine power pins without a driver. |
| PCB DRC | 85 | 202 | All errors are incomplete thermal reliefs. Warnings comprise 199 library footprint differences, two silkscreen overlaps and one mirrored front-side text item. |
| PCB/schematic parity, reported separately | 0 | 17 | Fourteen grounded pad-0 lands have no schematic pin. Three Datasheet fields differ in whitespace. |
| Modified run | — | — | Deferred until a reviewed conversion is implemented. |

ERC flags include CPU/Gary address pins declared as outputs at both ends and the shared X1/X2 oscillator output. X1/X2 are alternate populations. Check address-bus direction against chip documentation and check jumper-dependent inputs under each intended build. The 987 pin-to-pin warnings and 88 library symbol differences are recorded individually. An inherited warning cannot establish that a proposed DIP is interchangeable.

The 85 thermal findings break down as 51 on front GND, 29 on back GND, four on internal GND and one on internal +5 V. CN202 GND pad 5, for example, has one back-side thermal spoke where the zone calls for two. Inspect the available parallel current paths and solderability where a proposed drill approaches any of these pads. The reports include inherited ignored checks, including missing courtyards. Source exclusions and rule settings were preserved. [Full ERC](audit/baseline/erc.json) · [Full DRC and parity](audit/baseline/drc.json)

To reproduce in a disposable checkout with the KiCad libraries installed, run from the repository root. The DRC command uses the stored copper fill. Archive a separate in-memory refill result when comparing an edited layout. KiCad can write local project preferences while checking.

```sh
kicad-cli sch erc --format json --severity-all -o audit/baseline/erc.json 2000EATX-KiCAD-R31/2000ATX.kicad_sch
kicad-cli pcb drc --format json --severity-all --schematic-parity -o audit/baseline/drc.json 2000EATX-KiCAD-R31/2000ATX.kicad_pcb
kicad-cli sch export netlist --format kicadxml -o audit/baseline/schematic.xml 2000EATX-KiCAD-R31/2000ATX.kicad_sch
```

### Existing differences from Commodore Rev 6.x

The author identifies Rev 6.2 as the design ancestor. The original Rev 6 system schematics and parts list are available for cross-checking. The bundled Commodore PCB schematic PDF is marked Rev 4. A complete net-by-net historical equivalence certification would also require the applicable Rev 6.x ECOs and a defined donor revision. [Commodore Rev 6 system schematics](https://amiga.net.au/files/Tech_Amiga/Commodore_System_Schematics_A2000_Revision_6_ocr.pdf) · [Upstream design history](README.md)

| Area | Existing Rev 3.1 implementation to preserve |
|---|---|
| CPU, chipset and chip RAM | 68000, Gary, Buster, Paula, Denise and socketed Agnus. Configurable Agnus wiring supports several revisions. SRAM and its address/control logic replace the original DRAM bank. J503 defaults to the 5 V SRAM option. |
| Boot and RTC | The 42-pin Kickstart socket accommodates the original 40-pin ROM and larger EPROM options. U899 with crystal and trimmer or U801 with integral crystal implements the RTC. |
| Expansion | Five Zorro II positions, three 16-bit ISA positions, a relocated CPU slot and a two-connector video slot. The card order and bracket arrangements differ from the Commodore chassis. |
| Video and audio | HD15 carries selected analogue RGB and sync signals. External composite video is omitted. Audio uses a stereo jack. Preserve the full internal video slot and separate analogue return. |
| Disk and serial | External drives use a header and adapter. The internal serial port is omitted and external serial is retained. Stacked rear connectors establish the EATX I/O geometry. |
| Power, reset and timing | ATX standby/soft power, on-board negative regulator, case reset, optional external TICK and the default VSYNC-derived TICK replace the original PSU arrangement. X1 and X2 support alternative TTL and CMOS oscillators. |

### Mechanical and plane constraints

The released profile centreline measures **304.800 × 330.200 mm**. The board is 1.6 mm thick with four copper layers. Use the 11 mounting-hole coordinates and connector anchors from the register as datums. H8 is absent. In1 carries GND and routed signals. In2 has separate +5 V, −5 V, −12 V and +12 V pours as well as traces. Both outer faces carry GND pours. There are seven board zones and no board-level rule-area zones in the loaded design. The absence of a drawn rule area provides no card-height clearance. [Layer specification](PCB.md) · [Board and bracket clearance](userguide.md) · [Bracket models](STL)

The default, GND1 and PWR1 classes specify 0.20 mm clearance. PWRBIG specifies 0.40 mm. Minimum hole-to-hole and hole-to-copper settings are 0.25 mm, minimum track width 0.20 mm and minimum resolved thermal spokes two. Every new through-hole pad cuts an antipad in unrelated planes. Check the narrow copper webs on both inner layers at actual fabrication clearances, especially between adjacent DIP rows, slot power pins and plane boundaries. Confirm continuous return copper under clock, memory and bus traces after refill.

The guide gives approximately 21 mm between the planes of the CPU and video cards. It also lists up to 337.19 mm for a Zorro card, 356 mm for a CPU card and 210 mm for a video card. Full-length cards, adapters, protruding solder tails, heatsinks, socket extraction space and rear I/O shield engagement all need checking in the actual case. The baseline has 28 SMD components and 14 etched jumpers on the back. Preserve access around Agnus and the ATX standby circuit. [Mechanical guide](userguide.md)

## Phase 2 — substitution and placement plan

**First review group.** C402–C406 and C420–C422 are 47 µF bulk positions. Their candidate radial footprints passed the limited placement screen. R111, R201 and R803 provide early axial trials. D300, Q300, Q301 and Q302 provide polarity and transistor pin-map checks. XU1 offers a same-function TO-92 reset supervisor. Start with these positions after review, retaining each reference and net. Compare the actual radial body height and finished lead diameter against the connector envelope and drill chart before committing placement.

**Layout-intensive group.** U600 in a 20-pin DIP intersects the CN600 CPU slot envelope at its existing centre and approaches two drilled features. U207 intersects HY200 and approaches the internal +VID trace. R310 intersects C313, D301 and U305 and approaches both ±12 V tracks. U303 clears current neighbours in its screened orientation but overlaps the independently proposed U205 envelope. Resolve these as local placement groups before approving their net escape. A socket adds height, lead inductance and contact resistance and needs its own review. [Placement results for all 151 candidates](audit/placement-screen.csv)

**Placement method.** Each trial uses the installed KiCad THT library footprint centred on the original footprint’s bounding box, on the front face. Four right-angle orientations were tested. The recorded rotation is counterclockwise in mathematical coordinates applied to board X/Y, with board Y increasing down the page. Ranking first minimises current front-side body/edge conflicts, then drill conflicts, then distinct nearby inner-layer track/net pairs. Original and trial body boxes exclude fields. The drill test uses the existing via/pad drill plus 0.25 mm separation. The track test uses a circumscribed candidate pad, existing track width and a nominal 0.20 mm gap. The resulting trial boxes were also compared pairwise.

Of 151 sites, 94 have a hit against existing geometry in their best orientation and 57 have none in that screen. Of those 57, **47** also avoid all other selected trial envelopes. This assessment omits outer-layer routing, plane refill, full pad-to-pad clearance, exact 3D bodies and per-net clearance. A check against rectangular boxes can also overstate interference. These results rank placement work. Detailed DRC and actual component envelopes determine fit.

**Expansion termination study.** We separately screened 47 Zorro 1 kΩ/1 nF series RC pairs and 44 ISA 1 nF positions using DIN0207 on 10.16 mm centres and 5 mm radial ceramic bodies. Of the 138 trial positions, 137 hit existing geometry. All 138 overlap at least one other proposed body in those compact banks. Keep the existing terminations in the initial plan. If a majority remains essential, study re-placement of a complete termination bank with unchanged values and endpoint topology. Compare slot-to-termination stub length, loaded-edge settling, ringing and return paths against an instrumented Rev 3.1 board before extending that layout across the bus. A working mixed-technology design remains the fallback. [Termination study by reference](audit/termination-feasibility.csv)

### Component qualification

| Family | Candidate and evidence | Qualification still needed |
|---|---|---|
| Axial resistors | Vishay MRS25 spans the relevant 1 Ω–470 kΩ values, ±1%, 50 ppm/K and 0.6 W at 70 °C. Maximum body 6.5 × 2.5 mm, 0.6 mm nominal lead, minimum formed pitch 10 mm. Use the 10.16 mm DIN0207 trial. | Confirm exact order code/tolerance per value. R310 and R914 explicitly require 0.5 W. Check surge, ambient derating and heat near capacitors. A 7.62 mm pitch requires a part permitting that bend. [Manufacturer drawing](https://www.vishay.com/docs/28724/mrs16m25.pdf) · [Stocked 10 kΩ example](https://www.digikey.com.au/en/products/detail/vishay-beyschlag-draloric-bc-components/MRS25000C1002FCT00/5063978) |
| Radial electrolytics | The register gives a Panasonic order code for each of 4.7, 22, 47, 220 and 470 µF. Trial pitches are 2, 3.5 and 5 mm. The 47 µF part has a 5 mm body and may stand 12.5 mm high. | Source BOM omits voltage, ESR, ripple rating and temperature range for these sites. Establish original minimums, check leakage on audio/reset nodes and measure rail transients. Positive pad 1 can be ground on a negative rail, e.g. C408. [Panasonic 47 µF](https://na.industrial.panasonic.com/products/capacitors/aluminum-electrolytic-capacitors/lineup/aluminum-electrolytic-capacitors-radial-lead-type/series/83367/model/83711) · [Availability and height](https://www.digikey.com.au/en/products/detail/panasonic-industry/EEU-FR1E470/2433545) |
| Radial ceramics | Use the original capacitance and short leads. A 100 nF example is KEMET C315C104K5R5TA, ±10%, X7R, 50 V, 2.54 mm nominal pitch. | The source omits dielectric/tolerance for most ceramics. Verify effective capacitance and lead span. The generic disc footprint is a trial envelope. Match the final coating/body drawing. On Paula, verify both channel responses. [KEMET part listing](https://www.digikey.com.au/en/products/detail/kemet/C315C104K5R5TA/12701330) |
| Diodes and BJTs | D300 uses 1N4148 in DO-35, cathode band to pad 1. Four MMBT3904/3906 sites can use 2N3904/3906 TO-92 candidates. The existing B/E/C pad sequence 1/2/3 maps to new leads 2/1/3. | Check actual emitter/collector orientation, gain and dissipation at load. Preserve switching characteristics and diode surge/recovery. [DO-35 drawing](https://www.vishay.com/docs/81857/1n4148.pdf) · [NPN pinout](https://www.onsemi.com/download/data-sheet/pdf/2n3904-d.pdf) · [PNP pinout](https://www.onsemi.com/download/data-sheet/pdf/2n3906-d.pdf) |
| Logic and interfaces | Individual candidate TI order codes appear in the register. A DIP 74HCT08 and 74AHCT244 exist in their respective families. Preserve open-collector behaviour for 74LS38 and LM339. Retain the SRAM and its FCT registers. | Compare each package pin including enables, supply range, VIH/VIL, loaded VOH/VOL, I/O currents, worst-case delays and disable timing. Capture DMA and Zorro turnaround under load. [HCT08](https://www.ti.com/product/SN74HCT08/part-details/SN74HCT08N) · [AHCT244](https://www.ti.com/product/SN74AHCT244) |
| Reset, audio and RTC | DS1813-5+ has 1 RESET, 2 VCC, 3 GND in both packages. Keep threshold grade and reset timing. LF347N/NOPB provides a DIP evaluation option. Prefer the existing U899 DIP assembly for the original RTC circuit. | Verify the TO-92 bottom-view drawing, analogue inputs against physical LF347 pin numbers, RTC population and oscillator start-up. Preserve both original RTC choices. [DS1813 pin table](https://www.analog.com/media/en/technical-documentation/data-sheets/DS1813.pdf) · [LF347 DIP](https://www.ti.com/product/LF347-N/part-details/LF347N/NOPB) |

Manufacturer listings establish package families. The component register links exact examples where substantiated. The stock checks are snapshots. Tolerance, temperature, bias, thermal margins and lot availability are open where the source provides only a value. Treat the register as a review BOM until those limits and a fitted variant are recorded. Original Buster, Agnus, CIAs, Paula, Denise, Gary, Kickstart and the legacy RTC/oscillator options have donor or legacy sourcing constraints. [Legacy parts and population options](AssemblyNotes.md)

### Outstanding issues affecting the review

- **ISA slot fit.** The measured A1-to-B1 row spacing at CN700, CN701 and CN702 is **4.8514 mm**. The upstream issue cites a 5.08 mm connector drawing, a 0.2286 mm difference from the board measurement. Verify the exact purchased connector, tail tolerances and fit on a sample. Preserve the baseline datum pending any separate correction. [Upstream issue 45](https://github.com/jasonsbeer/Amiga-2000-EATX/issues/45)
- **U204 audio symbol.** The author reports that the B and D symbol input signs are incorrect while the physical wiring is correct. The baseline labels pin 5 minus and 6 plus, and pin 12 minus and 13 plus. The LF347 uses 5/12 non-inverting and 6/13 inverting. Preserve physical pad nets and reconcile symbol labels independently before changing package. [Upstream issue 41](https://github.com/jasonsbeer/Amiga-2000-EATX/issues/41) · [TI pin drawing](https://www.ti.com/lit/ds/symlink/lf347-n.pdf)
- **Purchasing discrepancies.** The shopping CSV calls for 18 × 47 µF electrolytics. The layout contains 12. D200, D301, D400 and D401 are labelled S1MWF-7 while the shopping code identifies RS1MWF-7. The former is listed as obsolete. Verify the built-board part and allowable recovery class before selecting any axial substitute. F3/F4 have generic board values and need the exact protection specification. [Source shopping list](BOM/A2000EATX-REV31-ShoppingList.csv) · [S1MWF manufacturer record](https://www.diodes.com/part/view/S1MWF)
- **Power and memory options.** J503 has +5 V, Mcc and +3V3 on pads 1, 2 and 3, with a factory 1–2 bridge. Confirm resistance before powering any alternate SRAM build. Upstream reports ATX supply-dependent startup and AHCT wide-package sourcing difficulty. Keep these items visible during bring-up and purchasing. [J503 discussion](https://github.com/jasonsbeer/Amiga-2000-EATX/issues/44) · [Power supply report](https://github.com/jasonsbeer/Amiga-2000-EATX/issues/42) · [Logic package sourcing](https://github.com/jasonsbeer/Amiga-2000-EATX/issues/40)
- **Population-dependent pin use.** The assembly notes describe X1 pin 1 as disconnected. The released PCB assigns it to Net-(X1-Enable) and RX1 connects that net to +5 V through 4.7 kΩ. Verify the chosen oscillator’s pin-1 function and populate only X1 or X2. Preserve the Agnus jumper map and TICK source for each build. [Assembly instructions](AssemblyNotes.md) · [Measured pad assignments](audit/baseline/pcb-pads.csv)

## Verification and fabrication release after review

- [ ] Approve the component groups and document actual fitted SMD parts or equivalent design limits. Resolve footprint pin maps, ratings and heights against exact lead forms. Obtain separate approval for any functional ECO.
- [ ] After approved edits, run ERC and DRC with parity, compare the detailed findings by reference and location, and compare all schematic pins and physical board pads to the baseline. Verify connector and shell nets independently. Record every exception.
- [ ] Refill all four copper layers, inspect each new hole at ground/power boundaries, review the 85 baseline thermal findings, and measure continuity and loaded voltage drop at distant slot contacts.
- [ ] Compare rail ripple and reset timing during power-up. Check ROM boot, chip RAM and DMA, interrupts, Zorro/CPU expansion under load, external clock and TICK, RGB/sync, both audio channels and serial/floppy operation under the intended variants.
- [ ] Check a 1:1 print or mechanical coupon, mounted card/bracket alignment, rear I/O, socket access, radial capacitor height and underside solder clearance. Confirm the ISA connector drawing and fit.
- [ ] Review final plotted drills, outline, silk polarity/pin-1 legends and mask. Specify traditional green mask, white silk and appropriate connector finishes. The motherboard uses receptacles for the expansion cards. Specify hard gold only for an actual mating board-edge contact. Preserve existing attribution.
- [ ] Release modified KiCad design, assembly BOM and new manufacturing files only after the electrical, mechanical and assembly review. The checked-in Gerbers describe the upstream R3.1 board.
