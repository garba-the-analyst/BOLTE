# Avionics Maintenance

**Document ID:** HFPX-MNT-AVM-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Specify avionics maintenance for HFP-X, covering Chapter 27.7 Avionics Maintenance. This document owns avionics maintenance task specifications and their relationship to built-in test outcomes.

## 2. Scope

Covers avionics maintenance tasks, built-in test hooks, intervals, and recording. Task inventory TBD. Intervals TBD. Built-in test hooks TBD. Records TBD. Maintenance specifications only; no implementation design is implied.

## 3. Applicable Documents

- HFPX-SYS-STK-001 Stakeholder Requirements, including REQ-HFPX-STK-005
- HFPX-MNT-PRG-001 Maintenance Programme
- Maintainability classification (details TBD)
- Avionics artefacts, including Vol 08.15 hooks (TBD)
- Vol 24 RAMS artefacts (hooks TBD)
- Vol 28 ILS artefacts (hooks TBD)

## 4. Definitions & Acronyms

- Avionics maintenance: inspection, test, servicing, and replacement activity applicable to avionics elements
- BIT: built-in test capability supporting fault detection and isolation (details TBD)
- Remaining terms TBD

## 5. System Context

Avionics maintenance sustains the serviceability of sensing, computing, and interface elements. Built-in test outcomes inform maintenance disposition where defined; test authority and coverage remain with avionics design artefacts (details TBD).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-LAM-001 | Avionics maintenance tasks shall be defined (task inventory TBD). | REQ-HFPX-STK-005 | Inspection |
| REQ-HFPX-LAM-002 | Use of built-in test outcomes to support avionics maintenance decisions shall be defined (BIT hooks TBD). | REQ-HFPX-STK-005 | Inspection |
| REQ-HFPX-LAM-003 | Avionics maintenance intervals shall be defined (intervals TBD). | REQ-HFPX-STK-005 | Inspection |
| REQ-HFPX-LAM-004 | Avionics maintenance actions and findings shall be recorded in accordance with the maintenance records process (records TBD). | REQ-HFPX-STK-005 | Inspection |

## 7. Architecture

Avionics maintenance structure TBD. Allocation to avionics elements TBD. Relationship to Vol 08.15 support artefacts TBD.

## 8. Detailed Design

Not applicable — task specification only. No design implementation is implied or authorised by this document.

## 9. Interfaces

- Interface to maintenance programme HFPX-MNT-PRG-001 (TBD)
- Interface to avionics design artefacts including Vol 08.15 hooks (TBD)
- Interface to maintenance records specification (TBD)
- Interface to Vol 24 and Vol 28 artefacts (TBD)

## 10. Operational Concept

Avionics condition is assessed through inspection and built-in test outcomes, dispositioned to applicable follow-up, and recorded. Flow details TBD.

## 11. Safety

Safety implications of avionics maintenance, including handling of sensitive elements and electrical exposure, TBD. Precautions TBD.

## 12. Performance

Avionics maintenance coverage expectations TBD. No limits are stated at this revision.

## 13. Verification & Validation

| Requirement | Method | Notes |
| --- | --- | --- |
| REQ-HFPX-LAM-001..004 | Inspection | Tasks, built-in test usage, intervals, and recording inspected (artefacts TBD) |
| BIT-informed maintenance disposition | Demonstration | Disposition using built-in test outcomes demonstrated where exercised (scope TBD) |

## 14. Risks

- Undefined built-in test hooks may weaken fault isolation; mitigation TBD
- Undefined intervals may leave avionics degradation undetected; mitigation TBD

## 15. Open Issues

- Task inventory TBD
- BIT hooks including Vol 08.15 TBD
- Intervals TBD
- Records TBD

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

- REQ-HFPX-STK-005 stakeholder maintainability need
- HFPX-MNT-PRG-001 maintenance programme (TBD)
- Maintainability classification (details TBD)
- Avionics and Vol 24 / Vol 28 inputs (TBD)

## 18. Traceability

Parents: REQ-HFPX-STK-005. Children: avionics task specifications and associated verification cases (TBD). Hooks to Vol 08 including Vol 08.15, plus Vol 24 and Vol 28 artefacts, TBD.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Changes after issue require change records (process TBD).

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial draft (Chapter 27.7) |
