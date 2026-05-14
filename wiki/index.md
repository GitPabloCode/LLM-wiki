# Wiki Index

*Last updated: 2025-07-17*

## Summaries
- [SUBSET-026](summaries/subset26.md) — ERTMS/ETCS System Requirements Specification — complete functional specification for train control system | 2025-07-17
- [subset40](summaries/subset40.md) — ERTMS/ETCS Dimensioning and Engineering Rules — installation rules, telegram/message rules, and message dimensioning for interoperability | 2025-07-17
- [SUBSET-058](summaries/subset58.md) — FFFIS STM Application Layer — variables, packets, and messages for STM/ETCS communication | 2025-07-17
- [SUBSET-035](summaries/subset35.md) — FFFIS STM — interface specification between ERTMS/ETCS on-board and National Train Control systems via Specific Transmission Module | 2025-07-17

## Entities
- [DMI](entities/dmi.md) — Driver Machine Interface for train information display | sources: subset26
- [Level Crossing](entities/level-crossing.md) — Road/rail crossing supervised by ERTMS/ETCS | sources: subset26
- [EOLM](entities/eolm.md) — End Of Loop Marker — balise group announcing Euroloop | sources: subset26
- [KMC](entities/key-management-centre.md) — Key Management Centre for Euroradio cryptographic keys | sources: subset26
- [Radio Infill Unit](entities/radio-infill-unit.md) — Trackside device providing radio infill in Level 1 | sources: subset26
- [Euroradio](entities/euroradio.md) — Radio protocol for track-to-train communication in Levels 2/3 | sources: subset26
- [GSM-R](entities/gsm-r.md) — Trackside radio communication network for ERTMS/ETCS | sources: subset26
- [LEU](entities/lineside-electronic-unit.md) — Lineside Electronic Unit generating balise telegrams | sources: subset26
- [ERTMS/ETCS On-board Equipment](entities/ertms-etcs-on-board-equipment.md) — Train-borne computer supervising movement | sources: subset26
- [RBC](entities/rbc.md) — Radio Block Centre — trackside computer generating Movement Authorities | sources: subset26
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
- [Juridical Recording](concepts/juridical-recording.md) — Legal recording of ERTMS/ETCS events | sources: subset26
- [Brake Percentage Conversion](concepts/brake-percentage-conversion.md) — Conversion of brake percentage to braking parameters | sources: subset26
- [Procedures](concepts/procedures.md) — SoM, End of Mission, Shunting, Override, Train Trip, Level Transitions | sources: subset26
- [Track Conditions](concepts/track-conditions.md) — Trackside data informing driver/train of conditions ahead | sources: subset26
- [System Version Management](concepts/system-version-management.md) — Backward compatibility rules for X=1 and X=2 system versions | sources: subset26
- [ERTMS/ETCS Language](concepts/ertms-etcs-language.md) — Variable, packet, and message definitions for air-gap transmission | sources: subset26
- [RBC Handover](concepts/rbc-handover.md) — Automatic transfer between RBC areas | sources: subset26
- [Static Speed Restrictions](concepts/static-speed-restrictions.md) — Independent speed restriction categories forming MRSP | sources: subset26
- [Infill Information](concepts/infill-information.md) — Advance signalling information in Level 1 | sources: subset26
- [Speed and Distance Monitoring](concepts/speed-and-distance-monitoring.md) — Supervision of train speed vs position with EBI/SBI/W/P/I limits | sources: subset26
- [Communication Session](concepts/communication-session.md) — Radio session between on-board and RBC/RIU | sources: subset26
- [Train Position](concepts/train-position.md) — Position determination relative to LRBG | sources: subset26
- [Operating Modes](concepts/ertms-etcs-modes.md) — 17 ERTMS/ETCS operating modes | sources: subset26
- [Application Levels](concepts/ertms-etcs-application-levels.md) — Five ERTMS/ETCS application levels (0, NTC, 1, 2, 3) | sources: subset26
- [Linking](concepts/linking.md) — Balise group linking for position reference and odometer correction | sources: subset26
- [Movement Authority](concepts/movement-authority.md) — Permission for train to move to a specific location | sources: subset26
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
