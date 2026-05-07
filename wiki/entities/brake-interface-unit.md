# Brake Interface Unit (BIU)

**Source:** [[subset35]] | **Date:** 2025-03-13 | **Type:** entity

The **Brake Interface Unit (BIU)** is part of the Train Interface that handles brake-specific commands and status between ERTMS/ETCS on-board and STMs. It is physically separated from TIU due to different safety and performance levels [¶112–§115].

## Brake Commands

- **Service Brake** — when STM commands service brake, indicates if backup emergency brake is needed [¶559–§560]
- **Emergency Brake** — direct command with higher safety level

## Status Information

- Brake status provides availability information [¶115](http://localhost:8765/go.html#subset35-115)
- BIU transmits brake performance parameters on connection [¶555–§558]
- Brake status/availability on change and on connection [¶555–§558]

## Brake Performance Parameters

Brake performance parameters are transmitted during the Configuration (CO) state [¶248–§257]:
- Max time delay for processing brake commands
- Used in braking curves [¶257](http://localhost:8765/go.html#subset35-257)

## Cross-references
- [[Train Interface Unit (TIU)]] — handles non-brake train signals
- [[Specific Transmission Module (STM)]] — issues brake commands
- [[STM Control Function]] — uses brake performance in supervision
- [[STM States]] — brake parameters exchanged in CO state
- [[subset35]] — source document
