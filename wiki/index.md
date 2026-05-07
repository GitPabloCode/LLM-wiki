# Wiki Index

*Last updated: 2026-05-07*

## Summaries
- [SUBSET-035: ERTMS/ETCS Specific Transmission Module FFFIS](summaries/subset35.md) — Form Fit Functional Interface Specification for the Specific Transmission Module, covering PROFIBUS, STM states, control function, DMI, odometer, TIU, BIU, juridical data, and version management | 2025-03-13
- [SUBSET-040: ERTMS/ETCS — Class 1, Dimensioning and Engineering Rules](summaries/subset40.md) — Dimensioning and engineering rules for ERTMS/ETCS Class 1, covering balise installation, telegrams, messages, and data dimensioning | 2026-05-07

## Entities
- [DMI STM Interface](entities/dmi-stm.md) — Driver-Machine Interface for STM national system interaction with unified and customisable services | sources: subset35
- [Juridical Data Recording](entities/juridical-data-recording.md) — National juridical data forwarding from STM to On-Board Recording Device | sources: subset35
- [Brake Interface Unit (BIU)](entities/brake-interface-unit.md) — Emergency and service brake command/status interface for STMs | sources: subset35
- [Train Interface Unit (TIU)](entities/train-interface-unit.md) — Train command/status signal interface for STMs (brakes, pantograph, traction) | sources: subset35
- [Odometer Function](entities/odometer-function.md) — On-board function providing speed/distance estimation with confidence intervals to STMs | sources: subset35
- [PROFIBUS (STM Interface)](entities/profibus-stm.md) — Physical communication bus (RS-485) with addressing and SAPs for STM interface | sources: subset35
- [STM Manager System](entities/stm-manager-system.md) — Subsystem handling STM state transitions between the eight operational states | sources: subset35
- [STM Control Function](entities/stm-control-function.md) — On-board function managing STM state, data distribution, and communication | sources: subset35
- [Specific Transmission Module (STM)](entities/stm.md) — Interface component connecting ERTMS/ETCS on-board to National Train Control systems | sources: subset35
- [RBC (Radio Block Centre)](entities/rbc.md) — Trackside RBC with handover and message size rules | sources: subset40
- [Euroloop](entities/euroloop.md) — Continuous trackside transmission system | sources: subset40
- [Eurobalise Antenna](entities/eurobalise-antenna.md) — Onboard antenna with front-to-antenna distance constraints | sources: subset40
- [Balise Group](entities/balise-group.md) — Grouped balises with spacing and reference location rules | sources: subset40
- [Balise](entities/balise.md) — Trackside transmission device with installation and telegram rules | sources: subset40

## Concepts
- [STM Customisable DMI Service](concepts/stm-customisable-dmi-service.md) — Configurable DMI layouts, icons, sounds, and indicator/button arrangements for STM | sources: subset35
- [Specific NTC Data Entry](concepts/specific-ntc-data-entry.md) — Driver entry procedure for national system data required by STM | sources: subset35
- [STM Version Management](concepts/stm-version-management.md) — X.Y version numbering scheme for FFFIS STM with backward compatibility envelope | sources: subset35
- [STM Connection Management](concepts/stm-connection-management.md) — Version check and connection establishment procedure between STM and ERTMS/ETCS on-board | sources: subset35
- [STM Safety Protocols](concepts/stm-safety-protocols.md) — SL4, SL2, SL0 safety protocol levels for STM communication | sources: subset35
- [STM States](concepts/stm-states.md) — Eight operational states of an STM: NP, PO, CO, DE, CS, HS, DA, FA | sources: subset35
- [Balise Installation Rules](concepts/balise-installation-rules.md) — Comprehensive installation distance and tolerance rules for balises | sources: subset40
- [KER Compatibility](concepts/ker-compatibility.md) — Additional requirements for KER-compatible transmission systems | sources: subset40
- [Message Dimensioning](concepts/message-dimensioning.md) — Size constraints on balise telegrams and radio messages | sources: subset40
- [Data Dimensioning](concepts/data-dimensioning.md) — Iteration and memorisation limits for all ETCS data elements | sources: subset40
- [Track Conditions](concepts/track-conditions.md) — Advance announcement distances for special track features | sources: subset40
- [Linking](concepts/linking.md) — Expected balise group sequence verification mechanism | sources: subset40
- [In-fill](concepts/in-fill.md) — Supplementary MA update via balise, loop, or radio | sources: subset40
- [Level Transition](concepts/level-transition.md) — Rules for transitions between ETCS operational levels | sources: subset40
- [EOA (End of Authority)](concepts/eoa.md) — Reference location for train movement authorisation | sources: subset40
