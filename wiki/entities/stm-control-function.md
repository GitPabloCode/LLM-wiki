# STM Control Function

**Source:** [[subset35]] | **Date:** 2025-03-13 | **Type:** entity

The **STM Control Function** is the ERTMS/ETCS on-board function that manages STM state transitions, controls communication, and distributes data between ERTMS/ETCS on-board and STMs. It is the central coordination point for STM interaction [¶118–§130].

## Responsibilities

- **STM State Management** — Sends state orders (Configuration, Data Entry, Cold Standby, Hot Standby, Data Available, Failure) to STMs based on conditions [¶339–§356].
- **Association Management** — Maps NID_NTC to one or more NID_STM with priority; selects the appropriate STM for a given Level NTC [¶325–§338].
- **ETCS Data Distribution** — Provides subsets of ETCS Train Data, Additional Data, National/Default Values to STMs [¶381–§414].
- **ETCS Status Data** — Sends current mode and level to all connected STMs [¶415–§418].
- **Language** — Transmits language to all STMs [¶419–§422].
- **Specific NTC Data Entry** — Manages the driver dialogue for national system data entry [¶424–§476].
- **Specific NTC Data View** — Allows driver to view national data values [¶482–§489].
- **Test Procedure** — Grants permission for STM self-test [¶490–§495].
- **Override** — Manages override activation across systems [¶497–§506].
- **Airgap Messages** — Forwards RBC/balise group messages to the associated STM [¶509–§513].
- **Speed/Distance Supervision** — Incorporates V_STMMAX and V_STMSYS/D_STMSYS into MRSP [¶514–§531].
- **Interface 'K' Management** — Indicates active Antenna/BTM to KER STMs [¶539–§543].
- **BTM Alarm Data** — Sends BTM alarm status to all STMs [¶545–§549].

## STM Availability

STM Control Function maintains a configurable list of STMs and tracks which are available (CS, HS, DA states) [¶312–§314]. If Level NTC X is selected and STM X is not available, emergency brake is applied (unless isolated via Train Interface) [¶365–§372].

## Cross-references
- [[Specific Transmission Module (STM)]] — the module being controlled
- [[STM Manager System]] — state handling subsystem within STM Control
- [[STM States]] — state machine managed by the function
- [[Specific NTC Data Entry]] — data entry procedure
- [[PROFIBUS]] — communication medium
- [[subset35]] — source document
