# STM States

**Source:** [[subset35]] | **Date:** 2025-03-13 | **Type:** concept

The **STM States** define the eight operational states of a Specific Transmission Module. The STM Manager System within the STM Control Function manages transitions between these states [¶288–§290].

## State Definitions

### NP — No Power
STM is unpowered. No communication possible [¶239–§240].

### PO — Power On
Default state after switch-on. STM synchronises Safe Time Layer, establishes connection with STM Control Function, and sends "Specific NTC Data Need" if required. After receiving bus addresses/safety levels, it may establish further connections. After ETCS status data, it may request CO state [¶241–§247].

### CO — Configuration
STM waits for exchange of configuration data: ETCS data, TIU status/availability, BIU status/availability, odometer performance parameters, brake performance parameters [¶248–§257]. If no Specific NTC Data is needed → requests CS; if in NL/SL mode → requests CS even without all ETCS data; if data is needed → requests DE [¶258–§262].

### DE — Data Entry
For STMs requiring Specific NTC Data for operation. Performed only once at start-up. When terminated → requests CS (even if data not received/skipped/invalid) [¶263–§268].

### CS — Cold Standby
STM is initialised, tested, and configured but not processing trackside information. Reception is off [¶269–§271].

### HS — Hot Standby
STM processes trackside information to be ready for supervision. Can send V_STMMAX, V_STMSYS, D_STMSYS for smooth transitions. May close connections except STM Control when ordered to CS [¶272–§280].

### DA — Data Available
STM is responsible for train movement supervision per national trackside information. This is the fully active state [¶281–§283].

### FA — Failure
STM is unable to work. No messages except state report are sent [¶284–§286].

## Transitions

State transitions are triggered by ETCS orders (Configuration, Data Entry, Cold Standby, Hot Standby, Data Available, Failure) or STM decisions. The STM Control Function manages these transitions based on current conditions [¶291–§297].

## Cross-references
- [[Specific Transmission Module (STM)]] — entity that uses these states
- [[STM Control Function]] — manages state transitions
- [[STM Manager System]] — handles state orders and reports
- [[subset35]] — source document
