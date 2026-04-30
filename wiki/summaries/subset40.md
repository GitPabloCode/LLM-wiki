# Subset-040: Dimensioning and Engineering Rules

**Source:** [subset40](subset40.md) | **Date:** 2009-04-07 | **Type:** summary

## Executive summary

SUBSET-040 defines the mandatory **Dimensioning and Engineering Rules** for ERTMS/ETCS Class 1 installations. Issue 2.3.0, aligned with SRS 2.3.0, establishes system-level installation constraints for balises, Eurobalise antennas, Euroloops, telegrams, and radio messages. These rules are complementary to the SRS and FFFIS/FFFS sub-documents — they constrain without contradicting, ensuring that trains from any supplier can interoperate on any compliant infrastructure. The document also specifies maximum data sizes for all ETCS packet types (max N_ITER per packet) and the corresponding minimum storage capacity required on-board, forming the envelope within which all ERTMS/ETCS deployments must operate.

## Key points

- **Engineering rules are mandatory** — They provide additional constraints to SRS requirements to ensure interoperability. Project-specific rules may add to but cannot relax these. The rules do not define everything needed for a project, but nothing that complies with them may be excluded. [¶28-35]
- **Balise spacing within a group** — Maximum 12m between two consecutive balises (reference mark to reference mark), balancing quick detection of missing balises against the minimum cross-talk protection distance. [¶60-61]
- **Signal balises and the stopping point (Level 1)** — Any balise in rear of the operational stopping point must be no more than 0.7m behind it, ensuring a stopped train (antenna ~2m from front, side lobe zone 1.3m) cannot read the next signal's balise group. [¶62-63]
- **Balise group before EOA/LOA (Level 1)** — The last balise of an MA-giving or level-transition-ordering group must be at least 1.3m in rear of the EOA/LOA, guaranteeing the antenna has fully read the group before the train's minimum safe antenna position passes the authority limit. [¶64-65]
- **Switchable balises and train detection (Level 1)** — When a change of train detection section affects balise information, the last switchable balise must be ≥13.8m in rear of where the next section's detection device may first sense the train (12.5m worst-case axle-to-antenna distance + 1.3m side lobe). [¶66-67]
- **Balise processing rate** — Within distance `d` (= max line speed × 0.8s), no more than 8 balises may be encountered, driven by on-board balise telegram processing capacity. [¶68-69]
- **Minimum curve radius** — Balises should be placed on curves ≥300m radius. Lower values require detailed analysis of lateral antenna deviation. This does not forbid tight curves on the network, only balise placement within them. [¶70-80]
- **Antenna mounting on the train** — Minimum 2m from front of engine to antenna reference mark (preventing cross-antenna interference); maximum 12.5m from front to 1st axle (allowing enough room for installation on all train types). [¶90-92]
- **Balise telegram sizes by speed** — 0-300 km/h: long or short telegrams for all balise sizes. 300-500 km/h: long or short for standard balises, but only short telegrams for reduced-size balises. [¶102-103]
- **Radio message size** — Application data (excluding Euroradio protocol) sent as normal priority shall not exceed 500 bytes per message. High-priority messages are always fixed-size so no limit is needed. [¶106-107]
- **In-fill content restriction** — In-fill information repeated from the main signal balise group is limited to MA, linking, gradient profile, SSP, TSR, track conditions, level transition, and in-fill location reference. General-purpose data (e.g., opposite direction info) is excluded. [¶111-114]
- **Data dimensioning table** — For each ETCS data type, the specification defines both the maximum N_ITER per packet (trackside constraint) and the minimum memorised value on-board (train constraint): MA sections (5/6), SSP changes (31/50), TSRs (10/30), gradients (31/50), linked balise groups (29/30), track conditions (19/20), text messages (1+1/5+5), and more. [¶143-185]
- **Position report timing** — Trackside shall not require position reports at intervals shorter than 5 seconds. [¶190-191]
- **Level transitions and RBC handovers** — These borders shall not be located where shunting or reversing could take place, since these modes do not handle transitions. [¶98-99]
- **KER compatibility appendix** — Additional non-ERTMS rules for equipment supporting KER-compatible national systems, referencing SUBSET-100 and SUBSET-101. [¶192-195]

## Notable entities and concepts

### New concepts
- [ERTMS Engineering Rules](../concepts/ertms-engineering-rules.md) — the concept of mandatory, complementary dimensioning constraints on top of the SRS
- [Balise Installation](../concepts/balise-installation.md) — installation constraints and spatial rules for balises and antennas
- [ERTMS Dimensioning](../concepts/ertms-dimensioning.md) — the data-size envelope (max per packet, minimum on-board) for all ETCS packet types

## Cross-references
- [ertms-engineering-rules](../concepts/ertms-engineering-rules.md) — the overarching concept this specification embodies
- [balise-installation](../concepts/balise-installation.md) — the spatial installation constraints for balises
- [ertms-dimensioning](../concepts/ertms-dimensioning.md) — the data dimensioning table
- [subset35](subset35.md) — the FFFIS STM specification (referenced in level transition rules)
- [index](../index.md) — wiki catalog
