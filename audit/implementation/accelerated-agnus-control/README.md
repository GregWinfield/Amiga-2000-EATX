# Agnus configuration and peripheral pull-ups

R101 mounts on the front beside U101. A 4.169 mm back trace connects its 4.7 kΩ pull-up to J102, and its supply barrel connects directly to +5 V. The J102-to-U101 trunk is unchanged. Its courtyard clears U101 by 0.030 mm and FB101 by 0.443 mm. Check actual socket overhang and extraction-tool clearance. R109 remains underneath the socket. Neither the underside land nor the JA1-side search yielded a clear front body and local connection within the 40.64 mm window.

R1000 biases _VPA, R217 biases _XCLKEN, R301 biases floppy _DKRD and R601 biases DOE. Five superseded local segments were removed. All vias and unrelated tracks are preserved. The 7.149 mm DOE branch adds about 43–50 ps one-way at an assumed 6–7 ps/mm. It retains adjacent ground outside its pad clearance. The sampled changes on existing front tracks are on _DKRD and _XCLKEN at their own new leads. The new _DKRD branch crosses 0.99 mm without immediate ground beyond the pad neighbourhood. No sampled preserved back route changes reference. Auxiliary rail areas and all contour counts match. FB101 has a relocated service reference and R917 has its value on F.Fab. Loaded waveform and mechanical validation remain open.

[Installed positions](conversion.csv) · [Net lengths](routing.csv) · [Verification](verification.json) · [KiCad reports](kicad-reports.zip)
