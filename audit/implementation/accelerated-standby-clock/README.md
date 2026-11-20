# Standby timing and oscillator enable

RX1 remains the optional 4.7 kΩ pull-up on X1 Enable. Its original schematic and PCB assembly exclusion are preserved. The oscillator output and clock distribution retain their original copper. The enable lead adds 1.148 mm of front track.

R9101 moves from the underside to a front-mounted 6.2 kΩ MRS16. Both branches remain on back copper. The D9100 cathode branch adds 1.561 mm and the anode branch adds 13.194 mm. The immediate In2 reference changes locally under its own existing anode connection at the new pin. Outside the pad neighbourhood, the added branches retain their +5 V reference. With 6.2 kΩ and the existing 10 µF capacitor the nominal RC scale is 62 ms. An additional 2 pF would change that product by about 12 ns. The diode and active circuitry determine the actual threshold and timing. Check startup and shutdown ramps on hardware.

All vias, original tracks, auxiliary rail areas, plane contour counts and fixed geometry are preserved. C406 and D9100 values moved to their fabrication layers. An initial R9104 site became occupied by the verified R308 layout. R9105 required a long high-impedance timing branch and was left in place.

[Installed positions and pin mapping](conversion.csv) · [Net lengths](routing.csv) · [Verification and fixed datums](verification.json) · [Native KiCad reports and netlists](kicad-reports.zip)
