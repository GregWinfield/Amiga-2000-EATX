# Low-leakage audio coupling capacitors

C233, C243 and C317 already have 5 mm radial footprints. Rubycon 25TWL22MEFC5X11 is the engineering BOM selection for these positions. The exact part was listed in stock by DigiKey. Rubycon flags some TWL values for discontinuation. Confirm the status of this exact ordering code and traceable stock with the supplier before production. [Distributor listing](https://www.digikey.com/en/products/detail/rubycon/25TWL22MEFC5X11/3562848) · [Manufacturer lifecycle notes](https://www.rubycon.co.jp/en/products/al-radial-lead/series/)

| Characteristic | Nichicon UKL1E220MDD | Rubycon 25TWL22MEFC5X11 |
|---|---:|---:|
| Capacitance, voltage, tolerance | 22 µF, 25 V, ±20% | 22 µF, 25 V, ±20% |
| Maximum leakage at rated voltage after two minutes | 1.1 µA | 1.1 µA |
| Nominal diameter × length and lead pitch | 5 × 11 mm, 2 mm | 5 × 11 mm, 2 mm |
| Temperature range | −40 to +85 °C | −40 to +85 °C |
| Maximum dissipation factor at 120 Hz and 20 °C | 0.08 | 0.14 |
| Derived series resistance at nominal capacitance, 120 Hz | 4.82 Ω | 8.44 Ω |

At minimum capacitance the corresponding series resistance bounds rise to 6.03 and 10.55 Ω. Their difference gives less than 0.04 dB additional calculated resistive attenuation into 1 kΩ and 0.004 dB into 10 kΩ. These bounds apply at the specified test frequency. Broadband response, capacitor leakage at operating bias and the actual external load on C317 require measurement. With the same lead spacing and seating, the previous 20 nH sensitivity still contributes about 2.5 mΩ at 20 kHz. Keep the previous 14 mm assembly allowance. Check startup polarity, both audio outputs under load and the serial connector audio input over operating temperature. The three positions add zero to the conversion count. [Rubycon TWL electrical and dimensional data](https://www.rubycon.co.jp/wp-content/uploads/catalog-aluminum/TWL.pdf) · [Nichicon UKL data](https://www.nichicon.com/getmedia/4d20532b-3c34-4ede-b997-d41a63e4243a/e-ukl.pdf) · [Existing layout verification](../resumed-av-capacitors/README.md)

