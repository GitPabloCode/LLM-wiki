# KER Compatibility

**Source:** [[subset40]] | **Date:** 2025-07-17 | **Type:** concept

KER (Kompatible Einrichtungen für das Rechnergestützte) compatibility refers to the ability of ERTMS/ETCS equipment to coexist and interoperate with legacy German KER train control systems. The rules in SUBSET-040 Appendix provide additional requirements for equipment offering KER compatibility — they are not required for pure ERTMS/ETCS interoperability. [subset40 ¶192][subset40 ¶193]

## Applicable Standards

Equipment offering KER compatibility must respect: [subset40 ¶194]

**SUBSET-100** (Interface 'G' Specification):
- Section 4: Physical Interaction and Environment
- Section 6: RAMs
- Annexes: Balise Type Specific Parameters

**SUBSET-101** (Interface 'K' Specification):
- Section 4.1.5: Balise group separation

## Antenna Interference

Interference between ERTMS/ETCS Eurobalise antennas and KER-based system antennas must be considered during installation. The antenna positioning rules (min 2m from train front, max 12.5m) partially address this, but project-specific constraints may apply. [subset40 ¶92][subset40 ¶38]

## Cross-References
- [[eurobalise-antenna]] — Antenna interference considerations with KER
- [[stm]] — Specific Transmission Module for other national systems
- [[subset40]] — Full engineering rule document
