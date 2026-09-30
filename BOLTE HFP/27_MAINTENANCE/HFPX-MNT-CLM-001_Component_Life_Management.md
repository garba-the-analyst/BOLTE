# Component Life Management

**Document ID:** HFPX-MNT-CLM-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Specify component life management for HFP-X, covering Chapter 27.11 Component Life Management. This document owns the identification, tracking, and retirement specification for life-managed components.

## 2. Scope

Covers identification of life-managed components, life-consumption tracking, replacement and retirement criteria, and recording. Tracking TBD. Intervals TBD. Records TBD. Maintenance specifications only; no implementation design is implied.

## 3. Applicable Documents

- HFPX-SYS-STK-001 Stakeholder Requirements, including REQ-HFPX-STK-005
- HFPX-MNT-PRG-001 Maintenance Programme
- Maintainability classification (details TBD)
- Vol 24 artefacts, including Vol 24.10 hooks (TBD)
- Vol 28 ILS artefacts (hooks TBD)

## 4. Definitions & Acronyms

- Life-managed component: a component subject to defined life tracking and retirement
- Life-consumption tracking: the defined method for accounting service exposure against retirement criteria
- Remaining terms TBD

## 5. System Context

Component life management assures that life-managed components are retired or replaced before exceeding defined criteria. Analytical and reliability inputs are expected from Vol 24; support integration from Vol 28 (details TBD).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-LCM-001 | Life-managed components subject to life management shall be identified (tracking TBD). | REQ-HFPX-STK-005 | Inspection |
| REQ-HFPX-LCM-002 | The life-consumption tracking method for life-managed components shall be defined (method TBD). | REQ-HFPX-STK-005 | Inspection |
| REQ-HFPX-LCM-003 | Replacement and retirement criteria for life-managed components shall be defined (criteria TBD). | REQ-HFPX-STK-005 | Inspection |
| REQ-HFPX-LCM-004 | Life-management status and replacements shall be recorded in accordance with the maintenance records process (records TBD). | REQ-HFPX-STK-005 | Inspection |

## 7. Architecture

Component life management structure TBD. Allocation of tracking responsibility across maintenance and support functions TBD. Relationship to Vol 24.10 support artefacts TBD.

## 8. Detailed Design

Not applicable — life-management specification only. No design implementation is implied or authorised by this document.

## 9. Interfaces

- Interface to maintenance programme HFPX-MNT-PRG-001 (TBD)
- Interface to Vol 24 artefacts including Vol 24.10 hooks (TBD)
- Interface to Vol 28 artefacts (TBD)
- Interface to maintenance records specification (TBD)

## 10. Operational Concept

Life exposure is tracked, assessed against retirement criteria, dispositioned to replacement, and recorded. Operational flow TBD.

## 11. Safety

Safety implications of exceeding retirement criteria TBD. Controls preventing use of retired components TBD.

## 12. Performance

Life-management coverage and accuracy expectations TBD. No limits are stated at this revision.

## 13. Verification & Validation

| Requirement | Method | Notes |
| --- | --- | --- |
| REQ-HFPX-LCM-001..004 | Inspection | Identification, tracking method, criteria, and recording inspected (artefacts TBD) |
| Tracking and retirement workflow | Demonstration | Tracking through to retirement disposition demonstrated where exercised (scope TBD) |

## 14. Risks

- Undefined tracking method may allow components to remain in service beyond criteria; mitigation TBD
- Undefined criteria may leave retirement decisions inconsistent; mitigation TBD

## 15. Open Issues

- Life-managed component identification TBD
- Tracking method TBD
- Replacement and retirement criteria TBD
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

Parents: REQ-HFPX-STK-005. Children: component life-management specifications and associated verification cases (TBD). Hooks to Vol 24 including Vol 24.10, plus Vol 28 artefacts, TBD.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Changes after issue require change records (process TBD).

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial draft (Chapter 27.11) |
