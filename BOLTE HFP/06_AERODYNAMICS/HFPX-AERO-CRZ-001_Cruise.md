# Cruise

**Document ID:** HFPX-AERO-CRZ-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the cruise flight regime for HFP-X (Chapter 06.15): cruise force and energy balance, cruise-efficiency factors, cruise envelope, and the feed of cruise data into endurance budgets.
This document owns requirements, budget table schemas, interfaces, and verification methodology only.

## 2. Scope

Covers cruise force and energy balance definition (values TBD), cruise-efficiency factors (set TBD), cruise-envelope definition (bounds TBD), and the rule by which cruise data feeds endurance budgets.
Out of scope: horizontal-flight and transition-law implementation (Vol 06.14 / 06.13, Vol 07), propulsion and fuel-system sizing (Vol 04 / Vol 05), and test execution (Vol 23).

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (SYS-001/008); mission thread MIS-007; PRF tier (details TBD)
- HFPX-PGM-SEM-001 SEMP; HFPX-VV-PLN-001 V&V Plan
- Sibling hooks: Vol 06.5 Aerodynamic Drag, Vol 06.6 Lift Characteristics, Vol 06.7 Propulsion-Airframe Interaction, Vol 06.14 Horizontal Flight (values TBD)
- Vol 19 analysis support; Vol 23 test execution (gated, methodology only here)

## 4. Definitions & Acronyms

- Cruise: sustained forward-flight regime between transition exit and transition entry; speed, altitude, and configuration bounds TBD.
- Cruise force balance: equilibrium of thrust, drag, lift, and weight in cruise; terms and values TBD.
- Cruise energy balance: accounting of energy source, conversion, and expenditure over cruise; terms and values TBD.
- Cruise-efficiency factors: parameters governing cruise energy cost per unit range or endurance; set and values TBD.
- Cruise envelope: conditions within which cruise is specified; bounds TBD.
- Endurance budget: allocation of mass, thrust, and energy against required endurance; values TBD.

## 5. System Context

Cruise connects aerodynamic characterisation to programme endurance claims: cruise force and energy balance determines thrust required and energy expended, which flows into mass, thrust, and energy budgets owned in this chapter schema.
Endurance performance is unproven at this revision; no endurance outcome is claimed until verified per REQ-HFPX-ACZ-004 (criteria TBD).
This document constrains budget structure and data-feed rules without sizing propulsion, fuel, or structure.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-ACZ-001 | The system shall define the cruise force and energy balance, with all terms and values TBD. | SYS-001/008, MIS-007, PRF tier | Analysis |
| REQ-HFPX-ACZ-002 | The system shall define cruise-efficiency factors, with factor set and values TBD. | SYS-001/008, MIS-007, PRF tier | Analysis |
| REQ-HFPX-ACZ-003 | The system shall define the cruise envelope, with all bounds TBD. | SYS-001/008, MIS-007, PRF tier | Analysis |
| REQ-HFPX-ACZ-004 | Cruise data shall feed endurance budgets per the budget schemas in §12, with feed rule and acceptance criteria TBD. | SYS-001/008, MIS-007, PRF tier | Inspection |

## 7. Architecture

Cruise analysis architecture (details TBD): force and energy balance model TBD, efficiency-factor set TBD, envelope statement TBD, budget-schema ownership TBD.
Balance model structure TBD; efficiency-factor derivation path TBD (Vol 19 support).
Envelope bounds TBD; relationship to transition and high-speed regimes TBD.

## 8. Detailed Design

Balance definition is a stub in this revision (all terms and values TBD; no aerodynamic coefficients, thrust values, or energy figures baselined).
Efficiency-factor set is a stub (factors TBD, derivation TBD).
Envelope definition is a stub (bounds TBD, configuration TBD).
Budget schemas are defined in §12; the first issue of populated budgets is an action owned by this document (owners TBD, values TBD, due gate TBD). No sizing decision is made in this revision.

## 9. Interfaces

- CRZ ↔ Drag / lift characterisation (Vol 06.5 / 06.6): coefficient and polar inputs; tables and uncertainties TBD.
- CRZ ↔ Propulsion-airframe interaction (Vol 06.7): installed thrust and interaction corrections; values TBD.
- CRZ ↔ Propulsion / fuel (Vol 04 / Vol 05): thrust available and energy available inputs to budgets; values TBD.
- CRZ ↔ Mass properties (Vol 03): empty mass and payload inputs to budgets; values TBD.
- CRZ ↔ Endurance claimants (MIS-007, PRF tier): budget outputs and feed rule; criteria TBD.

