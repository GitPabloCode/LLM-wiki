# SUBSET-040: ERTMS/ETCS — Class 1, Dimensioning and Engineering Rules

**Source:** [[subset40]] | **Date:** 2026-05-07 | **Type:** summary

SUBSET-040 (Issue 2.3.0, 7 April 2009) defines **dimensioning and engineering rules** for ERTMS/ETCS Class 1 implementations. Developed by UNISIG (ALSTOM, ANSALDO, BOMBARDIER, INVENSYS, SIEMENS, THALES) [¶0-¶11], these rules supplement the System Requirements Specification (SRS) and related sub-documents to guarantee interoperability.

The document covers:

- **Installation rules** for balises, antennas, and Euroloops — distances, tolerances, and positioning constraints [¶59-¶99].
- **Telegram and message rules** — balise telegram lengths by speed, radio message size limits, and data engineering constraints [¶101-¶142].
- **Dimensioning rules** — maximum iterations per packet and minimum values stored onboard for MA sections, mode profiles, gradients, TSRs, linking data, track conditions, and more [¶146-¶191].
- **KER compatibility** — additional constraints for equipment supporting KER-compatible transmission [¶193-¶195].

These rules are **mandatory** for interoperability and complementary to SUBSET-026 (SRS), SUBSET-036 (FFFS), and SUBSET-091 (FFFIS) [¶30-¶35].

## Cross-references
- [[Balise]] — primary trackside device governed by these installation rules
- [[Balise Group]] — structure and spacing rules defined in §4.1.1
- [[Eurobalise Antenna]] — on-board antenna installation constraints
- [[Euroloop]] — loop transmission system installation rules
- [[RBC]] — radio block centre referenced in handover rules
- [[EOA]] — End of Authority, a key reference location throughout the rules
- [[Balise Installation Rules]] — detailed installation constraints from §4.1.1
- [[Data Dimensioning]] — iteration and memorisation limits from §4.3
- [[In-fill]] — supplementary information transmission rules
- [[Level Transition]] — rules for transitions between ETCS levels
- [[Track Conditions]] — announcement distances for special track conditions
- [[KER Compatibility]] — alternative transmission system constraints
- [[Linking]] — rules for linked vs unlinked balise groups
