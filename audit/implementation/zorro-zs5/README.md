# ZS5 termination group

The 8 independent 1 kΩ branches share ground at pin 1 of a Bourns 4610X-101-102LF. Each capacitor retains its original signal, connector contact and private return. Pin 1 is at (117.540, 305.020) mm. The new private F.Cu paths range from 2.927 to 5.071 mm. All 1,211 vias retain their net and geometry. [Branch manifest](conversion.csv) · [Per-net routed lengths](routing.csv)

## Capacitor taps and card clearance

Eight returns now use pins 2–8 and 10. The spare pin 9 has an explicit no-connect. Four 0805 capacitors (C657, C662, C663 and C661) sit east of the SIP with their pads rotated through 90°. Eight others moved within the western strip. Their capacitance and signal assignments are unchanged. The new arrangement keeps both the R604 axial and every segment of the E7M clock in their accepted positions. A trial moving R604 south shorted its ground pin to E7M. A single western row of capacitors also shorted signal-side taps. Neither trial was installed.

Nineteen B.Cu nets were checked around the new pin row. The through-bus remains on B.Cu. The cost of keeping its topology and every original via is additional branch copper on four signal-side taps. Whole-net increases are 8.35 mm on _BAS, 8.88 mm on BD11, 9.20 mm on BD13 and 9.36 mm on _BUDS. The report separates the actual front-layer lengths from the adjacent-reference checks. Check loaded receiver overshoot, settling, setup/hold and SIP-ground bounce on these four signals in particular. Compare near and far slots against the accepted discrete layout. No measured timing margin is available.

The maximum Bourns body is 25.35 × 2.49 × 5.08 mm. The 3.19 mm separation between the ZS5 and ZS6 lead rows leaves about 0.70 mm between centred maximum-width bodies. The nearest courtyard polygon edges are 0.080 mm apart at ZS6 and 0.136 mm at R604. Insert the SMD capacitors before the SIP and sockets, then verify card overhang, angled extraction, hand soldering and lead trim on actual hardware. [Bourns drawing](https://bourns.com/docs/Product-Datasheets/4600x.pdf) · [TE connector](https://www.te.com/en/product-5645235-3.html)

The tightest nominal rear copper and land gaps leave about 0.201 mm in each case after the reviewed ±0.020 mm track-width and ±0.040 mm diametric land tolerances, before further positional allowance. The square common-pad mask corner approaches READ to 0.166 mm. Written guarantees for actual line/space, mask registration and residual rings are essential. If the process cannot guarantee those dimensions, reopen the escape rather than issuing production artwork.

## Plane and manufacturing checks

The refilled In2 +5 V region covers the sampled centrelines of every affected underside signal. Samples along the expanded test window used at most 0.025 mm spacing. The +5 V total across individual pin pitches at the drill centreline measures 0.535–0.535 mm. Ground copper reaches the common barrel on In1. The detailed report also gives the F.Cu route lengths above filled In1 copper and above local antipads. Board registration, return-current spreading and loaded signal behaviour require physical validation. [Fill and clearance measurements](verification.json)

Standard 1.60 mm rear lands leave 0.94 mm per gap. Paired 0.20 mm traces with three 0.20 mm spaces need 1.00 mm. This placement uses 1.40 mm rear lands with 1.60 mm lands on the remaining layers, 2.54 mm pitch and 0.80 mm finished bores. The minimum measured rear trace spacing is 0.2210 mm between edited 0.22 mm segments and 0.2263 mm to the comparison copper. Trace-to-land clearance is 0.2310 mm and trace-to-mask-opening clearance is 0.1659 mm. Nominal rear and inner rings are 0.300 and 0.400 mm. A 0.94 mm preplate tool, 0.040 mm diametric land loss and 0.060 mm radial registration leave 0.150 and 0.250 mm respectively. Obtain CAM confirmation of finished copper widths, minimum gaps, layer overlay and finished bores, then check barrel fill, wetting and insertion on a witness. [Reviewed tolerance stack](../zorro-zs2/README.md)

## Baseline comparison

The control is `476f802`. ERC retains 24 errors and 1,182 warnings. DRC retains 73 errors and 202 warnings, with zero opens and 17 inherited schematic-parity warnings. The comparison checks the complete logical map across 3,609 control and 3,603 evaluated assignments. Physical pad-net records change from 3,704 to 3,698 through intentional consolidation. The four-layer stack, outline and 54 fixed connector and mounting references match. Hardware qualification and fabrication remain on hold. [Object-level differences](verification.json) · [Raw KiCad reports](kicad-reports.zip)

This batch contains 77 THT and 477 SMD in 554 physical packages (13.9% THT).
