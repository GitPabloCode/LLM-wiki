# Balise Installation Rules

**Source:** [[subset40]] | **Date:** 2025-07-17 | **Type:** concept

This page captures the engineering rules for physical installation of Eurobalises on the trackside, as defined in SUBSET-040 Section 4.1.1. [subset40 ¶57]

## Reference Point Conventions

Balises are referenced by their Balise Reference Marks — visible signs on the balise surface. [subset40 ¶41]

## Distance Rules

| Rule | Value | Purpose |
|---|---|---|
| Max distance between balises in a group | 12m | Early detection of missing balises [subset40 ¶61] |
| Balise at signal to stopping point (Level 1) | ≤0.7m in rear | Prevent stopped train from reading forward balises [subset40 ¶63] |
| Last MA-giving balise to EOA/LOA (Level 1) | ≥1.3m in rear | Ensure all MA info received before EOA passed [subset40 ¶65] |
| Last switchable balise to train detection limit (Level 1) | ≥13.8m in rear | Avoid reading balise of block n while detected in block n+1 [subset40 ¶67] |
| Minimum curve radius for balise placement | 300m recommended | Ensure reliable antenna-to-balise transmission [subset40 ¶74] |

## Processing Capacity

No more than 8 balises may be encountered within the distance 'd' travelled at max line speed in 0.8 seconds. This accounts for onboard processing limitations per SUBSET-036 Section 4.2.9. [subset40 ¶69]

## In-fill Location

The in-fill device's location reference must be in rear of the current EOA, because MA extension via in-fill is only possible when there is no gap between the old MA and the MA extension. [subset40 ¶84]

## Lateral and Angular Tolerances

Installation must respect SUBSET-036 Sections 5.2.2.5 and 5.6.2.3 for lateral and angular tolerances. The minimum recommended curve radius is 300m; lower values require detailed analysis of antenna lateral deviation. [subset40 ¶74][subset40 ¶77]

## Cross-References
- [[eurobalise]] — The physical balise device
- [[eurobalise-antenna]] — Onboard antenna considerations
- [[balise-group]] — Group configuration rules
- [[subset40]] — Full engineering rule document
