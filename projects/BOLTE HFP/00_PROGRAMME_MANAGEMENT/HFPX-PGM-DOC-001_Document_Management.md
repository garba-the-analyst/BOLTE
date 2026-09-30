# Document Management

**Document ID:** HFPX-PGM-DOC-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define document management for HFP-X: identifier scheme, template compliance, review and approval workflow, and retention. Owns Chapter 00.8.

## 2. Scope

Covers all controlled programme documents across programme volumes. Covers identification, structure, review, approval, release and retention. Does not set technical values.

## 3. Applicable Documents

- HFPX-PGM-CHR-001 Programme Charter
- HFPX-PGM-SEM-001 SEMP
- HFPX-PGM-CFG-001 Configuration Management (version and baseline control)
- HFPX-PGM-TDM-001 Technical Data Management (data handling and retention linkage)

## 4. Definitions & Acronyms

- Document identifier: controlled reference of form HFPX-<DOMAIN>-<TYPE>-<NNN>
- Template: controlled section structure applied to programme documents
- Review / approval: examination and authorisation prior to release or baselining
- TBD / TBC: to be determined / to be confirmed

## 5. System Context

Document control structures programme knowledge:

```text
TEMPLATE → AUTHORING → REVIEW → APPROVAL → RELEASE → BASELINE → RETENTION
   ↑_______________ IDENTIFIER AND VERSION CONTROL _______________↑
```

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-GDC-001 | The programme shall identify controlled documents using the scheme HFPX-<DOMAIN>-<TYPE>-<NNN>. | DDR-003 | Inspection |
| REQ-HFPX-GDC-002 | The programme shall author controlled documents against the controlled template structure, with compliance verified at each applicable gate. | REQ-HFPX-PGM-001 | Inspection |
| REQ-HFPX-GDC-003 | The programme shall control document review and approval through a defined workflow, with roles and sequencing recorded as TBD at this revision. | REQ-HFPX-PGM-004 | Inspection |
| REQ-HFPX-GDC-004 | The programme shall retain controlled documents under defined retention provisions, recorded as TBD at this revision. | REQ-HFPX-PGM-004 | Inspection |

## 7. Architecture

Document management architecture TBD. Elements: identifier allocation, template, review and approval chain, release and retention store. Custodianship and tooling TBD.

## 8. Detailed Design

Identifier allocation rules, template compliance checklist, review and approval workflow and retention schedule TBD. Released documents shall carry header, revision, status, configuration, owner, approver and date. No retention durations are stated at this revision.

## 9. Interfaces

- To configuration (00.7): version control and baselining of documents
- To requirements (00.9): requirements contained in controlled documents
- To technical data (00.15): data artefacts supporting documents
- To reviews (00.14): required documents presented at gates

## 10. Operational Concept

Documents are identified, authored to template, reviewed, approved, released and retained. Review sequencing and retention handling TBD.

## 11. Safety

Safety documents shall be reviewed with safety authority involvement. Safety review provisions TBD.

## 12. Performance

Document management performance indicators TBD. No thresholds are baselined at this revision.

## 13. Verification & Validation

This document is verified by inspection against the document template checklist at the applicable gate. Validation is by programme authority approval (approver TBD).

## 14. Risks

- Identifier collisions or uncontrolled variants; mitigation TBD
- Template non-compliance obscuring missing content; mitigation TBD
- Review bypass releasing unexamined material; mitigation TBD

## 15. Open Issues

_TBD_

All open issues are recorded in the issue register. No issue is closed by this revision.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on identifier scheme (DDR-003), configuration control (00.7), review workflow needs (00.14) and retention policy (00.15).

## 18. Traceability

Parent: HFPX-PGM-CHR-001 (REQ-HFPX-PGM-001/004) and DDR-003. Children: document register, review records, retention schedule (all TBD). RTM: REQ-HFPX-GDC-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 00.8) |
