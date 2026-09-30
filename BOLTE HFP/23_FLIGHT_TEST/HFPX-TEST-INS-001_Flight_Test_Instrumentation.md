# Flight-Test Instrumentation (Vol 23.16)

**Document ID:** HFPX-TEST-INS-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define test-methodology and planning requirements for HFP-X flight-test instrumentation (Chapter 23.16).
Establishes measurand-list discipline, accuracy/sampling discipline, calibration discipline via Vol 09.17, and instrumentation-to-analysis trace discipline.
This document contains planning methodology only; it contains no flight-execution instructions, manoeuvre recipes, or propulsion-operation instructions.

## 2. Scope

Covers flight-test instrumentation planning for tethered, unmanned, transition, human-flight, envelope-expansion, and emergency-test campaigns: what is measured, how well, how calibrated, and how traced to analysis.
Applies to onboard and ground instrumentation supporting Vol 23.10–23.15 evidence claims.
Out of scope: instrumentation detailed design, sensor installation/operation instructions, flight-execution procedures, and certification credit — all TBD elsewhere.
Content is limited to requirements, architecture, interfaces, test methodology and safety analysis; it shall not contain instructions for constructing, igniting, or operating human-carrying high-energy propulsion outside appropriate engineering, test, safety and regulatory controls.

## 3. Applicable Documents

- HFPX-VV-PLN-001 V&V Plan (REQ-HFPX-VVP-001..006)
- HFPX-TEST-IDX-001 Vol 23 index / Test & Evaluation Strategy (TBD)
- HFPX-PGM-SEM-001 SEMP (gated reviews)
- Vol 09.17 calibration rules (TBD); Vol 19 analysis hooks (TBD)
- Vol 25 authorisation / range-safety rules (TBD)
- HFPX-SAFE-CAS-001 Safety Case; Vol 13/24 hazard inputs (TBD)
- Vol 23.10–23.15 test campaigns; Vol 23.17/23.18 analysis and reporting threads

## 4. Definitions & Acronyms

- Measurand: quantity selected for measurement to support a test objective or analysis claim (list TBD per campaign).
- Accuracy / sampling: measurement quality attributes (values TBD per measurand) covering uncertainty, rate, bandwidth, and synchronisation needs.
- Calibration: traceable assurance that instrumentation reads within defined quality (rules TBD per Vol 09.17).
- Instrumentation-to-analysis trace: mapping from each measurand to its consuming analysis or gate claim (mapping TBD).
- A/I/D/T: Analysis / Inspection / Demonstration / Test per HFPX-VV-PLN-001 §4; TBD: unknown data, no values baselined.

## 5. System Context

Instrumentation underpins every gated flight claim: without defined measurands, quality, calibration, and trace, test data cannot support VCRM closure or gate decisions.
Instrumentation planning is campaign-driven: Vol 23.10–23.15 objectives define measurand needs; this volume defines how those needs are captured, assured, and traced — not how flights are executed.
Gated progression per REQ-HFPX-VVP-004 and DDR-001 applies: instrumentation readiness is part of readiness/authorisation packages.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-TIN-001 | Each flight-test campaign shall define its measurand list with rationale and consuming objective or analysis claim (all TBD) per test. | REQ-HFPX-VVP-005, REQ-HFPX-VVP-002 | Inspection |
| REQ-HFPX-TIN-002 | Each measurand shall define accuracy, sampling, synchronisation, and data-quality requirements (all TBD) supporting its consuming analysis. | REQ-HFPX-VVP-005, REQ-HFPX-VVP-001 | Analysis |
| REQ-HFPX-TIN-003 | Flight-test instrumentation shall satisfy calibration rules per Vol 09.17 (intervals, standards, records TBD) before data is claimed as verification evidence. | REQ-HFPX-VVP-004, Vol 09.17 (TBD) | Inspection |
| REQ-HFPX-TIN-004 | Each measurand shall be traced to its consuming analysis method or gate claim (mapping TBD) with no untraced measurands and no unsupported analysis inputs. | REQ-HFPX-VVP-002 | Inspection |

All envelopes, thresholds, accuracies, rates, and criteria are TBD. No values are baselined in this revision.

## 7. Architecture

Organisation (roles TBD): instrumentation lead, calibration authority (Vol 09.17), campaign test leads (Vol 23.10–23.15), analysis lead (Vol 23.17), independent verifier.
Data-chain architecture: measurand need → sensor/channel allocation TBD → recording and time-reference TBD → quality check TBD → calibrated data set → traced analysis input.
Readiness architecture: instrumentation definition, calibration status, and trace completeness are entry inputs to test readiness and FRR-type gates.

## 8. Detailed Design

