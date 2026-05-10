# Specific NTC Data Entry

**Source:** [[subset35]], [[subset58]] | **Date:** 2025-07-17 | **Type:** concept

The Specific NTC Data Entry procedure allows STMs to request national data from the driver via the ERTMS/ETCS on-board DMI. These are data needed for national operation beyond the standard ETCS Train Data [subset58 ¶425].

## Application Layer Packets (SUBSET-058)

The procedure uses six dedicated packets [subset58 ¶161]-[subset58 ¶173]:

### STM → STM Control Function:
- **STM-181** (val=181): Specific NTC Data Need — Q_DATAENTRY (1 bit) indicates if the STM needs data. Sent in PO, CO, CS, HS, DA states. [subset58 ¶161]-[subset58 ¶162]
- **STM-179** (val=179): Specific NTC Data Entry Request — Q_FOLLOWING (1 bit) chains multiple requests; N_ITER (5 bits, max 15) iterations carrying NID_DATA, L_CAPTION (6 bits, max 40 bytes), X_CAPTION, L_VALUE (5 bits, max 20 bytes), X_VALUE (default), plus dedicated keyboard values (L_VALUE/X_VALUE). Sent in DE, CS, HS, DA states. End of entry signalled by N_ITER=0. [subset58 ¶163]-[subset58 ¶165]
- **STM-183** (val=183): Specific NTC Data View Values — Q_FOLLOWING, N_ITER, NID_DATA, L_CAPTION, X_CAPTION, L_VALUE (max 20 bytes, 0=no current value), X_VALUE. Sent in CS, HS, DA states. [subset58 ¶170]-[subset58 ¶171]

### STM Control Function → STM:
- **STM-184** (val=184): Specific NTC Data Entry Flag — M_DATAENTRYFLAG (1 bit: 0=STOP, 1=START). Sent in CO, DE, CS, HS, DA states. [subset58 ¶172]-[subset58 ¶173]
- **STM-180** (val=180): Specific NTC Data Values — N_ITER (max 15), NID_DATA (8 bits), L_VALUE (5 bits, max 20 bytes), X_VALUE. Sent in DE, CS, HS, DA states. [subset58 ¶166]-[subset58 ¶167]
- **STM-182** (val=182): Request for Specific NTC Data View Values — no additional variables beyond header. Sent in CS, HS, DA states. [subset58 ¶168]-[subset58 ¶169]

## Process Flow

1. After ETCS Train Data is validated, ERTMS/ETCS on-board sends START flag (STM-184) and ETCS Train Data to the STM [subset58 ¶456]-[§457]
2. STM responds with either a 'Specific NTC Data Entry request' (STM-179) or 'End of Specific NTC Data Entry' (STM-179 with N_ITER=0) [subset58 ¶467]-[§468]
3. The on-board performs the dialogue with the driver for data entry/validation [subset58 ¶469]
4. Once validated, the on-board sends the Specific NTC Data to the STM via STM-180 [subset58 ¶470]
5. STM checks data against national criteria; if OK, sends 'End of Specific NTC Data Entry' (STM-179 with N_ITER=0) [subset58 ¶471]-[§472]
6. The on-board sends STOP flag (STM-184) [subset58 ¶458]

## Timeouts

A 10-second timeout (TrainDataEntry_STM_Response_Timeout) is supervised separately for each STM from sending ETCS Train Data until response is received, and from each Specific NTC Data send until response [subset58 ¶474]-[§476].

## Key Features

- Driver can skip the Specific NTC Data Entry for an STM [subset58 ¶435]
- Data may become invalid at any time due to national requirements [subset58 ¶436]
- STM can use ETCS data to reduce the amount of driver-entered national data [subset58 ¶426]
- Up to 15 Data Identifiers per request/response [subset58 ¶768]-[§770]
- Maximum 40 bytes for caption labels, 20 bytes for values [subset58 ¶165]
- Configurable keyboard types and range checks per STM [subset58 ¶448]-[§453]

## Cross-references
- [[stm]] — The Specific Transmission Module
- [[stm-control-function]] — Manages the data entry procedure
- [[dmi-function]] — Displays data entry to the driver
- [[stm-states]] — DE state is used for data entry
- [[fffis-stm-application-layer]] — Application Layer protocol
