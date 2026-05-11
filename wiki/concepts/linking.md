# Linking (Balise)

**Source:** [[subset26-1]] | **Date:** 2026-05-12 | **Type:** concept

Linking is the mechanism by which balise groups are announced in advance to the on-board equipment. It serves three purposes: detecting missed balise groups, assigning coordinate systems to single balise groups, and correcting the odometer confidence interval. [subset26-1 ¶398-¶401]

## Linking Information Content

Each linking packet specifies:
- Identity of the linked balise group [subset26-1 ¶406]
- Where the location reference must be found [subset26-1 ¶407]
- Location accuracy [subset26-1 ¶408]
- Direction with which the group will be passed (nominal/reverse) [subset26-1 ¶410]
- Reaction required on data consistency problem [subset26-1 ¶411]

## Linking Reactions

Three possible reactions to data inconsistencies: Train trip, Service brake, or No reaction. [subset26-1 ¶417-¶420]

## Expectation Window

The on-board expects a balise group within a defined window: from when the max safe front end passes the first possible location until the min safe front end passes the last possible location. [subset26-1 ¶433-¶439]

## Unlinked Balise Groups

Balise groups not announced by linking can still be taken into account if marked as "unlinked". They must consist of at least two balises and contain the unlinked qualifier. [subset26-1 ¶422-¶425]

## Rules

- When no linking information is used, all balise groups are taken into account [subset26-1 ¶427]
- When linking is used, only linked (announced) and unlinked groups are accepted [subset26-1 ¶428]
- Balise groups are expected one by one in order given by linking information [subset26-1 ¶441]

## Cross-References
- [[balise-group]] — Balise group structure and configuration
- [[eurobalise]] — Individual balise component
- [[subset26-1]] — Source document
