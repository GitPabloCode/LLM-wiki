# ETCS Modes

**Source:** [[subset26-1]] | **Date:** 2026-05-12 | **Type:** concept

ERTMS/ETCS defines 17 operational modes for the on-board equipment, each specifying the context of use, applicable levels, and responsibilities. [subset26-1 ¶3162-¶3165]

## List of Modes

| Mode | Abbr. | Used in Levels | Description |
|------|-------|----------------|-------------|
| Full Supervision | FS | 1, 2, 3 | Complete train supervision with dynamic speed profile; all required data available [subset26-1 ¶3279-¶3294] |
| Limited Supervision | LS | 1, 2, 3 | Background supervision where trackside information is limited; driver observes lineside signals [subset26-1 ¶3463-¶3497] |
| On Sight | OS | 1, 2, 3 | Entering occupied or obstructed track sections [subset26-1 ¶3355-¶3371] |
| Staff Responsible | SR | 1, 2, 3 | Driver moves train under own responsibility; ceiling speed and given distance supervised [subset26-1 ¶3310-¶3354] |
| Shunting | SH | 0, NTC, 1, 2, 3 | Shunting movements; ceiling speed limit, list of expected balises [subset26-1 ¶3247-¶3278] |
| Unfitted | UN | 0 | Operation on non-equipped lines; ceiling speed supervision [subset26-1 ¶3295-¶3309] |
| Passive Shunting | PS | 0, NTC, 1, 2, 3 | Slave engine in shunting consist; desk closed, no supervision [subset26-1 ¶3498-¶3521] |
| Sleeping | SL | 0, NTC, 1, 2, 3 | Remote-controlled slave engine; desk closed, no supervision [subset26-1 ¶3209-¶3233] |
| Stand By | SB | 0, NTC, 1, 2, 3 | Default mode on awakening; data collection, standstill supervision [subset26-1 ¶3234-¶3246] |
| Trip | TR | 0, NTC, 1, 2, 3 | Emergency brakes commanded; train tripped after passing EOA [subset26-1 ¶3372-¶3386] |
| Post Trip | PT | 1, 2, 3 | After driver acknowledges trip; reverse movement allowed up to a distance [subset26-1 ¶3387-¶3405] |
| System Failure | SF | 0, NTC, 1, 2, 3 | Safety-critical fault; emergency brakes permanently commanded [subset26-1 ¶3199-¶3208] |
| Isolation | IS | 0, NTC, 1, 2, 3 | ETCS physically isolated from brakes; driver's complete responsibility [subset26-1 ¶3176-¶3186] |
| No Power | NP | 0, NTC, 1, 2, 3 | Equipment not powered; emergency brake commanded [subset26-1 ¶3187-¶3198] |
| Non Leading | NL | 0, NTC, 1, 2, 3 | Slave engine not remote controlled with own driver; no train supervision [subset26-1 ¶3406-¶3424] |
| National System | SN | NTC | Operation under national system via STM; ETCS provides DMI, odometer, train interface access [subset26-1 ¶3425-¶3441] |
| Reversing | RV | 1, 2, 3 | Change movement direction without changing train orientation; ceiling speed and distance supervised [subset26-1 ¶3442-¶3462] |

## Mode Transitions

Transitions between modes follow defined rules with priority ordering to resolve conflicts. Conditions for each transition are detailed in the Transitions Table and Transitions Conditions Table. [subset26-1 ¶3542-¶3549]

## Active Functions per Mode

Each mode has a defined set of active/inactive on-board functions including data consistency checking, train position determination, speed monitoring, MA management, communication management, etc. [subset26-1 ¶3527-¶3541]

## Cross-References
- [[ertms-etcs-onboard]] — On-board equipment that implements these modes
- [[speed-and-distance-monitoring]] — Speed supervision varies by mode
- [[etcs-application-levels]] — Levels in which modes can be used
- [[stm-states]] — STM states complement ETCS modes
- [[subset26-1]] — Source document
