# Mission Definition

**Document ID:** HFPX-SYS-MIS-001  
**Revision:** B (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 1 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define what HFP-X must achieve at mission level before any design is chosen. Owns Chapter 01.1 and anchors the traceability chain Mission → Stakeholder → System.

## 2. Scope

Covers the HFP-X concept from the master prompt: prone/semi-prone piloted VTOL/transition flight using distributed jet propulsion (arm, rear/torso, ankle modules), fly-by-wire control, inertial/GNSS/barometric/air-data navigation, embedded + independent safety computers, smart helmet/HUD, telemetry, adaptive impact protection and emergency recovery. Long-term objective is controlled human flight; near-term objective is unmanned validation. No performance values are set here — all TBD.

## 3. Applicable Documents

- HFPX-PGM-CHR-001 Programme Charter; HFPX-PGM-SEM-001 SEMP
- HFPX-SYS-OPC-001 Operational Concept; HFPX-SYS-CON-001 CONOPS; HFPX-SYS-STK-001 Stakeholder Requirements
- HFPX-SYS-REQ-001 SyRS (stub); HFPX-SYS-ARC-001 SAD (stub); HFPX-MVP-OBJ-001 MVP Objectives
- HFP Documentation schema (Vol 01); HFP prompt §§1–2, 12–15

## 4. Definitions & Acronyms

- VTOL: vertical take-off and landing; CONOPS: Concept of Operations
- Distributed propulsion: multiple jet modules (arm/rear/ankle) jointly producing controlled thrust
- Transition: conversion between hover (lift from thrust) and horizontal cruise (lift shared with aerodynamic surfaces); conceptual relations L + Tᵥ ≈ W, Tₕ ≈ D; detailed modelling uses full 6-DOF equations
- MVP: unmanned-first demonstrator programme (Vol 33, separate from production)

## 5. System Context

Mission actors: pilot (long-term), ground crew, ground station, regulators, test range. Mission environments: TBD (altitude, temperature, wind, visibility envelopes — all TBD, Vol 01.9/Vol 14). Mission sits inside the V-model: Mission → Stakeholder Needs → System Requirements → Architecture (Vol 02) → SYS-01..SYS-23.

## 6. Requirements

| ID | Requirement (shall) | Source | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-MIS-001 | HFP-X shall be capable of vertical take-off, controlled hover and vertical landing as a mission phase. | Programme concept | Test |
| REQ-HFPX-MIS-002 | HFP-X shall be capable of transitioning between hover and horizontal aerodynamic flight and back under controlled flight. | Programme concept | Test |
| REQ-HFPX-MIS-003 | HFP-X shall be capable of horizontal cruise flight using combined aerodynamic lift and distributed propulsion. | Programme concept | Analysis + Test |
| REQ-HFPX-MIS-004 | HFP-X shall carry mission telemetry to a ground station throughout flight. | Programme concept | Demonstration |
| REQ-HFPX-MIS-005 | HFP-X shall provide an independent emergency recovery capability for defined failure conditions (mechanism TBD, effectiveness TBD). | Safety objective | Analysis + Test |
| REQ-HFPX-MIS-006 | Human-carrying flight shall occur only after unmanned hover, transition and horizontal-flight evidence gates are passed. | DDR-001 | Inspection |
| REQ-HFPX-MIS-007 | Mission performance values (endurance, range, speed, altitude, payload) shall remain TBD until mass, thrust and energy budgets exist. | ISS-007 | Inspection |

## 7. Architecture

Mission segments: pre-flight → engine start → ground idle → hover → hover manoeuvre → transition → horizontal acceleration → cruise → horizontal deceleration → reverse transition → landing → shutdown, plus emergency stabilisation / emergency recovery / safe-aborted states (15 modes, prompt §13; detailed in CONOPS). Segment-to-system allocation is owned by the SAD.

## 8. Detailed Design

Not applicable — no design selected. Candidate propulsion energy sources (jet-fuel/ethanol/hydrogen turbine, hydrogen-electric, battery-electric) and airframe concepts (conventional wing, lifting/blended body, deployable wing, hybrid) are trade studies not started (ISS-003/ISS-004).

## 9. Interfaces

- Upstream: stakeholder needs (01.4); downstream: SyRS (01.6), SAD (02.1), MVP requirements (33.2)
- External: airspace/range, weather services, GNSS, communications spectrum (all TBD, Vol 11/25)

## 10. Operational Concept

Summary only; detail in HFPX-SYS-OPC-001 / HFPX-SYS-CON-001: unmanned demonstrator proves each segment before any human exposure; every flight is monitored from the ground station with abort/recovery authority TBD.

## 11. Safety

Mission success is subordinate to pilot and public safety. Low-altitude/hover recovery effectiveness is unanalysed (ISS-008); no mission profile assumes a working parachute/recovery system until Vol 13.11 analysis exists. Hazardous-subsystem boundary applies: this document contains no build/ignition/operation instructions for high-energy propulsion (prompt §§14, 34).

## 12. Performance

All mission performance values TBD (see REQ-HFPX-MIS-007). No speed, range, endurance, altitude, mass or thrust figure is stated or implied. First-order budgets (mass, thrust-to-weight, energy) are actions under ISS-007.

## 13. Verification & Validation

Mission requirements verified by: analysis (6-DOF models, Vol 06/19), demonstration (ground rig), test (unmanned demonstrator, Vol 33/Vol 23). Validation: stakeholder acceptance at SRR that mission + CONOPS + stakeholder set is complete and consistent.

## 14. Risks

- Thrust-to-weight/energy feasibility unknown (ISS-007) — mission may be infeasible as stated; mitigation: early budgets + trade studies
- Hover/transition controllability with prone pilot + distributed propulsion unanalysed (ISS-006)
- Recovery at low altitude may be ineffective (ISS-008) — constrains mission envelopes until analysed

## 15. Open Issues

ISS-002 (mission/stakeholder baseline — this document partly addresses, stays OPEN until SRR), ISS-006, ISS-007, ISS-008.

## 16. Assumptions


_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on stakeholder approval (01.4), regulatory pathway (Vol 25, ISS-001), trade studies (ISS-003/004), modelling capability (Vol 19).

## 18. Traceability

Parent: Charter (REQ-HFPX-PGM-003 unmanned-first). Children: stakeholder reqs (STK), SyRS (REQ-HFPX-SYS-*), SAD allocation, MVP objectives. RTM: REQ-HFPX-MIS-001..007 → CONCEPT, verification IDs TBD.

## 19. Configuration

BL-0.0. Tranche 1 draft, CONCEPT, not baselined.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 1 draft (Chapter 01.1) |
| B | 2026-09-29 | Assumptions removed; all unknowns recorded as TBD (no assumptions raised or relied upon). |
