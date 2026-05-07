# Train Interface Unit (TIU)

**Source:** [[subset35]] | **Date:** 2025-03-13 | **Type:** entity

The **Train Interface Unit (TIU)** is the ERTMS/ETCS on-board function that provides a subset of train interface signals to STMs, as defined in SUBSET-034 [¶101–§102].

## Command Signals

STM can command the following train functions [¶106, ¶110]:
- Regenerative Brake
- Magnetic Shoe Brake
- Eddy Current Brake (Service/Emergency)
- Pantograph
- Air Tightness
- Main Switch/Circuit Breaker
- Traction Cut Off

## Status Signals

TIU transmits the following status information [¶108, ¶111]:
- Traction status
- Direction Controller information
- Cab Status

## Communication

- TIU transmits train interface inputs status/availability on change and on connection [¶551–§554]
- Command configuration is also transmitted [¶551–§554]
- Service/Emergency Brake commands and status are handled by the Brake Interface Unit (BIU) [¶107, §109]

## Cross-references
- [[Brake Interface Unit (BIU)]] — handles brake-specific commands
- [[Specific Transmission Module (STM)]] — receives TIU signals
- [[subset35]] — source document
