# SUBSET-035: ERTMS/ETCS Specific Transmission Module FFFIS

**Source:** [[subset35]] | **Date:** 2025-03-13 | **Type:** summary

SUBSET-035 (Issue 3.2.0, 2015-12-16) defines the **Form Fit Functional Interface Specification (FFFIS)** for the **Specific Transmission Module (STM)** — the interface between ERTMS/ETCS on-board equipment and National Train Control (NTC) systems. Developed by UNISIG [¶0–¶7], its objective is to enable any ERTMS/ETCS on-board to connect to any STM, ensuring interchangeability [¶66](http://localhost:8765/go.html#subset35-66).

The document covers all protocol levels from the PROFIBUS physical connector up to the application layer functions [¶63–¶65].

## Key Areas

- **Functional Architecture** — STM communicates with: DMI, STM Control Function, Reference Time, Brake Interface (BIU), Train Interface (TIU), Juridical Data, and Odometer [¶85–¶96].
- **PROFIBUS Bus** — Physical layer using RS-485, 1500 Kbps, 9-pin D-SUB connector, addressing scheme mapping NID_NTC to PROFIBUS addresses [¶149–§192].
- **Safety Protocol Levels** — Three levels: SL4, SL2, SL0, mapped to equipment SIL [¶174–§181].
- **STM States** — Eight states: NP (No Power), PO (Power On), CO (Configuration), DE (Data Entry), CS (Cold Standby), HS (Hot Standby), DA (Data Available), FA (Failure) [¶239–§286].
- **STM Control Function** — Manages state transitions, association of STM X to Level NTC X, ETCS data distribution, Specific NTC Data Entry/View, Test Procedure, Override, airgap messages, speed/distance supervision, Interface 'K' antenna management, BTM alarm data [¶312–§549].
- **Train Interface (TIU)** — Command and status signals for regenerative brake, magnetic shoe brake, eddy current brake, pantograph, air tightness, main switch, traction cut off [¶101–§111].
- **Brake Interface (BIU)** — Emergency and service brake commands and status, physically separated with different safety levels [¶112–§115].
- **Odometer** — Speed/distance estimation with confidence intervals, min/max ranges [¶561–§598].
- **DMI** — Driver-Machine Interface for national system interaction: text messages, indicators, buttons, sounds, supervision information, with unified and customisable services [¶600–§753].
- **Version Management** — Format X.Y (0-255); X distinguishes incompatible versions, Y indicates compatibility within X; backward compatibility envelope [¶776–§796].
- **Connection Management** — Version check on connection; STM initiates; compatibility rules for version negotiation [¶215–§237].

## Cross-references
- [[STM]] — the Specific Transmission Module entity
- [[STM Control Function]] — manages STM state and data exchange
- [[STM Manager System]] — state handling and transitions
- [[STM States]] — the eight-state machine (NP, PO, CO, DE, CS, HS, DA, FA)
- [[PROFIBUS]] — the physical bus interface
- [[Odometer Function]] — speed/distance estimation interface
- [[Train Interface Unit]] — train command/status signals
- [[Brake Interface Unit]] — emergency/service brake commands
- [[Juridical Data Recording]] — national recording interface
- [[DMI STM]] — DMI interface for STM
- [[STM Connection Management]] — version check and connection setup
- [[STM Version Management]] — X.Y version format and compatibility
- [[Specific NTC Data Entry]] — national data entry procedure
- [[STM Safety Protocols]] — SL4, SL2, SL0 safety levels
- [[STM Customisable DMI Service]] — configurable DMI layouts
- [[subset40]] — related dimensioning and engineering rules
