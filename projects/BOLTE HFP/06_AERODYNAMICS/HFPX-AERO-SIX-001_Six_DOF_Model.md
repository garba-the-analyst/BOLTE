# Six-Degree-of-Freedom Model

**Document ID:** HFPX-AERO-SIX-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the six-degree-of-freedom (6-DOF) equation-of-motion structure for HFP-X and the input data it requires. Owns Chapter 06.11. This document defines structure only; all data are TBD and no coefficients are solved.

## 2. Scope

Covers 6-DOF force / moment summation structure, state-vector and control-vector definitions (structural only), required input-data enumeration, implementation ownership, claim limits for unverified models, and model-use rules at CONCEPT stage. Excludes solved aerodynamics (Chapters 06.5 / 06.6), thrust maps (Vol 04 / Vol 07), model implementation detail (Vol 19.3), and gating evidence (Vol 19.15). All data, tables, and parameters are TBD.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (SYS-001)
- HFPX-SYS-MIS-002 Mission Definition (MIS-002)
- HFPX-SYS-CON-001 CONOPS; HFPX-SYS-CON-003
- HFPX-SYS-ARC-001 SAD — control view, aero view
- Vol 06 Chapters 06.5 / 06.6 / 06.8–06.10 / 06.12–06.14; Vol 04 Propulsion; Vol 07 Flight Control (including 07.12)
- Vol 19.3 (model implementation ownership); Vol 19.15 (gating / evidence)
- ISS-006 (transition authority — key attack), ISS-007 actions

## 4. Definitions & Acronyms

- 6-DOF: six-degree-of-freedom rigid-body motion (three translational plus three rotational)
- State vector: minimal set describing rigid-body motion state (structure defined, data TBD)
- Control vector: commanded effector settings driving forces and moments (structure defined, data TBD)
- Force / moment summation: total = aerodynamic contribution + propulsion contribution + gravity (all terms TBD)

## 5. System Context

The 6-DOF structure is the common analysis backbone linking aerodynamics (Vol 06), propulsion (Vol 04), flight control (Vol 07), and simulation / V&V (Vol 19). At CONCEPT it bounds what may be asked of the model; it does not authorise any authority, feasibility, or clearance claim. All claims await verified data and Vol 19.15 gating.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-ASX-001 | The 6-DOF equation-of-motion structure shall be defined as force summation (aerodynamic TBD + propulsion TBD + gravity) and moment summation (aerodynamic TBD + propulsion TBD), with state-vector and control-vector structures defined and all data TBD. | HFPX-SYS-REQ-001, HFPX-SYS-ARC-001, ISS-006 | Inspection |
| REQ-HFPX-ASX-002 | Required 6-DOF input data shall be enumerated (mass / inertia TBD, aerodynamic tables TBD per Chapters 06.5 / 06.6, thrust maps TBD per Vol 04 / Vol 07, environment and initial conditions TBD), with all values TBD. | HFPX-SYS-REQ-001, HFPX-SYS-MIS-002 | Inspection |
| REQ-HFPX-ASX-003 | 6-DOF model implementation ownership shall reside with Vol 19.3, with implementation detail, tools, and configuration TBD. | HFPX-SYS-ARC-001 | Inspection |
| REQ-HFPX-ASX-004 | No authority, feasibility, or clearance claim shall be drawn from an unverified 6-DOF model; such claims shall be subject to Vol 19.15 evidence gates, with criteria TBD. | HFPX-SYS-CON-003, ISS-006 | Inspection |
| REQ-HFPX-ASX-005 | Model use at CONCEPT stage shall be limited to structure definition, data-requirements capture, and interface alignment; the model shall not support design freeze, envelope clearance, or flight authorisation, with permitted uses TBD. | HFPX-SYS-CON-001, HFPX-SYS-ARC-001, ISS-006 | Inspection |

## 7. Architecture

Structure-only model: equations (§8) consume enumerated inputs (§8) via Vol 19.3 implementation and serve Chapters 06.8–06.10 / 06.12–06.14 assessments, Vol 07 control design, and Vol 19 simulation. Claim authority sits outside this document with Vol 19.15. No implementation, toolchain, or data baseline is set here.

## 8. Detailed Design

Equation-of-motion structure (data TBD, no solved coefficients):

