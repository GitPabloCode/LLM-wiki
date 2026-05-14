# GSM-R (Trackside Radio Communication Network)

**Source:** [[subset26]] | **Date:** 2025-07-17 | **Type:** entity

GSM-R (Global System for Mobile Communications — Railway) is the radio communication network used for bi-directional exchange of messages between ERTMS/ETCS on-board subsystems and RBCs or radio infill units. [subset26 ¶110][subset26 ¶138]

## Role in ERTMS/ETCS

- Provides the physical communication channel for **Euroradio** protocol messages [subset26 ¶110]
- Enables continuous communication between train and RBC in Levels 2 and 3 [subset26 ¶250]
- Supports radio infill communication in Level 1 [subset26 ¶1096]
- Radio network registration is managed by the on-board equipment via its Mobile Terminal(s) [subset26 ¶555]

## Radio Network Registration

The on-board equipment orders its Mobile Terminal(s) to register to a radio network at power-up or when ordered from trackside. The radio network ID can be modified by the driver at standstill. [subset26 ¶555][subset26 ¶2789]

## Cross-references
- [[euroradio]] — The protocol layer above GSM-R
- [[rbc]] — Trackside entity communicating via GSM-R
- [[radio-infill-unit]] — Uses GSM-R for infill information