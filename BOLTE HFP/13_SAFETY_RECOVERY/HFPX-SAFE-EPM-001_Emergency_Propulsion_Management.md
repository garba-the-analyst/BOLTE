# Emergency Propulsion Management

**Document ID:** HFPX-SAFE-EPM-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define HFP-X emergency propulsion management requirements (Vol 13.9): fault-response ownership, thrust-reallocation versus shutdown criteria, emergency power-to-propulsion interface needs, and demonstration gating.
This document owns analysis, requirements, architecture, interfaces, and test methodology only.

## 2. Scope

Covers detection via health monitoring, response via the safety path, reallocation/shutdown decision criteria (all values TBD), and the interface by which emergency power supports propulsion response.
Hover/low-altitude is the limiting case for response effectiveness (quantification TBD).
Out of scope: propulsion detailed design (Vol 04), primary FCS laws (Vol 06/07), power-system implementation (Vol 05/13.16), and test execution (Vol 23).

## 3. Applicable Documents

- SYS-003 (system requirements basis — stub, values TBD)
- FHA/FMEA EPM hooks (Vol 13.4/13.5 — fault taxonomy and effects, values TBD)
- Health-monitoring definitions (Vol 07/10 as applicable, thresholds TBD)
- HFPX-SAFE-CAS-001 Safety Case; HFPX-VV-PLN-001 V&V Plan; HFPX-PGM-SEM-001 SEMP (gating)

## 4. Definitions & Acronyms

- Emergency propulsion management (EPM): safety-path response to a propulsion fault, distinct from nominal thrust control; scope and authority TBD.
- Health monitoring: detection function that declares propulsion faults; detection thresholds, latencies, and coverage TBD.
- Thrust reallocation: redistribution of thrust demand across remaining effectors; capability and limits TBD, mechanism unselected.
- Shutdown: intentional cessation of thrust from a faulted unit; criteria and sequencing TBD.
- Emergency power-to-propulsion interface: power and signal coupling that sustains the EPM response; capacity and duration TBD.

## 5. System Context

EPM is the propulsion branch of the independent safety path: health monitoring detects, the safety path responds, emergency power sustains the response where allocated (all TBD).
It constrains propulsion and power architecture without implementing them; allocation decisions flow to Vol 04/05 via SAD.
Recovery effectiveness is unproven (ISS-008); no EPM response is credited with achieving a safe state or successful recovery in this revision.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-EPM-001 | The system shall assign propulsion-fault response ownership such that faults are detected via health monitoring and responded to via the safety path, with detection coverage, latencies, and authority TBD. | SYS-003 | Analysis |
| REQ-HFPX-EPM-002 | The system shall define thrust-reallocation versus shutdown criteria, with all thresholds, conditions, and sequencing TBD. | SYS-003, FHA/FMEA hooks | Analysis |
| REQ-HFPX-EPM-003 | The system shall define the emergency power-to-propulsion interface sustaining the EPM response, with capacity, duration, and signal protocols TBD. | SYS-003 | Inspection |
| REQ-HFPX-EPM-004 | The EPM response shall be demonstrated unmanned before any human-flight credit is claimed, with demonstration scope and pass criteria TBD. | SYS-003 | Demonstration |

## 7. Architecture

EPM architecture (details TBD): health-monitoring source(s), safety-path decision function, actuation routing to propulsion effectors, and emergency-power coupling.
Segregation TBD: functional and physical separation of the EPM path from primary propulsion control (sensing, compute, power, actuation separation TBD; SAD to allocate).
Ownership TBD: which volume owns detection tuning versus response logic versus power provisioning.

## 8. Detailed Design

Decision logic is a stub in this revision (reallocation/shutdown criteria TBD, no thresholds baselined).
Methodology only: FHA/FMEA fault taxonomy → response option (reallocate/shutdown) → power/interface demand → VCRM case; completeness criteria TBD.
No control laws, power sizing, or effector selections are made in this revision.

## 9. Interfaces

- EPM ↔ Health monitoring (Vol 07/10): fault declarations in, with message content, latency, and integrity TBD.
- EPM ↔ Propulsion (Vol 04): thrust commands and shutdown signals out; effector interfaces and authority limits TBD.
- EPM ↔ Emergency power (Vol 05/13.16): power and status exchange sustaining the response; capacity/duration TBD.
- EPM ↔ Procedures/alerts (Vol 13.8, Vol 10): EPM state annunciation and crew/operator visibility TBD.

