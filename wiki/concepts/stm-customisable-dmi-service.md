# STM Customisable DMI Service

**Source:** [[subset35]] | **Date:** 2025-03-13 | **Type:** concept

The **STM Customisable DMI Service** allows an STM to provide configuration data to the ERTMS/ETCS on-board DMI for custom layouts, icons, sounds, and indicator/button arrangements. This configuration data is stored in the ERTMS/ETCS on-board [¶603, §700–§753].

## Configuration Data Per STM

Each STM provides the following configuration data (identified by NID_STM) [¶700–§753]:

- **Indicators** — List with id, font size, horizontal/vertical alignment [¶701–§703]
- **Indicator Positions** — Two lists (for soft key and touch screen): id, x:y offset, size [¶704–§708]
- **Buttons** — List with id, font size, alignment [¶709–§711]
- **Button Positions** — Two lists (for soft key and touch screen): id, offset, size, linked soft key [¶712–§717]
- **Icons** — List with id, bitmap, display text upon icon [¶718–§721]
- **Speed/Distance Supervision** — Yes/No, speed dial range [§722–§725]
- **Flashing Options** — Slow/fast frequency, style (yellow frame/whole area) [§726–§728]
- **Sounds** — List with id, WAV file [§729–§731]
- **Moved ETCS Layout Areas** — List of moved areas (A4, B7, C1, C7-C9, E1, F1-F5, G13) with new x:y offset and new soft key for buttons [§732–§751]

## Comparison with Unified Service

| Feature | Customisable | Unified |
|---|---|---|
| Configuration data | STM provides config | No config needed [§604] |
| Icon handling | Bitmap supplied by STM | Standard ETCS icons [§653] |
| Sound handling | WAV file supplied | Frequency segments [§661–§668] |
| Position layout | Custom cell coordinates | Standard ETCS layout areas [§635–§636] |
| Unconfigurable parts | Same as unified | Same as customisable [§605] |

## Cross-references
- [[DMI STM Interface]] — parent DMI interface
- [[Specific Transmission Module (STM)]] — provides configuration data
- [[STM Control Function]] — manages DMI channels
- [[subset35]] — source document
