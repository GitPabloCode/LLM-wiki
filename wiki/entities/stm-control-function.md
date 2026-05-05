# STM Control Function

**Source:** [subset35](../summaries/subset35.md), [subset58](../summaries/subset58.md) | **Date:** 2026-04-29 | **Type:** entity

The **STM Control Function** is the ERTMS/ETCS on-board component responsible for managing all STMs connected to the bus. It acts as the central coordinator for STM state transitions, version compatibility checks, and the routing of data between the ERTMS/ETCS on-board and individual STMs.

## Responsibilities

The STM Control Function handles the following tasks, as defined in the FFFIS STM specification [¶118-130](http://localhost:8765/go.html#subset35-118):

- **STM state management** — controls STM state transitions and monitors the state of each connected STM. [¶119](http://localhost:8765/go.html#subset35-119)
- **Version compatibility** — manages the compatibility check between the ERTMS/ETCS on-board and STM FFFIS STM version numbers during connection establishment. [¶119](http://localhost:8765/go.html#subset35-119)
- **ETCS data transmission** — sends ETCS operational data and status data to STMs, including mode, level, and supervision information. [¶120-121](http://localhost:8765/go.html#subset35-120)
- **Language handling** — transmits the active display language to STMs for driver interface consistency. [¶122](http://localhost:8765/go.html#subset35-122)
- **NTC Data Entry/View** — manages the Specific NTC Data Entry procedure and the NTC Data View for the driver. [¶120](http://localhost:8765/go.html#subset35-120)
- **Override procedure** — handles the Override activation flow (by ETCS or STM), reporting it to all STMs. [¶124](http://localhost:8765/go.html#subset35-124)
- **Airgap data** — transmits ETCS airgap messages (received from balises/loop) to STMs so they can forward relevant information to their NTC trackside. [¶125](http://localhost:8765/go.html#subset35-125)
- **STM max speed and system speed/distance** — receives speed/distance constraints from STMs in HS and DA states to support smooth level transitions. [¶126](http://localhost:8765/go.html#subset35-126)
- **STMPanel test procedure** — handles the initiation and reporting of the STM test procedure. [¶123](http://localhost:8765/go.html#subset35-123)
- **Interface 'K'** — transmits the active antenna/BTM identity to STMs. [¶129](http://localhost:8765/go.html#subset35-129)
- **BTM alarm** — transmits BTM alarm data to STMs. [¶130](http://localhost:8765/go.html#subset35-130)
- **Failure display** — reports STM failure status information for display to the driver. [¶128](http://localhost:8765/go.html#subset35-128)
- **Bus configuration** — distributes the bus addresses and safety levels of all available ERTMS/ETCS on-board functions to STMs during startup. [¶127](http://localhost:8765/go.html#subset35-127)

## Physical addressing

The STM Control Function uses physical PROFIBUS address 2 and SAP 100001 (binary). Each STM must establish a point-to-point connection with the STM Control Function during the Power On (PO) state. [¶190](http://localhost:8765/go.html#subset35-190) [¶203](http://localhost:8765/go.html#subset35-203) [¶244](http://localhost:8765/go.html#subset35-244)

## Application-layer packets

The following SUBSET-058 packets are managed by the STM Control Function [¶132-142](http://localhost:8765/go.html#subset58-132):

- **STM-1** — STM/ETCS function version number (bidirectional, carries N_VERMAJOR and N_VERMINOR)
- **STM-2** — ERTMS/ETCS on-board physical addresses and safety levels for all functions (TIU, BIU, JD, DMI channels 1-4, Odometer)
- **STM-5** — ETCS status data: current mode (M_MODESTM), level (M_LEVEL), and NID_NTC
- **STM-6/7** — Override activation report (STM→ETCS) and Override status change (ETCS→STM)
- **STM-13/14** — State request from STM and state order to STM (NID_STMSTATEREQUEST / NID_STMSTATEORDER)
- **STM-15** — State report from STM (NID_STMSTATE)
- **STM-16/17** — STM max speed and STM system speed/distance for level transition support
- **STM-18** — National Trip Procedure information
- **STM-175** — Train data to STM
- **STM-176** — Train data traction/brake parameters
- **STM-177** — Additional data values and date/time
- **STM-178** — National values to STM
- **STM-181/179/180/182/183/184** — Specific NTC Data Entry/View flow (6 packets)
- **STM-45** — ETCS airgap messages for STM (can appear multiple times in one message)
- **STM-21/22/23** — Test procedure: permission request, permission grant, end of test
- **STM-30** — Driver language transmission
- **STM-31** — Active DMI channel assignment
- **STM-20** — Antenna/BTM identity with Q_CHECKNEEDED
- **STM-47** — BTM alarm data

## Cross-references
- [STM (Specific Transmission Module)](stm.md) — the devices managed by this function
- [NTC (National Train Control)](ntc.md) — the national systems whose data the function routes
- [STM States](../concepts/stm-states.md) — the state machine the Control Function enforces
- [STM Version Check](../concepts/stm-version-check.md) — the compatibility protocol initiated through this function
- [FFFIS STM Language](../concepts/fffis-stm-language.md) — the variables/packets/messages model these packets follow
- [Specific NTC Data Entry](../concepts/specific-ntc-data-entry.md) — the 6-packet handshake managed by this function
- [subset35](../summaries/subset35.md) — the FFFIS STM architecture specification
- [subset58](../summaries/subset58.md) — the FFFIS STM Application Layer specification
