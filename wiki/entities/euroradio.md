# Euroradio

**Source:** [[subset26]] | **Date:** 2025-07-17 | **Type:** entity

Euroradio is the radio protocol used for track-to-train communication in ERTMS/ETCS Levels 2 and 3, and for communication with RBCs and radio infill units. [subset26 ¶250][subset26 ¶253][subset26 ¶260]

## Function

- Carries Movement Authorities from RBC to on-board equipment in Levels 2 and 3 [subset26 ¶250]
- Supports bi-directional exchange of messages between on-board and trackside [subset26 ¶110]
- Provides high-priority data channel for emergency messages [subset26 ¶1176]
- Uses secured connections managed through cryptographic keys from the Key Management Centre (KMC) [subset26 ¶123][subset26 ¶451]

## Characteristics

- The safe radio connection has three status indications: 'No Connection', 'Connection Lost/Set-Up failed', and 'Connection Up' [subset26 ¶572]
- Communication sessions are initiated only by the on-board equipment [subset26 ¶455]
- The on-board must manage simultaneous sessions with at least two different entities [subset26 ¶453]

## Cross-references
- [[gsm-r]] — The underlying physical radio network
- [[rbc]] — Primary communication partner using Euroradio
- [[radio-infill-unit]] — Also uses Euroradio for infill
- [[communication-session]] — Session management concept
- [[ertms-etcs-application-levels]] — Levels 2 and 3 use Euroradio
