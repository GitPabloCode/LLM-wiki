# Overview

**Date:** 2025-03-13 | **Type:** overview

## Ingested Sources

### SUBSET-040: ERTMS/ETCS — Class 1, Dimensioning and Engineering Rules
Developed by UNISIG (Issue 2.3.0, 7 April 2009), this document defines mandatory **dimensioning and engineering rules** that supplement the ERTMS/ETCS System Requirements Specification. Covering balise installation, telegram/message rules, data dimensioning limits, and KER compatibility, these rules ensure interoperability across different ETCS equipment manufacturers.

### SUBSET-035: ERTMS/ETCS Specific Transmission Module FFFIS
Developed by UNISIG (Issue 3.2.0, 2015-12-16), this document defines the **Form Fit Functional Interface Specification** for the Specific Transmission Module (STM). It covers the complete interface between ERTMS/ETCS on-board equipment and National Train Control systems across all protocol levels — from the PROFIBUS physical connector (RS-485, 1500 Kbps) up to the application layer functions. Key areas include the STM eight-state machine (NP, PO, CO, DE, CS, HS, DA, FA), the STM Control Function managing state transitions and data distribution, DMI interfaces (unified and customisable), odometer data provision, train interface and brake interface commands, juridical data recording, and version management with backward compatibility envelopes.

## Key Themes

### Installation Precision (SUBSET-040)
Multiple rules specify exact distances for balise placement relative to train front (2m–12.5m antenna offset), EOAs (≥1.3m), stopping points (≤0.7m), and train detection sections (≥13.8m).

### Data Bandwidth Management (SUBSET-040)
Dimensioning rules limit iterations of each data element in a single packet and memorisation limits for onboard systems.

### Operational Safety Boundaries (SUBSET-040)
Level transition borders, RBC handover areas, in-fill positioning rules, and advance announcement distances for track conditions (10–17 seconds).

### STM State Machine and State Management (SUBSET-035)
The eight-state STM machine (NP→PO→CO→DE→CS→HS→DA→FA) with defined transition conditions managed by the STM Control Function ensures safe and orderly activation and deactivation of National Train Control systems. Only one STM can be active at a time, and the ERTMS/ETCS on-board monitors STM safety integrity.

### Interface Standardisation (SUBSET-035)
Standardised interfaces (DMI, Train Interface, Brake Interface, Odometer, Juridical Recording) minimise the number of interfaces needed for multiple National Systems. The PROFIBUS addressing scheme maps NID_NTC values to physical addresses for automatic STM identification.

### Version Compatibility (SUBSET-035)
The X.Y version format with backward compatibility envelope ensures STMs can interoperate with ERTMS/ETCS on-board across different specification versions. Connection management includes version negotiation at connection setup.

## Cross-Source Connections
- SUBSET-035 references SUBSET-026 (SRS), SUBSET-056 (Safe Time Layer), SUBSET-057 (Safe Link Layer), SUBSET-058 (Application Layer), SUBSET-034 (Train Interface), SUBSET-041 (Performance Requirements), SUBSET-101 (Interface 'K'), and ERA_ERTMS_015560 (DMI).
- SUBSET-040 references SUBSET-026, SUBSET-036, SUBSET-091, SUBSET-035, SUBSET-044, SUBSET-054, SUBSET-100, and SUBSET-101.
- Both documents reference SUBSET-026 (System Requirements Specification) as the foundational specification.
- KER compatibility appears in both: SUBSET-040 addresses KER constraints for balise installation, while SUBSET-035 defines Interface 'K' antenna/BTM management for KER STMs.
- The odometer function in SUBSET-035 references performance requirements from SUBSET-041.
