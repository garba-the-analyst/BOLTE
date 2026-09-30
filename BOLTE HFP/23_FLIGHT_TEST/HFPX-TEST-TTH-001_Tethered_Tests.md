# Tethered Tests (Vol 23.10)

**Document ID:** HFPX-TEST-TTH-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define test-methodology and planning requirements for HFP-X tethered tests (Chapter 23.10).
Establishes tether-system requirements ownership, test-objective discipline, gated entry criteria, and abort-rule discipline.
This document contains planning methodology only; it contains no flight-execution instructions, manoeuvre recipes, or propulsion-operation instructions.

## 2. Scope

Covers tethered-test planning for restrained flight-test configurations: tether-system requirements (TBD), test objectives and success criteria (TBD), entry-gate evidence, and abort rules.
Applies after prior unmanned evidence gate and before any controlled human-flight claims.
Out of scope: flight-execution procedures, vehicle handling instructions, manoeuvre definitions, propulsion build/ignition/operation, tether detailed design, range conduct orders, and certification credit — all TBD in owning volumes/authorities.
Content is limited to requirements, architecture, interfaces, test methodology and safety analysis; it shall not contain instructions for constructing, igniting, or operating human-carrying high-energy propulsion outside appropriate engineering, test, safety and regulatory controls.

## 3. Applicable Documents

- HFPX-VV-PLN-001 V&V Plan (REQ-HFPX-VVP-001..006 — method allocation, VCRM, gated progression, acceptance principles)
- HFPX-TEST-IDX-001 Vol 23 index / Test & Evaluation Strategy (TBD)
- HFPX-PGM-SEM-001 SEMP (gated reviews, entrance/exit discipline)
- HFPX-SAFE-CAS-001 Safety Case; Vol 13/24 hazard and safety requirements (TBD)
- Vol 25 authorisation / range-safety / certification-credit rules (TBD)
- CONOPS threads (TBD); MRQ/MAR threads for flight items (TBD)
- DDR-001 gated-progression decision (tethered/human stages require prior unmanned evidence + FRR-type authorisation)
- MIS-006 / MVP-001 gating constraints (TBD)

## 4. Definitions & Acronyms

- Tethered test: restrained flight-test configuration with physical restraint system (requirements TBD) used to bound motion/energy while collecting test data under authorised conditions.
- TBD / TBC: unknown data; no values baselined in this revision.
- FRR-type authorisation: formal flight-readiness gate decision for the applicable test stage (criteria, membership, authority TBD per Vol 25).
- Gate skipping: proceeding without closing prior gate exit criteria — prohibited per REQ-HFPX-VVP-004 and DDR-001.
- A/I/D/T: Analysis / Inspection / Demonstration / Test per HFPX-VV-PLN-001 §4.

## 5. System Context

Tethered tests sit between unmanned flight evidence and any human-flight-test consideration in the gated chain: sim → SIL → HIL → subsystem → integrated propulsion → unmanned → tethered → controlled human flight → envelope expansion.
Tethered testing does not replace unmanned verification and does not grant human-flight credit; it provides bounded, instrumented test conditions under FRR-type control to inform subsequent gate decisions.
Tether-system definition, range authorisation, instrumentation (Vol 23.16), and data analysis (Vol 23.17) are interfacing capabilities, not directed by this document.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-TTT-001 | The programme shall define tether-system requirements (functions, attachment, restraint behaviour, monitoring, and release/safeing interfaces — all TBD) before tethered testing, with each requirement allocated a verification method. | REQ-HFPX-VVP-001, REQ-HFPX-VVP-004 | Inspection |
| REQ-HFPX-TTT-002 | The tethered-test campaign shall define test objectives and success criteria (conditions, measurands, and pass/fail logic — all TBD) per test, traced to parent needs and CONOPS threads. | REQ-HFPX-VVP-005, CONOPS (TBD) | Test |
| REQ-HFPX-TTT-003 | Tethered testing shall not commence until prior unmanned hover evidence (scope TBD) is accepted and FRR-type authorisation (criteria, authority TBD) is granted per the DDR-001 gate. | REQ-HFPX-VVP-004, DDR-001, MIS-006 | Inspection |
| REQ-HFPX-TTT-004 | The programme shall define tethered-test abort rules, abort decision authority, and post-abort response and review actions (all TBD), with range-safety hooks per Vol 25. | REQ-HFPX-VVP-006, Vol 25 (TBD) | Inspection |

All envelopes, thresholds, loads, and criteria are TBD. No values are baselined in this revision.

## 7. Architecture

Tethered-test planning organisation (roles TBD): flight-test lead, tether-system owner (TBD volume), safety/range interface, instrumentation and analysis leads (Vol 23.16/23.17), and independent safety verifier.
Test-article configuration: vehicle + restraint system + ground interfaces + instrumentation, each with defined configuration and representativeness claim (TBD per test).
Gate structure: unmanned-evidence review → tether readiness review / FRR-type gate (TBD) → authorised tethered-test window → data review → gate recommendation; no gate skipping.

## 8. Detailed Design

