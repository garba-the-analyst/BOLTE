# Configuration Management

**Document ID:** HFPX-PGM-CFG-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define configuration management for HFP-X: baselines, configuration-item identification, baseline-change control and status accounting. Owns Chapter 00.7.

## 2. Scope

Covers identification, baselining, change control and status accounting for documents, requirements, interfaces and evidence. Change-record workflow detail is owned by change management (00.10). Does not set technical values.

## 3. Applicable Documents

- HFPX-PGM-CHR-001 Programme Charter
- HFPX-PGM-SEM-001 SEMP
- HFPX-PGM-CHG-001 Change Management (change workflow)
- HFPX-PGM-DOC-001 Document Management (document control)
- HFPX-PGM-BSL-001 Master Technical Baseline

## 4. Definitions & Acronyms

- BL: configuration baseline; BL-0.0 is structure only with no technical values approved
- Configuration item: artefact placed under configuration control
- Status accounting: recording of baseline content, versions and change state
- TBD / TBC: to be determined / to be confirmed

## 5. System Context

Configuration control binds documentation, requirements and evidence:

```text
CONFIGURATION ITEMS → BASELINES → CONTROLLED CHANGES → STATUS ACCOUNTING
        ↑________________ TRACEABILITY (RTM) ________________↑
```

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-GCF-001 | The programme shall maintain a defined baseline scheme, with baseline content and approval provisions recorded as TBD at this revision. | REQ-HFPX-PGM-001 | Inspection |
| REQ-HFPX-GCF-002 | The programme shall identify configuration items, with identification rules and item lists recorded as TBD at this revision. | DDR-002 | Inspection |
| REQ-HFPX-GCF-003 | The programme shall control baseline changes so that no baselined item is silently changed; each change identifies affected requirements, subsystems, interfaces and evidence. | REQ-HFPX-PGM-012 | Demonstration |
| REQ-HFPX-GCF-004 | The programme shall maintain configuration status accounting, with records and reporting provisions recorded as TBD at this revision. | REQ-HFPX-PGM-002 | Inspection |

## 7. Architecture

Configuration architecture TBD. Elements: configuration-item register, baselines, change records, status accounting reports. Tooling and custodianship TBD.

## 8. Detailed Design

Baseline scheme, identification rules, change-control linkage and status-accounting format TBD. Baselined material shall change only through approved change records. No baseline content values are stated at this revision.

## 9. Interfaces

- To change management (00.10): change-record workflow enacting baseline change
- To document management (00.8): document versions under configuration control
- To requirements management (00.9): requirements baselines and RTM linkage
- To interface management (00.11): interface baselines
- To Master Technical Baseline: consolidation of baselined content

## 10. Operational Concept

Items are identified, baselined at gates, changed only by approved records, and reported through status accounting. Identification, baselining and reporting cadence TBD.

## 11. Safety

Safety-related configuration items and safety baselines shall be identified and controlled with safety authority visibility. Safety configuration provisions TBD.

## 12. Performance

Configuration performance indicators TBD. No thresholds are baselined at this revision.

## 13. Verification & Validation

This document is verified by inspection against the document template checklist at the applicable gate. Validation is by programme authority approval (approver TBD).

## 14. Risks

- Uncontrolled change to baselined material; mitigation TBD
- Incomplete configuration-item identification causing gaps in control; mitigation TBD
- Status accounting lagging actual baseline state; mitigation TBD

## 15. Open Issues

_TBD_

All open issues are recorded in the issue register. No issue is closed by this revision.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on Charter baseline policy, SEMP baseline rule, change workflow (00.10), document control (00.8) and RTM discipline (00.9).

## 18. Traceability

Parent: HFPX-PGM-CHR-001 (REQ-HFPX-PGM-001/002), HFPX-PGM-SEM-001 (REQ-HFPX-PGM-012) and DDR-002. Children: configuration-item list, baselines, status accounting reports (all TBD). RTM: REQ-HFPX-GCF-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 00.7) |
