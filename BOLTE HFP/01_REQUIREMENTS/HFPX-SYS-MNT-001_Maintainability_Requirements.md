# Maintainability Requirements — Chapter 01.13

**Document ID:** HFPX-SYS-MNT-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 8 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Capture system maintainability requirements for HFP-X in one tier. This Tranche 8 draft establishes structure only; all intervals, times and values are TBD.

## 2. Scope

Covers inspection, servicing, fault isolation and turnaround enablement at system level. Detailed maintenance tasks and support equipment live in Vol 03–18. All quantitative values TBD.

## 3. Applicable Documents

- HFPX-SYS-STK-001 Stakeholder Requirements (parent tier, including STK-005 supportability)
- HFPX-SYS-REQ-001 SyRS (Chapter 01.6)
- Maintenance and training subsystem views (Vol 03–18, TBD)
- HFP prompt §§8–10 (requirements format, classification, traceability)

## 4. Definitions & Acronyms

- Maintainability requirement ID `REQ-HFPX-MTN-NNN`; verification: Analysis / Inspection / Demonstration / Test
- TBD/TBC: unknown data handling; no invented values
- LRU: line-replaceable unit (candidate concept, definition TBD)

## 5. System Context

Maintainability requirements translate stakeholder supportability intent (STK-005) into verifiable maintenance behaviour:

```text
STAKEHOLDER (STK-005) → MAINTAINABILITY (this document) → SUBSYSTEM MAINTENANCE DESIGN → V&V
```

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-MTN-001 | The system shall enable fault isolation to defined replaceable units using built-in indications (units and means TBD). | REQ-HFPX-STK-005 | Demonstration |
| REQ-HFPX-MTN-002 | The system shall provide access for defined inspection and servicing tasks without special tooling beyond a defined list (tasks and tooling TBD). | REQ-HFPX-STK-005 | Demonstration |
| REQ-HFPX-MTN-003 | The system shall document maintenance tasks, servicing needs and turnaround actions in a defined maintenance set (document structure TBD). | REQ-HFPX-STK-005 | Inspection |
| REQ-HFPX-MTN-004 | The system shall meet defined turnaround and restoration targets for return to service (targets and conditions TBD; no interval is stated at this revision). | REQ-HFPX-STK-005 | Demonstration + Inspection |

## 7. Architecture

Allocation (SAD owns authoritative allocation): MTN-001 → avionics/BIT views; MTN-002/MTN-004 → airframe/propulsion/ground station views; MTN-003 → SE artefacts. Allocation table TBD.

## 8. Detailed Design

Not applicable — requirements tier only. Maintenance design and support equipment live in Vol 03–18 and are TBD.

## 9. Interfaces

Maintenance interfaces (ground support equipment, servicing ports, data download) reference Chapter 01.16; ICD details TBD.

## 10. Operational Concept

Maintainability requirements are exercised through turnaround and recovery CONOPS threads (mapping table TBD in V&V Plan).

## 11. Safety

Maintenance errors with safety effect are controlled via system safety requirements (01.10) and Safety Case; analyses TBD.

## 12. Performance

No maintenance interval, repair time, turnaround time or availability value is stated; all such values TBD.

## 13. Verification & Validation

Each requirement states its method above; verification cases and IDs are TBD in the V&V Plan (Vol 22). Demonstration via maintenance tasks on ground articles; Inspection via documentation review. Requirements without a verification method are rejected at SRR.

## 14. Risks

- Maintenance concept preceding physical architecture → mitigation: explicit TBD status, tasks refined as Vol 03–18 mature
- Support-equipment scope creep; mitigation: bounded task list via change control

## 15. Open Issues

- Replaceable-unit breakdown TBD
- Maintenance task list, tooling list and turnaround targets TBD

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on STK-005 approval, SAD allocation, subsystem maintenance concepts (Vol 03–18), safety analyses, V&V Plan cases.

## 18. Traceability

Parents: REQ-HFPX-STK-005. Children: subsystem maintainability requirements (Vol 03–18), maintenance documentation, V&V cases, RTM rows (01.18). RTM seed for MTN-001..004 added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0 (structure only) — Tranche 8 draft, not baselined. Changes require change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 8 draft (Chapter 01.13) |
