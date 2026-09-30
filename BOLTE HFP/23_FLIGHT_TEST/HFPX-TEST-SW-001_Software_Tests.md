# Software Tests

**Document ID:** HFPX-TEST-SW-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the software-test methodology (Chapter 23.8): unit/integration/system level structure referenced to Vol 16, coverage-criteria discipline, regression rule, and release-gate rule.
Methodology and gating only; no hazardous test-execution instructions.

## 2. Scope

Covers software verification methodology at unit, integration, and system levels (details TBD, Vol 16). Excludes detailed cases, procedures, coverage values (TBD) and flight conduct (Vol 23.10–23.14, Vol 25-gated).

## 3. Applicable Documents

- HFPX-TEST-STR-001 Test & Evaluation Strategy (gated thread, no-skipping)
- HFPX-VV-PLN-001 V&V Plan (REQ-HFPX-VVP-001..006)
- HFPX-PGM-SEM-001 SEMP (DDR-001 gate discipline)
- HFPX-SYS-REQ-001 SyRS (tier allocation TBD); Vol 16 (software assurance/levels, TBD)
- Vol 13 / Vol 24 (hazard-derived software obligations, TBD); Vol 25 (authorisation — TBD)

## 4. Definitions & Acronyms

- Unit: lowest software verification level (TBD, Vol 16).
- Integration: verification of software-software and software-hardware interfaces (TBD).
- System: verification of software in representative system context including SIL/HIL (TBD).
- Coverage: the defined measure of test completeness (criteria TBD, no percentages baselined).
- Release gate: the formal decision authorising a software release for the next test stage (criteria TBD).

## 5. System Context

Software testing ascends unit → integration → system (SIL/HIL), feeding flight stages only through closed gates and release decisions:

```text
UNIT → INTEGRATION → SYSTEM (SIL/HIL) → [RELEASE GATE] → GROUND / FLIGHT STAGES
```

All cases traced via the VCRM; advisory-AI vs deterministic-control separation per V&V Plan (details TBD).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-TSW-001 | Software verification shall be structured across unit, integration, and system levels referenced to Vol 16, with objectives and entrance/exit criteria defined per level and values recorded as TBD. | VVP-003 | Inspection |
| REQ-HFPX-TSW-002 | Each software-test level shall define coverage criteria before execution, with all coverage thresholds recorded as TBD and no percentages baselined in this revision. | VVP-005 | Test |
| REQ-HFPX-TSW-003 | Software changes shall trigger regression verification under a defined regression rule, with scope, method, and acceptance recorded as TBD. | VVP-002 | Analysis |
| REQ-HFPX-TSW-004 | Each software release for test-stage use shall satisfy a defined release-gate rule including evidence, configuration baseline, and approval, with rule details recorded as TBD. | VVP-004 | Demonstration |

All pass/fail and coverage thresholds: TBD. No quantitative values are baselined in this revision.

## 7. Architecture

Test levels (details TBD): unit environments (TBD), integration environments (TBD), system SIL/HIL configurations (TBD). Configuration management and release authority TBD. Data interfaces to Vol 23.16–23.17 (TBD).

## 8. Detailed Design

Level structure (values TBD): per-level objective, Vol 16 parent, article/configuration, environment, entrance/exit criteria, evidence set.
Coverage structure: per-level coverage measure (TBD), threshold (TBD), tooling (TBD), exclusion/waiver logic (TBD).
Regression-rule structure: change trigger, impact analysis, affected VCRM rows, re-verification scope (details TBD).
Release-gate structure: evidence package, baseline identity, approval authority (TBD), stage applicability (TBD).

## 9. Interfaces

- Software tests ↔ Vol 16 (levels, assurance logic — TBD).
- Software tests ↔ VCRM (case IDs, methods, levels — TBD).
- Software tests ↔ Ground/flight stages (only via release gates and stage gates, no skipping per DDR-001 / VVP-004).
- Software tests ↔ Safety/authorisation (Vol 13/24/25 — TBD).

## 10. Operational Concept

Define level cases and TBD coverage → confirm entrance criteria and baseline → execute at lowest adequate level → capture evidence → regression on change → release-gate decision → stage-gate progression.
No release in this document authorises flight; flight use requires closed gates and Vol 25 authorisation (TBD).

## 11. Safety

Safety-relevant software threads require independent review per VVP-006 (degree TBD). Deterministic bounded functions are the verified subject where AI-advisory threads exist (details TBD). This document contains no hazardous test-execution instructions.

## 12. Performance

Indicators TBD (no thresholds baselined): level-coverage completeness (TBD), coverage-threshold definition completeness (TBD), regression backlog (TBD), release-gate first-pass rate (TBD). Method and cadence TBD.

## 13. Verification & Validation

This document is verified at SRR/PDR against the SEMP checklist (header, 20 sections, IDs, shall-statements, A/I/D/T allocation, regression and release-gate rules, no-skipping alignment).
Validation is programme-authority approval at gated reviews. Certification validation owned by Vol 25 (no claims here).

## 14. Risks

- Coverage thresholds left TBD indefinitely; mitigation: per-level TBD tracking with due gate (assignments TBD).
- Regression scope creep or omission after change; mitigation: REQ-HFPX-TSW-003 regression rule with change-record linkage.
- Ungated software releases reaching test stages; mitigation: REQ-HFPX-TSW-004 release-gate rule.

## 15. Open Issues

Unit/integration/system objectives and criteria TBD (Vol 16). All coverage thresholds TBD (no percentages). Regression scope, method, acceptance TBD. Release-gate evidence, baseline, authority TBD.

## 16. Assumptions

- A-TSW-001: Vol 16 level definitions can host all software verification claims; validation: PDR review.
- A-TSW-002: Coverage tooling adequate for defined measures will be available at TBD maturity; validation: CDR review.

## 17. Dependencies

Depends on HFPX-TEST-STR-001, HFPX-TEST-GND-001, V&V Plan, SEMP gates, SyRS tier allocation, Vol 16 software volumes, Vol 23.16–23.17 instrumentation/data, Vol 25 authorisation.

## 18. Traceability

Parents: REQ-HFPX-VVP-001..006; HFPX-SYS-REQ-001 (tier allocation TBD); Vol 16 (level parents, TBD). Children: software verification cases and VCRM rows (IDs TBD).
RTM: REQ-HFPX-TSW-001..004 → CONCEPT. No orphaned requirements in this document.

## 19. Configuration

BL-0.0 (structure only) — Tranche 4 draft, not baselined. CONCEPT. Future changes via change records; changes re-validate affected VCRM rows before gate claims.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (Ch 23.8 Software Tests) |
