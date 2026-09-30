# Interface Management

**Document ID:** HFPX-PGM-IFM-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define interface management for HFP-X: register ownership, interface control discipline, interface change control and interface verification. Owns Chapter 00.11.

## 2. Scope

Covers programme, system and subsystem interfaces, including interface registers and interface control documents. Detailed interface values are owned by architecture and subsystem volumes. Does not set technical values.

## 3. Applicable Documents

- HFPX-PGM-CHR-001 Programme Charter
- HFPX-PGM-SEM-001 SEMP
- HFPX-PGM-CFG-001 Configuration Management (interface baselines)
- HFPX-PGM-CHG-001 Change Management (interface change workflow)
- HFPX-PGM-REV-001 Design Reviews (CDR gate provisions)

## 4. Definitions & Acronyms

- Interface: boundary across which systems, subsystems or organisations interact
- ICD: Interface Control Document
- Interface register: controlled list of interfaces and their control state
- TBD / TBC: to be determined / to be confirmed

## 5. System Context

Interface management binds architecture, design and verification:

```text
INTERFACE IDENTIFICATION → REGISTER → ICD → BASELINE
    → CHANGE CONTROL → VERIFICATION
```

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-GIF-001 | The programme shall maintain interface register ownership with defined custodianship and update provisions, recorded as TBD at this revision. | REQ-HFPX-PGM-002 | Inspection |
| REQ-HFPX-GIF-002 | The programme shall place interfaces under interface control documentation before CDR, with document scope and approval provisions recorded as TBD at this revision. | REQ-HFPX-PGM-003 | Inspection |
| REQ-HFPX-GIF-003 | The programme shall control interface changes so that no baselined interface is changed without an approved change record assessing both sides of the interface. | REQ-HFPX-PGM-012 | Demonstration |
| REQ-HFPX-GIF-004 | The programme shall verify interfaces against their control documentation, with verification methods and acceptance provisions recorded as TBD at this revision. | REQ-HFPX-PGM-002 | Inspection |

## 7. Architecture

Interface management architecture TBD. Elements: interface register, ICD set, interface baselines, change linkage, verification cross-reference. Ownership and tooling TBD.

## 8. Detailed Design

Register schema, ICD structure and approval chain, interface-change assessment rule and verification provisions TBD. Each ICD shall identify both sides of the interface and their agreed obligations. No interface values are stated at this revision.

## 9. Interfaces

- To architecture: interface identification from system partitioning
- To configuration (00.7): interface baselines
- To change (00.10): interface change records
- To V&V: interface verification planning and evidence
- To suppliers (00.13): supplier-owned interface boundaries

## 10. Operational Concept

Interfaces are identified, registered, placed under control documentation, baselined, changed only by record and verified. Registration and review cadence TBD.

## 11. Safety

Safety-critical interfaces shall be identified with safety authority visibility and verified with appropriate rigour. Safety interface provisions TBD.

## 12. Performance

Interface management performance indicators TBD. No thresholds are baselined at this revision.

## 13. Verification & Validation

This document is verified by inspection against the document template checklist at the applicable gate. Validation is by programme authority approval (approver TBD).

## 14. Risks

- Unregistered interfaces causing integration failure; mitigation TBD
- Late interface control destabilising design; mitigation TBD
- One-sided interface change breaking the counterpart; mitigation TBD

## 15. Open Issues

_TBD_

All open issues are recorded in the issue register. No issue is closed by this revision.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on system partitioning, configuration baselines (00.7), change workflow (00.10), CDR provisions (00.14) and V&V planning.

## 18. Traceability

Parent: HFPX-PGM-CHR-001 (REQ-HFPX-PGM-002/003) and HFPX-PGM-SEM-001 (REQ-HFPX-PGM-012). Children: interface register, ICD set, interface verification records (all TBD). RTM: REQ-HFPX-GIF-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 00.11) |
