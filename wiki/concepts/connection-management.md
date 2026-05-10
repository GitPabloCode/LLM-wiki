# Connection Management

**Source:** [[subset35]] | **Date:** 2025-07-17 | **Type:** concept

Connection management governs how STMs open, verify compatibility, maintain, and close connections with ERTMS/ETCS on-board functions over the [[profibus]].

## Opening the Connection

- A connection is established when the version check completes successfully [subset35 ¶215]
- The STM takes the initiative to establish connections [subset35 ¶216]
- If connection fails twice, retry is allowed after 10 seconds [subset35 ¶217]

## Version Check

Each time an STM opens a connection with any ERTMS/ETCS on-board function, it sends its 'FFFIS STM version number' followed by state report [subset35 ¶219]. The receiving function checks compatibility:

1. If STM version < lowest supported → close connection [subset35 ¶221]
2. If STM version is supported → respond with highest supported version with same X, allow data transmission [subset35 ¶222]
3. If STM version > highest supported → close connection [subset35 ¶223]
4. STM also checks the version received from on-board; if incompatible, STM closes the connection [subset35 ¶224]-[§225]

## Closing the Connection

Closing on the application layer is done by requesting the Safety Layers to close the connection [subset35 ¶228].

## Multicast Connections

- The multicast sender opens separate connections for all FFFIS STM versions in the legal backward compatibility envelope [subset35 ¶233]
- Version number transmission is repeated to support restarting STMs [subset35 ¶235]
- If version is incompatible, the STM ignores data from that multicast connection [subset35 ¶237]

## Connection Sequence Charts

Figure 5 in the document shows the disconnection sequence chart for bad version numbers [subset35 ¶231].

## Cross-references
- [[stm]] — The Specific Transmission Module
- [[stm-control-function]] — Manages connections
- [[profibus]] — The communication bus
- [[fffis-stm-version-management]] — Version numbering scheme
