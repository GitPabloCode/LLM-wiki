# RBC/RBC Handover

**Source:** [[subset26]] | **Date:** 2025-07-17 | **Type:** concept

RBC/RBC Handover is the automatic transfer of train supervision from one RBC (Handing Over RBC) to another (Accepting RBC) without driver action. [subset26 ¶2345][subset26 ¶2347]

## Procedure

1. **Announcement**: Every handover is announced via a balise group or via the RBC [subset26 ¶4272]
2. **Pre-announcement**: The Handing Over RBC sends route-related information request to the Accepting RBC [subset26 ¶2351]
3. **Session establishment**: The on-board establishes a session with the Accepting RBC [subset26 ¶2389]
4. **Border crossing**: A balise group at the border orders execution of the handover [subset26 ¶4277]
5. **Supervision transfer**: When the max safe front end passes the border, the on-board uses information from the Accepting RBC [subset26 ¶2398]
6. **Session termination**: The Handing Over RBC terminates the session after handover completion [subset26 ¶4284]

## Route-Related Information

The Handing Over RBC may request from the Accepting RBC [subset26 ¶2363][subset26 ¶2377]:
- Movement Authorities
- International static speed profiles and axle load speed profiles
- Gradients and TSRs
- Mode profiles and track conditions
- Level transition orders and route suitability data
- National values and adhesion factor
- Level crossing information
- Permitted braking distance

## Degraded Single-Session Scenario

If the on-board can handle only one communication session, it waits until the Handing Over session is terminated before establishing the session with the Accepting RBC. [subset26 ¶2394][subset26 ¶4319]

## Cross-references
- [[rbc]] — The RBC entity
- [[communication-session]] — Session management
- [[ertms-etcs-on-board-equipment]] — On-board handover actions
- [[ertms-etcs-application-levels]] — Handover in Levels 2/3
