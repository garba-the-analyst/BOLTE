# Fuel-System Maintenance

**Document ID:** HFPX-MNT-FSM-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Specify fuel-system maintenance for HFP-X, covering Chapter 27.6 Fuel-System Maintenance. This document owns fuel-system maintenance task specifications and their safety basis.

## 2. Scope

Covers fuel-system maintenance tasks, safety precautions, propulsion interfaces, and recording. Task inventory TBD. Intervals TBD. Safety precautions TBD. Records TBD. Maintenance specifications only; no implementation design is implied.

## 3. Applicable Documents

- HFPX-SYS-STK-001 Stakeholder Requirements, including REQ-HFPX-STK-005
- HFPX-MNT-PRG-001 Maintenance Programme
- Maintainability classification (details TBD)
- Vol 05 propulsion artefacts, including Vol 05.15 hooks (TBD)
- Vol 24 RAMS artefacts (hooks TBD)
- Vol 28 ILS artefacts (hooks TBD)

## 4. Definitions & Acronyms

- Fuel-system maintenance: inspection, servicing, and replacement activity applicable to fuel storage, distribution, and control elements
- Safety precaution: a mandated protective measure or constraint
- Remaining terms TBD

## 5. System Context

Fuel-system maintenance sustains the serviceability of propulsion feed elements while respecting fuel hazards. Design authority remains with Vol 05; this document specifies maintenance needs against that design (interface TBD).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-LFM-001 | Fuel-system maintenance tasks shall be defined (task inventory TBD). | REQ-HFPX-STK-005 | Inspection |
| REQ-HFPX-LFM-002 | Safety precautions applicable to fuel-system maintenance shall be defined (precautions TBD). | REQ-HFPX-STK-005 | Inspection |
| REQ-HFPX-LFM-003 | Fuel-system maintenance shall maintain interface consistency with applicable Vol 05 artefacts (interface TBD). | REQ-HFPX-STK-005 | Inspection |
| REQ-HFPX-LFM-004 | Fuel-system maintenance actions and findings shall be recorded in accordance with the maintenance records process (records TBD). | REQ-HFPX-STK-005 | Inspection |

## 7. Architecture

Fuel-system maintenance structure TBD. Allocation to fuel-system elements TBD. Relationship to Vol 05.15 support artefacts TBD.

## 8. Detailed Design

Not applicable — task specification only. No design implementation is implied or authorised by this document.

## 9. Interfaces

- Interface to maintenance programme HFPX-MNT-PRG-001 (TBD)
- Interface to Vol 05 propulsion artefacts including Vol 05.15 hooks (TBD)
- Interface to maintenance records specification (TBD)
- Interface to Vol 24 and Vol 28 artefacts (TBD)

## 10. Operational Concept

Fuel-system tasks are prepared under applicable precautions, executed, and closed with records. Operational flow TBD.

## 11. Safety

Fuel hazards require defined precautions for handling, ventilation, isolation, and ignition control. Precautions TBD. Nothing in this document authorises work outside controlled conditions.

## 12. Performance

Fuel-system maintenance coverage expectations TBD. No limits are stated at this revision.

## 13. Verification & Validation

| Requirement | Method | Notes |
| --- | --- | --- |
| REQ-HFPX-LFM-001..004 | Inspection | Tasks, precautions, interface consistency, and recording inspected (artefacts TBD) |
| Precaution-controlled task execution | Demonstration | Execution under defined precautions demonstrated where exercised (scope TBD) |

## 14. Risks

- Undefined precautions may expose maintainers to fuel hazards; mitigation TBD
- Interface drift from Vol 05 design evolution; mitigation TBD

## 15. Open Issues

- Task inventory TBD
- Safety precautions TBD
- Vol 05.15 interface TBD
- Intervals TBD
- Records TBD

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

- REQ-HFPX-STK-005 stakeholder maintainability need
- HFPX-MNT-PRG-001 maintenance programme (TBD)
- Maintainability classification (details TBD)
- Vol 05, Vol 24, and Vol 28 inputs (TBD)

## 18. Traceability

Parents: REQ-HFPX-STK-005. Children: fuel-system task specifications and associated verification cases (TBD). Hooks to Vol 05 including Vol 05.15, plus Vol 24 and Vol 28 artefacts, TBD.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Changes after issue require change records (process TBD).

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial draft (Chapter 27.6) |
