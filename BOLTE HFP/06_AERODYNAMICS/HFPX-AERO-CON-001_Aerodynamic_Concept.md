# Aerodynamic Concept

**Document ID:** HFPX-AERO-CON-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X aerodynamic concept at structure-only level before any airframe configuration is selected. Owns Chapter 06.1 and establishes the lift-sharing principle, flight-regime distinctions, and trade-study inputs for all downstream aerodynamics work in Volume 06.

## 2. Scope

Covers the conceptual relationship between aerodynamic lift and distributed propulsion lift across hover, transition, and horizontal flight. Applies to the prone/semi-prone piloted concept with distributed jet modules. No geometry, coefficient, area, mass, speed, or angle value is set here — all TBD. Detailed modelling, CFD, and test are owned by later chapters in this volume.

## 3. Applicable Documents

- HFPX-SYS-MIS-001 Mission Definition; HFPX-SYS-REQ-001 SyRS (stub); HFPX-SYS-ARC-001 SAD (stub)
- HFPX-SYS-OPC-001 Operational Concept; HFPX-SYS-CON-001 CONOPS
- Volume 06 chapters 06.2–06.7 (lifting body, wing, control surfaces, drag, lift, propulsion-airframe interaction); Vol 19 Modelling & Simulation; Vol 03 Structures; Vol 07 Flight Control
- HFP Documentation schema (Vol 01); HFP prompt flight-regime and trade-study provisions

## 4. Definitions & Acronyms

- VTOL: vertical take-off and landing; CONOPS: Concept of Operations
- Lift-sharing: combined support of weight by aerodynamic lift and the vertical component of distributed thrust; conceptual relations L + Tv ≈ W and Th ≈ D stated qualitatively only
- Hover: lift from thrust; Transition: conversion between hover and horizontal flight with lift shared; Cruise/horizontal flight: lift shared with aerodynamic surfaces
- Full 6-DOF equations: detailed modelling formulation owned by 06.11; structure only in this document, with no numeric coefficients stated or implied
- ISS-004: airframe-configuration trade study; ISS-007: budgets and feasibility actions

## 5. System Context

The aerodynamic concept sits between mission intent (vertical take-off, controlled hover, transition, horizontal cruise per REQ-HFPX-MIS-001..003) and the airframe trade space. Actors: pilot (long-term, prone/semi-prone integration TBD, Vol 12), distributed propulsion modules (Vol 05), flight control system (Vol 07), structures (Vol 03). Environments (altitude, temperature, wind, visibility envelopes): all TBD. This document allocates nothing to hardware; allocation is owned by the SAD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-ANC-001 | HFP-X aerodynamic concept shall define lift as shared between aerodynamic surfaces/body and distributed thrust, with the split between sources TBD by regime. | REQ-HFPX-MIS-002, REQ-HFPX-MIS-003, HFPX-SYS-REQ-001 | Inspection |
| REQ-HFPX-ANC-002 | HFP-X aerodynamic concept shall distinguish hover, transition, and cruise aerodynamic regimes with regime definitions TBD and no performance values stated. | REQ-HFPX-MIS-001, REQ-HFPX-MIS-002, HFPX-SYS-REQ-001 | Inspection |
| REQ-HFPX-ANC-003 | HFP-X aerodynamic concept shall provide trade-study inputs without selecting an airframe configuration; candidate families (conventional wing, lifting body, blended, deployable, hybrid) shall remain open under ISS-004. | HFPX-SYS-REQ-001, HFPX-SYS-ARC-001 SAD aero views | Inspection |
| REQ-HFPX-ANC-004 | HFP-X aerodynamic concept shall be verified by review and first-order analysis with method TBD and all quantitative results TBD. | HFPX-SYS-REQ-001 | Inspection + Analysis |

Conceptual relations L + Tv ≈ W and Th ≈ D are stated qualitatively only to frame lift-sharing. Full 6-DOF equations apply to detailed modelling (06.11) and are structure only here with no numeric coefficients.

