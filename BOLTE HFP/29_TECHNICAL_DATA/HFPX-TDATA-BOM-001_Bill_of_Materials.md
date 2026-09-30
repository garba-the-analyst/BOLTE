# Bill of Materials

**Document ID:** HFPX-TDATA-BOM-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the Bill of Materials data deliverable control for HFP-X: breakdown structure, format, approval and revision practice. Owns Chapter 29.2.

## 2. Scope

Covers structural control of the Bill of Materials deliverable across programme volumes. Covers definition, format and exchange standard, approval and release, and revision practice. Does not contain materials data itself and does not set technical values.

## 3. Applicable Documents

- HFPX-PGM-DOC-001 Document Management
- HFPX-PGM-TDM-001 Technical Data Management
- HFPX-PGM-CFG-001 Configuration Management
- Vol 21 / 27 / 28 consumer volumes (TBD)

## 4. Definitions & Acronyms

- Bill of Materials: controlled quantity-structured breakdown linking assemblies to constituent parts
- Format / exchange standard: controlled representation and transfer provisions for the breakdown deliverable
- Approval / release: authorisation and issue provisions for the breakdown deliverable
- TBD / TBC: to be determined / to be confirmed

## 5. System Context

Technical data control structures the breakdown deliverable:

```text
DEFINITION → FORMAT → APPROVAL → RELEASE → REVISION CONTROL
   ↑_______________ IDENTIFIER AND VERSION CONTROL _______________↑
```

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-JBM-001 | The programme shall define the Bill of Materials structure, content rules and source-data linkage, recorded as TBD at this revision. | HFPX-PGM-TDM-001; Vol 21/27/28 consumers (TBD) | Inspection |
| REQ-HFPX-JBM-002 | The programme shall control the Bill of Materials format and exchange standard, recorded as TBD at this revision. | HFPX-PGM-DOC-001; Vol 21/27/28 consumers (TBD) | Inspection |
| REQ-HFPX-JBM-003 | The programme shall control Bill of Materials approval, release and access provisions, recorded as TBD at this revision. | HFPX-PGM-DOC-001; Vol 21/27/28 consumers (TBD) | Inspection |
| REQ-HFPX-JBM-004 | The programme shall control Bill of Materials revision practice and change traceability, recorded as TBD at this revision. | HFPX-PGM-CFG-001; Vol 21/27/28 consumers (TBD) | Inspection |

## 7. Architecture

Bill of Materials control architecture TBD. Elements: breakdown schema, quantity rules, identifier linkage, format store, approval chain and revision record. Custodianship and tooling TBD.

## 8. Detailed Design

Breakdown definition, format and exchange provisions, approval and release workflow and revision practice TBD. Released deliverables shall carry header, revision, status, configuration, owner, approver and date. No breakdown content or values are stated at this revision.

## 9. Interfaces

- To document control (00.8): approval and release of the breakdown deliverable
- To technical data management (00.15): data handling and retention linkage
- To configuration (00.7): version control and baselining of the breakdown deliverable
- To Vol 21 / 27 / 28: consumer use of the controlled breakdown structure

## 10. Operational Concept

The Bill of Materials structure is defined, formatted to standard, approved, released and revised under control. Sequencing and handling TBD.

## 11. Safety

Safety-related breakdown provisions TBD. Safety review involvement TBD.

## 12. Performance

Breakdown control performance indicators TBD. No thresholds are baselined at this revision.

## 13. Verification & Validation

This document is verified by inspection against the document template checklist at the applicable gate. Validation is by programme authority approval (approver TBD).

## 14. Risks

- Incomplete breakdown structure obscuring missing constituents; mitigation TBD
- Uncontrolled format variants impeding exchange; mitigation TBD
- Unrecorded revisions breaking traceability; mitigation TBD

## 15. Open Issues

_TBD_

All open issues are recorded in the issue register. No issue is closed by this revision.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on document control (00.8), technical data management (00.15), configuration control (00.7) and consumer needs of Vol 21 / 27 / 28.

## 18. Traceability

Parent: HFPX-PGM-DOC-001, HFPX-PGM-TDM-001 and HFPX-PGM-CFG-001; Vol 21/27/28 consumers (TBD). Children: breakdown schema, format record, release records, revision records (all TBD). RTM: REQ-HFPX-JBM-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 29.2) |
