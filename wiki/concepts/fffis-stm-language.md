# FFFIS STM Language

**Source:** [subset58](../summaries/subset58.md) | **Date:** 2026-04-29 | **Type:** concept

The **FFFIS STM Language** is the application-layer protocol that defines how information is structured and transmitted over the PROFIBUS between the ERTMS/ETCS on-board and Specific Transmission Modules (STMs). It is a three-level data model composed of **variables**, **packets**, and **messages**, each with precise encoding and transmission rules. [¶54-58]

## Three-level hierarchy

### Variables

Variables are the fundamental building blocks — single data values that cannot be split into smaller units. Each variable has a unique name and a single meaning. Encoding rules [¶60-85]:

- **Type prefixes** indicate semantic category: `A_` (acceleration), `D_` (distance), `V_` (speed), `M_` (miscellaneous), `N_` (number), `NC_` (class number), `NID_` (identity), `Q_` (qualifier), `T_` (time/date), `X_` (text), `L_` (length), `G_` (gradient).
- Signed values use **2's complement** encoding.
- Boolean values: **0 = false, 1 = true**.
- Offsets should be avoided — 0 means 0, 1 means 1, etc.
- **Most significant bit transmitted first.**
- Variable length is given in bits unless otherwise stated.
- Reserved and spare values shall not be used.

### Packets

Packets group multiple variables into a structured unit with a defined internal format. Every packet follows this structure [¶86-105]:

```
NID_PACKET  (8 bits)   — Unique packet identifier
L_PACKET    (13 bits)  — Total packet length in bits
Q_SCALE     (2 bits)   — Distance scale (only in packets containing distance variables)
[variables...]         — Defined set of variables in top-to-bottom order
```

Rules:
- The packet length includes NID_PACKET, L_PACKET, Q_SCALE (if present), and all other variables, plus iterations.
- The sender must ensure the packet fits within one message.
- **N_ITER** specifies iterations of a variable or group; if N_ITER = 0, no iterated variables follow.
- **N_LITER** is a separate iteration counter for the NTC Data Entry procedure.
- Two nested levels of iteration are permitted.
- **L_CAPTION** / **L_VALUE** / **L_TEXT** specify byte counts for display labels, data values, and text strings, respectively.
- Optional variables (dependent on a preceding qualifier) are shown indented in packet definitions.

Undefined packet identifiers are reserved for future use. All future packets must follow the same structure. [¶92]

### Messages

A message is the complete unit of application data transmitted at a given time. Its structure [¶106-125]:

```
NID_STM         — Identifies which STM is the sender or receiver
L_MESSAGE       — Total message length
[Packet 1]      — NID_PACKET + L_PACKET + variables
[Packet 2...]   — More packets if needed
[Padding bits]  — 0-7 bits to achieve byte alignment for safety layers
```

Rules:
- The message header is identical for all on-board functions and for both directions.
- Messages must be transmitted chronologically by the sender, and processed in reception order by the receiver.
- Generally, no two packets of the same NID_PACKET can appear in one message.
- Exceptions to the no-duplicate rule: STM-45 (airgap messages), STM-38 (text messages), STM-39 (delete text messages), and STM-161 (juridical data) may appear multiple times.

## Backward compatibility

Unknown (non-standard) packets received by a device are silently ignored — the message is not rejected. This allows future extensions without breaking existing equipment. [¶125]

## Cross-references
- [FFFIS](fffis.md) — the specification concept this language implements at the Application Layer
- [Specific NTC Data Entry](specific-ntc-data-entry.md) — the most complex multi-packet procedure using this language
- [STM Version Check](stm-version-check.md) — the STM-1 packet that initiates every connection
- [STM States](stm-states.md) — the state machine governing which packets can be sent when
- [STM Control Function](../entities/stm-control-function.md) — the primary consumer and producer of STM Control packets
- [subset58](../summaries/subset58.md) — the FFFIS STM Application Layer specification
- [subset35](../summaries/subset35.md) — the FFFIS STM architecture specification
