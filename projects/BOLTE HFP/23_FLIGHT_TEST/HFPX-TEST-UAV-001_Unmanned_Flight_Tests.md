# Unmanned Flight Tests (Vol 23.11)

**Document ID:** HFPX-TEST-UAV-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define test-methodology and planning requirements for HFP-X unmanned flight tests (Chapter 23.11).
Establishes demonstration threads for hover/transition/cruise objectives, authorisation discipline, data-capture discipline, envelope-limit discipline, and mishap-investigation discipline.
This document contains planning methodology only; it contains no flight-execution instructions, manoeuvre recipes, or propulsion-operation instructions.

## 2. Scope

Covers unmanned flight-test planning: demonstration objectives traced to MRQ-001..003, range/authorisation needs, data-capture needs, envelope-limit definition, and mishap/anomaly handling.
Applies within the gated chain before any tethered-human or human-flight consideration.
Out of scope: flight-execution procedures, vehicle handling, manoeuvre definitions, propulsion build/ignition/operation, detailed range orders, and certification credit — all TBD in owning volumes/authorities.
Content is limited to requirements, architecture, interfaces, test methodology and safety analysis; it shall not contain instructions for constructing, igniting, or operating human-carrying high-energy propulsion outside appropriate engineering, test, safety and regulatory controls.

## 3. Applicable Documents

- HFPX-VV-PLN-001 V&V Plan (REQ-HFPX-VVP-001..006)
- HFPX-TEST-IDX-001 Vol 23 index / Test & Evaluation Strategy (TBD)
- HFPX-PGM-SEM-001 SEMP (gated reviews)
- HFPX-SAFE-CAS-001 Safety Case; Vol 13/24 hazard inputs (TBD)
- Vol 25 authorisation / range-safety / certification-credit rules (TBD)
- MRQ-001..003 mission-requirement threads; MAR threads (TBD); CONOPS threads (TBD)
- DDR-001 gated-progression decision; MIS-006 / MVP-001 gating (TBD)
- Vol 23.16 instrumentation, Vol 23.17 data analysis, Vol 23.18 reporting (TBD hooks)

## 4. Definitions & Acronyms

- Unmanned flight test: flight-test configuration without human onboard, executed under authorised range conditions to generate verification evidence.
- MRQ-001..003: mission-requirement threads for hover, transition, and cruise demonstration (details TBD in owning volume).
- Mishap: unplanned event causing damage, injury, envelope exceedance, or loss of control (thresholds TBD); anomaly: unexpected behaviour requiring review (criteria TBD).
- A/I/D/T: Analysis / Inspection / Demonstration / Test per HFPX-VV-PLN-001 §4.
- TBD / TBC: unknown data; no values baselined.

## 5. System Context

Unmanned flight tests provide the foundational flight evidence for the gated chain: sim → SIL → HIL → subsystem → integrated propulsion → unmanned → tethered → controlled human flight → envelope expansion.
Unmanned results feed tethered-entry claims (Vol 23.10), transition claims (Vol 23.12), emergency-procedure claims (Vol 23.15), and any future human-flight consideration (Vol 23.13) strictly through traced gate records; gates shall not be skipped per REQ-HFPX-VVP-004 and DDR-001.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-TUV-001 | The unmanned flight-test campaign shall demonstrate hover, transition, and cruise objectives (scope and success criteria TBD) traced to MRQ-001..003. | MRQ-001, MRQ-002, MRQ-003, REQ-HFPX-VVP-005 | Test |
| REQ-HFPX-TUV-002 | Unmanned flights shall not commence without applicable range and flight authorisation (authority, conditions TBD) per Vol 25. | REQ-HFPX-VVP-004, Vol 25 (TBD) | Inspection |
| REQ-HFPX-TUV-003 | The campaign shall define and capture the required flight-test data set (measurands, recording, retention hooks — all TBD) per test via Vol 23.16/23.17 threads. | REQ-HFPX-VVP-005, REQ-HFPX-VVP-002 | Inspection |
| REQ-HFPX-TUV-004 | Each unmanned test shall define envelope limits and exceedance-response actions (all TBD); exceedance shall trigger review and gate hold before further flights. | REQ-HFPX-VVP-004, REQ-HFPX-VVP-006 | Test |
| REQ-HFPX-TUV-005 | Any mishap or qualifying anomaly shall trigger a defined investigation and gate-hold process (membership, scope, re-entry criteria TBD) before test resumption. | REQ-HFPX-VVP-004, REQ-HFPX-VVP-006 | Inspection |

All envelopes, thresholds, and criteria are TBD. No values are baselined in this revision.

## 7. Architecture

Organisation (roles TBD): flight-test lead, range/authorisation interface, safety verifier, instrumentation and analysis leads, configuration authority.
Test-article logic: unmanned configuration(s) with representativeness claim TBD per test relative to downstream claims.
Gate structure: readiness review / FRR-type gate TBD → authorised unmanned-test window(s) → data review → mishap/anomaly review where triggered → gate recommendation; no gate skipping.

## 8. Detailed Design

