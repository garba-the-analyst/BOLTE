# Ground Effects

**Document ID:** HFPX-AERO-GND-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define ground-effect treatment for HFP-X (Chapter 06.18): required ground-effect characterisation, modelling ownership, and validation by test.
This document owns requirements, interfaces, and verification methodology only.

## 2. Scope

Covers ground-effect characterisation affecting hover and landing (FAL thread; extents TBD), modelling ownership and method (TBD), and validation by test (scope and criteria TBD).
Out of scope: hover and landing control implementation (Vol 06.12, Vol 07, FAL thread), undercarriage and airframe implementation (Vol 03), and test execution (Vol 23).

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (SYS-001/008); PRF tier (details TBD)
- HFPX-PGM-SEM-001 SEMP; HFPX-VV-PLN-001 V&V Plan
- Sibling hooks: Vol 06.12 Hover Flight, Vol 06.8 Stability; FAL thread (hover and landing; details TBD)
- Vol 19 modelling support; Vol 23 test execution (gated, methodology only here)

## 4. Definitions & Acronyms

- Ground effect: alteration of aerodynamic forces, moments, and flows due to proximity to the ground; characterisation TBD.
- FAL thread: flight-phase thread covering hover and landing as applicable to ground effect; scope TBD.
- Ground-effect model: representation of ground-effect corrections for use in analysis and simulation; ownership and form TBD.
- Validation by test: confirmation of ground-effect characterisation against measured data; scope and criteria TBD.

## 5. System Context

Ground effect directly affects the limiting hover and landing cases: uncharacterised ground effect leaves thrust, attitude, and touchdown behaviour unbounded in the regime where margins are smallest.
No ground-effect behaviour is claimed in this revision; characterisation, modelling, and validation are all TBD.
This document constrains what must be characterised, who models it, and how it is validated, without implementing control or structure.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-AGD-001 | The system shall characterise ground effect affecting hover and landing per the FAL thread, with extents and criteria TBD. | SYS-001/008 | Analysis |
| REQ-HFPX-AGD-002 | The system shall assign modelling ownership and method for ground effect, with owner, form, and fidelity TBD. | SYS-001/008 | Inspection |
| REQ-HFPX-AGD-003 | Ground-effect characterisation shall be validated by test, with scope and pass criteria TBD. | SYS-001/008 | Test |

## 7. Architecture

Ground-effect architecture (details TBD): characterisation record TBD, model ownership TBD, validation thread TBD.
Characterisation dimensions TBD (height dependence, attitude dependence, surface dependence, configuration dependence; all TBD).
Model form TBD (table, correction function, or coupled simulation; selection TBD).

## 8. Detailed Design

Characterisation is a stub in this revision (extents TBD, conditions TBD, criteria TBD).
Modelling ownership and method are stubs (owner TBD, form TBD, fidelity TBD, update authority TBD).
Validation thread is methodology only (test types TBD, configurations TBD, criteria TBD).
No ground-effect value, correction, or margin is baselined in this revision.

## 9. Interfaces

- GND ↔ Hover / landing threads (Vol 06.12, FAL thread): affected conditions and acceptance needs; scope TBD.
- GND ↔ Stability and control (Vol 06.8, Vol 07): model inputs for control assessment; form and fidelity TBD.
- GND ↔ Airframe / undercarriage (Vol 03): geometric and configuration context; details TBD.
- GND ↔ Modelling (Vol 19) and flight test (Vol 23): model development and validation allocation; scope TBD.

## 10. Operational Concept

Ground-effect concept (methodology only): characterise affecting conditions (extents TBD) → assign and build model per ownership TBD → validate by test (scope TBD).
This concept defines analysis allocation and validation flow only; it does not direct vehicle handling, flight conduct, or test execution (owned and gated under Vol 23/CONOPS).

## 11. Safety

Hazardous-subsystem boundary: this document contains requirements, characterisation scope, interfaces, and verification methodology only; it contains no propulsion build, ignition, or operation instructions.
No hover or landing outcome in ground effect is asserted; touchdown and low-hover behaviour is unproven at this revision (criteria TBD).
Uncharacterised ground effect is treated as an open safety input to Vol 13 (scope TBD).

## 12. Performance

All ground-effect performance values TBD with no thresholds baselined: effect magnitudes TBD, height-dependence TBD, attitude sensitivity TBD, touchdown dispersions TBD.
No numerical performance requirement is set in this revision.

## 13. Verification & Validation

- REQ-HFPX-AGD-001 verified by Analysis of ground-effect characterisation coverage against hover and landing conditions (extents and criteria TBD).
- REQ-HFPX-AGD-002 verified by Inspection of the modelling ownership and method assignment (completeness criteria TBD).
- REQ-HFPX-AGD-003 verified by Test of ground-effect characterisation against measured data; test types, configurations, and pass criteria TBD; human-flight credit gated on closure (criteria TBD).
- Validation is gate review of characterisation, model, and validation-thread adequacy (scope TBD).

## 14. Risks

- Characterisation left TBD while hover and landing threads advance; mitigation: characterisation action tracked at reviews with FAL-thread impact stated.
- Model ownership unassigned, producing divergent ground-effect representations; mitigation: single ownership assignment required before model use (owner TBD).
- Test validation deferred indefinitely; mitigation: gated-test requirement with scope TBD enforced at reviews.

## 15. Open Issues

Ground-effect extents, conditions, and criteria TBD. Model owner, form, fidelity, and update authority TBD. Validation test types, configurations, and pass criteria TBD. FAL-thread acceptance needs TBD. Human-flight gating criteria TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SYS-001/008, PRF tier, Vol 06.12 / 06.8 (aerodynamic context), FAL thread (hover and landing acceptance), Vol 03 (geometric context), Vol 07 (control use of model), Vol 19 (modelling capability), SEMP / V&V Plan (gates and discipline), Vol 23 (test execution).

## 18. Traceability

Parents: SYS-001/008, PRF tier. Children: characterisation record, ground-effect model, and validation cases (artefact IDs TBD).
RTM: REQ-HFPX-AGD-001..003 → CONCEPT. Each affecting condition traces to at least one characterisation element; each characterisation element traces to at least one validation case (all TBD except IDs).

## 19. Configuration

BL-0.0 (structure only) — Tranche 5 draft, not baselined. Characterisation, model, and validation content is under document control once populated; changes via change records with affected-condition impact stated.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 draft (ground effects; Ch 06.18) |
