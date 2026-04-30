# STM States

**Source:** [subset35](../summaries/subset35.md) | **Date:** 2026-04-29 | **Type:** concept

The **STM states** define the lifecycle of a Specific Transmission Module from power-off to active train supervision. The ERTMS/ETCS on-board's STM Control Function manages state transitions and enforces the rule that only one STM can be in the Data Available (DA) state at a time. The eight states form a mostly linear progression with the Failure (FA) state reachable from any other state. [¶238-274]

## The eight states

### NP — No Power
The STM is unpowered. No communication is possible. This is the initial and terminal state (before startup and after shutdown). [¶239-240]

### PO — Power On
Default state entered after power-up. The STM synchronises the Safe Time Layer and establishes a connection to the STM Control Function. Once the STM Control Function sends ETCS status data, the STM may request CO state. The STM also indicates whether it requires Specific NTC Data. [¶241-247]

### CO — Configuration
The STM waits for all configuration data from the ERTMS/ETCS on-board: ETCS data, TIU and BIU status/availability, odometer performance parameters, and brake performance parameters. Once complete, the STM either transitions to Data Entry (DE) if it needs Specific NTC Data, or directly to Cold Standby (CS) if it does not. [¶248-262]

### DE — Data Entry
Entered only once at startup by STMs that require Specific NTC Data. The Specific NTC Data Entry procedure runs, enabling the driver to input national operational data. Once complete (or skipped), the STM requests Cold Standby state. [¶263-268]

### CS — Cold Standby
The STM is initialised, configured, and in possession of all required information, but its trackside reception is turned off. It is prepared but not yet processing national trackside messages. [¶269-271]

### HS — Hot Standby
The STM is actively processing national trackside information and is prepared to take over supervision. It can send STM max speed and STM system speed/distance to the ERTMS/ETCS on-board to facilitate smooth level transitions. Multiple STMs can be in HS simultaneously. [¶272-278]

### DA — Data Available
The STM is actively supervising the train. Only one STM can be in this state. The STM has full access to DMI, TIU commands, and BIU commands. The ERTMS/ETCS on-board monitors the active STM's safety integrity and applies the emergency brake on failure. [¶78-79]

### FA — Failure
The STM has detected a failure. It can no longer supervise the train. Reachable from any other state. [¶274]

## State transitions

States follow a defined transition order managed by the STM Control Function. Transitions are requested by the STM and authorised by the Control Function based on the current state and received data. [¶119, 248-278]

## Cross-references
- [STM](../entities/stm.md) — the device whose lifecycle these states govern
- [STM Control Function](../entities/stm-control-function.md) — the function that manages state transitions
- [FFFIS](fffis.md) — the specification concept defining this state machine
- [STM Version Check](stm-version-check.md) — the version negotiation that runs during PO and CO transitions
- [subset35](../summaries/subset35.md) — the FFFIS STM specification
