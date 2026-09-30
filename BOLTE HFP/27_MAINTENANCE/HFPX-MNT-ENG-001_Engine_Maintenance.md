# Engine Maintenance

**Document ID:** HFPX-MNT-ENG-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Specify engine maintenance for HFP-X at analysis and methodology level, covering Chapter 27.5 Engine Maintenance. This document owns the analytical basis for engine maintenance decisions without authorising hands-on energetics work.

## 2. Scope

Covers engine maintenance methodology, analysis tasks, supporting data, and recording. Task inventory TBD. Intervals TBD. Records TBD. Analysis and methodology scope only; hands-on energetics instructions are excluded from this document (disposition TBD). Maintenance specifications only; no implementation design is implied.

## 3. Applicable Documents

- HFPX-SYS-STK-001 Stakeholder Requirements, including REQ-HFPX-STK-005
- HFPX-MNT-PRG-001 Maintenance Programme
- Maintainability classification (details TBD)
- Propulsion artefacts, including Vol 05 hooks (TBD)
- Vol 24 RAMS artefacts (hooks TBD)
- Vol 28 ILS artefacts (hooks TBD)

## 4. Definitions & Acronyms

- Engine maintenance methodology: the defined analytical approach supporting engine maintenance decisions
- Analysis task: an assessment activity informing maintenance disposition without hands-on intervention
- Remaining terms TBD

## 5. System Context

Engine maintenance decisions depend on analysis of inspection outcomes, health indications, and life-management status. Hands-on energetics activity remains outside the scope of this specification pending applicable authority and process (details TBD).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-LEM-001 | The engine maintenance methodology shall be defined (methodology TBD). | REQ-HFPX-STK-005 | Inspection |
| REQ-HFPX-LEM-002 | Engine analysis tasks supporting maintenance decisions shall be defined (task inventory TBD). | REQ-HFPX-STK-005 | Inspection |
| REQ-HFPX-LEM-003 | Data required to support engine maintenance decisions shall be defined (data TBD). | REQ-HFPX-STK-005 | Inspection |
| REQ-HFPX-LEM-004 | Engine maintenance actions and findings shall be recorded in accordance with the maintenance records process (records TBD). | REQ-HFPX-STK-005 | Inspection |

## 7. Architecture

Engine maintenance analysis structure TBD. Relationship to propulsion design artefacts, inspection programme, and component life management TBD.

## 8. Detailed Design

Not applicable — methodology specification only. No hands-on energetics instructions are contained in this document.

## 9. Interfaces

- Interface to maintenance programme HFPX-MNT-PRG-001 (TBD)
- Interface to propulsion artefacts including Vol 05 hooks (TBD)
- Interface to inspection and life-management specifications (TBD)
- Interface to maintenance records specification (TBD)
- Interface to Vol 24 and Vol 28 artefacts (TBD)

## 10. Operational Concept

Engine condition is assessed through analysis, dispositioned to applicable follow-up, and recorded. Analytical flow TBD. Authorisation boundaries for hands-on activity TBD.

## 11. Safety

Engine maintenance carries energetics and handling hazards. Safety precautions TBD. Nothing in this document authorises hands-on energetics work or operation outside controlled conditions.

## 12. Performance

Analytical coverage and decision-support expectations TBD. No limits are stated at this revision.

## 13. Verification & Validation

| Requirement | Method | Notes |
| --- | --- | --- |
| REQ-HFPX-LEM-001..004 | Inspection | Methodology, tasks, data needs, and recording inspected (artefacts TBD) |
| Analysis workflow execution | Demonstration | Execution of defined analysis workflows demonstrated where exercised (scope TBD) |

## 14. Risks

- Undefined methodology may produce inconsistent maintenance dispositions; mitigation TBD
- Misinterpretation of scope as authorising hands-on energetics work; mitigation: explicit scope exclusion maintained

## 15. Open Issues

- Methodology TBD
- Task inventory TBD
- Supporting data TBD
- Intervals TBD
- Records TBD

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

- REQ-HFPX-STK-005 stakeholder maintainability need
- HFPX-MNT-PRG-001 maintenance programme (TBD)
- Maintainability classification (details TBD)
- Propulsion and Vol 24 / Vol 28 inputs (TBD)

## 18. Traceability

Parents: REQ-HFPX-STK-005. Children: engine analysis task specifications and associated verification cases (TBD). Hooks to Vol 05, Vol 24, and Vol 28 artefacts TBD.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Changes after issue require change records (process TBD).

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial draft (Chapter 27.5) |
