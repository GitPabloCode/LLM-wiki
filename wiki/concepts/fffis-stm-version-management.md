# FFFIS STM Version Management

**Source:** [[subset35]] | **Date:** 2025-07-17 | **Type:** concept

Version management ensures compatibility between ERTMS/ETCS on-board equipment and STMs implementing different versions of the FFFIS STM specification.

## Version Number Format

Versions follow the format **X.Y** where X and Y are between 0 and 255 (e.g., 2.0, 3.0, 4.2) [subset35 ¶783]:
- **X** — distinguishes incompatible versions. Same X = compatible versions regardless of Y [subset35 ¶784]-[§786]
- **Y** — indicates compatibility within version X

## Version History

| Version | Support | Remark |
|---------|---------|--------|
| X=2, Y=0 | Supplier specific | Initial version from SUBSET-035 v2.0.0 |
| X=3, Y=0 | Supplier specific | General revision from SUBSET-035 v2.1.1 |
| X=4, Y=0 | **Yes** (all) | Legal backward compatibility envelope, introduced in SUBSET-035 v3.x.0 (ETCS Baseline 3) |

[subset35 ¶790]

## Requirements

- STMs must support and send the highest version number within the legal backward compatibility envelope [subset35 ¶791]
- ERTMS/ETCS on-board must support all version numbers X in the envelope [subset35 ¶792]
- All on-board nodes/functions must support the same version numbers [subset35 ¶793]
- When connecting with a lower X version, the on-board applies the corresponding set of requirements per section 16.4 [subset35 ¶794]
- Versions evolve sequentially (no branching) [subset35 ¶781]
- Version numbers increment only when functionality changes [subset35 ¶787]

## Legal Backward Compatibility Envelope

X=4 is the starting point of the envelope. Support for X lower than 4 by ERTMS/ETCS on-board is supplier-specific [subset35 ¶796].

## Cross-references
- [[connection-management]] — How version check is performed during connection
- [[stm]] — The Specific Transmission Module
- [[stm-control-function]] — Manages version compatibility
