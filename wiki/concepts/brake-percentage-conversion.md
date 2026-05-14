# Brake Percentage and Conversion Models

**Source:** [[subset26]] | **Date:** 2025-07-17 | **Type:** concept

Brake percentage is train data used with conversion models to derive braking parameters for speed/distance monitoring. [subset26 ¶1591][subset26 ¶1592]

## Conversion Model Applicability

Conversion models apply when [subset26 ¶1712][subset26 ¶1715]:
- Maximum speed ≤ 200 km/h
- Brake percentage 30–250%
- Train length ≤ 900 m (Passenger P) or ≤ 1500 m (Freight)

## Braking Models

The braking model uses [subset26 ¶1541][subset26 ¶1544]:
- **Speed-dependent deceleration** — step function with up to seven steps
- **Brake build-up time** — modeled as T_brake_react + 0.5 × T_brake_increase → T_brake_build_up [subset26 ¶1572]
- **Brake position** — Passenger train in P, Freight train in P or G [subset26 ¶1585]

## Emergency Brake Equivalent Time

Calculated as T_brake_basic_eb = a + b×(L/100) + c×(L/100)², with coefficients depending on train type (passenger, freight P, freight G). When target speed > 0, corrected by factor kto (1 + 0.20 for passenger/freight P, 1 + 0.16 for freight G). [subset26 ¶2982][subset26 ¶3019]

## Service Brake Equivalent Time

Similar calculation with different coefficients for passenger and freight trains. [subset26 ¶3029][subset26 ¶3061]

## Cross-references
- [[speed-and-distance-monitoring]] — Uses brake percentage
- [[ertms-etcs-on-board-equipment]] — Stores brake percentage as train data
