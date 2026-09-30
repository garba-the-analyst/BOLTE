# Fire Protection

**Document ID:** HFPX-SAFE-FIR-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X fire-protection direction (Chapter 13.15): how fire zones, detection, isolation/suppression, and post-fire safe-state requirements will be established and verified.
Sets requirements, architecture, and verification direction only; it contains no propulsion build, ignition, or operation instructions.

## 2. Scope

Covers fire-zone definition, fire detection functions, fire isolation/suppression functions, and post-fire safe-state behaviour for all applicable vehicle zones (zones TBD, with Vol 05/14 inputs).
In scope: fire functional requirements, architectural allocation direction, interface requirements, and test-methodology direction.
Out of scope: propulsion detailed design (Vol 05), thermal detailed design (Vol 14), suppression-agent implementation selection, and any build or handling instructions.

## 3. Applicable Documents

- Programme Charter STK-001; SyRS SYS-002/003; safety tier SAF-001..006, parent SCA-006 (all stubs, values TBD)
- HFPX-SAFE-CAS-001 Safety Case; HFPX-SAFE-FHA-001 Functional Hazard Assessment (engine/propulsion rows); hazard log (`13_SAFETY_RECOVERY/hazard_log.csv`)
- Vol 05 propulsion architecture; Vol 14 thermal design; HFPX-VV-PLN-001 V&V Plan
- Standards (structured according to): SAE ARP4754A, ARP4761/4761A concepts — no compliance claimed in this revision

## 4. Definitions & Acronyms

- Fire zone: bounded region within which fire hazards are assessed and protection functions allocated, boundaries TBD pending Vol 05/14 inputs
- Detection: function that determines a fire condition exists, means and thresholds TBD
- Isolation / suppression: functions that limit fire spread, remove energy/fuel, or extinguish fire effects, means TBD
- Post-fire safe-state: defined vehicle state after a fire event or protection actuation, conditions TBD
- FHA engine/propulsion rows: functional-hazard entries covering engine/propulsion fire functions, IDs TBD

## 5. System Context

Fire is a governing catastrophic-hazard class for HFP-X (coverage required by SCA-006); fire protection constrains propulsion, thermal, power, and recovery architectures.
Zone definitions depend on Vol 05 (propulsion layout) and Vol 14 (thermal layout) inputs, both TBD; no zone boundaries are baselined in this revision.
Detection, isolation/suppression, and safe-state functions depend on power, sensing, and control availability whose budgets and independence are TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-FIR-001 | The programme shall define fire zones, with boundaries and hazard allocation TBD (Vol 05/14 inputs). | SCA-006, FHA engine/propulsion rows | Inspection |
| REQ-HFPX-FIR-002 | The system shall provide fire-detection functions for each defined fire zone, with means, coverage, and thresholds TBD. | SCA-006, FHA engine/propulsion rows | Demonstration |
| REQ-HFPX-FIR-003 | The system shall provide fire isolation/suppression functions for each defined fire zone, with means, allocation, and effectiveness criteria TBD. | SCA-006, FHA engine/propulsion rows | Demonstration |
| REQ-HFPX-FIR-004 | The system shall achieve a defined post-fire safe-state following a fire event or protection actuation, with state definition and entry criteria TBD. | SCA-006, FHA engine/propulsion rows | Analysis |

All detection thresholds, suppression quantities, timings, and safe-state parameters: TBD. No fire-protection effectiveness is asserted until demonstrated through gated verification.

## 7. Architecture

Fire-protection allocation TBD across zones, sensors, isolation/suppression effectors, safety computer/logic, power, and crew/ground annunciation; SAD to allocate.
Detection and isolation/suppression are architecturally identified as separate function segments with independence from primary control to a degree TBD.
Post-fire safe-state is architecturally identified as a mode transition owned jointly with Vol 11 operations and the safety path (allocation TBD).
> Hazardous-subsystem boundary: architecture here addresses functional allocation and interfaces only; it contains no build, ignition, or operation instructions.

## 8. Detailed Design

No detailed design in this revision — zones, means, and thresholds TBD.
Design direction (methodology only): per-zone decomposition into detection → annunciation → isolation/suppression → safe-state entry, each with requirements, interfaces, and verification cases TBD.
Zone-definition methodology TBD: Vol 05/14 layout inputs, hazard allocation per FHA rows, and boundary review criteria to be defined before any zone claim.

## 9. Interfaces

