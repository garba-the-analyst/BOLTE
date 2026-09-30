# 19.15 Model Verification

**Document ID:** HFPX-SIM-VER-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define verification-versus-validation definitions for models, the verification-case inventory across models, the acceptance-tolerance policy, the verified-model register rule, and the prohibition on gate decisions from unregistered models.
Enforces evidence discipline for model-supported claims, consistent with ISS-006 and ISS-007 handling (details TBD).
This document owns Chapter 19.15 direction under Volume 19.

## 2. Scope

Covers verification of models under Chapters 19.2–19.8 and Chapters 19.12–19.14, acceptance tolerances, register control, and gate-use prohibition for unregistered models.
Applies wherever a model supports a gate decision; detailed verification cases are owned by child documents (IDs TBD).
Excludes model development (owned by source model chapters), test execution (owned by Vol 23), and certification credit decisions (owned by Vol 25).

## 3. Applicable Documents

- HFPX-VV-PLN-001 VV Plan, notably REQ-HFPX-VVP-001 (verification method), REQ-HFPX-VVP-004 (gated progression), and REQ-HFPX-VVP-005 (acceptance criteria before execution)
- Volume 19 model chapters 19.2–19.8 (IDs TBD) and analysis chapters 19.12–19.14 (IDs TBD) for models under verification
- MST tier (IDs TBD)
- Vol 22 VCRM (ID TBD) and Vol 23 execution volumes (IDs TBD) for case traceability and evidence capture
- ISS-006 and ISS-007 records (IDs TBD) for evidence-discipline context

## 4. Definitions & Acronyms

- Verification (for models): confirmation that a model implementation correctly represents its stated specification and behaves within stated tolerances; method TBD per case
- Validation (for models): confirmation that a model is adequate for its intended use when compared to higher authority such as test data; method TBD per case
- Verification case: a defined check of a model with objective, configuration, and acceptance criteria; IDs TBD
- Acceptance tolerance: the permitted difference between model output and authority; policy TBD
- Verified-model register: the controlled list of model revisions cleared to support gate decisions; mechanism TBD

## 5. System Context

Model verification sits as the evidence gate between models and all model-supported claims:

```text
MODELS (19.2-19.8, 19.12-19.14) → VERIFICATION CASES → REGISTER → GATE DECISIONS
                                           ↓
                              UNREGISTERED MODELS EXCLUDED FROM GATES
```

Only registered model revisions support gate decisions. Verification does not validate fitness for uses outside stated bounds and does not authorise flight.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-MMV-001 | The programme shall define verification-versus-validation for models, stating what each confirms and what evidence each requires; definitions and evidence rules TBD per application. | REQ-HFPX-VVP-001 | Inspection |
| REQ-HFPX-MMV-002 | The programme shall maintain a verification-case inventory covering each model under Chapters 19.2–19.8 and Chapters 19.12–19.14; cases, coverage, and authority TBD per model. | REQ-HFPX-VVP-001 | Inspection |
| REQ-HFPX-MMV-003 | The programme shall define the acceptance-tolerance policy for model verification; tolerance-setting method, authority, and per-case values TBD. | REQ-HFPX-VVP-001 | Analysis |
| REQ-HFPX-MMV-004 | The programme shall maintain a verified-model register and permit only registered model revisions to support gate decisions; register mechanism and entry criteria TBD. | REQ-HFPX-VVP-004 | Demonstration |
| REQ-HFPX-MMV-005 | The programme shall prohibit any gate decision relying on an unregistered model revision; non-compliance handling TBD, consistent with ISS-006 and ISS-007 evidence discipline. | REQ-HFPX-VVP-004 | Demonstration |

## 7. Architecture

Model-verification organisation (roles TBD): verification lead, model owners per Chapters 19.2–19.8 and 19.12–19.14, register custodian, independent reviewer TBD.
Model-verification structure TBD: per-model case suites (IDs TBD), authority data sets TBD, tolerance records TBD, register with revision trace TBD.
Register entries record model identity, revision, verified bounds, authority, and entry approval; fields TBD.

## 8. Detailed Design

