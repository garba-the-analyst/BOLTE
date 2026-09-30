# Unscheduled Maintenance

**Document ID:** HFPX-MNT-UNS-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Specify unscheduled maintenance for HFP-X, covering Chapter 27.3 Unscheduled Maintenance. This document owns the response to findings, faults, and events that fall outside scheduled tasks.

## 2. Scope

Covers triggers, response process, scoping, and recording of unscheduled maintenance. Task inventory TBD. Trigger criteria TBD. Records TBD. Maintenance specifications only; no implementation design is implied.

## 3. Applicable Documents

- HFPX-SYS-STK-001 Stakeholder Requirements, including REQ-HFPX-STK-005
- HFPX-MNT-PRG-001 Maintenance Programme
- Maintainability classification (details TBD)
- Vol 24 RAMS artefacts (hooks TBD)
- Vol 28 ILS artefacts (hooks TBD)

## 4. Definitions & Acronyms

- Unscheduled maintenance: maintenance performed in response to findings, faults, or events
- Trigger: a defined condition that initiates the unscheduled maintenance process
- Remaining terms TBD

## 5. System Context

Unscheduled maintenance restores the vehicle to a maintainable state when inspection findings or operational events require action outside the scheduled programme. Relationship to fault isolation and inspection outcomes TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-LUM-001 | Conditions that trigger unscheduled maintenance shall be defined (criteria TBD). | REQ-HFPX-STK-005 | Inspection |
| REQ-HFPX-LUM-002 | The response process for unscheduled maintenance shall be defined (process TBD). | REQ-HFPX-STK-005 | Inspection |
| REQ-HFPX-LUM-003 | Unscheduled maintenance actions shall be scoped from inspection findings and fault isolation outcomes (scope TBD). | REQ-HFPX-STK-005 | Demonstration |
| REQ-HFPX-LUM-004 | Unscheduled maintenance actions shall be recorded in accordance with the maintenance records process (records TBD). | REQ-HFPX-STK-005 | Inspection |

## 7. Architecture

Unscheduled maintenance workflow TBD. Relationship to inspection programme, scheduled tasks, and component life management TBD.

## 8. Detailed Design

Not applicable — process and task specification only. No design implementation is implied or authorised by this document.

## 9. Interfaces

- Interface to maintenance programme HFPX-MNT-PRG-001 (TBD)
- Interface to inspection findings and fault isolation (TBD)
- Interface to maintenance records specification (TBD)
- Interface to Vol 24 and Vol 28 artefacts (TBD)

## 10. Operational Concept

Unscheduled maintenance is initiated on trigger, scoped from findings, executed under applicable precautions, and closed with records. End-to-end flow TBD.

## 11. Safety

Safety implications of responding to faults and findings TBD. Precautions TBD. No unscheduled action is interpreted as permission to operate outside controlled conditions.

## 12. Performance

Responsiveness and coverage expectations TBD. No limits are stated at this revision.

## 13. Verification & Validation

| Requirement | Method | Notes |
| --- | --- | --- |
| REQ-HFPX-LUM-001..002, REQ-HFPX-LUM-004 | Inspection | Triggers, process, and recording inspected against programme (artefacts TBD) |
| REQ-HFPX-LUM-003 | Demonstration | Scoping of actions from findings demonstrated where exercised (scope TBD) |

## 14. Risks

- Undefined triggers may delay response to findings; mitigation TBD
- Undefined scoping basis may produce inconsistent corrective action; mitigation TBD

## 15. Open Issues

- Trigger criteria TBD
- Response process TBD
- Scoping basis TBD
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

Parents: REQ-HFPX-STK-005. Children: unscheduled task specifications and associated verification cases (TBD). Hooks to Vol 24 and Vol 28 artefacts TBD.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Changes after issue require change records (process TBD).

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial draft (Chapter 27.3) |
