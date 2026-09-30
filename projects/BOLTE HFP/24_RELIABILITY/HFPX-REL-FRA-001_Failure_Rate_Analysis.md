# Failure Rate Analysis

**Document ID:** HFPX-REL-FRA-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X failure-rate analysis direction for Volume 24 (Chapter 24.3): how failure-rate data sources, uncertainty treatment, and update rules will be controlled.
Sets data-source hierarchy and analysis rules only; it contains no failure rates or MTBF values beyond TBD.

## 2. Scope

Covers system and item failure-rate analysis inputs feeding Vol 24.2 allocation, Vol 24.4–24.6 analyses, and Vol 13 safety analyses as applicable.
In scope: source hierarchy, rate records, uncertainty treatment, update rule. Out of scope: quantitative rates, which are TBD, and demonstration testing owned under V&V.
Data-source hierarchy direction: handbook, test, and field precedence TBD.

## 3. Applicable Documents

- Programme Charter STK-001; SyRS SYS-002/003; reliability classification tier TBD; SAF tier (stubs)
- HFPX-REL-ENG-001 Reliability Engineering, HFPX-REL-ALC-001 Reliability Allocation, HFPX-SAFE-CAS-001 Safety Case
- HFPX-VV-PLN-001 V&V Plan; Vol 13.5/13.6 analysis exchange; Vol 27 field-data hooks as applicable
- Standards (structured according to): TBD — no compliance claimed in this revision

## 4. Definitions & Acronyms

- Failure rate: frequency measure of failure occurrence for a defined scope and conditions; all values TBD
- Data-source hierarchy: ordered precedence of handbook, test, and field sources; order and applicability TBD
- Uncertainty treatment: method for recording confidence, bounds, and data quality; method TBD
- Update rule: controlled revision of rates when higher-precedence data becomes available; triggers TBD
- TBD: to be determined; TBC: to be confirmed

## 5. System Context

Failure-rate analysis provides inputs to allocation assessment, FMEA/FTA, and availability modelling; credibility depends on source hierarchy and uncertainty recording.
This document constrains data discipline; it does not assert any rate is valid in this revision.
Operating scope, environment, and duty definitions feeding rates are TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-RFR-001 | The programme shall define a failure-rate data-source hierarchy across handbook, test, and field sources, with precedence and applicability TBD. | TBD reliability classification; HFPX-REL-ENG-001 | Inspection |
| REQ-HFPX-RFR-002 | The programme shall record failure rates with defined scope and conditions, with all rates TBD and record schema TBD. | TBD reliability classification; Vol 24.2 allocation | Inspection |
| REQ-HFPX-RFR-003 | The programme shall apply a defined uncertainty treatment to failure-rate inputs, with method and recording rules TBD. | TBD reliability classification; REQ-HFPX-SCA-004 | Analysis |
| REQ-HFPX-RFR-004 | The programme shall control failure-rate updates under a defined update rule, with triggers, authority, and re-verification TBD. | TBD reliability classification; SEMP gates | Inspection |

## 7. Architecture

Analysis structure TBD: rate tables per indenture level, ownership TBD, independent review TBD.
Record architecture TBD: schema fields TBD beyond ID, scope, source, rate TBD, uncertainty TBD, status.
Source-to-analysis flow TBD: hierarchy → rate record → consumer analyses (Vol 24.2/24.4–24.6, Vol 13.5/13.6).

## 8. Detailed Design

Methodology only, no values:
- Source hierarchy: handbook applicability TBD; test-data qualification TBD; field-data qualification TBD; precedence rules TBD.
- Rate records: scope definitions TBD (operating conditions, duty, environment TBD); all rate fields TBD.
- Uncertainty treatment: confidence recording TBD; bounding method TBD; data-quality flags TBD.
- Update rule: triggers TBD; supersession method TBD; propagation to consumers TBD.

## 9. Interfaces

- Failure-rate ↔ Allocation (Vol 24.2 budgets assessed against rate inputs; values TBD both sides)
- Failure-rate ↔ FMEA/FTA (Vol 24.4/24.5 and Vol 13.5/13.6 logic inputs; quantification TBD)
- Failure-rate ↔ Availability/MTBF (Vol 24.6/24.8 model inputs; models and values TBD)
- Failure-rate ↔ V&V (test and field evidence qualifies sources under V&V Plan; criteria TBD)
- Failure-rate ↔ Support/field (Vol 27 field-data hooks; schema and ownership TBD)

## 10. Operational Concept

Failure-rate maturity across the lifecycle: initial hierarchy-defined placeholders at SRR → refinement through test → field-data incorporation as applicable → gate acceptance TBD.
This concept defines data-maturation discipline only, not test conduct or field operations.
No rate is asserted as valid in this revision.

## 11. Safety

No safety claim is made in this revision; rate outputs may inform Vol 13 analyses but take no safety credit until verified through the safety path.
No probability claim for any hazard is made here; hazard probabilities owned by Vol 13 with scales TBD.

## 12. Performance

Failure-rate performance indicators TBD (no thresholds baselined): source traceability TBD, uncertainty-recording completeness TBD, update backlog TBD.
No failure rates, MTBF values, availability figures, or life limits are set in this revision.

## 13. Verification & Validation

This document is verified at SRR/PDR against the SEMP checklist (header, 20 sections, IDs, no-values rule, hierarchy direction).
Requirement verification follows the V&V Plan: Inspection/Analysis methods; acceptance criteria TBD per case; evidence TBD until closed.
Validation is programme-authority approval at gates; certification validation owned by Vol 25 with no claims here.

## 14. Risks

- Handbook data treated as proven without qualification; mitigation: hierarchy and qualification rules TBD before use
- Uncertainty hidden by point values; mitigation: mandatory uncertainty recording TBD
- Stale rates propagated after design change; mitigation: update rule with consumer-notification TBD

## 15. Open Issues

Source hierarchy precedence TBD. All rates TBD. Scope and condition definitions TBD. Uncertainty method TBD. Update triggers and authority TBD. Record schema TBD. Vol 13/27 exchange details TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on STK-001/SYS-002/003 and TBD reliability classification, HFPX-REL-ENG-001, HFPX-REL-ALC-001, SEMP, V&V Plan, SAF tier and HFPX-SAFE-CAS-001, Vol 13.5/13.6, Vol 24.2/24.4–24.6/24.8, Vol 27 field hooks.

## 18. Traceability

Parents: SYS-002/003, TBD reliability classification, HFPX-REL-ENG-001, SAF tier. Children: rate tables and consumer analyses (artefact IDs TBD).
RTM: REQ-HFPX-RFR-001..004 → CONCEPT. Each rate traces to source → uncertainty record → consumer analysis → VCRM case (all TBD except direction).

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Changes via change records with affected-rate impact stated.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (data-source hierarchy and update rules; rates TBD) |
