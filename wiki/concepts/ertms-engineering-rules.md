# ERTMS Engineering Rules

**Source:** [subset40](../summaries/subset40.md) | **Date:** 2026-04-29 | **Type:** concept

**Engineering rules** are system-related limitations for the installation of equipment and exchange of information that characterise the implementation of ERTMS/ETCS subsystems. They form a mandatory layer of constraints sitting between the System Requirements Specification (SRS) and project-specific implementation rules, ensuring that any compliant train can operate on any compliant infrastructure. [¶30-32]

## Relationship to the SRS

Engineering rules provide **additional constraints** to the SRS and sub-level documents (FFFIS, FFFS), not divergent requirements. They are complementary — they tighten where the SRS leaves flexibility for interoperability reasons, but never contradict it. References to the SRS are not exhaustive; a rule may apply even where the SRS is silent on the topic. [¶31-32]

## Scope and limits

The engineering rules do not define the entire set of rules needed for a real project. Additional rules dictated by project constraints, client requirements, or industry procedures may be needed — but those additions must not preclude the use of any equipment that meets the engineering rules stated in Subset-040. [¶33-34]

The rules are mandatory, not advisory. Engineering advice is explicitly out of scope. [¶35]

## Categories of rules

Subset-040 organises rules into three major categories:

### Installation rules
Physical positioning and environment constraints for trackside equipment: balises, Eurobalise antennas, Euroloops, and level transition / RBC handover borders. These govern spatial relationships (minimum distances, maximum gaps, angular tolerances) between infrastructure elements. [¶56-99]

### Telegram and message rules
Content and format constraints on transmitted data: balise telegram sizes by speed range, maximum radio message lengths, in-fill content restrictions, data type-specific rules (mode profiles, track conditions, linking, level transitions, text transmission). [¶100-142]

### Dimensioning rules
Quantitative limits on data volume: maximum N_ITER per packet for each ETCS packet type (trackside transmission constraint) and the corresponding minimum memorised values on-board (train storage requirement). Also covers data flow constraints like minimum position report intervals. [¶143-191]

## Non-ERTMS systems

For transmission systems other than ERTMS/ETCS (e.g., KER-compatible national systems), Subset-040 provides an appendix with additional rules. These are not required for ERTMS interoperability but apply to equipment offering KER compatibility. [¶192-195]

## Cross-references
- [Balise Installation](balise-installation.md) — the installation rules subset
- [ERTMS Dimensioning](ertms-dimensioning.md) — the data dimensioning subset
- [FFFIS](fffis.md) — the FFFIS specification concept these rules constrain
- [STM](../entities/stm.md) — STMs are referenced in level transition engineering rules
- [subset40](../summaries/subset40.md) — the Dimensioning and Engineering Rules specification
