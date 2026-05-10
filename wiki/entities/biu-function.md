# BIU Function (Brake Interface Unit)

**Source:** [[subset35]], [[subset58]] | **Date:** 2025-07-17 | **Type:** entity

The Brake Interface Unit (BIU) Function handles Emergency Brake and Service Brake commands and status between the STM and the ERTMS/ETCS on-board. It is separated from the [[tiu-function]] to allow different safety and performance levels [subset58 ¶114].

## Application Layer Packets (SUBSET-058)

### STM-128 — STM Emergency and Service Brake Command to Brake Interface (val=128) [subset58 ¶222]-[subset58 ¶223]
Sent by the STM in DA state. Commands:

| Variable | Bits | Values |
|----------|------|--------|
| M_BIEB_CMD | 2 | 00=reserved, 01=apply EB, 10=release EB, 11=keep current |
| M_BISB_CMD | 2 | 00=apply SB (or EB if SB fails), 01=apply SB, 10=release SB, 11=keep current |

### STM-136 — Brake Interface Emergency and Service Brake Status/Availability to STM (val=136) [subset58 ¶224]-[subset58 ¶225]
Sent in PO, CO, DE, CS, HS, DA states. Status:

| Variable | Bits | Values |
|----------|------|--------|
| M_BIEB_STATUS | 2 | 00=fail, 01=not available, 10=available, 11=reserved |
| M_BISB_STATUS | 2 | 00=fail, 01=not available, 10=available, 11=reserved |

### STM-143 — Emergency and Service Brake Parameters to STM (val=143) [subset58 ¶226]-[subset58 ¶227]
Sent in PO, CO, DE, CS, HS, DA states. Configuration:

| Variable | Bits | Description |
|----------|------|-------------|
| T_EB_MAXDELAY | 8 | Max EB command issue delay (10-2550 ms, step 10ms). 0=reserved. |
| T_SB_MAXDELAY | 8 | Max SB command issue delay (10-2550 ms, step 10ms). 0=not applicable. |

## Brake Performance Parameters

Brake performance parameters (maximum time delay for ETCS to process STM brake commands) are transmitted to STMs when connection is established [subset58 ¶255][subset58 ¶555].

## Access Rules

BIU commands (STM-128) are only available to the active STM in SN mode [subset58 ¶146]. BIU status/parameters (STM-136, STM-143) are available to all STMs in all states.

## Cross-references
- [[stm]] — The Specific Transmission Module
- [[tiu-function]] — Train Interface Unit
- [[stm-control-function]] — STM state management
- [[stm-states]] — STM state definitions
- [[fffis-stm-application-layer]] — Application Layer protocol
