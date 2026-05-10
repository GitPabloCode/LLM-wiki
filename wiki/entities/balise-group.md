# Balise Group

**Source:** [[subset40]] | **Date:** 2025-07-17 | **Type:** entity

A balise group is a set of one or more Eurobalises installed together on the trackside, treated as a complete device for ERTMS/ETCS purposes. Balise groups transmit messages (composed of telegrams from individual balises) to passing trains. [subset40 ¶42][subset40 ¶54]

## Configuration Rules

- A balise group is considered as a complete device limited by the reference locations of its outer balises [subset40 ¶42]
- The reference location of a balise group is the reference location of the outer balise with N_PIG variable = 0 [subset40 ¶43]
- The "last switchable balise" of a group is the last encountered switchable balise with regards to the group crossing direction [subset40 ¶44]
- Distance between groups is measured between the closest balises' Reference Marks, which differs from the linking distance (measured between N_PIG=0 balises of each group) [subset40 ¶45][subset40 ¶46]

## Spacing Rules

**Maximum spacing within a group:** 12m between consecutive balises (reference mark to reference mark). This allows early detection of a potentially missing balise. [subset40 ¶61]

**Minimum spacing:** Must respect the FFFIS Eurobalise (SUBSET-036) cross-talk protection and air gap interface requirements. [subset40 ¶59]

## Group Usage

- **Unlinked groups:** Balise groups with qualifier "unlinked" shall never be announced via linking, and shall never be used to transmit linking information (except as in-fill information). This avoids contradictions between the consistency reaction for unlinked groups and the announced linking reaction. [subset40 ¶130][subset40 ¶131]
- **Number of balises per group:** Must follow SUBSET-091 safety requirements, including rules for single balise groups and TSR balise groups. [subset40 ¶82]
- **Linking capacity:** A single linking packet can transmit up to 30 linked balise groups (29 iterations). Onboard memory stores 30 linked groups, sufficient for 30km at 1 group/km. [subset40 ¶167]

## Cross-References
- [[eurobalise]] — Individual balise component
- [[subset40]] — Full engineering rule document
- [[dimensioning-rules]] — Message dimensioning rules including linking capacity
