# Hydraulic/Pneumatic Schematics

**Document ID:** HFPX-TDATA-HYD-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the Hydraulic/Pneumatic Schematics data deliverable control for HFP-X: schematic structure, format, approval and revision practice. Owns Chapter 29.7.

## 2. Scope

Covers structural control of the Hydraulic/Pneumatic Schematics deliverable across programme volumes. Covers definition, format and exchange standard, approval and release, and revision practice. Does not contain schematic content itself and does not set technical values.

## 3. Applicable Documents

- HFPX-PGM-DOC-001 Document Management
- HFPX-PGM-TDM-001 Technical Data Management
- HFPX-PGM-CFG-001 Configuration Management
- Vol 21 / 27 / 28 consumer volumes (TBD)

## 4. Definitions & Acronyms

- Hydraulic/Pneumatic Schematics: controlled depictions of fluid power connectivity and associated schematic structure
- Format / exchange standard: controlled representation and transfer provisions for the schematic deliverable
- Approval / release: authorisation and issue provisions for the schematic deliverable
- TBD / TBC: to be determined / to be confirmed

## 5. System Context

Technical data control structures the schematic deliverable:

```text
DEFINITION → FORMAT → APPROVAL → RELEASE → REVISION CONTROL
   ↑_______________ IDENTIFIER AND VERSION CONTROL _______________↑
```

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-JHP-001 | The programme shall define the Hydraulic/Pneumatic Schematics structure, content rules and source-data linkage, recorded as TBD at this revision. | HFPX-PGM-TDM-001; Vol 21/27/28 consumers (TBD) | Inspection |
| REQ-HFPX-JHP-002 | The programme shall control the Hydraulic/Pneumatic Schematics format and exchange standard, recorded as TBD at this revision. | HFPX-PGM-DOC-001; Vol 21/27/28 consumers (TBD) | Inspection |
| REQ-HFPX-JHP-003 | The programme shall control Hydraulic/Pneumatic Schematics approval, release and access provisions, recorded as TBD at this revision. | HFPX-PGM-DOC-001; Vol 21/27/28 consumers (TBD) | Inspection |
| REQ-HFPX-JHP-004 | The programme shall control Hydraulic/Pneumatic Schematics revision practice and change traceability, recorded as TBD at this revision. | HFPX-PGM-CFG-001; Vol 21/27/28 consumers (TBD) | Inspection |

## 7. Architecture

Hydraulic/Pneumatic Schematics control architecture TBD. Elements: schematic schema, connectivity depiction rules, identifier linkage, format store, approval chain and revision record. Custodianship and tooling TBD.

## 8. Detailed Design

Schematic definition, format and exchange provisions, approval and release workflow and revision practice TBD. Released deliverables shall carry header, revision, status, configuration, owner, approver and date. No schematic content or values are stated at this revision.

## 9. Interfaces

- To document control (00.8): approval and release of the schematic deliverable
- To technical data management (00.15): data handling and retention linkage
- To configuration (00.7): version control and baselining of the schematic deliverable
- To Vol 21 / 27 / 28: consumer use of the controlled schematic structure

## 10. Operational Concept

Hydraulic/Pneumatic Schematics are defined, formatted to standard, approved, released and revised under control. Sequencing and handling TBD.

## 11. Safety

Safety-related schematic depiction provisions TBD. Safety review involvement TBD.

## 12. Performance

Schematic control performance indicators TBD. No thresholds are baselined at this revision.

## 13. Verification & Validation

This document is verified by inspection against the document template checklist at the applicable gate. Validation is by programme authority approval (approver TBD).

## 14. Risks

- Incomplete schematic structure obscuring missing connections; mitigation TBD
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

Parent: HFPX-PGM-DOC-001, HFPX-PGM-TDM-001 and HFPX-PGM-CFG-001; Vol 21/27/28 consumers (TBD). Children: schematic schema, format record, release records, revision records (all TBD). RTM: REQ-HFPX-JHP-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 29.7) |
