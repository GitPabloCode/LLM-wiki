# Chunk Summaries: subset40

## Chunk 1/1

- Document identity: **SUBSET-040** "ERTMS/ETCS - Class 1, Dimensioning and Engineering rules", Issue **2.3.0**, Date **7.4.2009** [¶0-¶7]. Developed and released by **UNISIG** [¶11, ¶91, ¶114]. Includes technical approval table for **ALSTOM, ANSALDO, BOMBARDIER, INVENSYS, SIEMENS, THALES** [¶8].

- **Modification history**: Versions from 0.0.1 (22-jun-99) to 2.3.0 (7/4/09) with section-by-section changes; final release updated to align with 2.3.0d plus CRs 302, 654, 690, 691, 692, 693 [¶10, ¶12].

### Introduction
- **References**: Documents referenced: SUBSET-108 v1.2.0, SUBSET-026 v2.3.0, SUBSET-091 v2.3.0, SUBSET-035 v2.1.1, SUBSET-036 v2.4.1, SUBSET-044 v2.3.0, SUBSET-054 v2.0.0, SUBSET-037 v2.3.0, SUBSET-100 v1.0.1, SUBSET-101 v1.0.0 [¶17-¶27].

- **Aim and purpose**: Engineering rules are system-related limitations for installation and information exchange characterising ERTMS subsystem implementation [¶30]. They provide additional constraints to the SRS and sub-documents to ensure interoperability; no divergent requirements [¶31]. Rules are complementary to SRS, FFFS, and FFFIS [¶32]. They do not define the whole set for a project; additional rules may be needed but must not preclude use of any equipment meeting these rules [¶33-¶34]. The rules are mandatory; engineering advice not in scope [¶35].

- **Transmission systems other than ERTMS/ETCS**: Constraints for **KER-compatible systems** described in appendix [¶37]. Additional constraints for other systems must be defined per project [¶38].

### Referencing balises and antennas
- **Balises**: Reference location is the **Balise Reference Marks** (visible signs on surface) [¶41]. Balise groups: considered as complete device limited by reference location of outer balises [¶42]; reference location of group is reference location of outer balise with **N_PIG = 0** [¶43]. "Last switchable balise" is last encountered switchable balise in crossing direction [¶44]. Distance between groups: distance between closest balises (Balise Reference Mark of last of first group to first of second group) [¶45]. Note: this differs from linking distance (between balises with N_PIG=0) [¶46].
- **Antennas**: Reference location is the **Antenna Reference Marks** (visible signs on surface) [¶48].

### Definitions
- **EOA**: location to which train is authorised to move (SUBSET-026 §3.8.1.1 a) [¶50].
- **Danger Point**: location beyond EOA reachable without risk if no overlap (SUBSET-026 §3.8.1.1 c) [¶51].
- **Overlap (end of)**: location beyond Danger Point reachable without risk for defined time (SUBSET-026 §3.8.1.1 d) [¶52].
- **Stopping point**: location in rear of EOA imposed by national operational constraints outside ERTMS/ETCS (e.g., France: 5m rear of signal) [¶53].
- **Telegram** transmitted by one balise; **Message** transmitted by balise group, loop, or radio (SUBSET-026 §8.3.2.3) [¶54].

### Installation rules (4.1)
#### Balises (4.1.1)
- **General installation**: Must respect SUBSET-036 §4.2.5 (cross-talk), §5.2 (air gap), §5.6.2 (installation requirements), §5.6.3 (distance between balises), §5.7 (environmental) [¶59].
- **Maximum distance within a group**: ≤12 m between reference marks of consecutive balises in same group [¶61].
- **Maximum distance from signal with switched info to stopping point (Level 1)**: Any balise in rear of operational stopping location shall not be further than **0.7m** in rear of that location [¶63]. (Justification uses 2m antenna-to-front distance and 1.3m side lobe zone.)
- **Minimum distance from balise group to EOA (Level 1)**: Last balise giving MA or immediate level transition order shall be ≥**1.3m** in rear of EOA/LOA. Exception: if level transition announced and executed before EoA/LoA passed [¶65].
- **Minimum distance from last switchable balise to limit of train detection section (Level 1)**: ≥**13.8m** in rear of detection device start [¶67]. (12.5m antenna-to-1st-axle + 1.3m side lobe). For jointless track circuits, overlapping area considered [¶67].
- **Number of balises processed per time unit**: Train runs distance **d** at max line speed during **0.8s**. Number of encountered balises in **d** shall **not exceed 8** [¶69]. Max speed = nominal line speed (SSP); tolerances not considered [¶69].
- **Lateral/angular tolerances**: Minimum curve radius recommended >**300m**; lower values require detailed analysis [¶74-¶75]. Properties of SUBSET-036 must be considered [¶76]. Reference: SUBSET-036 §5.2.2.5, §5.6.2.3 [¶77]. Very low radius curves not forbidden but no Eurobalise if transmission not guaranteed [¶80].
- **Balise group configurations**: Must respect SUBSET-091 §8.3.2.1 (number of balises per group, single groups, TSR groups) [¶82].
- **Installation relative to track locations**: In-fill location reference must be in rear of current EOA [¶84]. (SUBSET-026 §§3.4.3.1, 3.8.4.6.2-4, 4.8.1.5) [¶84].
- **Installation relative to mission profile**: Must respect SUBSET-091 ch.10 (unlinked groups, max distances) [¶86].

