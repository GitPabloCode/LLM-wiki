# Joining/Splitting Procedure

**Source:** [[subset26-2]] | **Date:** 2026-05-12 | **Type:** concept

Procedures for splitting a train into two parts or joining two trains into one.

## Definitions (5.14.1)

- **Splitting**: 'Train to be split' at standstill. 'Front train after splitting' = front part. 'New train after splitting' = other part. [subset26-2 ¶4254]
- **Joining**: 'Train to be joined' = train at standstill. 'Joining train' = train performing the operation. [subset26-2 ¶4255]

## Splitting Procedure (5.14.2)

1. **Step 1**: Remove electrical and mechanical links between the two trains (national operational procedure, outside SRS scope). [subset26-2 ¶4257]
   - If splitting requires moving parts apart, this can be done even in SB mode. [subset26-2 ¶4258]
2. **Step 2a** (leading engine): If no end of mission was performed, driver modifies Train Data to fit the new composition. For L2/3, new Train Data sent to RBC. [subset26-2 ¶4259]
3. **Step 2b** (SL engine of new train): Switches to SB when remote control signal no longer received. L2/3: opens communication session and reports mode change. [subset26-2 ¶4260]
4. **Step 2c** (NL engine of new train): Switches to SB when non leading input signal no longer received. [subset26-2 ¶4261]
5. Driver can start a new mission (SoM), begin shunting, or not move the train. [subset26-2 ¶4262]

## Joining Procedure (5.14.3)

1. **Step 1**: Joining train approaches train to be joined — in SR, OS, or SH mode (depending on information and national procedure). [subset26-2 ¶4264]
2. **Step 2**: Close electrical and mechanical links between trains (outside ETCS scope). [subset26-2 ¶4265]
3. **Step 3a** (remaining leading): If no end of mission, driver modifies Train Data. L2/3: new data sent to RBC. [subset26-2 ¶4266]
4. **Step 3b** (becoming SL slave): Closing desk → SB → End of Mission. Transition to SL from SB. [subset26-2 ¶4267]
5. **Step 3c** (becoming NL slave): Driver selects NL mode. [subset26-2 ¶4268]
6. For further steps: see [[start-of-mission-procedure]] and [[change-of-train-orientation]]. [subset26-2 ¶4269]

## Cross-References
- [[etcs-modes]] — SB, SL, NL, SR, OS, SH modes
- [[start-of-mission-procedure]] — Mission start after joining/splitting
- [[change-of-train-orientation]] — Further steps after joining
- [[end-of-mission-procedure]] — End of Mission when becoming slave
- [[subset26-1]] — Principles
