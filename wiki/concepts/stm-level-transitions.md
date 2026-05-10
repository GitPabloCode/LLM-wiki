# STM Level Transitions

**Source:** [[subset35]], [[subset58]] | **Date:** 2025-07-17 | **Type:** concept

Level transitions between ERTMS/ETCS and National Systems (NTCs), and between different NTCs, are handled seamlessly by the FFFIS STM interface using Eurobalises for the level transition [subset58 ¶68].

## Transition Packets (SUBSET-058)

During level transitions, STMs in HS or DA state exchange transition-related data:

- **STM-16** (val=16): Transition variables STM max speed from STM — sent in HS state. Contains V_STMMAX (7 bits, 0-600 km/h, step 5 km/h). 127 = no STM max speed to supervise. [subset58 ¶145]-[subset58 ¶146], [subset58 ¶464]-[subset58 ¶465]
- **STM-17** (val=17): Transition variables STM system speed and distance from STM — sent in HS state. Contains V_STMSYS (7 bits, 0-600 km/h, step 5 km/h. 127 = no STM system speed) and D_STMSYS (15 bits, 0-327.670 km, step 10 m). [subset58 ¶147]-[subset58 ¶148], [subset58 ¶242]-[subset58 ¶243], [subset58 ¶466]-[subset58 ¶467]

## Transition Types (Annex A)

The informative system diagrams cover [subset58 ¶797]-[§810]:

1. **ETCS → NTC** — Standard transition from ETCS level to NTC level [subset58 ¶798]
2. **ETCS → NTC (Trip Mode)** — Transition when ETCS is in Trip mode [subset58 ¶799]
3. **ETCS → NTC (NL/SL)** — Transition from Non-Leading or Sleeping mode [subset58 ¶800]
4. **NTC → ETCS** — Transition from NTC level to ETCS [subset58 ¶801]
5. **NTC → ETCS (National Trip Procedure)** — Transition during National Trip Procedure [subset58 ¶802]
6. **NTC → ETCS (NL/SL)** — Transition from Non-Leading or Sleeping mode [subset58 ¶803]
7. **NTC X → NTC Y** — Direct transition between two different NTC systems [subset58 ¶805]
8. **NTC X → NTC Y (NL/SL)** — In Non-Leading/Sleeping modes [subset58 ¶807]
9. **Power On in Level NTC (SoM)** — Start of Mission in NTC level [subset58 ¶808]
10. **Power On in Level NTC (NL)** — Power On in Non-Leading mode [subset58 ¶809]
11. **Power On in Level NTC (SL)** — Power On in Sleeping mode [subset58 ¶810]

## STM Max Speed and System Speed

During level transitions, STMs in HS can request speed restrictions via:
- **STM max speed (V_STMMAX)** — speed limit at the transition border [subset58 ¶516]
- **STM system speed (V_STMSYS)** with **STM system distance (D_STMSYS)** — speed limit starting at a distance in rear of the transition border [subset58 ¶520]

## Association Rules

Level NTC X is associated to an STM X via a configurable look-up table mapping NID_NTC to NID_STM values with priority ordering [subset58 ¶325]. The association is maintained until the level is left or Stand-By/No Power mode is entered [subset58 ¶337].

## Cross-references
- [[stm]] — The Specific Transmission Module
- [[stm-control-function]] — Manages level transitions
- [[stm-states]] — STM state definitions
- [[connection-management]] — Connection management during transitions
- [[fffis-stm-application-layer]] — Application Layer protocol
