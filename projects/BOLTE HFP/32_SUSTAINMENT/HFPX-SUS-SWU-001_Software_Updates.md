# Software Updates

**Document ID:** HFPX-SUS-SWU-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define how HFP-X software updates are planned, verified and released through sustainment without compromising safety or configuration control. Owns Chapter 32.7.

## 2. Scope

Covers software update planning, release governance, regression assurance linkage and airworthiness linkage. Does not set technical values. Update and release approach is TBD; regression provisions are TBD (Vol 16.16 hooks); airworthiness hooks are TBD (Vol 25.9 hooks).

## 3. Applicable Documents

- HFPX-SUS-CBL-001 Configuration Baselines
- HFPX-SUS-CIM-001 Continuous Improvement
- Software assurance and regression concepts (Vol 16.16 hooks, details TBD)
- Airworthiness and certification concepts (Vol 25.9 hooks, details TBD)
- Vol 24 safety assurance concepts (details TBD)
- Programme change control (00.10 hooks, details TBD)

## 4. Definitions & Acronyms

- Software update: a controlled change to fielded software embodied through a defined release
- Release: an authorised distribution of software with associated evidence and records
- TBD/TBC: unknown data markers; unknown values are never invented

## 5. System Context

Software updates flow through assurance into the field:

```text
CHANGE NEED → UPDATE DEVELOPMENT → REGRESSION ASSURANCE (TBD) → RELEASE → FIELD EMBODIMENT
   ↑________ Vol 16.16 REGRESSION HOOKS ________↑
   ↑________ Vol 25.9 AIRWORTHINESS HOOKS ______↑
```

Release scope, assurance depth and embodiment control remain TBD at this revision.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-USU-001 | Software updates shall be planned and released through a defined and controlled release process. | Lifecycle phase definition (TBD) | Inspection |
| REQ-HFPX-USU-002 | Software updates shall undergo defined regression assurance before release. | Vol 16.16 hooks (TBD) | Test |
| REQ-HFPX-USU-003 | Software releases with airworthiness relevance shall retain alignment with airworthiness provisions. | Vol 25.9 hooks (TBD) | Inspection |
| REQ-HFPX-USU-004 | Fielded software configuration shall be recorded with traceability to the authorised release and evidence. | Vol 28 hooks (TBD) | Demonstration |

## 7. Architecture

Update governance (roles TBD): software design authority, assurance authority, release authority and safety concurrence with responsibilities TBD. Repository and release infrastructure TBD.

## 8. Detailed Design

Release planning, assurance activities, acceptance criteria and field embodiment steps to be defined (TBD). Update and release approach is TBD and not baselined at this revision.

## 9. Interfaces

- Updates ↔ regression assurance (Vol 16.16) for verification depth
- Updates ↔ airworthiness (Vol 25.9) for approval linkage
- Updates ↔ configuration (32.2) and change control (00.10) for embodiment governance
- Updates ↔ safety (Vol 24) for safety-relevant assessment

## 10. Operational Concept

Updates operate as a pipeline: need → plan → develop → assure → approve → release → embody → record. Release forums and embodiment windows TBD.

## 11. Safety

Software updates with safety relevance require safety assessment and release concurrence (mechanisms TBD, Vol 24 hooks). No safety thresholds are set in this document.

## 12. Performance

Update indicators TBD (assurance completeness criteria TBD, release record completeness criteria TBD). No thresholds baselined.

## 13. Verification & Validation

This document is verified by inspection against the document template checklist (header, 20 sections, IDs, traceability). Requirements REQ-HFPX-USU-001..004 verified per §6. Validation: programme authority approval (TBD).

## 14. Risks

- Undefined release process → uncontrolled fielded software; mitigation: define release governance (TBD)
- Inadequate regression → introduced faults; mitigation: Vol 16.16 assurance linkage (TBD)
- Airworthiness misalignment → unauthorised operation; mitigation: Vol 25.9 linkage (TBD)

## 15. Open Issues

Release process, regression scope, airworthiness interface and embodiment control to be defined. All open details recorded as TBD.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on Vol 16.16 regression concepts, Vol 25.9 airworthiness concepts, configuration baselines (32.2), programme change control (00.10) and Vol 24 safety assurance.

## 18. Traceability

Parent: lifecycle phase definition, Vol 16.16 / Vol 25.9 / Vol 24 / Vol 28 hooks. Children: fielded release records and fleet embodiment status (TBD). RTM: REQ-HFPX-USU-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 32.7) |
