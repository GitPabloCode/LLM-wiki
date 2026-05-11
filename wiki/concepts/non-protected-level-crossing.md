# Non-Protected Level Crossing Procedure

**Source:** [[subset26-2]] | **Date:** 2026-05-12 | **Type:** concept

Procedure for when a Level Crossing (LX) is not protected. The ERTMS/ETCS on-board supervises the LX start location as both the EOA and SvL (no release speed). [subset26-2 ¶4356]

## General Requirements (5.16.1)

- In FS, LS, or OS mode, the on-board temporarily supervises the LX start location as both EOA and SvL (replacing the MA-derived EOA/LOA), with no release speed. [subset26-2 ¶4356]
- This supervision is substituted by the inclusion of the LX speed restriction in the MRSP under defined conditions (5.16.2 or 5.16.3). [subset26-2 ¶4357]
- The end location of the LX speed restriction is the LX end location. [subset26-2 ¶4358]
- Driver is informed about LX status when the EOA/SvL related to LX becomes Most Relevant Displayed Target, or when substitution occurs. [subset26-2 ¶4359-¶4361]
- Indication remains displayed until 'LX is protected' is received or train passes LX end location with min safe front end. [subset26-2 ¶4362-¶4364]

## Stopping in Rear Required (5.16.2)

Once the train stops with estimated front end inside the stopping area (given by trackside), the on-board:
- Stops supervising LX start as EOA/SvL (reverts to MA-derived EOA/LOA and SvL) [subset26-2 ¶4366]
- Immediately includes LX speed restriction in MRSP, starting from estimated front end [subset26-2 ¶4366]

## Stopping in Rear Not Required (5.16.3)

The LX start is supervised as EOA/SvL until the train reaches the location of the braking-to-target Permitted speed supervision limit calculated for the LX speed. [subset26-2 ¶4369]

When the train front (estimated or max safe, depending on most restrictive SBI supervision limit) reaches this location, the on-board:
- Stops supervising LX start as EOA/SvL [subset26-2 ¶4370]
- Includes LX speed restriction in MRSP from the relevant train front position [subset26-2 ¶4370]

## Cross-References
- [[speed-and-distance-monitoring]] — SBI supervision limits
- [[movement-authority]] — EOA/LOA concepts
- [[subset26-1]] — Track condition principles
