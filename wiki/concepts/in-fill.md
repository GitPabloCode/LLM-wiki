# In-fill

**Source:** [[subset40]] | **Date:** 2026-05-07 | **Type:** concept

**In-fill** is supplementary information transmitted to a train (via balise group, loop, or radio) that updates or extends a previously received Movement Authority. It allows the train to receive revised movement data without a full new MA.

## Rules from SUBSET-040

- In-fill location reference must be in rear of current EOA [¶84](http://localhost:8765/go.html#subset40-84).
- In-fill information is limited to: in-fill MA, linking, and route-related track description [¶113](http://localhost:8765/go.html#subset40-113).
- Permitted packets for in-fill: 136, 12, 80, 49, 21, 27, 51, 65/66, 70, 5, 41, 44, 39, 67, 68, 71, 133 [¶113](http://localhost:8765/go.html#subset40-113).
- For immediate level transition in in-fill, **D_LEVELTR = 0 m** [¶116](http://localhost:8765/go.html#subset40-116).
- Unlinked groups shall not transmit linking unless as in-fill [¶131](http://localhost:8765/go.html#subset40-131).

## Cross-references
- [[Level Transition]] — level transitions can be performed via in-fill
- [[Balise Group]] — in-fill can be provided by balise groups
- [[Euroloop]] — in-fill can be provided by loops
- [[RBC]] — in-fill can be provided by radio
- [[Linking]] — linking data in in-fill
- [[EOA]] — in-fill reference position relative to EOA
- [[subset40]] — source document
