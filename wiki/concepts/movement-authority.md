# Movement Authority (MA)

**Source:** [[subset26]] | **Date:** 2025-07-17 | **Type:** concept

A Movement Authority (MA) is permission for a train to move to a specific location. It is generated trackside and transmitted via balises (Level 1) or Euroradio (Levels 2/3). [subset26 ¶114][subset26 ¶216][subset26 ¶250]

## Structure

An MA consists of [subset26 ¶900][subset26 ¶901][subset26 ¶902]:

- **End of Movement Authority (EOA)** / **Limit of Authority (LOA)** — the target location
- **Danger Point (DP)** — a point beyond the EOA that the train must not pass
- **Overlap** — a safety zone beyond the danger point
- **Release Speed** — speed at which the EOA may be approached
- **Sections** — the MA is divided into sections, each with optional section time-out

## MA Characteristics

- Each section can have a **section time-out**; the last section can have an **end section time-out** [subset26 ¶905][subset26 ¶906][subset26 ¶907]
- **Supervised Location (SvL)** — end of overlap (if any and before time-out), else Danger Point, else End of Authority [subset26 ¶1011]
- **LOA** — a supervised target speed at a location [subset26 ¶908]

## MA Updates

- **Infill MA (Level 1)**: Additional information before reaching a signal, evaluated only in FS/LS mode [subset26 ¶1017]
- **MA Update**: A new MA from the main signal or RBC replaces the previous one [subset26 ¶1026]
- **Co-operative Shortening (Level 2/3)**: RBC proposes shortened MA; on-board checks position and accepts/rejects [subset26 ¶1084]

## Completeness

The MA must be accompanied by Static Speed Profile (SSP) and gradient data covering the full length; otherwise it is rejected. [subset26 ¶855]

## Time-out Values

- **Section timer** — starts at time stamp of message (L2) or passage of first balise (L1) [subset26 ¶981]
- **End section timer** — starts when max safe front end passes start location [subset26 ¶970]
- **LOA speed timer** — validity of LOA target speed [subset26 ¶904]
- **Overlap timer** — starts when max safe front end passes start location [subset26 ¶998]

## Cross-references
- [[rbc]] — Generates MA in Levels 2/3
- [[euroradio]] — Transmits MA in Levels 2/3
- [[ertms-etcs-application-levels]] — How MA is transmitted per level
- [[linking]] — Position reference for MA
- [[speed-and-distance-monitoring]] — How MA targets are supervised
- [[infill-information]] — Advance MA information in Level 1
