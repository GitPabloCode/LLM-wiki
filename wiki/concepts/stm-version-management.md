# STM Version Management

**Source:** [[subset35]] | **Date:** 2025-03-13 | **Type:** concept

**STM Version Management** defines the version numbering scheme for the FFFIS STM interface to ensure compatibility across different releases [¶776–§796].

## Version Format

- Format: **X.Y** where X and Y range from 0 to 255 [¶782](http://localhost:8765/go.html#subset35-782)
- **X** — Distinguishes incompatible versions (changes when backward compatibility is broken) [¶783](http://localhost:8765/go.html#subset35-783)
- **Y** — Indicates compatibility within the same X (functional evolution) [¶784–§785]
- Incremented when functionality changes [¶787](http://localhost:8765/go.html#subset35-787)

## Version Table

| X | Y | Description |
|---|---|---|
| 2 | 0 | Supplier specific [¶790](http://localhost:8765/go.html#subset35-790) |
| 3 | 0 | Supplier specific (from v2.1.1) [¶790](http://localhost:8765/go.html#subset35-790) |
| 4 | 0 | Legal backward compatibility envelope (from v3.x.0 for ETCS baseline 3) [¶790](http://localhost:8765/go.html#subset35-790) |

## Backward Compatibility Envelope

- STM supports and sends the highest version in the envelope [¶791](http://localhost:8765/go.html#subset35-791)
- ERTMS/ETCS on-board supports any version in the envelope [¶792](http://localhost:8765/go.html#subset35-792)
- All nodes support the same version numbers [¶793](http://localhost:8765/go.html#subset35-793)
- For lower X values, corresponding requirements from section 16.4 apply [¶794](http://localhost:8765/go.html#subset35-794)
- The version in this document is the starting point of the envelope; support for lower X is supplier specific [¶796](http://localhost:8765/go.html#subset35-796)

## Cross-references
- [[STM Connection Management]] — uses version numbers in connection setup
- [[Specific Transmission Module (STM)]] — implements version management
- [[subset35]] — source document
