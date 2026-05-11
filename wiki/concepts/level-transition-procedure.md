# Level Transition Procedure

**Source:** [[subset26-2]] | **Date:** 2026-05-12 | **Type:** concept

Level transitions define how the ERTMS/ETCS on-board equipment switches between application levels (0, NTC, 1, 2, 3) when crossing level borders.

## General Requirements (5.10.1)

- Every level transition border to L2/3 or NTC shall be announced via balise group or RBC. [subset26-2 ¶4045]
- The announcement consists of an order to execute the transition at a further location. [subset26-2 ¶4046]
- Driver is immediately informed about an announced level transition that will result in a change. [subset26-2 ¶4047]
- A border balise group with an immediate or conditional level transition order is placed at the transition border. [subset26-2 ¶4049]
- If the border balise group message is not received, the transition is still executed when the estimated front end passes the announced location. [subset26-2 ¶4052]
- Only one level transition order managed at a time; new order replaces previous. [subset26-2 ¶4053]
- In SH and PS modes, only one set of Level Transition Information stored at a time. [subset26-2 ¶4054]

## Table of Priority of Supported Levels (5.10.2)

Any combination of levels 0, NTC, 1, 2, 3 on a given area is possible. [subset26-2 ¶4062]

The level transition announcement contains a table of priority listing all supported levels. [subset26-2 ¶4063]

On-board selects from the table the level with highest priority available for use:
- **L2/3**: Configured on-board and at least one Mobile Terminal available [subset26-2 ¶4069]
- **NTC**: National System available on-board [subset26-2 ¶4070]
- **L0/1**: Always [subset26-2 ¶4071]

If none of the ordered levels is available, the on-board transitions to the lowest priority level anyway. [subset26-2 ¶4076-¶4077]

## Specific Transition Requirements (5.10.3)

### L1 ↔ L2/3
- Order to connect to RBC given via balise in rear of border [subset26-2 ¶4084]
- Old area must provide MA/track description info for new area (either as MA or as LOA) [subset26-2 ¶4085-¶4086]
- Train Data sent to RBC (unless in SL or NL) [subset26-2 ¶4088]
- On-board reports new level with position report [subset26-2 ¶4090]

### L0 ↔ L2/3
- RBC connection order via balise in rear [subset26-2 ¶4093]
- L2/3 MA and track description must be received before border, otherwise train tripped [subset26-2 ¶4095]
- Driver responsible for entering at appropriate speed [subset26-2 ¶4096]

### L2/3 → L1
- New area information provided as MA or LOA [subset26-2 ¶4100-¶4102]
- Position report sent when min safe rear end passes border [subset26-2 ¶4104]
- RBC orders session termination after exit position report [subset26-2 ¶4105]

### L0 → L1
- L1 MA and track description must be received before/at border, otherwise train tripped [subset26-2 ¶4108]
- Driver responsible for entering at appropriate speed [subset26-2 ¶4109]

### L1 → L0
- Old area provides MA or LOA for new area [subset26-2 ¶4111-¶4113]
- When entering UN mode, all MA and track description data deleted [subset26-2 ¶4114]

### L2/3 → L0
- Old area provides MA or LOA for new area [subset26-2 ¶4116-¶4118]
- Position report sent when min safe rear end passes border [subset26-2 ¶4119]
- All MA/track description data deleted on UN entry [subset26-2 ¶4121]

### L/NTC ↔ L2/3, L/NTC ↔ L1, L/NTC → L0, L0 → L/NTC
Each transition has requirements for MA availability, RBC connection, STM state orders (referencing SUBSET-035), and driver speed responsibility. [subset26-2 ¶4123-¶4160]

## Conditional Level Transition Order (5.10.3.14)

Allows checking whether a train operates in a permitted level (e.g., after cold movement). [subset26-2 ¶4161-¶4166]
- If current level is in the priority list, no level change. [subset26-2 ¶4163]
- If current level is not in the priority list, evaluated as an immediate level transition order. [subset26-2 ¶4164]

## Driver-Initiated Level Transitions (5.10.3.15)

At standstill, the driver can change the level. [subset26-2 ¶4167-¶4168]
- To L2/3: Establish communication session with RBC. [subset26-2 ¶4169-¶4171]
- From L2/3: Report new level to RBC, which orders session termination. [subset26-2 ¶4173-¶4175]

## Acknowledgement (5.10.4)

Defined table of transitions requiring driver acknowledgement. [subset26-2 ¶4184-¶4185]
- Entering L0 from L1/2/3: Yes, from NTC: Yes
- Entering L1 from L0/NTC: Yes, from L2/3: No
- Entering L2/3 from L0/1/NTC: No
- Entering NTC from any: Yes
- NL mode does not require acknowledgement. [subset26-2 ¶4180]

## Cross-References
- [[etcs-application-levels]] — Level definitions
- [[stm-level-transitions]] — STM-specific level transition rules
- [[rbc]] — RBC involved in L2/3 transitions
- [[information-acceptance]] — What information is accepted during announced transitions
- [[subset26-1]] — Level transition table
