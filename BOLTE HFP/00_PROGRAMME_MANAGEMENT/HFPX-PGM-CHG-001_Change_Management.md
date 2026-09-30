# Change Management

**Document ID:** HFPX-PGM-CHG-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define change management for HFP-X: change-record contents, control authority, emergency provisions and change-to-evidence flow. Owns Chapter 00.10.

## 2. Scope

Covers changes to baselined requirements, architecture, interfaces, documents and evidence. Covers standard and emergency paths. Does not set technical values.

## 3. Applicable Documents

- HFPX-PGM-CHR-001 Programme Charter
- HFPX-PGM-SEM-001 SEMP
- HFPX-PGM-CFG-001 Configuration Management (baseline control)
- HFPX-PGM-RQM-001 Requirements Management (requirement change linkage)
- HFPX-PGM-REV-001 Design Reviews (gate action linkage)

## 4. Definitions & Acronyms

- Change record: controlled account of a proposed and decided change
- CCB: Configuration Control Board or equivalent change authority (composition TBD)
- Emergency change: change requiring expedited handling under defined conditions
- TBD / TBC: to be determined / to be confirmed

## 5. System Context

Change control protects baselines while allowing evolution:

```text
CHANGE REQUEST → IMPACT ASSESSMENT → DECISION → IMPLEMENTATION
    → EVIDENCE UPDATE → BASELINE → STATUS ACCOUNTING
```

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-GCH-001 | The programme shall record each change in a change record addressing prompt §31 items 1–10, with field definitions recorded as TBD at this revision. | REQ-HFPX-PGM-012 | Inspection |
| REQ-HFPX-GCH-002 | The programme shall decide changes through a defined change authority, with composition and approval thresholds recorded as TBD at this revision. | REQ-HFPX-PGM-012 | Inspection |
| REQ-HFPX-GCH-003 | The programme shall control emergency changes through a defined expedited rule, with conditions and retrospective provisions recorded as TBD at this revision. | REQ-HFPX-PGM-012 | Demonstration |
| REQ-HFPX-GCH-004 | The programme shall flow each approved change through to affected requirements, design, interfaces and evidence, with completion verified before baseline update. | REQ-HFPX-PGM-002 | Demonstration |

## 7. Architecture

Change architecture TBD. Elements: change register, impact assessment, decision authority, implementation tracking, evidence linkage, status accounting update. Roles and tooling TBD.

## 8. Detailed Design

Change-record format covering prompt §31 items 1–10, decision workflow, emergency-change procedure and change-to-evidence closure checks TBD. No baselined item shall change without an approved record. No approval thresholds are stated at this revision.

## 9. Interfaces

- To configuration (00.7): baseline update following approved change
- To requirements (00.9): requirement impact and RTM update
- To interface management (00.11): interface impact assessment
- To reviews (00.14): gate actions handled as changes where applicable
- To change register: living record of change state

## 10. Operational Concept

Changes are raised, assessed for impact on requirements, subsystems, interfaces and evidence, decided, implemented and closed with evidence updated. Emergency handling follows the expedited rule with later reconciliation. Processing expectations TBD.

## 11. Safety

Safety-impacting changes shall receive safety authority review. Safety review trigger and concurrence provisions TBD.

## 12. Performance

Change performance indicators TBD. No thresholds are baselined at this revision.

## 13. Verification & Validation

This document is verified by inspection against the document template checklist at the applicable gate. Validation is by programme authority approval (approver TBD).

## 14. Risks

- Changes implemented without records, corrupting baselines; mitigation TBD
- Impact assessment missing interfaces or evidence; mitigation TBD
- Emergency path overused to bypass scrutiny; mitigation TBD

## 15. Open Issues

_TBD_

All open issues are recorded in the issue register. No issue is closed by this revision.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SEMP change rule, configuration baselines (00.7), requirement traceability (00.9) and gate action handling (00.14).

## 18. Traceability

Parent: HFPX-PGM-SEM-001 (REQ-HFPX-PGM-012) and HFPX-PGM-CHR-001 (REQ-HFPX-PGM-002). Children: change procedure, change register entries, evidence-update records (all TBD). RTM: REQ-HFPX-GCH-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 00.10) |
