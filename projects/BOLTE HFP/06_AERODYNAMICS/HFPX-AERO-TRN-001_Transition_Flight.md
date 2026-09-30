# Transition Flight

**Document ID:** HFPX-AERO-TRN-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define transition-flight aerodynamic requirements for HFP-X. Owns Chapter 06.13.

## 2. Scope

Covers the transition corridor concept, corridor-determination method, failed-transition dynamics, transition-data requirements for FCS, and the no-transition-attempt rule. Excludes FCS detailed design (Vol 07 / 07.12), 6-DOF implementation (Vol 19.3), and test execution (Vol 23). All boundaries, methods detail, and criteria are TBD.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (SYS-001)
- HFPX-SYS-MIS-002 Mission Definition (MIS-002)
- HFPX-SYS-CON-001 CONOPS; HFPX-SYS-CON-003 (transition scenarios)
- HFPX-SYS-ARC-001 SAD — control view, aero view
- Vol 06 Chapters 06.8 / 06.11 / 06.12 / 06.14; Vol 07 Flight Control (including 07.12); Vol 19.3 / 19.15; Vol 23 Test
- ISS-006 (transition authority), ISS-007 actions

## 4. Definitions & Acronyms

- Transition: conversion between hover and horizontal flight (direction, conditions TBD)
- Reverse transition: conversion from horizontal flight back to hover / landing (conditions TBD)
- Transition corridor: allowable region for transition attempts (boundaries TBD)
- Failed transition: inability to complete or safely abort conversion (behaviour TBD)

## 5. System Context

Transition is the highest-risk CONOPS segment and the ISS-006 focus. Aerodynamics, propulsion, FCS law-switching (Vol 07 / 07.12), and 6-DOF evidence (Chapter 06.11 / Vol 19.3) must jointly close the corridor before any attempt. No corridor, authority, or feasibility is claimed at CONCEPT.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-ATN-001 | A transition corridor concept shall be defined, with corridor boundaries, entry / exit conditions, and abort criteria TBD. | HFPX-SYS-CON-003, HFPX-SYS-MIS-002, ISS-006 | Inspection |
| REQ-HFPX-ATN-002 | The corridor-determination method (6-DOF plus simulation, conditions TBD) shall be defined, with tools, inputs, and acceptance logic TBD. | HFPX-SYS-ARC-001, ISS-006 | Analysis |
| REQ-HFPX-ATN-003 | Failed-transition dynamics (detection, response, safe-state behaviour) shall be characterised, with thresholds and behaviours TBD. | HFPX-SYS-CON-003, ISS-006 | Analysis |
| REQ-HFPX-ATN-004 | Transition-data requirements for FCS (Vol 07.12) shall be defined, with data content, formats, and ownership TBD. | HFPX-SYS-ARC-001 | Inspection |
| REQ-HFPX-ATN-005 | No transition attempt shall be made before corridor evidence is gated per Vol 19.15 and demonstrated by unmanned test, with gate criteria TBD. | HFPX-SYS-CON-001, HFPX-SYS-CON-003, ISS-006 | Test |

## 7. Architecture

Transition assessment chains corridor concept → 6-DOF / simulation determination → FCS data delivery (07.12) → 19.15 gating → unmanned demo. Failed-transition dynamics feed CONOPS off-nominal threads and Vol 13 safety analyses. No corridor or law is baselined.

## 8. Detailed Design

Corridor parameters, simulation matrices, aerodynamic / thrust inputs (all TBD per Chapter 06.11 / Vol 04 / Vol 07), law-switching definitions (TBD, Vol 07), and abort logic (TBD) are undefined at CONCEPT. No boundaries, speeds, attitudes, or control settings are stated.

## 9. Interfaces

Interfaces to Chapter 06.11 model structure, Chapters 06.12 / 06.14 (hover / horizontal boundaries TBD), Vol 07 including 07.12 (law-switching and data needs TBD), Vol 19.3 (simulation TBD), Vol 19.15 (gates TBD), and Vol 23 (unmanned demo TBD). Definitions are TBD.

## 10. Operational Concept

CONOPS transition and reverse-transition scenarios (entry/exit, law switching, abort) are placeholders implemented by this corridor logic. Attempt, continuation, and abort decisions are gated by REQ-HFPX-ATN-005; all scenario values remain TBD.

## 11. Safety

Transition attempt without corridor evidence is prohibited by REQ-HFPX-ATN-005. Failed-transition behaviour drives FHA inputs (Vol 13.4, TBD) and range-safety constraints (Vol 23, TBD). No flight authorisation is given.

## 12. Performance

Transition performance (corridor width, conversion capability, control remaining) is TBD. No values are stated or implied.

## 13. Verification & Validation

Verified by analysis and simulation (method TBD) plus unmanned demonstration per Vol 23 (conditions TBD), gated by Vol 19.15 (criteria TBD). Human-carrying transition remains gated per CONOPS DDR-001 (criteria TBD).

## 14. Risks

- Authority shortfall mid-corridor (ISS-006 core risk); mitigation: corridor method plus no-attempt rule
- Law-switching transient (Vol 07 TBD); mitigation: 07.12 data requirements defined before control claims
- Evidence–test gap (simulation TBD vs demo TBD); mitigation: dual gate (19.15 plus unmanned demo)

## 15. Open Issues

ISS-006 (primary), ISS-007 (thrust interface), ISS-008 (recovery). New TBDs: corridor boundaries, determination method detail, failed-transition characterisation, 07.12 data set, gate criteria and demo plan.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SYS-001, MIS-002, CON-001 / CON-003, SAD control / aero views, Chapters 06.8 / 06.11 / 06.12 / 06.14, Vol 04, Vol 07 (including 07.12), Vol 19.3 / 19.15, Vol 23, and ISS-006 / ISS-007 actions.

## 18. Traceability

Parent: SYS-001, MIS-002, CON-001 / CON-003, SAD control / aero views, ISS-006 / ISS-007 actions. Children: Vol 07.12 data requirements, 19.15 gate evidence, unmanned transition-test cases. RTM: REQ-HFPX-ATN-001..005 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 5 draft, CONCEPT, not baselined.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 draft (Chapter 06.13) |
