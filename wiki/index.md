# Wiki Index

*Last updated: 2025-07-17*

## Summaries
- [subset40](summaries/subset40.md) — ERTMS/ETCS Dimensioning and Engineering Rules — installation rules, telegram/message rules, and message dimensioning for interoperability | 2025-07-17
- [SUBSET-058](summaries/subset58.md) — FFFIS STM Application Layer — variables, packets, and messages for STM/ETCS communication | 2025-07-17
- [SUBSET-035](summaries/subset35.md) — FFFIS STM — interface specification between ERTMS/ETCS on-board and National Train Control systems via Specific Transmission Module | 2025-07-17

## Entities
- [euroloop](entities/euroloop.md) — Loop-based transmission system for continuous/semi-continuous communication | sources: subset40
- [balise-group](entities/balise-group.md) — Group of Eurobalises treated as a complete device for ERTMS messaging | sources: subset40
- [eurobalise-antenna](entities/eurobalise-antenna.md) — Onboard antenna communicating with trackside Eurobalises | sources: subset40
- [eurobalise](entities/eurobalise.md) — Trackside transponder for transmitting telegrams to passing trains | sources: subset40
- [STM](entities/stm.md) — Interface component connecting legacy NTC systems to ERTMS/ETCS on-board | sources: subset35, subset58
- [PROFIBUS](entities/profibus.md) — Communication bus (RS-485, 1500 Kbps) used for STM to ERTMS/ETCS on-board interface | sources: subset35
- [Juridical Data Function](entities/juridical-data-function.md) — Forwards national juridical data to recording devices | sources: subset35, subset58
- [Odometer Function](entities/odometer-function.md) — Provides speed/distance estimates to all STMs | sources: subset35, subset58
- [BIU Function](entities/biu-function.md) — Brake Interface Unit for emergency/service brake control | sources: subset35, subset58
- [TIU Function](entities/tiu-function.md) — Train Interface Unit for train command/status signals | sources: subset35, subset58
- [DMI Function](entities/dmi-function.md) — Driver Machine Interface for STM-driver interaction via default window | sources: subset35, subset58
- [STM Control Function](entities/stm-control-function.md) — Central manager for STM state transitions, version compatibility, data forwarding | sources: subset35, subset58

## Concepts
- [ker-compatibility](concepts/ker-compatibility.md) — Additional requirements for equipment offering KER (German legacy system) compatibility | sources: subset40
- [dimensioning-rules](concepts/dimensioning-rules.md) — Maximum iterations per packet and minimum onboard memory requirements | sources: subset40
- [data-engineering-rules](concepts/data-engineering-rules.md) — Content constraints for data types in balise telegrams and radio messages | sources: subset40
- [balise-installation-rules](concepts/balise-installation-rules.md) — Physical installation distance and positioning rules for trackside balises | sources: subset40
- [STM States](concepts/stm-states.md) — Eight-state lifecycle: NP → PO → CO → DE → CS → HS → DA → FA | sources: subset35, subset58
- [FFFIS STM Application Layer](concepts/fffis-stm-application-layer.md) — Three-level protocol structure (variables, packets, messages) for FFFIS STM | sources: subset58
- [STM Level Transitions](concepts/stm-level-transitions.md) — Seamless transitions between ETCS and NTC levels via Eurobalises | sources: subset35, subset58
- [Override Procedure](concepts/override-procedure.md) — Coordinated trip inhibition override between ETCS and STM | sources: subset35, subset58
- [Customisable DMI Service](concepts/customisable-dmi.md) — Configurable cell-based DMI layout service for STMs with custom indicator/button/icon/sound definitions | sources: subset35
- [Specific NTC Data Entry](concepts/specific-ntc-data-entry.md) — Procedure for driver entry of national data for STMs | sources: subset35, subset58
- [FFFIS STM Version Management](concepts/fffis-stm-version-management.md) — Version numbering scheme (X.Y format) and legal backward compatibility envelope for FFFIS STM | sources: subset35
- [Connection Management](concepts/connection-management.md) — Rules for opening, version-checking, maintaining, and closing STM-to-ETCS connections over PROFIBUS | sources: subset35
