# Wiki Index

*Last updated: 2026-05-11*

## Summaries
- [subset26-2](summaries/subset26-2.md) — ERTMS/ETCS SRS Chapters 4.6-7 — Mode transitions, procedures, system version management, and ETCS language | 2026-05-12
- [subset26-1](summaries/subset26-1.md) — ERTMS/ETCS System Requirements Specification — Chapters 1-4 (Introduction, Basic System Description, Principles, Modes) | 2026-05-12
- [subset40](summaries/subset40.md) — ERTMS/ETCS Dimensioning and Engineering Rules — installation rules, telegram/message rules, and message dimensioning for interoperability | 2025-07-17
- [SUBSET-058](summaries/subset58.md) — FFFIS STM Application Layer — variables, packets, and messages for STM/ETCS communication | 2025-07-17
- [SUBSET-035](summaries/subset35.md) — FFFIS STM — interface specification between ERTMS/ETCS on-board and National Train Control systems via Specific Transmission Module | 2025-07-17

## Entities
- [pki](entities/pki.md) — Public Key Infrastructure for secure digital certificate and key distribution | sources: subset26-1
- [kmc](entities/kmc.md) — Key Management Centre managing cryptographic keys for EURORADIO | sources: subset26-1
- [radio-infill-unit](entities/radio-infill-unit.md) — Radio Infill Unit providing semi-continuous infill information in Level 1 | sources: subset26-1
- [lineside-electronic-unit](entities/lineside-electronic-unit.md) — LEU generating balise telegrams from external trackside system information | sources: subset26-1
- [gsm-r](entities/gsm-r.md) — GSM-R radio communication network for bi-directional track-train messaging | sources: subset26-1
- [ertms-etcs-onboard](entities/ertms-etcs-onboard.md) — ERTMS/ETCS On-Board Equipment — computer-based system supervising train movement | sources: subset26-1
- [rbc](entities/rbc.md) — Radio Block Centre — computer-based trackside system generating movement authorities in Levels 2 and 3 | sources: subset26-1
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
- [override-procedure](concepts/override-procedure.md) — Override procedure allowing train to pass EOA in degraded situations (merged ETCS + STM) | sources: subset26-2, subset35, subset58
- [track-conditions-procedures](concepts/track-conditions-procedures.md) — Driver indications and external function info for track conditions (pantograph, brakes, tunnels, etc.) | sources: subset26-2
- [joining-splitting-procedure](concepts/joining-splitting-procedure.md) — Procedures for splitting a train or joining two trains | sources: subset26-2
- [non-protected-level-crossing](concepts/non-protected-level-crossing.md) — Supervision of LX start as EOA/SvL and substitution by LX speed restriction | sources: subset26-2
- [train-reversing-procedure](concepts/train-reversing-procedure.md) — Fast reversal to run away from danger in RV mode | sources: subset26-2
- [change-of-train-orientation](concepts/change-of-train-orientation.md) — Procedures for changing driving cab on same or different engine | sources: subset26-2
- [limited-supervision-procedure](concepts/limited-supervision-procedure.md) — Entry to and exit from Limited Supervision mode | sources: subset26-2
- [on-sight-procedure](concepts/on-sight-procedure.md) — Entry to and exit from On Sight mode | sources: subset26-2
- [rbc-handover-procedure](concepts/rbc-handover-procedure.md) — Normal and degraded RBC/RBC handover procedures | sources: subset26-2
- [level-transition-procedure](concepts/level-transition-procedure.md) — Rules for transitions between all ERTMS/ETCS application levels | sources: subset26-2
- [train-trip-procedure](concepts/train-trip-procedure.md) — Procedure when a train is tripped — TR mode, PT mode, and recovery paths | sources: subset26-2
- [shunting-procedure](concepts/shunting-procedure.md) — Driver-initiated and trackside-ordered entry to Shunting mode | sources: subset26-2
- [end-of-mission-procedure](concepts/end-of-mission-procedure.md) — Procedure when entering SB or SH from operational modes | sources: subset26-2
- [start-of-mission-procedure](concepts/start-of-mission-procedure.md) — Procedure from SB mode to starting a mission — data entry, session establishment, position validation | sources: subset26-2
- [stored-information-mode-level-actions](concepts/stored-information-mode-level-actions.md) — What happens to stored on-board data when entering a new mode or level | sources: subset26-2
- [information-acceptance](concepts/information-acceptance.md) — Three-filter model for accepting/rejecting trackside information based on level, media, and mode | sources: subset26-2
- [train-integrity](concepts/train-integrity.md) — Train integrity confirmation required for Level 3 operation | sources: subset26-1
- [linking](concepts/linking.md) — Balise group linking mechanism for missed-group detection, coordinate assignment, and odometer correction | sources: subset26-1
- [speed-and-distance-monitoring](concepts/speed-and-distance-monitoring.md) — Speed and Distance Monitoring — CSM, TSM, RSM supervision types with EBI/SBI/Warning/P/Indication limits | sources: subset26-1
- [etcs-modes](concepts/etcs-modes.md) — The 17 ERTMS/ETCS on-board operational modes and their transitions | sources: subset26-1
- [movement-authority](concepts/movement-authority.md) — Movement Authority — permission and distance granted to a train to move along a route | sources: subset26-1
- [etcs-application-levels](concepts/etcs-application-levels.md) — The five ERTMS/ETCS Application Levels (0, NTC, 1, 2, 3) defining track-train operating relationships | sources: subset26-1
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
