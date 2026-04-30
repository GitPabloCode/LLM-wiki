# ERTMS Dimensioning

**Source:** [subset40](../summaries/subset40.md) | **Date:** 2026-04-29 | **Type:** concept

**ERTMS Dimensioning** refers to the quantitative data-size limits that govern how much information can be packed into a single ETCS packet or message, and how much the on-board equipment must be able to store. These limits form the computational and memory envelope within which all interoperable ERTMS/ETCS implementations must operate. The concept spans two perspectives: the **trackside constraint** (maximum N_ITER per packet — what may be transmitted) and the **on-board requirement** (minimum memorised — what must be stored). [¶143-191]

## Trackside vs. on-board limits

For each data type, Subset-040 defines two numbers that serve different purposes [¶148-185]:

- **Maximum N_ITER per packet** — The trackside must not exceed this value when constructing a packet. It ensures that packet sizes remain within the processing and buffering capacity of on-board equipment. Where Subset-040 sets a limit, it overrides the SRS default of 31 iterations. [¶145-146]
- **Minimum memorised on-board** — The on-board must be able to store at least this many items. This value is often **higher** than the per-packet maximum because the on-board may accumulate data across multiple messages (e.g., SSP sections from successive MAs, or TSRs from multiple balise groups). [¶149]

## Dimensioning table

| Data type | Max per packet | Min memorised |
|---|---|---|
| MA sections (excluding end section) | 5 | 6 |
| Balise IDs in SR/Shunting list | 15 | — (replaced on update) |
| Mode profile sections | 2 | — |
| SSP changes | 31 | 50 |
| TSRs | 10 (packets per message) | 30 |
| Gradient changes | 31 | 50 |
| Position report locations | 15 | — (replaced on update) |
| Text messages | 1 plain + 1 fixed | 5 plain + 5 fixed |
| Linked balise groups | 29 | 30 |
| Track conditions — traction power | no iteration | 1 |
| Track conditions — Big Metal Masses | 4 | 5 |
| Track conditions — general | 19 | 20 |
| Route suitability data | 2 | 3 (one per type) |
| Train categories per SSP segment | 15 | — |
| ASP segments | 14 | 30 |
| ASP restriction values per segment | 3 | — |
| Adhesion profiles | no iteration | 10 |
| Reversing area | no iteration | 1 |

## Rationale behind the gaps

The minimum memorised value often exceeds the per-packet maximum for a specific reason [¶150-185]:

- **SSP (50 vs. 31)**: At one SSP change every 500m, 50 sections cover 25km — a practical MA length.
- **TSR (30 vs. 10)**: Multiple balise groups can each contribute up to 10 TSR packets, accumulating to 30 in memory.
- **Linked balise groups (30 vs. 29)**: An MA of 30km with one linked group per km requires 30 entries; 29 iterations in a single packet allows up to 30 groups with the header.
- **MA sections (6 vs. 5)**: In-fill information requires at least one additional section beyond what arrives in a single packet.

## Data flow constraints

The trackside must not request position reports at intervals shorter than **5 seconds**. [¶190-191]

## Cross-references
- [ERTMS Engineering Rules](ertms-engineering-rules.md) — the broader concept these dimensioning limits belong to
- [Balise Installation](balise-installation.md) — the physical installation rules counterpart
- [FFFIS STM Language](fffis-stm-language.md) — the packet structure concept that dimensioning limits constrain
- [subset40](../summaries/subset40.md) — the Dimensioning and Engineering Rules specification
