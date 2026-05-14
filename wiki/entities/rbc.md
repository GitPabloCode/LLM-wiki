# Radio Block Centre (RBC)

**Source:** [[subset26]] | **Date:** 2025-07-17 | **Type:** entity

The Radio Block Centre (RBC) is a computer-based trackside system that elaborates messages to be sent to the train based on information from external trackside systems and from on-board subsystems. Its main objective is to provide Movement Authorities (MAs). [subset26 ¶113][subset26 ¶114][subset26 ¶115]

## Functions

- **Movement Authority generation**: Provides MAs including sections, timeouts, overlap, and danger point information [subset26 ¶900]
- **Communication management**: Maintains bi-directional Euroradio sessions with on-board equipment [subset26 ¶450]
- **Train individual tracking**: In Level 2, the RBC knows each ERTMS/ETCS controlled train individually by its ETCS identity [subset26 ¶254]
- **Position tracking**: Uses the LRBG reported by the on-board as position reference [subset26 ¶628]
- **Handover**: Manages automatic RBC/RBC handover, transferring supervision between RBC areas [subset26 ¶2345]
- **Emergency message transmission**: Sends conditional/unconditional emergency stops and revocations [subset26 ¶1175]

## RBC/RBC Handover

Handover involves a **Handing Over RBC** (which hands over control) and an **Accepting RBC** (which accepts control). The Handing Over RBC sends route-related information (MA, linking, speed profiles, gradients, TSRs, mode profiles, track conditions, level transitions, national values, etc.) to the Accepting RBC. [subset26 ¶2351][subset26 ¶2363]

The on-board switches sessions automatically; no driver action is required. [subset26 ¶2347]

## Identification

Each RBC has a unique ETCS identity formed by NID_C (country) + NID_RBC (14-bit number). [subset26 ¶5607]

## Cross-references
- [[ertms-etcs-on-board-equipment]] — The train-borne counterpart
- [[movement-authority]] — Core product of the RBC
- [[communication-session]] — RBC-to-train session management
- [[rbc-handover]] — Between-RBC transition procedure
- [[euroradio]] — Communication protocol used
- [[ertms-etcs-application-levels]] — Levels 2 and 3 require RBC
