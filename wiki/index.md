# Wiki Index

*Last updated: 2026-04-29*

## Summaries
- [subset35](summaries/subset35.md) — FFFIS STM: Specific Transmission Module interface specification for ERTMS/ETCS interoperability with national train control systems | 2015-12-16
- [subset40](summaries/subset40.md) — Dimensioning and Engineering Rules: mandatory installation and data-size constraints for ERTMS/ETCS trackside infrastructure | 2009-04-07
- [subset58](summaries/subset58.md) — FFFIS STM Application Layer: packets, variables, and messages exchanged between STM and ERTMS/ETCS on-board functions | 2015-12-16

## Entities
- [stm](entities/stm.md) — Specific Transmission Module: on-board device adapting legacy NTC systems to the ERTMS/ETCS on-board | subset35, subset58
- [ntc](entities/ntc.md) — National Train Control: legacy national train protection system operating alongside ETCS | subset35, subset58
- [stm-control-function](entities/stm-control-function.md) — ERTMS/ETCS on-board function managing STM states, versioning, and data routing; ~25 application-layer packets defined | subset35, subset58

## Concepts
- [fffis](concepts/fffis.md) — Form Fit Functional Interface Specification: covering form, fit, and function for interchangeable safety-critical equipment | subset35
- [stm-states](concepts/stm-states.md) — The eight-state lifecycle of an STM: NP, PO, CO, DE, CS, HS, DA, FA | subset35
- [stm-version-check](concepts/stm-version-check.md) — Bidirectional handshake for FFFIS STM version compatibility negotiation using STM-1 packet | subset35, subset58
- [fffis-stm-language](concepts/fffis-stm-language.md) — Three-level data model of variables, packets, and messages forming the application-layer protocol | subset58
- [specific-ntc-data-entry](concepts/specific-ntc-data-entry.md) — Six-packet handshake procedure for entering national operational data during the DE state | subset58
- [ertms-engineering-rules](concepts/ertms-engineering-rules.md) — Mandatory dimensioning constraints complementary to the SRS, ensuring interoperable trackside installations | subset40
- [balise-installation](concepts/balise-installation.md) — Physical placement rules for Eurobalises and antennas: spacing, signals, EOA, train detection, and curve radius | subset40
- [ertms-dimensioning](concepts/ertms-dimensioning.md) — Data-size envelope: max N_ITER per packet and minimum memorised on-board for all ETCS packet types | subset40

## Comparisons
*No comparison pages yet.*

## Lint Reports
*No lint reports yet.*
