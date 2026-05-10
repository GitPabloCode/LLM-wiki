# Customisable DMI Service

**Source:** [[subset35]] | **Date:** 2025-07-17 | **Type:** concept

The Customisable DMI service allows STMs to define a bespoke layout for their default window on the ERTMS/ETCS on-board DMI, using cell-based positioning rather than the standard ETCS layout areas [subset35 ¶603].

## When Used

An STM designed for customisable DMI provides configuration data as part of its product documentation. The ERTMS/ETCS on-board is configurable to store this data and serve STM DMI requests accordingly. If no custom config exists, the [[dmi-function]] uses the unified DMI service instead [subset35 ¶603]-[§604].

## Configuration Data

For each STM using customisable DMI, the following is configured [subset35 ¶701]-[§753]:

- **Indicators** — identifier, font size, text alignment, position (x:y offset, size) for both touch screen and soft key technology
- **Buttons** — identifier, font size, text alignment, position, linked soft key
- **Icons** — identifier, bitmap (RGB BMP format), option to display text upon icon
- **Sounds** — identifier, WAV file
- **Speed and distance supervision** — yes/no, speed dial range (140/180/250/400 km/h or same as ETCS)
- **Flashing options** — slow/fast frequency (0.5-8 Hz), style (yellow frame or whole area)
- **Moved ETCS areas** — relocation of standard ETCS layout areas (F1-F5, A4, B7, C1, C7-C9, E1, G13) to custom positions

## Position Identifiers

For customisable DMI, Position Identifiers use cell coordinates (x:y offset and size) defined in the STM's configuration data [subset35 ¶636].

## Cross-references
- [[dmi-function]] — The DMI Function that provides this service
- [[stm]] — The Specific Transmission Module
- [[stm-control-function]] — Manages STM communication
