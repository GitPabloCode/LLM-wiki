# SUBSET-026-1 — ERTMS/ETCS System Requirements Specification (Chapters 1–4)

**Source:** [[subset26-1]] | **Date:** 2026-05-12 | **Type:** summary

This is the core ERTMS/ETCS System Requirements Specification (SRS), Baseline 3 2nd Release (v3.6.0, 13/05/2016). This document covers Chapters 1 through 4 of the SRS.

## Chapter 1: Introduction

Defines the purpose, scope, and structure of the SRS. ERTMS/ETCS is the European standard for interoperable train control, replacing incompatible national ATC systems. Advantages include cross-border interoperability, safety improvement, shorter headway via moving block, step-by-step migration, and Pan-European manufacturer competition. [subset26-1 ¶9-¶19]

Technical interoperability requires uniform behaviour of train and trackside equipment to received information. Operational interoperability (operating rules, engineering standards) is outside the SRS scope. [subset26-1 ¶23-¶25]

## Chapter 2: Basic System Description

Defines the system structure comprised of two subsystems:
- **Trackside subsystem**: Balises, Lineside Electronic Units (LEUs), GSM-R, Radio Block Centre (RBC), Euroloop, Radio Infill Unit, Key Management Centre (KMC), Public Key Infrastructure (PKI) [subset26-1 ¶91-¶125]
- **On-board subsystem**: ERTMS/ETCS on-board equipment, GSM-R onboard radio system [subset26-1 ¶126-¶139]

Defines five ERTMS/ETCS Application Levels:
- **Level 0**: Operation on non-equipped lines; on-board only supervises maximum design speed and unfitted area speed; no cab signalling [subset26-1 ¶162-¶182]
- **Level NTC**: Operation on lines equipped with national train control systems; supervision through STM; Eurobalises used only for level transitions [subset26-1 ¶183-¶212]
- **Level 1**: Spot transmission based train control via Eurobalises; continuous speed supervision; lineside signals required (except with semi-continuous infill) [subset26-1 ¶213-¶246]
- **Level 2**: Radio-based train control via Euroradio; RBC knows each train individually; lineside signals optional; train position reported by train to RBC [subset26-1 ¶247-¶276]
- **Level 3**: Radio-based train control similar to Level 2 but train position and integrity reported by train; enables moving block operation [subset26-1 ¶277-¶310]

Level transitions are defined in a transition table showing all permitted transitions between levels. [subset26-1 ¶311-¶318]

## Chapter 3: Principles

Specifies system principles for both on-board and trackside subsystems. Major topics:

### Balise Configuration and Linking
- Balise groups: 1–8 balises per group; coordinate system defined by balise number 1 [subset26-1 ¶343-¶355]
- Single balise groups require linking data to assign coordinate system (Level 1) or position report based on two balise groups (Level 2/3) [subset26-1 ¶358-¶385]
- Linking: determines if a balise group is missed; assigns coordinate system to single balises; corrects odometer confidence interval [subset26-1 ¶396-¶445]

### Radio Communication Management
- Only on-board can initiate communication sessions [subset26-1 ¶455]
- On-board manages simultaneous sessions with at least two entities [subset26-1 ¶453]
- Session establishment, maintenance (with loss-of-connection handling), and termination procedures [subset26-1 ¶454-¶553]
- Radio network registration and safe radio connection indication to driver [subset26-1 ¶554-¶589]

### Location Principles and Train Position
- Two types: Location data (refers to a given location) and Profile data (valid for a distance) [subset26-1 ¶592-¶593]
- Train position defined relative to LRBG (Last Relevant Balise Group) [subset26-1 ¶599-¶607]
- Confidence interval: accounts for odometer accuracy and balise location accuracy [subset26-1 ¶697-¶736]
- Position reporting to RBC includes distance, orientation, speed, and train integrity information [subset26-1 ¶737-¶803]

### Movement Authority (MA)
- End of Movement Authority: EOA (target speed zero) or LOA (Limit of Authority, non-zero target speed) [subset26-1 ¶900-¶901]
- Structure: multiple sections, time-outs, danger point, overlap [subset26-1 ¶940-¶967]
- MA update via repositioning information and infill [subset26-1 ¶1025-¶1082]
- Co-operative shortening of MA (Level 2/3 only) [subset26-1 ¶1083-¶1090]

### Static Speed Restrictions and Gradients
- Eleven categories: SSP, ASP, TSR, max train speed, signalling related, mode related, STM max/system speed, LX speed, override, PBD speed restriction [subset26-1 ¶1203-¶1216]
- SSP: Basic SSP and specific SSP categories (Cant Deficiency and Other Specific) [subset26-1 ¶1227-¶1252]
- Gradients: continuous profile, positive for uphill, negative for downhill [subset26-1 ¶1363-¶1372]

### Speed and Distance Monitoring
- Comprehensive braking models: traction model, speed-dependent deceleration, brake build-up time, brake position [subset26-1 ¶1510-¶1605]
- Safe deceleration (emergency brake), expected deceleration (service brake), normal service brake deceleration [subset26-1 ¶1784-¶1902]
- Supervision limits: EBI, SBI, Warning, Permitted speed, Indication [subset26-1 ¶1939-¶2082]
- Three monitoring types: Ceiling speed monitoring (CSM), Target speed monitoring (TSM), Release speed monitoring (RSM) [subset26-1 ¶2127-¶2135]
- Perturbation location: triggers MA request before train needs to brake [subset26-1 ¶2278-¶2305]

### Special Functions
- RBC/RBC Handover, Non-Leading engines, Splitting/Joining, Reversing, Track Ahead Free, National Systems, Big Metal Mass tolerance, Cold Movement Detection, Virtual Balise Cover [subset26-1 ¶2344-¶2499]

### Data Consistency
- Balise linking consistency, message consistency, unlinked balise group checks [subset26-1 ¶2500-¶2591]
- Radio message time-stamping, sequence supervision, safe radio connection supervision [subset26-1 ¶2592-¶2641]

### System Version Management
- On-board supports any version in the legally operated envelope [subset26-1 ¶2646-¶2699]

### System Data
- Fixed values, National/Default values, Train Data (entered before mission), Additional Data (Driver ID, Level, Radio data, ETCS Identity, Train Running Number, Adhesion Factor) [subset26-1 ¶2700-¶2810]

## Chapter 4: Modes and Transitions

Defines 17 ERTMS/ETCS modes: FS, LS, OS, SR, SH, UN, PS, SL, SB, TR, PT, SF, IS, NP, NL, SN, RV. [subset26-1 ¶3162-¶3165]

Each mode has defined context, applicable levels, and responsibilities. Mode transitions follow defined rules with priority ordering. Acceptance of received information depends on level, transmission medium, and current mode. [subset26-1 ¶3152-¶3541]

## Cross-References
- [[rbc]] — Radio Block Centre entity
- [[ertms-etcs-onboard]] — On-board equipment entity
- [[movement-authority]] — Movement Authority concept
- [[etcs-application-levels]] — Application Levels concept
- [[etcs-modes]] — ETCS modes concept
- [[speed-and-distance-monitoring]] — Speed and Distance Monitoring concept
- [[subset35]] — STM specification
- [[subset40]] — Dimensioning and Engineering Rules
