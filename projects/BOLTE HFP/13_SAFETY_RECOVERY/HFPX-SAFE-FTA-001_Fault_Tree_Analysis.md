# Fault Tree Analysis

**Document ID:** HFPX-SAFE-FTA-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 3 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X Fault Tree Analysis (Vol 13.6): top events, method and symbology, basic-event data rule, minimal-cut-set review, and flow to redundancy requirements.

## 2. Scope

Top-down analysis of TBD-final top events across hover, transition, and recovery phases. Qualitative structure in this revision; quantitative data TBD. Boundary note: analysis structure only — no propulsion build, ignition, or operation instructions; no recovery build or operation instructions.

## 3. Applicable Documents

- HFPX-SAFE-CAS-001 Safety Case (REQ-HFPX-SCA-001/002/006)
- HFPX-SAFE-HAZ-001; HFPX-SAFE-FHA-001; HFPX-SAFE-FME-001
- Safety tier SAF-001..006; SAD SFA-003; SEMP; V&V Plan

## 4. Definitions & Acronyms

- FTA: Fault Tree Analysis — top-down Boolean decomposition of a top event into basic events via gates.
- Gate symbology: AND / OR / TBD voted gates (definitions TBD); basic event: undecomposed failure with data TBD.
- Minimal cut set: smallest basic-event combination causing the top event; no probabilities asserted here.

## 5. System Context

FTA tests architectural adequacy: cut sets expose single points of failure and justify redundancy requirements verified under Vol 24.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-FTA-001 | The FTA shall define top events including uncontrolled descent in hover, failed transition with loss of control, and recovery-system non-deployment, with the final list TBD. | REQ-HFPX-SCA-002, SAF-002, SFA-003 | Analysis |
| REQ-HFPX-FTA-002 | The FTA shall use defined gate symbology (AND/OR/TBD) recorded per tree. | REQ-HFPX-SCA-002, SAF-006 | Inspection |
| REQ-HFPX-FTA-003 | Basic-event data shall remain TBD; no probabilities or rates shall be asserted until data sources and approval are defined. | REQ-HFPX-SCA-001, SAF-003 | Inspection |
|REQ-HFPX-FTA-004|Minimal cut sets shall be reviewed with single-point and TBD-order cut rules recorded.|REQ-HFPX-SCA-006, SAF-006, SFA-003|Inspection|
| REQ-HFPX-FTA-005 | FTA results shall flow to redundancy requirements traced to the SAF tier. | REQ-HFPX-SCA-002, SAF-006, SFA-003 | Analysis |

## 7. Architecture

One tree per top event; basic events sourced from FMEA rows; common-cause links flagged for CCA.

## 8. Detailed Design

Method: define top event → decompose to intermediate events → terminate in basic events (TBD data) → compute/review cut sets qualitatively → derive redundancy requirements. Each branch preserves Hazard → Cause → Effect → Severity(TBD) → Probability(TBD) → Mitigation(TBD) → Verification(TBD).

Text fault-tree sketch (qualitative, one top event, 3 levels):

```text
TOP: Uncontrolled descent in hover (Severity TBD, Probability TBD)
 ├─ AND/OR TBD: Loss of net hover thrust
 │    ├─ BASIC (TBD): Arm-module thrust loss (FMEA row; data TBD)
 │    └─ BASIC (TBD): Fuel-feed interruption (FMEA row; data TBD)
 └─ AND/OR TBD: Loss of hover control authority
      ├─ BASIC (TBD): Safety-computer channel fault (data TBD)
      └─ BASIC (TBD): Erroneous transition command (data TBD)
MITIGATION: TBD → Redundancy requirement (TBD) → VERIFICATION: TBD
```

## 9. Interfaces

- FTA ↔ FMEA: basic events from FMEA modes.
- FTA ↔ CCA: shared-cause branches flagged.
- FTA ↔ SAD / SAF tier: redundancy requirements allocated and traced.

## 10. Operational Concept

Build qualitative trees pre-CDR → review cut sets → derive redundancy → quantify only after data approval (TBD). Methodology and gating only.

## 11. Safety

No probabilities or rates asserted; no redundancy effectiveness claimed. Analysis only.

## 12. Performance

Indicators TBD: tree coverage of top events, cut-set review closure, redundancy derivation completeness. No thresholds baselined.

## 13. Verification & Validation

Verified by review (symbology, cut-set rule, data-TBD rule). Validation at CDR/FRR gates.

## 14. Risks

- Top-event list incompleteness; mitigation: FHA-tied list, final TBD.
- Invented data creeping into trees; mitigation: REQ-HFPX-FTA-003 TBD rule.
- Unreviewed single points of failure; mitigation: cut-set review rule.

## 15. Open Issues

Final top-event list TBD. Gate symbology definitions TBD. All basic-event data TBD. Redundancy requirements TBD.

## 16. Assumptions

- A-FTA-01: Listed top events bound concept FTA scope; validation: FHA review (TBD).
- A-FTA-02: Qualitative trees suffice before data approval; validation: CDR review (TBD).

## 17. Dependencies

Depends on Safety Case, HAZ/FHA/FME, SAF-001..006, SFA-003, SEMP, CCA-001, Vol 24.

## 18. Traceability

Parents: REQ-HFPX-SCA-001/002/006; SAF-001..006; SFA-003. Children: Vol 13.8–13.18; Vol 24. RTM: REQ-HFPX-FTA-001..005 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 3 draft, not baselined. Changes via change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 3 draft (FTA structure, sketch tree) |
