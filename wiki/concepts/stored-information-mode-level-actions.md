# Store of Information on Mode/Level Entry

**Source:** [[subset26-2]] | **Date:** 2026-05-12 | **Type:** concept

When the ERTMS/ETCS on-board equipment enters a given level or mode, stored data may be deleted, reset, revalidated, or left unchanged. This concept defines transition rules from chapters 4.9 and 4.10 of the SRS.

## Stored Information on Level Entry (4.9)

When entering a specific level, certain stored data is affected:
- **Entering Level 1**: MA Request Parameters, Position Report Parameters, Track Ahead Free Request → deleted [subset26-2 ¶3681]
- **Entering Level 0, NTC, or 1**: 'Inhibition of revocable TSRs from balises in L2/3' → deleted [subset26-2 ¶3682]
- **All other data**: Unchanged by level transition [subset26-2 ¶3683]

## Stored Information on Mode Entry (4.10)

Mode transitions affect stored information status according to a comprehensive table. Actions per mode entry:

| Data Type | NP | SB | PS | SH | FS | LS | SR | OS | NL | UN | TR | PT | SN | RV |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Movement Authority | D | D | D | D | U | U | D | U | D | D | D | D | D | D |
| Gradient Profile | D | D | D | D | U | U | D | U | D | D | D | D | D | D |
| International SSP | D | D | D | D | U | U | D | U | D | D | D | D | D | D |
| Mode Profile | D | D | D | D | U | U | D | U | D | D | D | D | D | D |
| TSR | D | D | D | D | U | U | U | U | D | D | U | U | D | D |
| Train Data | D | TBR | U | TBR | U | U | U | U | U | U | U | U | U | U |
| Train Position | TBR | U | U | U | U | U | U | U | U | U | U | U | U | U |
| Track Conditions | R | R | R | R | U | U | R | U | R | R | R | U | R | R |
| Emergency Stops | D | D | D | D | U | U | D | U | D | D | D | U | D | D |

D = Deleted, U = Unchanged, R = Reset, TBR = To Be Revalidated, NR = Not Relevant [subset26-2 ¶3697-¶3700]

### Exceptions
- Level Transition Order: 'U' (Unchanged) when entering SB from SH, or when entering PS from SH [subset26-2 ¶3701-¶3702]
- Entering SF or IS: all data marked NR [subset26-2 ¶3694]

### Non-Stored Information (4.10.1.4.2)
The following are not considered stored information (and therefore not affected by mode transitions):
Repositioning information, Session Management (except RBC ID/phone number), Danger for SH information, Assignment of Coordinate System, Infill Location Reference, Location Identity, Recognition of exit from TRIP mode, Acknowledgement of Train Data, SH refused/authorised, Balise/loop System Version, Revocation of Emergency Stop, TSR Revocation, Acknowledgement of session termination, Default Balise Information, Co-operative shortening of MA, Train Rejected/Accepted, SoM position report confirmed, Track Ahead Free up to level 2/3 transition location, Signalling related speed restriction value zero, Stop if in SR mode, Data forwarded to National System, LSSMA display toggle off order. [subset26-2 ¶3705-¶3729]

## Stored Information on Exiting NP Mode (4.11)

When exiting No Power mode, the status of EOLM information, Train Position, ERTMS/ETCS Level, Table of trackside supported levels, and RBC ID/Phone Number depends on cold movement detection:
- **No cold movement occurred**: Invalid data becomes Valid [subset26-2 ¶3731-¶3734]
- **Cold movement detected or unknown**: Invalid data stays Invalid until validated by other means [subset26-2 ¶3733]
- Data that remained valid during NP is unaffected by cold movement detection [subset26-2 ¶3732]

## Cross-References
- [[etcs-modes]] — All 17 ETCS modes
- [[etcs-application-levels]] — Application levels
- [[information-acceptance]] — What information is accepted per mode/level
- [[subset26-1]] — Mode and level definitions
- [[train-trip-procedure]] — TR/PT mode entry effects
