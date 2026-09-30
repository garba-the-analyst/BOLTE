# Reliability Allocation

**Document ID:** HFPX-REL-ALC-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X reliability allocation direction for Volume 24 (Chapter 24.2): how system-level reliability intent will be apportioned to lower levels under controlled rules.
Sets allocation-method and update rules only; it contains no failure rates, MTBF values, availability figures, or allocated budgets beyond TBD.

## 2. Scope

Covers allocation from system level to subsystems and items as applicable, with level definitions TBD.
In scope: allocation method, budget records, apportionment update rule, and verification approach. Out of scope: quantitative budgets, which are TBD, and safety apportionment owned by Vol 13.
Governs allocation records feeding Vol 24.3–24.13 analyses.

## 3. Applicable Documents

- Programme Charter STK-001; SyRS SYS-002/003; reliability classification tier TBD; SAF-001..006 tier (stubs)
- HFPX-REL-ENG-001 Reliability Engineering (programme direction), HFPX-SAFE-CAS-001 Safety Case
- Vol 13 safety analyses, Vol 24.3 failure-rate rules, Vol 27 support constraints as applicable
- Standards (structured according to): TBD — no compliance claimed in this revision

## 4. Definitions & Acronyms

- Allocation: apportionment of system-level reliability intent to lower indenture levels; method TBD
- Budget: allocated share recorded per item or subsystem; all budgets TBD
- Apportionment update: controlled revision of budgets when design or data changes; trigger and authority TBD
- Indenture level: system, subsystem, item decomposition level; breakdown TBD
- TBD: to be determined; TBC: to be confirmed

## 5. System Context

Allocation translates system-level intent into design guidance without asserting achievability; achievability is assessed through Vol 24.3–24.13 analyses and test evidence.
This document constrains how budgets are set and revised; it does not claim any budget is met in this revision.
Traceability to reliability classification and SCA tier is required; mapping TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-RAL-001 | The programme shall define a reliability allocation method applicable across indenture levels, with method and applicability TBD. | TBD reliability classification; HFPX-REL-ENG-001 | Inspection |
| REQ-HFPX-RAL-002 | The programme shall record reliability budgets per allocated item, with all budgets TBD and recording location TBD. | TBD reliability classification; REQ-HFPX-RRE-001 | Inspection |
| REQ-HFPX-RAL-003 | The programme shall control apportionment updates under a defined update rule, with triggers, authority, and re-verification TBD. | TBD reliability classification; SEMP gates | Inspection |
| REQ-HFPX-RAL-004 | Allocation and updates shall be verified for completeness, consistency, and traceability, with acceptance criteria TBD. | TBD reliability classification; REQ-HFPX-SCA-004 | Analysis |

## 7. Architecture

Allocation structure TBD: system node, subsystem nodes, item nodes, with ownership per node TBD.
Records architecture TBD: allocation table schema TBD (fields TBD beyond ID, parent, budget TBD, status).
Apportionment authority TBD; independent review TBD.

## 8. Detailed Design

Methodology only, no values:
- Allocation method: candidate approaches TBD; selection criteria TBD; weighting factors TBD.
- Budget records: schema TBD; all budget fields TBD; status values TBD.
- Update rule: triggers TBD (design change, data maturation, gate findings); impact assessment TBD; re-allocation method TBD.
- Consistency rule TBD: budgets trace to system intent under rules TBD; no closure claimed until verified.

## 9. Interfaces

- Allocation ↔ Reliability programme (HFPX-REL-ENG-001 method and gate rules)
- Allocation ↔ Failure-rate analysis (Vol 24.3 inputs; values TBD)
- Allocation ↔ Safety (Vol 13 apportionment exchange as applicable; safety authority owned by HFPX-SAFE-CAS-001)
- Allocation ↔ V&V (allocation records enter VCRM as applicable; verification returns closure status TBD)
- Allocation ↔ Design volumes (Vol 03–18 own implementation of allocated intent; details TBD)

## 10. Operational Concept

Allocation operates as design guidance across the lifecycle: initial apportionment at SRR/PDR as applicable → refinement through CDR → updates on change → gate acceptance TBD.
This concept defines apportionment discipline only, not design implementation or test conduct.
No budget is asserted as achieved in this revision.

## 11. Safety

No safety claim is made in this revision; allocation outputs may inform Vol 13 analyses but take no safety credit until verified through the safety path.
No hazard retirement or safety-target compliance is claimed here.

## 12. Performance

Allocation performance indicators TBD (no thresholds baselined): allocation coverage TBD, budget traceability TBD, update backlog TBD.
No failure rates, MTBF values, availability figures, or life limits are set in this revision.

## 13. Verification & Validation

This document is verified at SRR/PDR against the SEMP checklist (header, 20 sections, IDs, no-values rule, traceability).
Requirement verification follows the V&V Plan: Inspection/Analysis methods; acceptance criteria TBD per case; evidence TBD until closed.
Validation is programme-authority approval at gates; certification validation owned by Vol 25 with no claims here.

## 14. Risks

- Premature allocation treated as commitment without evidence; mitigation: TBD-only budgets enforced at gates
- Inconsistent apportionment across indenture levels; mitigation: consistency checks TBD before CDR as applicable
- Uncontrolled re-allocation on design change; mitigation: update rule with authority TBD

## 15. Open Issues

Allocation method TBD. Indenture breakdown TBD. All budgets TBD. Update triggers and authority TBD. Verification criteria TBD. Reliability classification mapping TBD. Vol 13 exchange details TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on STK-001/SYS-002/003 and TBD reliability classification, HFPX-REL-ENG-001 (programme), SEMP (gates), V&V Plan, SAF tier and HFPX-SAFE-CAS-001, Vol 24.3 (rate inputs), Vol 13 (safety exchange), design volumes (implementation).

## 18. Traceability

Parents: SYS-002/003, TBD reliability classification, HFPX-REL-ENG-001, SAF tier. Children: allocation tables and VCRM cases (artefact IDs TBD).
RTM: REQ-HFPX-RAL-001..004 → CONCEPT. Each budget traces to system intent → analysis → verification (all TBD except schema direction).

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Changes via change records with affected-allocation impact stated.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (allocation method and update rules; budgets TBD) |
