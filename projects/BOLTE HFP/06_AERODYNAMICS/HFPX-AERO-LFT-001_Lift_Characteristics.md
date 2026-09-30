# Lift Characteristics

**Document ID:** HFPX-AERO-LFT-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the lift-characteristics scope at structure-only level before any lift data exists. Owns Chapter 06.6 and establishes the lift-table schema, the stall/separation characterisation obligation, and the feed from lift data into the 6-DOF model and programme budgets.

## 2. Scope

Covers lift characteristics across hover, transition, and horizontal flight for whatever airframe family the ISS-004 trade retains. All lift values, coefficients, reference quantities, attitudes, speeds, and altitudes are TBD. Drag buildup is owned by 06.5; stability derivatives are owned by 06.8–06.10; the 6-DOF formulation is owned by 06.11. This document defines schema and process only.

## 3. Applicable Documents

- HFPX-SYS-MIS-001 Mission Definition; HFPX-SYS-REQ-001 SyRS (stub); HFPX-SYS-ARC-001 SAD (stub)
- HFPX-AERO-CON-001 Aerodynamic Concept (06.1); Volume 06 chapters 06.2–06.5, 06.7, 06.8–06.11, 06.19, 06.20
- Vol 19 Modelling & Simulation; ISS-007 budget actions (energy/endurance budgets)
- HFP Documentation schema (Vol 01)

## 4. Definitions & Acronyms

- Lift table: structured tabulation of lift versus flight condition; schema defined here, all values TBD, including coefficients TBD and reference quantities TBD
- Stall/separation: loss or breakdown of attached-flow lift requiring characterisation; results TBD
- Conceptual relation L + Tv ≈ W stated qualitatively only; full 6-DOF equations apply to detailed modelling (06.11), structure only here, no numeric coefficients
- ISS-007: budgets and feasibility actions fed in part by lift data

## 5. System Context

Lift characterisation sits between aerodynamic definition (06.1–06.4, 06.7) and consumers: 6-DOF model (06.11), stability assessments (06.8–06.10), regime performance (06.12–06.15), and ISS-007 budgets. Sources of lift data (analysis/CFD/test) are TBD across Vol 19, 06.19, and 06.20. Environments and envelopes: all TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-ALI-001 | HFP-X lift data shall use a defined lift-table schema with all lift values, coefficients, reference quantities, conditions, and methods TBD. | HFPX-SYS-REQ-001, HFPX-SYS-ARC-001 SAD aero views | Inspection |
| REQ-HFPX-ALI-002 | HFP-X lift characteristics shall include stall and separation characterisation with results and method TBD. | HFPX-SYS-REQ-001 | Analysis |
| REQ-HFPX-ALI-003 | HFP-X lift data shall feed the 6-DOF model (06.11) and programme budgets with feed content and timing TBD. | REQ-HFPX-MIS-002, REQ-HFPX-MIS-003, HFPX-SYS-REQ-001 | Inspection |

No coefficient, area, attitude, speed, altitude, mass, or thrust figure is stated or implied in the schema.

## 7. Architecture

Lift work packages: schema definition (this document) → attached-flow tables per regime (TBD) → stall/separation characterisation (TBD) → 6-DOF and budget feeds (TBD). Lift tables are versioned artefacts updated with design maturity; estimation ownership (analysis/CFD/test) is TBD.

## 8. Detailed Design

Not applicable — schema only, no data. Lift-table schema:

| Condition / regime | Lift quantity | Coefficient | Reference quantity | Method | Status |
| --- | --- | --- | --- | --- | --- |
| TBD | TBD | TBD | TBD | TBD | TBD |
| Stall / separation entry | TBD | TBD | TBD | TBD | TBD |

All cells TBD. No lift value, coefficient, reference quantity, condition, or method is stated or implied.

## 9. Interfaces

- Upstream: aerodynamic concept (06.1), lifting-body/wing/surface outputs (06.2–06.4), interaction effects (06.7), system requirements (SYS-001), SAD aero views
- Downstream: 06.8–06.10 stability, 06.11 6-DOF model, 06.12–06.15 regime performance, ISS-007 budgets
- External: modelling/CFD/test capability (Vol 19, 06.19, 06.20)

## 10. Operational Concept

Summary only; detail in CONOPS: lift tables, once populated, support unmanned-first envelope expansion from hover through transition to horizontal flight, including recognition of stall/separation boundaries once characterised. No operational envelope or handling claim is stated here.

## 11. Safety

No lift data in this document supports any flight-clearance or envelope claim. Uncharacterised stall/separation is a loss-of-control hazard; mitigation is the characterisation obligation (REQ-HFPX-ALI-002) owned with Vol 13 once candidates exist. Hazardous-subsystem boundary applies: this document contains no build, ignition, or operation instructions for high-energy propulsion.

## 12. Performance

All lift performance values TBD. No lift force, coefficient, reference quantity, stall boundary, speed, altitude, endurance, or range figure is stated or implied. Budget and 6-DOF impact is assessed only once data exists.

## 13. Verification & Validation

Requirements verified by: review of schema completeness (REQ-HFPX-ALI-001), review that stall/separation characterisation is planned (REQ-HFPX-ALI-002), and review that 6-DOF and budget feeds are defined (REQ-HFPX-ALI-003). Data verification by analysis/CFD/test is downstream (06.19, 06.20) and not claimed here. Validation: acceptance that the lift-data chain to the 6-DOF model and budgets is complete at SRR.

## 14. Risks

- Lift overestimated early, invalidating budgets and 6-DOF predictions — mitigation: schema discipline plus maturity-gated updates feeding ISS-007
- Stall/separation uncharacterised, hiding loss-of-control boundaries — mitigation: REQ-HFPX-ALI-002 obligation before envelope expansion
- Stale lift data feeding the 6-DOF model — mitigation: versioned tables with feed timing TBD

## 15. Open Issues

Lift-table values, coefficients, reference quantities, stall/separation method and results, feed timing, and estimation ownership TBD. ISS-007 budget actions pending first data.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on aerodynamic concept and contributor inputs (06.1–06.4, 06.7), system requirements and SAD aero views (Vol 02), stability and 6-DOF needs (06.8–06.11), modelling/CFD/test capability (Vol 19, 06.19, 06.20), and budget actions (ISS-007).

## 18. Traceability

Parent: HFPX-SYS-REQ-001 (SYS-001), REQ-HFPX-MIS-002, REQ-HFPX-MIS-003, HFPX-SYS-ARC-001 SAD aero views. Children: 06.8–06.10 stability inputs, 06.11 6-DOF model inputs, 06.12–06.15 regime assessments, ISS-007 budget inputs. RTM: REQ-HFPX-ALI-001..003 → CONCEPT, verification IDs TBD.

## 19. Configuration

BL-0.0. Tranche 5 draft, CONCEPT, not baselined.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 draft (Chapter 06.6) |
