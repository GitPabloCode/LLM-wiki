# Data Dimensioning

**Source:** [[subset40]] | **Date:** 2026-05-07 | **Type:** concept

**Data dimensioning** refers to the limits on the number of iterations (occurrences) permitted in a single ETCS packet and the minimum number the onboard system must memorise. These rules ensure interoperability between different manufacturers' equipment.

## General Rule (§4.3)

If engineering rules limit iterations below the SRS maximum of **31** (from SUBSET-026 ch.7), the engineering rule takes precedence [¶146](http://localhost:8765/go.html#subset40-146).

## Dimensioning Table

| Data Element | Max Iterations in 1 Packet | Min Memorised Onboard |
|---|---|---|
| MA sections (excl. End Section) | **5** | **6** [¶151](http://localhost:8765/go.html#subset40-151) |
| Balise IDs for SR/shunting | **15** | N/A [¶153](http://localhost:8765/go.html#subset40-153) |
| Mode profile sections | **2** | N/A [¶155](http://localhost:8765/go.html#subset40-155) |
| SSP change locations | **31** | **50** [¶157](http://localhost:8765/go.html#subset40-157) |
| TSR | **10 packets** | **30** [¶159](http://localhost:8765/go.html#subset40-159) |
| Gradient changes | **31** | **50** [¶161](http://localhost:8765/go.html#subset40-161) |
| Position report locations | **15** (new packet 58) | N/A [¶163](http://localhost:8765/go.html#subset40-163) |
| Text messages | **1 plain + 1 fixed** | **5 plain + 5 fixed** [¶165](http://localhost:8765/go.html#subset40-165) |
| Linked balise groups | **29** | **30** (except in-fill) [¶167](http://localhost:8765/go.html#subset40-167) |
| TC change of traction power | **No iteration** | **1** [¶169](http://localhost:8765/go.html#subset40-169) |
| TC big metal masses | **4** | **5** [¶171](http://localhost:8765/go.html#subset40-171) |
| TC | **19** | **20** [¶173](http://localhost:8765/go.html#subset40-173) |
| Route suitability data | **2** | **3** (max one per type) [¶175](http://localhost:8765/go.html#subset40-175) |
| Train categories per SSP segment | **15** | N/A [¶177](http://localhost:8765/go.html#subset40-177) |
| Axle load speed profile segments | **14** | **30** [¶179](http://localhost:8765/go.html#subset40-179) |
| Axle load speed restriction values per segment | **3** | N/A [¶181](http://localhost:8765/go.html#subset40-181) |
| Adhesion profiles | **No iteration** | **10** [¶183](http://localhost:8765/go.html#subset40-183) |
| Reversing area | **No iteration** | **1** [¶185](http://localhost:8765/go.html#subset40-185) |

## Multiple Packet Instances

Must respect SUBSET-026 §8.4.1.4 [¶188](http://localhost:8765/go.html#subset40-188).

## Cross-references
- [[Linking]] — linked group dimensioning (29/30)
- [[Track Conditions]] — TC dimensioning rules
- [[Message Dimensioning]] — radio message size limits
- [[subset40]] — source document
