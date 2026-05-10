# DMI Function

**Source:** [[subset35]], [[subset58]] | **Date:** 2025-07-17 | **Type:** entity

The Driver Machine Interface (DMI) Function allows the active STM to interact with the driver via the ERTMS/ETCS on-board DMI's default window.

## Capabilities

The DMI Function manages [subset58 ¶132]-[subset58 ¶138]:
- **Buttons** — push and release events with timestamps [subset58 ¶658]-[subset58 ¶660]
- **Indicators** — display of information without driver input [subset58 ¶646]-[§655]
- **Sounds** — audible information with configurable frequency and duration [subset58 ¶662]-[§670]
- **Text messages** — display with attributes (colour, flashing), optional driver acknowledgement [subset58 ¶638]-[§644]
- **Supervision information** — permitted speed, target speed, target distance, release speed, intervention speed, colours and display modes [subset58 ¶672]-[§699]

## DMI Channels

Up to four DMI channels (point-to-point connections), with only one active at a time for DMI object communication [subset58 ¶618]-[§622]. The active DMI channel is indicated by packet STM-31 (NID_DMICHANNEL, 3-bit identifier) [subset58 ¶362]-[subset58 ¶363].

## Application Layer Packets (SUBSET-058)

### From STM to DMI Function:
- **STM-32** (val=32): Button Request — create/update up to 24 button visual states (NID_BUTTON, NID_BUTPOS, NID_ICON, M_BUT_ATTRIB, L_CAPTION, X_CAPTION). Sent in HS, DA states. [subset58 ¶197]
- **STM-35** (val=35): Indicator Request — create/update up to 24 indicator visual states (NID_INDICATOR, NID_INDPOS, NID_ICON, M_IND_ATTRIB, L_CAPTION, X_CAPTION). Sent in HS, DA states. [subset58 ¶200]-[subset58 ¶201]
- **STM-38** (val=38): Text Message — display text with identifier NID_XMESSAGE, attributes M_XATTRIBUTE, acknowledgement flag Q_ACK, text L_TEXT/X_TEXT (max 80 bytes). Sent in HS, DA states. [subset58 ¶202]-[subset58 ¶203]
- **STM-39** (val=39): Delete Text Message — deletes previously displayed text by NID_XMESSAGE. Sent in HS, DA states. [subset58 ¶204]-[subset58 ¶205]
- **STM-43** (val=43): Speed and Distance Supervision Information — Q_SCALE, V_PERMIT (10 bits, 0-600 km/h), V_TARGET (7 bits, 0-600 km/h), V_RELEASE (10 bits), V_INTERV (10 bits), D_TARGET (15 bits), colours (M_COLOUR_SP/PS/TS/RS/IS, 3 bits each), display modes (Q_DISPLAY_PS/TS/RS/IS/TD, 2 bits each). Sent in HS, DA states. [subset58 ¶208]-[subset58 ¶209]
- **STM-46** (val=46): Sound Command — max 2 simultaneous sounds, each with NID_SOUND, Q_SOUND (stop/one-shot/continuous), frequency segments (M_FREQ, T_SOUND). Sent in HS, DA states. [subset58 ¶210]-[subset58 ¶211]

### From DMI Function to STM:
- **STM-34** (val=34): Button Event Report — reports button events with NID_BUTTON, Q_BUTTON (push/release), T_BUTTONEVENT (32-bit timestamp in ms). Sent in DA state. [subset58 ¶198]-[subset58 ¶199]
- **STM-40** (val=40): Acknowledgement Reply — reports driver acknowledgement of a text message by NID_XMESSAGE. Sent in DA state. [subset58 ¶206]-[subset58 ¶207]

## Button/Indicator Position Identifiers

Position identifiers (NID_BUTPOS, NID_INDPOS) are 5-bit values (1-24). For unified DMI service, positions map to standard ETCS DMI layout areas (F8-F10, C2-C6, G1-G10, etc.). For customisable DMI service, positions are defined by the STM's layout configuration. [subset58 ¶356]-[subset58 ¶357], [subset58 ¶370]-[subset58 ¶371]

## Access Rules

- Only the active STM can communicate with the driver [subset58 ¶607]
- STMs in HS can send preliminary DMI object requests, displayed upon transition to DA [subset58 ¶613]
- When STM is no longer active, all its DMI objects are deleted [subset58 ¶608]

## Cross-references
- [[stm]] — The Specific Transmission Module
- [[stm-control-function]] — Manages STM states
- [[customisable-dmi]] — Configurable DMI layout service
- [[stm-states]] — STM state definitions
- [[fffis-stm-application-layer]] — Application Layer protocol
