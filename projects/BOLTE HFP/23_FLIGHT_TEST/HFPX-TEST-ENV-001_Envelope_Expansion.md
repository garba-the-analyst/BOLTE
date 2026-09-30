# Envelope Expansion (Vol 23.14)

**Document ID:** HFPX-TEST-ENV-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define test-methodology and planning requirements for HFP-X envelope expansion (Chapter 23.14).
Establishes expansion-step discipline, per-step exit-criteria discipline, rollback discipline on exceedance, and envelope-documentation discipline.
This document contains planning methodology only; it contains no flight-execution instructions, manoeuvre recipes, or propulsion-operation instructions.

## 2. Scope

Covers envelope-expansion planning: definition of expansion steps (parameters TBD), exit criteria per step, rollback and review logic, and envelope documentation.
Applies to unmanned and (only where separately authorised) human-flight-test stages; each step is gated and no step grants open-envelope operation.
Out of scope: flight-execution procedures, manoeuvre recipes, propulsion operation, and certification of any envelope — all TBD elsewhere.
Content is limited to requirements, architecture, interfaces, test methodology and safety analysis; it shall not contain instructions for constructing, igniting, or operating human-carrying high-energy propulsion outside appropriate engineering, test, safety and regulatory controls.

## 3. Applicable Documents

- HFPX-VV-PLN-001 V&V Plan (REQ-HFPX-VVP-001..006)
- HFPX-TEST-IDX-001 Vol 23 index / Test & Evaluation Strategy (TBD)
- HFPX-PGM-SEM-001 SEMP (gated reviews)
- HFPX-SAFE-CAS-001 Safety Case; Vol 13/24 hazard inputs (TBD)
- Vol 25 authorisation / range-safety rules (TBD)
- MRQ/MAR envelope threads; CONOPS threads (all TBD)
- DDR-001 gated-progression decision; MIS-006 / MVP-001 gating (TBD)
- Vol 23.10–23.13 prior evidence; Vol 23.16/23.17/23.18 threads

## 4. Definitions & Acronyms

- Envelope: bounded set of tested conditions and configurations with supporting evidence (parameters TBD).
- Expansion step: planned increment from the cleared envelope toward new conditions (increments TBD), requiring authorisation and exit-criteria closure.
- Exit criteria: evidence and analysis required to clear a step (criteria TBD).
- Rollback: return to the last cleared envelope and defined review/re-entry logic on exceedance or anomaly (logic TBD).
- A/I/D/T: Analysis / Inspection / Demonstration / Test per HFPX-VV-PLN-001 §4; TBD: unknown data, no values baselined.

## 5. System Context

Envelope expansion sits downstream of demonstrated baseline conditions in the gated chain and proceeds one authorised step at a time.
Each step requires prior-step closure, hazard-control coverage for the proposed increment, and FRR-type/range authorisation where applicable (criteria TBD).
Gates shall not be skipped per REQ-HFPX-VVP-004 and DDR-001; human-flight envelope steps additionally require the Vol 23.13 authorisation chain.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-TEV-001 | The envelope-expansion campaign shall define ordered expansion steps with objectives and sequencing logic (parameters and increments TBD) per stage. | REQ-HFPX-VVP-005, MRQ/MAR (TBD) | Inspection |
| REQ-HFPX-TEV-002 | Each expansion step shall define exit criteria (evidence, analysis, and review scope TBD) that shall be closed before the next step is authorised. | REQ-HFPX-VVP-004, REQ-HFPX-VVP-005 | Inspection |
| REQ-HFPX-TEV-003 | Any envelope exceedance or qualifying anomaly shall trigger rollback to the last cleared envelope and defined review and re-entry logic (all TBD). | REQ-HFPX-VVP-004, REQ-HFPX-VVP-006 | Demonstration |
| REQ-HFPX-TEV-004 | The programme shall document the cleared envelope, supporting evidence, and limitations (format and content TBD) after each cleared step, with trace to test reports and the VCRM. | REQ-HFPX-VVP-002, REQ-HFPX-VVP-005 | Inspection |

All envelopes, thresholds, increments, and criteria are TBD. No values are baselined in this revision.

## 7. Architecture

Organisation (roles TBD): flight-test lead, envelope owner (TBD volume), safety/range interface, analysis lead, independent verifier.
Step architecture: cleared envelope → proposed increment TBD → readiness/authorisation → authorised test point(s) → data and analysis → exit-criteria review → cleared-envelope update or rollback.
Evidence architecture: per-step packages feed the envelope record and VCRM; exceedances branch to rollback/review records.

## 8. Detailed Design

