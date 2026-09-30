# Verification Cross-Reference Matrix

**Document ID:** HFPX-VV-VCR-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 8 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the Verification Cross-Reference Matrix (VCRM) discipline for Volume 22.3 as the single traceability authority from requirements to verification cases.
Sets matrix schema, no-orphan rules, coverage gating, and RTM hooks. Contains methodology only.

## 2. Scope

Covers VCRM structure, ownership, maintenance, and gating across all volumes and lifecycle gates.
Applies from SRR through FCA and PCA; detailed matrix rows and tooling are TBD. Test execution detail remains with Vol 23.

## 3. Applicable Documents

- HFPX-VV-PLN-001 VV Plan (REQ-HFPX-VVP-001..006, notably VCRM and no-orphan and gating rules)
- HFPX-PGM-SEM-001 SEMP (requirements management, gated reviews)
- HFPX-SYS-REQ-001 SyRS §13, HFPX-SYS-ARC-001 SAD (stub)
- Vol 19 (analysis), Vol 23 (test execution), Vol 25 (certification credit)

## 4. Definitions & Acronyms

- VCRM: Verification Cross-Reference Matrix; single traceability authority
- Orphaned requirement: requirement with no traced verification case
- Orphaned case: verification case with no traced parent requirement
- RTM: Requirements Traceability Matrix hooks linking needs, requirements, cases, and results
- Coverage gate: review gate conditioned on VCRM completeness; threshold TBD

## 5. System Context

The VCRM sits at the centre of the V-model, binding left-hand requirements to right-hand evidence:

```text
REQUIREMENTS → DESIGN → BUILD → VERIFY (cases A/I/D/T)
      ↑______________ VCRM TRACE (no orphans) ______________↑
      ↑______________ RTM HOOKS (needs → results) __________↑
```

All verification levels (hardware, software, system, safety) and acceptance threads are recorded in the VCRM with method, level, executing volume, and result status.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-VCM-001 | The programme shall maintain the VCRM to a documented schema recording requirement, verification case, method, level, executing volume, and result status, with schema fields defined as TBD. | REQ-HFPX-VVP-002 | Inspection |
| REQ-HFPX-VCM-002 | The VCRM shall contain no orphaned requirements and no orphaned verification cases, with orphan checks performed per a cadence defined as TBD. | REQ-HFPX-VVP-002 | Inspection |
| REQ-HFPX-VCM-003 | Each gated review shall apply a VCRM coverage gate with entrance and exit criteria defined as TBD, and gate progression shall require closure of the gate per criteria TBD. | REQ-HFPX-VVP-004 | Inspection |
| REQ-HFPX-VCM-004 | The VCRM shall provide RTM hooks linking stakeholder needs to requirements to verification cases to results, with hook structure and tooling defined as TBD. | REQ-HFPX-VVP-002 | Inspection |

## 7. Architecture

VCRM ownership and tooling TBD under VV governance; change control TBD.
Matrix structure: Requirement → Verification case ID (TBD) → Method (Analysis, Inspection, Demonstration, or Test) → Level → Executing volume → Result and status.
Safety and acceptance threads are typed distinctly within the same matrix.

## 8. Detailed Design

VCRM rows are created at case planning (SRR and PDR) and matured through CDR and TRR; acceptance criteria per row recorded as TBD where not yet defined.
Any baselined requirement change re-opens affected VCRM rows until re-verified; regression scope defined per change record with details TBD.
Matrix audit provisions and access control TBD.

## 9. Interfaces

- VCRM ↔ SE (SEMP gates; coverage evidence at each review)
- VCRM ↔ Design volumes (Vol 03–18 provide allocation and design evidence)
- VCRM ↔ Safety (Vol 13 hazard-derived requirements flow in; closure evidence flows back)
- VCRM ↔ Certification (Vol 25 defines certification credit mapping; no credit claimed here)

## 10. Operational Concept

VCRM operates plan-to-close: draft rows early → assign methods and levels → develop cases and criteria → execute via Vol 19 and Vol 23 → record results → gate on coverage.
Review cadence, board membership, and reporting format TBD.

## 11. Safety

Hazard-derived safety requirements are flagged in the VCRM with independent verification paths per VV Plan independence rules TBD.
Catastrophic hazard closure evidence is independently verified before human flight gates are considered (criterion TBD, owned by Safety Case).

## 12. Performance

VCRM performance indicators TBD, with all thresholds TBD: matrix coverage, orphan count, criteria definition backlog, closure burn-down per gate.
Measurement method and reporting cadence TBD in Vol 22 children.

## 13. Verification & Validation

This document is verified by Inspection against the VV Plan and SEMP checklist (header, 20 sections, IDs, parents, allowed methods only).
Validation of the VCRM approach is programme authority approval at gated reviews; certification validation owned by Vol 25.

## 14. Risks

- VCRM drift across volumes producing orphans or untraced tests; mitigation: no-orphan rule with audit cadence TBD and coverage gates
- Criteria left TBD indefinitely blocking closure; mitigation: per-row TBD tracking with owning volume and due gate (assignments TBD)
- Tooling shortfall for matrix scale; mitigation: tooling selection TBD under VV governance

## 15. Open Issues

Matrix schema fields TBD. Tooling TBD. Coverage gate thresholds TBD. RTM hook implementation TBD. Audit provisions TBD.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on VV Plan methodology, SEMP gates, SyRS and SAD allocation, Safety Case and Vol 13 safety inputs, Vol 19 analysis cases, Vol 23 execution cases, Vol 25 credit rules.

## 18. Traceability

Parents: REQ-HFPX-VVP-002, REQ-HFPX-VVP-004. Children: Vol 22 verification case volumes and Vol 23 execution volumes (case IDs TBD; VCRM rows TBD).
RTM: REQ-HFPX-VCM-001..004 → CONCEPT. No orphaned requirements; no orphaned verification cases.

## 19. Configuration

BL-0.0. Tranche 8 draft, CONCEPT, not baselined. Future changes via change records; affected VCRM rows re-validated before gate claims.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 8 draft (Vol 22.3 direction; structure only) |
