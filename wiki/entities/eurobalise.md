# Eurobalise

**Source:** [[subset40]] | **Date:** 2025-07-17 | **Type:** entity

A Eurobalise is a trackside transponder device used in the ERTMS/ETCS signalling system to transmit telegrams to passing trains. It is the primary spot-transmission element for Levels 1 and 2. [subset40 ¶0]

## Reference Location

The reference location of a balise is its Balise Reference Marks — visible signs on the surface of the balise body. [subset40 ¶41]

## Installation Rules

**Spacing within a group:** Maximum 12m between consecutive balises within the same group (reference mark to reference mark). This ensures missing balises can be detected quickly. [subset40 ¶61]

**Signal positioning (Level 1):** For balises at signals containing switched information, any balise in rear of the operational stopping location shall be no further than 0.7m in rear of that stopping point. This prevents trains stopped at a red signal from unexpectedly receiving data from balises beyond the stopping point. [subset40 ¶63]

**EOA clearance:** The last balise of a group giving a Movement Authority or immediate level transition must be at least 1.3m in rear of the EOA/LOA. Exception: if the level transition has been announced and engineered to execute before the EoA/LoA is passed. [subset40 ¶65]

**Train detection clearance:** If a switchable balise's information is affected by transitions between train detection sections, the balise shall be at least 13.8m in rear of the detection device limit. This accounts for the side-lobe zone (1.3m) and the maximum antenna-to-first-axle distance (12.5m). [subset40 ¶67]

**Processing limit:** No more than 8 balises shall be encountered within the distance travelled in 0.8s at maximum line speed. This is driven by onboard processing limitations. [subset40 ¶69]

**Curve radius:** Minimum curve radius of 300m recommended where balises are placed. Lower values require detailed analysis of antenna lateral deviation per the Eurobalise FFFIS. [subset40 ¶74][subset40 ¶75]

## Telegram Configuration

- 0–300 km/h: Long or short telegram for both standard and reduced-size balises [subset40 ¶103]
- >300–500 km/h: Long or short telegram for standard balises; short telegram only for reduced-size balises [subset40 ¶103]

## Group Configuration

- Balise groups are considered as a complete device limited by the reference locations of the outer balises [subset40 ¶42]
- The reference location of a group is the reference location of the outer balise with N_PIG = 0 [subset40 ¶43]
- The "last switchable balise" is the last encountered switchable balise with regards to the group crossing direction [subset40 ¶44]
- Distance between groups is defined as the distance between the closest balises of the two groups (Reference marks). This differs from the linking distance which uses N_PIG=0 balises. [subset40 ¶45][subset40 ¶46]

## Cross-References
- [[eurobalise-antenna]] — The onboard antenna that communicates with the balise
- [[balise-group]] — Group configuration and referencing rules
- [[subset40]] — Full engineering rule document
- [[euroloop]] — Alternative transmission medium (loop-based)