## 10. Operational Concept

Fault-response sequence (methodology only): monitor → declare fault (criteria TBD) → select reallocate or shutdown (criteria TBD) → sustain via emergency power (duration TBD) → transfer to stabilisation/recovery/landing thread (effectiveness TBD).
This concept defines response allocation and gating only; it does not direct ignition sequencing, vehicle handling, or flight conduct (owned and gated under Vol 23/CONOPS).
Hover-first emphasis: EPM threads applicable in hover/low-altitude are analysed and demonstrated first (scope TBD).

## 11. Safety

Hazardous-subsystem boundary: this document contains analysis, requirements, architecture, interfaces, and test methodology only; it contains no instructions for constructing, igniting, or operating high-energy propulsion, and prescribes no build/ignition/operation sequence.
FHA/FMEA hooks govern EPM completeness: every propulsion fault class with safety effect TBD shall trace to an EPM response option or a justified exclusion (criteria TBD).
Recovery effectiveness is unproven (ISS-008): EPM responses assert no safe-state or recovery outcome until demonstrated unmanned per REQ-HFPX-EPM-004 (criteria TBD).
Hover/low-altitude is the limiting case for EPM validation.

## 12. Performance

EPM performance measures TBD with no thresholds baselined: detection latency TBD, response-selection latency TBD, reallocated-thrust adequacy TBD, emergency-power sustain duration TBD.
All timings, loads, and capacities TBD; no numerical performance requirement is set in this revision.

## 13. Verification & Validation

- REQ-HFPX-EPM-001 verified by Analysis of detection-to-response ownership and coverage (criteria TBD).
- REQ-HFPX-EPM-002 verified by Analysis of reallocation/shutdown criteria against FHA/FMEA hooks (completeness TBD).
- REQ-HFPX-EPM-003 verified by Inspection of the interface definition (criteria TBD).
- REQ-HFPX-EPM-004 verified by Demonstration unmanned (SIL/HIL/rig/flight-test mix TBD); human-flight credit is gated on closure plus Safety Review Board concurrence (criteria TBD).
- Validation is gate review plus safety-board approval; certification credit owned by Vol 25 (none claimed here).

## 14. Risks

- Detection gap: health monitoring misses or delays a fault the response assumes caught; mitigation: coverage analysis against FMEA, thresholds TBD.
- Wrong-branch selection (reallocate versus shutdown) under uncertainty; mitigation: criteria analysis plus fault-injection test methodology, scope TBD.
- Unproven response treated as effective (ISS-008); mitigation: explicit unproven status and unmanned-demonstration gate enforced at reviews.

## 15. Open Issues

Fault taxonomy and coverage TBD. Reallocation/shutdown thresholds and sequencing TBD. Emergency power capacity/duration TBD. Detection latencies TBD. Unmanned demonstration scope and pass criteria TBD. Human-flight gating criteria TBD. ISS-008 applies to all EPM effectiveness claims.

## 16. Assumptions

- A-EPM-001: Health monitoring can supply fault declarations adequate to trigger a safety-path response; validation: Vol 07/10 verification (TBD).
- A-EPM-002: Emergency power can be allocated to sustain at least one EPM response thread; validation: Vol 05/13.16 sizing analysis (TBD).
- A-EPM-003: Hover/low-altitude bounds EPM effectiveness for early flight; validation: Vol 13 analysis and Vol 19 modelling (both TBD).

## 17. Dependencies

Depends on SYS-003 (requirements basis), FHA/FMEA (fault hooks), Vol 04/05 (propulsion/power implementation), Vol 07/10 (health monitoring/alerts), Vol 13.16 (emergency power), SEMP (gates), V&V Plan (verification discipline), Vol 23 (test execution).

## 18. Traceability

Parents: SYS-003, FHA/FMEA EPM hooks. Children: EPM decision criteria, interface definitions, and demonstration cases (artefact IDs TBD).
RTM: REQ-HFPX-EPM-001..004 → CONCEPT. Each fault class traces to a response option or justified exclusion; each response option traces to at least one demonstration case (all TBD except IDs).

## 19. Configuration

BL-0.0 (structure only) — Tranche 4 draft, not baselined. EPM criteria and interface definitions are under document control once populated; changes via change records with affected-fault impact stated.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (emergency propulsion management; Ch 13.9) |
