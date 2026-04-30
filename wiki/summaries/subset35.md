# Subset-035: FFFIS STM — Specific Transmission Module Interface

**Source:** [subset35](subset35.md) | **Date:** 2015-12-16 | **Type:** summary

## Executive summary

SUBSET-035 defines the **Form Fit Functional Interface Specification (FFFIS)** for the **Specific Transmission Module (STM)**, the component that allows the ERTMS/ETCS on-board equipment to interoperate with legacy **National Train Control (NTC)** systems. Issue 3.2.0 (Baseline 3, 2nd release) is a UNISIG document approved by Alstom, Ansaldo, AZD, Bombardier, CAF, Siemens, and Thales. The specification covers everything from the physical connector to the application-layer protocols, ensuring that any STM can connect to any compliant ERTMS/ETCS on-board and that level transitions between ETCS and national systems are seamless — requiring only Eurobalises as trackside markers.

## Key points

- **FFFIS scope** — Covers all protocol levels from the PROFIBUS FDL layer up through Safe Link Layer, Safe Time Layer, and Application Layer, plus physical connectors. The boundary with the trackside is the Interface 'K' antenna specification. [¶59-73]
- **PROFIBUS physical layer** — RS-485 twisted pair at 1500 Kbps, 9-pin female D-SUB connectors. Up to 200 m per segment and 32 stations with cable type A; repeaters extend this. [¶148-167]
- **Eight STM states** form a strict lifecycle: No Power (NP), Power On (PO), Configuration (CO), Data Entry (DE), Cold Standby (CS), Hot Standby (HS), Data Available (DA), and Failure (FA). Only one STM can be in DA (actively supervising) at a time. [¶238-274]
- **Three safety protocol levels** (SL 0, SL 2, SL 4) per CENELEC EN 50159, allowing equipment with different Safety Integrity Levels to coexist on the same bus without the lower-SIL device masquerading as a higher-SIL one. [¶173-181]
- **Connection management** is STM-initiated. A bidirectional version check handshake ensures compatibility: the STM sends its FFFIS STM version number, the ERTMS/ETCS on-board responds with the highest supported matching version. If incompatible, the connection is closed. [¶213-237]
- **Functions accessible to STMs** include the STM Control Function, Reference Time, DMI (4 point-to-point channels + default window), Odometer (multicast), Train Interface (TIU commands/status), Brake Interface (BIU for emergency/service brake), and Juridical Data recorder. Access to each function varies by ETCS mode. [¶83-146]
- **Level transitions** — Annex A provides detailed system diagrams for ETCS→NTC, NTC→ETCS, NTC X→NTC Y, and power-on scenarios, including Trip Mode and Non-Leading/Sleeping variants. [¶56-58]
- **Version management** — The ERTMS/ETCS on-board maintains a legal backward compatibility envelope supporting older FFFIS STM versions, identified by version number X (e.g., X=4 for Baseline 3). [¶218-226]
- **STM isolation** — An STM can be electrically isolated from the bus without disturbing bus operation for other devices. [¶81-82]

## Notable entities and concepts

### Entities
- [STM (Specific Transmission Module)](../entities/stm.md) — The device that adapts a national train protection system to the ERTMS/ETCS on-board via the FFFIS STM interface.
- [NTC (National Train Control)](../entities/ntc.md) — A legacy national train protection system operating alongside or under ETCS.
- [STM Control Function](../entities/stm-control-function.md) — The ERTMS/ETCS on-board function responsible for managing STM states, version compatibility, and data routing between ETCS and STMs.

### Concepts
- [FFFIS (Form Fit Functional Interface Specification)](../concepts/fffis.md) — The specification philosophy covering all protocol levels, connectors, and physical form factors for interchangeable equipment.
- [STM States](../concepts/stm-states.md) — The eight-state lifecycle governing how an STM boots, configures, enters standby, and takes over train supervision.
- [STM Version Check](../concepts/stm-version-check.md) — The bidirectional handshake protocol that ensures FFFIS STM version compatibility before application data is exchanged.

## Cross-references
- [subset35](subset35.md) — this page itself
- [index](../index.md) — wiki catalog
