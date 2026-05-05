# Balise Installation

**Source:** [subset40](../summaries/subset40.md) | **Date:** 2026-04-29 | **Type:** concept

**Balise installation** rules govern the physical placement of Eurobalises and Eurobalise antennas on the track and on-board rolling stock. These constraints ensure that every train antenna can reliably read every compliant balise, that trains stopped at signals do not inadvertently read the next block's information, and that balise groups are fully processed before the train reaches the authority limit. The rules apply principally to Level 1 installations where balises are the primary transmission medium. [¶57-93](http://localhost:8765/go.html#subset40-57)

## Balise spacing within a group

The maximum distance between two consecutive balises within the same group is **12m** (reference mark to reference mark). This balances two opposing needs: the distance must be short enough for the on-board to quickly determine that a missing balise is truly absent (reaching the 12m limit without detecting the next balise confirms it's gone), but long enough to respect the minimum cross-talk protection distances defined in the Eurobalise FFFIS (SUBSET-036). [¶60-61](http://localhost:8765/go.html#subset40-60)

## Balises at signals (Level 1)

At a signal showing stop, a train halts at the **operational stopping point** — a defined location in rear of the signal. Any balise containing switched information and located in rear of this stopping point must be **no more than 0.7m** behind it. This ensures a stopped train cannot receive information from the balise group belonging to the next block. [¶62-63](http://localhost:8765/go.html#subset40-62)

The calculation assumes the antenna is mounted closest to the front of the engine, with its reference mark 2m behind the front, and accounts for the 1.3m side-lobe zone of the balise signal.

## Balise group before EOA/LOA (Level 1)

The last encountered balise of a group that grants a Movement Authority (MA) or issues an immediate level transition order, placed near the End of Authority (EOA) or Limit of Authority (LOA), must be at least **1.3m in rear** of the EOA/LOA. Once the train's minimum safe antenna position passes the EOA/LOA, no further information can be received — and the 1.3m gap guarantees the antenna has fully passed the balise by that point (per SUBSET-036 side-lobe specification). [¶64-65](http://localhost:8765/go.html#subset40-64)

Exception: if the level transition has been pre-announced and the transition distance engineered so the transition executes before the EOA/LOA is passed, this rule does not apply.

## Switchable balises and train detection (Level 1)

When the transition between two train detection sections changes the information transmitted by a switchable balise, that balise must be at least **13.8m in rear** of where the next section's detection device may first detect the train. This is derived from the worst-case axle-to-antenna distance (12.5m) plus the side-lobe zone (1.3m), preventing a train's antenna from still reading block N's balise group after the train has already been detected in block N+1. [¶66-67](http://localhost:8765/go.html#subset40-66)

## Balise processing rate

In the distance `d` = **(max line speed) × 0.8s**, no more than **8 balises** may be encountered. This constraint derives from on-board telegram processing capacity, ensuring the EVC can handle the data stream at maximum speed. The line speed used is the nominal engineered SSP value — measurement inaccuracy and brake-intervention margins are excluded. [¶68-69](http://localhost:8765/go.html#subset40-68)

## Curve radius constraint

The recommended minimum curve radius for Eurobalise placement is **300m**. Tighter curves require detailed analysis of the lateral deviation between the antenna and the balise (which varies with speed, bogie spacing, antenna location, and dynamic effects). A curve tighter than 300m does not forbid balises altogether, but transmission cannot be guaranteed — so if analysis shows the risk is too high, no Eurobalise should be placed there. [¶70-80](http://localhost:8765/go.html#subset40-70)

## Antenna mounting

The Eurobalise antenna on the train must be mounted [¶90-92](http://localhost:8765/go.html#subset40-90):
- **Minimum 2m** from the front of the engine to the antenna reference mark — prevents one antenna from receiving a telegram from a balise energised by another antenna, and prevents cross-perturbation between adjacent antennas.
- **Maximum 12.5m** from the front of the engine to the 1st axle — provides sufficient installation space for all train types and allows a single antenna to serve both directions on a locomotive.

## Cross-references
- [ERTMS Engineering Rules](ertms-engineering-rules.md) — the broader concept these installation rules belong to
- [ERTMS Dimensioning](ertms-dimensioning.md) — the data dimensioning counterpart for telegram content
- [FFFIS](fffis.md) — the FFFIS concept for interchangeable equipment interfaces
- [subset40](../summaries/subset40.md) — the Dimensioning and Engineering Rules specification
