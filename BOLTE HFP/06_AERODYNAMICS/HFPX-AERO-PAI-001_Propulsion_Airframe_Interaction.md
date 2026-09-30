# Propulsion-Airframe Interaction

**Document ID:** HFPX-AERO-PAI-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the propulsion-airframe interaction scope at structure-only level before any interaction magnitude is known. Owns Chapter 06.7 and establishes which effects shall be enumerated, who shall model them, and how adverse interactions shall be mitigated — analysis only, with no propulsion operation instructions.

## 2. Scope

Covers aerodynamic effects of propulsion installation and operation on the airframe and vice versa — inflow, exhaust, and interference — across hover, transition, and horizontal flight. All magnitudes, coefficients, pressures, temperatures, speeds, and attitudes are TBD. Propulsion design is owned by Vol 05; drag accounting is owned by 06.5; lift tables are owned by 06.6. This document contains no propulsion operation instructions.

## 3. Applicable Documents

- HFPX-SYS-MIS-001 Mission Definition; HFPX-SYS-REQ-001 SyRS (stub); HFPX-SYS-ARC-001 SAD (stub)
- HFPX-AERO-CON-001 Aerodynamic Concept (06.1); Volume 06 chapters 06.2–06.6, 06.11, 06.19, 06.20
- Vol 03 Structures; Vol 05 Propulsion; Vol 07 Flight Control; Vol 19 Modelling & Simulation
- HFP Documentation schema (Vol 01)

## 4. Definitions & Acronyms

- Inflow effect: influence of propulsion-induced intake flow on airframe aerodynamics; magnitudes TBD
- Exhaust effect: influence of propulsion exhaust/jet flow on airframe aerodynamics, structures, and control; magnitudes TBD
- Interference effect: mutual aerodynamic interference between installed modules, pilot envelope, body, and surfaces; magnitudes TBD
- 6-DOF: six-degree-of-freedom model (06.11, structure only here, no numeric coefficients); CFD: computational fluid dynamics (06.19)

## 5. System Context

Propulsion-airframe interaction sits at the Vol 05 / Volume 06 boundary. Sources: distributed jet modules (arm, rear/torso, ankle installations, Vol 05). Affected systems: airframe lift and drag (06.2–06.6), control authority (06.4, Vol 07), structures including thermal and load effects (Vol 03). Environments and envelopes: all TBD. Allocation of modelling ownership is TBD per REQ-HFPX-API-002; system allocation is owned by the SAD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-API-001|HFP-X propulsion-airframe interaction effects (inflow, exhaust, interference) shall be enumerated with all magnitudes, conditions, and methods TBD.|HFPX-SYS-REQ-001, HFPX-SYS-ARC-001 SAD aero views|Inspection|
|REQ-HFPX-API-002|HFP-X propulsion-airframe interaction modelling ownership (analysis, CFD, test apportionment) shall be defined with methods and acceptance criteria TBD.|HFPX-SYS-REQ-001|Inspection|
|REQ-HFPX-API-003|HFP-X design shall mitigate adverse propulsion-airframe interactions under a defined mitigation rule with mitigation content TBD.|REQ-HFPX-MIS-002, REQ-HFPX-MIS-003, HFPX-SYS-REQ-001|Inspection|
| REQ-HFPX-API-004 | HFP-X propulsion-airframe interaction work shall remain analysis-only and shall contain no propulsion build, ignition, or operation instructions. | HFPX-SYS-REQ-001 | Inspection |

Full 6-DOF equations apply to detailed modelling (06.11) and are structure only here with no numeric coefficients stated or implied.

## 7. Architecture

Interaction work packages: effect enumeration (inflow/exhaust/interference, TBD) → modelling apportionment across analysis/CFD/test (TBD) → mitigation actions into airframe and installation design (TBD) → feeds to drag (06.5), lift (06.6), and 6-DOF model (06.11). Package-to-system allocation is owned by the SAD aero and propulsion views.

