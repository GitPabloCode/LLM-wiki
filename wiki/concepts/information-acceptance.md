# Information Acceptance

**Source:** [[subset26-2]] | **Date:** 2026-05-12 | **Type:** concept

The ERTMS/ETCS on-board equipment filters received trackside information through a three-stage process to determine what is accepted or rejected based on level, transmission medium, and current mode. [subset26-2 ¶3591-¶3592]

## Three-Filter Model (Figure 3)

1. **First Filter (Level & Transmission Media)**: Information accepted/rejected based on operating level (0, NTC, 1, 2, 3) and whether from RBC or balise/loop/RIU [subset26-2 ¶3612-¶3632]
2. **Second Filter (RBC/RBC Handover)**: Information stored in transition buffer during announced RBC transitions [subset26-2 ¶3660-¶3676]
3. **Third Filter (Mode)**: Information accepted/rejected based on the current operational mode [subset26-2 ¶3640-¶3658]

## Level & Transmission Media Acceptance (4.8.3)

For each information type, acceptance depends on operating level and source:

| Information | From RBC | Level 0 | NTC | L1 | L2 | L3 |
|---|---|---|---|---|---|---|
| National Values | No | A | A | A | A | A |
| Linking | No | R | R | A | R | R |
| MA + Mode Profile | No | R | R | A | R | R |
| Level Transition Order | Any | A | A | A | A | A |
| TSR | No | A | R | A | A | A |
| Unconditional Emergency Stop | Yes | R | R | R | A | A |

A = Accepted, R = Rejected [subset26-2 ¶3615-¶3620]

**Key exceptions**: Information stored if an order to switch to another level at a further location has been received (transition buffer). [subset26-2 ¶3621-¶3632]

**STM Interface**: STM max speed and STM system speed/distance accepted in all levels, except rejected in NTC level of the same STM (or accepted if a level transition to that NTC is pending). [subset26-2 ¶3634-¶3636]

## Mode-Based Acceptance (4.8.4)

For each information type, acceptance varies by mode. Examples:

- **Linking**: Accepted in SB (with conditions), FS, LS, SR, OS, NL, UN, PT, SN; Rejected in PS, SH, SL, TR, RV [subset26-2 ¶3645]
- **SR Authorisation**: Only accepted in SB (with conditions), SR, PT [subset26-2 ¶3647]
- **Unconditional Emergency Stop**: Accepted in SB (with conditions), FS, LS, SR, OS, UN, PT, SN [subset26-2 ¶3648]
- **Danger for SH**: Only accepted in SH [subset26-2 ¶3647]
- **Mode Profile**: Accepted in FS, LS, SR, OS, UN, PT, SN; Rejected in most others [subset26-2 ¶3648]
- **NP mode**: All information marked NR (Not Relevant) except for specific acceptance in NP [subset26-2 ¶3645]
- **SF, IS modes**: All information marked NR [subset26-2 ¶3645]

Exceptions apply for PT mode (L2/3 only following reception of 'Recognition of Exit from TR'), SB mode (only if a cab is active and valid Train Data stored), and PS/SH modes for level transition orders. [subset26-2 ¶3650-¶3658]

## Transition Buffer

When a level transition or RBC/RBC handover is announced, up to 3 sets of information can be stored in a transition buffer. These are released and re-evaluated sequentially when the transition is performed. [subset26-2 ¶3661-¶3675]

- Three sets max per transition buffer (level transition and RBC handover have separate buffers) [subset26-2 ¶3661-¶3662]
- New sets replace oldest if buffer full [subset26-2 ¶3664]
- Buffer deleted if transition order is deleted/overwritten or session terminated [subset26-2 ¶3665-¶3668]
- Re-evaluation is sequential and does not lead to intermediate mode changes or display changes [subset26-2 ¶3670-¶3673]
- Emergency Stop information re-evaluated according to stop location comparison [subset26-2 ¶3674-¶3675]

## Cross-References
- [[etcs-modes]] — Modes determine acceptance in third filter
- [[etcs-application-levels]] — Levels determine acceptance in first filter
- [[stm-level-transitions]] — STM interface information acceptance
- [[rbc-handover-procedure]] — RBC/RBC handover and transition buffer
- [[subset26-1]] — Core principles
