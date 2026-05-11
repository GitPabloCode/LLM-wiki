# Radio Infill Unit (RIU)

**Source:** [[subset26-1]] | **Date:** 2026-05-12 | **Type:** entity

A Radio Infill Unit (RIU) is a trackside subsystem that operates on Level 1 lines, providing signalling information in advance as regard to the next main signal in the train running direction. [subset26-1 ¶120]

## Function

- Provides semi-continuous infill information to on-board equipment in Level 1 areas [subset26-1 ¶224]
- Composed of on-board functionality and one or more trackside parts [subset26-1 ¶121]
- Communicates with on-board via GSM-R using the same protocols as Level 2/3 operations [subset26-1 ¶1126]
- Allows operation without release speed [subset26-1 ¶225]

## Communication

- Only on-board can initiate communication sessions with RIU [subset26-1 ¶1138]
- On-board can manage simultaneous sessions with multiple RIUs [subset26-1 ¶1135-¶1136]
- RIU sends infill information cyclically once train enters its area [subset26-1 ¶1156-¶1158]
- RIU terminates sending when train passes the next main signal balise group [subset26-1 ¶1167]

## Cross-References
- [[subset26-1]] — Source document
- [[gsm-r]] — Communication network
- [[euroloop]] — Alternative infill transmission medium
