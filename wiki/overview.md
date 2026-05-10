# Overview

*Last updated: 2025-07-17*

## Sources Ingested

- **SUBSET-035** (2015-12-16) — ERTMS/ETCS Specific Transmission Module FFFIS (FFFIS STM v3.2.0) — System-level specification covering all protocol layers
- **SUBSET-058** (2015-12-16) — FFFIS STM Application Layer — Detailed data format definitions for variables, packets, and messages
- **SUBSET-040** (2009-04-07) — ERTMS/ETCS Dimensioning and Engineering Rules — Installation rules, telegram/message constraints, and message dimensioning for interoperability

## Key Entities

### From SUBSET-035 / SUBSET-058 (STM System)
- [[stm]] — Specific Transmission Module, the interface component connecting legacy National Train Control systems to ERTMS/ETCS on-board
- [[stm-control-function]] — Central manager for STM state transitions, version compatibility, and data forwarding
- [[dmi-function]] — Driver Machine Interface for STM-driver interaction via default window
- [[tiu-function]] — Train Interface Unit for train command/status signals
- [[biu-function]] — Brake Interface Unit for emergency/service brake control
- [[odometer-function]] — Provides speed/distance estimates to all STMs
- [[juridical-data-function]] — Forwards national juridical data to recording devices
- [[profibus]] — Communication bus (RS-485, 1500 Kbps) linking STMs to ETCS

### From SUBSET-040 (Trackside & Transmission)
- [[eurobalise]] — Trackside transponder for spot transmission of telegrams to passing trains
- [[eurobalise-antenna]] — Onboard antenna mounted beneath the train for balise communication
- [[balise-group]] — Group of Eurobalises treated as a complete device for ERTMS messaging
- [[euroloop]] — Loop-based transmission system providing continuous/semi-continuous communication

## Key Concepts

### From SUBSET-035 / SUBSET-058 (STM Protocol)
- [[stm-states]] — Eight-state lifecycle: NP → PO → CO → DE → CS → HS → DA → FA
- [[connection-management]] — Version-checked connection establishment and maintenance
- [[fffis-stm-version-management]] — X.Y version numbering with legal backward compatibility envelope (X=4)
- [[specific-ntc-data-entry]] — Procedure for driver entry of national data for STMs
- [[customisable-dmi]] — Configurable cell-based DMI layout for STMs
- [[override-procedure]] — Coordinated trip inhibition override between ETCS and STM
- [[stm-level-transitions]] — Seamless transitions between ETCS and NTC levels via Eurobalises
- [[fffis-stm-application-layer]] — Three-level protocol structure (variables, packets, messages)

### From SUBSET-040 (Engineering Rules)
- [[balise-installation-rules]] — Physical installation distance and positioning rules for trackside balises
- [[data-engineering-rules]] — Content constraints for data types in balise telegrams and radio messages
- [[dimensioning-rules]] — Maximum iterations per packet and minimum onboard memory requirements
- [[ker-compatibility]] — Additional rules for equipment offering KER (German legacy system) compatibility

## Cross-Source Insights

- **SUBSET-035 + SUBSET-058:** SUBSET-035 defines system-level STM architecture; SUBSET-058 provides the exact bit-level encoding. Together they form a complete specification: *what* happens vs *how* to encode it on the wire.
- **SUBSET-040 relation:** SUBSET-040 provides the engineering constraints (installation distances, message sizing, data content rules) that complement the functional specifications in SUBSET-026 (SRS), SUBSET-036 (Eurobalise FFFIS), and SUBSET-044 (Euroloop FFFIS). It constrains *how* the system is physically deployed and dimensioned.
- **Level transitions:** SUBSET-040 references SUBSET-035 (FFFIS STM) for engineering requirements on level transitions involving STM, connecting the trackside engineering rules with the STM domain.
