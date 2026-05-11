# Speed and Distance Monitoring

**Source:** [[subset26-1]] | **Date:** 2026-05-12 | **Type:** concept

Speed and Distance Monitoring is the supervision of train speed versus position to ensure the train remains within given speed and distance limits. [subset26-1 ¶1500]

## Three Monitoring Types

### 1. Ceiling Speed Monitoring (CSM)
Speed supervision in areas where the train can run without braking to a target. Uses ceiling supervision limits derived from the Most Restrictive Speed Profile (MRSP). [subset26-1 ¶2132]

### 2. Target Speed Monitoring (TSM)
Speed and distance supervision in areas where the train brakes to a target (EOA/LOA or MRSP speed decrease). Uses both ceiling and braking-to-target supervision limits. [subset26-1 ¶2133]

### 3. Release Speed Monitoring (RSM)
Speed supervision near the EOA where the train runs at low release speed to approach the EOA. [subset26-1 ¶2134]

## Supervision Limits

- **EBI** (Emergency Brake Intervention): Assures train remains within limits [subset26-1 ¶1949]
- **SBI** (Service Brake Intervention): Assists driver to prevent emergency brake [subset26-1 ¶1950]
- **Warning (W)**: Warning before SBI [subset26-1 ¶2022-¶2027]
- **Permitted speed (P)**: Speed the driver should not exceed [subset26-1 ¶2028-¶2054]
- **Indication (I)**: First indication that braking may be needed [subset26-1 ¶2075-¶2082]

## Most Restrictive Speed Profile (MRSP)

Computed from all speed restriction categories (SSP, ASP, TSR, signalling related, mode related, train related, LX, override, PBD) by selecting the most restrictive parts. Recalculated when any element changes. [subset26-1 ¶1903-¶1907]

## Braking Curves

- **EBD** (Emergency Brake Deceleration curve): Based on safe deceleration A_safe(V,d) [subset26-1 ¶1923-¶1929]
- **SBD** (Service Brake Deceleration curve): Based on expected deceleration A_expected(V,d) [subset26-1 ¶1930-¶1933]
- **GUI** (Guidance curve): Comfortable braking, based on normal service brake deceleration [subset26-1 ¶1934-¶1938]

## Deceleration Calculations

- **Safe deceleration** A_safe(V,d): Safety-relevant, uses correction factors, adhesion conditions, rolling stock factors [subset26-1 ¶1787-¶1827]
- **Expected deceleration** A_expected(V,d): Not safety-relevant, no worst-case conditions [subset26-1 ¶1851-¶1866]
- **Normal service brake deceleration**: Uses correction factors Kn+ and Kn- for gradient [subset26-1 ¶1886-¶1902]

## Cross-References
- [[movement-authority]] — MA defines targets for speed monitoring
- [[ertms-etcs-onboard]] — On-board equipment performs monitoring
- [[etcs-modes]] — Monitoring behaviour varies by mode
- [[subset26-1]] — Source document
