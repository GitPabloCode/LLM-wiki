# Specific NTC Data Entry

**Source:** [subset58](../summaries/subset58.md) | **Date:** 2026-04-29 | **Type:** concept

The **Specific NTC Data Entry** procedure is a structured handshake between a Specific Transmission Module (STM) and the ERTMS/ETCS on-board's STM Control Function that allows the driver to enter national-specific operational data required by the legacy National Train Control (NTC) system. Examples include train numbers, driver IDs, route codes, or other data that ETCS does not natively handle. The procedure runs during the **Data Entry (DE)** state of the STM startup lifecycle. [¶263-268]

## Six-packet handshake

The procedure uses six dedicated application-layer packets, defined in SUBSET-058 [¶16-20]:

### Step 1: STM declares need
**STM-181 (Specific NTC Data Need)** — STM to STM Control Function. Sent in PO state. Indicates whether the STM requires Specific NTC Data at all. If no data is needed, the DE state is skipped and the STM proceeds directly to Cold Standby. [¶258]

### Step 2: STM requests data fields
**STM-179 (Specific NTC Data Entry request)** — STM to STM Control Function. Describes which data fields the national system needs the driver to fill in, specifying the layout, captions, and expected format of each entry.

### Step 3: ETCS relays driver input values
**STM-180 (Specific NTC Data values)** — STM Control Function to STM. Carries the actual values entered by the driver through the DMI, corresponding to the fields requested in STM-179.

### Step 4: STM requests display of entered data
**STM-182 (Request for Specific NTC Data View values)** — STM to STM Control Function. After receiving and validating the entered data, the STM may request that a summary be displayed to the driver for confirmation.

### Step 5: ETCS displays the view
**STM-183 (Specific NTC Data View values)** — STM Control Function to STM. Provides the formatted data view for the driver's confirmation on the DMI.

### Step 6: STM signals completion
**STM-184 (Specific NTC Data Entry flag)** — STM to STM Control Function. Indicates that the data entry procedure is complete (or has been skipped/aborted). After sending this, the STM requests transition to Cold Standby (CS) state. [¶267]

## Lifecycle context

The DE state is entered only once per STM startup, during the initial transition from Configuration (CO) state. Once the procedure terminates — successfully or not — the STM always transitions to CS. If Specific NTC Data is invalid or the procedure is skipped, the CS state is still entered to maintain uniform system behaviour. [¶265, 268]

## Cross-references
- [FFFIS STM Language](fffis-stm-language.md) — the variables/packets/messages model used by these packets
- [STM States](stm-states.md) — the lifecycle states (DE state in particular)
- [STM](../entities/stm.md) — the device that drives this procedure
- [NTC](../entities/ntc.md) — the national system whose data is being entered
- [STM Control Function](../entities/stm-control-function.md) — the on-board function that brokers the data exchange
- [subset58](../summaries/subset58.md) — the FFFIS STM Application Layer specification
- [subset35](../summaries/subset35.md) — the FFFIS STM architecture specification
