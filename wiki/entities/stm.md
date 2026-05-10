# Specific Transmission Module (STM)

**Source:** [[subset35]], [[subset58]] | **Date:** 2025-07-17 | **Type:** entity

The Specific Transmission Module (STM) is the interface component that allows ERTMS/ETCS on-board equipment to communicate with legacy National Train Control (NTC) systems. Each STM is identified by a unique NID_STM number, which corresponds to a NID_NTC value [subset58 ¶76]. The NID_STM variable in the Application Layer is an 8-bit value (0-254), with 255 reserved for multicast [subset58 ¶378]-[subset58 ¶379].

## Key Characteristics

- **Identification:** Each STM is identified by NID_STM, equal to one of the NID_NTC values from the ERA assignment list [subset58 ¶76]
- **Only one STM active at a time** — the active STM is responsible for train movement supervision [subset58 ¶78]
- **Physical bus address:** Default address = NID_NTC + 70, with a configurable range (50-69) for out-of-range cases [subset58 ¶191]-[subset58 ¶194]
- **Isolation:** An STM can be isolated from the bus without disturbing other bus functions [subset58 ¶82]

## States

An STM operates in one of eight states: NP, PO, CO, DE, CS, HS, DA, FA — managed by the [[stm-control-function]] [subset58 ¶238]-[subset58 ¶287]. The state is encoded in the 4-bit variable NID_STMSTATE [subset58 ¶380]-[subset58 ¶381], state orders use NID_STMSTATEORDER [subset58 ¶382]-[subset58 ¶383], and state requests use NID_STMSTATEREQUEST [subset58 ¶384]-[subset58 ¶385].

## Application Layer Packets

The STM sends and receives Application Layer packets (defined in SUBSET-058) that are grouped by function:

- **Version and connection:** STM-1 (version number N_VERMAJOR/N_VERMINOR, implicitly carries connection request/confirmation) [subset58 ¶128]-[subset58 ¶129]
- **State management:** STM-15 (state report from STM), STM-13 (state request), STM-14 (state order to STM) [subset58 ¶130]-[subset58 ¶144]
- **Transition data:** STM-16 (STM max speed V_STMMAX), STM-17 (STM system speed V_STMSYS and distance D_STMSYS) [subset58 ¶145]-[subset58 ¶148]
- **Override:** STM-6 (override activation from STM) [subset58 ¶137]-[subset58 ¶138]
- **National Trip Procedure:** STM-18 (indication to ETCS that STM is in National Trip) [subset58 ¶149]-[subset58 ¶150]
- **Test:** STM-21 (test permission request), STM-23 (end of test with result) [subset58 ¶176]-[subset58 ¶181]
- **Juridical Data:** STM-161 (national data to JD with timestamp T_JD) [subset58 ¶229]-[subset58 ¶230]

## Functions Available to STMs

The STM can access ERTMS/ETCS on-board functions including the [[dmi-function]], [[tiu-function]], [[biu-function]], [[odometer-function]], [[juridical-data-function]], and reference time — with access rights varying by ETCS mode/level [subset58 ¶139]-[subset58 ¶146].

## Safety Monitoring

The ERTMS/ETCS on-board monitors the STM interface safety integrity and applies emergency brake in case of failure of the active STM [subset58 ¶79].

## Cross-references
- [[stm-control-function]] — Controls STM states and version compatibility
- [[stm-states]] — The eight STM operational states
- [[dmi-function]] — Driver Machine Interface
- [[tiu-function]] — Train Interface Unit
- [[biu-function]] — Brake Interface Unit
- [[odometer-function]] — Odometry data provision
- [[juridical-data-function]] — Juridical recording
- [[profibus]] — The PROFIBUS communication bus
- [[fffis-stm-application-layer]] — Application Layer protocol
- [[connection-management]] — Connection opening and version check
- [[specific-ntc-data-entry]] — National data entry procedure
