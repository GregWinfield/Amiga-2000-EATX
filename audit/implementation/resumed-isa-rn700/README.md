# ISA termination at RN700

Seven 1 nF branches now use the KEMET C315C102J5G5TA radial capacitor. The capacitor pin facing the sockets, the unique RN700 pin and the 1 kΩ common-return network were traced separately for every branch. Only the connector-to-capacitor leaf and the private capacitor-to-network copper were replaced. The original inter-socket trunks and all vias are intact. The installation uses the same 50 V C0G part, drill, land, lead envelope and frequency assessment as the first termination batch. [Capacitor drawing and bench requirements](../resumed-termination-capacitors/README.md)

| Capacitor | Previous socket leaf, mm | Routed socket leaf, mm |
|---|---:|---:|
| C713 | 5.052 | 3.614 |
| C714 | 5.102 | 8.850 |
| C716 | 4.950 | 3.302 |
| C717 | 4.950 | 8.592 |
| C719 | 4.950 | 3.407 |
| C720 | 5.001 | 9.064 |
| C722 | 5.001 | 3.309 |

The maximum increase is 4.063 mm at C720, about 28 ps one way at 7 ps/mm. The 1 kΩ and 1 nF termination time constant remains 1 µs. Ground-reference gaps on the new branches are confined to within 1.4 mm of their own capacitor, resistor-network or socket pads. The independent terminal-reference report gives total length, length outside inner ground, and length outside inner ground beyond those terminals, in mm. Preserved nearby routes on both sides, auxiliary power-rail areas and all inner contour counts matched the control.

The staggered bodies clear the existing socket courtyard by at least 0.138 mm, in addition to both courtyard allowances. Use the 4.66 mm maximum seated envelope for card fit checks. Probe representative near and far socket waveforms with an installed bridgeboard and ISA cards, and verify component-side card overhang before manufacturing.

[Pin mappings and coordinates](conversion.csv) · [Copper lengths](routing.csv) · [Terminal reference samples](terminal-reference.json) · [Verification](verification.json) · [Native reports](kicad-reports.zip)
