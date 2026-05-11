# Limited Supervision Procedure

**Source:** [[subset26-2]] | **Date:** 2026-05-12 | **Type:** concept

The Limited Supervision (LS) procedure allows a train to enter areas where trackside information is limited and driver observes lineside signals, while the on-board provides background supervision.

## General Requirements (5.19.1)

- Order to switch to LS given by means of a mode profile. [subset26-2 ¶4542]
- Driver acknowledgement required. [subset26-2 ¶4543]

## Entry from Modes other than SB/PT (5.19.2)

- **L1**: Balise group giving the Mode Profile triggers immediate switch to LS when passed. [subset26-2 ¶4545]
- **L2/3**: If the train has already entered the LS area, immediate switch to LS. [subset26-2 ¶4546]
- Driver acknowledgement required; if not given within driver acknowledgement time, service brake triggered. [subset26-2 ¶4547-¶4548]
- If train speed exceeds LS mode speed limit at entry, emergency brake may be triggered immediately. [subset26-2 ¶4549]

## Entry for a Further Location (5.19.3)

Acknowledgement request ('rectangle of acknowledgement') displayed when:
- Distance to LS area start < value in mode profile [subset26-2 ¶4559]
- Speed < LS mode speed limit (national value or mode profile value) [subset26-2 ¶4560]
- Current mode is not LS [subset26-2 ¶4561]

Until switch to LS, the LS area start is temporarily considered as EOA. SvL derived from MA (as if no LOA) or from mode profile. [subset26-2 ¶4564-¶4567]

Driver acknowledgement triggers switch to LS. [subset26-2 ¶4568]

If max safe front end reaches LS area start without acknowledgement, forced switch to LS with acknowledgement request. [subset26-2 ¶4570]

## From Unfitted or SN Mode (5.19.4)

Mode profile for LS only evaluated in L1/2/3. Transition to LS can earliest occur at level transition (L0/L NTC → L1/2/3). [subset26-2 ¶4573]

## From Stand By or Post Trip (5.19.5)

In L2/3 during SoM or Train Trip procedure, if an LS area mode profile is received and the train has already entered, driver acknowledgement required. [subset26-2 ¶4575-¶4577]

## Exit from LS (5.19.6)

Exit when min safe front end passes the end of the LS area. [subset26-2 ¶4580]

- **LS ends at EOA/LOA**: Train must receive a new MA to exit. [subset26-2 ¶4581-¶4583]
- **LS ends before EOA/LOA**: Current MA already allows exit. Exit switches to FS, OS, or SH mode. [subset26-2 ¶4584-¶4586]

## Cross-References
- [[etcs-modes]] — LS mode definition
- [[on-sight-procedure]] — Similar entry/exit pattern
- [[shunting-procedure]] — Similar mode profile entry
- [[movement-authority]] — MA structure
- [[start-of-mission-procedure]] — SoM can lead to LS
- [[train-trip-procedure]] — Post-trip can lead to LS
- [[subset26-1]] — LS mode description
