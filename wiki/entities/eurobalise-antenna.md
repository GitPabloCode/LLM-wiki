# Eurobalise Antenna

**Source:** [[subset40]] | **Date:** 2025-07-17 | **Type:** entity

The Eurobalise Antenna is the onboard device mounted beneath the train that communicates with trackside Eurobalises. It energises passive balises and receives telegrams. [subset40 ¶48]

## Reference Location

The reference location of an antenna is its Antenna Reference Marks — visible signs on the surface of the antenna body. [subset40 ¶48]

## Positioning Rules

**Distance from train front and first axle:** [subset40 ¶90][subset40 ¶92]

| Parameter | Value |
|---|---|
| Minimum distance from train front | 2m |
| Maximum distance from train front | 12.5m |

The minimum 2m distance prevents an antenna from receiving a telegram from a balise energised by another antenna, and prevents a balise energised by one antenna from perturbing an adjacent antenna's transmission. [subset40 ¶92]

The maximum 12.5m allows the same antenna to be used for both directions on a locomotive and provides sufficient space for installation on all train types. [subset40 ¶92]

**Interference with other systems:** Interference with antennas of other systems (especially KER-based) must be considered. [subset40 ¶92]

## Installation Requirements

Installation must follow the FFFIS for Eurobalise (SUBSET-036) specifications for: [subset40 ¶89]
- Balise air gap interface (Section 5.2)
- Antenna installation requirements (Section 6.5)
- Specific environmental conditions (Section 6.6)
- Specific EMC requirements (Section 6.7)

## Lateral Deviation in Curves

Differences in antenna mounting on different train types generate varying lateral deviations in curves, in addition to dynamic deviations. The effects depend on train speed, distance between bogies, and antenna location. In curves with radius < 300m, detailed analysis is needed to ensure reliable transmission. [subset40 ¶78][subset40 ¶79]

## Cross-References
- [[eurobalise]] — The trackside balise the antenna communicates with
- [[balise-installation-rules]] — Installation rules for the trackside balise
- [[ker-compatibility]] — KER interference considerations
- [[subset40]] — Full engineering rule document
