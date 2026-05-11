# ERTMS/ETCS Application Levels

**Source:** [[subset26-1]] | **Date:** 2026-05-12 | **Type:** concept

ERTMS/ETCS Application Levels define the operating relationship between track and train. Level definitions relate to trackside equipment used, how trackside information reaches on-board units, and which functions are processed trackside vs. on-board. [subset26-1 ¶146]

## Level 0 — Non-Equipped Operation

Used on lines without ERTMS/ETCS or national systems, or when operation under their supervision is not possible (e.g., commissioning, component failure). [subset26-1 ¶164]

- No ERTMS/ETCS trackside equipment except Eurobalises for level transitions [subset26-1 ¶173]
- On-board supervises only maximum design speed and unfitted area speed [subset26-1 ¶178-¶179]
- No cab signalling; lineside optical signals give movement authorities [subset26-1 ¶165]

## Level NTC — National Train Control

Used to run ERTMS/ETCS equipped trains on lines with national train control systems. [subset26-1 ¶185]

- National system's communication channels used for trackside-to-train transmission [subset26-1 ¶186]
- Eurobalises for level transitions only [subset26-1 ¶191]
- STM (Specific Transmission Module) provides standardised interface to national system [subset26-1 ¶194]

## Level 1 — Spot Transmission

Spot-transmission-based train control overlay on an underlying signalling system. [subset26-1 ¶215]

- Movement authorities via Eurobalises at signals [subset26-1 ¶216]
- Continuous speed supervision [subset26-1 ¶217]
- Lineside signals required (except with semi-continuous infill) [subset26-1 ¶223]
- Optional infill via Euroloop or Radio Infill Unit [subset26-1 ¶224-¶225]
- Trackside does not know individual trains [subset26-1 ¶220]

## Level 2 — Radio-Based

Radio-based train control overlay on an underlying signalling system. [subset26-1 ¶249]

- Movement authorities via Euroradio [subset26-1 ¶250]
- RBC knows each train individually [subset26-1 ¶254]
- Train reads Eurobalises and reports position to RBC [subset26-1 ¶271]
- Lineside signals optional [subset26-1 ¶255]
- Train detection and integrity by trackside equipment [subset26-1 ¶252]

## Level 3 — Radio-Based with On-Board Train Integrity

Radio-based train control where train position and integrity are reported by the train. [subset26-1 ¶278-¶283]

- Enables moving block operation [subset26-1 ¶283]
- RBC co-operates with train for position and integrity [subset26-1 ¶283]
- Train integrity proving system required on-board [subset26-1 ¶302]
- Lineside signals not foreseen [subset26-1 ¶286]

## Mixed Levels

Multiple application levels can operate on the same track (e.g., Level 2 and Level 3 trains sharing a line). [subset26-1 ¶158]

## Permitted Level Transitions

All transitions follow defined rules. Permitted transitions (from/to): Level 0 ↔ Level NTC, Level 1 ↔ Level 0/NTC, Level 2 ↔ Level 0/NTC/1, Level 3 ↔ Level 0/NTC/1/2. Level NTC ↔ Level NTC transitions describe switching between national systems. Level 2↔2 and 3↔3 describe RBC handover. [subset26-1 ¶311-¶318]

## Cross-References
- [[ertms-etcs-onboard]] — On-board equipment functions per level
- [[rbc]] — Radio Block Centre (used in L2/3)
- [[stm]] — STM for Level NTC
- [[movement-authority]] — Movement Authority in different levels
- [[balise-group]] — Balise groups used for spot transmission
- [[euroloop]] — Infill transmission (Level 1)
- [[subset26-1]] — Source document
