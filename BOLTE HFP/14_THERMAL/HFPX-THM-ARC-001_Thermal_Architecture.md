# Thermal Architecture

**Document ID:** HFPX-THM-ARC-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X thermal architecture structure for Chapter 14.1. This Tranche 6 draft establishes thermal zones, heat-source/sink inventory, and management-approach structure with all values TBD; quantified design follows in later tranches.

## 2. Scope

Covers thermal architecture decomposition: zones, sources/sinks, management approaches, and model ownership hooks. Excludes quantified thermal design, operating instructions, and qualification detail (owned by 14.14 and Vol 22/23). All values TBD.

## 3. Applicable Documents

- HFPX-SYS-ENV-001 Environmental Requirements (parent REQ-HFPX-SYS-006, ENV tier)
- HFPX-SYS-REQ-001 SyRS (REQ-HFPX-SYS-006 environmental policy)
- Vol 04 propulsion, Vol 05 fuel/systems, Vol 06 airframe/aero, Vol 12 pilot interfaces (structure only)
- Vol 19.6 modelling ownership (to follow; no model invoked)

## 4. Definitions & Acronyms

- TAR: thermal architecture requirement tier; ID `REQ-HFPX-TAR-NNN`; verification: Review (intended).
- Thermal zone: bounded region for thermal accounting; boundaries TBD.
- Heat source / heat sink: inventoried thermal contributors; values TBD.
- TBD/TBC: unknown data; no values invented.

## 5. System Context

Thermal architecture refines SYS-006 and the ENV tier into a zone-based structure:

```text
SYS-006 → ENV-001/002 → TAR-001..005 (zones, sources/sinks, approaches) → Subsystem thermal specs (Vol 03–18) → Test correlation (14.14, Vol 22/23)
```

Zone boundaries and inventories require subsystem inputs and programme decisions before any limit is approved.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-TAR-001|The thermal architecture shall define thermal zones with boundaries of [TBD] (boundaries TBD).|REQ-HFPX-SYS-006; REQ-HFPX-ENV-001, REQ-HFPX-ENV-002|Inspection|
|REQ-HFPX-TAR-002|The thermal architecture shall maintain a heat-source and heat-sink inventory of [TBD] with identities and accounting rules TBD (values TBD).|REQ-HFPX-SYS-006; REQ-HFPX-ENV-001|Inspection|
|REQ-HFPX-TAR-003|The system shall apply defined thermal management approaches of [TBD] allocated to zones and subsystems (approaches TBD).|REQ-HFPX-SYS-006; REQ-HFPX-ENV-001, REQ-HFPX-ENV-002|Inspection|
|REQ-HFPX-TAR-004|Thermal models supporting this architecture shall have defined ownership and configuration of [TBD] in Vol 19.6 (ownership TBD).|REQ-HFPX-SYS-006|Inspection|
|REQ-HFPX-TAR-005|Each thermal architecture requirement shall be verified by review of [TBD] with criteria TBD (method detail TBD).|REQ-HFPX-SYS-006|Inspection|

No temperature, heat load, flow rate, or limit is stated or implied; all values are TBD.

## 7. Architecture

Starter allocation (SAD owns authoritative mapping): zones → airframe/propulsion/avionics volumes; sources/sinks → Vol 04/05/06 contributors; approaches → passive/active provisions TBD; models → Vol 19.6 ownership. All TBC pending subsystem specs.

## 8. Detailed Design

Not applicable — architecture level only. Material, routing, and sizing designs live in Vol 03–18 and are TBD.

## 9. Interfaces

Thermal interfaces (conduction/convection/radiation boundaries, coolant paths, instrumentation hooks) are TBD in Chapter 01.16 and Vol 02 ICDs with Vol 04/05/06/12 counterparts. No interface value is approved.

## 10. Operational Concept

Architecture applies across CONOPS ground, flight, and post-flight phases as applicable; phase applicability matrix is TBD. No operating instruction is given in this revision.

## 11. Safety

Thermally induced hazards feed Vol 13 safety analyses (to follow). No architecture element in this revision is a safety claim; safety credit requires analysed and tested limits via change record.

## 12. Performance

Architecture does not quantify performance. Thermal-performance interactions and derating behaviours are TBD and owned jointly with subsystem specs.

## 13. Verification & Validation

Intended method for each requirement is Review (see table); review criteria, artefacts, and entrance/exit conditions are TBD. No verification credit is claimed at this revision.

## 14. Risks

- Zones undefined → subsystem designers assume incompatible boundaries; mitigation: single TBD-owned architecture tier with CONCEPT status.
- Premature sizing to unapproved loads; mitigation: change-controlled quantification only.

## 15. Open Issues

Zone boundary set, source/sink inventory completeness, management-approach selection, and Vol 19.6 model ownership hooks. RTM seed for TAR-001..005 added with this tranche (Status CONCEPT).

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SYS-006 stability, ENV tier, subsystem thermal inputs (Vol 03–18), and Vol 19.6 modelling framework. Changes propagate by change record.

## 18. Traceability

Parents: REQ-HFPX-SYS-006; REQ-HFPX-ENV-001, REQ-HFPX-ENV-002 (see table). Children: subsystem thermal specs (Vol 03–18), thermal test cases (14.14, Vol 22/23), RTM rows. RTM seed for TAR-001..005 added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Quantification requires new revisions via change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 14.1; all values TBD) |