```text
Total force   = F_aero (TBD, per Chapters 06.5 / 06.6)
              + F_propulsion (TBD, per Vol 04 / Vol 07)
              + F_gravity (mass TBD, field TBD)

Total moment  = M_aero (TBD, per Chapters 06.5 / 06.6)
              + M_propulsion (TBD, per Vol 04 / Vol 07)
              + residual / coupling terms TBD

Translational dynamics: mass (TBD) relates total force to acceleration (form TBD)
Rotational dynamics: inertia (TBD) relates total moment to angular acceleration (form TBD)
Kinematics: attitude / position propagation (representation TBD)
```

State vector — structure defined, all data TBD:

```text
x = [ position (components TBD);
      velocity (components TBD);
      attitude (representation TBD);
      angular rate (components TBD) ]
```

Control vector — structure defined, all data TBD:

```text
u = [ control-surface commands (surfaces TBD, mapping TBD per Vol 07);
      propulsion commands (effectors TBD, mapping TBD per Vol 04 / Vol 07) ]
```

Required input-data list (all values TBD):

- Mass properties: mass, inertia, CG definition (positions TBD)
- Aerodynamic tables: force / moment tables as functions of state and control (structure TBD, data TBD per Chapters 06.5 / 06.6)
- Propulsion maps: thrust / moment maps as functions of command and state (maps TBD per Vol 04 / Vol 07)
- Environment: atmosphere, wind, ground-effect inputs (all TBD per Chapters 06.17 / 06.18)
- Initial conditions and simulation settings (all TBD, owned by Vol 19.3)

No aerodynamic tables, thrust maps, mass properties, derivatives, margins, positions, or speeds are given or implied. All entries are TBD.

## 9. Interfaces

Interfaces to Chapters 06.5 / 06.6 (aero tables TBD), Vol 04 (propulsion maps TBD), Vol 07 including 07.12 (control mapping and transition-data needs TBD), Vol 19.3 (implementation TBD), SAD control / aero views, and Vol 19.15 (evidence gates). Interface definitions and formats are TBD.

## 10. Operational Concept

The 6-DOF structure supports future walk-through of CONOPS threads (hover, transition, horizontal flight) in simulation; at CONCEPT it authorises no thread, envelope, or manoeuvre. Entry/exit conditions, abort criteria, and corridor boundaries remain TBD per Chapters 06.12–06.14.

## 11. Safety

An unverified model shall not be used to claim transition authority, controllability, or safety (ISS-006). Safety findings require verified data plus Vol 13 analyses and Vol 19.15 gates. No test or flight authorisation is given.

## 12. Performance

Model fidelity, accuracy, and runtime performance are TBD. No fidelity claims or performance values are stated.

## 13. Verification & Validation

Structure verified by inspection (equations, vectors, input list complete as structure). Model implementation V&V is owned by Vol 19.3 / Vol 19.15 and Vol 23 test correlation (all TBD). Success criteria are TBD.

## 14. Risks

- Unverified-model misuse (authority claimed from empty structure — ISS-006 core risk); mitigation: REQ-HFPX-ASX-004 / ASX-005 claim and use limits
- Input-data starvation (all inputs TBD); mitigation: enumerated TBD list drives Chapters 06.5 / 06.6 and Vol 04 / Vol 07 data actions
- Implementation drift (Vol 19.3 diverges from this structure); mitigation: ownership and traceability to this structure TBD

## 15. Open Issues

ISS-006 (transition authority — primary attack), ISS-007 (thrust-data interface). New TBDs: equation-form detail, state / control representations, every input table, implementation plan, 19.15 gate criteria.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SYS-001, MIS-002, CON-001 / CON-003, SAD control / aero views, Chapters 06.5 / 06.6 / 06.8–06.10, Vol 04, Vol 07 (including 07.12), Vol 19.3 / 19.15, and ISS-006 / ISS-007 actions.

## 18. Traceability

Parent: SYS-001, MIS-002, CON-001 / CON-003, SAD control / aero views, ISS-006 / ISS-007 actions. Children: Vol 19.3 implementation, Vol 07 control-interface requirements, Chapters 06.12–06.14 corridor and balance analyses, V&V evidence per 19.15. RTM: REQ-HFPX-ASX-001..005 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 5 draft, CONCEPT, not baselined.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 draft (Chapter 06.11) |
