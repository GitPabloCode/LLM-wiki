# STM Control Function

**Source:** [[subset35]], [[subset58]] | **Date:** 2025-07-17 | **Type:** entity

The STM Control Function is the ERTMS/ETCS on-board function that manages STM states, version compatibility, data forwarding, and the interface between STMs and other on-board functions. In the Application Layer (SUBSET-058), it is assigned bus address 2 [subset58 ¶337]-[subset58 ¶351].

## Responsibilities

- Controls the STM state and version compatibility [subset58 ¶119]
- Maintains a list of available STMs (those with established connections reporting CS, HS, or DA) [subset58 ¶314]
- Sends state transition orders to STMs based on evaluated conditions [subset58 ¶354]
- Handles transmission of ETCS data, ETCS status data, and language info to STMs [subset58 ¶120]-[subset58 ¶122]
- Manages Specific NTC Data Entry/Data View procedures [subset58 ¶120]
- Handles the STM Test Procedure [subset58 ¶123]
- Manages the Override procedure for STMs [subset58 ¶124]
- Transmits airgap data to NTCs [subset58 ¶125]
- Handles STM max speed and system speed/distance [subset58 ¶126]
- Transmits bus address, safety level, and availability of on-board functions [subset58 ¶127]
- Displays STM failure status [subset58 ¶128]
- Handles Interface 'K' Antenna/BTM ID transmission [subset58 ¶129]
- Handles BTM alarm data transmission [subset58 ¶130]

## Application Layer Packets (from STM Control Function)

The STM Control Function sends and receives the following packets defined in SUBSET-058 [subset58 ¶132]-[subset58 ¶189]:

### Sent to STM:
- **STM-2** (val=2): ERTMS/ETCS on-board physical addresses and safety levels — addresses of JD, DMI channels 1-4, Odometer, TIU, and BIU functions with associated safety levels (SL0/SL2/SL4). Sent in PO state. [subset58 ¶133]-[subset58 ¶134]
- **STM-5** (val=5): ETCS status data — ETCS mode (M_MODESTM) and level (M_LEVEL, NID_NTC). Sent in PO, CO, DE, CS, HS, DA states. [subset58 ¶135]-[subset58 ¶136]
- **STM-7** (val=7): Override status — reports change of ETCS Override status (Q_OVR_STATUS) to STMs. [subset58 ¶139]-[subset58 ¶140]
- **STM-14** (val=14): State order to STM — NID_STMSTATEORDER commands state transitions. [subset58 ¶143]-[subset58 ¶144]
- **STM-175** (val=175): Train Data — validated train data (NC_CDTRAIN, NC_TRAIN, L_TRAIN, V_MAXTRAIN, M_LOADINGGAUGE, M_TRAINTYPE, M_VOLTAGE, NID_CTRACTION). [subset58 ¶151]-[subset58 ¶152]
- **STM-176** (val=176): Traction/brake parameters (T_BRAKE_SERVICE, T_BRAKE_EMERGENCY, T_TRACTION_CUT_OFF, M_BRAKE_POSITION, M_BRAKE_PERCENTAGE_STM). [subset58 ¶153]-[subset58 ¶154]
- **STM-177** (val=177): Additional data values and date/time (NID_ENGINE, M_ADHESION, YEAR/MONTH/DAY/HOUR/MINUTES/SECONDS/TTS, NID_OPERATIONAL_STM). [subset58 ¶155]-[subset58 ¶156]
- **STM-178** (val=178): National Values (all national value variables from ETCS packet 3). [subset58 ¶157]-[subset58 ¶160]
- **STM-22** (val=22): Test Procedure Permission. [subset58 ¶178]-[subset58 ¶179]
- **STM-30** (val=30): Driver language transmission (NID_DRV_LANG — 16-bit ISO 639-1 code). [subset58 ¶182]-[subset58 ¶183]
- **STM-31** (val=31): Active DMI channel (NID_DMICHANNEL). [subset58 ¶184]-[subset58 ¶185]
- **STM-20** (val=20): Antenna/BTM ID — Q_CHECKNEEDED, Q_ANTN_BTM_ACTIVE, NID_ANTENNA_BTM. [subset58 ¶186]-[subset58 ¶187]
- **STM-47** (val=47): BTM status — Q_BTM_ALARM, Q_BMM_ANNOUNCED. [subset58 ¶188]-[subset58 ¶189]
- **STM-45** (val=45): ETCS airgap message for STM — D_ESTODO_BG, N_LITER, M_DATA. [subset58 ¶174]-[subset58 ¶175]
- **STM-180** (val=180): Specific NTC Data values (NID_DATA, L_VALUE, X_VALUE). [subset58 ¶166]-[subset58 ¶167]
- **STM-182** (val=182): Request for Specific NTC Data View values. [subset58 ¶168]-[subset58 ¶169]
- **STM-184** (val=184): Specific NTC Data Entry flag (M_DATAENTRYFLAG — START/STOP). [subset58 ¶172]-[subset58 ¶173]
- **STM-141** (val=141): Train interface command configuration (all M_*_CMD_AVAIL variables). [subset58 ¶219]-[subset58 ¶220]