## 10. Operational Concept

Cruise concept (methodology only): establish balance terms (values TBD) → derive efficiency factors (values TBD) → bound the cruise envelope (bounds TBD) → populate budget schemas (values TBD) → feed endurance budgets per REQ-HFPX-ACZ-004.
This concept defines analysis allocation and data flow only; it does not direct vehicle handling, flight conduct, or test execution (owned and gated under Vol 23/CONOPS).

## 11. Safety

Hazardous-subsystem boundary: this document contains requirements, budget schemas, interfaces, and verification methodology only; it contains no propulsion build, ignition, or operation instructions.
No safe-flight or endurance outcome is asserted in this revision; cruise-dependent safety claims trace to future verified budgets (criteria TBD).
Envelope exceedance handling is defined elsewhere (Vol 07 / Vol 13, details TBD).

## 12. Performance

All cruise performance values TBD with no thresholds baselined: balance residuals TBD, efficiency factors TBD, envelope bounds TBD, endurance TBD.
Budget table schemas (all values TBD; directly attacking ISS-007 endurance-budget gap):

| Budget line | Value | Owner | Status |
| --- | --- | --- | --- |
| Empty mass | TBD | TBD | TBD |
| Pilot / payload mass | TBD | TBD | TBD |
| Fuel mass / energy carried | TBD | TBD | TBD |
| Thrust available | TBD | TBD | TBD |
| Thrust required (cruise) | TBD | TBD | TBD |
| Energy required (cruise) | TBD | TBD | TBD |
| Endurance derived from budgets | TBD | TBD | TBD |

Schema rules TBD: sign conventions TBD, configuration control TBD, update cadence TBD, first-issue action owned by this document (owners TBD, due gate TBD).
No budget value, margin, or threshold is set in this revision.

## 13. Verification & Validation

- REQ-HFPX-ACZ-001 verified by Analysis of the cruise force and energy balance definition (terms, coverage, and criteria TBD).
- REQ-HFPX-ACZ-002 verified by Analysis of cruise-efficiency factors against balance and sibling inputs (coverage TBD).
- REQ-HFPX-ACZ-003 verified by Analysis of the cruise-envelope definition (bounds and criteria TBD).
- REQ-HFPX-ACZ-004 verified by Inspection of the cruise-to-endurance-budget feed against §12 schemas (rule and criteria TBD).
- Validation is gate review of balance, envelope, and budget-schema adequacy (scope TBD).

## 14. Risks

- Balance terms left TBD indefinitely, blocking endurance budgets; mitigation: first-issue action owned here with TBD owners tracked at reviews.
- Efficiency factors disconnected from drag / lift / interaction inputs; mitigation: interface-trace check per review (criteria TBD).
- Unverified endurance treated as performance (ISS-007); mitigation: explicit unproven status and gated-budget requirement enforced at reviews.

## 15. Open Issues

Cruise force and energy balance terms and values TBD. Cruise-efficiency factor set and values TBD. Cruise-envelope bounds TBD. Budget values, owners, sign conventions, and update cadence TBD. Feed rule and acceptance criteria for REQ-HFPX-ACZ-004 TBD. ISS-007 applies to all endurance claims fed by this chapter.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SYS-001/008, MIS-007, PRF tier, Vol 06.5 / 06.6 / 06.7 / 06.14 (aerodynamic inputs), Vol 03 (mass context), Vol 04 / Vol 05 (thrust and energy context), Vol 19 (analysis capability), SEMP / V&V Plan (gates and discipline), Vol 23 (test execution).

## 18. Traceability

Parents: SYS-001/008, MIS-007, PRF tier. Children: balance definition, efficiency-factor set, envelope statement, populated budget issues, and verification cases (artefact IDs TBD).
RTM: REQ-HFPX-ACZ-001..004 → CONCEPT. Each balance term traces to at least one budget line; each budget line traces to at least one verification case (all TBD except IDs).

## 19. Configuration

BL-0.0 (structure only) — Tranche 5 draft, not baselined. Balance, envelope, and budget-schema content is under document control once populated; changes via change records with affected-budget impact stated.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 draft (cruise; Ch 06.15) |
