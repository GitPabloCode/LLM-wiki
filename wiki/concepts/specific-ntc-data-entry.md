# Specific NTC Data Entry

**Source:** [[subset35]] | **Date:** 2025-03-13 | **Type:** concept

**Specific NTC Data Entry** is the procedure by which the driver enters national system-specific data required by an STM for operation. It is managed by the STM Control Function [¶424–§476].

## Initiation

- Possible at start-up and during mission [¶430](http://localhost:8765/go.html#subset35-430)
- STM requests data via "Specific NTC Data Need" if data is invalid [¶436](http://localhost:8765/go.html#subset35-436)

## Data Structure

- Each data item has a unique identity: NID_STM + Data Identifier [¶427](http://localhost:8765/go.html#subset35-427)
- Max 15 Data Identifiers per request [¶768–§770]
- Max 20 characters for labels, 10 for values [¶771–§774]

## Procedure

1. When ETCS Train Data is validated and STM is in CO/DE/CS/HS/DA → ERTMS/ETCS on-board sends START flag and ETCS Train Data [¶456–§457]
2. If STM needs data → sends "Specific NTC Data Entry request" [¶466–§467]
3. ERTMS/ETCS on-board manages driver dialogue, range checks (if configured), and transmits validated data [¶431–§432]
4. STM checks data content; if OK → sends "End"; if not → sends request again [¶471–§473]
5. STOP flag sent on completion, timeout (10s), abortion, or skip [¶458–§462]

## Keyboard Options

- Unless dedicated keyboard configured, alphanumeric keyboard is used [¶447](http://localhost:8765/go.html#subset35-447)
- Configurable parameters: window titles, keyboard type (numeric/enhanced numeric/alphanumeric), leading zeros, min/max values for range check [¶448–§453]

## Driver Options

- Driver may skip data entry for an STM [¶435](http://localhost:8765/go.html#subset35-435)
- On receiving "Specific NTC Data Need" in FS, LS, SR, OS, UN, TR, PT, SN → driver is informed [¶443](http://localhost:8765/go.html#subset35-443)
- Info deleted on Train Data entry initiation, STM failure, or isolation [¶444](http://localhost:8765/go.html#subset35-444)

## Cross-references
- [[STM Control Function]] — manages the procedure
- [[Specific Transmission Module (STM)]] — requests and validates data
- [[DMI STM Interface]] — driver interaction channel
- [[subset35]] — source document