Methodology elements only (no execution instructions):
- Measurand-capture framework: objective → measurand TBD → rationale TBD → range/condition coverage TBD → priority TBD.
- Quality-definition framework: accuracy TBD, sampling/rate TBD, synchronisation TBD, dropout/handling rules TBD per measurand.
- Calibration framework: standards TBD, intervals TBD, pre/post-test checks TBD, records TBD (owned by Vol 09.17).
- Trace framework: measurand → analysis method TBD → gate claim TBD, with orphan checks per REQ-HFPX-VVP-002.
No sensor installation, operation, flight-execution, or propulsion-operation instructions are defined in this document.

## 9. Interfaces

- V&V ↔ Vol 22 VCRM: each REQ-HFPX-TIN row traces to verification case(s) TBD.
- Instrumentation ↔ Vol 23.10–23.15: measurand-need threads per campaign.
- Instrumentation ↔ Vol 23.17/23.18: analysis-input and reporting threads.
- Instrumentation ↔ Vol 09.17: calibration-rule thread; ↔ Vol 19: analysis-method hooks.
- Instrumentation ↔ Safety (Vol 13/24) and Vol 25: safety-critical measurand and range-instrumentation hooks (all TBD).

## 10. Operational Concept

Planning flow only: derive measurand needs from objectives → define quality and calibration needs → verify trace to analysis → confirm readiness → support authorised testing under range controls → deliver quality-flagged data sets to analysis.
Instrument operation, installation, handling, and test conduct belong to authorised procedures (TBD), not this document.
Data gaps or calibration lapses trigger review before evidence claims.

## 11. Safety

Safety-critical measurands supporting hazard-closure or gate claims require defined quality and calibration status (both TBD) before evidence is credited, with independent review to a degree TBD per REQ-HFPX-VVP-006.
Instrumentation failures or data gaps affecting safety claims invoke review and gate hold.
Range-safety hooks TBD per Vol 25; no range approval or certification credit claimed here.

## 12. Performance

Indicators TBD (no thresholds baselined): measurand-definition completeness, quality-definition completeness, calibration currency, trace coverage, data-capture completeness per test.
Measurement and reporting cadence TBD in Vol 22/23 children.

## 13. Verification & Validation

Each REQ-HFPX-TIN row receives a single primary method (A/I/D/T) per REQ-HFPX-VVP-001; per-measurand acceptance values are TBD per case per REQ-HFPX-VVP-005.
This document is verified by inspection for header, 20-section structure, shall-statements, parent trace (including Vol 09.17), A/I/D/T allocation, TBD discipline, gated-readiness rule, and methodology-only boundary.
Validation is programme-authority review at the applicable gate; certification validation is owned by Vol 25.

## 14. Risks

- Measurand lists or quality attributes left TBD, producing unusable data; mitigation: measurand-definition gate per campaign.
- Calibration lapses invalidating evidence; mitigation: REQ-HFPX-TIN-003 calibration gate with Vol 09.17 records.
- Untraced measurands or unsupported analysis inputs; mitigation: REQ-HFPX-TIN-004 / REQ-HFPX-VVP-002 orphan checks.

## 15. Open Issues

Measurand lists TBD per campaign. Accuracy, sampling, synchronisation, and quality rules TBD per measurand. Calibration intervals, standards, and records TBD (Vol 09.17). Trace mapping to analysis/gate claims TBD. Safety-critical measurand set TBD.

## 16. Assumptions

- A-TIN-001: Campaign objectives can be decomposed into measurand needs sufficiently to support analysis claims (method TBD); validation: analysis-lead review.
- A-TIN-002: Calibration infrastructure per Vol 09.17 will exist to support flight-test currency (details TBD); validation: calibration-authority review.

## 17. Dependencies

Depends on V&V Plan and VCRM discipline, Vol 23.10–23.15 objective definitions, Vol 09.17 calibration capability, Vol 19/23.17 analysis capability, Safety inputs for critical measurands, and Vol 25 range hooks.

## 18. Traceability

Parents: REQ-HFPX-VVP-001, REQ-HFPX-VVP-002, REQ-HFPX-VVP-004, REQ-HFPX-VVP-005; Vol 09.17 (TBD); Vol 19 (TBD).
Children: instrumentation verification cases and channel allocations (IDs TBD; VCRM rows TBD).
RTM: REQ-HFPX-TIN-001..004 → CONCEPT. No orphans per REQ-HFPX-VVP-002 (to be shown in VCRM).

## 19. Configuration

BL-0.0. Tranche 4 draft, CONCEPT, not baselined. Future changes via change records; any baselined-requirement change re-opens affected VCRM rows until re-verified.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (Vol 23.16 Flight-Test Instrumentation; methodology/planning only, all values TBD) |
