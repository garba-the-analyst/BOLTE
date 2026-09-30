# Thermal Tests

**Document ID:** HFPX-TEST-THM-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the thermal-test methodology (Chapter 23.6): survey-scope structure referenced to Vol 14, limit discipline, pass/fail discipline, and model-correlation rule.
Methodology and gating only; no hazardous test-execution instructions.

## 2. Scope

Covers thermal verification methodology (survey, limits, correlation) referencing Vol 14 threads (scope TBD). Excludes detailed thermal cases, procedures, and limit values (TBD) and flight conduct (Vol 23.10–23.14, Vol 25-gated).

## 3. Applicable Documents

- HFPX-TEST-STR-001 Test & Evaluation Strategy (gated thread, no-skipping)
- HFPX-VV-PLN-001 V&V Plan (REQ-HFPX-VVP-001..006)
- HFPX-PGM-SEM-001 SEMP (DDR-001 gate discipline)
- HFPX-SYS-REQ-001 SyRS (tier allocation TBD); Vol 14 (thermal design/analysis, TBD)
- Vol 13 / Vol 24 (hazard-derived obligations, TBD); Vol 25 (authorisation — TBD)

## 4. Definitions & Acronyms

- Thermal survey: the planned mapping of temperature distributions across configurations and environments (scope TBD).
- Limits: operational and safety temperature bounds (values TBD).
- Model correlation: documented comparison of thermal-model predictions to measured results (tolerances TBD).

## 5. System Context

Thermal testing sits in the subsystem-to-integrated ground segment, correlating Vol 14 models to measured evidence before flight credit:

```text
THERMAL ANALYSIS (Vol 14) ⇄ SURVEY / LIMITS TESTING → [GATE] → FLIGHT
```

All cases traced via the VCRM with representativeness arguments (TBD per claim).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-TTH-001 | The thermal-test scope shall address the thermal survey referenced to Vol 14, with survey points, configurations, and environments recorded as TBD. | VVP-001 | Inspection |
| REQ-HFPX-TTH-002 | Each thermal-test case shall define applicable thermal limits, with all limit values recorded as TBD in this revision. | VVP-005 | Test |
| REQ-HFPX-TTH-003 | Every thermal-test case shall define pass/fail criteria before execution, with all threshold values recorded as TBD in this revision. | VVP-005 | Test |
| REQ-HFPX-TTH-004 | Thermal models shall be correlated to measured test results under a defined correlation rule, with tolerances, method, and acceptance recorded as TBD. | VVP-002 | Analysis |

All pass/fail thresholds and limits: TBD. No temperature or tolerance values are baselined in this revision.

## 7. Architecture

Test configurations (details TBD): survey rigs/fixtures (TBD), integrated ground thermal configurations (TBD). Ownership, calibration, adequacy TBD per HFPX-TEST-GND-001. Correlation interfaces to Vol 14 and Vol 23.16–23.17 data (TBD).

## 8. Detailed Design

Survey structure (values TBD): per-point objective, Vol 14 parent, article configuration, environment, entrance/exit criteria, evidence set.
Limit structure: applicable limits per case (TBD), margin policy (TBD), exceedance disposition (TBD; methodology reference only).
Correlation-rule structure: prediction set, measurement set, comparison method (TBD), tolerance (TBD), acceptance (TBD).

## 9. Interfaces

- Thermal tests ↔ Vol 14 (models, limit definitions — TBD).
- Thermal tests ↔ VCRM (case IDs, methods, levels — TBD).
- Thermal tests ↔ Ground programme (HFPX-TEST-GND-001: rig ownership, credit rule).
- Thermal tests ↔ Safety/authorisation (Vol 13/24/25 — TBD).

## 10. Operational Concept

Define case and TBD criteria/limits → confirm entrance criteria → execute at lowest adequate configuration per authorised procedure (procedure TBD, not in this document) → capture data → correlate to model → review → gate decision.
No case authorises flight; flight credit requires closed gates and Vol 25 authorisation (TBD).

## 11. Safety

Thermal exceedances with safety implications require independent review per VVP-006 (degree TBD). Hazardous thermal configurations are subject to safety/range controls TBD via Vol 25 hooks. This document contains no hazardous test-execution instructions.

## 12. Performance

Indicators TBD (no thresholds baselined): survey-coverage completeness (TBD), limit-definition completeness (TBD), correlation acceptance rate (TBD), first-pass rate (TBD). Method and cadence TBD.

## 13. Verification & Validation

This document is verified at SRR/PDR against the SEMP checklist (header, 20 sections, IDs, shall-statements, A/I/D/T allocation, correlation rule, no-skipping alignment).
Validation is programme-authority approval at gated reviews. Certification validation owned by Vol 25 (no claims here).

## 14. Risks

- Limits left TBD enabling unbounded testing; mitigation: REQ-HFPX-TTH-002 limit rule with gate check (values TBD).
- Model correlation tolerances left TBD; mitigation: REQ-HFPX-TTH-004 correlation rule with acceptance gate (threshold TBD).
- Criteria left TBD blocking closure; mitigation: per-case TBD tracking with due gate (assignments TBD).

## 15. Open Issues

Survey scope, points, configurations, environments TBD (Vol 14). All limits TBD. All pass/fail thresholds TBD. Correlation method and tolerances TBD.

## 16. Assumptions

- A-TTH-001: Vol 14 thermal models adequate for pre-test prediction exist at TBD maturity; validation: PDR review.
- A-TTH-002: Thermal surveys can be executed without prescribing hazardous operations in this document; validation: safety review.

## 17. Dependencies

Depends on HFPX-TEST-STR-001, HFPX-TEST-GND-001, V&V Plan, SEMP gates, SyRS tier allocation, Vol 14 analysis, Vol 23.16–23.17 instrumentation/data, Vol 25 authorisation.

## 18. Traceability

Parents: REQ-HFPX-VVP-001..006; HFPX-SYS-REQ-001 (tier allocation TBD); Vol 14 (thread parents, TBD). Children: thermal verification cases and VCRM rows (IDs TBD).
RTM: REQ-HFPX-TTH-001..004 → CONCEPT. No orphaned requirements in this document.

## 19. Configuration

BL-0.0 (structure only) — Tranche 4 draft, not baselined. CONCEPT. Future changes via change records; changes re-validate affected VCRM rows before gate claims.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (Ch 23.6 Thermal Tests) |
