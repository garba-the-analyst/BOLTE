# Predictive Maintenance

**Document ID:** HFPX-REL-PDM-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X predictive-maintenance direction for Volume 24 (Chapter 24.12): how prediction functions, AI hooks, action authority, and verification will be controlled.
Sets advisory-only prediction governance only; it contains no thresholds, horizons, or accuracy figures beyond TBD, and grants no autonomous maintenance authority.

## 2. Scope

Covers predictive-maintenance function definitions consuming condition-monitoring indicators as applicable, with functions TBD.
In scope: prediction-function definitions, AI hooks to Vol 18.4, human action-authority rule, verification approach. Out of scope: prediction implementation owned by Vol 18 as applicable, sensing owned by Vol 08/16, and maintenance execution owned by Vol 27.
All prediction outputs are advisory in this revision.

## 3. Applicable Documents

- Programme Charter STK-001; SyRS SYS-002/003; reliability classification tier TBD; SAF tier (stubs)
- HFPX-REL-ENG-001 Reliability Engineering, HFPX-REL-CDM-001 Condition Monitoring, HFPX-SAFE-CAS-001 Safety Case
- Vol 18.4 AI hooks, Vol 08.10/16.11 indicator hooks, Vol 27 support hooks, HFPX-VV-PLN-001 V&V Plan
- Standards (structured according to): TBD — no compliance claimed in this revision

## 4. Definitions & Acronyms

- Predictive maintenance: use of condition and history insight to advise future maintenance need; functions TBD
- Prediction function: defined analytic function producing an advisory; list TBD
- AI hook: interface to AI-enabled analysis owned under Vol 18.4 governance; details TBD
- Action authority: human authority for maintenance action on advisories; authority human TBD
- TBD: to be determined; TBC: to be confirmed

## 5. System Context

Predictive maintenance constrains how advisories are defined and governed before any maintenance reliance; reliance requires verified functions plus human-authority acceptance.
This document governs advisory discipline; no prediction is claimed as valid in this revision.
AI elements remain advisory-only and bounded under Vol 18.4 governance TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-RPM-001 | The programme shall define predictive-maintenance prediction functions as advisory-only, with functions and scope TBD. | TBD reliability classification; HFPX-REL-ENG-001 | Inspection |
| REQ-HFPX-RPM-002 | Prediction functions shall maintain defined AI hooks governed by Vol 18.4, with interface, bounds, and governance TBD. | TBD reliability classification; Vol 18.4 | Inspection |
| REQ-HFPX-RPM-003 | Maintenance action on predictive advisories shall remain under human authority, with authority and procedure TBD. | TBD reliability classification; SAF tier; REQ-HFPX-SCA-003 | Demonstration |
| REQ-HFPX-RPM-004 | Prediction functions and authority rules shall be verified under a defined verification approach, with method and criteria TBD. | TBD reliability classification; REQ-HFPX-SCA-004 | Analysis |

## 7. Architecture

Prediction organisation TBD: predictive-maintenance owner, Vol 18.4 AI owner, Vol 24.11 indicator owner, Vol 27 consumer, independent reviewer TBD.
Function architecture TBD: advisory path from indicators to functions to human decision; no autonomous path in this revision.
Record architecture TBD: function table schema TBD with all functions TBD.

## 8. Detailed Design

Methodology only, no values:
- Functions: candidate functions TBD; input-indicator mapping TBD (Vol 24.11 hooks); output-advisory format TBD; horizon and confidence treatment TBD (no figures baselined).
- AI hooks: applicable AI methods TBD; bounds TBD; training-data governance TBD; Vol 18.4 compliance TBD.
- Authority: human decision procedure TBD; override rules TBD; advisory-routing TBD; autonomous-action prohibition in this revision.
- Recording: function and authority records TBD; status values TBD; change control TBD.

## 9. Interfaces

- Prediction ↔ Condition monitoring (Vol 24.11 indicators; indicators TBD)
- Prediction ↔ AI (Vol 18.4 method and governance hooks; details TBD)
- Prediction ↔ Support (Vol 27 maintenance-planning inputs; advisory-only; details TBD)
- Prediction ↔ Safety (advisory-only; safety path owned by HFPX-SAFE-CAS-001; no safety credit here)
- Prediction ↔ V&V (function and authority cases enter VCRM; verification returns closure TBD)

## 10. Operational Concept

Prediction matures across the lifecycle: function definitions at SRR/PDR as applicable → hooks through CDR → advisory governance through test → gate acceptance TBD.
This concept defines advisory-governance discipline only, not maintenance execution, flight conduct, or AI training.
No predictive advisory is authorised beyond human-decided action in this revision.

## 11. Safety

No safety claim is made in this revision; prediction outputs are advisory-only and take no safety credit until verified through the safety path.
Prediction shall not command safety-critical action in this revision; AI remains advisory-only per safety-case direction.

## 12. Performance

Prediction performance indicators TBD (no thresholds baselined): function coverage TBD, hook completeness TBD, authority-procedure completeness TBD.
No accuracy figures, horizons, thresholds, failure rates, MTBF/MTTR values, availability figures, or life limits are set in this revision.

## 13. Verification & Validation

This document is verified at SRR/PDR against the SEMP checklist (header, 20 sections, IDs, advisory-only and human-authority rules, no-values rule).
Requirement verification follows the V&V Plan: Inspection/Analysis/Demonstration methods; acceptance criteria TBD per case; evidence TBD until closed.
Validation is programme-authority approval at gates; certification validation owned by Vol 25 with no claims here.

## 14. Risks

- Advisory treated as directive without human decision; mitigation: human-authority rule enforced at gates
- Unbounded AI behaviour in prediction path; mitigation: Vol 18.4 bounds and governance TBD before reliance
- Indicator immaturity propagated into predictions; mitigation: Vol 24.11 qualification required, details TBD

## 15. Open Issues

Prediction functions TBD. AI hooks and bounds TBD. Human authority procedure TBD. Verification method TBD. Indicator mapping TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on STK-001/SYS-002/003 and TBD reliability classification, HFPX-REL-ENG-001, HFPX-REL-CDM-001 (Vol 24.11), SEMP, V&V Plan, SAF tier and HFPX-SAFE-CAS-001, Vol 18.4 AI governance, Vol 08.10/16.11, Vol 27 support.

## 18. Traceability

Parents: SYS-002/003, TBD reliability classification, SAF tier, Vol 18.4, REQ-HFPX-SCA-003/004. Children: prediction-function records and VCRM cases (artefact IDs TBD).
RTM: REQ-HFPX-RPM-001..004 → CONCEPT. Each function traces to indicators TBD → AI hook TBD → human authority → VCRM closure (all TBD except direction).

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Changes via change records with affected-function impact stated.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (predictive-maintenance advisory direction; functions TBD, human authority) |
