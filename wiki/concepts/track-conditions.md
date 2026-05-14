# Track Conditions

**Source:** [[subset26]] | **Date:** 2025-07-17 | **Type:** concept

Track Conditions are data transmitted from trackside to inform the driver/train of conditions ahead, given as profile data (start and end) or location data (start only). [subset26 ¶1374][subset26 ¶1375][subset26 ¶1376]

## Track Condition Types

The SRS defines 16 track condition types [subset26 ¶1382][subset26 ¶1397]:

| Type | Description |
|------|-------------|
| Non-stopping area | Area where train must not stop |
| Tunnel | Tunnel ahead |
| Sound horn | Horn must be sounded |
| Lower pantograph | Pantograph must be lowered |
| Neutral section / End of powerless section | Power switch required |
| Radio hole | No radio coverage |
| Air tightness | Close air conditioning intake |
| Switch off regenerative/eddy current/magnetic shoe brakes | Brake inhibition |
| Tunnel stopping area | Stop inside tunnel |
| Big Metal Masses | Ignore integrity alarms |
| Station Platform | Platform location and height |
| Change of allowed current consumption | Current limit change |
| Change of traction system | Traction system change |
| Brake inhibition related to level crossing | Brake inhibition at LX |

## Evaluation Rules

Profile-type conditions: start evaluated using max safe front end, end using min safe rear end. Exceptions exist for Big Metal Mass, powerless sections, station platforms, etc. [subset26 ¶1377][subset26 ¶1381]

## Actions on Reception

Actions include DMI indication (with exceptions) and sending information to an ERTMS/ETCS external function. [subset26 ¶1403][subset26 ¶1404][subset26 ¶1405]

## Cross-references
- [[dmi-function]] — Displays condition information
- [[ertms-etcs-on-board-equipment]] — Processes conditions
- [[ertms-etcs-language]] — Packet 68/206 carry track conditions
