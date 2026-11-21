# Keyboard-clock substitution review

C260 is a two-terminal 100 pF ceramic 1206 between CN300.1 / FB302.1 and GND. The original shopping list specifies 100 pF and ceramic construction but leaves the order code blank. Its separate 100 pF three-terminal feedthrough line describes a different component type. FB302 is generic in the design and the shopping list gives 80 Ω for the 1206 bead group without a test frequency or an ordering code. The original capacitor tolerance, dielectric, voltage, temperature coefficient, ESR, ESL and self-resonance therefore remain unidentified. [Original shopping list](../../../BOM/A2000EATX-REV31-ShoppingList.csv)

The orderable KEMET C315C101J5G5TA is a 100 pF ±5%, 50 V C0G radial specified at 1 MHz, 1 V RMS. The temperature coefficient is ±30 ppm/°C, and the 0.1% maximum dissipation factor implies about 1.59 Ω maximum ESR at that test frequency and nominal capacitance. The drawing gives 3.81 × 2.54 × 3.14 mm maximum body, 2.54 ±0.78 mm lead spacing and 0.61 mm maximum wire. The project radial footprint allows 0.80 mm holes and 4.66 mm above the board with coating and seating allowance. [KEMET part drawing](https://www.farnell.com/datasheets/4397040.pdf) · [Orderable part](https://www.digikey.com/en/products/detail/kemet/C315C101J5G5TA/6562399)

The existing layout screen found a physically clear radial candidate. Its signal lead shortened by 0.067 mm, its ground connection lengthened by 1.015 mm and its screened nearest back-copper edge was 1.789 mm from a lead centre. This is a placement calculation. The following impedance magnitudes use a lossless series-LC model to test sensitivity to package and lead inductance. Assumed 0.5–1 nH for a short SMD loop and 5–20 nH for the radial loop are illustrative. They are not characterized part limits. The sweep covers the slow clock and representative conducted edge harmonics. FB302's actual impedance curve and the assembled keyboard edge spectrum are unknown.

| Frequency | Ideal 100 pF | 0.5–1 nH examples | 5–20 nH examples |
|---|---:|---:|---:|
| 10 kHz | 159.15 kΩ | ≈159.15 kΩ | ≈159.15 kΩ |
| 1 MHz | 1.592 kΩ | ≈1.592 kΩ | ≈1.591 kΩ |
| 10 MHz | 159.15 Ω | 159.09–159.12 Ω | 157.90–158.84 Ω |
| 100 MHz | 15.92 Ω | 15.29–15.60 Ω | 3.35–12.77 Ω |

At nominal capacitance these inductance ranges put series resonance at about 503–712 MHz and 113–225 MHz respectively. Loss and fixture impedance determine the actual minima. The radial model can become inductive within the upper edge spectrum. A nominal 100 pF match cannot establish the port's loss, ringing or threshold margin there. Retain C260 in SMD. Reopen with the original capacitor and bead ordering codes or impedance sweeps of known boards, a short-lead radial fixture, and keyboard-clock measurements with representative cables.
