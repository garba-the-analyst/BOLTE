# Functional Hazard Assessment

**Document ID:** HFPX-SAFE-FHA-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 3 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X Functional Hazard Assessment (Vol 13.4): assessment of loss/malfunction of SAD functional-view functions, classification, safety-requirement derivation, independence, update, and review rules.

## 2. Scope

Assesses aviate / navigate / communicate / protect functions per SAD functional view and derived sub-functions (list TBD). Covers loss, malfunction, and erroneous function (omission/commission TBD). Analysis only — no build or operation instructions.

## 3. Applicable Documents

- HFPX-SAFE-CAS-001 Safety Case (REQ-HFPX-SCA-001/002/006)
- HFPX-SAFE-HAZ-001; HFPX-SAFE-PHA-001
- Safety tier SAF-001..006; SAD SFA-003 (functional view); SEMP; V&V Plan

## 4. Definitions & Acronyms

- FHA: Functional Hazard Assessment — function-level failure-condition analysis independent of implementation.
- Failure condition: effect of functional loss/malfunction at aircraft level; classification scale TBD (levels and definitions TBD).
- Assessor independence: organisational separation of assessor from designers, degree TBD.

## 5. System Context

FHA bridges functions to safety requirements: each functional failure condition derives safety requirements allocated to architecture, verified under Vol 24.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-FHA-001 | The FHA shall assess loss and malfunction of aviate, navigate, communicate, and protect functions per the SAD functional view. | REQ-HFPX-SCA-002, SAF-002, SFA-003 | Analysis |
| REQ-HFPX-FHA-002 | Each failure condition shall be classified on a TBD scale with TBD definitions; no classification shall be asserted until the scale is approved. | REQ-HFPX-SCA-001, SAF-003, SFA-003 | Inspection |
| REQ-HFPX-FHA-003 | Each classified failure condition shall derive safety requirements traced to the SAF tier. | REQ-HFPX-SCA-002, SAF-006, SFA-003 | Analysis |
|REQ-HFPX-FHA-004|The FHA assessor shall be independent of the design team to a TBD degree.|REQ-HFPX-SCA-002, SAF-006|Inspection|
| REQ-HFPX-FHA-005 | The FHA shall be updated at PDR and CDR to reflect functional and architectural maturity. | REQ-HFPX-SCA-002, SAF-006, SFA-003 | Inspection |
|REQ-HFPX-FHA-006|The FHA shall be verified by review against coverage, classification, and derivation rules.|REQ-HFPX-SCA-006, SAF-006|Inspection|

## 7. Architecture

FHA structure follows SFA-003 function tree; each function row expands to failure conditions. Safety requirements allocated via SAD.

## 8. Detailed Design

FHA row schema: Function, Failure (loss/malfunction/erroneous), Hazard → Cause → Effect → Severity(TBD) → Probability(TBD) → Mitigation(TBD) → Verification(TBD), plus Classification (TBD) and derived safety requirement ID.

Starter FHA table (classifications TBD):

| Function / Failure | Hazard → Cause → Effect | Severity | Probability | Classification | Mitigation / Derived Req | Verification |
| --- | --- | --- | --- | --- | --- | --- |
| Aviate — loss of hover stabilisation | Hazard: uncontrolled hover departure → Cause (qualitative): FCS stabilisation loss (detail TBD) → Effect: loss of hover control (quantification TBD) | TBD | TBD | TBD | TBD | TBD |
| Aviate — erroneous transition command | Hazard: uncommanded transition → Cause (qualitative): erroneous mode command (detail TBD) → Effect: envelope departure (quantification TBD) | TBD | TBD | TBD | TBD | TBD |
| Protect — loss of emergency stabilisation | Hazard: failed safe-state entry → Cause (qualitative): backup stabilisation unavailable (detail TBD) → Effect: no assured recovery path (quantification TBD) | TBD | TBD | TBD | TBD | TBD |
| Navigate — loss of attitude/position data | Hazard: loss of navigation solution → Cause (qualitative): sensor/solution fault (detail TBD) → Effect: degraded control and awareness (quantification TBD) | TBD | TBD | TBD | TBD | TBD |
| Communicate — loss of telemetry/voice | Hazard: loss of off-board link → Cause (qualitative): link failure (detail TBD) → Effect: delayed abort/guidance (quantification TBD) | TBD | TBD | TBD | TBD | TBD |

## 9. Interfaces

- FHA ↔ SAD: function list from SFA-003.
- FHA ↔ Hazard log: failure conditions create/extend rows.
- FHA ↔ SAF tier / Vol 24: derived requirements enter VCRM.

## 10. Operational Concept

Assess functions pre-PDR → classify (TBD scale) → derive requirements → update at PDR/CDR → review-verify. Methodology and gating only.

## 11. Safety

No classifications or safety targets asserted; scale TBD. No compliance claimed.

## 12. Performance

Indicators TBD: function coverage, derivation completeness, update closure. No thresholds baselined.

## 13. Verification & Validation

Verified by review (REQ-HFPX-FHA-006). Validation at PDR/CDR gates.

## 14. Risks

- Incomplete function list; mitigation: SAD trace audit.
- Classification subjectivity; mitigation: TBD scale gate.
- Orphan failure conditions without derived requirements; mitigation: derivation audit.

## 15. Open Issues

Classification scale TBD. Assessor independence degree TBD. Derived requirement IDs TBD. All ratings TBD.

## 16. Assumptions

- A-FHA-01: SFA-003 functional view bounds aviate/navigate/communicate/protect at concept; validation: SAD review (TBD).
- A-FHA-02: Qualitative failure conditions suffice before PDR; validation: PDR review (TBD).

## 17. Dependencies

Depends on Safety Case, HAZ-001, PHA-001, SAF-001..006, SFA-003, SEMP, Vol 24.

## 18. Traceability

Parents: REQ-HFPX-SCA-001/002/006; SAF-001..006; SFA-003. Children: Vol 13.8–13.18; Vol 24. RTM: REQ-HFPX-FHA-001..006 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 3 draft, not baselined. Changes via change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 3 draft (FHA structure, starter table) |
