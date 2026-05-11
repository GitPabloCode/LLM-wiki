# On Sight Procedure

**Source:** [[subset26-2]] | **Date:** 2026-05-12 | **Type:** concept

The On Sight (OS) procedure allows a train to enter occupied or obstructed track sections under strict speed and distance supervision.

## Entry from Modes other than SB/PT (5.9.2)

- **L1**: Balise group giving the Mode Profile triggers immediate switch to OS when passed. [subset26-2 ¶3994]
- **L2/3**: If the train has already entered the OS area, immediate switch to OS. [subset26-2 ¶3995]
- Driver acknowledgement required; if not given within driver acknowledgement time, service brake triggered until acknowledgement. [subset26-2 ¶3996-¶3997]
- If train speed exceeds OS mode speed limit at entry, emergency brake may be triggered immediately. [subset26-2 ¶3998]

## Entry for a Further Location (5.9.3)

Acknowledgement request ('rectangle of acknowledgement') displayed when:
- Distance to OS area start < value in mode profile [subset26-2 ¶4008]
- Speed < OS mode speed limit (national value or mode profile value) [subset26-2 ¶4009]
- Current mode is not OS [subset26-2 ¶4010]

Until switch to OS, the OS area start is temporarily considered as EOA (replacing MA-derived EOA/LOA). SvL derived from MA (as if no LOA) or from mode profile. [subset26-2 ¶4013-¶4016]

Driver acknowledgement triggers switch to OS. [subset26-2 ¶4017]

If max safe front end reaches OS area start without acknowledgement, forced switch to OS with acknowledgement request. [subset26-2 ¶4018]

## From Unfitted or SN Mode (5.9.4)

Mode profile for OS is only evaluated in L1/2/3. If OS area profile received in L0 or NTC, transition to OS occurs at the level transition (L0/L NTC → L1/2/3). [subset26-2 ¶4021-¶4022]

## From Stand By or Post Trip (5.9.5)

In L2/3 during SoM or Train Trip procedure, if an OS area mode profile is received and the train has already entered it, on-board requires driver acknowledgement to transition to OS. [subset26-2 ¶4024-¶4026]

## Exit from OS (5.9.6)

Exit when min safe front end passes the end of the OS area. [subset26-2 ¶4029]

- **OS ends at EOA/LOA**: Train must receive a new MA to exit. Track Ahead Free mechanism: RBC sends 'track ahead free' request; driver confirms track is free to allow new MA. [subset26-2 ¶4030-¶4036]
- **OS ends before EOA/LOA**: Current MA already allows exit. Exit switches to FS, LS, or SH mode. [subset26-2 ¶4037-¶4039]

## Cross-References
- [[etcs-modes]] — OS mode definition
- [[movement-authority]] — MA structure for OS
- [[limited-supervision-procedure]] — Similar entry/exit pattern
- [[shunting-procedure]] — Similar mode profile entry
- [[start-of-mission-procedure]] — SoM can lead to OS
- [[train-trip-procedure]] — Post-trip can lead to OS
- [[subset26-1]] — OS mode description
