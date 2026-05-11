# Override Procedure

**Source:** [[subset26-2]], [[subset35]], [[subset58]] | **Date:** 2026-05-12 | **Type:** concept

The Override procedure allows a train to pass its End of Movement Authority in specific degraded situations, such as failed signals, failed track circuits, radio unavailability, or RBC unreachability. [subset26-2 ¶3928-¶3935]

## ETCS Override Procedure (from SUBSET-026-2)

### Selection Conditions (5.8.2)
The driver can select 'Override' only when:
- Train speed ≤ speed limit for triggering override (national value) [subset26-2 ¶3949]
- Current mode is FS, LS, OS, SR, SH, UN, PT, SB (L2/3 only), or SN [subset26-2 ¶3950]
- Validated Train Data and Train Running Number available (except when already in SH) [subset26-2 ¶3951]

### Mode Change on Override (5.8.3)
- From FS, LS, OS, SB, PT: → SR mode [subset26-2 ¶3956]
- From SH: remains SH [subset26-2 ¶3957]
- From UN/SN: changes to SR only when level changes to L1/2/3 [subset26-2 ¶3958]

### Active Override Effects
- If mode was OS, LS, or FS: former EOA/LOA retained [subset26-2 ¶3959]
- If mode was SB or PT: current train front position considered as former EOA/LOA [subset26-2 ¶3959]
- The former EOA/LOA is deleted if train reads 'stop if in SR mode' or if SR mode is left [subset26-2 ¶3962-¶3964]
- In L2/3: RBC informed of override via mode change report [subset26-2 ¶3965]
- RBC may transmit SR distance limits and list of balises [subset26-2 ¶3966]
- Override revokes all previously received emergency stop orders in L2/3 [subset26-2 ¶3967]
- Driver may modify SR mode speed limit and distance [subset26-2 ¶3968]
- Train trip is inhibited; MRSP includes Override function related Speed Restriction [subset26-2 ¶3969]
- 'Override active' indicated to driver (exceptions: activated by STM, or in level NTC after transition) [subset26-2 ¶3970-¶3972]
- New SR distance from EUROLOOP rejected while override active [subset26-2 ¶3973]
- Re-selecting Override while already active restarts time and distance supervision [subset26-2 ¶3974]

### End of Override (5.8.4)
Override ends when any of:
a) Max time for train trip suppression elapses (national value) [subset26-2 ¶3977]
b) Train runs more than distance for trip suppression (national value) [subset26-2 ¶3978]
c) Former EOA/LOA passed with min safe antenna position [subset26-2 ¶3979]
d) Train passes 'stop if in SR' or 'stop if in SH' balise group [subset26-2 ¶3980]
e) Train passes balise group giving proceed information (MA with no zero speed restriction) [subset26-2 ¶3981]
f) In L2/3, MA received from RBC [subset26-2 ¶3982]
g) Train passes balise group not in expected list for SR or SH mode [subset26-2 ¶3983]
h) Train overpasses SR distance with estimated front end [subset26-2 ¶3984]
i) On-board switches to TR, LS, OS, or SH mode [subset26-2 ¶3985]

For UN and SN modes, only conditions a) and b) are supervised. [subset26-2 ¶3986]

## STM-Level Override Coordination (from SUBSET-035/058)

The Override procedure provides a coordinated capability across both ETCS and STM systems [subset58 ¶498].

See [[stm-control-function]] for STM-override packet details.

## Cross-References
- [[etcs-modes]] — SR, SH, UN, SN modes
- [[stm-control-function]] — STM override coordination
- [[stm-states]] — STM state machine
- [[train-trip-procedure]] — Override as alternative when RBC unreachable
- [[subset26-1]] — Core SRS principles
- [[subset35]] — STM specification
- [[subset58]] — STM Application Layer
