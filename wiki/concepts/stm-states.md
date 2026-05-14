# STM States

**Source:** [[subset35]], [[subset58]] | **Date:** 2025-07-17 | **Type:** concept

The STM operates in one of eight states, managed by the [[stm-control-function]]. The states define the STM's lifecycle from power-on through active supervision.

## State Definitions

| State | Code | Description |
|-------|------|-------------|
| No Power | NP | STM is unpowered [subset58 ¶240] |
| Power On | PO | Default state after switch-on; performs Safe Time Layer synchronisation and establishes connection to STM Control Function [subset58 ¶242]-[subset58 ¶247] |
| Configuration | CO | Waiting for all configuration data to be exchanged (ETCS data, TIU/BIU status, odometer/brake parameters) [subset58 ¶249]-[subset58 ¶262] |
| Data Entry | DE | Used by STMs requiring Specific NTC Data from the driver [subset58 ¶264]-[subset58 ¶268] |
| Cold Standby | CS | Initialised, configured, and in possession of all required information but trackside reception is turned off [subset58 ¶270] |
| Hot Standby | HS | Can process information from/to national trackside, can send STM max speed and system speed/distance [subset58 ¶273]-[subset58 ¶280] |
| Data Available | DA | STM is responsible for train movement supervision [subset58 ¶282] |
| Failure | FA | STM cannot work due to internal or external reasons; must not send messages on the bus except to report FA state [subset58 ¶285]-[subset58 ¶286] |

## Application Layer Representation (SUBSET-058)

Three variables encode state information in packets [subset58 ¶380]-[subset58 ¶385]:

- **NID_STMSTATE** (4 bits): Current STM state reported by the STM. Values: 0=reserved, 1=PO, 2=CO, 3=DE, 4=CS, 5=reserved(→CS), 6=HS, 7=DA, 8=FA, 9-15=spare. [subset58 ¶380]-[subset58 ¶381]
- **NID_STMSTATEORDER** (4 bits): State ordered by ERTMS/ETCS on-board. Values: 0=reserved, 1=reserved, 2=CO, 3=DE, 4=U-CS, 5=C-CS, 6=HS, 7=DA, 8=FA, 9-15=spare. [subset58 ¶382]-[subset58 ¶383]
- **NID_STMSTATEREQUEST** (4 bits): State requested by the STM. Values: 0=reserved, 1=reserved, 2=CO, 3=DE, 4=CS, 5=reserved(→CS), 6-8=reserved, 9-15=spare. [subset58 ¶384]-[subset58 ¶385]

## State Transitions

The STM transitions through states in a defined order: NP → PO → CO → (DE →) CS → HS → DA. Transitions are triggered by STM-14 (state order) or STM-13 (state request) packets. Invalid transition orders cause the STM to enter FA state [subset58 ¶303].

## Key Rules

- Only one STM can be active (in DA state) at a time [subset58 ¶78]
- The STM reports its NID_STM and current state with every application message [subset58 ¶304]-[subset58 ¶307]
- FA state is reported if possible; the STM may be unable to report due to the failure itself [subset58 ¶310]
- Packet sending permissions vary by state (specified for each packet definition in SUBSET-058)

## Cross-references
- [[stm]] — The Specific Transmission Module entity
- [[stm-control-function]] — Manages STM states and transitions
- [[connection-management]] — Connection opening and closing
- [[fffis-stm-application-layer]] — Application Layer protocol