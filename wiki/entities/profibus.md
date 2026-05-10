# PROFIBUS

**Source:** [[subset35]] | **Date:** 2025-07-17 | **Type:** entity

PROFIBUS (defined by CENELEC 50170-2) is the communication bus used for the interface between STM and ERTMS/ETCS on-board functions [subset35 ¶149].

## Bus Configuration Parameters

| Parameter | Value |
|-----------|-------|
| Baud Rate | 1500 Kbps |
| Min Station Delay (min TSDR) | 11 tBit |
| Max Station Delay (max TSDR) | 150 tBit |
| Slot Time (TSL) | 300 tBit |
| Quiet Time (TQUI) | 0 tBit |
| Setup Time (TSET) | 1 tBit |
| Time Target Rotation (TTR) | 30000 tBit (20 ms) |
| GAP Actualisation Factor (G) | 10 |
| Highest Station Address (HSA) | 126 |
| Max Retry Limit | 1 |

[subset35 ¶152]-[§162]

## Physical Layer

- Default medium: RS-485 twisted pair shielded copper cable [subset35 ¶166]
- Connectors: 9-pin female D-SUB per PROFIBUS specifications [subset35 ¶167]
- Max 200m per segment, max 32 stations (cable type A); repeaters extend this [subset35 ¶163]

## Addressing

- Physical addresses: STM Control Function = 2, STMs = NID_NTC + 70 (range 70-126), configurable range 50-69 [subset35 ¶190]
- Function addressing via Service Access Points (SAPs) for logical connections [subset35 ¶197]

## Protocol Stack

FDL layer → Safe Link Layer → Safe Time Layer → Application Layer [subset35 ¶207][subset35 ¶211]

## Cross-references
- [[stm]] — The Specific Transmission Module
- [[connection-management]] — Connection management over PROFIBUS
- [[stm-control-function]] — Uses PROFIBUS for communication
