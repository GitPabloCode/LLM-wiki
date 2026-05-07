# STM Manager System

**Source:** [[subset35]] | **Date:** 2025-03-13 | **Type:** entity

The **STM Manager System** is the subsystem within the STM Control Function that handles STM state transitions and maintains the state machine. It defines how STMs move between the eight operational states [¶288–§290].

## Scope

Defines all state handling for STMs, including transition conditions between NP, PO, CO, DE, CS, HS, DA, and FA [¶288–§290].

## Transition Rules

- State transitions are triggered by ETCS orders (Configuration, Data Entry, Cold Standby unconditional/conditional, Hot Standby, Data Available, Failure) and STM decisions [¶296–§297].
- STM in DA executing National Trip Procedure sends "National Trip Procedure" cyclically to fulfil timeout [¶298](http://localhost:8765/go.html#subset35-298).
- If mode changes to TR, STM is expected to enter CS even if National Trip Procedure is not finished [¶298](http://localhost:8765/go.html#subset35-298).
- STM antenna is only energised in HS/DA or for test [¶300–§302].
- Invalid state order → FA [¶303](http://localhost:8765/go.html#subset35-303).
- STM reports NID_STM and current state on all point-to-point connections with each message and on state change [¶304–§308].

## Cross-references
- [[STM Control Function]] — parent entity
- [[STM States]] — the state machine definitions
- [[Specific Transmission Module (STM)]] — the module being managed
- [[subset35]] — source document
