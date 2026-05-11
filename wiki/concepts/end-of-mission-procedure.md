# End of Mission Procedure

**Source:** [[subset26-2]] | **Date:** 2026-05-12 | **Type:** concept

The End of Mission procedure is triggered when the ERTMS/ETCS on-board equipment enters Stand-By or Shunting mode from operational modes.

## Entry to Mode Considered as End of Mission (5.5.2)

### Stand-By mode
- Entering SB from FS, LS, OS, UN, NL, SR, PT, RV, or SN → End of Mission [subset26-2 ¶3847]
- Entering SB from PT → End of Mission only if there was an ongoing mission [subset26-2 ¶3849]
- While in SN mode (level NTC), additional conditions may depend on the National System. [subset26-2 ¶3848]

### Shunting mode
- Entering SH from FS, LS, OS, SR, SN, or UN → End of Mission [subset26-2 ¶3851]
- Entering SH from PT → End of Mission only if there was an ongoing mission [subset26-2 ¶3852]

## Procedure Steps (5.5.3)

1. **Step 1**: MA, Track Description Data, and Train Data may be deleted (mode dependent, see [[stored-information-mode-level-actions]]). If no communication session exists, procedure ends. [subset26-2 ¶3856-¶3857]
2. **Step 2 (with RIU session)**: Terminate communication session with RIU. [subset26-2 ¶3858-¶3859]
3. **Step 2 (with RBC session)**: Report end of mission to RBC via 'End of Mission' message (contains position report). [subset26-2 ¶3861]
4. **Step 3**: RBC requests session termination. [subset26-2 ¶3862]
5. **Step 4**: On-board terminates communication session. [subset26-2 ¶3863]

## Degraded Situation (5.5.4)

In L2/3: If no termination request received from RBC within fixed waiting time after sending 'End of Mission', the message is repeated. After defined number of repetitions with no reply, on-board terminates session. [subset26-2 ¶3868-¶3870]

If no communication session is open, no session is established to report end of mission. [subset26-2 ¶3871]

## Cross-References
- [[etcs-modes]] — SB, SH modes
- [[start-of-mission-procedure]] — Follows End of Mission
- [[change-of-train-orientation]] — End of Mission occurs during cab change
- [[shunting-procedure]] — End of Mission occurs on SH entry from operational modes
- [[stored-information-mode-level-actions]] — Data deletion on mode entry
- [[rbc]] — RBC session termination
- [[subset26-1]] — Principles
