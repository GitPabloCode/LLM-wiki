# Radio Block Centre (RBC)

**Source:** [[subset26-1]] | **Date:** 2026-05-12 | **Type:** entity

The Radio Block Centre (RBC) is a computer-based trackside system that generates movement authorities and controls train movements in ERTMS/ETCS Levels 2 and 3. [subset26-1 ¶113]

## Functions

- Elaborates messages to be sent to trains based on information from external trackside systems and from on-board subsystems [subset26-1 ¶113]
- Provides movement authorities for safe train movement within its area of responsibility [subset26-1 ¶114]
- Knows each ERTMS/ETCS controlled train individually by its ETCS identity [subset26-1 ¶254]
- Follows each train's location within its RBC area [subset26-1 ¶264]
- Determines movement authorities according to the underlying signalling system for each train individually [subset26-1 ¶265]
- Transmits movement authorities and track description to each train individually [subset26-1 ¶266]
- Handles handover of train control between different RBCs at RBC-RBC borders [subset26-1 ¶267]
- In Level 3: performs route locking and releasing based on information received from trains [subset26-1 ¶296]

## RBC/RBC Handover

Trains pass from one RBC area to another automatically without driver action [subset26-1 ¶2347].

**Handing Over RBC responsibilities:**
- Sends train information (ETCS identity, mode, train data, supported system versions) to Accepting RBC [subset26-1 ¶2354-¶2360]
- Requests route-related information from Accepting RBC (MA, linking, SSP, gradients, TSRs, etc.) [subset26-1 ¶2362-¶2378]
- Detects when train passes border and informs Accepting RBC [subset26-1 ¶2381]
- Sends disconnection order to on-board when min safe rear end crosses border [subset26-1 ¶2383]
- Stops sending route info when Accepting RBC takes over [subset26-1 ¶2384]

**Accepting RBC responsibilities:**
- Keeps route-related information sent to Handing Over RBC updated [subset26-1 ¶2411]
- Informs Handing Over RBC when it has taken over responsibility [subset26-1 ¶2412]
- Train Data from on-board takes precedence over Handing Over RBC data [subset26-1 ¶2413]

## Communication

- Communication with on-board via Euroradio (GSM-R) [subset26-1 ¶110]
- Only on-board can initiate communication sessions [subset26-1 ¶455]
- System version determined during session establishment [subset26-1 ¶490-¶494]

## Cross-References
- [[ertms-etcs-onboard]] — The on-board equipment that communicates with RBC
- [[movement-authority]] — The concept of Movement Authority managed by RBC
- [[subset26-1]] — Source document
- [[eurobalise]] — Used for location referencing in L2/3
- [[gsm-r]] — Radio communication network
