# SUBSET-026-2 — ERTMS/ETCS System Requirements Specification (Chapters 4.6–7)

**Source:** [[subset26-2]] | **Date:** 2026-05-12 | **Type:** summary

This is part 2 of the core ERTMS/ETCS System Requirements Specification (SRS), Baseline 3 2nd Release (v3.6.0, 13/05/2016). This document covers Chapters 4.6 through 7 of the SRS.

## Chapter 4.6: Mode Transitions

### 4.6.2 Transitions Table
A matrix defining permitted transitions between all 17 ETCS modes (NP, SB, PS, SH, FS, LS, SR, OS, SL, NL, UN, TR, PT, SF, IS, SN, RV). Each cell identifies the condition(s) that trigger a specific mode transition. [subset26-2 ¶3550-¶3552]

### 4.6.3 Transitions Conditions Table
Detailed definitions of conditions [1] through [74] that trigger mode transitions. Conditions cover driver actions (isolating equipment, selecting modes, acknowledging requests), train state (standstill, speed thresholds, position relative to EOA/LOA), trackside inputs (mode profiles, balise telegrams, emergency stops), level transitions, equipment faults, and time-outs. [subset26-2 ¶3554-¶3568]

## Chapter 4.7: DMI Depending on Modes

Specifies which DMI inputs and outputs are active/available/NA in each mode. The DMI is the interface for direct information exchange between driver and ERTMS/ETCS onboard. [subset26-2 ¶3569-¶3588]

- **X** = Active: displayed/enterable in the mode
- **A** = Available: becomes active only if additional conditions fulfilled
- Grey cells: defined by national system
- **NA** = Not applicable (SF, IS modes)

Tables cover: Train Data, language selection, driver id, train running number, level, adhesion, RBC contact, radio network, train integrity, start, override/shunting requests, acknowledgement types, speed/distance supervision outputs, track conditions, brake indication, geographical position, etc. [subset26-2 ¶3576-¶3588]

## Chapter 4.8: Acceptance of Received Information

Defines how received information is filtered based on (1) level and transmission medium, (2) mode, using a three-filter model (Figure 3). [subset26-2 ¶3589-¶3676]

**Level & Transmission Media Filter (4.8.3)**: For each information type (National Values, Linking, MA, Gradient, SSP, TSR, Emergency Stops, Session Management, etc.), defines whether it is Accepted or Rejected depending on:
- Whether from RBC or not (balise/loop/RIU) [subset26-2 ¶3612-¶3620]
- Operating level (0, NTC, 1, 2, 3) [subset26-2 ¶3615-¶3620]
- Exceptions for level transition announcements, buffer storage rules [subset26-2 ¶3621-¶3632]
- Information from National System via STM interface [subset26-2 ¶3633-¶3636]

**Mode Filter (4.8.4)**: For each information type, defines acceptance/rejection in each of the 17 modes. Includes exceptions for PT mode (L2/3 only after Recognition of Exit from TR), SB mode (only if cab active/valid Train Data), PS/SH modes, etc. [subset26-2 ¶3640-¶3658]

**Transition Buffer (4.8.5)**: Stores up to 3 sets of information during announced level transitions or RBC/RBC handovers. Released and re-evaluated sequentially when transition is performed. [subset26-2 ¶3660-¶3676]

## Chapter 4.9: Stored Information on Level Entry

When entering a given level, certain stored data is affected. Entering Level 1 deletes MA Request Parameters, Position Report Parameters, and Track Ahead Free Request. Entering Level 0/NTC/1 deletes 'Inhibition of revocable TSRs from balises in L2/3'. Other data unchanged. [subset26-2 ¶3677-¶3683]

## Chapter 4.10: Stored Information on Mode Entry

Comprehensive table showing what happens to each type of stored data when entering each mode: Deleted (D), To Be Revalidated (TBR), Unchanged (U), Reset (R), or Not Relevant (NR). Covers National Values, Linking, MA, Gradient, SSP, TSR, Mode Profiles, Train Data, Level, RBC ID, Driver ID, Train Position, Track Conditions, Emergency Stops, etc. [subset26-2 ¶3684-¶3729]

## Chapter 4.11: Stored Information on Exiting NP Mode

When exiting No Power mode, status of stored information (EOLM, Train Position, ERTMS/ETCS Level, trackside supported levels, RBC ID/Phone Number) depends on whether a cold movement was detected. If no cold movement occurred, invalid data becomes valid. If cold movement detected or unknown, invalid data stays invalid until validated by other means. [subset26-2 ¶3730-¶3734]

## Chapter 5: Procedures

### 5.4 Start of Mission
Detailed procedure from SB mode to starting a mission. Covers data entry (Driver ID, Level, Train Data, Train Running Number, Radio Network, RBC ID), session establishment, position validation by RBC, and transition to operational modes (FS, SR, OS, LS, SH, UN, SN, NL). [subset26-2 ¶3775-¶3841]

