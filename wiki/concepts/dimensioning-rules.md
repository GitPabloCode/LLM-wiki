# Dimensioning Rules

**Source:** [[subset40]] | **Date:** 2025-07-17 | **Type:** concept

Dimensioning rules define the maximum number of iterations per packet and minimum onboard memory requirements for data elements in ERTMS/ETCS messages, as specified in SUBSET-040 Section 4.3. [subset40 ¶143]

## Core Principle

If engineering rules limit the number of iterations of a certain information type, this takes precedence over the default 31-iteration maximum stated in the SRS (SUBSET-026 Chapter 7). The SRS value range was chosen to rationalise the ETCS language, but specific limits are defined here. [subset40 ¶146]

## Data Dimensioning Table

| Data Element | Section | Max Iterations per Packet | Min Memorised Onboard |
|---|---|---|---|
| MA sections (excluding End Section) | a | 5 | 6 |
| Balise IDs for SR/shunting | b | 15 | — |
| Mode profile sections | c | 2 | — |
| SSP changes | d | 31 | 50 |
| TSR packets | e | 10 *per message* | 30 |
| Gradient changes | f | 31 | 50 |
| Position report locations | g | 15 | — |
| Text messages | h | 1 plain + 1 fixed | 5 plain + 5 fixed |
| Linked balise groups | i | 29 | 30 |
| Track condition — change of traction | j | No iteration in packet | 1 |
| Track condition — Big Metal masses | k | 4 | 5 |
| Track conditions (general) | l | 19 | 20 |
| Route suitability data | m | 2 | 3 |
| Train categories per SSP segment | n | 15 | — |
| Axle load speed profile segments | o | 14 | 30 |
| Axle load speed restrictions per segment | p | 3 | — |
| Adhesion profiles | q | No iteration in packet | 10 |
| Reversing areas | r | No iteration in packet | 1 |

## Key Rationale

- **MA sections (6 onboard):** In-fill information requires at least one additional section to be stored compared to what can be transmitted in a single packet. [subset40 ¶151]
- **Linked balise groups (30 onboard):** Sufficient for 30km with an average of 1 linked group per km. New linking info completely overwrites old info. Exception: in-fill linking must account for balises between in-fill location and reference location. [subset40 ¶167]
- **SSP and gradient (50 onboard):** With a change every 500m, 50 sections cover 25km. [subset40 ¶157][subset40 ¶161]
- **TSR (30 onboard):** No specific justification given. [subset40 ¶159]

## General Constraints

- The maximum number of packet iterations is stated per packet (N_ITER value) unless otherwise specified [subset40 ¶149]
- Multiple instances of the same packet in a message follow SUBSET-026 Section 8.4.1.4 [subset40 ¶188]
- Trackside shall not require position reports at intervals shorter than 5 seconds [subset40 ¶191]

## Cross-References
- [[data-engineering-rules]] — Complementary rules for data content
- [[balise-group]] — Linking capacity affects group configuration
- [[subset40]] — Full engineering rule document
