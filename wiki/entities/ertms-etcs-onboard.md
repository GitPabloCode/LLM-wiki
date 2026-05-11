# ERTMS/ETCS On-Board Equipment

**Source:** [[subset26-1]] | **Date:** 2026-05-12 | **Type:** entity

The ERTMS/ETCS on-board equipment is a computer-based system that supervises the movement of the train to which it belongs, based on information exchanged with the trackside subsystem. [subset26-1 ¶132]

## Components

Depending on the application level, the on-board subsystem includes:
- ERTMS/ETCS on-board equipment [subset26-1 ¶128]
- On-board part of the GSM-R radio system [subset26-1 ¶129]

## Interfaces

Interoperability requirements relate to data exchange between:
- Trackside subsystems and the on-board subsystem [subset26-1 ¶133]
- The driver (via DMI) [subset26-1 ¶134]
- The train (via Train Interface) [subset26-1 ¶135]
- On-board part of existing national train control systems (via STM) [subset26-1 ¶136]

## Functions per Level

**Level 0:** Supervision of maximum train speed and unfitted area speed; reading Eurobalises for level transitions; no cab signalling [subset26-1 ¶178-¶182]

**Level NTC:** No train supervision (handed over to national system); reading Eurobalises for level transitions; STM management; no cab signalling [subset26-1 ¶207-¶212]

**Level 1:** Reception of MA from Eurobalises; dynamic speed profile calculation; speed comparison and brake command; cab signalling [subset26-1 ¶241-¶246]

**Level 2:** Reads Eurobalises and reports position to RBC; receives MA via Euroradio; dynamic speed profile; cab signalling [subset26-1 ¶270-¶276]

**Level 3:** Same as Level 2 plus train integrity monitoring and reporting to RBC [subset26-1 ¶303-¶310]

## Core Functions

- Speed and Distance Monitoring (CSM, TSM, RSM) [subset26-1 ¶2127-¶2135]
- Movement Authority management [subset26-1 ¶897-¶1090]
- Communication session management with RBC/RIU [subset26-1 ¶449-¶589]
- Train position determination relative to LRBG [subset26-1 ¶590-¶636]
- Data consistency checking [subset26-1 ¶2500-¶2641]
- System version management [subset26-1 ¶2646-¶2699]
- Mode management and transitions [subset26-1 ¶3162-¶3541]

## Cross-References
- [[rbc]] — Radio Block Centre
- [[movement-authority]] — Movement Authority concept
- [[stm]] — Specific Transmission Module interface
- [[etcs-application-levels]] — Application Levels
- [[etcs-modes]] — ETCS Modes
- [[speed-and-distance-monitoring]] — Speed monitoring concept
- [[subset26-1]] — Source document
