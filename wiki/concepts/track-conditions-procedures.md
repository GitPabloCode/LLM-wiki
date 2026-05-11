# Track Conditions Procedures

**Source:** [[subset26-2]] | **Date:** 2026-05-12 | **Type:** concept

ERTMS/ETCS defines procedures for driver indications and external function information related to track conditions. These are defined in SRS sections 5.18 (driver indications) and 5.20 (external function information).

## Driver Indications (5.18)

Each track condition defines announcement and active indication points relative to the train's safe front/rear positions.

### Powerless Section — Pantograph Lowering (5.18.2)
- 'Lower pantograph announcement' displayed when max safe front end reaches point C (determined by time needed for action and speed) [subset26-2 ¶4405-¶4406]
- At point D (start): announcement replaced by 'Lowered Pantograph' [subset26-2 ¶4411-¶4414]
- At point E (end): 'Raise pantograph' displayed; stays for fixed time after min safe rear end passes end [subset26-2 ¶4417-¶4424]

### Powerless Section — Main Power Switch (5.18.3)
- Same pattern: announcement (C) → active indication (D-E) → 'End of Neutral section' at E [subset26-2 ¶4429-¶4445]

### Non-Stopping Area (5.18.4)
- Two virtual SBI supervision limits calculated from SBD curves with feet at start (D) and train-length past end (G) [subset26-2 ¶4451]
- Between SBID and SBIG: display 'Non stopping area announcement' (if before D) or 'Non stopping area' (if past D) [subset26-2 ¶4452-¶4459]

### Radio Hole (5.18.5)
- 'Radio hole' displayed from D (start) until min safe rear end passes E (end) [subset26-2 ¶4465-¶4466]

### Air Tightness (5.18.6)
- 'Close air conditioning intake announcement' at C → 'Air conditioning intake closed' at D-E → 'Open air conditioning intake' after E [subset26-2 ¶4471-¶4488]

### Brake Inhibition (5.18.7)
- For regenerative/eddy current/magnetic shoe brakes: announcement at C → active at D-E [subset26-2 ¶4492-¶4503]

### Tunnel Stopping Area (5.18.8)
- Driver can enable/disable display (initial: disabled) [subset26-2 ¶4508]
- If enabled: virtual Permitted supervision limit calculated with foot at tunnel end [subset26-2 ¶4509]
- 'Tunnel stopping area announcement' (with remaining distance) before D; 'Tunnel stopping area' at D [subset26-2 ¶4512-¶4516]

### Sound Horn (5.18.9)
- 'Sound horn' from C (estimated front end, with driver reaction time) until E [subset26-2 ¶4521-¶4523]

### Change of Traction System (5.18.10)
- 'Change of traction system announcement' at C → 'New traction system' at F, stays for fixed time after min safe rear end passes F [subset26-2 ¶4528-¶4537]

## External Function Information (5.20)

The on-board generates remaining distance information (from train ends to condition locations) for ERTMS/ETCS external functions. Distances counted positive when train end is in rear of location, negative when in advance. [subset26-2 ¶4600]

### For Pantograph Lowering (5.20.2)
- Starts at C: provides remaining distance from max safe front end to D and from min safe front end to E [subset26-2 ¶4603-¶4604]
- When min safe rear end passes D: distance to D stops; distance to E continues [subset26-2 ¶4607-¶4608]
- When min safe rear end passes E: all generation stops [subset26-2 ¶4609]

### For Main Power Switch (5.20.3)
- Same pattern: two distances (max front→D, min front→E) until respective train ends pass locations [subset26-2 ¶4616-¶4621]

### For Air Tightness (5.20.4)
- Distances: max safe front end→D, min safe rear end→E [subset26-2 ¶4629-¶4633]

### For Brake Inhibition (5.20.5)
- Distances: max safe front end→D, min safe rear end→E [subset26-2 ¶4642-¶4647]

### For Traction System Change (5.20.6)
- Distance from max safe front end to F, plus identity of new traction system [subset26-2 ¶4654-¶4656]
- Stops when min safe rear end passes F [subset26-2 ¶4657]

### For Current Consumption Change (5.20.7)
- Distance from max safe front end to F, plus new allowed current consumption [subset26-2 ¶4665-°4667]

### For Station Platform (5.20.8)
- Distances: max front→D, min front→E, plus nominal height and side position (left/right/both) [subset26-2 ¶4676-¶4680]
- After min rear passes D: distance to D stops; other info continues [subset26-2 ¶4681]

### Resumption of Initial State
If a track condition is shortened or deleted (due to resuming initial state or other reasons), the on-board adjusts or stops providing the related external function information. [subset26-2 ¶4611-¶4612, ¶4624-¶4625, ¶4636-¶4637, ¶4648-¶4649, ¶4659, ¶4671, ¶4687-¶4688]

## Cross-References
- [[speed-and-distance-monitoring]] — SBI supervision limits for non-stopping areas
- [[ertms-etcs-onboard]] — On-board equipment functions
- [[subset26-1]] — Track condition data principles
