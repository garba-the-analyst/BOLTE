# Horizontal Flight

**Document ID:** HFPX-AERO-HRZ-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define horizontal-flight aerodynamic requirements for HFP-X. Owns Chapter 06.14.

## 2. Scope

Covers horizontal-flight force balance, control allocation between aerodynamic surfaces and thrust, deceleration / reverse-transition dynamics, and verification. Excludes cruise detail (Chapter 06.15), high-speed detail (Chapter 06.16), FCS detailed design (Vol 07), and 6-DOF implementation (Vol 19.3). All balances, allocations, and criteria are TBD.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (SYS-001)
- HFPX-SYS-MIS-002 Mission Definition (MIS-002)
- HFPX-SYS-CON-001 CONOPS; HFPX-SYS-CON-003
- HFPX-SYS-ARC-001 SAD — control view, aero view
- Vol 06 Chapters 06.3–06.8 / 06.11 / 06.13; Vol 04 Propulsion; Vol 07 Flight Control; Vol 19.3 / 19.15
- ISS-006, ISS-007 actions

## 4. Definitions & Acronyms

- Horizontal flight: wing-borne / forward flight phase including acceleration, cruise interface, and deceleration (definitions TBD)
- Force balance: equilibrium of lift, drag, thrust, and weight components (conditions TBD)
- Control allocation: distribution of control demand between aerodynamic surfaces and thrust (logic TBD)
- Reverse-transition dynamics: behaviour during deceleration back toward hover (characterisation TBD)

## 5. System Context

Horizontal flight links transition exit (Chapter 06.13) to cruise (Chapter 06.15) and back to reverse transition and landing per CONOPS. Aerodynamic surfaces (Chapters 06.3 / 06.4), lift / drag tables (Chapters 06.5 / 06.6), propulsion (Vol 04), and FCS allocation (Vol 07) must jointly close the balance. All data are TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-AHZ-001 | The horizontal-flight force balance shall be defined, with conditions, contributions, and data TBD. | HFPX-SYS-REQ-001, HFPX-SYS-MIS-002 | Analysis |
| REQ-HFPX-AHZ-002 | Control allocation between aerodynamic surfaces and thrust shall be defined, with effectors, logic, and ownership TBD (Vol 07). | HFPX-SYS-ARC-001, ISS-006 | Inspection |
| REQ-HFPX-AHZ-003 | Deceleration and reverse-transition dynamics shall be characterised, with conditions, behaviours, and criteria TBD. | HFPX-SYS-CON-003, ISS-006 | Analysis |
| REQ-HFPX-AHZ-004 | Horizontal-flight aerodynamic claims shall be verified, with methods, conditions, and success criteria TBD. | HFPX-SYS-CON-001 | Analysis + Test |

## 7. Architecture

Horizontal-flight assessment comprises force-balance definition, allocation to surfaces / thrust via Vol 07, and deceleration characterisation feeding Chapter 06.13 reverse-transition logic. Analysis uses Chapter 06.11 structure with Chapters 06.5 / 06.6 and Vol 04 inputs (all TBD).

## 8. Detailed Design

Balance conditions, aerodynamic tables, thrust settings, allocation tables, and deceleration profiles are TBD. No lift, drag, thrust, speed, attitude, or deflection values are stated.

## 9. Interfaces

Interfaces to Chapters 06.3–06.6 (surfaces and tables TBD), Chapter 06.11 (model TBD), Chapter 06.13 (transition boundaries TBD), Vol 04 (thrust TBD), Vol 07 (allocation and laws TBD), and SAD control / aero views. Definitions are TBD.

## 10. Operational Concept

CONOPS horizontal-acceleration, cruise-interface, horizontal-deceleration, and reverse-transition threads assume TBD balances and allocations. No horizontal-flight envelope, manoeuvre, or landing approach is cleared.

## 11. Safety

Unbalanced or unallocated demands and uncharacterised deceleration behaviour are treated as constraints blocking progression. No flight authorisation is given; Vol 13 and Vol 23 gating apply.

## 12. Performance

Horizontal-flight performance (balances achieved, control remaining, deceleration capability) is TBD. No values are stated or implied.

## 13. Verification & Validation

Verified by analysis and simulation (TBD) with test correlation TBD (Vol 23, unmanned). Success criteria are TBD. Gating per Vol 19.15 applies.

## 14. Risks

- Allocation conflict (surfaces vs thrust demand exceeds TBD capability — ISS-006 / ISS-007); mitigation: allocation defined with Vol 07 before claims
- Deceleration / reverse-transition coupling surprise; mitigation: characterisation gates corridor definition
- Balance-data immaturity (tables TBD); mitigation: TBD-tracked inputs, no unverified balance claims

## 15. Open Issues

ISS-006, ISS-007 interfaces. New TBDs: force-balance data, allocation logic and ownership, deceleration characterisation, verification plan and criteria.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SYS-001, MIS-002, CON-001 / CON-003, SAD control / aero views, Chapters 06.3–06.8 / 06.11 / 06.13, Vol 04, Vol 07, Vol 19.3 / 19.15, and ISS-006 / ISS-007 actions.

## 18. Traceability

Parent: SYS-001, MIS-002, CON-001 / CON-003, SAD control / aero views, ISS-006 / ISS-007 actions. Children: Vol 07 allocation requirements, reverse-transition verification cases, cruise-interface inputs (06.15). RTM: REQ-HFPX-AHZ-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 5 draft, CONCEPT, not baselined.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 draft (Chapter 06.14) |
