# Requirements Verification

**Document ID:** HFPX-VV-RQV-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 8 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define requirements verification discipline for Volume 22.4, governing assignment of verification methods and traceability of every requirement to verification cases.
Sets method assignment, TBD prohibition, trace, and records rules. Methodology only.

## 2. Scope

Covers verification method allocation for requirements across all volumes from SRR through FCA and PCA.
Detailed cases remain with Vol 22.5–22.13 and Vol 23; VCRM structure owned by Vol 22.3.

## 3. Applicable Documents

- HFPX-VV-PLN-001 VV Plan (REQ-HFPX-VVP-001..006 — method assignment, VCRM, acceptance, gating)
- HFPX-PGM-SEM-001 SEMP (requirements management, verification method, gated reviews)
- HFPX-SYS-REQ-001 SyRS §13, HFPX-SYS-ARC-001 SAD (stub)
- Vol 19 (analysis), Vol 23 (test execution), Vol 22.3 (VCRM)

## 4. Definitions & Acronyms

- Verification methods: Analysis (calculation, modelling, simulation review); Inspection (visual and document examination); Demonstration (witnessed functional observation without quantitative pass and fail instrumentation); Test (measured execution against TBD acceptance criteria)
- Primary method: the single governing method assigned per requirement
- TBD method: unassigned or deferred method allocation, prohibited as a closure basis

## 5. System Context

Requirements verification binds the requirements baseline to evidence through the VCRM:

```text
REQUIREMENT → METHOD (A/I/D/T) → CASE → EVIDENCE → GATE CLOSE
      ↑______________ VCRM TRACE (Vol 22.3) ______________↑
```

Every requirement carries exactly one primary method; supporting methods may be recorded additionally with details TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-RQV-001 | The programme shall assign every requirement exactly one primary verification method from Analysis, Inspection, Demonstration, or Test, with the assignment recorded in the VCRM. | REQ-HFPX-VVP-001 | Inspection |
| REQ-HFPX-RQV-002 | The programme shall prohibit TBD as a verification method for gate closure, and any requirement with method recorded as TBD shall be tracked as an open TBD item with owning volume and due gate defined as TBD. | REQ-HFPX-VVP-001 | Inspection |
| REQ-HFPX-RQV-003 | Every requirement shall be traced to its verification case or cases in the VCRM, with trace structure and case identifiers defined as TBD. | REQ-HFPX-VVP-002 | Inspection |
| REQ-HFPX-RQV-004 | Every verification case shall define acceptance criteria before execution, with criteria recorded as TBD per case where not yet defined and closure provisions defined as TBD. | REQ-HFPX-VVP-005 | Inspection |

## 7. Architecture

Method assignment authority and workflow TBD under VV governance with SE coordination.
VCRM is the allocation record: method, level, executing volume, and status per requirement; supporting evidence linkages TBD.
Safety requirements receive method assignment with independence provisions per VV Plan rules TBD.

## 8. Detailed Design

Method assignment occurs at requirement authoring and is confirmed at SRR and PDR; late changes follow change control with re-verification scope TBD.
Case templates contain objective, traced parent requirement or requirements, method, level, environment and configuration, acceptance criteria (TBD per case), and independence claim where applicable.
Regression on baselined requirement change re-opens affected rows until re-verified; scope per change record TBD.

## 9. Interfaces

- Requirements verification ↔ SE (SEMP method and gate rules)
- Requirements verification ↔ VCRM (Vol 22.3 row discipline)
- Requirements verification ↔ Levels (Vol 22.9–22.12 allocation)
- Requirements verification ↔ Safety and Certification (Vol 13, Safety Case, Vol 25 credit mapping)

## 10. Operational Concept

Operate assign-to-close: assign method at authoring → trace cases early → develop criteria and procedures → execute via Vol 19 and Vol 23 → record evidence → close at gates.
Cadence and board provisions TBD.

## 11. Safety

Safety requirements receive Test or Analysis verification with independent review or test per VV Plan independence rules TBD.
Hazard closure traceability is maintained through the VCRM with criteria TBD and Safety Case ownership.

## 12. Performance

Indicators TBD, with all thresholds TBD: method assignment completeness, TBD method backlog, trace coverage, criteria definition backlog, closure burn-down.
Measurement method and reporting cadence TBD.

## 13. Verification & Validation

This document is verified by Inspection against the VV Plan and SEMP checklist (header, 20 sections, IDs, parents, allowed methods only).
Validation of this approach is programme authority approval at gated reviews; certification validation owned by Vol 25.

## 14. Risks

- Methods left TBD blocking gate closure; mitigation: prohibition rule with per-item TBD tracking (assignments TBD)
- Method mismatch to requirement type (observation where measurement needed and similar); mitigation: method adequacy check at PDR and CDR (checklist TBD)
- Trace drift across volumes; mitigation: VCRM coverage gates (threshold TBD)

## 15. Open Issues

Method assignment workflow TBD. TBD tracking ownership TBD. Trace tooling TBD. Criteria templates TBD. Regression scope rules TBD.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on VV Plan methodology, SEMP gates, SyRS §13, SAD allocation, Vol 22.3 VCRM, Vol 19 analysis capability, Vol 23 execution capability, Safety Case and Vol 25 rules.

## 18. Traceability

Parents: REQ-HFPX-VVP-001, REQ-HFPX-VVP-002, REQ-HFPX-VVP-005. Children: Vol 22.5–22.13 method volumes and Vol 23 execution volumes (case IDs TBD).
RTM: REQ-HFPX-RQV-001..004 → CONCEPT. Coverage tracked in Vol 22.3 VCRM.

## 19. Configuration

BL-0.0. Tranche 8 draft, CONCEPT, not baselined. Future changes via change records; affected VCRM rows re-validated before gate claims.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 8 draft (Vol 22.4 direction; structure only) |
