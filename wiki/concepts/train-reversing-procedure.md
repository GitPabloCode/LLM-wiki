# Train Reversing Procedure

**Source:** [[subset26-2]] | **Date:** 2026-05-12 | **Type:** concept

The Train Reversing procedure allows the fast reversal of a train to run away from a danger up to a 'safe' location. [subset26-2 ¶4243-¶4244]

## Procedure (5.13)

1. **Reversing Area Announcement**: Trackside announces the area where reversing is permitted via packet 138 (Reversing area information). [subset26-2 ¶4245]
2. **Driver Notification**: While the train is at standstill inside the reversing permitted area, the driver is informed that reversing is possible. [subset26-2 ¶4246]
3. **Acknowledgment**: If the on-board detects the driver's intention to reverse (e.g., direction controller in reverse position), it asks the driver to acknowledge transition to RV mode. [subset26-2 ¶4247]
4. **Switch to RV**: When driver acknowledges, the on-board switches to RV mode. [subset26-2 ¶4248]
5. **Trackside Updates**: Once in RV mode, trackside can send:
   - A new permitted distance to run and new maximum speed (packet 139) [subset26-2 ¶4249]
   - A new reference location for the permitted distance [subset26-2 ¶4250]

The reference location is used only for distance referencing in RV mode. [subset26-2 ¶4251]

## Cross-References
- [[etcs-modes]] — RV mode description
- [[subset26-1]] — Reversing supervision principles
- [[speed-and-distance-monitoring]] — Speed supervision in RV
- [[etcs-application-levels]] — RV available in L1/2/3
