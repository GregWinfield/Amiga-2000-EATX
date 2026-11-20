# ZS4 termination group

The 5 independent 1 kΩ branches share ground at pin 1 of a Bourns 4606X-101-102LF. Each capacitor retains its original signal, connector contact and private return. Pin 1 is at (120.790, 297.995) mm. The new private F.Cu paths range from 5.529 to 7.260 mm. All 1,211 vias retain their net and geometry. [Branch manifest](conversion.csv) · [Per-net routed lengths](routing.csv)

## Slot-side placement

The five capacitors and their signal-side taps retain their positions. R604A1, R604B1 and R604E1 moved within their original termination strip and keep independent return nodes. Fourteen bottom-layer signals use the local escape. The largest added through-bus length is 0.2494 mm on BA23. The BA21/BA22 approaches fan before the SIP and rejoin their original slot routes. A separate site beyond CN604 admitted five routes with 108.7 mm of total private copper, compared with 30.23 mm here. The first near-side placement produced BA21/BA22 shorts. Both problems were resolved in the installed layout.

The six-pin maximum body measures 15.19 × 2.49 × 5.08 mm. The nearest SIP courtyard gaps are 0.071 mm to CN604, 0.230 mm to R604A1 and 0.946 mm to the H7 courtyard bounding box. Nominal side clearance from the centred maximum-width body to the CN604 housing is approximately 0.85 mm. The socket top stands 10.42 mm above the seated SIP. Fit the small parts first and inspect lead trim, pick-up clearance, near-side solder access and actual card withdrawal on the witness. [Bourns drawing](https://bourns.com/docs/Product-Datasheets/4600x.pdf) · [TE connector](https://www.te.com/en/product-5645235-3.html)

At ±0.020 mm finished track width and ±0.040 mm diametric land tolerance, the closest changed-to-existing copper and trace-to-land gaps calculate to approximately 0.202 and 0.202 mm before further positional error. This is a provisional layout condition. A supplier must guarantee final widths, spaces and registration in writing. Changes to the granted escape geometry require another board comparison.

## Plane and manufacturing checks

The refilled In2 +5 V region covers the sampled centrelines of every affected underside signal. Samples along the expanded test window used at most 0.025 mm spacing. The +5 V total across individual pin pitches at the drill centreline measures 0.535–0.535 mm. Ground copper reaches the common barrel on In1. The detailed report also gives the F.Cu route lengths above filled In1 copper and above local antipads. Board registration, return-current spreading and loaded signal behaviour require physical validation. [Fill and clearance measurements](verification.json)

Standard 1.60 mm rear lands leave 0.94 mm per gap. Paired 0.20 mm traces with three 0.20 mm spaces need 1.00 mm. This placement uses 1.40 mm rear lands with 1.60 mm lands on the remaining layers, 2.54 mm pitch and 0.80 mm finished bores. The minimum measured rear trace spacing is 0.2242 mm between edited 0.22 mm segments and 0.2224 mm to the comparison copper. Trace-to-land clearance is 0.2320 mm and trace-to-mask-opening clearance is 0.1820 mm. Nominal rear and inner rings are 0.300 and 0.400 mm. A 0.94 mm preplate tool, 0.040 mm diametric land loss and 0.060 mm radial registration leave 0.150 and 0.250 mm respectively. Obtain CAM confirmation of finished copper widths, minimum gaps, layer overlay and finished bores, then check barrel fill, wetting and insertion on a witness. [Reviewed tolerance stack](../zorro-zs2/README.md)

## Baseline comparison

The control is `5195fc4`. ERC retains 24 errors and 1,182 warnings. DRC retains 73 errors and 202 warnings, with zero opens and 17 inherited schematic-parity warnings. The comparison checks the complete logical map across 3,613 control and 3,609 evaluated assignments. Physical pad-net records change from 3,708 to 3,704 through intentional consolidation. The four-layer stack, outline and 54 fixed connector and mounting references match. Hardware qualification and fabrication remain on hold. [Object-level differences](verification.json) · [Raw KiCad reports](kicad-reports.zip)

This batch contains 76 THT and 485 SMD in 561 physical packages (13.5% THT).