### 5.5 End of Mission
Procedure triggered when entering SB or SH from operational modes. Involves possible data deletion, reporting end to RBC (with position report), and session termination. [subset26-2 ¶3842-¶3871]

### 5.6 Shunting Initiated by Driver
Procedure for driver-selected Shunting mode. For L2/3: sends request to RBC, awaits authorisation. For L0/1: immediate transition. Includes degraded situation handling for no RBC response. [subset26-2 ¶3872-¶3893]

### 5.7 Entry in Shunting with Order from Trackside
Entry to SH mode via mode profile from balise group (L1) or RBC (L2/3). Can be for current location or further location. Driver acknowledgement required with time-out. [subset26-2 ¶3894-¶3925]

### 5.8 Override Procedure
Allows train to pass End of Movement Authority in degraded situations. From FS/LS/OS/SR/SB/PT: switches to SR mode. From SH: remains SH. From UN/SN: only changes to SR when level changes to L1/2/3. Override active until time/distance limits, passing stop information, receiving MA, or other termination conditions. [subset26-2 ¶3926-¶3988]

### 5.9 On Sight Procedure
Entry to OS mode via mode profile. For current or further location. Driver acknowledgement required with defined rectangle of acknowledgement. Exit from OS when min safe front end passes end of OS area. Track Ahead Free mechanism for RBC to extend MA beyond OS area. [subset26-2 ¶3989-¶4041]

### 5.10 Level Transitions
Comprehensive rules for all level transitions (L0↔L1, L0↔L2/3, L1↔L2/3, L0↔NTC, L1↔NTC, L2/3↔NTC, NTC↔NTC). Each transition has specific requirements for MA/track description availability, RBC connection orders, position reporting, session management. Conditional level transitions allow checking if train operates in a permitted level. Driver-initiated level transitions also possible at standstill. Acknowledgement requirements defined per transition direction. [subset26-2 ¶4043-¶4185]

### 5.11 Train Trip Procedure
Triggered when events cause a train trip. On-board switches to TR mode, deletes MA/track description, reports to RBC (L2/3), awaits standstill. Driver acknowledges trip, leading to PT mode (L1/2/3), SH (L0/NTC without valid Train Data), UN (L0 with Train Data), or SN (NTC with Train Data). From PT, driver can select Start (requesting new MA) or SH. [subset26-2 ¶4186-¶4204]

### 5.12 Change of Train Orientation
Procedures for changing driving cab: same engine (mission ongoing or shunting ongoing) or different engine (leading becomes slave). Involves desk closure → SB mode → End of Mission → desk opening → Start of Mission. [subset26-2 ¶4205-¶4242]

### 5.13 Train Reversing
Allows fast reversal to run away from danger. Trackside announces reversing permitted area. Driver acknowledges transition to RV mode. Trackside can send new permitted distance and speed in RV mode. [subset26-2 ¶4243-¶4251]

### 5.14 Joining/Splitting
Procedures for splitting a train (remove mechanical links, update Train Data, handle SL/NL slave engines) and joining trains (approach in SR/OS/SH, close links, update Train Data, handle leading/slave roles). [subset26-2 ¶4252-¶4269]

### 5.15 RBC/RBC Handover
Procedure for passing from one RBC area to another. Normal operation: pre-announcement, registration to new radio network (optional), MA generation including border, announcement, transfer of supervision, session termination. Degraded situation for single-session handling: terminate with Handing Over RBC first, then establish with Accepting RBC. [subset26-2 ¶4270-¶4353]

### 5.16 Non-Protected Level Crossing
Procedure for LX not protected. On-board supervises LX start location as both EOA and SvL (no release speed). Substituted by LX speed restriction in MRSP under defined conditions. Stopping in rear may be required or not required. Driver informed about LX status. [subset26-2 ¶4354-¶4372]

### 5.17 Changing Train Data from External Sources
Procedure when Train Data changes from non-driver external sources (e.g., tilting device). Depending on data type requiring/not requiring validation, train standstill state, and mode, the procedure commands service brake if needed, requests driver acknowledgement, and updates Train Data. [subset26-2 ¶4373-¶4388]

### 5.18 Indication of Track Conditions
Procedures for driver indications related to: powerless section (pantograph lowering/main power switch), non-stopping area, radio hole, air tightness, brake inhibition (regenerative/eddy current/magnetic shoe), tunnel stopping area, sound horn, change of traction system. Each defines announcement and active indication points relative to the train's front/rear safe positions. [subset26-2 ¶4389-¶4539]

### 5.19 Limited Supervision Procedure
Entry to LS mode via mode profile. Current or further location. Driver acknowledgement with rectangle of acknowledgement. Exit when min safe front end passes end of LS area. [subset26-2 ¶4540-¶4588]

