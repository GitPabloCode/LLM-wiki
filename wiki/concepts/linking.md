# Linking

**Source:** [[subset40]] | **Date:** 2026-05-07 | **Type:** concept

**Linking** is a mechanism in ETCS where the trackside informs the onboard system about the expected sequence of balise groups the train will encounter. Linking data enables the train to verify its position and detect missing or unexpected balise groups.

## Rules from SUBSET-040

### Distance Measurement
The distance between groups differs from the linking distance (which is between balises with N_PIG=0) [¶46](http://localhost:8765/go.html#subset40-46).

### Unlinked Groups
- Unlinked balise groups shall **never** be announced via linking [¶130](http://localhost:8765/go.html#subset40-130).
- Unlinked groups shall **never** transmit linking unless acting as in-fill [¶131](http://localhost:8765/go.html#subset40-131).

### Dimensioning
- **Linked balise groups**: max **29** iterations in one packet, minimum **30** memorised on board (exception for in-fill) [¶167](http://localhost:8765/go.html#subset40-167).

## Cross-references
- [[Balise Group]] — groups that may be linked
- [[In-fill]] — exception for unlinked groups transmitting linking
- [[Data Dimensioning]] — linking iteration limits
- [[subset40]] — source document
