# System Version Management

**Source:** [[subset26]] | **Date:** 2025-07-17 | **Type:** concept

System Version Management defines the backward compatibility rules for ERTMS/ETCS when trackside and on-board equipment operate with different system version numbers (X.Y). [subset26 ¶4711]

## Version Numbering

System version is identified by X.Y where:
- **X** — major version (1 or 2)
- **Y** — minor version (0 or 1)

Within a given X, trackside infrastructure may use specific Y values (0 or 1). [subset26 ¶4711][subset26 ¶4712]

## Allowed M_VERSION Values

- **X=1 trackside**: M_VERSION 1.0 and 1.1 allowed; balises in RBC area can also use 2.0 and 2.1 [subset26 ¶4717][subset26 ¶4718]
- **X=2 trackside**: M_VERSION 1.0, 1.1, 2.0, and 2.1 all allowed [subset26 ¶4911]

## Marking Requirements

Packets requiring system version 1.1 marking (balise telegrams, loop messages, RBC/RIU communications) when containing packets 2, 6, 135, 145, 200, 203, 206, 207, or 239. [subset26 ¶4901][subset26 ¶4904]

## Translation (Air Gap Data)

When the on-board receives data from X=1 trackside, it must translate certain packets to the newer format [subset26 ¶4954]:
- Packet 206 → Packet 68 (Track Condition)
- Packet 207 → Packet 70 (Route Suitability)
- Packet 239 → Packet 39 (Traction System)
- M_AXLELOAD → M_AXLELOADCAT via translation table
- M_TRACTION → M_VOLTAGE + NID_CTRACTION

## Cross-references
- [[ertms-etcs-language]] — Variables and packets affected by version
- [[rbc]] — Trackside entity with version
- [[ertms-etcs-on-board-equipment]] — Applies translations
- [[ertms-etcs-application-levels]] — Version applies per trackside area