- Fire ↔ Propulsion (Vol 05): zone geometry, energy/fuel isolation points, details TBD
- Fire ↔ Thermal (Vol 14): temperature sensing, thermal isolation, details TBD
- Fire ↔ Power (Vol 15): detection and actuation power, independence, details TBD
- Fire ↔ Operations / Safety computer (Vol 11 / safety path): annunciation, safe-state entry, crew/ground authority, details TBD
- Fire ↔ V&V (Vol 22–24): fire verification cases and test-methodology hooks, IDs TBD

## 10. Operational Concept

Test methodology and gating only: this concept defines readiness evidence and mode-transition logic structure, not vehicle handling, ignition sequencing, or flight conduct.
Lifecycle direction: zone definition → analysis (FHA/FMEA as applicable) → ground demonstration of detection and isolation/suppression logic → safe-state demonstration at a fidelity TBD → Safety Review Board assessment.
No operational fire procedure is authorised in this revision; procedures and authority delegation are TBD and gated by FRR.

## 11. Safety

Fire-hazard coverage is required (SCA-006) and traced to FHA engine/propulsion rows; coverage completeness is TBD pending zone definition.
No compliance claimed in this revision; no suppression effectiveness or safe-state achievability is asserted until verified.
Fire protection shall not take credit for retiring catastrophic hazards until mitigations are verified and retired by the Safety Review Board (criteria TBD).
> Hazardous-subsystem boundary: this section states safety-analysis and gating rules only.

## 12. Performance

Fire performance indicators and thresholds TBD (no values baselined): detection coverage and latency TBD, isolation/suppression effectiveness TBD, false-alarm behaviour TBD, post-fire safe-state entry criteria TBD.
No numerical targets are set in this revision; scales and acceptance criteria TBD in later revisions with Vol 13/24 concurrence.

## 13. Verification & Validation

Verification direction: REQ-HFPX-FIR-001 by inspection (zone definitions reviewed against Vol 05/14 inputs and FHA coverage); REQ-HFPX-FIR-002..003 by demonstration (detection and isolation/suppression logic demonstrated at a fidelity TBD); REQ-HFPX-FIR-004 by analysis (safe-state reachability and transition analysis, means TBD).
Acceptance criteria TBD per case; evidence recorded as TBD/empty until closed.
Validation by Safety Review Board plus programme-authority approval at gates; certification validation owned by Vol 25 with no claims here.

## 14. Risks

- Zone-definition debt: Vol 05/14 inputs late or unstable, blocking FHA/FMEA allocation; mitigation: zone-definition owner and due gate TBD with open-zone status enforced at reviews
- Detection gap: undetected or late-detected fire in an undefined zone; mitigation: coverage analysis required before any zone-closure claim (method TBD)
- Suppression shortfall: isolation/suppression ineffective against actual energy release (values TBD); mitigation: no effectiveness claimed until demonstrated; analysis bounds TBD

## 15. Open Issues

Fire-zone boundaries undefined (Vol 05/14 inputs TBD). Detection means, coverage, and thresholds undefined. Isolation/suppression means and effectiveness criteria undefined. Post-fire safe-state undefined. FHA engine/propulsion row IDs TBD. All fire evidence TBD/empty.

## 16. Assumptions

- Fire zones can be bounded from Vol 05/14 layouts once available; validation: Vol 05/14 inputs and Vol 13 analysis (both TBD)
- Detection plus isolation/suppression plus safe-state entry is architecturally feasible within mass/power budgets TBD; validation: SAD allocation (TBD)
- Ground demonstration can verify detection and isolation/suppression logic without live-fire qualification in early gates; validation: Vol 23 test methodology (TBD)

## 17. Dependencies

Depends on STK-001/SYS-002/003/SAF tier and SCA-006 (requirements basis), FHA engine/propulsion rows (hazard basis), Vol 05/14 (zone inputs), SEMP (gates), V&V Plan (verification discipline), Vol 19 (modelling), Vol 22–24 (VCRM and verification), Vol 25 (certification basis).

## 18. Traceability

Parents: SCA-006, FHA engine/propulsion rows (row IDs TBD).
Children: per-zone detection, isolation/suppression, and safe-state requirements and verification cases (artefact IDs TBD).
RTM: REQ-HFPX-FIR-001..004 → CONCEPT. Each fire zone traces to hazards → requirements → VCRM cases → evidence (all TBD except schema).

## 19. Configuration

BL-0.0. Tranche 4 draft, CONCEPT, not baselined. Zone-definition change, means selection, or safe-state change requires a change record with affected-requirement and hazard impact stated.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (fire-protection direction; zones TBD) |