Definitions elaboration TBD per REQ-HFPX-MMV-001: verification evidence content TBD, validation evidence content TBD, per-application tailoring TBD.
Inventory elaboration TBD per REQ-HFPX-MMV-002: per-model case lists TBD, authority per case TBD, coverage rule TBD, gap-handling TBD.
Tolerance elaboration TBD per REQ-HFPX-MMV-003: policy for setting tolerances TBD, authority hierarchy TBD, per-case values TBD.
Register elaboration TBD per REQ-HFPX-MMV-004: entry criteria TBD, custodian workflow TBD, revision and bounds recording TBD, removal and re-verification rules TBD.
Prohibition elaboration TBD per REQ-HFPX-MMV-005: gate-check method TBD, violation handling TBD, ISS-006 and ISS-007 linkage TBD.
No values are baselined in this revision.

## 9. Interfaces

- Model verification ↔ Models (Chapters 19.2–19.8, 19.12–19.14): model revisions enter verification; verified bounds return to consumers
- Model verification ↔ Register: entry, update, and removal workflow; mechanism TBD
- Model verification ↔ Gates (VV Plan REQ-HFPX-VVP-004): gate authorities check register before accepting model-supported evidence
- Model verification ↔ VCRM (Vol 22.3) and Safety (Vol 13/24): cases traced with no orphans; safety-relevant cases independently reviewed to a degree TBD

## 10. Operational Concept

Model verification operates case-to-register-to-gate: define cases and tolerances before execution → execute against recorded authority → record verdicts → enter qualifying revisions in the register → check register at each gate.
No gate decision proceeds on an unregistered model revision per REQ-HFPX-MMV-005.
Cadence, staffing, and tooling TBD in child documents.

## 11. Safety

Safety-relevant model verification cases receive independent review to a degree TBD, with review records feeding hazard-closure evidence paths owned by the Safety Case.
Unregistered models shall not support safety claims relied upon for flight decisions.
Any advisory-function influence on verified threads shall identify the deterministic bounded function actually verified; method TBD.

## 12. Performance

Model-verification performance indicators TBD; no thresholds baselined: case coverage TBD, tolerance closure TBD, register currency TBD, gate-check compliance TBD.
Measurement method and reporting cadence TBD in child documents.

## 13. Verification & Validation

This document is verified at gated reviews against the document template checklist (header, structure, IDs, method on every requirement, TBD discipline, register and prohibition coherence).
Model verification cases (IDs TBD) shall each define objective, traced parent requirement and model revision, authority, method, configuration, and acceptance criteria TBD per case before execution, consistent with REQ-HFPX-VVP-005.
Validation of the model-verification approach is programme-authority approval at gated reviews; certification validation is owned by Vol 25 with no claims here.

## 14. Risks

- Verification cases incomplete across the model set, leaving model-supported claims unanchored; mitigation: REQ-HFPX-MMV-002 inventory with per-model TBD tracking (owners TBD)
- Tolerances left TBD, blocking verdict defensibility; mitigation: REQ-HFPX-MMV-003 policy with per-case TBD tracking (assignments TBD)
- Gate reliance on unregistered models under schedule pressure; mitigation: REQ-HFPX-MMV-005 prohibition with formal register check at each gate

## 15. Open Issues

Verification-versus-validation tailoring TBD per application. Per-model case inventory and authority TBD. Tolerance policy and per-case values TBD. Register mechanism and entry criteria TBD. Gate-check method and violation handling TBD. ISS-006 and ISS-007 linkage detail TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on VV Plan methodology and gate discipline, models from Chapters 19.2–19.8 and analyses from Chapters 19.12–19.14, MST tier direction (IDs TBD), Vol 22 VCRM discipline, Vol 23 evidence capture, Vol 25 credit rules, and ISS-006/007 records.

## 18. Traceability

Parents: REQ-HFPX-VVP-001 (verification method); REQ-HFPX-VVP-004 (gated progression, no skipping); REQ-HFPX-VVP-005 (acceptance criteria before execution); MST tier (IDs TBD); model chapters 19.2–19.8 (IDs TBD).
Children: model verification cases, tolerance records, and register entries (IDs TBD; rows TBD in VCRM).
RTM: REQ-HFPX-MMV-001..005 → CONCEPT. No orphaned requirements; no orphaned verification cases per REQ-HFPX-VVP-002 principle.

## 19. Configuration

BL-0.0. Tranche 5 draft, CONCEPT, not baselined. Future changes via change records; any change re-validates affected traceability and register entries before gate claims.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 draft (Chapter 19.15 model verification definitions, case inventory, tolerances, register, gate prohibition; structure only) |
