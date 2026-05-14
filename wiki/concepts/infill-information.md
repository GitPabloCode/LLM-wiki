# Infill Information

**Source:** [[subset26]] | **Date:** 2025-07-17 | **Type:** concept

Infill Information is additional signalling information transmitted ahead of the next main signal in Level 1, allowing the train to receive updated information before reaching the signal. [subset26 ¶222][subset26 ¶224]

## Transmission Means

Infill can be transmitted by three media [subset26 ¶1093]:
1. **Balise groups** — additional balises between signals
2. **Euroloops** — continuous loop transmission
3. **Radio Infill Units (RIU)** — radio-based infill

All three follow the same principle, independent of the medium. [subset26 ¶1098]

## Infill MA (Level 1 only)

Infill MA is evaluated only in FS or LS mode and requires linking information for the main signal balise group. Section timers start at balise passing, loop message reception, or radio message timestamp. [subset26 ¶1017][subset26 ¶1018][subset26 ¶1020][subset26 ¶1021][subset26 ¶1022][subset26 ¶1023][subset26 ¶1024]

## Location Referencing

Infill data refers to the balise group at the next main signal and its orientation. [subset26 ¶639][subset26 ¶640]

## Cross-references
- [[euroloop]] — One transmission medium for infill
- [[radio-infill-unit]] — Radio-based infill
- [[eolm]] — Marks loop start/end
- [[movement-authority]] — Infill provides advance MA information
- [[ertms-etcs-application-levels]] — Level 1 uses infill
