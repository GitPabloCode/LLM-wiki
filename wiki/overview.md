# Overview

*Last updated: 2025-07-17*

## Sources Ingested

- **SUBSET-035** (2015-12-16) — ERTMS/ETCS Specific Transmission Module FFFIS (FFFIS STM v3.2.0) — System-level specification covering all protocol layers
- **SUBSET-058** (2015-12-16) — FFFIS STM Application Layer — Detailed data format definitions for variables, packets, and messages
- **SUBSET-040** (2009-04-07) — ERTMS/ETCS Dimensioning and Engineering Rules — Installation rules, telegram/message constraints, and message dimensioning for interoperability
- **SUBSET-026** (2016-05-13) — ERTMS/ETCS System Requirements Specification (SRS) — Complete functional specification for the ERTMS/ETCS train control system

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
- [[eolm]] — End Of Loop Marker, balise group announcing Euroloop presence

### From SUBSET-026 (System Requirements)
- [[rbc]] — Radio Block Centre, the trackside computer generating Movement Authorities for Levels 2/3
- [[ertms-etcs-on-board-equipment]] — The train-borne computer supervising movement
- [[euroradio]] — Radio protocol for track-to-train communication
- [[gsm-r]] — GSM-Railway communication network
- [[lineside-electronic-unit]] — Drives switchable balises
- [[radio-infill-unit]] — Provides radio infill in Level 1
- [[key-management-centre]] — Manages cryptographic keys for Euroradio
- [[level-crossing]] — Road/rail crossing supervised by ERTMS/ETCS
- [[dmi]] — Driver Machine Interface

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

### From SUBSET-026 (System Requirements)
- [[movement-authority]] — Permission for train movement to a specific location
- [[ertms-etcs-application-levels]] — Five levels (0, NTC, 1, 2, 3) defining transmission and supervision mode
- [[ertms-etcs-modes]] — 17 operating modes (FS, LS, OS, SR, SH, UN, PS, SL, SB, TR, PT, SF, IS, NP, NL, SN, RV)
- [[linking]] — Balise group linking for position reference and odometer correction
- [[train-position]] — Position determination relative to Last Relevant Balise Group
- [[communication-session]] — Radio session between on-board and RBC/RIU
- [[speed-and-distance-monitoring]] — Braking curve supervision with EBI/SBI/W/P/I limits
- [[infill-information]] — Advance signalling data in Level 1 via balise, loop, or radio
- [[static-speed-restrictions]] — SSP, TSR, ASP and other independent speed categories
- [[rbc-handover]] — Automatic transfer between RBC areas
- [[ertms-etcs-language]] — Variable, packet, and message definitions for air-gap transmission
- [[system-version-management]] — Backward compatibility for X=1/X=2 system versions
- [[track-conditions]] — 16 types of track condition data transmitted to the train
- [[procedures]] — SoM, End of Mission, Shunting, Override, Train Trip, Level Transitions
- [[brake-percentage-conversion]] — Conversion of brake percentage to braking parameters
- [[juridical-recording]] — Legal event recording for post-incident analysis

## Cross-Source Insights

- **SUBSET-035 + SUBSET-058:** SUBSET-035 defines system-level STM architecture; SUBSET-058 provides the exact bit-level encoding. Together they form a complete specification: *what* happens vs *how* to encode it on the wire.
- **SUBSET-040 relation:** SUBSET-040 provides the engineering constraints (installation distances, message sizing, data content rules) that complement the functional specifications in SUBSET-026 (SRS), SUBSET-036 (Eurobalise FFFIS), and SUBSET-044 (Euroloop FFFIS). It constrains *how* the system is physically deployed and dimensioned.
- **SUBSET-026 as the core SRS:** SUBSET-026 is the central specification that defines *what* the ERTMS/ETCS system does functionally. SUBSET-040 provides engineering rules that implement the SRS constraints. SUBSET-035/058 define the STM interface for National System compatibility as specified in SUBSET-026's Level NTC requirements.
- **Level NTC integration:** SUBSET-026 defines the STM/National System interface at the functional level (Level NTC) and level transition rules. SUBSET-035/058 provide the detailed FFFIS implementation of that interface. The [[stm-level-transitions]] concept from SUBSET-035/058 directly implements the Level Transition procedure defined in SUBSET-026.
- **Override coordination:** The [[override-procedure]] defined in SUBSET-035/058 coordinates with the Override procedure specified in SUBSET-026 Chapter 5, ensuring consistent behavior when ETCS and NTC systems interact at level transitions.
- **Language compatibility:** The [[ertms-etcs-language]] (Chapter 7 of SUBSET-026) and [[fffis-stm-application-layer]] (SUBSET-058) share the same variable/packet/message structure principles but apply to different air gaps (Euroradio/Eurobalise/Euroloop vs. STM PROFIBUS).
