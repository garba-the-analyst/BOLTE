# Propulsion Tests

**Document ID:** HFPX-TEST-PRP-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

> **Boundary note (mandatory).** This document defines propulsion test *methodology and gating only* (progression, measurement-set structure, abort-rule structure, flight-credit rule). It contains no instructions for constructing, fuelling, igniting, or operating propulsion hardware, no fuel/ignition recipes, and no flight-execution procedures. All thresholds and procedures are TBD and subject to Vol 25 authorisation and appropriate engineering, test, safety, and regulatory controls.

## 1. Purpose

Define the propulsion-test methodology (Chapter 23.3): controlled-conditions progression from bench to rig to integrated configurations, measurement-set structure, abort-rule structure, and flight-credit rule.
Methodology and gating only; no hazardous test-execution instructions.

## 2. Scope

Covers propulsion verification methodology at bench, rig/subsystem, and integrated ground configurations. Excludes build, fuel handling, ignition execution, flight conduct (Vol 23.10–23.14), and detailed procedures/thresholds (TBD, Vol 25-gated).

## 3. Applicable Documents

- HFPX-TEST-STR-001 Test & Evaluation Strategy (gated thread, no-skipping)
- HFPX-VV-PLN-001 V&V Plan (REQ-HFPX-VVP-001..006)
- HFPX-PGM-SEM-001 SEMP (DDR-001 gate discipline)
- HFPX-SYS-REQ-001 SyRS (tier allocation TBD); propulsion design volumes (articles, TBD)
- Vol 13 / Vol 24 (hazard-derived obligations, TBD); Vol 25 (range-safety, authorisation — TBD)

## 4. Definitions & Acronyms

- Bench: component/element-level verification under controlled conditions.
- Rig: subsystem-level propulsion verification configuration (TBD).
- Integrated: multi-subsystem ground configuration (TBD).
- Abort rule: pre-defined conditions and authority requiring test termination (values and logic TBD).
- Controlled conditions: constrained, authorised, instrumented configuration — details TBD per case.

## 5. System Context

Propulsion testing occupies the subsystem-to-integrated segment of the gated thread, feeding flight stages only through closed gates and Vol 25 authorisation:

```text
BENCH → RIG → INTEGRATED GROUND → [GATE] → UNMANNED / TETHERED / HUMAN / EXPANSION
```

All credit flows via the VCRM with representativeness arguments (TBD per claim).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-TPR-001 | Propulsion verification shall progress bench → rig → integrated configurations under controlled conditions, with entrance/exit criteria defined per stage and threshold values recorded as TBD. | VVP-004 | Demonstration |
| REQ-HFPX-TPR-002 | Each propulsion test case shall define its measurement set including thrust and related parameters, with instruments, sampling, and all threshold values recorded as TBD and no figures baselined in this revision. | VVP-005 | Test |
| REQ-HFPX-TPR-003 | Each propulsion test configuration shall define abort rules including conditions, authority, and evidence capture, with rule details recorded as TBD via Vol 25 hooks. | VVP-006 | Inspection |
| REQ-HFPX-TPR-004 | Propulsion ground results claimed as flight-verification credit shall satisfy the ground-to-flight credit rule with representativeness and gate approval, with rule details TBD per claim and no credit claimed in this revision. | VVP-004 | Analysis |

All pass/fail thresholds including thrust values: TBD. No quantitative values are baselined in this revision.

## 7. Architecture

Test levels (details TBD): bench articles and fixtures (TBD), rig configurations (TBD), integrated ground configuration (TBD). Ownership, calibration, and adequacy TBD per HFPX-TEST-GND-001. Instrumentation feeds Vol 23.16–23.17 (TBD).

## 8. Detailed Design

Progression structure: per-stage objective, article configuration, controlled-conditions constraints, entrance/exit criteria (TBD), evidence set, gate record.
Measurement-set structure (values TBD): thrust (TBD), pressures/temperatures/flows/vibration as applicable (TBD), instrument identity, range, sampling, uncertainty (all TBD).
Abort-rule structure (logic TBD): monitored conditions (TBD), thresholds (TBD), authority, termination method (methodology reference only, no execution instruction), post-abort evidence capture.
Credit-rule structure: representativeness + coverage mapping + independent review + gate decision.

## 9. Interfaces

- Propulsion tests ↔ VCRM (case IDs, methods, levels — TBD).
- Propulsion tests ↔ Design volumes (articles, ICDs — TBD).
- Propulsion tests ↔ Ground programme (HFPX-TEST-GND-001: rig ownership, credit rule).
- Propulsion tests ↔ Safety/authorisation (Vol 13/24/25: hazard controls, range-safety, authorisation — TBD).

## 10. Operational Concept

Lowest-adequate-stage-first under controlled, authorised conditions: define case and TBD criteria → confirm entrance criteria → verify abort-rule structure and authorisation → execute per authorised procedure (procedure TBD, not in this document) → capture data → review → gate decision.
No case in this document authorises ignition, fuelling, or flight.

## 11. Safety

Hazardous propulsion configurations require safety review and independent verification per VVP-006 (degree TBD). Range-safety controls, abort authority, and flight authorisation are TBD via Vol 25 hooks. This document contains no hazardous test-execution instructions.

## 12. Performance

Indicators TBD (no thresholds baselined): stage-closure burn-down (TBD), measurement-completeness (TBD), abort-rule definition completeness (TBD), credit-claim acceptance (TBD). Method and cadence TBD.

## 13. Verification & Validation

This document is verified at SRR/PDR against the SEMP checklist (header, 20 sections, IDs, shall-statements, A/I/D/T allocation, boundary note, no-skipping alignment).
Validation is programme-authority approval at gated reviews. Certification validation owned by Vol 25 (no claims here).

## 14. Risks

- Pressure to bypass bench/rig stages; mitigation: REQ-HFPX-TPR-001 progression rule with DDR-001 / VVP-004 no-skipping enforcement.
- Measurement set defined without thresholds; mitigation: per-case TBD tracking with due gate (assignments TBD).
- Over-claim of ground results for flight; mitigation: REQ-HFPX-TPR-004 credit rule with gate approval.

## 15. Open Issues

Stage entrance/exit values TBD. Measurement set instruments, sampling, and all thresholds TBD (thrust TBD, no figures). Abort-rule conditions, authority, and logic TBD (Vol 25). Credit-rule details TBD per claim. Procedures TBD (not in this volume section).

## 16. Assumptions

- A-TPR-001: Controlled-conditions bench/rig/integrated configurations can be defined adequate for stated verification claims; validation: independent review.
- A-TPR-002: Abort-rule structure can be defined without prescribing execution actions in this document; validation: safety review.

## 17. Dependencies

Depends on HFPX-TEST-STR-001, HFPX-TEST-GND-001, V&V Plan, SEMP gates, SyRS tier allocation, propulsion design volumes, Vol 23.16–23.17 instrumentation/data, Vol 25 authorisation/credit rules.

## 18. Traceability

Parents: REQ-HFPX-VVP-001..006; HFPX-SYS-REQ-001 (tier allocation TBD); HFPX-TEST-STR-001 (thread). Children: propulsion verification cases and VCRM rows (IDs TBD).
RTM: REQ-HFPX-TPR-001..004 → CONCEPT. No orphaned requirements in this document.

## 19. Configuration

BL-0.0 (structure only) — Tranche 4 draft, not baselined. CONCEPT. Future changes via change records; changes re-validate affected VCRM rows before gate claims.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (Ch 23.3 Propulsion Tests) |
