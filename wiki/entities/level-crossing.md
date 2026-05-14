# Level Crossing (LX)

**Source:** [[subset26]] | **Date:** 2025-07-17 | **Type:** entity

A Level Crossing (LX) is a physical crossing between road and track where ERTMS/ETCS provides supervision. [subset26 ¶1488]

## LX Information

Trackside provides [subset26 ¶1489][subset26 ¶1497]:
- **Identity** (NID_LX) — unique identifier
- **Protection status** — protected or not protected
- **Allowed speed** — if not protected
- **Optional stopping area** — where train must stop if required

## Non-Protected LX Procedure

In FS, LS, or OS mode, the on-board temporarily supervises the LX start location as both the EOA and SvL. If stopping is required, the train must stop inside the stopping area before the LX speed restriction is included in the MRSP. [subset26 ¶4354][subset26 ¶4356]

## Cross-references
- [[speed-and-distance-monitoring]] — LX speed restriction in MRSP
- [[ertms-etcs-application-levels]] — LX supervision in all levels
