# ERTMS/ETCS Operating Modes

**Source:** [[subset26]] | **Date:** 2025-07-17 | **Type:** concept

ERTMS/ETCS defines 17 operating modes that determine how the on-board equipment supervises the train and interacts with the trackside. [subset26 ¶3162][subset26 ¶3165]

## Mode List

| Code | Abbrev. | Mode Name | Description |
|------|---------|-----------|-------------|
| 0 | FS | Full Supervision | Complete supervision against dynamic speed profile; entered automatically when all required data available [subset26 ¶3279] |
| 1 | OS | On Sight | Allows entry into possibly occupied track sections; entered on trackside command [subset26 ¶3355] |
| 2 | SR | Staff Responsible | Driver moves under own responsibility; ceiling speed and SR distance supervision [subset26 ¶3310] |
| 3 | SH | Shunting | Shunting movements; ceiling speed, list of expected balises; no train data required [subset26 ¶3247] |
| 4 | UN | Unfitted | Used in Level 0 areas; ceiling speed and TSR supervision [subset26 ¶3295] |
| 5 | PS | Passive Shunting | Slave engine coupled to leading engine in shunting; desk closed; no train supervision [subset26 ¶3498] |
| 6 | SL | Sleeping | Remote-controlled slave engine; no train supervision; desk must be closed [subset26 ¶3209] |
| 7 | SB | Stand By | Default awake mode; collects mission data; performs standstill supervision [subset26 ¶3234] |
| 8 | TR | Trip | Emergency brakes commanded and cannot be released; driver must acknowledge at standstill [subset26 ¶3372] |
| 9 | PT | Post Trip | After driver acknowledges trip; releases EB; allows supervised backward movement [subset26 ¶3387] |
| 10 | SF | System Failure | Safety-critical fault; permanently commands emergency brake [subset26 ¶3199] |
| 11 | IS | Isolation | On-board physically isolated from brakes [subset26 ¶3176] |
| 12 | NL | Non Leading | Slave engine not electrically coupled; no train supervision [subset26 ¶3406] |
| 13 | LS | Limited Supervision | Background supervision using dynamic speed profile [subset26 ¶3463] |
| 14 | SN | National System | National system accesses DMI, odometer, brakes via STM [subset26 ¶3425] |
| 15 | RV | Reversing | Change direction without changing cab; ceiling speed and distance limits [subset26 ¶3442] |
| - | NP | No Power | Equipment not powered; permanently commands EB; cold movement detection [subset26 ¶3187] |

## Key Mode Transitions

- **SoM**: SB → FS/LS/SR/OS/NL/UN/SN (Start of Mission) [subset26 ¶3775]
- **Train Trip**: Any → TR (when trip conditions met) [subset26 ¶4186]
- **Override**: Any → SR (when override activated at EOA) [subset26 ¶3926]
- **On Sight**: FS/LS → OS (when entering OS area) [subset26 ¶3989]
- **Mode Profile**: Trackside can order OS, LS, or SH mode via mode profile packets [subset26 ¶1480]

## Active Functions per Mode

Each mode activates specific on-board functions (check linking consistency, standstill supervision, manage track conditions, etc.). A detailed Active Functions Table shows which functions are active (X), optional (O), or inactive (blank) in each mode. [subset26 ¶3528][subset26 ¶3531]

## Cross-references
- [[ertms-etcs-on-board-equipment]] — The equipment managing modes
- [[speed-and-distance-monitoring]] — Supervision varies per mode
- [[communication-session]] — Session management varies per mode
- [[override-procedure]] — Override leading to SR mode
- [[stm-states]] — STM states associated with SN mode
