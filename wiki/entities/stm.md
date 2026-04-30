# STM (Specific Transmission Module)

**Source:** [subset35](../summaries/subset35.md) | **Date:** 2026-04-29 | **Type:** entity

A **Specific Transmission Module (STM)** is an on-board device that adapts a legacy **National Train Control (NTC)** system to the ERTMS/ETCS on-board equipment. Each STM implements the FFFIS STM interface, allowing it to connect via PROFIBUS to the ERTMS/ETCS on-board and supervise train movements when operating in Level NTC / mode SN (National System).

## Identification

Each STM is identified by a unique **NID_STM** number, which must equal one of the NID_NTC values defined in the ERA_ERTMS_040001 assignment of values document. [¶76]

## States

An STM progresses through eight defined states during its lifecycle: NP → PO → CO → (DE) → CS → HS → DA, with FA (Failure) reachable from most states. Only one STM can be in DA (actively supervising) at a time. The ERTMS/ETCS on-board monitors the active STM's safety integrity and applies the emergency brake on failure of the active STM. [¶78-79, 238-274]

## Access to ERTMS/ETCS functions

An STM can access the following ERTMS/ETCS on-board functions through the FFFIS STM interface: STM Control, Reference Time, DMI (4 channels + default window), Odometer (multicast), Train Interface (TIU commands and status), Brake Interface (BIU for emergency and service brake), and Juridical Data recording. Access rights depend on the STM's current state and the ETCS operating mode. [¶85-92, 139-146]

## Physical addressing

By default, an STM's physical PROFIBUS address is `NID_NTC + 70`. A configurable address range (50-69) is available when the default calculation exceeds the PROFIBUS address range. Multiple STMs can share a physical address by differentiating themselves at the Application Layer using their NID_STMs. [¶187-194]

## Isolation

An STM can be isolated from the bus without disturbing the operation of other connected devices. [¶82]

## Cross-references
- [NTC (National Train Control)](ntc.md) — the legacy system an STM interfaces with
- [STM Control Function](stm-control-function.md) — the ERTMS/ETCS function that manages STMs
- [STM States](../concepts/stm-states.md) — the eight-state lifecycle
- [FFFIS](../concepts/fffis.md) — the interface specification concept the STM implements
- [STM Version Check](../concepts/stm-version-check.md) — how compatibility is negotiated at connection
- [subset35](../summaries/subset35.md) — the FFFIS STM specification
