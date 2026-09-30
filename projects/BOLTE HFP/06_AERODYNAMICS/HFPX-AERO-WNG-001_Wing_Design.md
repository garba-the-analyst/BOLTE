# Wing Design

**Document ID:** HFPX-AERO-WNG-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the wing-design scope at structure-only level before any wing is chosen. Owns Chapter 06.3 and establishes what wing geometry, load interfaces, and fixed/deployable trades the programme shall address without selecting a configuration.

## 2. Scope

Covers the wing family as one candidate under the ISS-004 trade — fixed, deployable, or hybrid installations integrated with the prone/semi-prone airframe and distributed propulsion. No geometry, coefficient, area, mass, speed, or angle value is set here — all TBD. Lifting-body-specific design is owned by 06.2; control-surface allocation is owned by 06.4.

## 3. Applicable Documents

- HFPX-SYS-MIS-001 Mission Definition; HFPX-SYS-REQ-001 SyRS (stub); HFPX-SYS-ARC-001 SAD (stub)
- HFPX-AERO-CON-001 Aerodynamic Concept (06.1); Volume 06 chapters 06.4–06.7, 06.11, 06.19, 06.20
- Vol 03 Structures; Vol 05 Propulsion; Vol 07 Flight Control; Vol 19 Modelling & Simulation
- HFP Documentation schema (Vol 01)

## 4. Definitions & Acronyms

- Wing: lifting surface candidate distinct from lifting-body lift; geometry TBD, candidate status only, not selected
- Deployable/fixed trade: comparison of stowable versus permanent wing installations including deployment, locking, and stowage considerations; outcome TBD
- Wing-load interface: transfer of wing aerodynamic loads to structure (Vol 03); content TBD
- 6-DOF: six-degree-of-freedom model (06.11, structure only here, no numeric coefficients); ISS-004: airframe-configuration trade study

## 5. System Context

Wing design sits inside the aerodynamic concept (06.1) as one candidate path alongside lifting-body, blended, deployable, and hybrid families. It interacts with structures (wing loads and attachment), flight control (surface authority and FCS allocation), propulsion (installation and interference effects in 06.7), and pilot integration (Vol 12). Environments and envelopes: all TBD. Allocation is owned by the SAD aero views.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-AWG-001|HFP-X wing geometry (planform, section, arrangement, and installation definition) shall remain TBD as a candidate with no selection implied.|HFPX-SYS-REQ-001, HFPX-SYS-ARC-001 SAD aero views|Inspection|
|REQ-HFPX-AWG-002|HFP-X wing design shall define a wing-load and stress interface with Vol 03 with interface content TBD.|HFPX-SYS-REQ-001, HFPX-SYS-ARC-001 SAD aero views|Inspection|
|REQ-HFPX-AWG-003|HFP-X wing design shall address the deployable-versus-fixed trade with trade method, criteria, and outcome TBD.|HFPX-SYS-REQ-001|Inspection|
|REQ-HFPX-AWG-004|HFP-X wing design shall be verified by a method TBD with acceptance criteria TBD and all quantitative results TBD.|HFPX-SYS-REQ-001|Inspection|

Full 6-DOF equations apply to detailed modelling (06.11) and are structure only here with no numeric coefficients stated or implied.

## 7. Architecture

Wing work packages: geometry definition (TBD) → load/stress interface capture (Vol 03, TBD) → deployable/fixed trade (TBD) → verification (method TBD). Outputs feed drag buildup (06.5), lift characteristics (06.6), and the 6-DOF model (06.11). Package-to-system allocation is owned by the SAD.

## 8. Detailed Design

Not applicable — no design selected. No span, chord, area, aspect, taper, sweep, thickness, twist, dihedral, incidence, or deployment-mechanism value is stated or implied. Fixed, deployable, and hybrid options are trades not started (ISS-004).

## 9. Interfaces

- Upstream: aerodynamic concept (06.1), system requirements (SYS-001), SAD aero views
- Downstream: 06.4 control surfaces, 06.5 drag, 06.6 lift characteristics, 06.11 6-DOF model, 06.19 CFD, 06.20 wind-tunnel testing
- External: structures wing loads and attachment (Vol 03 interface TBD per REQ-HFPX-AWG-002), flight control allocation (Vol 07 interface TBD), propulsion installation (Vol 05 interface TBD, effects in 06.7)

## 10. Operational Concept

Summary only; detail in CONOPS: any wing, if pursued, is proven unmanned across transition and horizontal flight including deployment sequencing where applicable before any human exposure. No operational envelope, deployment timeline, or handling claim is stated here.

## 11. Safety

No wing configuration is cleared for flight by this document. Deployment failure, asymmetric deployment, flutter, and structural-failure implications are unanalysed and owned with Vol 03 and Vol 13 once candidates exist. Hazardous-subsystem boundary applies: this document contains no build, ignition, or operation instructions for high-energy propulsion.

## 12. Performance

All wing performance values TBD. No lift, drag, moment, coefficient, reference quantity, stall, deployment, speed, or altitude figure is stated or implied. Contribution to mass, thrust-to-weight, and energy budgets is via ISS-007 actions once estimates exist.

## 13. Verification & Validation

Requirements verified by: review of geometry scope, load-interface capture, and trade coverage (REQ-HFPX-AWG-001..003) and a verification method TBD (REQ-HFPX-AWG-004). Analysis, CFD (06.19), and wind-tunnel testing (06.20) are downstream and not claimed here. Validation: acceptance that the wing scope plus trade-study linkage is complete at SRR.

## 14. Risks

- Wing feasibility unknown (mass, stowage, deployment reliability, pilot-integration penalty) — mitigation: ISS-004 trade under REQ-HFPX-AWG-003 before any selection
- Wing-load path undefined — mitigation: Vol 03 interface per REQ-HFPX-AWG-002
- Premature wing selection before trades and budgets complete — mitigation: candidate-only rule per REQ-HFPX-AWG-001

## 15. Open Issues

ISS-004 (wing versus lifting-body/blended/deployable/hybrid trade stays OPEN), ISS-006, ISS-007. Geometry method, load-interface content, trade criteria, verification method, and acceptance criteria TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on aerodynamic concept (06.1), system requirements and SAD aero views (Vol 02), structures inputs (Vol 03), flight-control inputs (Vol 07), modelling capability (Vol 19), and budget actions (ISS-007).

## 18. Traceability

Parent: HFPX-SYS-REQ-001 (SYS-001), REQ-HFPX-MIS-002, REQ-HFPX-MIS-003, HFPX-SYS-ARC-001 SAD aero views. Children: 06.4 surface allocation, 06.5 drag buildup entries, 06.6 lift tables, 06.11 6-DOF model inputs, Vol 03 interface requirements. RTM: REQ-HFPX-AWG-001..004 → CONCEPT, verification IDs TBD.

## 19. Configuration

BL-0.0. Tranche 5 draft, CONCEPT, not baselined.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 draft (Chapter 06.3) |
