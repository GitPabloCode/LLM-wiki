# STM Version Check

**Source:** [subset35](../summaries/subset35.md), [subset58](../summaries/subset58.md) | **Date:** 2026-04-29 | **Type:** concept

The **STM version check** is a bidirectional handshake protocol that runs each time an STM opens a point-to-point connection with any ERTMS/ETCS on-board function. Its purpose is to verify that the FFFIS STM version implemented by the STM is compatible with the version supported by the on-board function before any application data is exchanged. A connection is only considered established once the version check completes successfully. [¶215-226](http://localhost:8765/go.html#subset35-215)

## Procedure

The handshake has three steps, always initiated by the STM:

1. **STM sends its version** — The STM transmits packet **STM-1** containing the FFFIS STM version number (N_VERMAJOR for X, N_VERMINOR for Y, each an 8-bit field) together with its STM state report (packet STM-15) in the same application message. [¶219](http://localhost:8765/go.html#subset35-219), [¶128-131](http://localhost:8765/go.html#subset58-128)

2. **ERTMS/ETCS on-board validates and responds** — The on-board function compares the received version X against its supported range [¶220-223](http://localhost:8765/go.html#subset35-220):
   - If the STM's version X is **lower** than the lowest supported version: the on-board closes the connection (final disconnection on Safety Layers).
   - If the STM's version X is **among the supported versions**: the on-board responds with the **highest supported FFFIS STM version** whose version number X equals the one received from the STM. Application data transmission is now permitted.
   - If the STM's version X is **higher** than the highest supported version: the on-board closes the connection.

3. **STM validates the response** — The STM checks whether the on-board's version is compatible with its own [¶224-225](http://localhost:8765/go.html#subset35-224):
   - If compatible: the version check is successful. The STM may transmit further application data.
   - If incompatible: the STM closes the connection on Safety Layers.

## Version number structure

The FFFIS STM version number has the format `X.Y.Z`:
- **X** represents the compatibility number (e.g., 4 for Baseline 3). Changes to X indicate a compatibility break.
- **Y** and **Z** represent minor and maintenance revisions that preserve backward compatibility within the same X.

## Multicast connections

For multicast functions (Reference Time, Odometer), the multicast sender opens a separate connection for each FFFIS STM version number defined in the legal backward compatibility envelope. An STM receiving a multicast whose version is incompatible simply ignores the data on that connection. [¶233-237](http://localhost:8765/go.html#subset35-233)

## Legal backward compatibility

The ERTMS/ETCS on-board maintains a **legal backward compatibility envelope** — a defined set of older FFFIS STM version numbers it must support to ensure older STMs remain interoperable with newer on-board equipment. [¶233](http://localhost:8765/go.html#subset35-233)

## Cross-references
- [STM](../entities/stm.md) — the device that initiates the version check
- [STM Control Function](../entities/stm-control-function.md) — the function that enforces version-based STM management
- [FFFIS](fffis.md) — the specification concept requiring version negotiation
- [FFFIS STM Language](fffis-stm-language.md) — the data model for the STM-1 packet used in this handshake
- [STM States](stm-states.md) — the state machine; the version check runs during PO/CO transitions
- [subset35](../summaries/subset35.md) — the FFFIS STM architecture specification
- [subset58](../summaries/subset58.md) — the FFFIS STM Application Layer specification
