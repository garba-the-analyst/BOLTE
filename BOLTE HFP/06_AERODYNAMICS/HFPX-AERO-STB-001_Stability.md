# Stability

**Document ID:** HFPX-AERO-STB-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the stability assessment scope for HFP-X across all flight modes. Owns Chapter 06.8.

## 2. Scope

Covers static and dynamic stability assessment scope for hover, transition, and horizontal flight of the unmanned demonstrator. Excludes detailed static-stability analysis (Chapter 06.9), dynamic-stability analysis (Chapter 06.10), 6-DOF implementation (Chapter 06.11 / Vol 19.3), and flight-control design (Vol 07).

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (SYS-001)
- HFPX-SYS-MIS-002 Mission Definition (MIS-002)
- HFPX-SYS-CON-001 CONOPS; HFPX-SYS-CON-003 (transition scenarios)
- HFPX-SYS-ARC-001 SAD — control view, aero view
- Vol 06 Chapters 06.9–06.11; Vol 07 Flight Control; Vol 19.3 / 19.15 (modelling and gating)
- ISS-006 (transition authority), ISS-007 (propulsion / thrust budget) actions

## 4. Definitions & Acronyms

- Static stability: tendency to return toward trim after a disturbance (criteria TBD)
- Dynamic stability: time response of disturbed motion, including modal behaviour (criteria TBD)
- 6-DOF: six-degree-of-freedom flight model
- TBD: to be determined; TBC: to be confirmed

## 5. System Context

Stability assessment constrains the air-vehicle configuration (SYS-01 aerodynamics / structures / propulsion integration) and bounds what the flight-control system (Vol 07 / SAD control view) may assume. All stability data, boundaries, and criteria are TBD at this revision.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-ASB-001 | Stability assessment shall cover static stability and dynamic stability in all flight modes (hover, transition, horizontal flight), with mode-specific scope TBD. | HFPX-SYS-CON-001, HFPX-SYS-MIS-002 | Inspection |
| REQ-HFPX-ASB-002 | Stability assessment input-data requirements (geometry, mass properties, aerodynamic tables, propulsion effects) shall be defined, with all data TBD. | HFPX-SYS-REQ-001, HFPX-SYS-ARC-001 | Inspection |
| REQ-HFPX-ASB-003 | Any identified instability shall require a recorded design change or operational limitation before progression, with disposition TBD. | HFPX-SYS-REQ-001, ISS-006 | Analysis |
| REQ-HFPX-ASB-004 | Stability claims shall be verified by analysis and test, with methods and success criteria TBD. | HFPX-SYS-CON-003, HFPX-SYS-ARC-001 | Analysis + Test |

## 7. Architecture

Stability scope decomposes into static assessment (Chapter 06.9), dynamic assessment (Chapter 06.10), and 6-DOF equation structure (Chapter 06.11). Results feed the SAD aero view and the Vol 07 FCS-augmentation interface. No stability architecture beyond this decomposition is defined at CONCEPT.

## 8. Detailed Design

Assessment scope includes trim conditions (TBD), disturbance definitions (TBD), and response evaluation (TBD) for each flight mode. Assessment inputs, tools, and data sources are TBD. No stability boundaries, coefficients, or criteria values are defined in this document.

## 9. Interfaces

Interfaces to Vol 06 Chapters 06.9 / 06.10 / 06.11 (detailed analyses and model), Vol 07 (FCS augmentation needs), Vol 19.3 (model implementation), and SAD control / aero views. Interface data and formats are TBD.

## 10. Operational Concept

Stability assessment underpins CONOPS nominal and off-nominal threads (hover, transition, cruise): no thread is claimed stable until assessed per REQ-HFPX-ASB-001 and verified per REQ-HFPX-ASB-004. Entry/exit conditions and abort criteria remain TBD.

## 11. Safety

Unassessed or unstable behaviour is treated as a constraint on flight (ISS-006). No hazardous test or operation is authorised by this document; test methodology lives in Vol 23 under gated progression.

## 12. Performance

Stability performance (boundaries, damping, margins) is TBD. No performance values are stated or implied.

## 13. Verification & Validation

Verified by analysis (scope coverage, data-requirements completeness) and test (correlation per Vol 23, criteria TBD). Human-carrying progression is gated per CONOPS and Vol 19.15 (criteria TBD).

## 14. Risks

- Transition-authority shortfall (ISS-006); mitigation: scoped assessment plus 6-DOF-gated corridor evidence
- Stability–FCS mismatch (control assumes stability the airframe lacks); mitigation: Vol 07 interface definition TBD
- Data immaturity (all inputs TBD); mitigation: explicit TBD tracking, no unverified claims

## 15. Open Issues

ISS-006 (transition authority), ISS-007 (thrust budget interface). New TBDs: assessment methods, input-data tables, instability disposition process, verification criteria.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SyRS (SYS-001), Mission (MIS-002), CONOPS threads (CON-001 / CON-003), SAD control / aero views, Vol 07 FCS architecture, Chapters 06.9–06.11 inputs, Vol 19.3 modelling, and ISS-006 / ISS-007 actions.

## 18. Traceability

Parent: SYS-001, MIS-002, CON-001 / CON-003, SAD control / aero views, ISS-006 / ISS-007 actions. Children: Chapters 06.9–06.11 detailed requirements, Vol 07 augmentation requirements, V&V cases. RTM: REQ-HFPX-ASB-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 5 draft, CONCEPT, not baselined.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 draft (Chapter 06.8) |
