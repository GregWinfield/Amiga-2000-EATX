# Three peripheral interface resistors

| Position | Fitted part | Circuit and measured copper change |
|---|---|---|
| R606 | Vishay MRS16000C1001FCT00, 1 kΩ ±1% | Return resistor of C675's dedicated CN601 bus-grant RC termination. The private junction grew 0.249 mm. The ground escape grew 0.689 mm. The bus-side C675 tap and the 1 µs nominal time constant are preserved. |
| RN204C1 | Vishay MBA0204AC6809FCT00, 68 Ω ±1% | U202 mouse multiplexer output to M0V. Driver-side copper shortened by 0.348 mm, load-side copper grew 0.107 mm. |
| R904 | Vishay MBA0204AC4709FCT00, 47 Ω ±1% | Buster DOE driver to the Zorro slots. Driver-side copper grew 0.006 mm and DOE copper shortened by 0.770 mm. The 15° mounting angle clears the opposite-layer tracks. |

Each resistor is nonpolar and mounts horizontally on 5.08 mm centres in 0.70 mm finished holes. The RF parts use non-helical trim, 0.5 mm nominal wire and a 3.6 × 1.6 mm maximum body. At the 250 mW long-term rating their RMS current limits are 61 mA for 68 Ω and 73 mA for 47 Ω at 70 °C. The 1 kΩ MRS16 dissipates less than 28 mW even with a continuous 5.25 V drop. With a 1 pF incremental terminal load, the 47 Ω and 68 Ω RC sensitivities are 47 ps and 68 ps. Confirm loaded DOE and bus-grant waveforms at the far slot and check the mouse receiver's transitions with its fitted loads. [RF resistor specifications](https://www.vishay.com/docs/28769/mbasmahf.pdf) · [MRS16 ratings and outline](https://www.vishay.com/docs/28724/mrs16m25.pdf)

R606 clears RN903 by 0.145 mm and C675 by 0.161 mm at the courtyards. RN204C1 clears RN200 by 0.176 mm. Check lead forming, socket access and rework on the populated board. The R606 ground land sees same-net In1 copper in all 72 samples on the 1.04 mm ring. Every zone retained its contour count, and each auxiliary inner-rail area matched. No sampled front or bottom route lost its adjacent reference. The new routes have adjacent reference beyond the immediate land clearances. The three positions passed the full netlist, protected geometry and native finding comparisons.

[Converted positions](conversion.csv) · [Route lengths](routing.csv) · [Object-level diagnostics and returns](verification.json) · [All-layer zones](zones.json) · [Native reports](kicad-reports.zip)
