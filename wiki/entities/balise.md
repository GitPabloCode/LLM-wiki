# Balise

**Source:** [[subset40]] | **Date:** 2026-05-07 | **Type:** entity

A **balise** is a trackside transmission device used in the ERTMS/ETCS signalling system. Balises transmit telegrams to passing trains via the Eurobalise antenna.

## Reference Location

The reference location of a balise is the **Balise Reference Mark** — a visible sign on the track surface [¶41](http://localhost:8765/go.html#subset40-41).

## Installation Rules (SUBSET-040 §4.1.1)

- Must respect SUBSET-036 cross-talk, air gap, installation, and environmental requirements [¶59](http://localhost:8765/go.html#subset40-59).
- **Maximum distance within a group**: ≤12 m between reference marks of consecutive balises in the same group [¶61](http://localhost:8765/go.html#subset40-61).
- **Maximum distance from signal with switched info to stopping point (Level 1)**: Any balise in rear of operational stopping location shall not be further than **0.7 m** in rear of that location [¶63](http://localhost:8765/go.html#subset40-63).
- **Minimum distance from balise group to EOA (Level 1)**: Last balise giving MA or immediate level transition order shall be ≥**1.3 m** in rear of EOA/LOA [¶65](http://localhost:8765/go.html#subset40-65).
- **Minimum distance from last switchable balise to limit of train detection section (Level 1)**: ≥**13.8 m** in rear of detection device start [¶67](http://localhost:8765/go.html#subset40-67).
- **Lateral/angular tolerances**: Minimum curve radius recommended >**300 m**; lower values require detailed analysis [¶74-¶80].
- **Balise group configurations**: Must respect SUBSET-091 §8.3.2.1 [¶82](http://localhost:8765/go.html#subset40-82).

## Telegram Rules (§4.2.1)

- 0–300 km/h: long or short telegram for standard and reduced size balises [¶103](http://localhost:8765/go.html#subset40-103).
- >300–500 km/h: long or short for standard size, only short for reduced size [¶103](http://localhost:8765/go.html#subset40-103).

## Processing Limit

Number of balises processed per 0.8 s time unit shall not exceed **8** at max line speed [¶69](http://localhost:8765/go.html#subset40-69).

## Cross-references
- [[Balise Group]] — structure and spacing rules for grouped balises
- [[Eurobalise Antenna]] — onboard device that reads balise telegrams
- [[Balise Installation Rules]] — detailed set of constraints
- [[Telegram Rules]] — speed-dependent telegram length rules
- [[Linking]] — rules for linked vs unlinked balise groups
- [[In-fill]] — balises used for in-fill information
- [[subset40]] — source document
