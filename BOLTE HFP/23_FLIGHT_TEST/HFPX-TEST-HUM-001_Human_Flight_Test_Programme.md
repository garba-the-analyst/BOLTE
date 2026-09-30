# Human Flight Test Programme (Vol 23.13)

**Document ID:** HFPX-TEST-HUM-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define test-methodology and planning requirements for the HFP-X human flight test programme (Chapter 23.13).
Establishes FRR-type authorisation gating, pilot-qualification hooks, controlled-conditions discipline, incremental build-up discipline, and anomaly stop-rule discipline.
This document contains planning methodology only; it contains no flight-execution instructions, manoeuvre recipes, or propulsion-operation instructions.

## 2. Scope

Covers human-flight-test planning: authorisation gates, personnel-qualification needs, controlled-conditions rules, incremental build-up logic, and anomaly stop rules.
Applies only after all prior gated evidence (including unmanned demonstration and tethered stages where applicable) is accepted; human flight is the most constrained stage of the test chain.
Out of scope: flight-execution procedures, piloting instructions, manoeuvre definitions, propulsion operation, medical/certification decisions, and range conduct orders — all TBD in owning volumes/authorities.
Content is limited to requirements, architecture, interfaces, test methodology and safety analysis; it shall not contain instructions for constructing, igniting, or operating human-carrying high-energy propulsion outside appropriate engineering, test, safety and regulatory controls.

## 3. Applicable Documents

- HFPX-VV-PLN-001 V&V Plan (REQ-HFPX-VVP-001..006)
- HFPX-TEST-IDX-001 Vol 23 index / Test & Evaluation Strategy (TBD)
- HFPX-PGM-SEM-001 SEMP (gated reviews)
- HFPX-SAFE-CAS-001 Safety Case; Vol 13/24 hazard inputs (TBD)
- Vol 25 authorisation / range-safety / certification-credit rules (TBD)
- Vol 30 personnel / pilot-qualification rules (TBD)
- MRQ/MAR threads for flight items; CONOPS threads (all TBD)
- DDR-001 gated-progression decision; MIS-006 / MVP-001 gating (TBD)
- Vol 23.10–23.12 prior evidence; Vol 23.16/23.17/23.18 threads

## 4. Definitions & Acronyms

- Human flight test: flight-test configuration with human onboard, permitted only under FRR-type authorisation and controlled conditions (both TBD).
- FRR-type authorisation: formal flight-readiness gate for human flight (criteria, membership, authority TBD per Vol 25 and Safety Case).
- Controlled conditions: bounded configuration, environment, range, and support conditions defined per flight (all TBD).
- Stop rule: mandatory halt to human-flight testing on defined anomaly/trigger pending review (triggers TBD).
- A/I/D/T: Analysis / Inspection / Demonstration / Test per HFPX-VV-PLN-001 §4; TBD: unknown data, no values baselined.

## 5. System Context

The human flight test programme sits at the end of the gated chain: sim → SIL → HIL → subsystem → integrated propulsion → unmanned → tethered → controlled human flight → envelope expansion.
Human flight generates no routine operational capability in this revision; each flight is a gated test event requiring prior-evidence closure and explicit authorisation.
Gates shall not be skipped per REQ-HFPX-VVP-004 and DDR-001; catastrophic-hazard closure evidence is independently verified before any human-flight gate is considered (criterion TBD, owned by Safety Case).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-THM-001 | Human flight testing shall not commence without FRR-type authorisation (criteria, authority, evidence scope TBD) granted after acceptance of prior unmanned and tethered evidence per the DDR-001 gate. | REQ-HFPX-VVP-004, DDR-001, MIS-006 | Inspection |
| REQ-HFPX-THM-002 | Human-flight-test personnel, including pilot qualification, currency, and fitness requirements (all TBD), shall be defined per Vol 30 and verified before authorisation. | REQ-HFPX-VVP-004, Vol 30 (TBD) | Inspection |
| REQ-HFPX-THM-003 | Each human flight test shall define controlled conditions (configuration, environment, range, support — all TBD) that bound the test; flight outside defined conditions shall trigger review. | REQ-HFPX-VVP-005, REQ-HFPX-VVP-006 | Demonstration |
| REQ-HFPX-THM-004 | The human-flight-test campaign shall follow an incremental build-up with objectives and sequencing logic (steps and success logic TBD) per flight. | REQ-HFPX-VVP-005, CONOPS (TBD) | Inspection |
| REQ-HFPX-THM-005 | Any qualifying anomaly during the human-flight-test campaign shall invoke a stop rule halting further human flights pending investigation and re-authorisation (triggers, scope TBD). | REQ-HFPX-VVP-004, REQ-HFPX-VVP-006 | Inspection |

All envelopes, thresholds, and criteria are TBD. No values are baselined in this revision.

## 7. Architecture

Organisation (roles TBD): flight-test lead, FRR-type board (membership TBD), pilot/personnel authority (Vol 30), safety/range interface (Vol 25), instrumentation and analysis leads, independent safety verifier reporting via Safety Review Board.
Build-up architecture: authorised flight → objectives TBD → controlled conditions TBD → data capture → analysis → gate/stop-review decision; each flight requires its own authorisation and closure record.
Evidence architecture: prior unmanned/tethered evidence packages are entry inputs; human-flight results feed envelope-expansion and reporting threads only through gate records.

## 8. Detailed Design

