# Pilot Restraint

**Document ID:** HFPX-HUM-RST-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define pilot-restraint requirements for HFP-X (Chapter 12.3). This Tranche 6 draft establishes restraint-function, release/egress, and structural-interface placeholders; all values and details are TBD.

## 2. Scope

Covers restraint functions, release and egress provisions including emergency egress, and the restraint structural interface. Excludes load-distribution detail (12.4), ergonomics detail (12.5), and protection detail (12.7). Structural substantiation is Vol 03 scope.

## 3. Applicable Documents

- HFPX-SYS-HUM-001 Human Factors Requirements (parent HUM tier)
- Stakeholder need STK-002 (human involvement)
- HSA tier (ID TBD — allocation to follow)
- Vol 30 hooks (TBD — egress/training inputs to follow)
- Vol 03 airframe structures including Chapter 03.5 (TBD), HFPX-HUM-ARC-001 (Chapter 12.1)

## 4. Definitions & Acronyms

- HUM: human-factors requirement tier; IDs `REQ-HFPX-HUM-NNN`.
- URS: pilot-restraint requirement tier; IDs `REQ-HFPX-URS-NNN`; verification TBD.
- TBD/TBC: unknown data; no values invented.

## 5. System Context

Pilot restraint refines system-level restraint needs into testable placeholders:

```text
STK-002 + HUM tier → URS-001..004 → restraint / airframe detail (Vol 03.5) → V&V cases
```

No restraint geometry, load, or timing is approved at this revision.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-URS-001|The system shall provide pilot-restraint functions retaining the pilot in defined phases and conditions (restraint functions TBD).|STK-002, REQ-HFPX-HUM-003, HSA tier (ID TBD)|Inspection|
|REQ-HFPX-URS-002|The restraint shall provide release and egress provisions, including emergency egress provisions (release/egress provisions TBD).|STK-002, REQ-HFPX-HUM-003, HSA tier (ID TBD)|Inspection|
|REQ-HFPX-URS-003|The restraint shall interface to vehicle structure at defined attachment provisions (structural interface TBD; Vol 03.5 detail to follow).|STK-002, REQ-HFPX-HUM-003, HSA tier (ID TBD)|Inspection|
|REQ-HFPX-URS-004|Restraint performance and egress provisions shall be verified against defined criteria (criteria TBD; Vol 30 hook TBD).|STK-002, REQ-HFPX-HUM-003, HSA tier (ID TBD)|Inspection|

All functions, provisions, interfaces, and criteria are TBD. No value is approved.

## 7. Architecture

Starter allocation (SAD owns authoritative mapping): URS-001/002 → restraint subsystem and egress provisions; URS-003 → airframe structure (Vol 03.5); URS-004 → V&V framework with Vol 30 hooks. All TBC.

## 8. Detailed Design

Not applicable — requirements level only. Harness geometry, release mechanisms, attachment hardware, and procedures are TBD in follow-on revisions.

## 9. Interfaces

Restraint interfaces (suit/restraint couplings, airframe attachments, release linkages) are TBD in Vol 02 ICDs, Vol 03.5, and Chapter 12.1 register. No interface value or layout is approved.

## 10. Operational Concept

Restraint requirements apply across ingress, flight, emergency, egress, and recovery phases; phase-specific applicability is TBD. Unmanned demonstration precedes any crewed evaluation per safety gating.

## 11. Safety

Restraint failures, inadvertent release, and failed egress feed Vol 13 safety analyses (to follow). No URS requirement confers flight approval; human flight remains gated by tier 01.10 and the Safety Case.

## 12. Performance

No URS requirement quantifies performance. All retention, release, and egress measures are TBD pending follow-on studies.

## 13. Verification & Validation

Each requirement states its method above as TBD; verification IDs, test conditions, participant criteria, and pass thresholds are TBD in the V&V Plan (Vol 22) with Vol 03/12/30 inputs. No restraint credit is claimed at this revision.

## 14. Risks

- Restraint functions undefined → retention or egress shortfall discovered late; mitigation: early URS placeholders plus review gates.
- Structural interface undefined → airframe rework; mitigation: URS-003 placeholder plus Vol 03.5 coordination.

## 15. Open Issues

TBD: restraint functions, release/egress including emergency provisions, structural interface definition, and verification criteria pending Vol 03.5/30 and HSA-tier inputs.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on STK-002 stability, HUM-tier stability (HFPX-SYS-HUM-001), HSA-tier allocation (TBD), Vol 30 hooks (TBD), Vol 03.5 structural work, Chapter 12.1 architecture, and V&V Plan cases. Changes propagate by change record.

## 18. Traceability

Parents: STK-002, HUM tier (REQ-HFPX-HUM-003), HSA tier (ID TBD), Vol 30 hooks (TBD) — see table. Children: restraint specs, Vol 03.5 attachment specs, egress procedures, V&V cases, RTM rows. RTM seed for URS-001..004 added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Additions or interface changes require new revisions via change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 12.3) |
