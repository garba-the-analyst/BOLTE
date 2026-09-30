# 6-DOF Simulation

**Document ID:** HFPX-SIM-SIX-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the 6-DOF simulation structure and discipline (Chapter 19.3): equation-structure implementation, enumerated input-data requirements, solver and integration-step approach, hover/transition-first application priority, and the no-authority-claim-before-verification rule. This document defines structures with TBD parameters; no capability or feasibility claim rests on any unverified model in this revision.

## 2. Scope

Covers 6-DOF equation-structure implementation per 06.11, required input-data families (mass/inertia, aerodynamic tables, thrust maps, environment), integration/solver selection, and hover/transition-first prioritisation per ISS-006. Excludes aerodynamic, propulsion, and environment model internals (owned by 19.4, 19.5, 19.14 respectively), flight-control laws (19.8), and verification execution (Vol 22/23).

## 3. Applicable Documents

- HFPX-VV-PLN-001 V&V Plan (notably REQ-HFPX-VVP-001, REQ-HFPX-VVP-004)
- HFPX-SYS-REQ-001 SyRS (notably SYS-001, SYS-008)
- HFPX-SIM-STR-001 Digital Engineering Strategy
- Volume 06 architecture, notably 06.11 equation structure (values TBD)
- ISS-006 action (hover/transition-first evidence priority; details TBD), ISS-007 action (budget interfaces; details TBD)
- Sibling models: 19.4 aerodynamic, 19.5 propulsion, 19.14 environment (inputs TBD)

## 4. Definitions & Acronyms

- 6-DOF: six-degree-of-freedom rigid-body dynamics; equation structure per 06.11, parameters TBD.
- Input-data families: mass/inertia data TBD, aerodynamic tables TBD (via 19.4), thrust maps TBD (via 19.5), environment definitions TBD (via 19.14).
- Solver/integration approach: numerical method and step treatment; method TBD, results TBD.
- TBD: to be defined; TBC: to be confirmed.

## 5. System Context

The 6-DOF simulation is the central dynamics integrator for Volume 19 under the 19.1 hierarchy, combining mass/inertia properties, aerodynamic tables, thrust maps, and environment definitions to propagate trajectories for mission threads exercised by 19.2. It is applied hover/transition-first per ISS-006 and is subject to verification via 19.15 hooks before any trajectory or handling result is offered as gate evidence.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-MSX-001 | The 6-DOF simulation shall implement the equation structure defined in 06.11, with equation parameters recorded as TBD. | SYS-001; ASX tier; ISS-006 | Analysis |
| REQ-HFPX-MSX-002 | The programme shall enumerate the 6-DOF input-data requirements comprising mass/inertia data TBD, aerodynamic tables TBD via 19.4, thrust maps TBD via 19.5, and environment definitions TBD via 19.14, with values TBD in every family. | SYS-008; ISS-006; ISS-007 | Inspection |
| REQ-HFPX-MSX-003 | The programme shall define the 6-DOF integration-step and solver approach, with numerical method TBD and numerical results TBD. | VVP-001; ASX tier; ISS-006 | Analysis |
| REQ-HFPX-MSX-004 | The programme shall prioritise hover and transition regimes in 6-DOF application before other regimes, with regime definitions and prioritisation records TBD per ISS-006. | SYS-001; ISS-006; VVP-004 | Inspection |
| REQ-HFPX-MSX-005 | The programme shall enforce a no-authority-claim-before-verification rule such that no capability or feasibility claim rests on 6-DOF output until the simulation and each input-data family are verified via 19.15 hooks, with verification status TBD. | VVP-004; VVP-001; ISS-006 | Analysis |

## 7. Architecture

6-DOF architecture (structure only): equation core per 06.11 (REQ-HFPX-MSX-001); input-data interface layer with four families per REQ-HFPX-MSX-002; solver layer per REQ-HFPX-MSX-003; application layer with hover/transition-first ordering per REQ-HFPX-MSX-004; authority gate per REQ-HFPX-MSX-005 routed via 19.15. Internal data flows and interface specifications TBD.

## 8. Detailed Design

