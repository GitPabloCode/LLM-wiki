# RBC (Radio Block Centre)

**Source:** [[subset40]] | **Date:** 2026-05-07 | **Type:** entity

The **Radio Block Centre (RBC)** is the trackside system responsible for issuing Movement Authorities and other information to ETCS-equipped trains via radio messages.

## Handover Rules (§4.1.4)

Level transition borders and RBC/RBC handover borders shall **not** be located where shunting or reversing could take place [¶99](http://localhost:8765/go.html#subset40-99). These areas are not handled in Shunting/Reversing modes [¶99](http://localhost:8765/go.html#subset40-99).

## RBC Transition Order (§4.2.4)

Packet 131 (RBC Transition Order) is forbidden from using the special value 'Contact the last known RBC' for **NID_RBC** [¶139](http://localhost:8765/go.html#subset40-139).

## Radio Messages (§4.2.2)

RBC messages (or radio in-fill messages, using the same protocol) have a maximum application data length of **500 bytes** for normal priority (excluding Euroradio protocol) [¶107](http://localhost:8765/go.html#subset40-107). High priority data is fixed size only [¶107](http://localhost:8765/go.html#subset40-107).

## Cross-references
- [[Level Transition]] — handover rules between RBCs
- [[In-fill]] — radio-based in-fill messages
- [[Message Dimensioning]] — size constraints on RBC messages
- [[subset40]] — source document
