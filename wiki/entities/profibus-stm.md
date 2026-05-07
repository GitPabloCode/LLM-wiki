# PROFIBUS (STM Interface)

**Source:** [[subset35]] | **Date:** 2025-03-13 | **Type:** entity

The **PROFIBUS** bus is the physical communication medium for the STM interface, defined per CENELEC 50170-2 up to the FDL layer [¶149–§150]. It serves as the lower boundary of the FFFIS STM specification [¶64](http://localhost:8765/go.html#subset35-64).

## Configuration

- **Baud Rate**: 1500 Kbps [¶152](http://localhost:8765/go.html#subset35-152)
- **Min TSDR**: 11 tBit [¶153](http://localhost:8765/go.html#subset35-153)
- **Max TSDR**: 150 tBit [¶154](http://localhost:8765/go.html#subset35-154)
- **TSL**: 300 tBit [¶155](http://localhost:8765/go.html#subset35-155)
- **TQUI**: 0 tBit [¶156](http://localhost:8765/go.html#subset35-156)
- **TSET**: 1 tBit [¶157](http://localhost:8765/go.html#subset35-157)
- **TTR**: 30000 tBit (20 ms) [¶158](http://localhost:8765/go.html#subset35-158)
- **G**: 10 [¶159](http://localhost:8765/go.html#subset35-159)
- **HSA**: 126 [¶160](http://localhost:8765/go.html#subset35-160)
- **Max_retry_limit**: 1 [¶161](http://localhost:8765/go.html#subset35-161)

## Physical Characteristics

- Max 200 m per segment, 32 stations on cable type A [¶163](http://localhost:8765/go.html#subset35-163)
- Default medium: RS-485 twisted pair shielded copper cable [¶165–§166]
- Connector: 9-pin female D-SUB per PROFIBUS specs [¶167](http://localhost:8765/go.html#subset35-167)
- Repeaters for greater length/more stations [¶163](http://localhost:8765/go.html#subset35-163)

## Redundancy

- Retransmission per Safe Link Layer [¶168–§169]
- STM and ERTMS/ETCS on-board have at least one bus interface, may have two [¶170](http://localhost:8765/go.html#subset35-170)
- If different number of buses, only one connected [¶171](http://localhost:8765/go.html#subset35-171)
- Dual bus managed by Redundancy Supervisor [¶172](http://localhost:8765/go.html#subset35-172)

## Physical Addressing

- Each STM has one physical address [¶183](http://localhost:8765/go.html#subset35-183)
- Address 2: STM Control Function [¶190](http://localhost:8765/go.html#subset35-190)
- Addresses 0,1,2,3…19: other functions [¶190](http://localhost:8765/go.html#subset35-190)
- Addresses 20…49: unused [¶190](http://localhost:8765/go.html#subset35-190)
- Addresses 50…69: configurable STM range [¶190](http://localhost:8765/go.html#subset35-190)
- Addresses 70…126: STMs (NID_NTC+70) [¶190](http://localhost:8765/go.html#subset35-190)
- Address 127: Broadcast/Multicast [¶190](http://localhost:8765/go.html#subset35-190)
- Default STM address = NID_NTC + 70 [¶191](http://localhost:8765/go.html#subset35-191)
- Configurable range for STMs where NID_STM+70 exceeds PROFIBUS range or to resolve conflicts [¶192–§194]

## Function Addressing (SAPs)

- All functions have fixed SAP regardless of physical address [¶198–§199]
- SSAP and DSAP have same value [¶200](http://localhost:8765/go.html#subset35-200)
- Key SAPs: DMI (000000, 000001, 000100, 000101), Juridical Data (000010), Reference Time (100000, multicast), STM Control (100001), TIU (100101), BIU (100110), Odometer (100111, multicast), Broadcast (111111) [¶202–§203]

## Cross-references
- [[Specific Transmission Module (STM)]] — communicates via this bus
- [[STM Control Function]] — uses address 2
- [[Odometer Function]] — uses multicast SAP 100111
- [[STM Safety Protocols]] — safety layers above PROFIBUS
- [[subset35]] — source document
