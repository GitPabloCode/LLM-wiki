# Odometer Function

**Source:** [[subset35]] | **Date:** 2025-03-13 | **Type:** entity

The **Odometer Function** is an ERTMS/ETCS on-board function that provides speed and distance estimation data to all connected STMs via multicast [¶99–§100].

## Data Provided

The odometer regularly transmits [¶561–§566]:
- **Estimated distance** (D_Est) — most probable position [¶581](http://localhost:8765/go.html#subset35-581)
- **Direction** — positive = forward (cab A) [¶567–§568]
- **Estimated speed** (V_Est) — estimated as in SUBSET-026 [¶574](http://localhost:8765/go.html#subset35-574)
- **Confidence intervals** — min/max distance (D_Min, D_Max), min/max speed (V_Min, V_Max) [¶574–§584]

All data is time-stamped with Reference Time from the Safe Time Layer [¶565–§566].

## Speed Definitions

- **V_Est**: Estimated speed per SUBSET-026 [¶574](http://localhost:8765/go.html#subset35-574)
- **V_Max**: Most positive speed (including under-reading for positive movement, lowest absolute for negative) [¶575–§576]
- **V_Min**: Most negative speed (including over-reading for positive movement, highest absolute for negative) [¶577–§578]

## Distance Definitions

- **D_Est**: Most probable position [¶581](http://localhost:8765/go.html#subset35-581)
- **D_Max**: Most positive position (all over/under-reading accumulated) [¶582](http://localhost:8765/go.html#subset35-582)
- **D_Min**: Most negative position (all over/under-reading accumulated) [¶583](http://localhost:8765/go.html#subset35-583)
- Confidence interval per SUBSET-041 [¶585](http://localhost:8765/go.html#subset35-585)
- Resolution parameter in each report [¶586](http://localhost:8765/go.html#subset35-586)
- Distance parameters may wrap individually [¶590](http://localhost:8765/go.html#subset35-590)

## Configuration Information

- **T_OdoCycle**: Typical cycle time [¶591–§592]
- **T_OdoMaxProd**: Maximum production delay including clock synchronisation [¶593–§596]

Odometer is not reset while powered on [¶570–§571].

## Cross-references
- [[Specific Transmission Module (STM)]] — receives odometer data
- [[PROFIBUS (STM Interface)]] — uses multicast SAP 100111
- [[STM Control Function]] — uses odometer data for speed supervision
- [[subset35]] — source document
