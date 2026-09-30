# Control Surfaces

**Document ID:** HFPX-AERO-CSF-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the control-surface scope at structure-only level before any surface set is chosen. Owns Chapter 06.4 and establishes what surface definitions, authority contributions, and flight-control interfaces the programme shall address while keeping pure thrust-vectoring control as an open alternative.

## 2. Scope

Covers aerodynamic control surfaces (candidate set, definitions TBD) and their relationship to thrust-vectoring control from distributed propulsion. No surface type, count, geometry, deflection, hinge, effectiveness, speed, or angle value is set here — all TBD. Wing geometry is owned by 06.3; control laws and FCS architecture are owned by Vol 07.

## 3. Applicable Documents

- HFPX-SYS-MIS-001 Mission Definition; HFPX-SYS-REQ-001 SyRS (stub); HFPX-SYS-ARC-001 SAD (stub)
- HFPX-AERO-CON-001 Aerodynamic Concept (06.1); Volume 06 chapters 06.2, 06.3, 06.8–06.11 (stability, 6-DOF)
- Vol 05 Propulsion (thrust-vectoring sources); Vol 07 Flight Control (FCS); Vol 19 Modelling & Simulation
- HFP Documentation schema (Vol 01)

## 4. Definitions & Acronyms

- Control surface: aerodynamic device contributing control moments/forces; set TBD
- Thrust-vectoring control: attitude/translation control via distributed-thrust direction or modulation; authority TBD, retained as an alternative to surfaces with the trade open
- Surface authority: control contribution attributed to surfaces within the overall control allocation; values TBD
- FCS: flight control system (Vol 07); 6-DOF: six-degree-of-freedom model (06.11, structure only here, no numeric coefficients)

## 5. System Context

Control surfaces sit between aerodynamics (Volume 06) and flight control (Vol 07). Control allocation blends surface moments with distributed-thrust effects across hover, transition, and horizontal flight. Actors: FCS computers and actuators (Vol 07), propulsion modules (Vol 05), pilot inputs via smart helmet/HUD pathways (Vol 12, TBD). Environments and envelopes: all TBD. Allocation is owned by the SAD aero and FCS views.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-ACF-001|HFP-X control-surface set (surface types, locations, and allocation roles) shall remain TBD with the trade between surfaces and pure thrust-vectoring control held open.|HFPX-SYS-REQ-001, HFPX-SYS-ARC-001 SAD aero views|Inspection|
| REQ-HFPX-ACF-002 | HFP-X control-surface authority contribution within the overall control allocation shall remain TBD with estimation method TBD. | HFPX-SYS-REQ-001 | Analysis |
|REQ-HFPX-ACF-003|HFP-X control-surface design shall define an FCS interface with Vol 07 with interface content TBD.|HFPX-SYS-REQ-001, HFPX-SYS-ARC-001 SAD aero views|Inspection|
|REQ-HFPX-ACF-004|HFP-X control-surface design shall be verified by a method TBD with acceptance criteria TBD and all quantitative results TBD.|HFPX-SYS-REQ-001|Inspection|

Full 6-DOF equations apply to detailed modelling (06.11) and are structure only here with no numeric coefficients stated or implied.

## 7. Architecture

Control-effector work packages: surface-set definition (TBD) → authority estimation (TBD) → FCS allocation interface (Vol 07, TBD) → verification (method TBD). Outputs feed stability work (06.8–06.10) and the 6-DOF model (06.11). Package-to-system allocation is owned by the SAD.

## 8. Detailed Design

Not applicable — no surface selected. No surface type, span, chord, area, hinge, deflection, rate, or effectiveness value is stated or implied. Surface-versus-thrust-vectoring apportionment is a trade not started.

## 9. Interfaces

- Upstream: aerodynamic concept (06.1), wing/lifting-body outputs (06.2, 06.3), system requirements (SYS-001), SAD aero views
- Downstream: 06.8 stability, 06.9 static stability, 06.10 dynamic stability, 06.11 6-DOF model
- External: FCS control laws, sensing, and actuation (Vol 07 interface TBD per REQ-HFPX-ACF-003), propulsion thrust-vectoring sources (Vol 05 interface TBD)

## 10. Operational Concept

Summary only; detail in CONOPS: control-effector behaviour, whatever the surface/thrust-vectoring blend, is proven unmanned across hover, transition, and horizontal flight before any human exposure. No handling-qualities or envelope claim is stated here.

## 11. Safety

No control-surface configuration is cleared for flight by this document. Loss of surface, jam, float, actuator failure, and thrust-vectoring failure implications are unanalysed and owned with Vol 07 and Vol 13 once candidates exist. Hazardous-subsystem boundary applies: this document contains no build, ignition, or operation instructions for high-energy propulsion.

## 12. Performance

All control-surface performance values TBD. No force, moment, effectiveness, coefficient, deflection, rate, speed, or altitude figure is stated or implied. Handling-qualities assessment awaits stability analysis (06.8–06.10) and FCS design (Vol 07).

## 13. Verification & Validation

Requirements verified by: review of surface-set scope and FCS-interface capture (REQ-HFPX-ACF-001, REQ-HFPX-ACF-003) and analysis of authority contributions when methods exist (REQ-HFPX-ACF-002, REQ-HFPX-ACF-004). CFD, wind-tunnel testing, rig, and flight test are downstream and not claimed here. Validation: acceptance that the control-effector scope plus trade linkage is complete at SRR.

## 14. Risks

- Control-authority shortfall in one or more regimes if surfaces prove ineffective at low dynamic pressure and thrust vectoring alone is insufficient — mitigation: open trade per REQ-HFPX-ACF-001 plus analysis per REQ-HFPX-ACF-002
- FCS allocation undefined — mitigation: Vol 07 interface per REQ-HFPX-ACF-003
- Premature effector selection before stability and FCS trades complete — mitigation: TBD-only rule

## 15. Open Issues

Surface set, authority method, FCS-interface content, verification method, and acceptance criteria TBD. Stability inputs (06.8–06.10) and FCS architecture (Vol 07) pending.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on aerodynamic concept (06.1), wing/lifting-body outputs (06.2, 06.3), system requirements and SAD aero views (Vol 02), propulsion control sources (Vol 05), FCS architecture (Vol 07), and modelling capability (Vol 19).

## 18. Traceability

Parent: HFPX-SYS-REQ-001 (SYS-001), REQ-HFPX-MIS-002, REQ-HFPX-MIS-003, HFPX-SYS-ARC-001 SAD aero views. Children: 06.8–06.10 stability inputs, 06.11 6-DOF model inputs, Vol 07 FCS interface requirements. RTM: REQ-HFPX-ACF-001..004 → CONCEPT, verification IDs TBD.

## 19. Configuration

BL-0.0. Tranche 5 draft, CONCEPT, not baselined.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 draft (Chapter 06.4) |
