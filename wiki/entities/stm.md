# Specific Transmission Module (STM)

**Source:** [[subset35]] | **Date:** 2025-03-13 | **Type:** entity

The **Specific Transmission Module (STM)** is the interface component that connects ERTMS/ETCS on-board equipment to National Train Control (NTC) systems. Defined in SUBSET-035, it enables any ERTMS/ETCS on-board to connect to any STM, ensuring interchangeability [¶66](http://localhost:8765/go.html#subset35-66).

## Identification

Each STM is uniquely identified by `NID_STM`, which equals `NID_NTC` values from ERA_ERTMS_040001 [¶76](http://localhost:8765/go.html#subset35-76). STM uses common Reference Time from ERTMS/ETCS on-board [¶77](http://localhost:8765/go.html#subset35-77). Only one STM is active (supervising) at a time [¶78](http://localhost:8765/go.html#subset35-78).

## Interfaces

STM communicates with the following ERTMS/ETCS on-board functions via PROFIBUS [¶85–§96]:
- **DMI** — driver interaction for national system information
- **STM Control Function** — state and data management
- **Reference Time** — common time synchronisation
- **Brake Interface (BIU)** — emergency/service brake commands
- **Train Interface (TIU)** — train command signals
- **Juridical Data** — national recording data
- **Odometer** — speed/distance estimation

## Physical Connection

STM connects via PROFIBUS (RS-485, 1500 Kbps) with a 9-pin D-SUB connector [¶149–§167]. Default PROFIBUS address = `NID_NTC + 70` [¶191](http://localhost:8765/go.html#subset35-191).

## States

STM operates in eight states: NP (No Power), PO (Power On), CO (Configuration), DE (Data Entry), CS (Cold Standby), HS (Hot Standby), DA (Data Available), FA (Failure) [¶239–§286].

## Safety

STM implements safety protocol levels SL4, SL2, or SL0 depending on its SIL [¶174–§181]. ERTMS/ETCS on-board monitors the interface safety integrity and applies emergency brake on active STM failure [¶79–§80].

## Cross-references
- [[STM Control Function]] — manages STM state and data exchange
- [[STM Manager System]] — handles STM state transitions
- [[STM States]] — the eight-state machine
- [[PROFIBUS]] — physical bus interface
- [[Odometer Function]] — speed/distance interface
- [[Train Interface Unit]] — train command signals
- [[Brake Interface Unit]] — brake command signals
- [[Juridical Data Recording]] — national recording interface
- [[DMI STM]] — driver interface for STM
- [[STM Connection Management]] — version check and connection setup
- [[STM Version Management]] — X.Y version format
- [[Specific NTC Data Entry]] — national data entry procedure
- [[STM Safety Protocols]] — SL4, SL2, SL0
- [[subset35]] — source document
