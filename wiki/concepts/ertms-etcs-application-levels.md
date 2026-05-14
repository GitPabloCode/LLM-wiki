# ERTMS/ETCS Application Levels

**Source:** [[subset26]] | **Date:** 2025-07-17 | **Type:** concept

ERTMS/ETCS defines five application levels that determine how the train receives Movement Authorities and signalling information from the trackside. [subset26 ¶151]

## Level 0

Operation on non-ERTMS/ETCS lines or lines where supervision is not possible. Only Eurobalises for level transitions, no cab signalling. Speed supervision of maximum train speed and unfitted area speed. [subset26 ¶153][subset26 ¶164][subset26 ¶168][subset26 ¶169]

## Level NTC

Operation on lines equipped with a national train control system. Train supervision is handed over to the National System via an STM. Eurobalises are used for level transitions to/from NTC. [subset26 ¶154][subset26 ¶185][subset26 ¶191][subset26 ¶208]

## Level 1

Spot-transmission based train control system. Movement Authorities are transmitted via Eurobalises at signals. Continuous speed supervision is performed. Optional infill (advance signalling information) can be provided via Euroloop or radio. [subset26 ¶155][subset26 ¶215][subset26 ¶216][subset26 ¶217]

## Level 2

Radio-based train control system. Movement Authorities are transmitted via Euroradio from an RBC. The RBC knows each train individually by its ETCS identity. Lineside signals can be suppressed as the driver receives signalling information via DMI. [subset26 ¶156][subset26 ¶249][subset26 ¶250][subset26 ¶254][subset26 ¶255]

## Level 3

Radio-based train control system like Level 2, but train position and train integrity are reported by the train itself. No lineside signals are planned. The RBC performs position and integrity supervision in co-operation with the train. [subset26 ¶157][subset26 ¶280][subset26 ¶283][subset26 ¶286]

## Level Transitions

All transitions between application levels (0, NTC, 1, 2, 3) are performed according to defined functions and procedures. A table of priority determines which level takes precedence at transition borders. [subset26 ¶151][subset26 ¶312][subset26 ¶315][subset26 ¶316][subset26 ¶4061]

## Cross-references
- [[rbc]] — Required for Levels 2 and 3
- [[eurobalise]] — Spot transmission in Level 1
- [[euroradio]] — Radio transmission in Levels 2/3
- [[stm]] — Interface for Level NTC
- [[movement-authority]] — Transmitted differently per level
- [[stm-level-transitions]] — NTC level transition specifics