### 5.20 Generation of Track Conditions to External Function
Generation of distance information (remaining distances from train ends to condition locations) for ERTMS/ETCS external functions. Covers pantograph lowering, main power switch, air tightness, brake inhibition, traction system change, current consumption change, station platforms. Remaining distances generated until min safe rear end passes the relevant location. [subset26-2 ¶4590-¶4688]

## Chapter 6: Management of Older System Versions

Defines the envelope of legally operated system versions and exceptions for older versions.

### Envelope
- System version X (incompatible): 1 or 2 [subset26-2 ¶4708-¶4709]
- System version Y (compatible within X): 0 or 1 [subset26-2 ¶4710-¶4712]

### Trackside Requirements (X=1)
Exceptions to chapters 3, 4, 7, 8 when operating with system version X=1. Defines which packets are allowed/forbidden, modified packet structures for National Values, SSP, Axle Load, Mode Profile, Route Suitability, etc. Additional packets specific to X=1: Packet 200 (VBC marker), Packet 203 (National Values for braking curves), Packet 206 (Track Condition), Packet 207 (Route Suitability Data), Packet 239 (Track Condition Change of traction system). [subset26-2 ¶4713-¶4906]

### Trackside Requirements (X=2)
Exceptions for X=2 infrastructure, distinguishing between RBCs certified to 2.0 and 2.1. [subset26-2 ¶4907-¶4932]

### On-Board Requirements
Translation tables for handling data received from X=1 trackside (packets, messages, variables). Specific translations for M_AXLELOAD → M_AXLELOADCAT, NC_DIFF → NC_CDDIFF/Q_DIFF/NC_DIFF, M_TRACTION → M_VOLTAGE+NID_CTRACTION and other format conversions. [subset26-2 ¶4933-¶5050]

## Chapter 7: ERTMS/ETCS Language

Defines the communication language used over radio, balise, and loop airgaps.

### Components
- **Variables**: Single data values with defined prefixes (A_ acceleration, D_ distance, G_ gradient, L_ length, M_ miscellaneous, N_ number, NC_ class number, NID_ identity, Q_ qualifier, T_ time, V_ speed, X_ text) [subset26-2 ¶5075-¶5103]
- **Packets**: Groups of variables with packet header (NID_PACKET, Q_DIR, L_PACKET, Q_SCALE, information section). Track-to-Train and Train-to-Track. [subset26-2 ¶5104-¶5124]

### Track-to-Train Packets (7.4.2)
Defines 48 packet types (0-255) covering: Virtual Balise Cover marker, System Version order, National Values, Linking, Movement Authorities (L1 and L2/3), Gradient Profile, SSP, Track Conditions, Level Transition Orders, Session Management, Mode Profiles, TSRs, Adhesion Factor, Text Messages, Geographical Position, RBC Transition Order, Reversing Information, Train Running Number, LSSMA toggle, Generic LS marker, etc. [subset26-2 ¶5128-¶5290]

### Train-to-Track Packets (7.4.3)
Defines 8 packet types: Position Report, Position Report based on two balise groups, Onboard supported system versions, Error Reporting, Train running number, Level 2/3 transition information, Validated train data, Data for external applications. [subset26-2 ¶5292-¶5313]

### Variable Definitions (7.5)
Complete specification of all variables including name, description, length, min/max values, resolution, and special/reserved values. [subset26-2 ¶5315-¶5634]

## Cross-References
- [[subset26-1]] — Part 1 of this specification (Chapters 1–4.5)
- [[etcs-modes]] — ETCS modes concept
- [[etcs-application-levels]] — Application Levels concept
- [[movement-authority]] — Movement Authority concept
- [[override-procedure]] — Override procedure
- [[information-acceptance]] — Information acceptance filtering
- [[start-of-mission-procedure]] — Start of Mission procedure
- [[train-trip-procedure]] — Train Trip procedure
- [[level-transition-procedure]] — Level Transition procedure
- [[rbc-handover-procedure]] — RBC/RBC Handover procedure
- [[shunting-procedure]] — Shunting procedure
- [[on-sight-procedure]] — On Sight procedure
- [[limited-supervision-procedure]] — Limited Supervision procedure
- [[end-of-mission-procedure]] — End of Mission procedure
- [[track-conditions-procedures]] — Track conditions procedures
- [[stored-information-mode-level-actions]] — Stored information handling
- [[etcs-system-version-management]] — System version management
- [[etcs-language]] — ERTMS/ETCS language
- [[change-of-train-orientation]] — Change of Train Orientation
- [[train-reversing-procedure]] — Train Reversing procedure
- [[non-protected-level-crossing]] — Non-protected Level Crossing
- [[joining-splitting-procedure]] — Joining/Splitting procedure
- [[rbc]] — Radio Block Centre
- [[ertms-etcs-onboard]] — On-board equipment
- [[stm]] — Specific Transmission Module
- [[dmi-function]] — Driver Machine Interface
- [[stm-level-transitions]] — STM level transitions
