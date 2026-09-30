# Inspection Programme

**Document ID:** HFPX-MNT-INP-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Specify the inspection programme for HFP-X, covering Chapter 27.4 Inspection Programme. This document owns inspection task specifications that detect findings feeding scheduled and unscheduled maintenance.

## 2. Scope

Covers inspection tasks, methods, acceptance criteria, intervals, and recording. Task inventory TBD. Intervals TBD. Records TBD. Maintenance specifications only; no implementation design is implied.

## 3. Applicable Documents

- HFPX-SYS-STK-001 Stakeholder Requirements, including REQ-HFPX-STK-005
- HFPX-MNT-PRG-001 Maintenance Programme
- Maintainability classification (details TBD)
- Vol 24 RAMS artefacts (hooks TBD)
- Vol 28 ILS artefacts (hooks TBD)

## 4. Definitions & Acronyms

- Inspection: observation and assessment to detect degradation, damage, or nonconformance
- Acceptance criteria: defined basis for judging inspection outcomes
- Remaining terms TBD

## 5. System Context

Inspection provides the detection layer for the maintenance programme, supporting preventive action and triggering corrective action where criteria are not met. Relationship to structural, system, and recovery inspections TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-LIP-001 | The inspection task inventory shall be defined (task inventory TBD). | REQ-HFPX-STK-005 | Inspection |
| REQ-HFPX-LIP-002 | Inspection methods and acceptance criteria shall be defined (criteria TBD). | REQ-HFPX-STK-005 | Inspection |
| REQ-HFPX-LIP-003 | Inspection intervals shall be defined (intervals TBD). | REQ-HFPX-STK-005 | Inspection |
| REQ-HFPX-LIP-004 | Inspection results shall be recorded in accordance with the maintenance records process (records TBD). | REQ-HFPX-STK-005 | Inspection |

## 7. Architecture

Inspection programme structure TBD. Allocation of inspections to zones, systems, and components TBD.

## 8. Detailed Design

Not applicable — inspection specification only. No design implementation is implied or authorised by this document.

## 9. Interfaces

- Interface to maintenance programme HFPX-MNT-PRG-001 (TBD)
- Interface to structural, system, and recovery inspection specifications (TBD)
- Interface to maintenance records specification (TBD)
- Interface to Vol 24 and Vol 28 artefacts (TBD)

## 10. Operational Concept

Inspections are planned, executed, assessed against criteria, and dispositioned to scheduled or unscheduled follow-up. Flow details TBD.

## 11. Safety

Safety implications of inspection access and exposure TBD. Precautions TBD. Inspection does not authorise operation of unserviceable items.

## 12. Performance

Inspection coverage and effectiveness expectations TBD. No limits are stated at this revision.

## 13. Verification & Validation

| Requirement | Method | Notes |
| --- | --- | --- |
| REQ-HFPX-LIP-001..004 | Inspection | Inspection inventory, methods, criteria, intervals, and recording inspected (artefacts TBD) |
| Inspection execution capability | Demonstration | Execution of inspections demonstrated where exercised (scope TBD) |

## 14. Risks

- Undefined methods and criteria may produce inconsistent findings; mitigation TBD
- Undefined intervals may leave degradation undetected; mitigation TBD

## 15. Open Issues

- Task inventory TBD
- Methods and acceptance criteria TBD
- Intervals TBD
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

Parents: REQ-HFPX-STK-005. Children: inspection task specifications and associated verification cases (TBD). Hooks to Vol 24 and Vol 28 artefacts TBD.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Changes after issue require change records (process TBD).

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial draft (Chapter 27.4) |
