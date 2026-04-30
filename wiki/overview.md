# Overview

## Current state

The wiki contains three ingested sources spanning two layers of the ERTMS/ETCS system:

- **On-board / STM layer**: SUBSET-035 (architecture and state machine) and SUBSET-058 (Application Layer protocol) define how ERTMS/ETCS interoperates with legacy National Train Control (NTC) systems through Specific Transmission Modules (STMs).
- **Trackside / engineering layer**: SUBSET-040 (Dimensioning and Engineering Rules) defines the mandatory physical and data-size constraints for ERTMS/ETCS infrastructure — balises, antennas, Euroloops, radio — that ensure any compliant train can operate on any compliant track.

## Architecture picture

### On-board STM subsystem

The FFFIS STM establishes a **PROFIBUS-based on-board bus** where multiple STMs coexist, each representing a different national system. The ERTMS/ETCS on-board provides shared functions (DMI, odometer, train interface, brake interface, juridical recorder) that STMs access through Service Access Points (SAPs). The **STM Control Function** (physical address 2) acts as the bus coordinator, managing STM states and routing data.

The **FFFIS STM Language** (Subset-058) defines the concrete protocol: ~120 variables with type-coded prefixes, ~30+ packet types organised by on-board function, and messages that bundle packets with NID_STM addressing and byte-aligned padding. The most complex protocol sequence is the **Specific NTC Data Entry** 6-packet handshake for entering national operational data during STM startup.

### Trackside infrastructure constraints

**Engineering rules** (Subset-040) form a mandatory constraint layer between the SRS and project-specific implementation. They cover three domains: **installation** (spatial relationships for balises, antennas, Euroloops), **telegrams** (content and speed-based format restrictions), and **dimensioning** (a comprehensive table of max N_ITER per packet and minimum memorised on-board for every ETCS data type — from MA sections to track conditions to linked balise groups).

## Key relationships

- An **STM** is always associated with exactly one **NTC** (identified by NID_NTC = NID_STM).
- Only **one STM** can be in the Data Available (DA) state at a time, meaning only one national system supervises the train.
- **Level transitions** between ETCS and NTC (or between two NTCs) are triggered by Eurobalises — the trackside needs no additional infrastructure beyond what ETCS already requires.
- The **DMI function** gives the active STM a dedicated "default window" on the driver's display.
- Every STM-to-function connection starts with a **STM-1 version check** handshake (N_VERMAJOR + N_VERMINOR).
- **Balise installation rules** (Subset-040) precisely govern where Eurobalises can be placed relative to signals, stopping points, EOA/LOA, train detection boundaries, and curves — ensuring the STM's trackside data source is physically reliable.
- **Dimensioning limits** bridge the trackside and on-board: the trackside must not exceed a given N_ITER per packet, while the on-board must be able to store more than the per-packet maximum to accumulate data across multiple messages.

## Cross-source connections

- Subset-058's packet catalogue maps directly to Subset-035's STM Control Function responsibilities.
- Subset-035's level transition chapter (§7.5) is referenced by Subset-040's level transition engineering rules.
- Subset-040 references SUBSET-035 v2.1.1 (STM FFFIS) and SUBSET-036 (Eurobalise FFFIS) as authoritative sources for the installation rules it summarises and constrains.
- Subset-040's dimensioning table constrains the SRS (SUBSET-026) — it overrides the default N_ITER=31 where tighter limits are needed for interoperability.

## Gaps

- No SUBSET-026 (System Requirements Specification) — the core SRS that defines modes, levels, variables, and procedures referenced by all three ingested subsets.
- No SUBSET-036 (Eurobalise FFFIS), SUBSET-044 (Euroloop FFFIS), SUBSET-056 (Safe Time Layer), or SUBSET-057 (Safe Link Layer) — referenced throughout the ingested subsets.
- No real-world STM implementations or NTC-specific pages yet.
- No comparison pages.
