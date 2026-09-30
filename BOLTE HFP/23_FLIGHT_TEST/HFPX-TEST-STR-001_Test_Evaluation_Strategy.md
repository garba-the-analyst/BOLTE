# Test & Evaluation Strategy

**Document ID:** HFPX-TEST-STR-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the Volume 23 test and evaluation strategy (Chapter 23.1): the gated methodology, stage structure, entrance/exit discipline, article-representativeness rule, data-capture rule, and no-gate-skipping rule governing all ground and flight test activity.
This document sets methodology and gating only; it contains no propulsion build, fuel, ignition, or flight-execution instructions.

## 2. Scope

Covers the end-to-end test thread: simulation → SIL → HIL → subsystem → integrated → unmanned → tethered → human → envelope expansion.
Applies to all Vol 23 children (23.2–23.18). Detailed scopes, procedures, pass/fail values, and range conduct are owned by child documents (criteria TBD). Range-safety and authorisation rules are hooked to Vol 25 (TBD).

## 3. Applicable Documents

- HFPX-VV-PLN-001 V&V Plan (REQ-HFPX-VVP-001..006 — method assignment, VCRM, levels, gated progression, acceptance, independence)
- HFPX-PGM-SEM-001 SEMP (gated reviews, DDR-001 gate discipline)
- HFPX-SYS-REQ-001 SyRS (§13 verification approach)
- HFPX-SAFE-CAS-001 Safety Case (companion); Vol 13 / Vol 24 (hazard-derived test obligations, TBD)
- Vol 25 (range-safety, authorisation, certification credit — TBD, no credit claimed)
- Vol 23 children HFPX-TEST-GND-001 through HFPX-TEST-CTL-001 and 23.10–23.18 (TBD)

## 4. Definitions & Acronyms

- SIL: System/Software Integration Laboratory; HIL: Hardware-in-the-Loop.
- Gate: a formal decision point with entrance criteria, evidence, and exit authorisation.
- Gate skipping: proceeding to a higher test stage without closing the prior gate — prohibited.
- Test article: the hardware/software/configuration under test; representativeness: the documented claim that an article and environment are adequate for the verification credit sought.
- TBD / TBC: not yet defined; no values baselined in this revision.

## 5. System Context

The test strategy sits on the right-hand side of the programme V-model, executing verification cases defined via the Vol 22 VCRM:

```text
SIM → SIL → HIL → SUBSYSTEM → INTEGRATED → UNMANNED → TETHERED → HUMAN → EXPANSION
  ↑________________ GATE DECISIONS (entrance / evidence / exit) ________________↑
  ↑________________ VCRM TRACEABILITY → Vol 22.3 _______________________________↑
  ↑________________ INDEPENDENT SAFETY VERIFICATION ____________________________↑
```

MVP (Vol 33) follows the same gated logic in miniature under separate control; no production credit is claimed from MVP results unless explicitly traced.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-TST-001 | The test programme shall execute verification through the gated thread simulation → SIL → HIL → subsystem → integrated → unmanned → tethered → human → envelope expansion, with each stage's objectives and evidence defined before entry. | VVP-004 | Inspection |
| REQ-HFPX-TST-002 | Each test stage shall define entrance criteria and exit criteria before entry, with all threshold values recorded as TBD in this revision and closed by formal gate decision. | VVP-005 | Inspection |
| REQ-HFPX-TST-003 | Each test claim shall document test-article representativeness (configuration, fidelity, environment limits), with representativeness acceptance criteria TBD per claim. | VVP-003 | Analysis |
| REQ-HFPX-TST-004 | The test programme shall capture and retain test data, configuration, and gate records per a defined data-rights and data-capture plan, with tooling, retention, and access rules TBD. | VVP-002 | Inspection |
| REQ-HFPX-TST-005 | The test programme shall prohibit gate skipping; progression to any higher stage without closure of all prior gate exit criteria and formal authorisation is prohibited. | VVP-004, DDR-001 | Demonstration |

All pass/fail thresholds: TBD. No quantitative acceptance values are baselined in this revision.

## 7. Architecture

Test organisation (roles TBD): test lead, ground-test lead, flight-test lead, data/instrumentation lead, independent safety verifier reporting via Safety Review Board.
Stage structure: Vol 23.2 ground; 23.3–23.9 domain tests (propulsion, fuel, structures, thermal, avionics, software, control); 23.10–23.11 tethered/unmanned; 23.12 transition; 23.13 human; 23.14 expansion; 23.15–23.18 emergency, instrumentation, analysis, reporting.
Gate board membership, cadence, and tooling TBD in Vol 22/23 children.

