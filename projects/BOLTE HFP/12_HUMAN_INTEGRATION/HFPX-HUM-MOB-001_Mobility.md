# Mobility

**Document ID:** HFPX-HUM-MOB-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define mobility requirements for HFP-X pilot integration (Chapter 12.10). This Tranche 6 draft establishes mobility-need, suit-joint, and ground-handling placeholders; all values are TBD.

## 2. Scope

Covers suited pilot mobility needs including ankle-module articulation, suit-joint provisions, and ground-handling provisions. Excludes load-distribution detail (12.4), fatigue detail (12.11), and ground-operations design, which is operations/Vol scope TBD.

## 3. Applicable Documents

- HFPX-SYS-HUM-001 Human Factors Requirements (parent HUM tier)
- Stakeholder need STK-002 (human involvement)
- HSA tier (ID TBD — allocation to follow)
- Vol 30 hooks (TBD — training/evaluation inputs to follow)
- HFPX-HUM-ARC-001 (Chapter 12.1), HFPX-HUM-ERG-001 (Chapter 12.5)

## 4. Definitions & Acronyms

- HUM: human-factors requirement tier; IDs `REQ-HFPX-HUM-NNN`.
- UMO: mobility requirement tier; IDs `REQ-HFPX-UMO-NNN`; verification TBD.
- TBD/TBC: unknown data; no values invented.

## 5. System Context

Mobility refines system-level accommodation needs into testable placeholders:

```text
STK-002 + HUM tier → UMO-001..004 → suit-joint / station / handling detail → V&V cases
```

No mobility range, joint, or handling value is approved at this revision.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-UMO-001|The system shall support defined suited mobility needs across defined tasks and phases, including ankle-module articulation (mobility needs TBD).|STK-002, REQ-HFPX-HUM-003, HSA tier (ID TBD)|Inspection|
|REQ-HFPX-UMO-002|The suit shall provide joint provisions supporting defined mobility needs (suit-joint provisions TBD).|STK-002, REQ-HFPX-HUM-003, HSA tier (ID TBD)|Inspection|
|REQ-HFPX-UMO-003|The system shall support ground-handling tasks in defined suited configurations (ground-handling provisions TBD).|STK-002, REQ-HFPX-HUM-003, HSA tier (ID TBD)|Inspection|
|REQ-HFPX-UMO-004|Mobility provisions shall be verified against defined criteria (criteria TBD; Vol 30 hook TBD).|STK-002, REQ-HFPX-HUM-003, HSA tier (ID TBD)|Inspection|

All mobility needs, joint provisions, handling provisions, and criteria are TBD. No value is approved.

## 7. Architecture

Starter allocation (SAD owns authoritative mapping): UMO-001/002 → suit joints including ankle-module articulation and station provisions; UMO-003 → ground-handling provisions and procedures; UMO-004 → V&V framework with Vol 30 hooks. All TBC.

## 8. Detailed Design

Not applicable — requirements level only. Joint designs, ranges, and handling aids are TBD in follow-on revisions.

## 9. Interfaces

Mobility interfaces (suit joints, station ingress/egress provisions, ground-handling interfaces) are TBD in Vol 02 ICDs and Chapter 12.1 register. No interface value or layout is approved.

## 10. Operational Concept

Mobility requirements apply across donning, ingress, ground handling, flight, egress, and doffing phases; phase-specific applicability is TBD. Unmanned demonstration precedes any crewed evaluation per safety gating.

## 11. Safety

Mobility shortfalls affecting ingress, egress, or emergency handling feed Vol 13 safety analyses (to follow). No UMO requirement confers flight approval; human flight remains gated by tier 01.10 and the Safety Case.

## 12. Performance

No UMO requirement quantifies performance. All mobility measures are TBD pending follow-on studies.

## 13. Verification & Validation

Each requirement states its method above as TBD; verification IDs, task scenarios, participant criteria, and pass thresholds are TBD in the V&V Plan (Vol 22) with Vol 12/30 inputs. No mobility credit is claimed at this revision.

## 14. Risks

- Mobility needs undefined → task failure or handling hazard discovered late; mitigation: early UMO placeholders plus review gates.
- Suit-joint scope undefined → redesign across suit/station; mitigation: UMO-002 placeholder plus architecture review.

## 15. Open Issues

TBD: mobility needs including ankle-module articulation, suit-joint provisions, ground-handling provisions, and verification criteria pending HSA-tier and Vol 30 inputs.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on STK-002 stability, HUM-tier stability (HFPX-SYS-HUM-001), HSA-tier allocation (TBD), Vol 30 hooks (TBD), Chapters 12.1/12.5 architecture and ergonomics inputs, and V&V Plan cases. Changes propagate by change record.

## 18. Traceability

Parents: STK-002, HUM tier (REQ-HFPX-HUM-003), HSA tier (ID TBD), Vol 30 hooks (TBD) — see table. Children: suit-joint specs, handling procedures, V&V cases, RTM rows. RTM seed for UMO-001..004 added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Additions or need changes require new revisions via change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 12.10) |
