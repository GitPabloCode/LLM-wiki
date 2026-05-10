# SUBSET-058: FFFIS STM Application Layer

**Source:** [[subset58]] | **Date:** 2025-07-17 | **Type:** summary

SUBSET-058 (v3.2.0, 2015-12-16) specifies the FFFIS STM Application Layer — the data formats, variables, packets, and messages used for communication between Specific Transmission Modules (STMs) and ERTMS/ETCS on-board functions over the PROFIBUS link. It is the layer immediately above the Safe Time Layer (SUBSET-056). [subset58 ¶42]-[subset58 ¶48]

## Scope

The document defines the complete application-level protocol: variables (encoding rules, prefixes, lengths), packets (structures, identifiers, iteration rules), and messages (headers, ordering, padding). It forms part of the FFFIS STM stack: Application Layer [4] → Safe Time Layer [5] → Safe Link Layer [6] → PROFIBUS FDL. [subset58 ¶44]-[subset58 ¶48]

## Language Components

The FFFIS STM language is built from three levels [subset58 ¶57]:

- **Variables** — single data values with unique names and defined encodings. Prefix conventions: A_ (acceleration), D_ (distance), G_ (gradient), L_ (length), M_ (miscellaneous), N_ (number), NID_ (identity number), Q_ (qualifier), T_ (time/date), V_ (speed), X_ (text). [subset58 ¶68]-[subset58 ¶85]
- **Packets** — groups of variables with a unique NID_PACKET identifier, length (L_PACKET), and optional Q_SCALE. Two nested levels of iteration (N_ITER, N_LITER) are supported. [subset58 ¶86]-[subset58 ¶104]
- **Messages** — the complete application data unit, composed of a header (NID_STM + L_MESSAGE) followed by one or more packets, with optional padding bits for byte alignment. [subset58 ¶106]-[subset58 ¶124]

## Packet Categories

Packets are organised by function:

- **All on-board functions (ETCS+STM):** STM-1 (version number), STM-15 (state report) [subset58 ¶127]-[subset58 ¶131]
- **STM Control Function:** STM-2 (addresses/safety), STM-5 (ETCS status), STM-6 (override activation), STM-7 (override status), STM-13 (state request), STM-14 (state order), STM-16/17 (transition variables), STM-18 (National Trip Procedure), STM-175/176/177/178 (train data, traction/brake, additional data, national values), STM-179/180/181/182/183/184 (Specific NTC Data Entry/View), STM-45 (airgap message), STM-21/22/23 (test procedure), STM-30 (driver language), STM-31 (active DMI channel), STM-20 (antenna/BTM ID), STM-47 (BTM status) [subset58 ¶132]-[subset58 ¶189]
- **Odometer Function:** STM-9 (odometer parameters), STM-8 (odometer multicast) [subset58 ¶190]-[subset58 ¶194]
- **DMI Function:** STM-32 (button request), STM-34 (button event), STM-35 (indicator request), STM-38 (text message), STM-39 (delete text), STM-40 (acknowledgement reply), STM-43 (speed/distance supervision), STM-46 (sound command) [subset58 ¶195]-[subset58 ¶211]
- **TIU Function:** STM-129 (brake control), STM-130 (train commands), STM-139 (TIU status), STM-141 (command configuration) [subset58 ¶212]-[subset58 ¶220]
- **BIU Function:** STM-128 (brake command), STM-136 (brake status), STM-143 (brake parameters) [subset58 ¶221]-[subset58 ¶227]
- **Juridical Data Function:** STM-161 (STM information to JD) [subset58 ¶228]-[subset58 ¶230]

## Variables (121 defined)

Variables include odometry values (D_EST, V_EST, D_MAX, D_MIN, D_RES, etc.), brake commands/status (M_BIEB_CMD, M_BISB_STATUS, etc.), train interface commands (M_TIRB_CMD, M_TIPANTO_CMD, M_TIFLAP_CMD, etc.), DMI attributes (M_BUT_ATTRIB, M_IND_ATTRIB, M_XATTRIBUTE, M_COLOUR_*, etc.), address identifiers (N_ADDR_*, NID_*), timer/date variables, and text strings (X_CAPTION, X_TEXT, X_VALUE). [subset58 ¶231]-[subset58 ¶475]

## Key Rules

- Messages are transmitted chronologically; the first transmitted message is the oldest [subset58 ¶110]
- It is forbidden to send multiple instances of the same packet type in one message, with four exceptions: STM-45 (airgap), STM-38 (text), STM-39 (delete text), STM-161 (JD data) [subset58 ¶117]-[subset58 ¶121]
- Non-standard packets (NID_PACKET 200-255) unknown to the receiver shall be ignored, not rejected [subset58 ¶125]
- Variables are encoded with MSB first, signed values as 2's complement, Boolean as 0=false/1=true [subset58 ¶64]-[subset58 ¶67]
- Padding bits (0-7) complete message byte alignment for safety layer transmission [subset58 ¶124]

## Cross-references
- [[stm]] — The Specific Transmission Module
- [[stm-control-function]] — Manages STM states and data forwarding
- [[dmi-function]] — Driver Machine Interface
- [[tiu-function]] — Train Interface Unit
- [[biu-function]] — Brake Interface Unit
- [[odometer-function]] — Odometry data provision
- [[juridical-data-function]] — Juridical recording
- [[fffis-stm-application-layer]] — Conceptual overview of the protocol structure
- [[subset35]] — FFFIS STM system-level specification
- [[profibus]] — The underlying communication bus
