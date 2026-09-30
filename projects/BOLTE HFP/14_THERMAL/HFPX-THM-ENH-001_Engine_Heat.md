# Engine Heat

**Document ID:** HFPX-THM-ENH-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X engine-heat structure for Chapter 14.2. This Tranche 6 draft establishes heat-rejection paths, affected structures, and limit structure with all values TBD; quantified design follows in later tranches.

## 2. Scope

Analysis, modelling, and test methodology only. Covers engine-heat rejection paths, affected structures, and thermal limit structure. Provides no operating instructions. Excludes exhaust-plume detail (14.3) and qualification detail (14.14, Vol 22/23). All values TBD.

## 3. Applicable Documents

- HFPX-SYS-ENV-001 Environmental Requirements (parent REQ-HFPX-SYS-006, ENV tier)
- HFPX-SYS-REQ-001 SyRS (REQ-HFPX-SYS-006 environmental policy)
- Vol 03.19 structures, Vol 04 propulsion (structure only; no values invoked)
- Vol 19.6 modelling framework (to follow)

## 4. Definitions & Acronyms

- TEH: engine-heat requirement tier; ID `REQ-HFPX-TEH-NNN`; verification: Model + Test (intended).
- Heat-rejection path: conduction/convection/radiation route from engine sources; paths TBD.
- TBD/TBC: unknown data; no values invented.

## 5. System Context

Engine-heat tier refines SYS-006 and ENV-001 into analysable paths and interfaces:

```text
SYS-006 → ENV-001 → TEH-001..004 (paths, structures, limits) → Vol 03/04 thermal design → Model correlation + test (14.14, Vol 22/23)
```

Path inventories and limits require models, surveys, and programme decisions before any value is approved.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-TEH-001 | The system shall define engine heat-rejection paths of [TBD] with path inventory and accounting rules TBD (values TBD). | REQ-HFPX-SYS-006; REQ-HFPX-ENV-001 | Model + Test |
| REQ-HFPX-TEH-002 | The system shall identify engine-heat-affected structures of [TBD] with interfaces to Vol 03.19 TBD (identities TBD). | REQ-HFPX-SYS-006; REQ-HFPX-ENV-001 | Model + Test |
| REQ-HFPX-TEH-003 | The system shall operate within defined engine-heat thermal limits of [TBD] (limits TBD). | REQ-HFPX-SYS-006; REQ-HFPX-ENV-001 | Model + Test |
| REQ-HFPX-TEH-004 | Each engine-heat requirement shall be verified by model of [TBD] and test of [TBD] with correlation criteria TBD (detail TBD). | REQ-HFPX-SYS-006 | Model + Test |

Scope note: analysis, modelling, and test methodology only; no operating instruction is given. No temperature, heat load, flow rate, or limit is stated or implied; all values are TBD.

## 7. Architecture

Starter allocation (SAD owns authoritative mapping): paths → engine bay/airframe conduction and convection routes TBD; affected structures → Vol 03.19 mapping TBD; limits → zone allocation TBD. All TBC pending subsystem specs and models.

## 8. Detailed Design

Not applicable — structure level only. Shields, insulation, routing, and sizing designs live in Vol 03/04 and are TBD.

## 9. Interfaces

Engine-heat interfaces (mounts, bay boundaries, Vol 03.19 structural interfaces, Vol 04 propulsion interfaces) are TBD in Chapter 01.16 and Vol 02 ICDs. No interface value is approved.

## 10. Operational Concept

Requirements apply across CONOPS phases as applicable; phase applicability matrix is TBD. No operating instruction is given in this revision.

## 11. Safety

Engine-heat-induced hazards feed Vol 13 safety analyses (to follow). No limit in this revision is a safety claim; safety credit requires analysed and tested limits via change record.

## 12. Performance

Engine-heat limits do not quantify performance. Derating and performance interactions under thermal stress are TBD and owned jointly with propulsion and performance tiers.

## 13. Verification & Validation

Intended method for each requirement is Model + Test (see table); model fidelity, test conditions, and pass criteria are TBD in 14.14 and the V&V Plan (Vol 22). No verification credit is claimed at this revision.

## 14. Risks

- Paths undefined → incompatible shielding/sizing assumptions; mitigation: single TBD-owned tier with CONCEPT status.
- Testing to unapproved levels; mitigation: change-controlled quantification only.

## 15. Open Issues

Path inventory completeness, Vol 03.19 affected-structure mapping, limit definition, and model-plus-test correlation approach. RTM seed for TEH-001..004 added with this tranche (Status CONCEPT).

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SYS-006 stability, ENV tier, Vol 03/04 thermal inputs, Vol 19.6 models, and 14.14 test thread. Changes propagate by change record.

## 18. Traceability

Parents: REQ-HFPX-SYS-006; REQ-HFPX-ENV-001 (see table). Children: Vol 03/04 thermal designs, test cases (14.14, Vol 22/23), RTM rows. RTM seed for TEH-001..004 added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Quantification requires new revisions via change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 14.2; all values TBD) |
