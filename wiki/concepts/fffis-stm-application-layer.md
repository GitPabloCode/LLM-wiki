# FFFIS STM Application Layer

**Source:** [[subset58]] | **Date:** 2025-07-17 | **Type:** concept

The FFFIS STM Application Layer is the highest protocol layer in the FFFIS STM communication stack, defining the data formats (variables, packets, messages) used between STMs and ERTMS/ETCS on-board functions over [[profibus]].

## Protocol Stack Position

The Application Layer sits above the Safe Time Layer (SUBSET-056), which itself sits above the Safe Link Layer (SUBSET-057) and PROFIBUS FDL. [subset58 ¶44]-[subset58 ¶48]

## Three-Level Language Structure

The language is organised hierarchically [subset58 ¶57]:

### 1. Variables

Single data values with unique names and defined encodings. Variable naming prefixes indicate semantics [subset58 ¶68]-[subset58 ¶85]:

| Prefix | Meaning | Examples |
|--------|---------|---------|
| A_ | Acceleration | A_NVMAXREDADH1 |
| D_ | Distance | D_EST, D_MAX, D_MIN, D_TARGET |
| G_ | Gradient | — |
| L_ | Length | L_MESSAGE, L_PACKET, L_TEXT |
| M_ | Miscellaneous | M_MODE, M_BUT_ATTRIB, M_BRAKE_PERCENTAGE_STM |
| N_ | Number | N_ITER, N_LITER, N_VERMAJOR |
| NC_ | Class Number | NC_TRAIN, NC_CDTRAIN |
| NID_ | Identity Number | NID_PACKET, NID_STM, NID_BUTTON |
| Q_ | Qualifier | Q_SCALE, Q_ACK, Q_OVR_STATUS |
| T_ | Time/Date | T_ODO, T_JD, T_BUTTONEVENT |
| V_ | Speed | V_EST, V_MAX, V_PERMIT, V_TARGET |
| X_ | Text | X_CAPTION, X_TEXT, X_VALUE |

**Encoding rules** [subset58 ¶60]-[subset58 ¶70]:
- Signed values are 2's complement
- Boolean uses 0=false, 1=true
- Offsets for numerical values are avoided (0 = 0, 1 = 1)
- MSB transmitted first
- Reserved/spare values must not be used

### 2. Packets

Groups of variables forming a single unit with defined internal structure [subset58 ¶87]-[subset58 ¶88]:

```
| NID_PACKET (8 bits) | L_PACKET (13 bits) | Q_SCALE (2 bits, optional) | Other variables |
```

- **NID_PACKET**: Unique packet identifier (0-199 standard, 200-255 supplier-specific) [subset58 ¶375]
- **L_PACKET**: Total packet length in bits (max 1888) [subset58 ¶251]
- **Q_SCALE**: Distance scale for distance variables in the packet
- **Iterations**: Two nested levels supported via N_ITER and N_LITER variables [subset58 ¶94]-[subset58 ¶98]
- Optional variables are indented and depend on prior qualifier values [subset58 ¶104]
- Packet length must fit within one message [subset58 ¶93]

### 3. Messages

The complete application data unit transmitted at one time [subset58 ¶107]:

```
| NID_STM (8 bits) | L_MESSAGE (8 bits) | Packet 1 | ... | Packet N | Padding (0-7 bits) |
```

- **Message Header**: NID_STM identifies the STM; L_MESSAGE is total length in bytes (5-238) [subset58 ¶112]-[subset58 ¶113]
- **Body**: One or more packets (see exception rules below) [subset58 ¶116]
- **Padding**: 0-7 bits for byte alignment through safety layers [subset58 ¶124]
- Messages are transmitted chronologically (oldest first) [subset58 ¶110]

## Multiple Packet Instance Exceptions

It is forbidden to send multiple instances of the same packet type in one message, with four exceptions where multiple instances are allowed [subset58 ¶117]-[subset58 ¶121]:
1. STM-45 (ETCS airgap message for STM)
2. STM-38 (Text message)
3. STM-39 (Delete text message)
4. STM-161 (STM information to Juridical Data Function)

## Non-Standard Packets

Packets with NID_PACKET 200-255 are supplier-specific (non-standard). If a receiver receives a non-standard packet it does not recognise, it shall ignore the packet but must not reject the entire message. [subset58 ¶125]

## Cross-references
- [[subset58]] — The source document defining the Application Layer
- [[subset35]] — FFFIS STM system-level specification
- [[stm]] — The Specific Transmission Module
- [[profibus]] — The underlying communication bus
- [[fffis-stm-version-management]] — Version numbering
