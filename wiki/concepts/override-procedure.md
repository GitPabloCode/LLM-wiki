# Override Procedure

**Source:** [[subset35]], [[subset58]] | **Date:** 2025-07-17 | **Type:** concept

The Override procedure (Trip Inhibition, Pass Stop, or Pass signal at danger) provides a coordinated override capability for both the active system and the system to be activated, without applying brakes by both systems [subset58 ¶498].

## Application Layer Packets (SUBSET-058)

- **STM-6** (val=6): Override Activation — sent by STM to STM Control Function in DA state to report activation of the Override procedure. No additional variables beyond header. [subset58 ¶137]-[subset58 ¶138]
- **STM-7** (val=7): Override Status — sent by STM Control Function to all STMs in PO, CO, DE, CS, HS, DA states to report a change in ETCS Override status. Contains Q_OVR_STATUS (1 bit: 0=not active, 1=active). [subset58 ¶139]-[subset58 ¶140]
- **Q_OVR_STATUS** (variable): 1-bit qualifier indicating whether ETCS Override status is active or not. [subset58 ¶432]-[subset58 ¶433]

## Mechanism

- When Override is activated in the active system (ETCS or STM), all on-board systems receive notification via STM-7 [subset58 ¶499]
- Each system independently monitors its specific Override limits (time, distance, trackside info) and trip inhibition
- After a level transition, the newly activated system can immediately have its Override function active [subset58 ¶500]

## ETCS Override Activation in Level NTC

- ETCS Override status is activated when in level NTC and the ERTMS/ETCS on-board receives an activation report (STM-6) from the active STM [subset58 ¶502]
- The ETCS Override function is reset each time a new activation report is received from the active STM [subset58 ¶503]
- ERTMS/ETCS on-board reports its Override status to all connected STMs whenever it changes and at connection establishment via STM-7 [subset58 ¶504]-[subset58 ¶506]

## Supervision During Override

If Override is active while in Mode SN, no speed supervision is performed by the ERTMS/ETCS on-board or any connected STMs except for the active STM [subset58 ¶508].

## Cross-references
- [[stm-control-function]] — Handles the Override procedure
- [[stm]] — The Specific Transmission Module
- [[stm-states]] — STM state definitions
- [[fffis-stm-application-layer]] — Application Layer protocol
