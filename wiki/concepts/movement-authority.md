# Movement Authority (MA)

**Source:** [[subset26-1]] | **Date:** 2026-05-12 | **Type:** concept

A Movement Authority (MA) is the permission and distance granted to a train to move along a given route. It is the core mechanism by which ERTMS/ETCS controls train movements. [subset26-1 ¶835]

## Characteristics

- **End of Movement Authority**: The location to which the train is authorised to move [subset26-1 ¶900]
- **EOA** (End of Authority): When target speed at the End of Movement Authority is zero [subset26-1 ¶901]
- **LOA** (Limit of Authority): When target speed is non-zero (can be time-limited) [subset26-1 ¶901]
- **Danger Point**: A location beyond the End of Movement Authority reachable without hazardous situation [subset26-1 ¶902]
- **Overlap**: Additional distance beyond the Danger Point, valid for a defined time [subset26-1 ¶903]
- **Release speed**: Speed limit near the End of Movement Authority when target speed is zero [subset26-1 ¶904]

## Section Structure

An MA can be split into multiple sections, each with:
- Length of the section [subset26-1 ¶942]
- Optional Section time-out value and stop location [subset26-1 ¶942]

The End Section can additionally include:
- End Section time-out [subset26-1 ¶947]
- Danger point information [subset26-1 ¶948]
- Overlap information (distance, time-out, release speed) [subset26-1 ¶949]

## Time-Outs

- **Section time-out**: Revokes route if train has not entered the section in time [subset26-1 ¶906]
- **End Section time-out**: Revokes last section when occupied by train after time expires [subset26-1 ¶907]
- **Overlap time-out**: Overlap remains valid for a defined time [subset26-1 ¶903]
- **LOA speed time-out**: LOA target speed reverts to zero after time expires [subset26-1 ¶996]

## MA Update

- New MA from a balise group at main signal (non-infill) or from RBC replaces previous MA entirely [subset26-1 ¶1026]
- Infill MA replaces data beyond the announced balise group at the next main signal [subset26-1 ¶1028]
- Repositioning information updates the length of the current MA section [subset26-1 ¶1034]
- Co-operative shortening (Level 2/3 only): RBC proposes shortened MA, on-board checks if train position allows it [subset26-1 ¶1083-¶1090]

## Delivery by Level

- **Level 1**: Via Eurobalises at signals; optionally via Euroloop or Radio Infill Unit [subset26-1 ¶216]
- **Level 2/3**: Via Euroradio from RBC [subset26-1 ¶250]

## Required Accompanying Data

The MA must be accompanied by track description covering the full MA distance: SSP, gradient profile, optionally ASP, track conditions, route suitability, linking information, etc. [subset26-1 ¶835-¶848]

## Cross-References
- [[rbc]] — RBC generates MAs for Levels 2/3
- [[ertms-etcs-onboard]] — On-board equipment uses MA for supervision
- [[etcs-application-levels]] — How MA delivery varies by level
- [[speed-and-distance-monitoring]] — MA used as target for speed/distance supervision
- [[subset26-1]] — Source document