#### Eurobalise antenna (4.1.2)
- **General installation**: Must respect SUBSET-036 §§5.2, 6.5, 6.6, 6.7 [¶89].
- **Minimum/maximum distance from front of engine/1st axle to antenna**: Max **12.5m**, min **2m** to train front [¶92]. (Interference with other systems like KER considered [¶92].)

#### Euroloops (4.1.3)
- **General installation**: Must respect SUBSET-044 §§6.1.3, 6.10, 6.11, 6.13, 7.8 [¶96].

#### Miscellaneous (4.1.4)
- **Level transition borders and RBC/RBC handover borders**: Shall not be located where shunting or reversing could take place [¶99]. (SUBSET-026 §§3.15.4.6, 4.4.8.1.5) [¶99]. Not handled in Shunting/Reversing modes [¶99].

### Telegrams and messages (4.2)
#### Balise telegrams (4.2.1)
- **Length**: 0–300 km/h: long or short telegram for standard and reduced size balises; >300–500 km/h: long or short for standard size, only short for reduced size [¶103]. Speed = nominal line speed (SSP); tolerances not considered [¶103].

#### Radio messages (4.2.2)
- **Definition**: RBC messages or radio in-fill messages (same protocol) [¶105].
- **Max length**: Application data (excluding Euroradio protocol) as normal priority ≤ **500 bytes** [¶107]. High priority data: fixed size only [¶107].

#### Data engineering rules (4.2.4)
- **Sharing of identifiers**: Must respect SUBSET-026 §3.18.4.4.1 [¶110].
- **In-fill information**: Limited to in-fill MA, linking, route-related track description. Permitted packets: 136, 12, 80, 49, 21, 27, 51, 65/66, 70, 5, 41, 44, 39, 67, 68, 71, 133 [¶113]. For immediate level transition in in-fill, **D_LEVELTR = 0m** [¶116].
- **Mode profile**: Overlapping of mode profile areas forbidden [¶119]. If Level 1 MA has **V_MAIN=0**, no mode profile packet allowed [¶120].
- **Track conditions**:
  - Powerless section with pantograph lowering: min announcement distance = **17s** at line speed [¶124].
  - Powerless section without pantograph lowering: min announcement distance = **11s** at line speed [¶124].
  - Other conditions (non-stopping area, air tightness, brake switches): min announcement distance = **10s** at line speed [¶126].
- **Linking data handling**: Unlinked balise groups shall **never** be announced via linking [¶130]. Unlinked groups shall **never** transmit linking unless as in-fill [¶131].
- **Level transition announcement**: Trackside shall announce all applicable **NID_STM** values for national systems installed [¶135].
- **Text transmission**: End condition 'location' allowed only if start condition 'location' used [¶137].
- **Packet 131 (RBC Transition Order)**: Forbidden to use special value 'Contact the last known RBC' for **NID_RBC** [¶139]. All engineering requirements for Level transition involving STM from SUBSET-035 §7.5 must be respected [¶140].
- **NID_RADIO**: Refer to Subset 054 [¶142].

### Dimensioning rules for messages (4.3)
- **Constraints**: If engineering rules limit iterations, they take precedence over **31** (max N_ITER in SRS ch.7) [¶146].
- **Data dimensioning (max iterations in 1 packet / min memorised on board)**:
  - MA sections (excl. End Section): **5 / 6** [¶151].
  - Balise IDs for SR/shunting: **15** (max) / no memorisation [¶153].
  - Mode profile sections: **2 / not applicable** [¶155].
  - SSP change locations: **31 / 50** [¶157].
  - TSR: **10 packets / 30** [¶159].
  - Gradient changes: **31 / 50** [¶161].
  - Position report locations: **15** (new packet 58 replaces old) [¶163].
  - Text messages: **1 plain + 1 fixed / 5 plain + 5 fixed** [¶165].
  - Linked balise groups: **29 / 30** (exception for in-fill) [¶167].
  - TC change of traction power: **no iteration / 1** [¶169].
  - TC big metal masses: **4 / 5** [¶171].
  - TC: **19 / 20** [¶173].
  - Route suitability data: **2 / 3** (max one per type) [¶175].
  - Train categories per SSP segment: **15** (max) [¶177].
  - Axle load speed profile segments: **14 / 30** [¶179].
  - Axle load speed restriction values per segment: **3** [¶181].
  - Adhesion profiles: **no iteration / 10** [¶183].
  - Reversing area: **no iteration / 1** [¶185].
- **Multiple instances of packets**: Must respect SUBSET-026 §8.4.1.4 [¶188].
- **Data flows – position reports**: Trackside shall not require position reports at cycle < **5 sec** [¶191].

### Appendix: Rules for KER compatibility (5)
- **Additional requirements** for equipment offering KER compatibility (not required for ERTMS/ETCS interoperability) [¶193]. Must respect SUBSET-100 §§4, 6 and Annexes; SUBSET-101 §4.1.5 [¶194]. Subsections 5.1.1.2 and 5.1.1.3 intentionally deleted [¶195].