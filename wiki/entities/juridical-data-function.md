# Juridical Data Function

**Source:** [[subset35]], [[subset58]] | **Date:** 2025-07-17 | **Type:** entity

The Juridical Data Function allows STMs to transmit national juridical data to the On-Board Recording Device (JRU/DRU) via the ERTMS/ETCS on-board [subset58 ¶117].

## Application Layer Packet (SUBSET-058)

### STM-161 — STM Information to JD (val=161) [subset58 ¶229]-[subset58 ¶230]

Sent in PO, CO, DE, CS, HS, DA, FA states. National STM data transmitted to the Juridical Data Function.

| Variable | Bits | Description |
|----------|------|-------------|
| NID_PACKET | 8 | =161 |
| L_PACKET | 13 | Packet length |
| T_JD | 32 | Time stamp (Local Reference Time, 0-4,294,967,295 ms) [subset58 ¶440]-[subset58 ¶441] |
| N_LITER | 8 | Number of data bytes (max 228) [subset58 ¶352]-[subset58 ¶353] |
| M_DATA(k) | 8×N_LITER | Information to JD (data bytes, internal structure per STM supplier) |

Note: multiple instances of STM-161 are allowed in the same message (exception 4 to the single-instance rule) [subset58 ¶121].

## Key Requirements

- The ERTMS/ETCS on-board receives and forwards national juridical data from the STM to the recording device [subset58 ¶755]
- STMs must use the Reference Time for time-stamping juridical data [subset58 ¶756]
- The time stamp must represent the time the sent event occurred, to preserve event chronology [subset58 ¶757]
- The maximum value of N_LITER is limited to 228 [subset58 ¶353] (limitation from lower layers for SIL4 STM, as used in SUBSET-040)
- The T_JD timestamp (T_JD variable) uses Local Reference Time as specified in SUBSET-056 chapter 3.4.8 [subset58 ¶440]-[subset58 ¶441]

## Cross-references
- [[stm]] — The Specific Transmission Module
- [[stm-control-function]] — STM state management
- [[fffis-stm-application-layer]] — Application Layer protocol
