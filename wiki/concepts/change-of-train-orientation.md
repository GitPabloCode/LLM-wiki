# Change of Train Orientation

**Source:** [[subset26-2]] | **Date:** 2026-05-12 | **Type:** concept

Procedures for changing the driving cab of a train, which may involve the same engine or a different engine.

## Same Engine, Mission Ongoing (5.12.2)

Driver closes desk A, leaves cab A, goes to cab B on same engine. Both desks connected to same on-board equipment. [subset26-2 ¶4211-¶4213]

- Closing desk → SB mode → End of Mission [subset26-2 ¶4214]
- Opening desk B → Start of Mission procedure [subset26-2 ¶4215]
- On-board calculates new train position (front position, orientation) using previous data. [subset26-2 ¶4216]

## Different Engine (5.12.3)

The leading engine A becomes slave; slave engine B becomes leading.

### Engine B was in SL (Sleeping) mode
- Driver closes desk A → SB → End of Mission [subset26-2 ¶4226]
- Remote control signal disappears → engine B switches to SB [subset26-2 ¶4227]
- In L2/3: engine B opens communication session, reports mode change to RBC [subset26-2 ¶4228]
- Driver opens desk B → Start of Mission [subset26-2 ¶4229]

### Engine B was in NL (Non Leading) mode
- Driver of engine A selects 'Non Leading' → NL mode [subset26-2 ¶4231]
- Non leading input signal no longer received → engine B switches to SB [subset26-2 ¶4232]
- With desk open, SoM triggered automatically [subset26-2 ¶4233]

### Engine B was in PS (Passive Shunting) mode
- Driver of engine A selects 'Continue Shunting on desk closure' → PS mode after desk closure [subset26-2 ¶4235]
- Driver opens desk in engine B → switches to SH mode [subset26-2 ¶4236]

## Same Engine, Shunting Ongoing (5.12.4)

While in SH mode, driver closes desk A and goes to desk B on same engine. [subset26-2 ¶4238]

- Before closing desk: driver enables 'Continue Shunting on desk closure' [subset26-2 ¶4240]
- Closing desk A → PS mode [subset26-2 ¶4240]
- Opening desk B → back to SH mode [subset26-2 ¶4241]
- New train position calculated from previous data [subset26-2 ¶4242]

## Cross-References
- [[etcs-modes]] — SB, SH, PS, SL, NL modes
- [[start-of-mission-procedure]] — SoM triggered after cab change
- [[end-of-mission-procedure]] — End of Mission on desk closure
- [[shunting-procedure]] — Shunting mode entry
- [[subset26-1]] — Mode definitions
