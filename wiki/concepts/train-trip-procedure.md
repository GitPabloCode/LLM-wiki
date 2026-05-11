# Train Trip Procedure

**Source:** [[subset26-2]] | **Date:** 2026-05-12 | **Type:** concept

The Train Trip procedure is triggered when an event occurs that causes a train trip, such as passing the End of Movement Authority, a linking error, a radio connection time-out, or receiving an emergency stop. [subset26-2 ¶4187-¶4188]

## Procedure Steps

1. **Trip Triggered** (S010): Events leading to train trip from FS, LS, OS, SR, SB, SH, SN, or UN. [subset26-2 ¶4192]

2. **Mode Change to TR** (A025): On-board switches to Trip mode. [subset26-2 ¶4192]

3. **Level-dependent Actions** (D020):
   - **L1**: Proceed to A035 [subset26-2 ¶4192]
   - **L2/3**: Report mode change to RBC (A030), then proceed [subset26-2 ¶4192]
   - **L0/NTC**: Proceed to S050 [subset26-2 ¶4192]

4. **Delete MA/Track Description** (A035): All current MA and track description data (except track conditions) deleted; new ones not accepted. [subset26-2 ¶4192]

5. **Awaits Standstill** (S050): Braking continues even across level borders. [subset26-2 ¶4192]

6. **Driver Acknowledges** (S060): Request for acknowledgement displayed. Driver acknowledges (E065). [subset26-2 ¶4192]

7. **Post-Acknowledgement Path** (D080):
   - **L1/2/3**: → PT mode (A105). Emergency brake command revoked. [subset26-2 ¶4194]
   - **L0/NTC without valid Train Data**: → SH mode (A140) [subset26-2 ¶4194]
   - **L0 with valid Train Data**: → UN mode (A145) [subset26-2 ¶4194]
   - **NTC with valid Train Data**: → SN mode (A150) [subset26-2 ¶4194]

## Post Trip (PT) Mode

After entering PT:
- **L1**: Driver can select Start (→SR) or SH [subset26-2 ¶4195]
- **L2/3**: Report mode change to RBC. RBC acknowledges (Recognition of exit from TR). If pending emergency stops exist, wait for revocation. Then driver can select Start or SH. [subset26-2 ¶4194-¶4195]
  - Start → MA request: SR authorisation (→SR), OS/LS/SH MA (→acknowledge), FS MA (→FS) [subset26-2 ¶4195]

## Degraded Situations

- **No RBC acknowledgement for PT mode**: Mode change report repeated. After defined repetitions with no reply, terminate communication session. [subset26-2 ¶4201-¶4203]
- **Accidental session loss in L2/3 PT mode**: Driver can select Override (if conditions met). [subset26-2 ¶4204]

## Cross-References
- [[etcs-modes]] — TR and PT mode definitions
- [[override-procedure]] — Alternative when RBC unreachable
- [[rbc]] — RBC communication during trip
- [[start-of-mission-procedure]] — Post-trip can lead to SoM-like flow
- [[information-acceptance]] — What information is accepted in TR/PT modes
- [[stored-information-mode-level-actions]] — What happens to stored data on entering TR/PT
- [[subset26-1]] — Trip conditions
