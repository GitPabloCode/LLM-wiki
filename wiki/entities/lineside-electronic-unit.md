# Lineside Electronic Unit (LEU)

**Source:** [[subset26]] | **Date:** 2025-07-17 | **Type:** entity

The Lineside Electronic Unit (LEU) is an electronic trackside device that generates telegrams to be sent by balises based on information from external trackside systems. [subset26 ¶108]

## Function

The LEU receives signalling information from interlocking or other trackside systems and converts it into balise telegrams. When the LEU or its underlying system fails, it transmits **default balise information** — a telegram indicating the failure, of which the driver is informed. [subset26 ¶2558][subset26 ¶2561]

## Relationship with Balises

The LEU is the intermediary between trackside signalling logic and Eurobalises. It powers and controls switchable balises (balises whose content can change based on signal states), as opposed to fixed-data balises which have pre-programmed telegrams.

## Cross-references
- [[eurobalise]] — The transmission device the LEU drives
- [[rbc]] — Another trackside entity with complementary function
- [[ertms-etcs-application-levels]] — Used in Level 1 for switched balise information
