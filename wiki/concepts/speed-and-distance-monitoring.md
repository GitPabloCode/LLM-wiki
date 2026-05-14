# Speed and Distance Monitoring

**Source:** [[subset26]] | **Date:** 2025-07-17 | **Type:** concept

Speed and Distance Monitoring is the supervision of train speed versus position to remain within safe limits. It is the core safety function of ERTMS/ETCS on-board equipment. [subset26 ¶1498][subset26 ¶1500]

## Monitoring Types

Three types of speed and distance monitoring are defined [subset26 ¶2128][subset26 ¶2129][subset26 ¶2131]:

1. **Ceiling Speed Monitoring (CSM)** — when the train can run without needing to brake to a target (uses only ceiling supervision limits) [subset26 ¶2128][subset26 ¶2132]
2. **Target Speed Monitoring (TSM)** — when the train is braking toward a specific target [subset26 ¶2129][subset26 ¶2133]
3. **Release Speed Monitoring (RSM)** — close to the EOA where only the release speed is supervised [subset26 ¶2131][subset26 ¶2134]

## Supervision Limits

The on-board calculates several supervision limits [subset26 ¶1951][subset26 ¶1964]:

- **EBI** (Emergency Brake Intervention) — final limit; triggers emergency brake
- **SBI1/SBI2** (Service Brake Intervention) — triggers service brake
- **W** (Warning) — warns the driver before SBI
- **P** (Permitted speed) — speed the driver should not exceed
- **I** (Indication) — earliest indication to the driver

## Braking Models

Speed and distance monitoring uses either [subset26 ¶1534]:
- **Braking models** acquired as Train Data (speed-dependent deceleration, brake build-up time), or
- **Brake percentage** with conversion model (for speeds ≤200 km/h, brake percentage 30-250%)

## Most Restrictive Speed Profile (MRSP)

The MRSP is a composite of the most restrictive speed restrictions from all sources (SSP, TSR, ASP, signalling-related, mode-related, etc.). [subset26 ¶1903][subset26 ¶1904]

## Key Parameters

- **T_driver**: Fixed driver reaction time [subset26 ¶2034]
- **T_indication**: Time for indication limit calculation [subset26 ¶2079]
- **Supervised targets**: MRSP speed reductions, LOA, EOA, SvL, SR distance end [subset26 ¶1915]
- **Gradient compensation**: Profiles compensated by train length and rotating mass [subset26 ¶1742]

## Cross-references
- [[movement-authority]] — Targets come from MA
- [[ertms-etcs-modes]] — Supervision varies per mode
- [[train-position]] — Position input for monitoring
- [[rbc]] — Provides speed restriction data
- [[ertms-etcs-application-levels]] — Supervision rules per level
