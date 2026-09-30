# Static Stability

**Document ID:** HFPX-AERO-SSB-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define static-stability assessment requirements for HFP-X. Owns Chapter 06.9.

## 2. Scope

Covers centre-of-gravity / centre-of-pressure relationship assessment, static-margin policy, and trim analysis across hover, transition, and horizontal flight. Excludes dynamic modal analysis (Chapter 06.10), 6-DOF implementation (Chapter 06.11), and FCS design (Vol 07). All positions, values, and criteria are TBD.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (SYS-001)
- HFPX-SYS-MIS-002 Mission Definition (MIS-002)
- HFPX-SYS-CON-001 CONOPS; HFPX-SYS-CON-003
- HFPX-SYS-ARC-001 SAD — control view, aero view
- Vol 06 Chapters 06.8 / 06.11; Vol 07 Flight Control; Vol 19.3 / 19.15
- ISS-006 (transition authority), ISS-007 actions

## 4. Definitions & Acronyms

- CG: centre of gravity (position TBD)
- CP: centre of pressure (position TBD)
- Static margin: static-stability policy parameter (definition and values TBD)
- Trim: equilibrium condition for a flight mode (conditions TBD)

## 5. System Context

Static stability bounds the allowable CG / CP relationship and trim capability that structures, mass-properties, aerodynamics, and propulsion integration must jointly satisfy. Results constrain the SAD aero view and Vol 07 trim / augmentation assumptions. All data are TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-ASS-001 | Static-stability assessment shall evaluate the CG / CP relationship in all flight modes, with CG positions, CP positions, and evaluation conditions TBD. | HFPX-SYS-REQ-001, HFPX-SYS-MIS-002 | Analysis |
| REQ-HFPX-ASS-002 | A static-margin policy shall be defined, with definitions, applicability, and values TBD. | HFPX-SYS-REQ-001, HFPX-SYS-ARC-001 | Inspection |
| REQ-HFPX-ASS-003 | Trim analysis shall be performed for all flight modes, with trim conditions, control settings, and acceptance criteria TBD. | HFPX-SYS-CON-001, HFPX-SYS-CON-003, ISS-006 | Analysis |

## 7. Architecture

Static-stability assessment comprises CG / CP evaluation, static-margin policy application, and trim analysis. Outputs feed Chapter 06.8 scope closure, Chapter 06.11 model inputs, and Vol 07 FCS interfaces. No further architecture is defined at CONCEPT.

## 8. Detailed Design

Assessment inputs (geometry, mass properties, aerodynamic tables, propulsion effects) are TBD. Assessment methods, tools, and data tables are TBD. No CG positions, CP positions, margins, deflections, or trim settings are stated.

## 9. Interfaces

Interfaces to mass-properties source (TBD), Chapters 06.5 / 06.6 aerodynamic tables (TBD), propulsion data per Vol 04 / Vol 07 (TBD), SAD aero view, and Vol 07 trim interface. Data formats and ownership are TBD.

## 10. Operational Concept

Trim and static-stability status condition whether CONOPS threads (hover, transition, horizontal flight) can be planned or flown. No operational trim settings or limitations are given; all are TBD pending analysis and test.

## 11. Safety

Untrimmed or statically unstable conditions are treated as constraints requiring design change or operational limitation per Chapter 06.8. No flight clearance is implied by this document.

## 12. Performance

Static-stability performance (margins, trim capability, control remaining) is TBD. No values are stated or implied.

## 13. Verification & Validation

Verified by analysis (assessment coverage, method TBD) with test correlation TBD (Vol 23). Success criteria are TBD. Gated progression per Vol 19.15 applies.

## 14. Risks

- CG / CP excursion outside assessable range (data TBD); mitigation: explicit TBD tracking and mass-properties control TBD
- Trim shortfall in transition (ISS-006); mitigation: trim analysis gates FCS interface definition
- Policy–design mismatch (policy TBD vs configuration TBD); mitigation: policy defined before design claims

## 15. Open Issues

ISS-006, ISS-007 interfaces. New TBDs: CG / CP data, static-margin definitions and values, trim conditions and criteria, verification method.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SYS-001, MIS-002, CON-001 / CON-003, SAD control / aero views, Chapters 06.5 / 06.6 / 06.8 / 06.11, Vol 04 / Vol 07 propulsion and control data, Vol 19.3 / 19.15, and ISS-006 / ISS-007 actions.

## 18. Traceability

Parent: SYS-001, MIS-002, CON-001 / CON-003, SAD control / aero views, ISS-006 / ISS-007 actions. Children: trim and margin verification cases, Vol 07 interface requirements. RTM: REQ-HFPX-ASS-001..003 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 5 draft, CONCEPT, not baselined.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 draft (Chapter 06.9) |
