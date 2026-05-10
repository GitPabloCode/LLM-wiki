# Odometer Function

**Source:** [[subset35]], [[subset58]] | **Date:** 2025-07-17 | **Type:** entity

The Odometer Function provides odometry information from the ERTMS/ETCS on-board to all STMs via multicast messages over the FFFIS STM [subset58 ¶100].

## Application Layer Packets (SUBSET-058)

### STM-9 — Odometer Parameters to STM (val=9) [subset58 ¶191]-[subset58 ¶192]
Multicast in any state. Configuration data:

| Variable | Bits | Description |
|----------|------|-------------|
| T_ODOCYCLE | 8 | Typical cycle time (0-2550 ms, step 10ms) |
| T_ODOMAXPROD | 8 | Max production delay time (10-2550 ms, step 10ms). 0=reserved. |

### STM-8 — Odometer Multicast (val=8) [subset58 ¶193]-[subset58 ¶194]
Periodic multicast in any state. Odometer data:

| Variable | Bits | Description |
|----------|------|-------------|
| T_ODO | 32 | Timestamp (Local Reference Time, 0-4,294,967,295 ms) [subset58 ¶442]-[subset58 ¶443] |
| V_MAX | 16 | Upper bound of speed confidence interval (-32,768 to +32,767 cm/s, signed) [subset58 ¶456]-[subset58 ¶457] |
| V_EST | 16 | Estimated speed (-32,768 to +32,767 cm/s, signed) [subset58 ¶452]-[subset58 ¶453] |
| V_MIN | 16 | Lower bound of speed confidence interval (-32,768 to +32,767 cm/s, signed) [subset58 ¶458]-[subset58 ¶459] |
| D_MAX | 32 | Upper bound of distance confidence interval (-2,147,483,648 to +2,147,483,647 cm, signed) [subset58 ¶236]-[subset58 ¶237] |
| D_EST | 32 | Estimated distance (-2,147,483,648 to +2,147,483,647 cm, signed) [subset58 ¶232]-[subset58 ¶233] |
| D_MIN | 32 | Lower bound of distance confidence interval (-2,147,483,648 to +2,147,483,647 cm, signed) [subset58 ¶238]-[subset58 ¶239] |
| D_RES | 8 | Distance resolution (0-255 cm) [subset58 ¶240]-[subset58 ¶241] |

## Transmitted Information

- **Estimated speed (V_Est)** — as used by ERTMS/ETCS on-board [subset58 ¶574]
- **Maximum speed (V_Max)** — most positive physical speed including under-reading amount [subset58 ¶575]
- **Minimum speed (V_Min)** — most negative physical speed including over-reading amount [subset58 ¶578]
- **Estimated distance (D_Est)** — most probable position in vehicle coordinate system [subset58 ¶581]
- **Maximum distance (D_Max)** — most positive position with all over/under-reading amounts [subset58 ¶583]
- **Minimum distance (D_Min)** — most negative position with all over/under-reading amounts [subset58 ¶584]
- **Confidence intervals** for both speed and distance [subset58 ¶564]
- **Resolution** — provided in each odometer report [subset58 ¶586]

## Timing and Configuration

- Each report is time-stamped using the Reference Time [subset58 ¶565]
- Distance values are not reset while ERTMS/ETCS on-board is powered-on [subset58 ¶570]
- Performance parameters (cycle time, maximum production delay) are transmitted repeatedly to support restarting STMs [subset58 ¶592]-[§597]
- Positive movement = forward direction (cab A) with positive speed and increasing distance; negative = opposite [subset58 ¶567]-[§568]

## Wrapping

D_Est, D_Max, and D_Min may wrap individually when exceeding value range [subset58 ¶590].

## Cross-references
- [[stm]] — The Specific Transmission Module
- [[stm-control-function]] — STM state management
- [[stm-states]] — STM state definitions
- [[fffis-stm-application-layer]] — Application Layer protocol