Methodology elements only (no execution instructions):
- Authorisation-package framework: prior-evidence list TBD, hazard-control closure TBD, configuration definition TBD, controlled-conditions statement TBD, approval routing TBD.
- Qualification framework: roles requiring qualification TBD, qualification/currency evidence TBD, verification timing TBD (owned by Vol 30).
- Controlled-conditions framework: condition parameters TBD, monitoring approach TBD, deviation classification and response TBD.
- Build-up framework: flight objectives TBD, step ordering TBD, per-flight success logic TBD.
- Stop-rule framework: triggers TBD, halt scope TBD, investigation and re-authorisation gate TBD.
No manoeuvre recipes, piloting instructions, or propulsion-operation sequences are defined in this document.

## 9. Interfaces

- V&V ↔ Vol 22 VCRM: each REQ-HFPX-THM row traces to verification case(s) TBD.
- Human-flight programme ↔ Vol 23.10/23.11/23.12: prior-evidence threads (gate records only).
- Human-flight programme ↔ Vol 30: qualification thread; ↔ Vol 25: authorisation/range-safety thread; ↔ Safety Case/Vol 13/24: hazard-closure thread.
- Human-flight programme ↔ Vol 23.14/23.15/23.16/23.17/23.18: envelope, emergency-procedure, instrumentation, analysis, and reporting threads.

## 10. Operational Concept

Campaign-level flow only: define objectives, build-up, and controlled conditions → verify personnel qualification → assemble prior-evidence and hazard-closure package → seek FRR-type authorisation → conduct authorised testing under range/authority controls → capture data → analyse → gate/stop-review decision.
Test conduct, piloting, vehicle handling, range operations, and emergency response execution belong to authorised procedures and range orders (TBD, Vol 25), not this document.
Progression between flights and to envelope expansion requires gate closure; anomalies invoke the stop rule before any further human flight.

## 11. Safety

Human flight is safety-gated at the highest level: no flight without accepted prior evidence, independent safety verification of catastrophic-hazard closure (criterion TBD), verified personnel qualification, defined controlled conditions, and FRR-type authorisation (all TBD).
Hazard-derived safety requirements flow from Vol 13/24 and Safety Case with independent review to a degree TBD per REQ-HFPX-VVP-006.
Range-safety and certification-credit hooks are TBD per Vol 25; this document claims no range approval and no certification credit.

## 12. Performance

Indicators TBD (no thresholds baselined): authorisation-package completeness, qualification-verification completeness, controlled-conditions compliance record, build-up closure progress, stop-rule review backlog.
Measurement and reporting cadence TBD in Vol 22/23 children.

## 13. Verification & Validation

Each REQ-HFPX-THM row receives a single primary method (A/I/D/T) per REQ-HFPX-VVP-001; per-flight acceptance criteria are TBD per case per REQ-HFPX-VVP-005.
This document is verified by inspection for header, 20-section structure, shall-statements, parent trace, A/I/D/T allocation, TBD discipline, DDR-001 gating with prior-evidence + FRR-type rule, and methodology-only boundary.
Validation is programme-authority review at the applicable gate; certification validation is owned by Vol 25.

## 14. Risks

- FRR-type criteria and prior-evidence scope left TBD, blocking authorisation; mitigation: authorisation-package definition gate with Vol 25 and Safety Case.
- Pressure to fly with incomplete qualification or outside controlled conditions; mitigation: REQ-HFPX-THM-002/003 gates with formal records.
- Anomalies without enforced stop discipline; mitigation: REQ-HFPX-THM-005 stop rule with investigation and re-authorisation gate.

## 15. Open Issues

FRR-type membership, criteria, authority, and evidence scope TBD. Pilot/personnel qualification, currency, and fitness TBD (Vol 30). Controlled-conditions parameters TBD. Build-up steps and success logic TBD. Anomaly triggers, investigation scope, and re-authorisation logic TBD. Range-safety hooks TBD (Vol 25).

## 16. Assumptions

- A-THM-001: Prior unmanned and tethered evidence can be scoped to support a human-flight authorisation claim via explicit gate trace; validation: FRR-type review (method TBC).
- A-THM-002: Qualification and controlled-conditions bounding sufficient for gate decisions can be defined (details TBD); validation: Vol 30 and range-authority review.

## 17. Dependencies

Depends on V&V Plan and VCRM discipline, SEMP gates, Safety Case and Vol 13/24 hazard closure, Vol 25 authorisation/range rules, Vol 30 qualification rules, prior unmanned/tethered/transition evidence, MRQ/MAR/CONOPS parents, and Vol 23.14–23.18 threads.

## 18. Traceability

Parents: REQ-HFPX-VVP-001, REQ-HFPX-VVP-004, REQ-HFPX-VVP-005, REQ-HFPX-VVP-006; DDR-001; MIS-006, MVP-001; Vol 30 (TBD); Vol 25 (TBD); MRQ/MAR (TBD); CONOPS (TBD).
Children: human-flight verification cases and procedures (IDs TBD; VCRM rows TBD).
RTM: REQ-HFPX-THM-001..005 → CONCEPT. No orphans per REQ-HFPX-VVP-002 (to be shown in VCRM).

## 19. Configuration

BL-0.0. Tranche 4 draft, CONCEPT, not baselined. Future changes via change records; any baselined-requirement change re-opens affected VCRM rows until re-verified.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (Vol 23.13 Human Flight Test Programme; methodology/planning only, all values TBD) |
