# Procedures

**Source:** [[subset26]] | **Date:** 2025-07-17 | **Type:** concept

Procedures in ERTMS/ETCS define the required reactions of ERTMS/ETCS entities (on-board equipment, RBC, driver) to information or events. They are defined in Chapter 5 of SUBSET-026. [subset26 ¶3765][subset26 ¶3766]

## Key Procedures

### Start of Mission (SoM)
Begins when on-board is in Stand-By mode with desk open and no session established. The driver enters/revalidates Driver ID, Train Running Number, and optionally sets/removes Virtual Balise Covers. Ends when the on-board transitions to FS, LS, SR, OS, NL, UN, or SN mode. [subset26 ¶3795][subset26 ¶3803]

### End of Mission
Terminates a mission when entering Stand-By or Shunting mode. If an RBC session exists, an 'End of Mission' message with position report is sent, and the RBC requests session termination. [subset26 ¶3842][subset26 ¶3861]

### Shunting
- **Driver initiated**: Driver selects shunting mode; in Levels 2/3 the RBC is requested [subset26 ¶3873]
- **Trackside ordered**: Via mode profile from balise or RBC [subset26 ¶3894]

### Override
Allows a train to pass its EOA in degraded situations. Switches to Staff Responsible mode. The former EOA/LOA is retained as a trip condition. Override ends when time/distance limit elapses, or when proceed information is received. [subset26 ¶3926][subset26 ¶3959]

### Train Trip
When a trip event occurs, the mode changes to TR. After standstill and driver acknowledgement, mode changes to PT (Level 1/2/3) or SH/UN/SN (Level 0/NTC). All MA and track description data (except track conditions) are deleted. [subset26 ¶4186][subset26 ¶4192]

### On Sight
Entered when the train enters an On Sight area announced by trackside. If speed exceeds the OS speed limit on entry, brake command can be triggered immediately. [subset26 ¶3989]

### Level Transitions
All transitions between levels (0, NTC, 1, 2, 3) follow defined procedures with announcement, border balises, and data management. The table of priority determines which level is chosen. [subset26 ¶4043][subset26 ¶4061]

### RBC/RBC Handover
Automatic transfer between RBC areas. See [[rbc-handover]].

### Joining and Splitting
Procedures for coupling/uncoupling trains, involving train data modification and mode transitions for slave engines. [subset26 ¶4254][subset26 ¶4263]

## Cross-references
- [[ertms-etcs-modes]] — Modes used in procedures
- [[rbc-handover]] — RBC handover procedure
- [[override-procedure]] — STM-level override coordination
- [[ertms-etcs-application-levels]] — Level transitions