## 7. Architecture

Aerodynamic-concept segments: hover (thrust-supported) → transition (mixed support, conversion both directions) → horizontal flight including cruise (shared support). Segment definitions feed 06.12 Hover Flight, 06.13 Transition Flight, 06.14 Horizontal Flight, and 06.15 Cruise. Segment-to-system allocation is owned by the SAD aero views.

## 8. Detailed Design

Not applicable — no design selected. Candidate airframe families (conventional wing, lifting body, blended, deployable, hybrid) are trade studies not started (ISS-004). No planform, section, area, twist, dihedral, incidence, or control-allocation value is stated or implied.

## 9. Interfaces

- Upstream: mission requirements (MIS-001..003), system requirements (SYS-001), SAD aero views
- Downstream: 06.2 lifting-body design, 06.3 wing design, 06.4 control surfaces, 06.5 drag, 06.6 lift characteristics, 06.7 propulsion-airframe interaction, 06.11 6-DOF model
- External: structures (Vol 03 load interfaces TBD), flight control (Vol 07 authority interfaces TBD), propulsion (Vol 05 installation interfaces TBD), pilot integration (Vol 12 interface TBD)

## 10. Operational Concept

Summary only; detail in CONOPS: unmanned demonstrator proves hover, then transition, then horizontal flight before any human exposure; each regime transition is monitored from the ground station with abort/recovery authority TBD. No operational envelope value is stated here.

## 11. Safety

Aerodynamic-concept safety is subordinate to pilot and public safety. No flight envelope is cleared by this document. Hover/transition controllability with prone pilot plus distributed propulsion is unanalysed (ISS-006). Hazardous-subsystem boundary applies: this document contains no build, ignition, or operation instructions for high-energy propulsion.

## 12. Performance

All aerodynamic performance values TBD. No lift, drag, moment, coefficient, reference quantity, speed, altitude, mass, or thrust figure is stated or implied. First-order budgets (mass, thrust-to-weight, energy) are actions under ISS-007 and fed by later Volume 06 outputs, not set here.

## 13. Verification & Validation

Requirements verified by: review of concept completeness and consistency (REQ-HFPX-ANC-001..004), plus first-order analysis with method TBD. CFD and wind-tunnel testing (06.19, 06.20) and 6-DOF-model validation (06.11) are downstream and not claimed here. Validation: stakeholder acceptance at SRR that the concept plus trade-study scope is complete.

## 14. Risks

- Thrust-to-weight/energy feasibility unknown (ISS-007) — lift-sharing split may be infeasible as stated; mitigation: early budgets fed by Volume 06 estimates
- Hover/transition controllability with prone pilot plus distributed propulsion unanalysed (ISS-006)
- Premature airframe down-selection before ISS-004 trades complete — mitigation: REQ-HFPX-ANC-003 no-selection rule

## 15. Open Issues

ISS-004 (airframe-configuration trade — this document provides inputs, trade stays OPEN), ISS-006, ISS-007. Verification methods and analysis tools (Vol 19) TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on mission baseline (Vol 01), system requirements and SAD aero views (Vol 02), trade studies (ISS-003/ISS-004), modelling capability (Vol 19), and budget actions (ISS-007).

## 18. Traceability

Parent: HFPX-SYS-REQ-001 (SYS-001), REQ-HFPX-MIS-002, REQ-HFPX-MIS-003, HFPX-SYS-ARC-001 SAD aero views. Children: 06.2–06.7 design and characteristics documents, 06.11 6-DOF model, Vol 03/05/07 interface requirements. RTM: REQ-HFPX-ANC-001..004 → CONCEPT, verification IDs TBD.

## 19. Configuration

BL-0.0. Tranche 5 draft, CONCEPT, not baselined.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 draft (Chapter 06.1) |
