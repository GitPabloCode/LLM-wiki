# TIU Function (Train Interface Unit)

**Source:** [[subset35]], [[subset58]] | **Date:** 2025-07-17 | **Type:** entity

The Train Interface Unit (TIU) Function handles the exchange of train interface information between the train and the STM, transmitting a subset of the train interface signals specified in SUBSET-034 via the FFFIS STM [subset58 ¶102].

## Application Layer Packets (SUBSET-058)

### STM-130 — STM Commands to Train Interface (val=130) [subset58 ¶215]-[subset58 ¶216]
Sent in DA state. Commands transmitted to the train interface:

| Variable | Bits | Description |
|----------|------|-------------|
| M_TIPANTO_CMD | 2 | Pantograph: reserved/raise/lower/keep |
| M_TIFLAP_CMD | 2 | Air tightness: reserved/open/close/keep |
| M_TIMS_CMD | 2 | Main switch/CB: reserved/close/open/keep |
| M_TITR_C_CMD | 2 | Traction cut-off: reserved/cut/no cut/keep |

### STM-129 — STM Specific Brake Control Command (val=129) [subset58 ¶213]-[subset58 ¶214]
Sent in DA state. Brake system inhibition commands:

| Variable | Bits | Description |
|----------|------|-------------|
| M_TIRB_CMD | 2 | Inhibit regenerative brake: reserved/allow/suppress/keep |
| M_TIMSH_CMD | 2 | Inhibit magnetic shoes brake: reserved/allow/suppress/keep |
| M_TIEDCBEB_CMD | 2 | Inhibit eddy current brake for EB: reserved/allow/suppress/keep |
| M_TIEDCBSB_CMD | 2 | Inhibit eddy current brake for SB: reserved/allow/suppress/keep |

### STM-139 — Train Interface Inputs Status/Availability to STM (val=139) [subset58 ¶217]-[subset58 ¶218]
Sent in PO, CO, DE, CS, HS, DA states. Status signals:

| Variable | Bits | Description |
|----------|------|-------------|
| M_TITR_STATUS | 2 | Traction status: fail/off/on/spare |
| M_TIDIR_STATUS | 3 | Direction handle: fail/forward/neutral/reserved/backward |
| M_TICAB_STATUS | 2 | Cab status: fail/cab A/cab B/no cab |

### STM-141 — Train Interface Command Configuration to STM (val=141) [subset58 ¶219]-[subset58 ¶220]
Sent in PO, CO, DE, CS, HS, DA states. Availability flags (1-bit each) for each TIU command:

| Variable | Description |
|----------|-------------|
| M_TIRB_CMD_AVAIL | Regenerative brake command availability |
| M_TIMSH_CMD_AVAIL | Magnetic shoes brake command availability |
| M_TIEDCBEB_CMD_AVAIL | Eddy current brake for EB command availability |
| M_TIEDCBSB_CMD_AVAIL | Eddy current brake for SB command availability |
| M_TIPANTO_CMD_AVAIL | Pantograph command availability |
| M_TIFLAP_CMD_AVAIL | Air tightness command availability |
| M_TIMS_CMD_AVAIL | Main switch/CB command availability |
| M_TITR_C_CMD_AVAIL | Traction cut-off command availability |

## Signal Mapping

| Signal | Description |
|--------|-------------|
| Regenerative Brake | Allow/suppress regenerative brake use |
| Magnetic Shoe Brake | Allow/suppress magnetic shoe brake use |
| Eddy Current Brake (Service) | Allow/suppress eddy current brake for service brake |
| Eddy Current Brake (Emergency) | Allow/suppress eddy current brake for emergency brake |
| Pantograph | Lower or raise the pantograph |
| Air Tightness | Open or close air flaps |
| Main Switch / Circuit Breaker | Open or close (single command) |
| Traction Cut Off | Cut off or not the traction |

## TIU Status Signals (Train Interface → STM)

| Signal | Description |
|--------|-------------|
| Traction status | Status of traction power |
| Direction Controller information | Position of direction controller |
| Cab Status | Active cab information |

## Service and Emergency Brake

These are handled via the [[biu-function]], not the TIU [subset58 ¶107][subset58 ¶109].

## Cross-references
- [[stm]] — The Specific Transmission Module
- [[biu-function]] — Brake Interface Unit
- [[stm-control-function]] — STM state management
- [[fffis-stm-application-layer]] — Application Layer protocol
