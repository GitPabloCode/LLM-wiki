# STM Connection Management

**Source:** [[subset35]] | **Date:** 2025-03-13 | **Type:** concept

**STM Connection Management** defines how STMs establish connections with ERTMS/ETCS on-board functions through version checking and negotiation [¶215–§237].

## Connection Establishment

- Connection is established when version check is successful [¶215](http://localhost:8765/go.html#subset35-215)
- STM initiates the connection [¶216](http://localhost:8765/go.html#subset35-216)
- After 2 connection failures, retry after 10 seconds [¶217](http://localhost:8765/go.html#subset35-217)

## Version Check Process

1. STM sends its "FFFIS STM version number" along with a state report to the function [¶219](http://localhost:8765/go.html#subset35-219)
2. Function checks the version [¶221–§223]:
   - If version lower than lowest supported → close connection
   - If version among supported → send highest supported with same X
   - If version higher than highest → close connection
3. STM checks the version returned by the function [¶224–§225]:
   - If compatible → transmit data
   - If not → close connection

Connection closing is performed via the Safety Layers [¶228](http://localhost:8765/go.html#subset35-228).

## Multicast Connections

- Sender opens separate connection for each version number in the legal backward compatibility envelope [¶233](http://localhost:8765/go.html#subset35-233)
- Table 6.5.1.5 contains one SAP per version number for Odometer [¶234](http://localhost:8765/go.html#subset35-234)
- Sender transmits corresponding version number repeatedly for restarting STMs [¶235](http://localhost:8765/go.html#subset35-235)
- STM checks compatibility; ignores data from incompatible multicast [¶236–§237]

## Cross-references
- [[Specific Transmission Module (STM)]] — initiates connections
- [[STM Version Management]] — defines the version format used in checks
- [[STM Safety Protocols]] — connection closing via Safety Layers
- [[PROFIBUS (STM Interface)]] — communication medium
- [[subset35]] — source document
