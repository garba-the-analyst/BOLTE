# Technical Data Management

**Document ID:** HFPX-PGM-TDM-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define technical data management for HFP-X: data classes, design-data control, access and protection, and retention. Owns Chapter 00.15.

## 2. Scope

Covers technical data supporting requirements, design, analysis, test and operation, including CAD and drawing artefacts. Covers access, protection and retention. Does not set technical values.

## 3. Applicable Documents

- HFPX-PGM-CHR-001 Programme Charter
- HFPX-PGM-SEM-001 SEMP
- HFPX-PGM-DOC-001 Document Management (document control linkage)
- HFPX-PGM-CFG-001 Configuration Management (data baselines)
- Design-data provisions with CAD and drawing control hooks (Vol 29)

## 4. Definitions & Acronyms

- Technical data: models, drawings, analyses, test data and supporting artefacts
- CAD: computer-aided design model data
- Access / protection: provisions governing availability, integrity and disclosure control
- TBD / TBC: to be determined / to be confirmed

## 5. System Context

Data management underpins design integrity and evidence:

```text
DATA CREATION → CONTROL → ACCESS → USE → BASELINE → RETENTION
   ↑_______________ CAD / DRAWING CONTROL _______________↑
```

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-GTD-001 | The programme shall define technical data classes, with class definitions and handling provisions recorded as TBD at this revision. | REQ-HFPX-PGM-001 | Inspection |
| REQ-HFPX-GTD-002 | The programme shall control CAD and drawing data through provisions linked to Vol 29, with control details recorded as TBD at this revision. | REQ-HFPX-PGM-001 | Inspection |
| REQ-HFPX-GTD-003 | The programme shall control technical-data access and protection, with provisions recorded as TBD at this revision. | REQ-HFPX-PGM-004 | Inspection |
| REQ-HFPX-GTD-004 | The programme shall retain technical data under defined retention provisions, recorded as TBD at this revision. | REQ-HFPX-PGM-004 | Inspection |

## 7. Architecture

Data management architecture TBD. Elements: data classes, CAD and drawing control, access provisions, retention store. Custodianship and tooling TBD.

## 8. Detailed Design

Data-class definitions, CAD and drawing control linkage, access and protection rules and retention schedule TBD. Controlled data shall carry identification and version. No retention durations are stated at this revision.

## 9. Interfaces

- To document management (00.8): data supporting controlled documents
- To configuration (00.7): data baselines and version control
- To design volumes: CAD and drawing data creation and use
- To V&V: test data handling and evidence linkage

## 10. Operational Concept

Data is classified, controlled, made available to authorised users, baselined with its parent artefact and retained per schedule. Classification and access-granting workflow TBD.

## 11. Safety

Safety-related data shall be protected for integrity and available to the safety authority. Safety data provisions TBD.

## 12. Performance

Data management performance indicators TBD. No thresholds are baselined at this revision.

## 13. Verification & Validation

This document is verified by inspection against the document template checklist at the applicable gate. Validation is by programme authority approval (approver TBD).

## 14. Risks

- Unclassified data escaping control; mitigation TBD
- CAD and drawing variants diverging; mitigation TBD
- Access failure blocking authorised use or permitting unauthorised disclosure; mitigation TBD

## 15. Open Issues

_TBD_

All open issues are recorded in the issue register. No issue is closed by this revision.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on document control (00.8), configuration control (00.7), design-data provisions and retention policy.

## 18. Traceability

Parent: HFPX-PGM-CHR-001 (REQ-HFPX-PGM-001/004). Children: data-class register, CAD control procedure, retention schedule (all TBD). RTM: REQ-HFPX-GTD-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 00.15) |
