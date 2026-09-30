# Common Cause Analysis

**Document ID:** HFPX-SAFE-CCA-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 3 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X Common Cause Analysis (Vol 13.7): shared-cause scope, zonal/particular-risk considerations, independence-claim evidence rule, and update with physical-architecture maturity.

## 2. Scope

Shared causes across redundant paths: shared fuel, shared power bus, shared software, environmental, maintenance error (checklist TBD); zonal and particular-risk considerations TBD. Boundary note: analysis structure only — no propulsion build, ignition, or operation instructions; no recovery build or operation instructions.

## 3. Applicable Documents

- HFPX-SAFE-CAS-001 Safety Case (REQ-HFPX-SCA-001/002/006)
- HFPX-SAFE-HAZ-001; HFPX-SAFE-FME-001; HFPX-SAFE-FTA-001
- Safety tier SAF-001..006; SAD SFA-003; SEMP; V&V Plan

## 4. Definitions & Acronyms

- CCA: Common Cause Analysis — assessment of shared causes defeating independence (includes TBD zonal / particular-risk aspects).
- Independence claim: assertion that redundant paths fail independently; valid only with CCA evidence.
- Checklist item: candidate shared cause with Hazard → Cause → Effect → Severity(TBD) → Probability(TBD) → Mitigation(TBD) → Verification(TBD).

## 5. System Context

CCA guards redundancy credits from FTA/FMEA: any independence assumed in trees or voted architectures must survive CCA scrutiny before verification credit.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-CCA-001 | The CCA shall address shared fuel, shared power bus, shared software, environmental, and maintenance-error causes with a TBD checklist. | REQ-HFPX-SCA-002, SAF-002, SFA-003 | Analysis |
| REQ-HFPX-CCA-002 | Zonal and particular-risk considerations shall be addressed to a TBD extent tied to physical-architecture maturity. | REQ-HFPX-SCA-006, SAF-002, SFA-003 | Analysis |
|REQ-HFPX-CCA-003|Each independence claim shall require CCA evidence; no independence shall be credited without it.|REQ-HFPX-SCA-002, SAF-006|Inspection|
| REQ-HFPX-CCA-004 | The CCA shall be updated with physical-architecture maturity, with deltas recorded. | REQ-HFPX-SCA-006, SAF-006, SFA-003 | Inspection |

## 7. Architecture

CCA organised by checklist category; each item links to affected FTA branches and FMEA rows; evidence stored with hazard-log trace.

## 8. Detailed Design

Checklist columns: Shared cause, Affected items/paths, Hazard → Cause → Effect, Severity (TBD), Probability (TBD), Mitigation (TBD), Verification (TBD).

Starter common-cause checklist (all TBD):

| Shared cause | Affected items / paths | Hazard → Cause → Effect | Severity | Probability | Mitigation | Verification |
| --- | --- | --- | --- | --- | --- | --- |
| Shared fuel | Qualitative: propulsion modules fed from common path (detail TBD) | Hazard: common-mode thrust loss → Cause: shared-path fault → Effect: multi-module degradation (quantification TBD) | TBD | TBD | TBD | TBD |
| Shared power bus | Qualitative: FCS/avionics on common bus (detail TBD) | Hazard: simultaneous control loss → Cause: bus fault → Effect: loss of redundant channels (quantification TBD) | TBD | TBD | TBD | TBD |
| Shared software | Qualitative: redundant channels run common software (detail TBD) | Hazard: systematic failover failure → Cause: common defect → Effect: loss of voting benefit (quantification TBD) | TBD | TBD | TBD | TBD |
| Environmental | Qualitative: EMI/thermal/ingress exposure (detail TBD) | Hazard: multi-path degradation → Cause: shared environment → Effect: correlated failures (quantification TBD) | TBD | TBD | TBD | TBD |
| Maintenance error | Qualitative: common servicing action (detail TBD) | Hazard: latent multi-path fault → Cause: repeated error → Effect: undetected degraded redundancy (quantification TBD) | TBD | TBD | TBD | TBD |

## 9. Interfaces

- CCA ↔ FTA/FMEA: consumes branches and modes; returns independence findings.
- CCA ↔ SAD: zonal/particular-risk inputs follow physical architecture.
- CCA ↔ Vol 24: independence evidence enters verification.

## 10. Operational Concept

Screen checklist → assess against architecture → challenge independence claims → update with physical maturity. Methodology and gating only.

## 11. Safety

No independence credited; no probabilities asserted. Analysis only.

## 12. Performance

Indicators TBD: checklist coverage, independence-claim closure, update currency. No thresholds baselined.

## 13. Verification & Validation

Verified by review (evidence rule REQ-HFPX-CCA-003). Validation at CDR/FRR gates.

## 14. Risks

- Checklist incompleteness; mitigation: TBD checklist approval.
- Credited independence without evidence; mitigation: evidence rule.
- Architecture drift invalidating CCA; mitigation: update rule.

## 15. Open Issues

Checklist finalisation TBD. Zonal/particular-risk extent TBD. All ratings/mitigations TBD.

## 16. Assumptions

- A-CCA-01: Listed categories bound concept CCA scope; validation: architecture review (TBD).
- A-CCA-02: Physical architecture will mature enough for zonal review before CDR; validation: SAD review (TBD).

## 17. Dependencies

Depends on Safety Case, HAZ/FME/FTA, SAF-001..006, SFA-003, SEMP, Vol 24.

## 18. Traceability

Parents: REQ-HFPX-SCA-001/002/006; SAF-001..006; SFA-003. Children: Vol 13.8–13.18; Vol 24. RTM: REQ-HFPX-CCA-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 3 draft, not baselined. Changes via change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 3 draft (CCA structure, starter checklist) |
