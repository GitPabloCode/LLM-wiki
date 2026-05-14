# Driver Machine Interface (DMI)

**Source:** [[subset26]] | **Date:** 2025-07-17 | **Type:** entity

The Driver Machine Interface (DMI) is the display providing information to the driver in ERTMS/ETCS. In Level 0, only train speed is indicated. [subset26 ¶169]

## Functions

- Displays supervision information: permitted speed, target speed, target distance, release speed, intervention speed [subset26 ¶2039]
- Shows text messages from trackside with conditions and optional acknowledgment [subset26 ¶1427]
- Displays mode-specific information (e.g., LSSMA toggling) [subset26 ¶3469]
- Provides driver input controls (buttons, acknowledgments) [subset26 ¶3577]

## DMI Input/Output per Mode

The DMI distinguishes between "active" (X) and "available" (A) inputs and outputs per operating mode. In SF and IS modes, DMI inputs and outputs are marked "Not Applicable" (NA). [subset26 ¶3577][subset26 ¶3578][subset26 ¶3580]

## Cross-references
- [[dmi-function]] — STM-related DMI function
- [[ertms-etcs-modes]] — DMI availability varies per mode
- [[ertms-etcs-on-board-equipment]] — The system hosting the DMI
