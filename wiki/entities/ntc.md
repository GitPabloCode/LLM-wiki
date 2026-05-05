# NTC (National Train Control)

**Source:** [subset35](../summaries/subset35.md) | **Date:** 2026-04-29 | **Type:** entity

A **National Train Control (NTC)** is a legacy national train protection or automatic train control system that predates ERTMS/ETCS. Examples include KVB (France), ATB (Netherlands), AWS/TPWS (UK), and others. The FFFIS STM allows these systems to interoperate with the ERTMS/ETCS on-board by connecting through a Specific Transmission Module (STM).

## Identification

Each NTC system is identified by a **NID_NTC** value, assigned in the ERA_ERTMS_040001 document. An STM providing access to a given NTC uses this NID_NTC value as its NID_STM. [¶76](http://localhost:8765/go.html#subset35-76)

## Level NTC X and Mode SN

When the ERTMS/ETCS on-board operates in a national system, it enters **Level NTC X** (where X identifies the specific national system) and **mode SN** (National System mode). In this configuration, the corresponding STM is in the Data Available (DA) state and is responsible for supervising train movement using its national trackside infrastructure. [¶66-68](http://localhost:8765/go.html#subset35-66)

## Level transitions

Transitions between ETCS and NTC systems use Eurobalises as transition markers. The FFFIS STM specification requires that these transitions be seamless, with no additional trackside equipment beyond the Eurobalises already used for ETCS. Transitions include: ETCS→NTC, NTC→ETCS, NTC X→NTC Y, and power-on scenarios within Level NTC. [¶68](http://localhost:8765/go.html#subset35-68) [¶56-58](http://localhost:8765/go.html#subset35-56)

## Specific NTC Data

National systems often require data specific to their operation (e.g., train numbers, driver credentials, route information). This **Specific NTC Data** is obtained by the STM through the Specific NTC Data Entry procedure during the Data Entry (DE) state. [¶120](http://localhost:8765/go.html#subset35-120) [¶263-268](http://localhost:8765/go.html#subset35-263)

## Cross-references
- [STM (Specific Transmission Module)](stm.md) — the device that connects an NTC to the ERTMS/ETCS on-board
- [STM Control Function](stm-control-function.md) — manages level transitions involving NTCs
- [STM States](../concepts/stm-states.md) — the lifecycle, including states specific to NTC operation
- [subset35](../summaries/subset35.md) — the FFFIS STM specification
