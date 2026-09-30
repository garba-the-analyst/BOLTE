# Availability

**Document ID:** HFPX-REL-AVL-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X availability direction for Volume 24 (Chapter 24.6): how the availability model, inputs, targets, and verification approach will be controlled.
Sets modelling and recording rules only; it contains no availability figures, MTBF/MTTR values, or failure rates beyond TBD.

## 2. Scope

Covers system-level availability modelling across defined operating scopes, with scope and mission definitions TBD.
In scope: model definition, input rules, target records, verification approach. Out of scope: quantitative availability claims, which are TBD, and support-execution owned by Vol 27.
Inputs draw on Vol 24.3/24.8/24.9 under TBD rules.

## 3. Applicable Documents

- Programme Charter STK-001; SyRS SYS-002/003; reliability classification tier TBD; SAF tier (stubs)
- HFPX-REL-ENG-001 Reliability Engineering, HFPX-REL-FRA-001 Failure Rate Analysis, HFPX-REL-MTB-001 MTBF, HFPX-REL-MTR-001 MTTR direction documents
- HFPX-SAFE-CAS-001 Safety Case; HFPX-VV-PLN-001 V&V Plan; Vol 27 support hooks
- Standards (structured according to): TBD — no compliance claimed in this revision

## 4. Definitions & Acronyms

- Availability: ability to be in a state to perform as required when called upon under stated conditions; all figures TBD
- Availability model: analytical structure combining reliability, maintainability, and support inputs; model TBD
- Model input: reliability, maintainability, or support parameter feeding the model; all inputs TBD
- Target: availability objective recorded for assessment; all targets TBD
- TBD: to be determined; TBC: to be confirmed

## 5. System Context

Availability constrains support and design trades by showing how reliability and maintainability inputs combine under stated conditions.
This document governs modelling discipline; no availability outcome is claimed in this revision.
Operating conditions, duty, and support concepts feeding the model are TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-RAV-001 | The programme shall define an availability model with stated scope and conditions, with model and scope TBD. | TBD reliability classification; HFPX-REL-ENG-001 | Inspection |
| REQ-HFPX-RAV-002 | The programme shall govern availability-model inputs under defined input rules, with all inputs TBD per Vol 24.3/24.8/24.9. | TBD reliability classification; Vol 24.3/24.8/24.9 | Analysis |
| REQ-HFPX-RAV-003 | The programme shall record availability targets with defined scope, with all targets TBD and recording location TBD. | TBD reliability classification; SYS-002/003 | Inspection |
| REQ-HFPX-RAV-004 | Availability assessment shall be verified under a defined verification approach, with method and acceptance criteria TBD. | TBD reliability classification; REQ-HFPX-SCA-004 | Analysis |

## 7. Architecture

Model organisation TBD: availability owner, input owners in Vol 24.3/24.8/24.9, independent reviewer TBD.
Model architecture TBD: block structure, state definitions TBD, support-input interfaces TBD.
Record architecture TBD: target table schema TBD with all target fields TBD.

## 8. Detailed Design

Methodology only, no values:
- Model: modelling formalism TBD; scope and condition statements TBD; exclusion rules TBD.
- Inputs: reliability inputs TBD; maintainability inputs TBD; logistics/support inputs TBD with Vol 27 hooks TBD.
- Targets: recording schema TBD; traceability to classification tier TBD; no target baselined.
- Sensitivity and uncertainty treatment TBD; update rule on input change TBD.

## 9. Interfaces

- Availability ↔ Failure-rate/MTBF/MTTR (Vol 24.3/24.8/24.9 inputs; values TBD)
- Availability ↔ Allocation (Vol 24.2 intent assessed against model outputs as applicable)
- Availability ↔ Support (Vol 27 logistics inputs; details TBD)
- Availability ↔ Safety (no safety credit; safety path owned by HFPX-SAFE-CAS-001)
- Availability ↔ V&V (model and targets enter VCRM as applicable; verification returns closure TBD)

## 10. Operational Concept

Availability matures across the lifecycle: model defined at SRR/PDR as applicable → inputs matured through test → assessment at gates TBD.
This concept defines modelling-maturation discipline only, not operations or support execution.
No availability outcome is asserted in this revision.

## 11. Safety

No safety claim is made in this revision; availability outputs take no safety credit until verified through the safety path.
No operational-readiness or dispatch claim is made here.

## 12. Performance

Availability performance indicators TBD (no thresholds baselined): model coverage TBD, input traceability TBD, target traceability TBD.
No availability figures, failure rates, MTBF/MTTR values, or life limits are set in this revision.

## 13. Verification & Validation

This document is verified at SRR/PDR against the SEMP checklist (header, 20 sections, IDs, no-values rule, model direction).
Requirement verification follows the V&V Plan: Inspection/Analysis methods; acceptance criteria TBD per case; evidence TBD until closed.
Validation is programme-authority approval at gates; certification validation owned by Vol 25 with no claims here.

## 14. Risks

- Immature inputs treated as firm model outputs; mitigation: TBD-only inputs enforced at gates
- Model-scope ambiguity across operating conditions; mitigation: scope statements TBD before assessment
- Support-input optimism without Vol 27 evidence; mitigation: Vol 27 hook qualification TBD

## 15. Open Issues

Model formalism TBD. All inputs TBD. All targets TBD. Scope and condition definitions TBD. Verification method TBD. Vol 27 hook details TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on STK-001/SYS-002/003 and TBD reliability classification, HFPX-REL-ENG-001, Vol 24.3/24.8/24.9 inputs, SEMP, V&V Plan, SAF tier and HFPX-SAFE-CAS-001, Vol 27 support inputs.

## 18. Traceability

Parents: SYS-002/003, TBD reliability classification, HFPX-REL-ENG-001, SAF tier. Children: availability model and target records (artefact IDs TBD).
RTM: REQ-HFPX-RAV-001..004 → CONCEPT. Each target traces to model → inputs TBD → VCRM cases (all TBD except direction).

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Changes via change records with affected-model impact stated.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (availability model direction; inputs and targets TBD) |
