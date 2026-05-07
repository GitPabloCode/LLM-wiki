# Juridical Data Recording

**Source:** [[subset35]] | **Date:** 2025-03-13 | **Type:** entity

The **Juridical Data Recording** function is the ERTMS/ETCS on-board service that receives national juridical data from STMs and forwards it to the On-Board Recording Device [¶116–§117, §754–§755].

## Data Flow

- STM transmits national juridical data to ERTMS/ETCS on-board
- ERTMS/ETCS on-board forwards the data to the On-Board Recording Device
- STM uses Reference Time for timestamping; timestamp represents event occurrence time for chronology [¶756–§758]

## Communication

- SAP: 000010 (point-to-point) [¶202](http://localhost:8765/go.html#subset35-202)
- Only Juridical Data and DMI channels 2,3,4 may be marked unavailable by STM Control Function [¶320](http://localhost:8765/go.html#subset35-320)

## Cross-references
- [[Specific Transmission Module (STM)]] — source of juridical data
- [[PROFIBUS (STM Interface)]] — uses SAP 000010
- [[STM Control Function]] — manages availability
- [[subset35]] — source document
