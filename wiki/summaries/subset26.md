# SUBSET-026: ERTMS/ETCS System Requirements Specification

**Source:** [[subset26]] | **Date:** 2025-07-17 | **Type:** summary

SUBSET-026 (Issue 3.6.0, 13/05/2016) is the System Requirements Specification (SRS) for the ERTMS/ETCS — the European Rail Traffic Management System / European Train Control System. It defines the functional requirements, technical specifications, and operational principles for both trackside and on-board subsystems across all application levels (0, NTC, 1, 2, 3).

## Document Structure

The SRS comprises the following chapters:

| Chapter | Content |
|---------|---------|
| 1 | Introduction — scope, modification history, objectives |
| 2 | Basic System Description — subsystems, application levels overview |
| 3 | Principles — detailed technical requirements (linking, MA, position reporting, speed profiles, braking, supervision) |
| 4 | Modes and Transitions — 17 operating modes and mode transition rules |
| 5 | Procedures — Start of Mission, End of Mission, Shunting, Override, On-Sight, Level Transitions, Train Trip, Joining/Splitting, RBC Handover |
| 6 | Management of Older System Versions — X=1 and X=2 compatibility |
| 7 | Language — variable and packet definitions for air-gap transmission |
| 8 | Messages — Eurobalise, Euroloop, and Euroradio message definitions |
| 9 | Classification of Clauses — requirement categorisation for compliance |

## Key Subsystems

The ERTMS/ETCS system is divided into a **trackside subsystem** (balises, LEUs, GSM-R, RBCs, Euroloops, Radio Infill Units, KMC, PKI) and an **on-board subsystem** (ERTMS/ETCS on-board equipment, GSM-R radio, DMI, STM). [subset26 ¶84]

## Application Levels

- **Level 0**: Non-ERTMS lines; only ceiling speed supervision [subset26 ¶153]
- **Level NTC**: Operation with national train control systems via STM [subset26 ¶154]
- **Level 1**: Spot-transmission via balises; MA from trackside; optional infill via Euroloop or radio [subset26 ¶155]
- **Level 2**: Radio-based; MA via Euroradio from RBC; RBC knows each train individually [subset26 ¶156]
- **Level 3**: Radio-based; train reports position and integrity; no lineside signals [subset26 ¶157]

## Operating Modes (17)

FS (Full Supervision), LS (Limited Supervision), OS (On Sight), SR (Staff Responsible), SH (Shunting), UN (Unfitted), PS (Passive Shunting), SL (Sleeping), SB (Stand By), TR (Trip), PT (Post Trip), SF (System Failure), IS (Isolation), NP (No Power), NL (Non Leading), SN (National System), RV (Reversing). [subset26 ¶3162]

## Key Concepts Covered

- **Movement Authority (MA)**: Permission to move to a specific location, with sections, timeouts, overlap, and danger point [subset26 ¶900]
- **Linking**: Balise group linking for position reference and odometer correction [subset26 ¶398]
- **Speed and Distance Monitoring**: Ceiling, Target, and Release speed monitoring with EBI/SBI/W/P/I limits [subset26 ¶1498]
- **Communication Sessions**: Initiated only by on-board; simultaneous sessions with at least two entities [subset26 ¶455]
- **RBC/RBC Handover**: Automatic transfer between RBC areas [subset26 ¶2345]
- **System Version Management**: Backward compatibility rules for versions X=1 and X=2 [subset26 ¶4711]
- **Juridical Recording**: Legal recording of events [subset26 ¶2818]

## Cross-references
- [[rbc]] — Radio Block Centre, core trackside entity
- [[ertms-etcs-on-board-equipment]] — The train-borne subsystem
- [[movement-authority]] — Core concept of train permission
- [[ertms-etcs-application-levels]] — The five application levels
- [[ertms-etcs-modes]] — The 17 operating modes
- [[speed-and-distance-monitoring]] — Braking curve and supervision concept
- [[linking]] — Balise group linking concept
- [[communication-session]] — Radio session management
- [[rbc-handover]] — Between-RBC transitions
- [[ertms-etcs-language]] — Variable, packet, and message definitions
