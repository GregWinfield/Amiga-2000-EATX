# Paula audio and video bias

R209 retains the 1.2 kΩ +AUD to Vref resistor. The new pin 1 introduces a local In2 antipad adjacent to its own existing +AUD feed on B.Cu. Twenty-three samples changed at 0.075 mm or finer spacing, confined to the new lead neighbourhood. Copper width and continuity on that feed are unchanged. No other existing back route changes its sampled reference. In1 ground remains continuous underneath the added Vref trace outside its pad clearance. The nearby C219, C242 and R210 service references moved.

R240, R241 and R244 retain the RAWLEFT input, filter node and FLTLEFT termination respectively. The longest addition is 20.47 mm on the 390 Ω FLTLEFT branch. For a conservative additional 30 nH, reactance at 20 kHz is 0.0038 Ω. Two pF of stray capacitance would give a pole above 200 MHz against 390 Ω. These are sensitivities, not measurements of coupling. Use a stereo sweep and noise-floor measurement on a populated board. R203 remains a 10 kΩ _HSYNC bias. Its driver and trunk are unchanged. Check its loaded waveform with the other video signals.

The front-plane sampling changes beneath existing RAWLEFT, C241 and supply tracks are local to the converted pads. All added routes have underlying In1 ground outside the lead neighbourhood. Auxiliary rail areas and all plane contour counts match. The maximum MRS16 and MRS25 body lengths are 3.6 mm and 6.5 mm respectively. [Vishay dimensions](https://www.vishay.com/docs/28724/mrs16m25.pdf)

[Installed positions and pin mapping](conversion.csv) · [Net lengths](routing.csv) · [Verification and fixed datums](verification.json) · [Native KiCad reports and netlists](kicad-reports.zip)