## 8. Detailed Design

Stage objectives (methodology only, criteria TBD): sim — model-based verification of threads; SIL — integrated software/functions; HIL — hardware-in-the-loop; subsystem — domain-level verification; integrated — end-to-end ground integration; unmanned — flight verification without crew; tethered — constrained human-proximate verification; human — crewed verification only after prior gates and FRR; expansion — incremental envelope growth within authorised bounds (bounds TBD).
Each stage template shall contain objective, traced parent requirement(s), entrance criteria, evidence set, exit criteria (TBD per stage), and gate-record reference.
No stage description in this document authorises test execution; execution is gated by Vol 25 authorisation hooks (TBD).

## 9. Interfaces

- Strategy ↔ V&V (Vol 22: VCRM rows, method A/I/D/T, level allocation).
- Strategy ↔ Safety (Vol 13/24: hazard-derived test obligations flow in; closure evidence flows back).
- Strategy ↔ Design volumes (Vol 03–18 provide articles and design evidence; ICDs per 02.17 define interface threads).
- Strategy ↔ Certification/authorisation (Vol 25: range-safety rules, flight authorisation, certification credit — all TBD).

## 10. Operational Concept

Operate gate-to-gate: plan cases early → define entrance/exit criteria → assemble representative article → execute at the lowest adequate stage → capture data → independent review where safety-relevant → formal gate decision → progress or remediate.
Flight stages (unmanned, tethered, human, expansion) are verification levels, not operations; conduct, range, and handling belong to Vol 23.10–23.14 under Vol 25 authorisation (TBD).

## 11. Safety

Safety-relevant test threads require independent review per VVP-006 (degree TBD). Catastrophic-hazard closure evidence is independently verified before any human-flight gate is considered (criterion TBD, owned by Safety Case).
This document contains no hazardous test-execution instructions. Range-safety controls and abort/authorisation logic are TBD (Vol 25 hooks).

## 12. Performance

Strategy effectiveness indicators TBD (no thresholds baselined): gate first-pass rate (TBD), VCRM test-coverage (TBD), gate-evidence closure burn-down (TBD), regression backlog (TBD). Measurement method and cadence TBD in Vol 22/23 children.

## 13. Verification & Validation

This document is verified at SRR/PDR against the SEMP checklist (header, 20 sections, IDs, shall-statements, A/I/D/T allocation, gated thread, no-skipping rule).
Validation is programme-authority approval at gated reviews. Certification validation is owned by Vol 25 (no claims here).

## 14. Risks

- Pressure to skip gates to accelerate flight; mitigation: REQ-HFPX-TST-005 no-skipping rule with formal gate records (DDR-001 / VVP-004).
- Entrance/exit criteria left TBD indefinitely; mitigation: per-stage TBD tracking with owning volume and due gate (assignments TBD).
- Unrepresentative articles generating false credit; mitigation: REQ-HFPX-TST-003 representativeness rule with independent review.

## 15. Open Issues

Stage entrance/exit threshold values TBD. Gate board membership and cadence TBD. Data tooling, retention, and rights TBD. Range-safety and authorisation hooks TBD (Vol 25). Representativeness acceptance criteria TBD per claim.

## 16. Assumptions

- A-TST-001: The nine-stage thread is adequate as the single backbone for all Vol 23 verification; validation: SRR review.
- A-TST-002: Formal gate records can be maintained with TBD document control; validation: Vol 22.3 pilot matrix.
- A-TST-003: Unmanned/tethered evidence can support human-flight threads only through explicitly traced similarity claims (method TBC).

## 17. Dependencies

Depends on V&V Plan (methods, VCRM, independence), SEMP (gates, DDR-001), SyRS §13, Safety Case and Vol 13 hazards, Vol 19 analysis capability, Vol 23 children execution capability, Vol 25 authorisation/credit rules.

## 18. Traceability

Parents: REQ-HFPX-VVP-001..006; HFPX-SYS-REQ-001 §13 (tier allocation TBD); SEMP DDR-001 (gate discipline). Children: Vol 23.2–23.18 test-methodology documents (verification case IDs TBD; VCRM rows TBD).
RTM: REQ-HFPX-TST-001..005 → CONCEPT. No orphaned requirements in this document.

## 19. Configuration

BL-0.0 (structure only) — Tranche 4 draft, not baselined. CONCEPT. Future changes via change records; any change re-validates affected VCRM rows before gate claims.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (Ch 23.1 Test & Evaluation Strategy) |
