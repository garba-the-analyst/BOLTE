# Aerodynamic Drag

**Document ID:** HFPX-AERO-DRG-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the aerodynamic-drag scope at structure-only level before any estimate exists. Owns Chapter 06.5 and establishes the drag-buildup schema, the update rule with design maturity, and the feed from drag data into energy and endurance budgets.

## 2. Scope

Covers drag buildup across hover, transition, and horizontal flight, including body, pilot, propulsion-module, and interference contributors. All drag values, coefficients, reference quantities, speeds, and altitudes are TBD. Lift characteristics are owned by 06.6; propulsion-airframe interaction magnitudes are owned by 06.7. This document defines schema and process only.

## 3. Applicable Documents

- HFPX-SYS-MIS-001 Mission Definition; HFPX-SYS-REQ-001 SyRS (stub); HFPX-SYS-ARC-001 SAD (stub)
- HFPX-AERO-CON-001 Aerodynamic Concept (06.1); Volume 06 chapters 06.2–06.4, 06.6, 06.7, 06.11, 06.19, 06.20
- Vol 05 Propulsion; Vol 12 Human Systems / Pilot Integration; Vol 19 Modelling & Simulation; ISS-007 budget actions (energy/endurance budgets)
- HFP Documentation schema (Vol 01)

## 4. Definitions & Acronyms

- Drag buildup: structured summation of drag contributors (body, pilot, modules, interference) into a total per regime; schema defined here, all values TBD
- Interference drag: increment attributed to mutual interference between airframe, pilot, and propulsion flows; estimates TBD, method TBD
- Conceptual relation Th ≈ D stated qualitatively only; full 6-DOF equations apply to detailed modelling (06.11), structure only here, no numeric coefficients
- ISS-007: budgets and feasibility actions including energy/endurance budgets fed by drag data

## 5. System Context

Drag estimation sits between aerodynamic definition (06.1–06.4, 06.6, 06.7) and programme budgets (ISS-007 energy/endurance). Consumers: 6-DOF model (06.11), transition/cruise performance assessments (06.13–06.15), energy and endurance budgets. Contributors: body shape (06.2), wing (06.3), pilot envelope (Vol 12), installed modules (Vol 05, effects in 06.7). Environments: all TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-ADR-001|HFP-X drag buildup shall use a defined table schema covering body, pilot, propulsion-module, and interference contributors with all estimates, coefficients, reference quantities, and methods TBD.|HFPX-SYS-REQ-001, HFPX-SYS-ARC-001 SAD aero views|Inspection|
|REQ-HFPX-ADR-002|HFP-X drag estimates shall be updated with design maturity under a defined update rule with maturity gates TBD.|HFPX-SYS-REQ-001|Inspection|
|REQ-HFPX-ADR-003|HFP-X drag data shall feed energy and endurance budgets under ISS-007 with feed content and timing TBD.|REQ-HFPX-MIS-003, HFPX-SYS-REQ-001|Inspection|

No coefficient, area, speed, angle, mass, or thrust figure is stated or implied in the schema. Estimates and method remain TBD.

## 7. Architecture

Drag work packages: schema definition (this document) → contributor estimates per regime (TBD) → interference accounting via 06.7 (TBD) → budget and 6-DOF feeds (TBD). Drag tables are versioned artefacts updated at maturity gates TBD. Allocation of estimation ownership (analysis/CFD/test) is TBD across 06.19, 06.20, and Vol 19.

## 8. Detailed Design

Not applicable — schema only, no estimates. Drag-buildup table schema:

| Contributor | Regime applicability | Estimate | Method | Status |
| --- | --- | --- | --- | --- |
| Body | TBD | TBD | TBD | TBD |
| Pilot | TBD | TBD | TBD | TBD |
| Propulsion modules (installed) | TBD | TBD | TBD | TBD |
| Interference | TBD | TBD | TBD | TBD |
| Total | TBD | TBD | TBD | TBD |

All cells TBD. No contributor value, coefficient, reference quantity, or method is stated or implied.

## 9. Interfaces

- Upstream: aerodynamic concept (06.1), lifting-body/wing/surface outputs (06.2–06.4), lift characteristics (06.6), interaction effects (06.7), system requirements (SYS-001), SAD aero views
- Downstream: 06.11 6-DOF model, 06.13–06.15 regime performance, ISS-007 energy/endurance budgets
- External: pilot-envelope inputs (Vol 12, TBD), propulsion installation inputs (Vol 05, TBD), modelling/CFD/test capability (Vol 19, 06.19, 06.20)

## 10. Operational Concept

Summary only; detail in CONOPS: drag tables, once populated, support unmanned-first envelope expansion from hover through transition to horizontal flight. No operational envelope, range, endurance, or speed claim is stated here.

## 11. Safety

No drag estimate in this document supports any flight-clearance or envelope claim. Understated drag propagates to energy shortfall and forced-landing risk; mitigation is the update rule (REQ-HFPX-ADR-002) plus ISS-007 budget scrutiny. Hazardous-subsystem boundary applies: this document contains no build, ignition, or operation instructions for high-energy propulsion.

## 12. Performance

All drag performance values TBD. No drag force, coefficient, reference quantity, speed, altitude, endurance, or range figure is stated or implied. Budget impact is assessed only through ISS-007 actions once estimates exist.

## 13. Verification & Validation

Requirements verified by: review of schema completeness (REQ-HFPX-ADR-001), review of the update rule (REQ-HFPX-ADR-002), and review that budget feeds are defined (REQ-HFPX-ADR-003). Estimate verification by analysis/CFD/test is downstream (06.19, 06.20) and not claimed here. Validation: acceptance that the drag-data chain to budgets is complete at SRR.

## 14. Risks

- Drag underestimated early, invalidating energy/endurance budgets (ISS-007) — mitigation: schema discipline plus maturity-gated updates per REQ-HFPX-ADR-002
- Interference drag unaccounted across pilot/modules/body — mitigation: contributor row plus 06.7 linkage per REQ-HFPX-ADR-001
- Stale drag data feeding budgets — mitigation: update rule with gates TBD

## 15. Open Issues

Drag-buildup values, methods, reference quantities, maturity gates, budget-feed timing, and estimation ownership TBD. ISS-007 budget actions pending first estimates.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on aerodynamic concept and contributor inputs (06.1–06.4, 06.6, 06.7), system requirements and SAD aero views (Vol 02), pilot/propulsion inputs (Vol 12, Vol 05), modelling/CFD/test capability (Vol 19, 06.19, 06.20), and budget actions (ISS-007).

## 18. Traceability

Parent: HFPX-SYS-REQ-001 (SYS-001), REQ-HFPX-MIS-002, REQ-HFPX-MIS-003, HFPX-SYS-ARC-001 SAD aero views. Children: ISS-007 energy/endurance budget inputs, 06.11 6-DOF model inputs, 06.13–06.15 regime assessments. RTM: REQ-HFPX-ADR-001..003 → CONCEPT, verification IDs TBD.

## 19. Configuration

BL-0.0. Tranche 5 draft, CONCEPT, not baselined.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 draft (Chapter 06.5) |
