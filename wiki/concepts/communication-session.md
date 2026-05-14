# Communication Session

**Source:** [[subset26]] | **Date:** 2025-07-17 | **Type:** concept

A communication session is a data exchange between an ERTMS/ETCS on-board equipment and a trackside entity (RBC or radio infill unit). Only the on-board equipment can initiate a session. [subset26 ¶450][subset26 ¶455][subset26 ¶458]

## Key Rules

- **Initiation**: Only the on-board equipment can initiate a communication session [subset26 ¶455]
- **Simultaneous sessions**: The on-board shall manage simultaneous sessions with at least two different entities [subset26 ¶453]
- **Safe Radio Connection**: A secured radio link between on-board and trackside; its definition and management are in the Euroradio specification [subset26 ¶451][subset26 ¶522]
- **Session Management**: Uses Packet 42 (Session Management) containing RBC identity, telephone number, and session order [subset26 ¶5182]

## Session Status

The safe radio connection has three status indications [subset26 ¶572]:
- 'No Connection'
- 'Connection Lost/Set-Up failed'
- 'Connection Up'

## Session Timeout

When the safe radio connection timer (T_NVCONTACT) elapses, the reaction can be train trip, service brake, or no reaction (national value). [subset26 ¶2618][subset26 ¶2629]

## Cross-references
- [[euroradio]] — The radio protocol for sessions
- [[rbc]] — Primary session partner
- [[radio-infill-unit]] — Secondary session partner
- [[rbc-handover]] — Session transfers between RBCs
- [[ertms-etcs-modes]] — Session rules per mode
