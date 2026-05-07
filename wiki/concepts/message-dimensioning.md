# Message Dimensioning

**Source:** [[subset40]] | **Date:** 2026-05-07 | **Type:** concept

**Message dimensioning** covers the size constraints on ETCS messages, both for balise telegrams and radio messages.

## Balise Telegrams (§4.2.1)

| Speed Range | Standard Size Balise | Reduced Size Balise |
|---|---|---|
| 0–300 km/h | Long or short telegram | Long or short telegram [¶103](http://localhost:8765/go.html#subset40-103) |
| >300–500 km/h | Long or short telegram | **Short only** [¶103](http://localhost:8765/go.html#subset40-103) |

Speed refers to nominal line speed (SSP); tolerances are not considered [¶103](http://localhost:8765/go.html#subset40-103).

## Radio Messages (§4.2.2)

- **Normal priority**: Max **500 bytes** application data (excluding Euroradio protocol) [¶107](http://localhost:8765/go.html#subset40-107).
- **High priority**: Fixed size only [¶107](http://localhost:8765/go.html#subset40-107).

## Position Reports (§4.3)

Trackside shall not require position reports at a cycle of less than **5 seconds** [¶191](http://localhost:8765/go.html#subset40-191).

## Cross-references
- [[Data Dimensioning]] — iteration limits within messages
- [[RBC]] — RBC message rules
- [[Balise]] — telegram length rules
- [[subset40]] — source document
