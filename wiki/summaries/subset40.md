# SUBSET-040: ERTMS/ETCS Dimensioning and Engineering Rules

**Source:** This document | **Date:** 2025-07-17 | **Type:** summary

SUBSET-040 v2.3.0 (2009-04-07) defines the dimensioning and engineering rules for ERTMS/ETCS Class 1 systems. It provides system-related constraints for equipment installation, information exchange, and message sizing that complement the System Requirements Specification (SUBSET-026) and subsystem FFFIS documents to ensure interoperability. [subset40 ¶30][subset40 ¶31]

## Scope

The engineering rules cover three main areas: [subset40 ¶56][subset40 ¶100][subset40 ¶143]

1. **Installation rules** — Physical placement of balises, Eurobalise antennas, and Euroloops
2. **Telegram and message rules** — Content and formatting constraints for balise telegrams and radio messages
3. **Dimensioning rules** — Maximum iterations and minimum onboard storage for data elements in messages

## Key Installation Rules

- **Balise group spacing**: Maximum 12m between consecutive balises within a group [subset40 ¶61]
- **Signal-related positioning**: Balises at signals containing switched info must be ≤0.7m in rear of the operational stopping point for Level 1 [subset40 ¶63]
- **EOA clearance**: Last balise giving an MA must be ≥1.3m in rear of the EOA/LOA [subset40 ¶65]
- **Train detection clearance**: Last switchable balise must be ≥13.8m in rear of train detection section limits [subset40 ¶67]
- **Processing capacity**: No more than 8 balises encountered within the distance travelled in 0.8s at line speed [subset40 ¶69]
- **Curve radius**: Minimum 300m radius recommended where balises are placed [subset40 ¶74]
- **Antenna positioning**: Front of engine to antenna: min 2m, max 12.5m [subset40 ¶92]

## Key Message and Data Rules

- **Balise telegram length**: Long or short telegram up to 300 km/h; restrictions above 300 km/h for reduced-size balises [subset40 ¶103]
- **Radio message max**: 500 bytes application data for normal priority [subset40 ¶107]
- **In-fill information**: Limited to MA, linking, route-related data; no EOLM or opposite-direction data [subset40 ¶113]
- **Mode profiles**: Overlapping forbidden; no mode profile packet with V_MAIN=0 [subset40 ¶119][subset40 ¶120]
- **Linking**: Unlinked balise groups shall never be announced via linking [subset40 ¶130]

## Key Dimensioning Rules

| Data Element | Max Iterations per Packet | Min Memorised Onboard |
|---|---|---|
| MA sections | 5 | 6 |
| Balise IDs for SR/shunting | 15 | n/a |
| Mode profile sections | 2 | n/a |
| SSP changes | 31 | 50 |
| TSR packets | 10 per message | 30 |
| Gradient changes | 31 | 50 |
| Linked balise groups | 29 | 30 |
| Track conditions | 19 | 20 |
| Route suitability | 2 | 3 |
| Axle load speed profiles | 14 | 30 |

## Cross-References
- [[eurobalise]] — The physical trackside device governed by these installation rules
- [[eurobalise-antenna]] — The onboard antenna whose positioning is specified in this document
- [[euroloop]] — The loop-based transmission system covered by installation rules
- [[balise-installation-rules]] — Detailed installation distance rules for balises
- [[data-engineering-rules]] — Rules for individual data types in telegrams and messages
- [[dimensioning-rules]] — Maximum iterations and onboard memory requirements
- [[ker-compatibility]] — Additional rules for KER-compatible systems