Methodology elements only (no execution instructions):
- Step-definition framework: envelope parameters TBD, increment rationale TBD, configuration and conditions TBD, hazard-coverage check TBD.
- Exit-criteria framework: required evidence TBD, analysis methods TBD (via Vol 23.17), review membership TBD, closure recording TBD.
- Rollback framework: exceedance/anomaly classification TBD, rollback scope TBD, investigation TBD, re-entry gate TBD.
- Documentation framework: envelope-record contents TBD, evidence trace TBD, limitation statements TBD.
No manoeuvre recipes, handling instructions, or propulsion-operation sequences are defined in this document.

## 9. Interfaces

- V&V ↔ Vol 22 VCRM: each REQ-HFPX-TEV row traces to verification case(s) TBD.
- Envelope expansion ↔ MRQ/MAR and CONOPS threads: envelope-requirement trace.
- Envelope expansion ↔ Vol 23.10–23.13: prior-evidence and authorisation threads (including DDR-001 gate for human stages).
- Envelope expansion ↔ Vol 23.16/23.17/23.18: instrumentation, analysis, and reporting threads.
- Envelope expansion ↔ Safety (Vol 13/24) and Vol 25: hazard controls, range-safety, authorisation threads (all TBD).

## 10. Operational Concept

Campaign-level flow only: document cleared envelope → propose next increment with rationale → verify hazard coverage and readiness → seek authorisation → conduct authorised testing under range controls → capture and analyse data → exit-criteria review → update envelope record or invoke rollback.
Test conduct, vehicle handling, range operations, and recovery execution belong to authorised procedures and range orders (TBD, Vol 25), not this document.

## 11. Safety

Expansion is safety-gated: no step without closed prior-step criteria, hazard-control coverage for the increment, and applicable authorisation (all TBD).
Exceedances invoke rollback and review per REQ-HFPX-TEV-003; further expansion is held pending re-entry approval.
Hazard-derived safety requirements flow from Vol 13/24 with independent review to a degree TBD; range-safety hooks TBD per Vol 25; no range approval or certification credit claimed here.

## 12. Performance

Indicators TBD (no thresholds baselined): step-definition completeness, exit-criteria closure progress, rollback/review backlog, envelope-record currency.
Measurement and reporting cadence TBD in Vol 22/23 children.

## 13. Verification & Validation

Each REQ-HFPX-TEV row receives a single primary method (A/I/D/T) per REQ-HFPX-VVP-001; per-step acceptance criteria are TBD per case per REQ-HFPX-VVP-005.
This document is verified by inspection for header, 20-section structure, shall-statements, parent trace, A/I/D/T allocation, TBD discipline, gated-progression rule, and methodology-only boundary.
Validation is programme-authority review at the applicable gate; certification validation is owned by Vol 25.

## 14. Risks

- Expansion increments and exit criteria left TBD, blocking readiness; mitigation: per-step definition gate.
- Pressure to skip steps or fly outside the cleared envelope; mitigation: REQ-HFPX-TEV-002/003 no-skipping and rollback rules with formal records.
- Envelope records drifting from evidence; mitigation: REQ-HFPX-TEV-004 documentation and VCRM trace discipline.

## 15. Open Issues

Envelope parameters, increments, and sequencing TBD. Per-step exit criteria and review membership TBD. Exceedance classification, rollback scope, and re-entry logic TBD. Envelope-record format and ownership TBD. Range/authorisation hooks TBD (Vol 25).

## 16. Assumptions

- A-TEV-001: A cleared envelope can be bounded and documented sufficiently to support step decisions (format TBD); validation: envelope-owner review.
- A-TEV-002: Analysis capability sufficient to assess step evidence exists (methods TBD); validation: Vol 19/23.17 review.

## 17. Dependencies

Depends on V&V Plan and VCRM discipline, SEMP gates, MRQ/MAR/CONOPS envelope parents, prior flight evidence (Vol 23.10–23.13), Safety and Vol 25 inputs, and Vol 23.16/23.17/23.18 capability.

## 18. Traceability

Parents: REQ-HFPX-VVP-001, REQ-HFPX-VVP-002, REQ-HFPX-VVP-004, REQ-HFPX-VVP-005, REQ-HFPX-VVP-006; MRQ/MAR (TBD); DDR-001; MIS-006; CONOPS (TBD); Vol 25 (TBD).
Children: envelope-expansion verification cases and procedures (IDs TBD; VCRM rows TBD).
RTM: REQ-HFPX-TEV-001..004 → CONCEPT. No orphans per REQ-HFPX-VVP-002 (to be shown in VCRM).

## 19. Configuration

BL-0.0. Tranche 4 draft, CONCEPT, not baselined. Future changes via change records; any baselined-requirement change re-opens affected VCRM rows until re-verified.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (Vol 23.14 Envelope Expansion; methodology/planning only, all values TBD) |
