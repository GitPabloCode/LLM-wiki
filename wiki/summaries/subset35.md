da# SUBSET-035: ERTMS/ETCS Specific Transmission Module FFFIS

**Source:** [[subset35]] | **Date:** 2025-07-17 | **Type:** summary

SUBSET-035 (v3.2.0, 2015-12-16) defines the Form-Fit-Functional Interface Specification (FFFIS) for the Specific Transmission Module (STM) — the interface between ERTMS/ETCS on-board equipment and National Train Control (NTC) systems (legacy national systems). It specifies all protocol layers from the PROFIBUS physical layer up through the application layer.

## Scope and Purpose

The FFFIS STM enables ERTMS/ETCS on-board equipment to connect to any STM (i.e., interchangeability). The combined ERTMS/ETCS on-board + STM in Level NTC / Mode SN is functionally equivalent to the legacy National Train Control system [subset35 ¶62]-[subset35 ¶68]. Transitions between ETCS and National Systems are seamless using Eurobalises for level transitions.

## Key Architecture

- **Bus:** PROFIBUS (RS-485, 1500 Kbps, up to 200m per segment) [subset35 ¶149]-[subset35 ¶166]
- **Protocol Layers:** Application Layer ([4]), Safe Time Layer ([2]), Safe Link Layer ([3]), PROFIBUS FDL ([5]) [subset35 ¶207]
- **Safety Levels:** SL 4, SL 2, SL 0 — equipment must not implement a higher SL than its SIL [subset35 ¶174]-[subset35 ¶180]

## STM States

Eight states defined: No Power (NP), Power On (PO), Configuration (CO), Data Entry (DE), Cold Standby (CS), Hot Standby (HS), Data Available (DA), and Failure (FA) [subset35 ¶238]-[subset35 ¶287]. The STM transitions through these states under control of the STM Control Function [subset35 ¶342]-[subset35 ¶361].

## ERTMS/ETCS On-Board Functions Accessible to STMs

- **STM Control Function** — state management, version check, data forwarding [subset35 ¶118]-[subset35 ¶130]
- **DMI Function** — driver interaction via default window (buttons, indicators, sounds, text messages, supervision info) [subset35 ¶131]-[subset35 ¶138]
- **TIU Function** — train interface signals (commands: regenerative brake, pantograph, etc.; status: traction, direction, cab) [subset35 ¶101]-[subset35 ¶111]
- **BIU Function** — emergency and service brake commands/status [subset35 ¶112]-[subset35 ¶115]
- **Odometer Function** — estimated speed/distance, confidence intervals [subset35 ¶561]-[§598]
- **Juridical Data Function** — national juridical data recording [subset35 ¶116]-[subset35 ¶117]
- **Reference Time** — common time base for all STMs [subset35 ¶97]-[subset35 ¶98]

## Specific NTC Data Entry

Procedure allowing STMs to request national data from the driver via the DMI, with configurable keyboards, range checks, and timeouts [subset35 ¶423]-[subset35 ¶481].

## Version Management

FFFIS STM versions identified as X.Y where X denotes compatible families. Legal backward compatibility envelope starts at X=4 (introduced with SUBSET-035 v3.x.0, ETCS Baseline 3) [subset35 ¶775]-[subset35 ¶796].

## Level Transitions

Annex A provides informative system diagrams for transitions between ETCS and NTC levels in various modes (SN, NL, SL, Trip) [subset35 ¶797]-[subset35 ¶810].

## Cross-references
- [[stm]] — The Specific Transmission Module entity
- [[stm-control-function]] — Controls STM states and version compatibility
- [[stm-states]] — The eight STM operational states
- [[dmi-function]] — Driver Machine Interface
- [[tiu-function]] — Train Interface Unit
- [[biu-function]] — Brake Interface Unit
- [[odometer-function]] — Odometry data provision
- [[juridical-data-function]] — Juridical recording
- [[profibus]] — The PROFIBUS communication bus
- [[fffis-stm-version-management]] — Version numbering and compatibility
- [[specific-ntc-data-entry]] — National data entry procedure
- [[stm-level-transitions]] — Level transition diagrams
- [[connection-management]] — Connection opening, version check, closing
- [[customisable-dmi]] — Configurable DMI layout service
- [[override-procedure]] — Override (trip inhibition) procedure