Methodology elements only (no execution instructions):
- Tether-system requirements capture: functional and safety requirements list (TBD), interface requirements to vehicle and ground (TBD), and verification allocation per REQ-HFPX-VVP-001.
- Objective decomposition: each tethered test maps to parent thread → objective → success criteria (TBD) → required measurands (via Vol 23.16) → analysis method (via Vol 23.17).
- Test-condition definition framework: configuration, environment envelope, and constraints recorded as TBD per test; envelope values are not baselined here.
- Abort-rule framework: abort triggers (TBD), decision roles (TBD), safeing and recovery interfaces (TBD), and evidence capture on abort.
No manoeuvre recipes, handling instructions, or propulsion-operation sequences are defined in this document.

## 9. Interfaces

- V&V ↔ Vol 22 VCRM: each REQ-HFPX-TTT row traces to verification case(s) TBD.
- Tethered tests ↔ unmanned evidence (Vol 23.11): entry-evidence thread.
- Tethered tests ↔ instrumentation (Vol 23.16) and data analysis (Vol 23.17): measurand and analysis threads.
- Tethered tests ↔ Safety (Vol 13/24) and Vol 25: hazard controls, range-safety hooks, and authorisation threads (all TBD).
- Tethered tests ↔ transition/human-flight planning (Vol 23.12/23.13): results feed forward as evidence only; no credit claimed beyond gate record.

## 10. Operational Concept

Campaign-level flow only: plan objectives and criteria → define tether-system and instrumentation needs → assemble entry-evidence package → seek FRR-type authorisation → conduct authorised testing under range/authority controls → capture data → analyse → gate review.
Test conduct, vehicle handling, range operations, and emergency response execution belong to authorised procedures and range orders (TBD, Vol 25), not this document.
Progression to any subsequent stage requires gate closure per DDR-001; anomalies invoke stop/review per abort rules (criteria TBD).

## 11. Safety

Tethered testing is safety-gated: no commencement without accepted prior evidence and FRR-type authorisation (criteria TBD).
Hazard-derived safety requirements and controls flow from Vol 13/24 and Safety Case; closure evidence is independently reviewed to a degree TBD.
Range-safety and authorisation hooks are TBD per Vol 25; this document claims no range approval and no certification credit.
Abort rules per REQ-HFPX-TTT-004 bound testing within TBD conditions; any exceedance triggers review before further testing.

## 12. Performance

Test-planning performance indicators TBD (no thresholds baselined): gate-readiness completeness, objective-to-criteria trace coverage, abort-rule definition completeness, data-capture completeness per test.
Measurement methods and reporting cadence TBD in Vol 22/23 children.

## 13. Verification & Validation

Each REQ-HFPX-TTT row receives a single primary method (A/I/D/T) per REQ-HFPX-VVP-001; acceptance criteria per tethered-test case are TBD per case per REQ-HFPX-VVP-005.
This document is verified by inspection for header, 20-section structure, shall-statements, parent trace, A/I/D/T allocation, TBD discipline (no invented numbers), gated-progression rule, and methodology-only boundary.
Validation is programme-authority review at the applicable gate; certification validation is owned by Vol 25 (no claims here).

## 14. Risks

- Tether-system requirements left TBD, blocking readiness; mitigation: requirements-capture gate with owning volume TBD.
- Pressure to enter tethered testing without unmanned evidence or FRR-type authorisation; mitigation: REQ-HFPX-TTT-003 / DDR-001 no-skipping rule with formal gate records.
- Abort criteria left TBD, risking inconsistent test decisions; mitigation: per-test abort-rule definition required before authorisation.

## 15. Open Issues

Tether-system requirements, attachment and monitoring design, and owning volume TBD. Test objectives, conditions, success criteria, and envelope values TBD per test. Unmanned-evidence scope for entry TBD. FRR-type membership, criteria, and authority TBD (Vol 25). Abort triggers, authority, and post-abort actions TBD. Range-safety hooks TBD.

## 16. Assumptions

- A-TTH-001: A restraint system can be defined that bounds tethered-test conditions sufficiently to support gate decisions; validation: tether-system requirements review (TBD).
- A-TTH-002: Unmanned hover evidence can be scoped to support a tethered-entry claim via explicit trace; validation: gate review (method TBC).

## 17. Dependencies

Depends on V&V Plan gating and VCRM discipline, SEMP gate process, Safety Case and Vol 13/24 hazard inputs, unmanned flight evidence (Vol 23.11), instrumentation and analysis capability (Vol 23.16/23.17), Vol 25 authorisation/range-safety rules, and CONOPS/MRQ/MAR parent threads (TBD).

## 18. Traceability

Parents: REQ-HFPX-VVP-001, REQ-HFPX-VVP-004, REQ-HFPX-VVP-005, REQ-HFPX-VVP-006; DDR-001; MIS-006; CONOPS (TBD); Vol 25 (TBD).
Children: tethered-test verification cases and procedures (IDs TBD; VCRM rows TBD).
RTM: REQ-HFPX-TTT-001..004 → CONCEPT. No orphaned requirements; no orphaned verification cases per REQ-HFPX-VVP-002 (to be shown in VCRM).

## 19. Configuration

BL-0.0. Tranche 4 draft, CONCEPT, not baselined. Future changes via change records; any baselined-requirement change re-opens affected VCRM rows until re-verified.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (Vol 23.10 Tethered Tests; methodology/planning only, all values TBD) |
