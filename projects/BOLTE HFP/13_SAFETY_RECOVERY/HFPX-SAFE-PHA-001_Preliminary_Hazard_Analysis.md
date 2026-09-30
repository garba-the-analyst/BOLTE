# Preliminary Hazard Analysis

**Document ID:** HFPX-SAFE-PHA-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 3 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X Preliminary Hazard Analysis (Vol 13.3): concept-stage qualitative method, outputs, update rule, and completion criteria feeding FHA/FMEA.

## 2. Scope

Concept-stage PHA across SYS-01..23 and 15 flight modes using checklist, energy-source, and functional-decomposition methods. Boundary note: analysis structure only — no propulsion build, ignition, or operation instructions; no recovery build or operation instructions.

## 3. Applicable Documents

- HFPX-SAFE-CAS-001 Safety Case (REQ-HFPX-SCA-001/002/006)
- HFPX-SAFE-HAZ-001 Hazard Analysis (log schema, coverage)
- Safety tier SAF-001..006 (stubs); SAD SFA-003; SEMP; V&V Plan

## 4. Definitions & Acronyms

- PHA: Preliminary Hazard Analysis — early qualitative hazard identification before design maturity.
- Energy-source method: hazard search by energy form (kinetic, thermal, chemical, electrical — list TBD); functional decomposition: search by SAD function breakdown.
- PHA worksheet: TBD-format record with Hazard → Cause → Effect → Severity(TBD) → Probability(TBD) → Mitigation(TBD) → Verification(TBD).

## 5. System Context

PHA is the first analysis pass: it seeds the hazard log and scopes deeper FHA/FMEA/FTA/CCA. It bounds concept risk without claiming design safety.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-PHA-001 | The PHA shall address the concept-stage system across SYS-01..23 and 15 flight modes using qualitative reasoning only. | REQ-HFPX-SCA-002, SAF-002, SFA-003 | Analysis |
| REQ-HFPX-PHA-002 | The PHA shall apply checklist, energy-source, and functional-decomposition methods with TBD worksheets recorded per method. | REQ-HFPX-SCA-002, SAF-002, SFA-003 | Inspection |
| REQ-HFPX-PHA-003 | PHA outputs shall feed the hazard log and scope FHA and FMEA, with trace from each PHA row to log entries. | REQ-HFPX-SCA-001, SAF-006, SFA-003 | Analysis |
| REQ-HFPX-PHA-004 | The PHA shall be updated at PDR to reflect design maturity; deltas shall be recorded. | REQ-HFPX-SCA-002, SAF-006 | Inspection |
|REQ-HFPX-PHA-005|PHA completion criteria (coverage, review, TBD thresholds) shall be met before PHA closure is claimed.|REQ-HFPX-SCA-006, SAF-006|Inspection|

## 7. Architecture

PHA team: safety lead plus design delegates (staffing TBD); independent review per SEMP. Worksheets under safety configuration control.

## 8. Detailed Design

PHA method (TBD worksheets): (1) checklist pass per hazard class (fire/fuel/thermal/structural/software + TBD); (2) energy-source pass; (3) functional-decomposition pass per SFA-003 functions. Each row follows Hazard → Cause → Effect → Severity(TBD) → Probability(TBD) → Mitigation(TBD) → Verification(TBD).

Starter PHA worksheet (qualitative, no numbers):

| Hazard | Cause | Effect | Severity | Probability | Mitigation | Verification |
| --- | --- | --- | --- | --- | --- | --- |
| Loss of hover thrust margin | Qualitative: multiple arm-module degradation (detail TBD) | Descent below safe hover height (quantification TBD) | TBD | TBD | TBD | TBD |
| Uncommanded mode change | Qualitative: FCS mode-logic fault (detail TBD) | Departure from intended flight envelope (quantification TBD) | TBD | TBD | TBD | TBD |
| Fuel-related fire | Qualitative: fuel leak near hot surface (detail TBD) | Thermal damage / loss of function (quantification TBD) | TBD | TBD | TBD | TBD |
| Loss of pilot awareness cues | Qualitative: display or telemetry dropout (detail TBD) | Delayed corrective action (quantification TBD) | TBD | TBD | TBD | TBD |

## 9. Interfaces

- PHA ↔ Hazard log: PHA rows create/extend log entries.
- PHA ↔ FHA/FMEA: PHA scopes deeper analyses.
- PHA ↔ SAD: functional decomposition follows SFA-003.

## 10. Operational Concept

Conduct PHA pre-PDR → review → feed FHA/FMEA → update at PDR. Gating and methodology only.

## 11. Safety

Qualitative only; no probabilities asserted. No build/ignition/operation instructions.

## 12. Performance

Indicators TBD: worksheet coverage, log feed-through, PDR update closure. No thresholds baselined.

## 13. Verification & Validation

Verified by review of method application and trace to log. Validation at PDR gate.

## 14. Risks

- Checklist blindness to novel hazards; mitigation: energy-source + functional passes.
- PHA staleness after design change; mitigation: PDR update rule.
- Premature closure; mitigation: completion criteria TBD.

## 15. Open Issues

Worksheets TBD. Energy-source list TBD. Completion criteria TBD. All ratings/mitigations TBD.

## 16. Assumptions

- A-PHA-01: Qualitative PHA suffices to scope FHA/FMEA at concept; validation: PDR review (TBD).
- A-PHA-02: SAD functional breakdown is stable enough for decomposition; validation: SAD review (TBD).

## 17. Dependencies

Depends on Safety Case, HAZ-001 log, SAF-001..006, SFA-003, SEMP, Vol 24.

## 18. Traceability

Parents: REQ-HFPX-SCA-001/002/006; SAF-001..006; SFA-003. Children: Vol 13.8–13.18; Vol 24. RTM: REQ-HFPX-PHA-001..005 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 3 draft, not baselined. Worksheet changes via change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 3 draft (PHA structure, starter worksheet) |
