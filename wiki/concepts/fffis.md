# FFFIS (Form Fit Functional Interface Specification)

**Source:** [subset35](../summaries/subset35.md) | **Date:** 2026-04-29 | **Type:** concept

**FFFIS** stands for **Form Fit Functional Interface Specification**. It is the specification philosophy used in ERTMS/ETCS for interfaces between equipment from different suppliers. A FFFIS covers all three aspects needed for true interchangeability: the **form** (physical connectors and dimensions), the **fit** (compatibility at physical and electrical levels), and the **function** (all protocol layers of communication).

## Scope boundaries

In the context of SUBSET-035 (the FFFIS STM) [¶63-65]:

- **Lower boundary**: The PROFIBUS Field Data Link (FDL) layer. The PROFIBUS standards (CENELEC 50170-2) cover the physical layer including connectors. [¶64]
- **Upper boundary**: The functions linked to the interface between the ERTMS/ETCS on-board equipment and an STM — essentially the Application Layer services. [¶65]

## Protocol layers

The FFFIS STM protocol stack has four layers [¶206-211]:

1. **Application Layer** (defined in SUBSET-058) — message formats and procedures
2. **Safe Time Layer** (defined in SUBSET-056) — safe timestamping and sequence numbering
3. **Safe Link Layer** (defined in SUBSET-057) — safe addressing and error detection
4. **PROFIBUS FDL** (defined in CENELEC 50170-2) — fieldbus data link

The Safe Time Layer and Safe Link Layer together form the **Safety Layers**. [¶208]

## Interchangeability goal

The FFFIS STM enables the ERTMS/ETCS on-board equipment to be connected to any STM, meaning the on-board and the STMs are interchangeable. The assembly achieves the same functionality as the legacy national system while ensuring seamless transitions between ETCS and NTC, with no extra trackside equipment beyond Eurobalises. [¶66-68]

## Cross-references
- [STM States](stm-states.md) — the state machine the FFFIS STM defines for STMs
- [STM Version Check](stm-version-check.md) — version compatibility negotiation within the FFFIS STM
- [STM](../entities/stm.md) — the device that implements this interface
- [subset35](../summaries/subset35.md) — the FFFIS STM specification
