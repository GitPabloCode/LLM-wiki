# DMI STM Interface

**Source:** [[subset35]] | **Date:** 2025-03-13 | **Type:** entity

The **DMI (Driver-Machine Interface) STM Interface** allows the active STM to communicate with the driver through the ERTMS/ETCS on-board DMI, providing national system information in the default window [¶131–§138, §600–§601].

## Principles

- Only the active STM communicates with the driver [¶607](http://localhost:8765/go.html#subset35-607)
- On loss of active status → all DMI objects are deleted [¶608](http://localhost:8765/go.html#subset35-608)
- On DMI connection disconnection → objects deleted after 2s timeout [¶609–§611]
- Up to 4 DMI channels, each with one connection [¶617–§618]
- At most one channel is active at a time [¶619](http://localhost:8765/go.html#subset35-619)

## DMI Objects

- **Text Messages** — Up to 40 characters (UTF-8), with colour, background, flashing mode attributes; optional acknowledgement request [¶637–§644, §761]
- **Indicators** — Display-only elements with icon, caption, position, display attribute [¶646–§655]
- **Buttons** — Functional extension of indicators; push and release events transmitted with Reference Time timestamp [¶656–§660]
- **Sounds** — Sequence of segments (duration, frequency); continuous/one-shot/stop; two simultaneous STM sound requests managed [¶661–§670]
- **Supervision Information** — Speed/distance values (Permitted Speed, Target Speed, Target Distance, Release Speed, Intervention Speed) and colours/display modes [¶671–§699]

## Services

Two DMI service types exist [¶602–§605]:
- **Unified DMI Service** — STM provides no configuration data; uses standard ETCS layout areas [¶604](http://localhost:8765/go.html#subset35-604)
- **Customisable DMI Service** — STM provides configuration data stored in ERTMS/ETCS on-board for custom layouts, icons, sounds, and positions [¶603, §700–§753]

## Cross-references
- [[Specific Transmission Module (STM)]] — communicates via this interface
- [[STM Control Function]] — manages DMI channels
- [[PROFIBUS (STM Interface)]] — DMI uses SAPs 000000, 000001, 000100, 000101
- [[STM Customisable DMI Service]] — configuration details
- [[subset35]] — source document
