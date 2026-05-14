# Train Position

**Source:** [[subset26]] | **Date:** 2025-07-17 | **Type:** concept

Train position in ERTMS/ETCS is defined relative to the Last Relevant Balise Group (LRBG). It includes an estimated distance from the LRBG, a confidence interval, and directional information relative to the LRBG orientation. [subset26 ¶599][subset26 ¶600][subset26 ¶601][subset26 ¶602]

## LRBG (Last Relevant Balise Group)

The LRBG is the balise group used as the reference for defining train position. [subset26 ¶599]

- **On-board selection**: Uses the last linked balise group, or last unlinked balise group (if no linking) as LRBG [subset26 ¶623][subset26 ¶624][subset26 ¶626]
- **RBC selection**: Uses the balise group reported by the on-board as LRBG [subset26 ¶628]
- **Unknown**: During Start of Mission or when position is unknown, LRBG identifier is set to "unknown" [subset26 ¶630]

## Train Position Components

- **Estimated front end position** — calculated from odometer distance travelled since last balise group [subset26 ¶722]
- **Max safe front end** = estimated front end + under-reading + LRBG location accuracy [subset26 ¶723]
- **Min safe front end** = estimated front end − over-reading + LRBG location accuracy [subset26 ¶725]
- **Confidence interval** — depends on odometer accuracy and LRBG location accuracy; increases with travelled distance [subset26 ¶699]

## Location Reference Rules

All location and profile data transmitted from the RBC must refer to the LRBG given in the same message. [subset26 ¶621]

When a new LRBG is established, location information is relocated by subtracting the distance between the old reference and the new LRBG (using linking information or estimated travelled distance). [subset26 ¶705][subset26 ¶706][subset26 ¶707]

## Cross-references
- [[linking]] — Balise group linking for coordinate system
- [[balise-group]] — Physical reference points
- [[movement-authority]] — Uses position information
- [[speed-and-distance-monitoring]] — Uses position for supervision
- [[rbc]] — Uses position reports for MA management
