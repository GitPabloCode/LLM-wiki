# Linking

**Source:** [[subset26]] | **Date:** 2025-07-17 | **Type:** concept

Linking is the process that determines if a balise group has been missed, assigns a coordinate system to single balise groups, and corrects odometer confidence interval. [subset26 ¶398][subset26 ¶399][subset26 ¶400][subset26 ¶401]

## Linking Information

Linking information includes [subset26 ¶405][subset26 ¶406][subset26 ¶407][subset26 ¶408][subset26 ¶410][subset26 ¶411]:

- Identity of the linked balise group
- Location accuracy
- Direction of passage
- Required reaction if a data inconsistency occurs

## Expectation Window

The expectation window is the interval between the first possible location and the last possible location of a balise group within which the balise group is accepted. [subset26 ¶438][subset26 ¶439]

## Key Rules

- A balise group shall consist of between one and eight balises [subset26 ¶344]
- Every balise group has its own coordinate system; the origin is given by balise number 1 [subset26 ¶351][subset26 ¶354]
- Linking information is used to determine if a balise group has been missed, assign a coordinate system to single balise groups, and correct odometer inaccuracy [subset26 ¶398]
- **Unlinked balise groups** shall consist of at minimum two balises and shall never be used as LRBG [subset26 ¶424][subset26 ¶608]
- For linked balise groups, if the expected group is found outside its expectation window, the on-board rejects the message and reacts per the linking reaction [subset26 ¶2524]

## Linking Consistency

If two consecutive linked balise groups announced by linking are not detected, the on-board commands service brake. [subset26 ¶2584]

## Cross-references
- [[balise-group]] — The physical entity being linked
- [[movement-authority]] — Uses linking for position reference
- [[train-position]] — Position relative to LRBG uses linking
- [[ertms-etcs-application-levels]] — Linking used in all levels