Equation-structure mapping to 06.11 TBD (mapping table TBD, parameters TBD). Input-data requirement records TBD per family: mass/inertia source TBD, aerodynamic-table reference TBD (19.4), thrust-map reference TBD (19.5), environment reference TBD (19.14); values TBD throughout. Solver record TBD: method TBD, step treatment TBD, convergence handling TBD, results TBD. Hover/transition-first application record TBD: regime definitions TBD, ordering rationale TBD, coverage records TBD. Authority-gate record TBD: verification references TBD, gate-release criteria TBD.

## 9. Interfaces

- 6-DOF ↔ 06.11: equation structure consumed; parameters TBD.
- 6-DOF ↔ 19.4/19.5/19.14: aerodynamic tables, thrust maps, environment definitions consumed (formats TBD).
- 6-DOF ↔ mass/inertia source: properties consumed (source TBD).
- 6-DOF ↔ 19.2 system-level sim: trajectories and regime results supplied (status TBD, unverified in this revision).
- 6-DOF ↔ 19.15 Model Verification: verification methodology and status for core, solver, and input families.

## 10. Operational Concept

Operates regime-ordered: configure input-data families TBD → select solver treatment TBD → execute hover cases TBD → execute transition cases TBD → execute remaining regimes TBD → record outputs TBD → submit for verification per 19.15 before any gate use. No output is offered as feasibility or handling evidence until REQ-HFPX-MSX-005 is satisfied. Cadence TBD.

## 11. Safety

No safety-related claim (including hover/transition handling or departure behaviour) is made from 6-DOF output until verification per 19.15 with independence per VVP-006 (degree TBD). Safety-significant regimes and failure-combination inputs arrive via 19.13 hooks (scope TBD). Hazard mapping TBD (Vol 13/24).

## 12. Performance

6-DOF performance indicators TBD (no thresholds baselined): input-data completeness TBD, solver-definition status TBD, hover/transition coverage TBD, verification closure TBD. Measurement method and reporting cadence TBD.

## 13. Verification & Validation

This document is verified by Inspection against template, header, and requirement discipline. REQ-HFPX-MSX-001..005 are verified by their stated methods applied to the equation mapping, input-data enumeration, solver record, prioritisation record, and authority-gate record. Verification methodology for the simulation is owned by 19.15; execution evidence is owned by Vol 22/23. Validation is programme-authority approval at a gated review (review TBD).

## 14. Risks

- Equation structure implemented with assumed parameters filling TBD fields; mitigation: REQ-HFPX-MSX-001 TBD-parameter rule plus input enumeration per REQ-HFPX-MSX-002.
- Solver selection by precedent with unrecorded step treatment; mitigation: REQ-HFPX-MSX-003 explicit method record (method TBD).
- Hover/transition results cited as feasibility before verification (ISS-006 risk); mitigation: REQ-HFPX-MSX-004 ordering plus REQ-HFPX-MSX-005 no-claim rule with 19.15 hooks.

## 15. Open Issues

Equation parameters TBD. All four input-data families TBD in value and source detail. Solver method and numerical results TBD. Hover/transition regime definitions and coverage records TBD. Verification status of core, solver, and every input family TBD via 19.15.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on 06.11 equation structure, mass/inertia source (TBD), 19.4 aerodynamic tables (TBD), 19.5 thrust maps (TBD), 19.14 environment definitions (TBD), 19.1 authority rule, 19.15 verification methodology, ISS-006 prioritisation scope, and Vol 22/23 execution.

## 18. Traceability

Parents: VVP-001, VVP-004; SYS-001, SYS-008; ASX tier (details TBD); ISS-006, ISS-007 actions. Children: equation-mapping record, input-data records, solver record, regime-application records, verification cases (IDs TBD; rows TBD). RTM: REQ-HFPX-MSX-001..005 → CONCEPT. No capability or feasibility claim in this document rests on an unverified model; authority for any such future claim routes via 19.15.

## 19. Configuration

BL-0.0. Tranche 5 draft, CONCEPT, not baselined. Future changes via change records; any change re-validates affected traceability before gate claims.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 draft (19.3 6-DOF structure; requirements REQ-HFPX-MSX-001..005) |