### Received from STM:
- **STM-1** (val=1): Version number (N_VERMAJOR, N_VERMINOR). [subset58 ¶128]-[subset58 ¶129]
- **STM-15** (val=15): State report (NID_STMSTATE). [subset58 ¶130]-[subset58 ¶131]
- **STM-6** (val=6): Override activation. [subset58 ¶137]-[subset58 ¶138]
- **STM-13** (val=13): State request (NID_STMSTATEREQUEST). [subset58 ¶141]-[subset58 ¶142]
- **STM-16** (val=16): STM max speed (V_STMMAX). [subset58 ¶145]-[subset58 ¶146]
- **STM-17** (val=17): STM system speed/distance (V_STMSYS, D_STMSYS). [subset58 ¶147]-[subset58 ¶148]
- **STM-18** (val=18): National Trip Procedure indication. [subset58 ¶149]-[subset58 ¶150]
- **STM-21** (val=21): Test Procedure Permission Request (NID_TEST). [subset58 ¶176]-[subset58 ¶177]
- **STM-23** (val=23): End of Test (M_TESTOK, L_TEXT, X_TEXT). [subset58 ¶180]-[subset58 ¶181]
- **STM-179** (val=179): Specific NTC Data Entry request (Q_FOLLOWING, NID_DATA, L_CAPTION, X_CAPTION, L_VALUE, X_VALUE). [subset58 ¶163]-[subset58 ¶165]
- **STM-181** (val=181): Specific NTC Data Need (Q_DATAENTRY). [subset58 ¶161]-[subset58 ¶162]
- **STM-183** (val=183): Specific NTC Data View values (Q_FOLLOWING, NID_DATA, L_CAPTION, X_CAPTION, L_VALUE, X_VALUE). [subset58 ¶170]-[subset58 ¶171]

## State Management

The STM Control Function's state manager uses a state order table and condition table to determine when to send orders to each STM [subset58 ¶342]-[§361]. It applies the emergency brake when conditions require it (e.g., active STM not responding, conditional CS order with active National Trip Procedure) [subset58 ¶363]-[§366].

## Association of STM to Level NTC

Uses a configurable look-up table mapping NID_NTC values to NID_STM values with priority ordering [subset58 ¶325]-[§338].

## Cross-references
- [[stm]] — The Specific Transmission Module entity
- [[stm-states]] — The eight STM operational states
- [[dmi-function]] — Driver Machine Interface
- [[connection-management]] — Connection opening and version check
- [[override-procedure]] — Override (trip inhibition) procedure
- [[specific-ntc-data-entry]] — National data entry procedure
- [[fffis-stm-application-layer]] — Application Layer protocol
