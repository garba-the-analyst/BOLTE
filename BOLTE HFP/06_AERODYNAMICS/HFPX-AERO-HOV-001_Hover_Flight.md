# Hover Flight

**Document ID:** HFPX-AERO-HOV-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define hover-flight aerodynamic requirements for HFP-X. Owns Chapter 06.12.

## 2. Scope

Covers hover aerodynamic environment, thrust-to-weight placeholder, hover-efficiency factors, and hover-model validation. Excludes propulsion detailed design (Vol 04), FCS hover laws (Vol 07), and ground-effect detail (Chapter 06.18). All values, environments, and criteria are TBD.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (SYS-001)
- HFPX-SYS-MIS-002 Mission Definition (MIS-002)
- HFPX-SYS-CON-001 CONOPS; HFPX-SYS-CON-003
- HFPX-SYS-ARC-001 SAD — control view, aero view
- Vol 06 Chapters 06.7 / 06.8 / 06.11 / 06.18; Vol 04 Propulsion; Vol 07 Flight Control; Vol 19.3 / 19.15; Vol 23 Test
- ISS-006, ISS-007 (thrust budget) actions

## 4. Definitions & Acronyms

- Hover: sustained flight with no translational velocity demand (tolerances TBD)
- Downwash: propulsion-induced downward flow (characterisation TBD)
- Recirculation: re-ingestion / ground-interaction of induced flow (characterisation TBD)
- Thrust-to-weight: hover thrust relative to weight (value TBD, budget owned by ISS-007 action)

## 5. System Context

Hover is the CONOPS entry flight mode (ground idle → hover → hover manoeuvre) and the limiting low-altitude safety case. Hover aerodynamics couple airframe, propulsion-airframe interaction (Chapter 06.7), ground effects (Chapter 06.18), and FCS hover laws (Vol 07). All environments and budgets are TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-AHV-001 | The hover aerodynamic environment shall be characterised (downwash, recirculation, interaction effects), with definitions, conditions, and data TBD. | HFPX-SYS-REQ-001, HFPX-SYS-MIS-002 | Analysis |
| REQ-HFPX-AHV-002 | A hover thrust-to-weight requirement placeholder shall be defined, with value TBD and budget ownership under the ISS-007 action. | HFPX-SYS-REQ-001, ISS-007 | Inspection |
| REQ-HFPX-AHV-003 | Hover-efficiency factors (losses, interactions, installation effects) shall be identified, with definitions and values TBD. | HFPX-SYS-ARC-001, ISS-007 | Analysis |
| REQ-HFPX-AHV-004 | The hover aerodynamic model shall be validated by unmanned test, with test conditions, methods, and success criteria TBD. | HFPX-SYS-CON-001, ISS-006 | Test |

## 7. Architecture

Hover assessment comprises environment characterisation, thrust-budget placeholder, efficiency-factor capture, and unmanned-test validation. Inputs come from Chapter 06.11 structure, Vol 04 thrust data (TBD), and Chapter 06.18 ground effects. Outputs feed SAD aero view and Vol 07 hover-law needs.

## 8. Detailed Design

Environment definitions, measurement planes, test matrices, efficiency breakdowns, and thrust-budget tables are TBD. No downwash velocities, recirculation boundaries, efficiency values, or thrust values are stated.

## 9. Interfaces

Interfaces to Vol 04 (thrust maps TBD), Vol 07 (hover control allocation TBD), Chapters 06.7 / 06.11 / 06.18 (interaction, model, ground effect TBD), Vol 19.3 (simulation TBD), and Vol 23 (unmanned hover test TBD). Formats are TBD.

## 10. Operational Concept

Hover threads per CONOPS (lift to hover, hover manoeuvre box) assume TBD hover characteristics. Abort-to-hover and emergency-stabilisation behaviours reference TBD data. No hover envelope, duration, or manoeuvre is cleared.

## 11. Safety

Low-altitude hover is the limiting safety case; uncharacterised downwash / recirculation effects are treated as constraints. No hover flight is authorised by this document; Vol 13 analyses and Vol 23 gating apply.

## 12. Performance

Hover performance (payload, endurance, control remaining in hover) is TBD. No values are stated or implied.

## 13. Verification & Validation

Verified by analysis (environment and efficiency capture TBD) and unmanned test per Vol 23 (conditions and criteria TBD). Gating per Vol 19.15 applies before any progression.

## 14. Risks

- Thrust shortfall vs TBD demand (ISS-007); mitigation: placeholder budget tracked under ISS-007 action, no flight claim until closed
- Recirculation / ground-interaction surprise (Chapter 06.18 TBD); mitigation: environment characterisation before envelope definition
- Model–test mismatch; mitigation: unmanned-test validation gate REQ-HFPX-AHV-004

## 15. Open Issues

ISS-006 (hover-to-transition handover), ISS-007 (thrust budget). New TBDs: environment data, thrust-to-weight value, efficiency factors, validation test plan and criteria.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SYS-001, MIS-002, CON-001 / CON-003, SAD control / aero views, Chapters 06.7 / 06.8 / 06.11 / 06.18, Vol 04, Vol 07, Vol 19.3 / 19.15, Vol 23, and ISS-006 / ISS-007 actions.

## 18. Traceability

Parent: SYS-001, MIS-002, CON-001 / CON-003, SAD control / aero views, ISS-006 / ISS-007 actions. Children: Vol 04 thrust-budget requirements, Vol 07 hover-law requirements, unmanned hover-test cases. RTM: REQ-HFPX-AHV-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 5 draft, CONCEPT, not baselined.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 draft (Chapter 06.12) |
