# Overview

*Last updated: 2026-05-12*

## Sources Ingested

- **SUBSET-026-1** (2016-05-13) — ERTMS/ETCS System Requirements Specification v3.6.0 — Core specification covering Chapters 1–4: Introduction, Basic System Description, Principles, Modes and Transitions
- **SUBSET-035** (2015-12-16) — ERTMS/ETCS Specific Transmission Module FFFIS (FFFIS STM v3.2.0) — System-level specification covering all protocol layers
- **SUBSET-058** (2015-12-16) — FFFIS STM Application Layer — Detailed data format definitions for variables, packets, and messages
- **SUBSET-040** (2009-04-07) — ERTMS/ETCS Dimensioning and Engineering Rules — Installation rules, telegram/message constraints, and message dimensioning for interoperability

## Key Entities

### Trackside Entities (from SUBSET-026-1 and SUBSET-040)
- [[rbc]] — Radio Block Centre, the computer-based system generating movement authorities for Levels 2/3
- [[eurobalise]] — Trackside transponder for spot transmission of telegrams to passing trains
- [[eurobalise-antenna]] — Onboard antenna for balise communication
- [[balise-group]] — Group of Eurobalises treated as a complete device
- [[euroloop]] — Loop-based continuous/semi-continuous transmission
- [[lineside-electronic-unit]] — LEU generating variable balise telegrams
- [[radio-infill-unit]] — RIU providing semi-continuous infill in Level 1
- [[gsm-r]] — Radio communication network for track-train messaging
- [[kmc]] — Key Management Centre for cryptographic keys
- [[pki]] — Public Key Infrastructure for certificate distribution

### On-Board Entities (from SUBSET-026-1, SUBSET-035, SUBSET-058)
- [[ertms-etcs-onboard]] — Core on-board equipment supervising train movement
- [[stm]] — Specific Transmission Module connecting National Systems to ETCS
- [[stm-control-function]] — Central manager for STM state transitions
- [[dmi-function]] — Driver Machine Interface
- [[tiu-function]] — Train Interface Unit
- [[biu-function]] — Brake Interface Unit
- [[odometer-function]] — Speed/distance estimation
- [[juridical-data-function]] — Juridical recording
- [[profibus]] — RS-485 communication bus for STMs

## Key Concepts

### From SUBSET-026-1 (Core SRS)
- [[etcs-application-levels]] — Five levels (0, NTC, 1, 2, 3) defining track-train relationships
- [[movement-authority]] — Permission/distance for train movement; core mechanism for train control
- [[etcs-modes]] — 17 operational modes defining on-board behaviour and responsibilities
- [[speed-and-distance-monitoring]] — Three supervision types (CSM, TSM, RSM) with EBI/SBI/W/P/I limits
- [[linking]] — Balise group linking for missed-group detection and odometer correction
- [[train-integrity]] — Train completeness confirmation required for Level 3

### From SUBSET-035/058 (STM Protocol)
- [[stm-states]] — Eight-state lifecycle: NP → PO → CO → DE → CS → HS → DA → FA
- [[connection-management]] — Version-checked connection establishment
- [[fffis-stm-version-management]] — X.Y version numbering
- [[specific-ntc-data-entry]] — Driver entry of national data for STMs
- [[customisable-dmi]] — Configurable DMI layout for STMs
- [[override-procedure]] — Coordinated trip inhibition override between ETCS and STM
- [[stm-level-transitions]] — Seamless ETCS↔NTC transitions
- [[fffis-stm-application-layer]] — Three-level protocol (variables, packets, messages)

### From SUBSET-040 (Engineering Rules)
- [[balise-installation-rules]] — Physical installation rules for balises
- [[data-engineering-rules]] — Data content constraints
- [[dimensioning-rules]] — Maximum iterations, minimum memory
- [[ker-compatibility]] — German legacy system compatibility

## Cross-Source Insights

- **Level NTC ↔ STM Integration**: The Level NTC concept from SUBSET-026-1 aligns with the STM interface specification in SUBSET-035/058. SUBSET-026-1 defines Level NTC operation and the STM as the standardised interface to national systems [subset26-1 ¶194], while SUBSET-058 defines the detailed application-layer protocol for STM-ETCS communication. The level transition rules from SUBSET-026-1 ¶311-¶318 are implemented through the STM state machine and transition packets (STM-16, STM-17).

- **Balise Configuration Consistency**: SUBSET-026-1 defines balise group configuration (1-8 balises per group, linking, coordinate systems) which is complemented by SUBSET-040's engineering rules for physical installation (spacing, signal positioning, EOA clearance). The linking mechanism described in SUBSET-026-1 ¶396-¶445 requires the engineering constraints on inter-balise spacing defined in SUBSET-040.

- **Speed Monitoring and Brake Models**: SUBSET-026-1 defines comprehensive braking models (traction, speed-dependent deceleration, build-up times) and supervision limits (EBI, SBI, Warning, Permitted, Indication). These are referenced by the STM interface for speed/distance data exchange.

## Comparisons
*(None yet)*
