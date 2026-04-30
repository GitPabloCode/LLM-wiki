# Subset-058: FFFIS STM Application Layer

**Source:** [subset58](subset58.md) | **Date:** 2015-12-16 | **Type:** summary

## Executive summary

SUBSET-058 defines the **Application Layer** of the FFFIS STM interface — the concrete data formats that flow over the PROFIBUS between the ERTMS/ETCS on-board and Specific Transmission Modules (STMs). Issue 3.2.0 (Baseline 3, 2nd release) specifies the complete language: **variables** (single data units with type-coded prefixes), **packets** (groups of variables identified by NID_PACKET and L_PACKET), and **messages** (one or more packets prefixed with NID_STM and L_MESSAGE). The specification organises ~30+ packet types by on-board function — STM Control, Odometer, DMI, Train Interface (TIU), Brake Interface (BIU), and Juridical Data (JD) — and defines a catalogue of ~120 variables with encoding rules.

## Key points

- **Three-level data model** — Variables encode single values (signed as 2's complement, one-bit values as Boolean). Packets have a mandatory `NID_PACKET` (8 bits) + `L_PACKET` (13 bits) header, optionally followed by `Q_SCALE` (2 bits) when distance values are present. Messages consist of `NID_STM` + `L_MESSAGE` header, one or more packets, and padding bits to achieve byte alignment for the safety layers. [¶55-125]
- **Variable naming convention** — Prefixes indicate semantic type: `A_` (acceleration), `D_` (distance), `V_` (speed), `M_` (miscellaneous), `N_` (number), `NID_` (identity), `NC_` (class number), `Q_` (qualifier), `T_` (time/date), `X_` (text). Most significant bit transmitted first. Special values and offsets avoided. [¶60-85]
- **Packet catalogue by function** — STM Control handles ~18 packet types: version check (STM-1), physical addresses (STM-2), ETCS status (STM-5), Override (STM-6/7), state requests/orders (STM-13/14), train data (STM-175/176/177/178), National Values (STM-178), Specific NTC Data (STM-181/179/180/182/183/184), airgap messages (STM-45), test procedure (STM-21/22/23), language (STM-30), active DMI channel (STM-31), antenna/BTM (STM-20), and BTM alarm (STM-47). [¶132-142]
- **DMI packets** — STM-34 (button events), STM-35 (indicator requests), STM-38 (text messages), STM-39 (delete text), STM-40 (acknowledgement reply), STM-43 (speed/distance supervision info), and STM-46 (sound commands). Multiple STM-38 and STM-39 packets may appear in a single message. [¶143-151]
- **Odometer packets** — STM-9 transmits odometer configuration parameters to STMs (point-to-point). STM-8 sends estimated odometer values via multicast (estimated speed `V_EST`, estimated distance `D_EST`, time reference). [¶152-153]
- **Train & Brake Interface packets** — TIU: STM-129 (STM-specific brake control), STM-130 (commands: pantograph, traction, brake types), STM-139 (status/availability), STM-141 (command configuration). BIU: STM-128 (emergency and service brake commands), STM-136 (brake status/availability), STM-143 (brake parameters: max delays for emergency/service brake processing by ETCS). [¶154-158]
- **Juridical Data** — Packet STM-161 carries national juridical data from the STM to the on-board recording device, including NID_STM, timestamp, and national recorder information. [¶159]
- **Backward compatibility rules** — Non-standard packets unknown to the receiver are silently ignored (message is not rejected). Multiple copies of STM-45 (airgap messages), STM-38 (text), STM-39 (delete text), and STM-161 (juridical data) are allowed in the same message, overriding the general no-duplicate rule. Nested iterations (two levels) are supported via `N_ITER` and `N_LITER`. [¶93-121]
- **Message ordering** — Messages must be transmitted chronologically by the sender and processed in reception order by the receiver. Packets within a message must be processed as if each were handled separately in received order. [¶110-111, 122]

## Notable entities and concepts

### New entities
- [STM Control Function](../entities/stm-control-function.md) — updated with application-layer packet responsibilities

### New concepts
- [FFFIS STM Language](../concepts/fffis-stm-language.md) — the variables/packets/messages data model forming the application-layer protocol
- [Specific NTC Data Entry](../concepts/specific-ntc-data-entry.md) — the 6-packet handshake procedure for entering national operational data

### Updated concepts
- [STM Version Check](../concepts/stm-version-check.md) — added STM-1 packet structure (N_VERMAJOR, N_VERMINOR)

## Cross-references
- [subset35](subset35.md) — the FFFIS STM architecture specification that references these packets
- [FFFIS STM Language](../concepts/fffis-stm-language.md) — the data model this specification defines
- [Specific NTC Data Entry](../concepts/specific-ntc-data-entry.md) — the data entry protocol defined herein
- [STM Control Function](../entities/stm-control-function.md) — the on-board function that originates and consumes most of these packets
- [index](../index.md) — wiki catalog
