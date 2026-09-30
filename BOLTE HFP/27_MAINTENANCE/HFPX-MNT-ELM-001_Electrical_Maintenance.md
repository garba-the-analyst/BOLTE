# Electrical Maintenance

**Document ID:** HFPX-MNT-ELM-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Specify electrical maintenance for HFP-X, covering Chapter 27.8 Electrical Maintenance. This document owns electrical maintenance task specifications and their safety basis.

## 2. Scope

Covers electrical maintenance tasks, isolation and safety precautions, intervals, and recording. Task inventory TBD. Intervals TBD. Records TBD. Maintenance specifications only; no implementation design is implied.

## 3. Applicable Documents

- HFPX-SYS-STK-001 Stakeholder Requirements, including REQ-HFPX-STK-005
- HFPX-MNT-PRG-001 Maintenance Programme
- Maintainability classification (details TBD)
- Electrical design artefacts (hooks TBD)
- Vol 24 RAMS artefacts (hooks TBD)
- Vol 28 ILS artefacts (hooks TBD)

## 4. Definitions & Acronyms

- Electrical maintenance: inspection, servicing, and replacement activity applicable to electrical generation, distribution, and control elements
- Isolation: the defined safe state for electrical work (details TBD)
- Remaining terms TBD

## 5. System Context

Electrical maintenance sustains the serviceability of power and distribution elements while respecting electrical hazards. Design authority remains with electrical design artefacts; this document specifies maintenance needs against that design (interface TBD).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-LEL-001 | Electrical maintenance tasks shall be defined (task inventory TBD). | REQ-HFPX-STK-005 | Inspection |
| REQ-HFPX-LEL-002 | Isolation and safety precautions applicable to electrical maintenance shall be defined (precautions TBD). | REQ-HFPX-STK-005 | Inspection |
| REQ-HFPX-LEL-003 | Electrical maintenance intervals shall be defined (intervals TBD). | REQ-HFPX-STK-005 | Inspection |
| REQ-HFPX-LEL-004 | Electrical maintenance actions and findings shall be recorded in accordance with the maintenance records process (records TBD). | REQ-HFPX-STK-005 | Inspection |

## 7. Architecture

Electrical maintenance structure TBD. Allocation to electrical elements TBD. Relationship to avionics maintenance and Vol 24 / Vol 28 support structures TBD.

## 8. Detailed Design

Not applicable — task specification only. No design implementation is implied or authorised by this document.

## 9. Interfaces

- Interface to maintenance programme HFPX-MNT-PRG-001 (TBD)
- Interface to electrical design artefacts (TBD)
- Interface to maintenance records specification (TBD)
- Interface to Vol 24 and Vol 28 artefacts (TBD)

## 10. Operational Concept

Electrical tasks are isolated, executed under applicable precautions, and closed with records. Operational flow TBD.

## 11. Safety

Electrical hazards require defined isolation and precautions. Precautions TBD. Nothing in this document authorises work on energised elements outside defined precautions.

## 12. Performance

Electrical maintenance coverage expectations TBD. No limits are stated at this revision.

## 13. Verification & Validation

| Requirement | Method | Notes |
| --- | --- | --- |
| REQ-HFPX-LEL-001..004 | Inspection | Tasks, precautions, intervals, and recording inspected (artefacts TBD) |
| Precaution-controlled task execution | Demonstration | Execution under defined precautions demonstrated where exercised (scope TBD) |

## 14. Risks

- Undefined isolation precautions may expose maintainers to electrical hazards; mitigation TBD
- Undefined intervals may leave electrical degradation undetected; mitigation TBD

## 15. Open Issues

- Task inventory TBD
- Isolation and safety precautions TBD
- Intervals TBD
- Records TBD

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

- REQ-HFPX-STK-005 stakeholder maintainability need
- HFPX-MNT-PRG-001 maintenance programme (TBD)
- Maintainability classification (details TBD)
- Electrical and Vol 24 / Vol 28 inputs (TBD)

## 18. Traceability

Parents: REQ-HFPX-STK-005. Children: electrical task specifications and associated verification cases (TBD). Hooks to Vol 24 and Vol 28 artefacts TBD.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Changes after issue require change records (process TBD).

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial draft (Chapter 27.8) |
