# Euroradio FFFIS (ERTMS/ETCS Language)

**Source:** [[subset26]] | **Date:** 2025-07-17 | **Type:** concept

The ERTMS/ETCS Language is the set of variables, packets, messages, and telegrams used to transmit information over radio (Euroradio), balise (Eurobalise), and loop (Euroloop) airgaps. It is defined in Chapters 7 and 8 of SUBSET-026. [subset26 ¶5072][subset26 ¶5073]

## Variables

Variables encode single data values and cannot be split. Each variable has one type and meaning. [subset26 ¶5076]

**Prefix conventions** [subset26 ¶5088][subset26 ¶5103]:
- A_ = acceleration (e.g., A_NVP12)
- D_ = distance (e.g., D_GRADIENT, D_LEVELTR)
- G_ = gradient (e.g., G_A)
- L_ = length (e.g., L_SECTION, L_TRAIN)
- M_ = miscellaneous (e.g., M_MODE, M_VERSION)
- N_ = number (e.g., N_ITER)
- NID_ = identity number (e.g., NID_RBC, NID_BG)
- Q_ = qualifier (e.g., Q_DIR, Q_SCALE)
- T_ = time/date (e.g., T_TRAIN, T_SECTIONTIMER)
- V_ = speed (e.g., V_MAIN, V_STATIC)
- X_ = text (e.g., X_TEXT)

## Packets

Packets group multiple variables into a single unit. Each packet has [subset26 ¶5106][subset26 ¶5109]:
- **NID_PACKET** — packet identifier
- **Q_DIR** — validity direction (track-to-train only)
- **L_PACKET** — length in bits
- **Q_SCALE** — distance scale (optional)
- **Information section** — the actual data

Over 50 packet types are defined for track-to-train communication (e.g., Linking, MA, Gradient, SSP, TSR, Mode Profile) and over 10 for train-to-track (e.g., Position Report, Train Data, Error Reporting). [subset26 ¶5123]

## Messages

Messages are transmitted over Euroradio. Track-to-train radio messages include a header (NID_MESSAGE, L_MESSAGE, T_TRAIN, M_ACK, NID_LRBG) followed by packets. Train-to-track messages include a header (NID_MESSAGE, L_MESSAGE, T_TRAIN, NID_ENGINE) followed by packets. [subset26 ¶5930][subset26 ¶5938]

**Key messages**:
- Message 3: Movement Authority [subset26 ¶6002]
- Message 15: Conditional Emergency Stop [subset26 ¶6010]
- Message 129: Validated Train Data [subset26 ¶5959]
- Message 136: Train Position Report [subset26 ¶5966]

## Eurobalise Telegrams

The Eurobalise telegram format has a 50-bit header (Q_UPDOWN, M_VERSION, Q_MEDIA, N_PIG, N_TOTAL, M_DUP, M_MCOUNT, NID_C, NID_BG, Q_LINK) followed by optional packets and Packet 255 (End of Information). [subset26 ¶5899]

## Cross-references
- [[euroradio]] — The protocol using this language
- [[eurobalise]] — Uses telegram format
- [[euroloop]] — Uses message format
- [[rbc]] — Sends/receives messages
- [[ertms-etcs-on-board-equipment]] — Processes the language
