# Static Speed Restrictions

**Source:** [[subset26]] | **Date:** 2025-07-17 | **Type:** concept

Static Speed Restrictions in ERTMS/ETCS are independent speed restriction categories that together form the Most Restrictive Speed Profile (MRSP) used for train supervision. [subset26 ¶1205]

## Categories

The following independent speed restriction categories exist [subset26 ¶1205][subset26 ¶1206][subset26 ¶1207][subset26 ¶1208][subset26 ¶1209][subset26 ¶1210][subset26 ¶1211][subset26 ¶1212][subset26 ¶1213][subset26 ¶1214][subset26 ¶1215][subset26 ¶1216]:

| Category | Description |
|----------|-------------|
| **SSP** | Static Speed Profile — fixed permanent speed restrictions |
| **ASP** | Axle Load Speed Profile — speed per axle load category |
| **TSR** | Temporary Speed Restrictions — temporary limits, revocable or non-revocable |
| **Max Train Speed** | Train's maximum capable speed |
| **Signalling related** | Level 1 signal-based restrictions; zero means trip |
| **Mode related** | Speed limits by operating mode |
| **STM max/system speed** | National system speed limits |
| **LX SR** | Level Crossing speed restriction |
| **Override function SR** | Speed limit during override |
| **PBD SR** | Permitted Braking Distance speed restriction |

## SSP Selection (Cant Deficiency)

The on-board selects the Cant Deficiency SSP best matching its train category. If none matches, it uses the highest below or the Basic SSP. [subset26 ¶1238][subset26 ¶1239][subset26 ¶1240][subset26 ¶1241]

## Temporary Speed Restrictions (TSR)

TSRs can be revocable or non-revocable. A new TSR with the same identity replaces the previous unless non-revocable. In Level 2/3, revocable TSRs can be inhibited by RBC order. [subset26 ¶1262][subset26 ¶1274]

## Cross-references
- [[speed-and-distance-monitoring]] — MRSP used for supervision
- [[rbc]] — Provides speed restriction data
- [[movement-authority]] — MA requires SSP coverage
- [[train-position]] — Restrictions applied based on location
