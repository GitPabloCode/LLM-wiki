# Level Transition

**Source:** [[subset40]] | **Date:** 2026-05-07 | **Type:** concept

**Level transition** is the process of changing between ETCS operational levels (e.g., Level 1, Level 2, STM) during train operation.

## Rules from SUBSET-040

### Border Location (§4.1.4)
Level transition borders and RBC/RBC handover borders shall **not** be located where shunting or reversing could take place [¶99](http://localhost:8765/go.html#subset40-99). These areas are not handled in Shunting/Reversing modes, per SUBSET-026 §§3.15.4.6 and 4.4.8.1.5 [¶99](http://localhost:8765/go.html#subset40-99).

### Immediate Level Transition (§4.2.1)
A balise group giving an MA or immediate level transition order must be ≥ **1.3 m** in rear of EOA/LOA. Exception: if the level transition is announced and executed before the EoA/LoA is passed [¶65](http://localhost:8765/go.html#subset40-65).

### Level Transition Announcement (§4.2.4)
Trackside shall announce all applicable **NID_STM** values for national systems installed [¶135](http://localhost:8765/go.html#subset40-135).

### In-fill Level Transition
For immediate level transition in in-fill, **D_LEVELTR = 0 m** [¶116](http://localhost:8765/go.html#subset40-116).

### STM Level Transition
All engineering requirements for Level transition involving STM from SUBSET-035 §7.5 must be respected [¶140](http://localhost:8765/go.html#subset40-140).

## Cross-references
- [[In-fill]] — level transitions via in-fill messages
- [[RBC]] — RBC handover borders
- [[EOA]] — EOA reference for level transition positioning
- [[subset40]] — source document
