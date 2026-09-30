# Requirements Management

**Document ID:** HFPX-PGM-RQM-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define requirements management for HFP-X: requirement quality, traceability coverage, requirement change control and tooling. Owns Chapter 00.9.

## 2. Scope

Covers stakeholder, system, subsystem and verification requirements across all volumes, including RTM discipline and requirement change rules. Does not set technical values.

## 3. Applicable Documents

- HFPX-PGM-CHR-001 Programme Charter
- HFPX-PGM-SEM-001 SEMP
- HFPX-PGM-CFG-001 Configuration Management (requirement baselines)
- HFPX-PGM-CHG-001 Change Management (requirement change workflow)
- Standards structured according to: ISO/IEC/IEEE 29148

## 4. Definitions & Acronyms

- RTM: Requirements Traceability Matrix from needs through evidence
- Requirement attribute: structured property supporting quality, ownership and verification
- TBD / TBC: to be determined / to be confirmed

## 5. System Context

Requirements flow from needs to evidence under traceability:

```text
STAKEHOLDER NEEDS → SYSTEM REQUIREMENTS → ARCHITECTURE → DESIGN
    → TEST → EVIDENCE
    ↑________________ RTM (no orphaned major requirements) __↑
```

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-GRQ-001 | The programme shall author requirements with defined attributes structured according to ISO/IEC/IEEE 29148, with attribute set and quality rules recorded as TBD at this revision. | REQ-HFPX-PGM-010 | Inspection |
| REQ-HFPX-GRQ-002 | The programme shall maintain RTM coverage such that progression past each gate requires full traceability of major requirements through design to verification provisions. | REQ-HFPX-PGM-002 | Inspection |
| REQ-HFPX-GRQ-003 | The programme shall control requirement changes so that no baselined requirement is changed without an approved change record identifying affected requirements, subsystems, interfaces and evidence. | REQ-HFPX-PGM-012 | Demonstration |
| REQ-HFPX-GRQ-004 | The programme shall define requirements-management tooling, with tool selection and usage provisions recorded as TBD at this revision. | REQ-HFPX-PGM-002 | Inspection |

## 7. Architecture

Requirements architecture TBD. Elements: needs set, system requirements, allocated subsystem requirements, RTM, verification cross-reference. Custodianship and tooling TBD.

## 8. Detailed Design

Attribute definitions, RTM structure and coverage rule, requirement-change linkage and tooling procedure TBD. Each requirement shall state its verification method. RTM coverage of major requirements is a gate condition. No tooling selection is made at this revision.

## 9. Interfaces

- To SEMP and Charter: quality and traceability policy
- To configuration (00.7): requirement baselines
- To change (00.10): requirement change records
- To architecture and V&V: allocation and verification linkage
- To RTM register: living traceability record

## 10. Operational Concept

Requirements are elicited, authored to quality rules, traced, baselined at gates and changed only by record. RTM is reviewed at each gate. Review cadence and tooling workflow TBD.

## 11. Safety

Safety requirements shall be identified, traced and verified with safety authority visibility. Safety traceability provisions TBD.

## 12. Performance

Requirements performance indicators TBD. No thresholds are baselined at this revision, other than the RTM coverage gate rule stated in Section 6.

## 13. Verification & Validation

This document is verified by inspection against the document template checklist at the applicable gate. Validation is by programme authority approval (approver TBD).

## 14. Risks

- Poor requirement quality causing unverifiable design; mitigation TBD
- RTM gaps leaving orphaned major requirements; mitigation TBD
- Informal requirement change bypassing impact assessment; mitigation TBD

## 15. Open Issues

_TBD_

All open issues are recorded in the issue register. No issue is closed by this revision.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on Charter traceability policy, SEMP requirement rules, configuration baselines (00.7), change workflow (00.10) and V&V verification methods.

## 18. Traceability

Parent: HFPX-PGM-CHR-001 (REQ-HFPX-PGM-002), HFPX-PGM-SEM-001 (REQ-HFPX-PGM-010/012). Children: requirement sets, RTM, tooling procedure (all TBD). RTM: REQ-HFPX-GRQ-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 00.9) |
