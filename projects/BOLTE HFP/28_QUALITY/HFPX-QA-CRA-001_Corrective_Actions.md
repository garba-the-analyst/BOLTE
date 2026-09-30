# Corrective Actions

**Document ID:** HFPX-QA-CRA-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the structure-only corrective action approach for HFP-X: how causes of non-conformances and quality issues are investigated, acted upon, checked for effectiveness, and closed. This document owns Chapter 28.7 and does not set technical values.

## 2. Scope

Covers root-cause investigation intent, action planning and tracking, effectiveness evaluation, and closure governance. Includes intake from non-conformance management, audits, supplier issues, and production feedback. Detailed methods, responsibilities, and timing provisions remain TBD.

## 3. Applicable Documents

- HFPX-QA-QMS-001 Quality Management System
- HFPX-QA-NCM-001 Non-Conformance Management
- HFPX-QA-SUQ-001 Supplier Quality (for supplier-related actions, TBD)
- Vol 20 Manufacturing (implementation of actions in production, TBD)
- Vol 25.8 Certification and quality liaison (TBD)

## 4. Definitions & Acronyms

- Corrective action: action addressing causes to prevent recurrence (scope TBD)
- Root-cause analysis: structured investigation of causes (method TBD)
- Effectiveness check: evaluation that actions achieved intended prevention of recurrence (method TBD)
- Closure: authorised completion of the corrective action file (authority TBD)
- TBD/TBC: unknown data markers

## 5. System Context

Corrective actions close the improvement loop:

```text
FINDING (NCM / AUDIT / SUPPLIER / PRODUCTION) → INVESTIGATE CAUSE (28.7) → ACT → CHECK EFFECTIVENESS → CLOSE
                                                         ↓
                                              PRODUCTION + QMS UPDATE (Vol 20 / 28.1)
```

Containment stays in HFPX-QA-NCM-001; prevention of recurrence is governed here.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-ZCA-001 | The programme shall define root-cause investigation provisions for issues transferred to corrective action. Methods and responsibilities remain TBD. | Quality improvement classification / HFPX-QA-NCM-001 | Inspection |
| REQ-HFPX-ZCA-002 | The programme shall define corrective action planning and tracking, including action ownership, traceability to findings, and status control. Tracking details remain TBD. | Quality classification / Vol 20 implementation | Inspection |
| REQ-HFPX-ZCA-003 | The programme shall evaluate effectiveness of corrective actions against defined effectiveness intent before closure. Evaluation methods remain TBD. | Quality assurance classification / Vol 25.8 liaison | Inspection |
| REQ-HFPX-ZCA-004 | The programme shall govern closure of corrective actions through defined authority and records. Closure criteria and authority remain TBD. | Quality records classification | Inspection |

## 7. Architecture

Corrective action structure (TBD): intake and grading, investigation file, action plan, implementation evidence, effectiveness evaluation, closure record. Grading between correction, corrective action, and improvement opportunity remains TBD.

## 8. Detailed Design

To be defined. Intended elements include: intake criteria from NCM, audit, and supplier channels (TBD), investigation approach without prescribing a method (TBD), action plan structure (TBD), tracking register structure without presupposing tooling (TBD), effectiveness evaluation structure (TBD), closure authorisation (TBD). No time values, thresholds, or effectiveness metrics are set in this revision.

## 9. Interfaces

- CRA ↔ HFPX-QA-NCM-001: intake of non-conformances requiring action (TBD)
- CRA ↔ HFPX-QA-SUQ-001: supplier-related actions and flow-down (TBD)
- CRA ↔ Vol 20: implementation of process and instruction changes (TBD)
- CRA ↔ HFPX-QA-QMS-001: QMS updates from systemic learning (TBD)
- CRA ↔ HFPX-QA-CCB-001: configuration control of resulting changes (TBD)

## 10. Operational Concept

Findings graded for action are investigated, actions are planned with owners, implementation is tracked to evidence, effectiveness is evaluated, and files close only through authorised review. Reopening provisions for ineffective actions remain TBD.

## 11. Safety

Corrective actions support safety by addressing causes of safety-relevant findings and preventing recurrence. Escalation of safety-relevant actions to the safety programme and any independence provisions remain TBD. No safety values set in this document.

## 12. Performance

Measures of corrective action throughput and recurrence prevention remain TBD in qualitative form, without targets or thresholds in this revision. No performance values baselined.

## 13. Verification & Validation

This document is verified by inspection against the template checklist. Corrective action implementation is verified by inspection and audit of action files and effectiveness evidence (criteria TBD). Validation is programme authority approval (path TBD).

## 14. Risks

- Cause unidentified → actions address symptoms; mitigation: investigation provisions per REQ-HFPX-ZCA-001 (TBD)
- Actions untracked → loss of control; mitigation: planning and tracking per REQ-HFPX-ZCA-002 (TBD)
- Premature closure → recurrence; mitigation: effectiveness evaluation per REQ-HFPX-ZCA-003 and closure governance per REQ-HFPX-ZCA-004 (TBD)

## 15. Open Issues

- Investigation methods and responsibilities (TBD)
- Action-tracking structure and ownership (TBD)
- Effectiveness evaluation methods (TBD)
- Closure criteria and authority (TBD)

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on HFPX-QA-NCM-001 (intake), HFPX-QA-QMS-001 (framework), Vol 20 (implementation), and HFPX-QA-CCB-001 (change control). Supports QMS improvement and supplier quality where applicable.

## 18. Traceability

Parent: manufacturing and quality classification; Vol 20 Manufacturing, Vol 25.8 quality liaison. Children: implemented changes via Vol 20 and configuration control; learning to QMS. RTM: REQ-HFPX-ZCA-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 28.7) |
