# Balise Group

**Source:** [[subset40]] | **Date:** 2026-05-07 | **Type:** entity

A **balise group** is a set of one or more balises installed together to transmit a message to a passing train. The group is considered as a complete device limited by the reference location of the outer balises [¶42](http://localhost:8765/go.html#subset40-42).

## Reference Location

The reference location of a balise group is the reference location of the outer balise with **N_PIG = 0** [¶43](http://localhost:8765/go.html#subset40-43).

## Spacing Rules

- **Maximum distance within a group**: ≤12 m between reference marks of consecutive balises in the same group [¶61](http://localhost:8765/go.html#subset40-61).
- **Distance between groups**: Measured between the closest balises (Balise Reference Mark of the last balise of the first group to the first balise of the second group) [¶45](http://localhost:8765/go.html#subset40-45). Note: this differs from linking distance (between balises with N_PIG=0) [¶46](http://localhost:8765/go.html#subset40-46).

## "Last Switchable Balise"

The "last switchable balise" is the last encountered switchable balise in the crossing direction [¶44](http://localhost:8765/go.html#subset40-44).

## Group Configurations

Must respect SUBSET-091 §8.3.2.1 regarding number of balises per group, single groups, and TSR groups [¶82](http://localhost:8765/go.html#subset40-82).

## Installation Relative to Track Locations

In-fill location reference must be in rear of current EOA [¶84](http://localhost:8765/go.html#subset40-84). Installation relative to mission profile must respect SUBSET-091 chapter 10 (unlinked groups, max distances) [¶86](http://localhost:8765/go.html#subset40-86).

## Cross-references
- [[Balise]] — individual balise within a group
- [[Linking]] — linking distance differs from group distance
- [[In-fill]] — in-fill balise groups
- [[subset40]] — source document
