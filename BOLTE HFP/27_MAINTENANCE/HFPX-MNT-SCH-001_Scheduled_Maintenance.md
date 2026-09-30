# Scheduled Maintenance

**Document ID:** HFPX-MNT-SCH-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Specify scheduled maintenance for HFP-X, covering Chapter 27.2 Scheduled Maintenance. This document owns interval-based and condition-based scheduled task specifications under the maintenance programme.

## 2. Scope

Covers scheduled maintenance tasks derived from the maintenance programme. Task inventory TBD. Intervals TBD. Records TBD. Maintenance specifications only; no implementation design is implied.

## 3. Applicable Documents

- HFPX-SYS-STK-001 Stakeholder Requirements, including REQ-HFPX-STK-005
- HFPX-MNT-PRG-001 Maintenance Programme
- Maintainability classification (details TBD)
- Vol 24 RAMS artefacts (hooks TBD)
- Vol 28 ILS artefacts (hooks TBD)

## 4. Definitions & Acronyms

- Scheduled maintenance: maintenance performed at defined intervals or under defined conditions
- Task inventory: the governed list of scheduled tasks and their specifications
- Remaining terms TBD

## 5. System Context

Scheduled maintenance provides the preventive element of the maintenance programme, enabling maintainers to service applicable items before findings force unscheduled action. Classification and interval policy TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-LSM-001 | The scheduled maintenance task inventory shall be defined (task inventory TBD). | REQ-HFPX-STK-005 | Inspection |
| REQ-HFPX-LSM-002 | Intervals associated with scheduled maintenance tasks shall be defined (intervals TBD). | REQ-HFPX-STK-005 | Inspection |
| REQ-HFPX-LSM-003 | Scheduled maintenance tasks shall specify required access, tools, and consumables (details TBD). | REQ-HFPX-STK-005 | Inspection |
| REQ-HFPX-LSM-004 | Completion of scheduled maintenance tasks shall be recorded in accordance with the maintenance records process (records TBD). | REQ-HFPX-STK-005 | Inspection |

## 7. Architecture

Allocation of scheduled tasks to systems and components TBD. Relationship to inspection programme and component life management TBD.

## 8. Detailed Design

Not applicable — task specification only. No design implementation is implied or authorised by this document.

## 9. Interfaces

- Interface to maintenance programme HFPX-MNT-PRG-001 (TBD)
- Interface to inspection programme (TBD)
- Interface to maintenance records specification (TBD)
- Interface to Vol 24 and Vol 28 artefacts (TBD)

## 10. Operational Concept

Scheduled tasks are released, executed, and closed through the maintenance programme workflow. Sequencing and release logic TBD.

## 11. Safety

Safety implications of accessing and servicing applicable items TBD. Precautions TBD. No scheduled task is interpreted as permission to operate outside controlled conditions.

## 12. Performance

Scheduled maintenance effectiveness thresholds TBD. No limits are stated at this revision.

## 13. Verification & Validation

| Requirement | Method | Notes |
| --- | --- | --- |
| REQ-HFPX-LSM-001..002, REQ-HFPX-LSM-004 | Inspection | Task inventory, intervals, and recording inspected against programme (artefacts TBD) |
| REQ-HFPX-LSM-003 | Demonstration | Access, tooling, and consumables provision demonstrated where exercised (scope TBD) |

## 14. Risks

- Undefined intervals may leave preventive coverage incomplete; mitigation TBD
- Undefined tooling and access needs may delay task readiness; mitigation TBD

## 15. Open Issues

- Task inventory TBD
- Intervals TBD
- Access, tools, and consumables TBD
- Records TBD

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

- REQ-HFPX-STK-005 stakeholder maintainability need
- HFPX-MNT-PRG-001 maintenance programme (TBD)
- Maintainability classification (details TBD)
- Vol 24 and Vol 28 inputs (TBD)

## 18. Traceability

Parents: REQ-HFPX-STK-005. Children: scheduled task specifications and associated verification cases (TBD). Hooks to Vol 24 and Vol 28 artefacts TBD.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Changes after issue require change records (process TBD).

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial draft (Chapter 27.2) |
