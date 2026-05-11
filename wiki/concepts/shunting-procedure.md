# Shunting Procedure

**Source:** [[subset26-2]] | **Date:** 2026-05-12 | **Type:** concept

ERTMS/ETCS defines two ways to enter Shunting (SH) mode: driver-initiated and trackside-ordered.

## Shunting Initiated by Driver (5.6)

Procedure triggered when the driver selects Shunting from FS, LS, OS, SR, SN, UN, PT, or SB mode (with necessary preconditions). [subset26-2 ¶3880]

### Procedure Steps
1. Driver selects Shunting at standstill (E015) [subset26-2 ¶3880]
2. **Level-dependent path**:
   - **L0/L1**: Immediate transition to SH mode (A050) [subset26-2 ¶3880]
   - **L2/L3**: On-board sends 'Request for Shunting' to RBC. If authorised (optionally with list of balises for SH area), transition to SH. If refused, driver informed (A220). [subset26-2 ¶3880]
   - **NTC**: If National Trip Procedure ongoing, goes to Train Trip procedure. Otherwise immediate transition to SH. [subset26-2 ¶3880]
3. **End of Mission**: If an ongoing mission exists, End of Mission procedure is performed (A100) [subset26-2 ¶3882]
4. **L2/3 session**: Mode change reported to RBC; RBC orders session termination [subset26-2 ¶3882]

### Degraded Situations
- **No RBC response** to Shunting request: message repeated after fixed waiting time. After defined repetitions with no reply, informs driver and terminates session. [subset26-2 ¶3888-¶3890]
- If no authorisation can be obtained, driver may use Override procedure. [subset26-2 ¶3891]
- **No session termination order** from RBC: mode change report repeated; after defined repetitions with no reply, terminates session. [subset26-2 ¶3892-¶3893]

## Entry in Shunting with Order from Trackside (5.7)

Entry via mode profile from balise group (L1) or RBC (L2/3), optionally with list of balises for SH area. [subset26-2 ¶3898]

### Current Location
If max safe front end is at/in advance of the shunting area start, on-board immediately switches to SH mode and displays acknowledgement request. [subset26-2 ¶3904]
- If driver does not acknowledge within driver acknowledgement time, service brake is triggered until acknowledgement. [subset26-2 ¶3905]

### Further Location
Until switch to SH, the beginning of the shunting area is considered as EOA (replacing the MA-derived EOA/LOA). SvL determined either from MA (as if no LOA) or from mode profile. [subset26-2 ¶3914-¶3917]
- Acknowledgement request displayed when distance and speed conditions are met ('rectangle of acknowledgement'). [subset26-2 ¶3910-¶3912]
- Once displayed, acknowledgement request not taken back. [subset26-2 ¶3913]
- Driver acknowledgement triggers immediate switch to SH. [subset26-2 ¶3918]
- If max safe front end reaches shunting area start without driver acknowledgement, switch to SH is forced and acknowledgement requested. [subset26-2 ¶3919]

### Stand By or Post Trip
In L2/3 during SoM or Train Trip procedure, if a mode profile for SH area is received and the train has already entered it, on-board requires driver acknowledgement to transition to SH. [subset26-2 ¶3921-¶3923]

## End of Mission
When switching to SH from FS, LS, OS, SR, SN, or UN, this is considered an End of Mission. [subset26-2 ¶3851]

## Cross-References
- [[etcs-modes]] — SH mode definition
- [[start-of-mission-procedure]] — SoM can lead to SH
- [[train-trip-procedure]] — Trip can lead to SH (L0/NTC without valid Train Data)
- [[override-procedure]] — Alternative when SH request refused
- [[rbc]] — RBC authorises SH in L2/3
- [[subset26-1]] — SH mode description
