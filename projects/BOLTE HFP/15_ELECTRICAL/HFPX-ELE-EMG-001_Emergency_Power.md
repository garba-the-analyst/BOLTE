# Emergency Power

**Document ID:** HFPX-ELE-EMG-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the emergency power structure (Chapter 15.8): role, covered states, load-feed provisions, and interfaces. Structure only; no source selection or ratings are made.

## 2. Scope

Covers emergency source role and its feeds to designated loads, including Vol 13.16 safety loads (TBD). Excludes ratings, endurance, schematics, and load values (all TBD).

## 3. Applicable Documents

- HFPX-ELE-ARC-001 Electrical Architecture (parent structure)
- HFPX-ARC-PWR-001 Power Architecture (SAD PWR view parent)
- HFPX-SYS-REQ-001 SyRS (SYS tier parent)
- Vol 13 Chapter 13.16 (safety load hook, TBD)

## 4. Definitions & Acronyms

- Emergency power: source role for defined degraded and emergency states (rating TBD).
- Safety load: designated load sustained in emergency states (list TBD).

## 5. System Context

Emergency power interfaces with distribution, protection, control, and designated avionics, helmet, sensor, and safety loads. It activates on defined loss or degradation of normal sources.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-EEP-001 | The emergency power structure shall define the emergency source role and covered states (ratings TBD). | HFPX-ELE-ARC-001; SAD PWR view; SYS tier | Inspection |
| REQ-HFPX-EEP-002 | The emergency power structure shall define emergency feeds to designated loads including Vol 13.16 safety loads (lists TBD). | HFPX-ELE-ARC-001; Vol 13.16 hook | Inspection |
| REQ-HFPX-EEP-003 | The emergency power structure shall define activation and transfer behaviour structure (logic TBD). | HFPX-ELE-ARC-001; SAD PWR view; Vol 13.16 hook | Analysis |
| REQ-HFPX-EEP-004 | The emergency power structure shall define emergency-source status and control interface structure (details TBD). | HFPX-ELE-ARC-001; SYS tier | Inspection |

## 7. Architecture

Emergency source block (TBD) → segregated emergency buses and feeders (TBD) → designated load interfaces (TBD), with activation paths (TBD) and status to power management (TBD). No ratings, endurance values, or schematics stated.

## 8. Detailed Design

Not applicable at this revision. Source selection, sizing, and schematics deferred. No electrical values stated.

## 9. Interfaces

Emergency outputs to distribution, activation inputs, status / control to power management and crew interfaces. Definitions TBD in ICDs.

## 10. Operational Concept

Emergency power supports defined emergency states; activation may be automatic, crew-commanded, or both (TBD). Return-to-normal concepts (TBD) align with CONOPS degraded states.

## 11. Safety

Failure to activate, premature deactivation, and safety-load coverage cases feed Vol 13.16 analyses. No safety values stated.

## 12. Performance

Endurance and power-quality allocations are TBD. No values stated.

## 13. Verification & Validation

Verified by inspection (role and feed coverage) and analysis (activation and coverage concepts). Validated later by integration test. Pass/fail criteria TBD.

## 14. Risks

- Incomplete safety-load coverage; mitigation: Vol 13.16 load-list completion (TBD).
- Activation failure; mitigation: activation concept redundancy review (TBD).

## 15. Open Issues

Source selection, ratings, covered states, safety-load list, activation logic, and endurance TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on HFPX-ELE-ARC-001, SAD PWR view, distribution structure (Chapter 15.5), and Vol 13.16 safety-load inputs.

## 18. Traceability

Parents: SYS tier; SAD PWR view (HFPX-ARC-PWR-001); HFPX-ELE-ARC-001; Vol 13.16 hook (TBD). Children: ICDs, V&V cases. RTM: REQ-HFPX-EEP-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Chapter 15.8.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 15.8) |
