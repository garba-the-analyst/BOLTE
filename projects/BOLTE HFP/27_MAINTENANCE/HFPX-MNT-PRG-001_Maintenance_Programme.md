# Maintenance Programme

**Document ID:** HFPX-MNT-PRG-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Specify the content and governance of the HFP-X maintenance programme, covering Chapter 27.1 Maintenance Programme. This document owns programme-level maintenance specifications from which task-level specifications in sibling maintenance documents are derived.

## 2. Scope

Covers the maintenance programme framework for HFP-X, including scheduled maintenance, unscheduled maintenance, inspection, and supporting disciplines. Task inventory TBD. Intervals TBD. Records TBD. Maintenance specifications only; no implementation design is implied.

## 3. Applicable Documents

- HFPX-SYS-STK-001 Stakeholder Requirements, including maintainability need REQ-HFPX-STK-005
- Maintainability classification (details TBD)
- Vol 24 RAMS artefacts (hooks TBD)
- Vol 28 ILS artefacts (hooks TBD)
- Sibling maintenance specifications, Chapter 27.2 through Chapter 27.14 (details TBD)

## 4. Definitions & Acronyms

- Maintenance programme: the governed set of maintenance specifications applicable to HFP-X
- Scheduled maintenance: maintenance performed on a defined interval or condition basis
- Unscheduled maintenance: maintenance triggered by findings, faults, or events
- Remaining terms TBD

## 5. System Context

Maintainers need to inspect, service, and replace applicable components with defined intervals (REQ-HFPX-STK-005). The maintenance programme connects that stakeholder need to task-level specifications owned across this volume, under the applicable maintainability classification (classification TBD).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-LMP-001 | The maintenance programme shall define the set of maintenance tasks applicable to HFP-X. | REQ-HFPX-STK-005 | Inspection |
| REQ-HFPX-LMP-002 | The maintenance programme shall specify the interval basis for scheduled tasks (intervals TBD). | REQ-HFPX-STK-005 | Inspection |
| REQ-HFPX-LMP-003 | The maintenance programme shall specify responsibility and competence needs for maintenance tasks (details TBD). | REQ-HFPX-STK-005 | Inspection |
| REQ-HFPX-LMP-004 | The maintenance programme shall specify the records required for maintenance tasks (records TBD). | REQ-HFPX-STK-005 | Inspection |
| REQ-HFPX-LMP-005 | The maintenance programme shall maintain traceability to stakeholder maintainability needs and to supporting Vol 24 and Vol 28 artefacts (details TBD). | REQ-HFPX-STK-005 | Inspection |

## 7. Architecture

Maintenance programme structure TBD. Allocation of programme elements to sibling maintenance specifications TBD. Relationship to Vol 24 and Vol 28 support structures TBD.

## 8. Detailed Design

Not applicable — programme specification only. No design implementation is implied or authorised by this document.

## 9. Interfaces

- Interface to Vol 24 RAMS artefacts (TBD)
- Interface to Vol 28 ILS artefacts (TBD)
- Interface to Vol 26 operations processes (TBD)
- Interface to maintenance records specification (TBD)

## 10. Operational Concept

The maintenance programme is exercised through applicable maintenance threads spanning preparation, execution, and recording. Thread definitions TBD. Operational sequencing TBD.

## 11. Safety

No maintenance activity is interpreted as permission to bypass gated testing or controlled-condition constraints. Safety implications of programme structure TBD. Handling and energetics constraints TBD.

## 12. Performance

Programme acceptance thresholds TBD. No limits are stated at this revision.

## 13. Verification & Validation

| Requirement | Method | Notes |
| --- | --- | --- |
| REQ-HFPX-LMP-001..005 | Inspection | Programme definition artefacts inspected for completeness and traceability (artefacts TBD) |
| Programme-driven task execution capability | Demonstration | Demonstrated where task execution is exercised (scope TBD) |

## 14. Risks

- Undefined task inventory and intervals may delay maintenance planning; mitigation TBD
- Traceability gaps to Vol 24 and Vol 28 may weaken support claims; mitigation TBD

## 15. Open Issues

- Task inventory TBD
- Intervals TBD
- Records TBD
- Responsibility and competence definitions TBD
- Owner and approver assignment TBD

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

- REQ-HFPX-STK-005 stakeholder maintainability need
- Maintainability classification (details TBD)
- Vol 24 RAMS inputs (TBD)
- Vol 28 ILS inputs (TBD)

## 18. Traceability

Parents: REQ-HFPX-STK-005. Children: task-level maintenance specifications across this volume (TBD). Hooks to Vol 24 and Vol 28 artefacts TBD. RTM status TBD.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Changes after issue require change records (process TBD).

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial draft (Chapter 27.1) |
