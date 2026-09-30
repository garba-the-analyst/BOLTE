# Fuel-System Tests

**Document ID:** HFPX-TEST-FUL-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

> **Boundary note (mandatory).** This document defines fuel-system test *methodology and gating only* (rig/integrated structure, leak/isolation verification hooks, pass/fail discipline, controlled-conditions rule). It contains no instructions for fuelling, handling, pressurising, or operating fuel-system hardware, no fluid/handling recipes, and no flight-execution procedures. All thresholds and procedures are TBD and subject to Vol 25 authorisation and appropriate engineering, test, safety, and regulatory controls.

## 1. Purpose

Define the fuel-system test methodology (Chapter 23.4): rig and integrated test structure, leak/isolation verification hooks, pass/fail discipline, and controlled-conditions rule.
Methodology and gating only; no hazardous test-execution instructions.

## 2. Scope

Covers fuel-system verification methodology at rig/subsystem and integrated ground configurations. Excludes fuel handling execution, detailed procedures/thresholds (TBD), and flight conduct (Vol 23.10–23.14, Vol 25-gated).

## 3. Applicable Documents

- HFPX-TEST-STR-001 Test & Evaluation Strategy (gated thread, no-skipping)
- HFPX-VV-PLN-001 V&V Plan (REQ-HFPX-VVP-001..006)
- HFPX-PGM-SEM-001 SEMP (DDR-001 gate discipline)
- HFPX-SYS-REQ-001 SyRS (tier allocation TBD); fuel-system design volumes (articles, TBD)
- Vol 13 / Vol 24 (hazard-derived obligations including leak/isolation, TBD); Vol 25 (range-safety, authorisation — TBD)

## 4. Definitions & Acronyms

- Rig test: subsystem-level fuel-system verification configuration (TBD).
- Integrated test: multi-subsystem ground configuration including fuel-system interfaces (TBD).
- Leak/isolation verification: the thread confirming containment and isolation functions (hooks only; criteria TBD).
- Controlled conditions: constrained, authorised, instrumented configuration — details TBD per case.

## 5. System Context

Fuel-system testing occupies the subsystem-to-integrated segment of the gated thread, with leak/isolation threads traced from hazard-derived safety requirements:

```text
RIG → INTEGRATED GROUND → [GATE] → FLIGHT STAGES (Vol 25-authorised, TBD)
  ↑_________ LEAK / ISOLATION HOOKS ← Vol 13/24 _________↑
```

All credit flows via the VCRM with representativeness arguments (TBD per claim).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-TFL-001 | Fuel-system verification shall be structured as rig tests and integrated tests under controlled conditions, with objectives, configurations, and entrance/exit criteria defined per case and values recorded as TBD. | VVP-004 | Demonstration |
| REQ-HFPX-TFL-002 | Fuel-system leak and isolation functions shall have verification hooks traced to parent hazard-derived requirements, with methods, levels, and criteria recorded as TBD. | VVP-002 | Inspection |
| REQ-HFPX-TFL-003 | Every fuel-system test case shall define pass/fail criteria before execution, with all threshold values recorded as TBD in this revision. | VVP-005 | Test |
| REQ-HFPX-TFL-004 | Fuel-system testing shall be conducted only under defined controlled conditions including configuration control, authorisation, and evidence capture, with condition details recorded as TBD via Vol 25 hooks. | VVP-006 | Demonstration |

All pass/fail thresholds: TBD. No quantitative values are baselined in this revision.

## 7. Architecture

Test levels (details TBD): fuel-system rigs and fixtures (ownership TBD per HFPX-TEST-GND-001), integrated ground configuration (TBD). Leak/isolation hooks interface to Vol 13/24 safety threads. Instrumentation feeds Vol 23.16–23.17 (TBD).

## 8. Detailed Design

Rig/integrated structure (values TBD): per-case objective, article configuration, interface set, controlled-conditions constraints, entrance/exit criteria, evidence set, gate record.
Leak/isolation hook structure: parent hazard-derived requirement (TBD) → verification case ID (TBD) → method (A/I/D/T, TBD) → level (TBD) → criteria (TBD).
Controlled-conditions structure: configuration baseline, authorisation, monitoring, evidence capture (details TBD; no execution instruction in this document).

## 9. Interfaces

- Fuel tests ↔ VCRM (case IDs, methods, levels — TBD).
- Fuel tests ↔ Design volumes (articles, ICDs — TBD).
- Fuel tests ↔ Ground programme (HFPX-TEST-GND-001: rig ownership, credit rule).
- Fuel tests ↔ Safety/authorisation (Vol 13/24/25: leak/isolation parents, range-safety, authorisation — TBD).

## 10. Operational Concept

Lowest-adequate-stage-first under controlled, authorised conditions: define case and TBD criteria → confirm entrance criteria and leak/isolation hooks → verify authorisation → execute per authorised procedure (procedure TBD, not in this document) → capture data → review → gate decision.
No case in this document authorises fuelling or flight.

## 11. Safety

Fuel-system configurations require safety review and independent verification per VVP-006 (degree TBD). Leak/isolation closure evidence is independently reviewed where safety-relevant (criterion TBD). Range-safety and authorisation are TBD via Vol 25 hooks. This document contains no hazardous test-execution instructions.

## 12. Performance

Indicators TBD (no thresholds baselined): rig/integrated coverage (TBD), hook-trace completeness (TBD), first-pass rate (TBD), controlled-conditions compliance (TBD). Method and cadence TBD.

## 13. Verification & Validation

This document is verified at SRR/PDR against the SEMP checklist (header, 20 sections, IDs, shall-statements, A/I/D/T allocation, boundary note, no-skipping alignment).
Validation is programme-authority approval at gated reviews. Certification validation owned by Vol 25 (no claims here).

## 14. Risks

- Leak/isolation hooks left untraced; mitigation: REQ-HFPX-TFL-002 hook rule with VCRM coverage gate (threshold TBD).
- Controlled conditions left TBD enabling unauthorised execution; mitigation: REQ-HFPX-TFL-004 rule with Vol 25 authorisation gate.
- Criteria left TBD blocking closure; mitigation: per-case TBD tracking with due gate (assignments TBD).

## 15. Open Issues

Rig/integrated objectives and configurations TBD. Leak/isolation parents, methods, levels, criteria TBD. All pass/fail thresholds TBD. Controlled-conditions details and authorisation TBD (Vol 25). Procedures TBD (not in this volume section).

## 16. Assumptions

- A-TFL-001: Rig and integrated configurations can be defined adequate for fuel-system verification claims via arguments TBD per claim; validation: independent review.
- A-TFL-002: Leak/isolation functions can be verified without prescribing handling actions in this document; validation: safety review.

## 17. Dependencies

Depends on HFPX-TEST-STR-001, HFPX-TEST-GND-001, V&V Plan, SEMP gates, SyRS tier allocation, fuel-system design volumes, Vol 13/24 hazard parents, Vol 23.16–23.17 instrumentation/data, Vol 25 authorisation/credit rules.

## 18. Traceability

Parents: REQ-HFPX-VVP-001..006; HFPX-SYS-REQ-001 (tier allocation TBD); HFPX-TEST-STR-001 (thread). Children: fuel-system verification cases and VCRM rows (IDs TBD).
RTM: REQ-HFPX-TFL-001..004 → CONCEPT. No orphaned requirements in this document.

## 19. Configuration

BL-0.0 (structure only) — Tranche 4 draft, not baselined. CONCEPT. Future changes via change records; changes re-validate affected VCRM rows before gate claims.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (Ch 23.4 Fuel-System Tests) |
