# ERTMS/ETCS On-board Equipment

**Source:** [[subset26]] | **Date:** 2025-07-17 | **Type:** entity

The ERTMS/ETCS On-board Equipment is a computer-based system installed on the train that supervises the movement of the train based on information exchanged with the trackside subsystem. It can command brake application if necessary. [subset26 ¶132][subset26 ¶133][subset26 ¶245]

## Key Responsibilities

- **Train supervision**: Monitors speed against dynamic speed profile and applies brakes when limits are exceeded [subset26 ¶1498]
- **Position determination**: Calculates train position relative to the Last Relevant Balise Group (LRBG) with confidence intervals [subset26 ¶599]
- **Communication**: Initiates and manages communication sessions with RBCs and radio infill units [subset26 ¶455]
- **Mode management**: Transitions between 17 operating modes based on conditions [subset26 ¶3539]
- **Data processing**: Processes trackside information (balise telegrams, radio messages) for movement authorities, speed restrictions, track conditions [subset26 ¶2501]
- **Juridical recording**: Transmits information to the on-board recording device for legal purposes [subset26 ¶2818]

## Interfaces

- **DMI** (Driver Machine Interface) — displays information and accepts driver input [subset26 ¶169]
- **Train Interface** — commands brakes, traction cut-off, and monitors train state [subset26 ¶1606]
- **STM Interface** — interfaces with Specific Transmission Modules for National Systems [subset26 ¶194]
- **Eurobalise Antenna** — reads balise telegrams [subset26 ¶2144]
- **GSM-R Radio** — communicates with RBC/RIU via Euroradio [subset26 ¶138]
- **Odometry** — measures speed and distance travelled [subset26 ¶698]

## Identification

Each on-board unit has a unique ETCS identity (NID_ENGINE). [subset26 ¶5583]

## Cross-references
- [[rbc]] — The trackside counterpart
- [[dmi-function]] — Driver interface
- [[stm]] — National system interface
- [[eurobalise-antenna]] — Balise reading device
- [[euroradio]] — Radio communication protocol
- [[ertms-etcs-modes]] — Operating modes managed
- [[speed-and-distance-monitoring]] — Core supervision function
- [[movement-authority]] — Permission processed
