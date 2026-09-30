# Configuration Baselines

**Document ID:** HFPX-SUS-CBL-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define how HFP-X sustainment configuration baselines are established, evolved and controlled through life. Owns Chapter 32.2.

## 2. Scope

Covers sustainment baseline identification, baseline evolution and change governance linkage. Does not set technical values or baseline content. Programme configuration processes are owned elsewhere (hooks to 00.7/28.9).

## 3. Applicable Documents

- HFPX-PGM-SEM-001 SEMP (configuration control concepts)
- Programme configuration management (00.7 hooks, details TBD)
- Vol 28 configuration and records concepts (28.9 hooks, details TBD)
- Vol 24 safety assurance concepts (details TBD)

## 4. Definitions & Acronyms

- Configuration baseline: an agreed reference definition of the product and its documentation at a lifecycle point
- Baseline evolution: controlled progression of baselines across lifecycle phases
- TBD/TBC: unknown data markers; unknown values are never invented

## 5. System Context

Sustainment baselines anchor the fielded configuration:

```text
DESIGN BASELINE → PRODUCTION BASELINE → SUSTAINED BASELINE → RETIREMENT BASELINE
        ↑______________ CHANGE GOVERNANCE (00.7 hooks) ______________↑
        ↑______________ RECORDS (28.9 hooks) ________________________↑
```

Baseline evolution is TBD and remains under formal control once established.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-UCB-001 | The sustainment configuration baselines shall be identified and placed under configuration control. | Lifecycle phase definition (TBD) | Inspection |
| REQ-HFPX-UCB-002 | Baseline evolution across lifecycle phases shall follow a defined and controlled progression. | Programme configuration management, 00.7 hooks (TBD) | Inspection |
| REQ-HFPX-UCB-003 | Changes affecting sustainment baselines shall be recorded with traceability to affected items and evidence. | Vol 28 configuration and records concepts, 28.9 hooks (TBD) | Demonstration |
| REQ-HFPX-UCB-004 | Sustainment baseline changes with safety relevance shall retain alignment with safety assurance. | Vol 24 hooks (TBD) | Inspection |

## 7. Architecture

Baseline control structure (roles TBD): configuration authority, design authority and safety concurrence with responsibilities TBD. Board structure aligns with programme configuration governance (00.7 hooks).

## 8. Detailed Design

Baseline types, content, identification scheme and evolution steps to be defined (TBD). Baseline evolution approach is TBD and not baselined at this revision.

## 9. Interfaces

- Baselines ↔ programme configuration management (00.7) for control process alignment
- Baselines ↔ Vol 28 records (28.9) for baseline capture and retention
- Baselines ↔ safety (Vol 24) for safety-relevant change concurrence

## 10. Operational Concept

Baselines operate as the sustainment reference: identify → baseline → control evolution → audit. Identification events and audit forums TBD.

## 11. Safety

Safety-relevant baseline changes require safety assessment with mechanisms TBD (Vol 24 hooks). No safety thresholds are set in this document.

## 12. Performance

Baseline control indicators TBD (change trace completeness criteria TBD, audit finding closure criteria TBD). No thresholds baselined.

## 13. Verification & Validation

This document is verified by inspection against the document template checklist (header, 20 sections, IDs, traceability). Requirements REQ-HFPX-UCB-001..004 verified per §6. Validation: programme authority approval (TBD).

## 14. Risks

- Uncontrolled baseline evolution → configuration divergence; mitigation: formal baseline control (TBD)
- Incomplete change traceability → unknown fielded state; mitigation: records linkage via 28.9 hooks (TBD)
- Process misalignment with 00.7 → conflicting governance; mitigation: harmonisation with programme configuration (TBD)

## 15. Open Issues

Baseline types, evolution approach, control workflow and 00.7/28.9 interface details to be defined. All open details recorded as TBD.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on programme configuration management (00.7), Vol 28 records concepts (28.9), SEMP configuration principles and Vol 24 safety assurance.

## 18. Traceability

Parent: lifecycle phase definition, programme configuration (00.7 hooks), Vol 28 (28.9 hooks), Vol 24 hooks. Children: fleet, update, upgrade and obsolescence baselines (Chapters 32.3, 32.7, 32.8, 32.9). RTM: REQ-HFPX-UCB-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 32.2) |
