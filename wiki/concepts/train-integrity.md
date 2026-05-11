# Train Integrity

**Source:** [[subset26-1]] | **Date:** 2026-05-12 | **Type:** concept

Train integrity is the confirmation that the train is complete (i.e., no portion has become detached). It is required for Level 3 operation where train position and integrity supervision rely on information from the train rather than trackside equipment. [subset26-1 ¶157]

## Levels and Responsibility

- **Level 1 & 2**: Train detection and train integrity supervision performed by trackside equipment (interlocking, track circuits) outside ERTMS/ETCS scope [subset26-1 ¶218]
- **Level 3**: Train position and integrity supervised by RBC in co-operation with the train; train sends position reports and integrity information [subset26-1 ¶283]

## Integrity Information

The train integrity information consists of:
- **Status**: No integrity information / confirmed by monitoring device / confirmed by driver / integrity lost [subset26-1 ¶793-¶798]
- **Safe train length**: Distance between min safe rear end and estimated front end, only valid when integrity is confirmed [subset26-1 ¶800-¶801]

## Driver Input

Driver confirmation of train integrity is only permitted at standstill. [subset26-1 ¶792]

## Cross-References
- [[subset26-1]] — Source document
- [[etcs-application-levels]] — Level 3 requires train integrity
- [[ertms-etcs-onboard]] — On-board equipment reports integrity
