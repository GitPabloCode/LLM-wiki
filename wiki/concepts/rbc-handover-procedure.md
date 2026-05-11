# RBC/RBC Handover Procedure

**Source:** [[subset26-2]] | **Date:** 2026-05-12 | **Type:** concept

The RBC/RBC Handover procedure allows a train to pass from one RBC area to another automatically without driver action. [subset26-2 ¶4270-¶4271]

## Normal Operation (Dual Session) (5.15.2)

The train uses two communication sessions simultaneously (one with each RBC).

### Steps
1. **Pre-announcement**: Handing Over RBC generates MA reaching the border, informs Accepting RBC. [subset26-2 ¶4293-¶4295]
2. **Radio Registration & Session** (optional): Second Mobile Terminal registers to new radio network (if network change), establishes session with Accepting RBC. [subset26-2 ¶4296-¶4298]
3. **MA Generation**: Handing Over RBC requests route info from Accepting RBC for extending MA beyond border. [subset26-2 ¶4299-¶4305]
4. **Announcement**: When max safe front end reaches border, on-board sends position report to both RBCs. Handing Over forwards announcement info. [subset26-2 ¶4306-¶4309]
5. **Supervision Transfer**: On-board considers itself supervised by Accepting RBC after sending position report. Accepting RBC takes over when it detects max safe front end passed border. [subset26-2 ¶4310-¶4312]
6. **Session Termination**: When min safe rear end passes border, on-board sends position report to Handing Over RBC, which orders session termination. [subset26-2 ¶4314-¶4316]
7. **First Mobile Terminal Registration** (optional): After session termination, first MT registers to new network. [subset26-2 ¶4317-¶4318]

## Degraded Situation: Single Session (5.15.3)

If only one communication session can be handled, the sequence changes:

1. **Pre-announcement and MA Generation**: Same as normal. [subset26-2 ¶4329-¶4336]
2. **Announcement**: Position report sent only to Handing Over RBC, which forwards to Accepting RBC. [subset26-2 ¶4337-¶4339]
3. **Session Termination**: When min safe rear end passes border, on-board sends position report to Handing Over RBC, which orders session termination. [subset26-2 ¶4340-¶4342]
4. **New Session**: On-board terminates with Handing Over, then opens session with Accepting RBC (including radio network registration if needed). [subset26-2 ¶4343-¶4345]
5. **Supervision Transfer**: After establishing session and sending position report to Accepting RBC, considers itself supervised by Accepting RBC. [subset26-2 ¶4346-¶4348]

## Other Degraded Situations (5.15.4)

- If Handing Over RBC cannot extend MA into Accepting RBC area: driver may select Override or manually change level. [subset26-2 ¶4350]
- If on-board cannot open session with Accepting RBC: train stops at EOA; driver may select Override or manually change level. [subset26-2 ¶4351]
- If session termination with Handing Over RBC fails: position report repeated; after defined repetitions with no reply, on-board terminates session. [subset26-2 ¶4352-¶4353]

## Cross-References
- [[rbc]] — RBC entity
- [[level-transition-procedure]] — Related transition mechanisms
- [[information-acceptance]] — Transition buffer handling during handover
- [[start-of-mission-procedure]] — Session establishment procedures
- [[override-procedure]] — Degraded situation fallback
- [[subset26-1]] — RBC handover principles