## 8. Detailed Design

Not applicable — enumeration and process only, no magnitudes. Interaction register schema:

| Effect | Source installation | Affected system | Magnitude | Method | Status |
| --- | --- | --- | --- | --- | --- |
| Inflow | TBD | TBD | TBD | TBD | TBD |
| Exhaust | TBD | TBD | TBD | TBD | TBD |
| Interference | TBD | TBD | TBD | TBD | TBD |

All cells TBD. No magnitude, coefficient, pressure, temperature, speed, or attitude value is stated or implied.

## 9. Interfaces

- Upstream: aerodynamic concept (06.1), lifting-body/wing/surface outputs (06.2–06.4), system requirements (SYS-001), SAD aero views
- Downstream: 06.5 drag buildup, 06.6 lift tables, 06.11 6-DOF model, mitigation actions into Vol 03/05/07
- External: propulsion module definitions and installation data (Vol 05, TBD), structures thermal/load interfaces (Vol 03, TBD), FCS authority interfaces (Vol 07, TBD), CFD/test capability (06.19, 06.20, Vol 19)

## 10. Operational Concept

Summary only; detail in CONOPS: interaction effects, once characterised, inform unmanned-first envelope expansion and installation refinements. No operational envelope, throttle, sequencing, or handling claim is stated here, and no operating procedure is given.

## 11. Safety

No interaction assessment in this document clears any installation or envelope for flight. Adverse interactions (lift loss, control degradation, thermal/structural distress, ingestion effects) are unanalysed and owned with Vol 03, Vol 05, Vol 07, and Vol 13 once candidates exist. Hazardous-subsystem boundary applies: this document contains no build, ignition, or operation instructions for high-energy propulsion per REQ-HFPX-API-004.

## 12. Performance

All interaction performance values TBD. No thrust, lift/drag increment, moment, coefficient, pressure, temperature, speed, or altitude figure is stated or implied. Budget and 6-DOF impact is assessed only once characterised data exists.

## 13. Verification & Validation

Requirements verified by: review of effect enumeration (REQ-HFPX-API-001), review of modelling-ownership apportionment (REQ-HFPX-API-002), review of the mitigation rule (REQ-HFPX-API-003), and inspection of analysis-only scope compliance (REQ-HFPX-API-004). Characterisation by analysis/CFD/test is downstream (06.19, 06.20) and not claimed here. Validation: acceptance that the interaction scope plus mitigation path is complete at SRR.

## 14. Risks

- Adverse interactions discovered late (lift loss, control loss, thermal distress) forcing installation redesign — mitigation: early enumeration per REQ-HFPX-API-001 plus mitigation rule per REQ-HFPX-API-003
- Modelling ownership undefined, leaving effects unowned — mitigation: apportionment per REQ-HFPX-API-002
- Scope creep into propulsion operation guidance — mitigation: analysis-only rule per REQ-HFPX-API-004

## 15. Open Issues

Effect magnitudes, conditions, modelling ownership, methods, acceptance criteria, and mitigation content TBD. Propulsion installation definitions (Vol 05) pending.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on aerodynamic concept and contributor inputs (06.1–06.6), system requirements and SAD aero views (Vol 02), propulsion installation inputs (Vol 05), structures/FCS inputs (Vol 03, Vol 07), and modelling/CFD/test capability (Vol 19, 06.19, 06.20).

## 18. Traceability

Parent: HFPX-SYS-REQ-001 (SYS-001), REQ-HFPX-MIS-002, REQ-HFPX-MIS-003, HFPX-SYS-ARC-001 SAD aero views. Children: 06.5 drag entries, 06.6 lift-table corrections, 06.11 6-DOF model inputs, Vol 03/05/07 mitigation actions. RTM: REQ-HFPX-API-001..004 → CONCEPT, verification IDs TBD.

## 19. Configuration

BL-0.0. Tranche 5 draft, CONCEPT, not baselined.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 draft (Chapter 06.7) |
