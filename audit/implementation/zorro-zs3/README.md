# ZS3 termination group

The 5 independent 1 kΩ branches share ground at pin 1 of a Bourns 4606X-101-102LF. Each capacitor retains its original signal, connector contact and private return. Pin 1 is at (117.480, 267.250) mm. The new private F.Cu paths range from 3.601 to 7.245 mm. All 1,211 vias retain their net and geometry. [Branch manifest](conversion.csv) · [Per-net routed lengths](routing.csv)

## Fit and routing

ZS3 sits between CN605 and the installed ZS2. Eight 0805 capacitors moved 1.15 mm toward CN605. Their BA12–BA19 termination taps shortened by 0.47–1.17 mm, including the revised BA19 approach around C645. The longest of the four adjacent ZS2 private connections is 8.560 mm. All nine private connections remain on F.Cu. Twelve underside signals use local escapes, with at most 0.068 mm displacement at the SIP centreline. The original E and _VMA copper remains intact. A candidate at y = 272.075 mm incurred a BA18/BA19 short and 31 clearance violations. At the installed position the original nine ZS2 branches and all five ZS3 branches verify electrically. The local In1 zone has a 0.25 mm thermal gap to keep copper beneath the C633 approach to ZS2.8.

The maximum six-pin body is 15.19 × 2.49 × 5.08 mm. The two SIP centrelines are 3.26 mm apart, leaving 0.77 mm between maximum-width centred bodies and 0.050 mm between courtyards. The shifted capacitor courtyards approach the CN605 courtyard to 0.011 mm. These are nominal CAD dimensions. Straight card insertion passes above a seated SIP with 10.42 mm to the nominal socket top. Fit the adjacent capacitors before the SIP and sockets. Confirm part tolerance, tilted-card clearance, cap rework, access from below and underside lead trim on a populated witness. [Bourns package drawing](https://bourns.com/docs/Product-Datasheets/4600x.pdf) · [TE socket drawing](https://www.te.com/en/product-5645235-3.html)

The measured nominal spacing translates to 0.206 mm for the closest trace pair and 0.205 mm to a SIP land at ±0.020 mm track width and ±0.040 mm diametric land tolerance, before additional positional errors. Supplier guarantees and sample measurements are still required.

## Plane and manufacturing checks

The refilled In2 +5 V region covers the sampled centrelines of every affected underside signal. Samples along the expanded test window used at most 0.025 mm spacing. The +5 V total across individual pin pitches at the drill centreline measures 0.535–0.535 mm. Ground copper reaches the common barrel on In1. The detailed report also gives the F.Cu route lengths above filled In1 copper and above local antipads. Board registration, return-current spreading and loaded signal behaviour require physical validation. [Fill and clearance measurements](verification.json)

Standard 1.60 mm rear lands leave 0.94 mm per gap. Paired 0.20 mm traces with three 0.20 mm spaces need 1.00 mm. This placement uses 1.40 mm rear lands with 1.60 mm lands on the remaining layers, 2.54 mm pitch and 0.80 mm finished bores. The minimum measured rear trace spacing is 0.2260 mm between edited 0.22 mm segments and 0.2260 mm to the comparison copper. Trace-to-land clearance is 0.2350 mm and trace-to-mask-opening clearance is 0.1850 mm. Nominal rear and inner rings are 0.300 and 0.400 mm. A 0.94 mm preplate tool, 0.040 mm diametric land loss and 0.060 mm radial registration leave 0.150 and 0.250 mm respectively. Obtain CAM confirmation of finished copper widths, minimum gaps, layer overlay and finished bores, then check barrel fill, wetting and insertion on a witness. [Reviewed tolerance stack](../zorro-zs2/README.md)

## Baseline comparison

The control is `86c9236`. ERC retains 24 errors and 1,182 warnings. DRC retains 73 errors and 202 warnings, with zero opens and 17 inherited schematic-parity warnings. The comparison checks the complete logical map across 3,617 control and 3,613 evaluated assignments. Physical pad-net records change from 3,712 to 3,708 through intentional consolidation. The four-layer stack, outline and 54 fixed connector and mounting references match. Hardware qualification and fabrication remain on hold. [Object-level differences](verification.json) · [Raw KiCad reports](kicad-reports.zip)

This batch contains 75 THT and 490 SMD in 565 physical packages (13.3% THT).
