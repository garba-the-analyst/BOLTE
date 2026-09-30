# Hazard Analysis

**Document ID:** HFPX-SAFE-HAZ-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 3 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X hazard-analysis programme (Vol 13.2): hazard-log ownership, schema, coverage, scales, and analysis-to-requirement flow governing Vol 13.3–13.7.

## 2. Scope

Covers hazard identification, logging, and tracking across SYS-01..23 and all 15 flight modes. Boundary note: analysis structure only — no propulsion build, ignition, or operation instructions; no recovery build or operation instructions.

## 3. Applicable Documents

- HFPX-SAFE-CAS-001 Safety Case (REQ-HFPX-SCA-001/002/006)
- Safety requirements tier SAF-001..006 (stubs, values TBD); SAD functional view SFA-003
- SEMP (gates); V&V Plan; `13_SAFETY_RECOVERY/hazard_log.csv`; Vol 13.3–13.7 children; Vol 24 assurance

## 4. Definitions & Acronyms

- Hazard log: controlled record, one row per hazard, schema §8.
- Hazard → Cause → Effect → Severity → Probability → Mitigation → Verification: mandatory row chain; Severity/Probability scales TBD.
- SYS-01..23: SyRS requirement set; 15 flight modes: defined mode set, enumeration TBD (reference SAD).

## 5. System Context

Hazard analysis constrains all design volumes: no design claim proceeds without logged hazards, qualitative causes/effects, and traced mitigations. Hover/low-altitude is the limiting case (quantification TBD).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-HZA-001 | The programme shall maintain a single owned hazard log conforming to the schema in §8 with `hazard_log.csv` columns Hazard ID, Hazard, Cause, Effect, Severity, Probability, Mitigation, Verification, Status. | REQ-HFPX-SCA-001, SAF-001, SFA-003 | Inspection |
| REQ-HFPX-HZA-002 | The hazard analysis shall cover SYS-01..23 and all 15 flight modes, with coverage recorded per hazard (applicability TBD per mode). | REQ-HFPX-SCA-006, SAF-002, SFA-003 | Analysis |
| REQ-HFPX-HZA-003 | The programme shall define severity and probability scales before any retirement claim; all ratings shall remain TBD until scales are approved. | REQ-HFPX-SCA-001, SAF-003 | Inspection |
| REQ-HFPX-HZA-004 | Each hazard shall flow to safety requirements and verification cases; no hazard shall retire on analysis alone without verified mitigation. | REQ-HFPX-SCA-002, SAF-006, SFA-003 | Analysis |

## 7. Architecture

Hazard-log ownership: Safety lead owns log; design-domain delegates propose entries; independent verifier reviews; Safety Review Board retires (composition TBD). Log under safety configuration control once opened.

## 8. Detailed Design

Hazard-log schema (`hazard_log.csv` columns): Hazard ID, Hazard, Cause, Effect, Severity (TBD), Probability (TBD), Mitigation (TBD), Verification (TBD), Status. No empty Mitigation/Verification at retirement.

Starter hazard table (qualitative; ratings and mitigations TBD):

| Hazard | Cause | Effect | Severity | Probability | Mitigation | Verification |
| --- | --- | --- | --- | --- | --- | --- |
| Loss of distributed thrust in hover | Qualitative: arm-module thrust loss or fuel-feed interruption (detail TBD) | Uncontrolled descent / hard landing attitude (quantification TBD) | TBD | TBD | TBD | TBD |
| Uncommanded transition | Qualitative: erroneous transition command from FCS (detail TBD) | Loss of controlled flight path during mode change (quantification TBD) | TBD | TBD | TBD | TBD |
| Loss of telemetry mid-transition | Qualitative: telemetry-link loss or ground-station dropout (detail TBD) | Loss of situational awareness / delayed abort decision (quantification TBD) | TBD | TBD | TBD | TBD |
| Recovery-system failure at low altitude | Qualitative: non-deployment or partial deployment (detail TBD) | Insufficient recovery margin before ground contact (quantification TBD) | TBD | TBD | TBD | TBD |
| Pilot spatial disorientation | Qualitative: misleading cues during transition or hover (detail TBD) | Incorrect control inputs / delayed recovery action (quantification TBD) | TBD | TBD | TBD | TBD |

## 9. Interfaces

- Safety ↔ SE: log open at SRR; retirement gates per SEMP.
- Safety ↔ V&V: mitigations enter VCRM as safety requirements.
- Safety ↔ Vol 13.3–13.7: PHA/FHA/FMEA/FTA/CCA consume and extend log rows.
- Safety ↔ Vol 03–18: design owns mitigation implementation.

## 10. Operational Concept

Open log at SRR → populate via PHA/FHA → refine via FMEA/FTA/CCA → verify mitigations via Vol 24 → retire via Safety Review Board at gated reviews. Methodology and gating only; no flight conduct defined here.

## 11. Safety

No severity/probability values baselined; no retirement claimed. Recovery effectiveness unproven. Analysis only — no build/ignition/operation instructions.

## 12. Performance

Indicators TBD: log completeness, mode coverage, mitigation closure backlog. No thresholds baselined.

## 13. Verification & Validation

Verified by inspection against schema rule, coverage rule, and TBD-scale rule at SRR/PDR. Validation by Safety Review Board at gates.

## 14. Risks

- Incomplete mode coverage; mitigation: coverage matrix SYS-01..23 × 15 modes (TBD).
- Subjective ratings without scales; mitigation: REQ-HFPX-HZA-003 scale gate.
- Log debt outpacing design; mitigation: change-driven log updates.

## 15. Open Issues

Severity/probability scales TBD. 15-mode enumeration reference TBD. Log owner/board composition TBD. All mitigations and verifications TBD.

## 16. Assumptions

- A-HZA-01: SYS-01..23 plus 15 flight modes bound the hazard space at concept stage; validation: SAD/SyRS review (TBD).
- A-HZA-02: Qualitative causes/effects suffice before PDR; validation: PHA/FHA review (TBD).

## 17. Dependencies

Depends on Safety Case, SAF-001..006, SFA-003, SEMP (gates), V&V Plan, Vol 13.3–13.7, Vol 24.

## 18. Traceability

Parents: REQ-HFPX-SCA-001/002/006; SAF-001..006; SFA-003. Children: Vol 13.8–13.18; Vol 24 (VCRM safety cases, verification evidence). RTM: REQ-HFPX-HZA-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 3 draft, not baselined. Changes via change records with affected-hazard impact stated.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 3 draft (hazard-analysis structure, starter table) |
