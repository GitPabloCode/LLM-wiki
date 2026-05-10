# Data Engineering Rules

**Source:** [[subset40]] | **Date:** 2025-07-17 | **Type:** concept

Data engineering rules define the content constraints for individual data types transmitted in balise telegrams and radio messages, as specified in SUBSET-040 Section 4.2.4. [subset40 ¶108]

## In-fill Information

In-fill information repeated from the balise group at the next main signal shall be limited to: [subset40 ¶113]

**Permitted packets:**
- Packet 136 (in-fill location reference)
- Packets 12, 80, 49 (MA, Mode Profile, List of Balises for SH area)
- Packet 21 (Gradient Profile)
- Packets 27, 51, 65/66, 70 (SSP, ASP, TSR, Route Suitability)
- Packet 5 (Linking)
- Packet 41 (Level transition)
- Packet 44 (data used outside ERTMS)
- Packets 39, 67, 68 (Track condition)
- Packet 71 (adhesion factor)
- Packet 133 (Radio in-fill area information)

**Prohibited:** Information not related to in-fill, such as data for the opposite direction or EOLM. [subset40 ¶113]

If in-fill contains an immediate level transition announcement at the location reference, D_LEVELTR shall be 0m. [subset40 ¶116]

## Mode Profiles

- Overlapping of mode profile areas in the mode profile packet is forbidden — the system cannot handle two mode profiles at the same location. [subset40 ¶119]
- A Level 1 MA Packet with V_MAIN = 0 shall not include any mode profile packet — a STOP signal aspect must not contain a mode profile. [subset40 ¶120]

## Track Conditions

**Powerless Section (pantograph down):** Minimum announcement-to-start distance corresponds to 17s at line speed (engineered SSP). For sections not requiring pantograph lowering: 11s. The "Distance to change of traction" shall refer to the middle of the permanently earthed neutral contact line section. [subset40 ¶124]

**Other track conditions (Non-stopping area, Air tightness, Brake switch-off):** Minimum announcement-to-start distance corresponds to 10s at line speed. [subset40 ¶126]

## Linking

- Unlinked balise groups shall never be announced via linking. [subset40 ¶130]
- Unlinked balise groups shall never transmit linking information (except as in-fill). They can never become an LRBG. [subset40 ¶131]

## Level Transition Announcement

Trackside shall announce all applicable NID_STM values containing the national system(s) installed. [subset40 ¶135]

## Text Transmission

The end condition "location" shall only be used if the start condition "location" is also used. [subset40 ¶137]

## Packet 131 (RBC Transition Order)

The special value 'Contact the last known RBC' for NID_RBC is forbidden — it would point to the Handing Over RBC, which is meaningless for an RBC handover announcement. [subset40 ¶139]

## Cross-References
- [[dimensioning-rules]] — Message sizing rules complementing data engineering
- [[subset40]] — Full engineering rule document
- [[stm-level-transitions]] — Level transition rules involving STM
