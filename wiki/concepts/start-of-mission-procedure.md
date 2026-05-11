# Start of Mission Procedure

**Source:** [[subset26-2]] | **Date:** 2026-05-12 | **Type:** concept

The Start of Mission (SoM) procedure begins when the ERTMS/ETCS on-board equipment is in Stand-By mode with a desk open and no communication session is established or being established. [subset26-2 ¶3795]

## Data Status at Start

At the beginning of SoM, data may be in one of three states: valid, invalid, or unknown. This applies to Driver ID, ERTMS/ETCS level, RBC ID/phone number, Train Data, Train Running Number, and Train Position. [subset26-2 ¶3784-¶3791]

## Procedure Steps

The SoM procedure follows a defined flowchart with numbered steps (S0, S1, S2...):

1. **Driver ID Entry** (S1): Driver enters/revalidates Driver ID. Option to enter Train Running Number and set/remove Virtual Balise Cover. [subset26-2 ¶3795]

2. **Level Validation** (D2, S2): If stored position and level are valid, proceeds. If invalid/unknown, driver enters/revalidates level. [subset26-2 ¶3795]

3. **Radio Network & RBC Session** (D7, S3, A31): For L2/3 with valid position, opens communication session with RBC. If no Mobile Terminal registered, waits for registration or informs driver of failure (A29). Driver may select/re-enter Radio Network ID and RBC ID/phone number. [subset26-2 ¶3795-¶3797]

4. **Position Validation** (D32, A33-A35, D22, A23-A24): If stored position is valid, sends 'SoM position report' to RBC. If invalid/unknown, sends marked position report; RBC may validate it (A35), accept train without valid position (A24), or reject the train (A38-A40). [subset26-2 ¶3801-¶3802]

5. **Data Entry & Start** (S10-S25): After session established and data collected, driver is offered options:
   - Select SH (Shunting)
   - Select NL (Non Leading)
   - Select Train Data Entry → then Train Running Number
   - Select 'Start' → mode transition based on level:
     - Level 0 → UN mode (driver acknowledges) [subset26-2 ¶3800]
     - Level NTC → SN mode (driver acknowledges) [subset26-2 ¶3800]
     - Level 1 → SR mode (driver acknowledges) [subset26-2 ¶3800]
     - Level 2/3 → sends MA request to RBC; may receive SR authorisation (→SR), OS/LS/SH MA (→OS/LS/SH), or FS MA (→FS) [subset26-2 ¶3800-¶3801]

## Degraded Situations

- Accidental loss of session: if above D11, nominal procedure applies; if further, returns to S10 [subset26-2 ¶3818]
- Driver can at S10/S20: re-enter Driver ID, Train Running Number, Level, Radio data; select Override (if conditions met); set/remove Virtual Balise Cover [subset26-2 ¶3820-¶3838]

## End Condition

The SoM procedure ends when a transition to any mode other than SB occurs, or when the desk is closed. If the driver closes the desk, any communication session with RBC is terminated. [subset26-2 ¶3803-¶3806]

## Mission Status

A mission is considered started when the on-board equipment enters FS, LS, SR, OS, NL, UN, or SN mode from SB. Entry into other modes from SB is not considered a mission. [subset26-2 ¶3839-¶3841]

## Cross-References
- [[etcs-modes]] — SB, FS, LS, SR, OS, UN, SN, NL modes
- [[ertms-etcs-onboard]] — On-board equipment
- [[rbc]] — RBC session management
- [[override-procedure]] — Override available during SoM in L2/3
- [[shunting-procedure]] — Shunting initiated from SoM
- [[subset26-1]] — Core SRS principles
