# ISA termination capacitors

C726 and five positions beside RN704 use the established KEMET C315C102J5G5TA radial 1 nF C0G, 5%, 50 V part. Each private resistor junction and ISA socket pin retains its original assignment. C782 and C787 connect to the socket on B.Cu through the existing terminals. The other socket leaves and all six resistor branches run on F.Cu. The interslot trunks and all vias are preserved.

The six socket nets change by −2.64 to +2.94 mm. The largest private branch increase is 6.56 mm at RN704-R2. The reference-plane comparison found no change on the sampled surrounding routes and no new copper islands. The [verification](verification.json) includes the added track lengths over local plane clearance around terminals. The minimum courtyard separation is 0.087 mm between C786 and CN702. Use the specified body envelope and check the assembled socket, card and lead seating at that position. Validate termination waveforms on representative loaded slots before fabrication release.

The C722 reference and the existing capacitance legend moved clear of the new parts. Refilled DRC, parity and ERC match the control by reported object. [Pin assignments](conversion.csv) · [Copper lengths](routing.csv) · [Native reports](kicad-reports.zip)

