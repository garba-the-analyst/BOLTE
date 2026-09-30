# Transition Tests (Vol 23.12)

**Document ID:** HFPX-TEST-TRN-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define test-methodology and planning requirements for HFP-X transition tests (Chapter 23.12).
Establishes build-up discipline, entry/exit/abort criteria discipline, failed-transition response discipline, data-set discipline supporting the FTN thread, and the no-human-exposure rule until unmanned transition is demonstrated.
This document contains planning methodology only; it contains no flight-execution instructions, manoeuvre recipes, or propulsion-operation instructions.

## 2. Scope

Covers transition-test planning between flight regimes (regime definitions TBD): build-up sequencing logic, entry/exit/abort criteria frameworks, failed-transition response planning, and data requirements validating the FTN thread.
Applies to unmanned transition demonstration first; any human exposure is out of scope until the unmanned-transition gate is closed.
Out of scope: flight-execution procedures, manoeuvre recipes, handling qualities direction, propulsion operation, and certification credit — all TBD elsewhere.
Content is limited to requirements, architecture, interfaces, test methodology and safety analysis; it shall not contain instructions for constructing, igniting, or operating human-carrying high-energy propulsion outside appropriate engineering, test, safety and regulatory controls.

## 3. Applicable Documents

- HFPX-VV-PLN-001 V&V Plan (REQ-HFPX-VVP-001..006)
- HFPX-TEST-IDX-001 Vol 23 index / Test & Evaluation Strategy (TBD)
- HFPX-PGM-SEM-001 SEMP (gated reviews)
- HFPX-SAFE-CAS-001 Safety Case; Vol 13/24 hazard inputs (TBD)
- Vol 25 authorisation / range-safety rules (TBD)
- FTN flight-transition thread; MRQ/MAR threads (notably MRQ-002 — details TBD); CONOPS threads (TBD)
- DDR-001 gated-progression decision; MIS-006 / MVP-001 gating (TBD)
- Vol 23.11 unmanned evidence; Vol 23.16/23.17/23.18 threads

## 4. Definitions & Acronyms

- Transition: change between flight regimes (definitions and boundaries TBD) evaluated through a planned build-up.
- Build-up: ordered progression of test conditions of increasing challenge (steps TBD), each with entry/exit criteria.
- Failed transition: inability to achieve or sustain the planned regime change within defined criteria (criteria TBD), triggering defined response.
- FTN thread: flight-transition analysis/design thread validated in part by transition-test data (details TBD).
- A/I/D/T: Analysis / Inspection / Demonstration / Test per HFPX-VV-PLN-001 §4; TBD: unknown data, no values baselined.

## 5. System Context

Transition tests sit on the unmanned path of the gated chain and inform downstream tethered/human-flight and envelope-expansion decisions strictly through gate records.
No human exposure is permitted on transition objectives until unmanned transition has been demonstrated and accepted through the applicable gate with FRR-type authorisation where required (criteria TBD).
Gates shall not be skipped per REQ-HFPX-VVP-004 and DDR-001.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-TTN-001 | The transition-test campaign shall define an ordered build-up with objectives and sequencing logic (steps and success logic TBD) per test stage. | REQ-HFPX-VVP-005, FTN (TBD) | Inspection |
| REQ-HFPX-TTN-002 | Each transition-test step shall define entry, exit, and abort criteria (all TBD) before authorisation, with range-safety hooks per Vol 25. | REQ-HFPX-VVP-004, REQ-HFPX-VVP-005, Vol 25 (TBD) | Inspection |
| REQ-HFPX-TTN-003 | The programme shall define failed-transition response actions, including safeing, recovery interfaces, and review and re-entry logic (all TBD). | REQ-HFPX-VVP-006 | Demonstration |
| REQ-HFPX-TTN-004 | Each transition test shall define and capture the data set (measurands, conditions, quality rules — all TBD) required to validate the FTN thread. | REQ-HFPX-VVP-005, FTN (TBD) | Test |
| REQ-HFPX-TTN-005 | No human exposure shall be permitted on transition objectives until unmanned transition demonstration (scope TBD) is accepted and FRR-type authorisation (criteria TBD) is granted per the DDR-001 gate. | REQ-HFPX-VVP-004, DDR-001, MIS-006, MRQ-002 | Inspection |

All envelopes, thresholds, and criteria are TBD. No values are baselined in this revision.

## 7. Architecture

Organisation (roles TBD): flight-test lead, FTN-thread owner, safety/range interface, instrumentation and analysis leads, independent verifier.
Build-up architecture: stage → step → criteria set (entry/exit/abort TBD) → data set → analysis → gate recommendation; each step requires its own readiness and closure record.
Evidence architecture: unmanned transition evidence package feeds any subsequent tethered/human-flight consideration only through formal gate acceptance.

## 8. Detailed Design

