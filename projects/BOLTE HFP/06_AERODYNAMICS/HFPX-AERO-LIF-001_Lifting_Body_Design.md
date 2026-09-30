# Lifting-Body Design

**Document ID:** HFPX-AERO-LIF-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the lifting-body design scope at structure-only level before any geometry is chosen. Owns Chapter 06.2 and establishes what the lifting-body contribution shall cover, how it shall be estimated, and which interfaces bound it.

## 2. Scope

Covers the lifting-body airframe family as one candidate under the ISS-004 trade — body-generated aerodynamic lift integrated with the prone/semi-prone pilot envelope and distributed propulsion installation. No geometry, coefficient, area, mass, speed, or angle value is set here — all TBD. Wing-specific design is owned by 06.3; blended-body trades remain open under ISS-004.

## 3. Applicable Documents

- HFPX-SYS-MIS-001 Mission Definition; HFPX-SYS-REQ-001 SyRS (stub); HFPX-SYS-ARC-001 SAD (stub)
- HFPX-AERO-CON-001 Aerodynamic Concept (06.1); Volume 06 chapters 06.5–06.7, 06.11, 06.19, 06.20
- Vol 03 Structures; Vol 05 Propulsion; Vol 12 Human Systems / Pilot Integration; Vol 19 Modelling & Simulation
- HFP Documentation schema (Vol 01)

## 4. Definitions & Acronyms

- Lifting body: airframe whose fuselage/body form contributes aerodynamic lift in addition to any wing surfaces; geometry TBD
- Lift contribution: share of weight support attributed to the body in the lift-sharing concept (L + Tv ≈ W stated qualitatively); estimates TBD, method TBD
- CFD: computational fluid dynamics (06.19); 6-DOF: six-degree-of-freedom model (06.11, structure only here, no numeric coefficients)
- ISS-004: airframe-configuration trade study; ISS-007: budgets and feasibility actions

## 5. System Context

Lifting-body design sits inside the aerodynamic concept (06.1) as one candidate path. It interacts with pilot integration (body conforms around the prone/semi-prone pilot, Vol 12), propulsion installation (Vol 05 module integration effects owned by 06.7), structures (Vol 03 body-load interfaces), and flight control (Vol 07). Environments and envelopes: all TBD. No configuration is selected; allocation is owned by the SAD aero views.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-ALF-001|HFP-X lifting-body geometry (outer mould line, body planform and section definition) shall remain TBD with definition method TBD and no selection implied.|HFPX-SYS-REQ-001, HFPX-SYS-ARC-001 SAD aero views|Inspection|
| REQ-HFPX-ALF-002 | HFP-X lifting-body lift and contribution estimates shall remain TBD with estimation method TBD and all coefficients and reference quantities TBD. | REQ-HFPX-MIS-002, REQ-HFPX-MIS-003, HFPX-SYS-REQ-001 | Analysis |
|REQ-HFPX-ALF-003|HFP-X lifting-body design shall define a pilot-integration interface with Vol 12 with interface content TBD.|HFPX-SYS-REQ-001, HFPX-SYS-ARC-001 SAD aero views|Inspection|
| REQ-HFPX-ALF-004 | HFP-X lifting-body design shall be verified by analysis, CFD, or test with method and acceptance criteria TBD. | HFPX-SYS-REQ-001 | Analysis |

Full 6-DOF equations apply to detailed modelling (06.11) and are structure only here with no numeric coefficients stated or implied.

## 7. Architecture

Lifting-body work packages: outer-shape definition (TBD) → lift-contribution estimation (TBD) → pilot/propulsion/structures integration (TBD) → verification (analysis/CFD/test, TBD). Outputs feed drag buildup (06.5), lift characteristics (06.6), and the 6-DOF model (06.11). Package-to-system allocation is owned by the SAD.

## 8. Detailed Design

Not applicable — no design selected. No outer mould line, section, area, aspect, camber, incidence, or edge-detail value is stated or implied. Candidate relationships to blended and hybrid families are trades not started (ISS-004).

## 9. Interfaces

- Upstream: aerodynamic concept (06.1), system requirements (SYS-001), SAD aero views
- Downstream: 06.5 drag, 06.6 lift characteristics, 06.11 6-DOF model, 06.19 CFD, 06.20 wind-tunnel testing
- External: pilot integration (Vol 12 interface TBD per REQ-HFPX-ALF-003), structures body loads (Vol 03 interface TBD), propulsion installation (Vol 05 interface TBD, effects in 06.7)

## 10. Operational Concept

Summary only; detail in CONOPS: lifting-body behaviour, if pursued, is proven unmanned across hover, transition, and horizontal flight before any human exposure. No operational envelope or handling claim is stated here.

## 11. Safety

No lifting-body geometry is cleared for flight by this document. Pilot-enclosure, egress, and emergency-recovery implications of any body shape are unanalysed and owned with Vol 12 and Vol 13. Hazardous-subsystem boundary applies: this document contains no build, ignition, or operation instructions for high-energy propulsion.

## 12. Performance

All lifting-body performance values TBD. No lift, drag, moment, coefficient, reference quantity, stall, speed, or altitude figure is stated or implied. Contribution to mass, thrust-to-weight, and energy budgets is via ISS-007 actions once estimates exist.

## 13. Verification & Validation

Requirements verified by: review of geometry and interface completeness (REQ-HFPX-ALF-001, REQ-HFPX-ALF-003) and analysis of lift/contribution estimates when methods exist (REQ-HFPX-ALF-002, REQ-HFPX-ALF-004). CFD (06.19) and wind-tunnel testing (06.20) are downstream and not claimed here. Validation: acceptance that the lifting-body scope plus trade-study linkage is complete at SRR.

## 14. Risks

- Body lift contribution unknown — concept may over-rely on body lift; mitigation: estimates TBD under REQ-HFPX-ALF-002 before any selection
- Pilot-integration conflict (aerodynamic shape versus pilot posture, enclosure, egress) — mitigation: Vol 12 interface per REQ-HFPX-ALF-003
- Premature lifting-body selection before ISS-004 trades complete — mitigation: no-selection rule carried from 06.1

## 15. Open Issues

ISS-004 (lifting-body versus wing/blended/deployable/hybrid trade stays OPEN), ISS-006, ISS-007. Geometry method, estimation method, CFD/test ownership, and acceptance criteria TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on aerodynamic concept (06.1), system requirements and SAD aero views (Vol 02), pilot-integration inputs (Vol 12), structures inputs (Vol 03), modelling capability (Vol 19), and budget actions (ISS-007).

## 18. Traceability

Parent: HFPX-SYS-REQ-001 (SYS-001), REQ-HFPX-MIS-002, REQ-HFPX-MIS-003, HFPX-SYS-ARC-001 SAD aero views. Children: 06.5 drag buildup entries, 06.6 lift tables, 06.11 6-DOF model inputs, Vol 03/12 interface requirements. RTM: REQ-HFPX-ALF-001..004 → CONCEPT, verification IDs TBD.

## 19. Configuration

BL-0.0. Tranche 5 draft, CONCEPT, not baselined.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 draft (Chapter 06.2) |
