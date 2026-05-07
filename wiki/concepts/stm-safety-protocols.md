# STM Safety Protocols

**Source:** [[subset35]] | **Date:** 2025-03-13 | **Type:** concept

The **STM Safety Protocols** define three safety levels (SL4, SL2, SL0) for communication over the STM interface, based on CENELEC EN 50159 [¶174–§178].

## Protocol Levels

- **SL4** — Highest safety level, for functions requiring SIL4 [¶174–§177]
- **SL2** — Medium safety level [¶175](http://localhost:8765/go.html#subset35-175)
- **SL0** — No safety protocol [¶176](http://localhost:8765/go.html#subset35-176)

## Implementation Rules

- Equipment shall not implement an SL higher than its SIL [¶180](http://localhost:8765/go.html#subset35-180)
- ERTMS/ETCS on-board functions implement all safety protocols up to the SL corresponding to the function's SIL [¶181](http://localhost:8765/go.html#subset35-181)
- Safety justification per CENELEC EN 50159 [¶178](http://localhost:8765/go.html#subset35-178)

## Protocol Stack

Safety protocols correspond to layers in the communication stack [¶207–§211]:
- **Safe Time Layer** (SUBSET-056) — provides time synchronisation [¶2, §208]
- **Safe Link Layer** (SUBSET-057) — provides reliable link [¶3, §208]
- Together these form the **Safety Layers** [¶208](http://localhost:8765/go.html#subset35-208)

## Cross-references
- [[Specific Transmission Module (STM)]] — uses these protocols
- [[PROFIBUS (STM Interface)]] — sits below the safety layers
- [[subset35]] — source document
