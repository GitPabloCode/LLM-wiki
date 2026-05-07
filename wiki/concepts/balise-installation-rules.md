# Balise Installation Rules

**Source:** [[subset40]] | **Date:** 2026-05-07 | **Type:** concept

This page collects all the installation constraints for balises from SUBSET-040 §4.1.1.

## General Installation

Must respect SUBSET-036 §4.2.5 (cross-talk), §5.2 (air gap), §5.6.2 (installation requirements), §5.6.3 (distance between balises), and §5.7 (environmental) [¶59](http://localhost:8765/go.html#subset40-59).

## Distances

| Rule | Value | Reference |
|---|---|---|
| Max distance within a group | ≤ **12 m** between reference marks | [¶61](http://localhost:8765/go.html#subset40-61) |
| Max distance from signal with switched info to stopping point (Level 1) | ≤ **0.7 m** in rear | [¶63](http://localhost:8765/go.html#subset40-63) |
| Min distance from balise group to EOA (Level 1) | ≥ **1.3 m** in rear | [¶65](http://localhost:8765/go.html#subset40-65) |
| Min distance from last switchable balise to limit of train detection section (Level 1) | ≥ **13.8 m** in rear | [¶67](http://localhost:8765/go.html#subset40-67) |

## Processing Limit

Number of balises encountered in the distance **d** travelled at max line speed during **0.8 s** shall not exceed **8** [¶69](http://localhost:8765/go.html#subset40-69).

## Lateral/Angular Tolerances

Minimum curve radius recommended >**300 m**; lower values require detailed analysis [¶74-¶75]. Very low radius curves require verification that transmission is guaranteed [¶80](http://localhost:8765/go.html#subset40-80).

## Group Configurations

Must respect SUBSET-091 §8.3.2.1 (number of balises per group, single groups, TSR groups) [¶82](http://localhost:8765/go.html#subset40-82).

## Cross-references
- [[Balise]] — the device being installed
- [[Balise Group]] — grouping rules
- [[Eurobalise Antenna]] — antenna dimensions used in distance calculations
- [[EOA]] — reference location for distance rules
- [[subset40]] — source document