Methodology elements only (no execution instructions):
- Objective decomposition: MRQ-001..003 → unmanned objectives → per-test success criteria TBD → measurands → analysis methods.
- Authorisation package framework: configuration definition, hazard controls, envelope limits TBD, data plan, and approval routing TBD.
- Data-plan framework: required data set TBD per test, recording and quality checks TBD, trace to analysis threads.
- Envelope-limit framework: limit parameters TBD per test, monitoring approach TBD, exceedance classification and response TBD.
- Mishap-investigation framework: reporting triggers TBD, evidence preservation TBD, investigation scope and re-entry gate TBD.
No manoeuvre recipes, handling instructions, or propulsion-operation sequences are defined in this document.

## 9. Interfaces

- V&V ↔ Vol 22 VCRM: each REQ-HFPX-TUV row traces to verification case(s) TBD.
- Unmanned tests ↔ MRQ/MAR and CONOPS threads: demonstration trace.
- Unmanned tests ↔ Vol 23.10/23.12/23.13: forward evidence feed (gate records only).
- Unmanned tests ↔ Vol 23.16/23.17/23.18: instrumentation, analysis, and reporting threads.
- Unmanned tests ↔ Safety (Vol 13/24) and Vol 25: hazard controls, range-safety, and authorisation threads (all TBD).

## 10. Operational Concept

Campaign-level flow only: plan objectives and criteria → define configuration, envelope, and data needs → assemble readiness/authorisation package → seek authorisation → conduct authorised testing under range controls → capture data → analyse → gate/anomaly review.
Test conduct, vehicle handling, range operations, and emergency response execution belong to authorised procedures and range orders (TBD, Vol 25), not this document.
Anomalies and exceedances invoke stop/review per REQ-HFPX-TUV-004/005 before any progression.

## 11. Safety

Unmanned testing is safety-gated: no flights without authorisation and closed readiness criteria (both TBD).
Hazard-derived safety requirements flow from Vol 13/24; safety verification is independent to a degree TBD per REQ-HFPX-VVP-006.
Range-safety hooks and certification-credit rules are TBD per Vol 25; this document claims no range approval and no certification credit.
Envelope exceedance and mishap rules bound testing within TBD conditions pending review.

## 12. Performance

Indicators TBD (no thresholds baselined): objective-closure progress, data-capture completeness, envelope-compliance record, anomaly/mishap review backlog.
Measurement and reporting cadence TBD in Vol 22/23 children.

## 13. Verification & Validation

Each REQ-HFPX-TUV row receives a single primary method (A/I/D/T) per REQ-HFPX-VVP-001; per-test acceptance criteria are TBD per case per REQ-HFPX-VVP-005.
This document is verified by inspection for header, 20-section structure, shall-statements, parent trace (including MRQ-001..003), A/I/D/T allocation, TBD discipline, gated-progression rule, and methodology-only boundary.
Validation is programme-authority review at the applicable gate; certification validation is owned by Vol 25.

## 14. Risks

- MRQ demonstration scope left TBD, blocking objective decomposition; mitigation: traced objective-definition gate with owning volume TBD.
- Pressure to fly without range/authorisation closure; mitigation: REQ-HFPX-TUV-002 gate with formal records.
- Data gaps or envelope exceedances without defined response; mitigation: REQ-HFPX-TUV-003/004/005 data, limit, and investigation discipline.

## 15. Open Issues

Demonstration scope and success criteria for MRQ-001..003 TBD. Range authority, conditions, and FRR-type criteria TBD (Vol 25). Data set, recording, and retention details TBD. Envelope-limit parameters and exceedance logic TBD. Mishap/anomaly thresholds, investigation membership, and re-entry criteria TBD.

## 16. Assumptions

- A-TUV-001: Unmanned configurations can be shown representative for their verification claims via a representativeness argument TBD per test; validation: independent review.
- A-TUV-002: Range and authorisation processes sufficient to bound unmanned testing will exist (details TBD); validation: Vol 25 review.

## 17. Dependencies

Depends on V&V Plan and VCRM discipline, SEMP gates, Safety Case and Vol 13/24 inputs, MRQ/MAR/CONOPS parent threads, Vol 25 authorisation/range rules, prior sim/SIL/HIL and ground-test evidence, and Vol 23.16/23.17/23.18 capability.

## 18. Traceability

Parents: REQ-HFPX-VVP-001, REQ-HFPX-VVP-002, REQ-HFPX-VVP-004, REQ-HFPX-VVP-005, REQ-HFPX-VVP-006; MRQ-001, MRQ-002, MRQ-003; DDR-001; MIS-006; CONOPS (TBD); Vol 25 (TBD).
Children: unmanned verification cases and procedures (IDs TBD; VCRM rows TBD).
RTM: REQ-HFPX-TUV-001..005 → CONCEPT. No orphans per REQ-HFPX-VVP-002 (to be shown in VCRM).

## 19. Configuration

BL-0.0. Tranche 4 draft, CONCEPT, not baselined. Future changes via change records; any baselined-requirement change re-opens affected VCRM rows until re-verified.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (Vol 23.11 Unmanned Flight Tests; methodology/planning only, all values TBD) |