Methodology elements only (no execution instructions):
- Build-up decomposition: objectives → ordered steps TBD → per-step conditions and constraints TBD → success logic TBD.
- Criteria framework: entry conditions TBD, exit/success logic TBD, abort triggers TBD, decision authority TBD, post-step review TBD.
- Failed-transition framework: detection logic TBD, safeing/recovery interfaces TBD, evidence preservation TBD, investigation and re-entry gate TBD.
- Data framework: FTN-validation data set TBD, recording and quality rules TBD, trace to Vol 23.16/23.17.
No manoeuvre recipes, handling instructions, or propulsion-operation sequences are defined in this document.

## 9. Interfaces

- V&V ↔ Vol 22 VCRM: each REQ-HFPX-TTN row traces to verification case(s) TBD.
- Transition tests ↔ FTN thread and MRQ-002: validation and demonstration trace.
- Transition tests ↔ Vol 23.11/23.10: unmanned-evidence and tether interfaces.
- Transition tests ↔ Vol 23.16/23.17/23.18: instrumentation, analysis, reporting threads.
- Transition tests ↔ Safety (Vol 13/24) and Vol 25: hazard controls, range-safety, authorisation threads (all TBD).

## 10. Operational Concept

Campaign-level flow only: define build-up and criteria → define data needs → assemble readiness/authorisation package → seek authorisation → conduct authorised testing under range controls → capture data → analyse against FTN needs → step/gate review.
Test conduct, vehicle handling, range operations, and recovery execution belong to authorised procedures and range orders (TBD, Vol 25), not this document.
Failed transitions and exceedances invoke defined response and review before any re-entry or progression.

## 11. Safety

Transition testing is safety-gated: no step without closed entry criteria and authorisation (both TBD).
Failed-transition and abort planning per REQ-HFPX-TTN-002/003 bounds testing within TBD conditions; hazard controls flow from Vol 13/24 with independent review to a degree TBD.
The no-human-exposure rule per REQ-HFPX-TTN-005 is absolute pending unmanned demonstration and FRR-type authorisation.
Range-safety hooks TBD per Vol 25; no range approval or certification credit claimed here.

## 12. Performance

Indicators TBD (no thresholds baselined): build-up step-closure progress, criteria-definition completeness, FTN-data completeness, failed-transition review backlog.
Measurement and reporting cadence TBD in Vol 22/23 children.

## 13. Verification & Validation

Each REQ-HFPX-TTN row receives a single primary method (A/I/D/T) per REQ-HFPX-VVP-001; per-step acceptance criteria are TBD per case per REQ-HFPX-VVP-005.
This document is verified by inspection for header, 20-section structure, shall-statements, parent trace (including FTN and MRQ-002), A/I/D/T allocation, TBD discipline, gated-progression and no-human-exposure rules, and methodology-only boundary.
Validation is programme-authority review at the applicable gate; certification validation is owned by Vol 25.

## 14. Risks

- Build-up steps and criteria left TBD, blocking readiness; mitigation: per-step criteria-definition gate.
- Pressure to expose human test subjects before unmanned transition is demonstrated; mitigation: REQ-HFPX-TTN-005 / DDR-001 prohibition with formal gate records.
- FTN-validation data gaps or undefined failed-transition response; mitigation: REQ-HFPX-TTN-003/004 data and response discipline.

## 15. Open Issues

Build-up steps, conditions, and sequencing TBD. Entry/exit/abort criteria and authority TBD. Failed-transition detection, safeing, and re-entry logic TBD. FTN-validation data set TBD. Unmanned-transition acceptance scope and FRR-type criteria TBD. Range-safety hooks TBD (Vol 25).

## 16. Assumptions

- A-TTN-001: Transition regimes and boundaries can be defined sufficiently to support a build-up argument (details TBD); validation: FTN-thread review.
- A-TTN-002: Unmanned transition results can support downstream claims only through explicitly traced similarity/gate claims (method TBC).

## 17. Dependencies

Depends on V&V Plan and VCRM discipline, SEMP gates, FTN thread definition, MRQ-002/MAR/CONOPS parents, unmanned evidence (Vol 23.11), Safety and Vol 25 inputs, and Vol 23.16/23.17/23.18 capability.

## 18. Traceability

Parents: REQ-HFPX-VVP-001, REQ-HFPX-VVP-004, REQ-HFPX-VVP-005, REQ-HFPX-VVP-006; FTN (TBD); MRQ-002; DDR-001; MIS-006; CONOPS (TBD); Vol 25 (TBD).
Children: transition verification cases and procedures (IDs TBD; VCRM rows TBD).
RTM: REQ-HFPX-TTN-001..005 → CONCEPT. No orphans per REQ-HFPX-VVP-002 (to be shown in VCRM).

## 19. Configuration

BL-0.0. Tranche 4 draft, CONCEPT, not baselined. Future changes via change records; any baselined-requirement change re-opens affected VCRM rows until re-verified.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (Vol 23.12 Transition Tests; methodology/planning only, all values TBD) |
