# Pilot Interface

**Document ID:** HFPX-HUM-PIF-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define pilot-interface requirements for HFP-X (Chapter 12.13). This Tranche 6 draft establishes interface-inventory, labelling/consistency, and evaluation placeholders; all values are TBD.

## 2. Scope

Covers pilot-interface inventory, labelling and consistency provisions, and interface evaluation methods. Excludes pilot-controls functional design (12.6), HMI detailed design (Vol 10), and training detail (Vol 30 hooks).

## 3. Applicable Documents

- HFPX-SYS-HUM-001 Human Factors Requirements (parent HUM tier)
- Stakeholder need STK-002 (human involvement)
- HSA tier (ID TBD — allocation to follow)
- Vol 30 hooks (TBD — evaluation inputs to follow)
- Vol 10 HMI (TBD detail), HFPX-HUM-CTL-001 (Chapter 12.6)

## 4. Definitions & Acronyms

- HUM: human-factors requirement tier; IDs `REQ-HFPX-HUM-NNN`.
- UPI: pilot-interface requirement tier; IDs `REQ-HFPX-UPI-NNN`; verification TBD.
- TBD/TBC: unknown data; no values invented.

## 5. System Context

Pilot interface refines system-level interface needs into testable placeholders:

```text
STK-002 + HUM tier → UPI-001..004 → control / display / labelling detail (Vol 10) → V&V cases
```

No interface layout, label, or criterion is approved at this revision.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-UPI-001|The system shall provide a defined pilot-interface inventory covering controls, displays, and alerts (interface inventory TBD).|STK-002, REQ-HFPX-HUM-002, HSA tier (ID TBD)|Demonstration|
|REQ-HFPX-UPI-002|Pilot interfaces shall follow defined labelling and consistency provisions (labelling/consistency TBD).|STK-002, REQ-HFPX-HUM-002, HSA tier (ID TBD)|Inspection|
|REQ-HFPX-UPI-003|The system shall define the pilot-interface evaluation method, including tasks and conditions (evaluation TBD).|STK-002, REQ-HFPX-HUM-001, HSA tier (ID TBD)|Inspection|
|REQ-HFPX-UPI-004|Interface provisions shall be verified against defined criteria (criteria TBD; Vol 30 hook TBD).|STK-002, REQ-HFPX-HUM-002, HSA tier (ID TBD)|Inspection|

All inventories, provisions, methods, and criteria are TBD. No value is approved.

## 7. Architecture

Starter allocation (SAD owns authoritative mapping): UPI-001/002 → pilot controls/displays with Vol 10 detail; UPI-003/004 → evaluation and V&V framework with Vol 30 hooks. All TBC.

## 8. Detailed Design

Not applicable — requirements level only. Layouts, symbology, labels, and hardware selection are TBD in Vol 10 and follow-on revisions.

## 9. Interfaces

Pilot-interface provisions are TBD in Vol 02 ICDs, Vol 10, and Chapter 12.1 register. No interface value or layout is approved.

## 10. Operational Concept

Interface requirements apply across preparation, flight, emergency, and recovery phases; phase-specific applicability is TBD. Unmanned demonstration precedes any crewed evaluation per safety gating.

## 11. Safety

Interface confusion or error-inducing provisions feed Vol 13 safety and Vol 30 error analyses (to follow). No UPI requirement confers flight approval; human flight remains gated by tier 01.10 and the Safety Case.

## 12. Performance

No UPI requirement quantifies performance. All interface measures are TBD pending Vol 10/30 studies.

## 13. Verification & Validation

Each requirement states its method above as TBD; verification IDs, task scenarios, participant criteria, and pass thresholds are TBD in the V&V Plan (Vol 22) with Vol 10/12/30 inputs. No interface credit is claimed at this revision.

## 14. Risks

- Interface inventory undefined → late functional gaps; mitigation: early UPI-001 placeholder plus review gates.
- Consistency provisions undefined → error-prone interfaces; mitigation: UPI-002 placeholder plus evaluation gates.

## 15. Open Issues

TBD: interface inventory, labelling/consistency provisions, evaluation method, and verification criteria pending Vol 10, HSA-tier, and Vol 30 inputs.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on STK-002 stability, HUM-tier stability (HFPX-SYS-HUM-001), HSA-tier allocation (TBD), Vol 30 hooks (TBD), Vol 10 HMI work, Chapter 12.6 control inputs, and V&V Plan cases. Changes propagate by change record.

## 18. Traceability

Parents: STK-002, HUM tier (REQ-HFPX-HUM-001, REQ-HFPX-HUM-002), HSA tier (ID TBD), Vol 30 hooks (TBD) — see table. Children: interface specs, Vol 10 detail specs, evaluation specs, V&V cases, RTM rows. RTM seed for UPI-001..004 added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Additions or inventory changes require new revisions via change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 12.13) |
