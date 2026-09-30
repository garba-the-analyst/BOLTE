# Propulsion Model

**Document ID:** HFPX-SIM-PRP-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the propulsion model structure and discipline (Chapter 19.5): thrust-response structure, module-failure injection hooks, fuel and thermal coupling hooks, data-source rules, and feeds to the 6-DOF simulation (19.3) and energy budgets. This document defines structures with TBD values; no capability or feasibility claim rests on any unverified model in this revision.

## 2. Scope

Covers steady and transient thrust-response structures, failure-injection hooks feeding 19.13, fuel and thermal coupling hooks, bench/rig data-source discipline, and consumer feeds to 19.3 and energy budgets. Excludes propulsion hardware design (Vol 07 or TBD owner), 6-DOF integration (19.3), failure-simulation execution (19.13), and verification execution (Vol 22/23).

## 3. Applicable Documents

- HFPX-VV-PLN-001 V&V Plan (notably REQ-HFPX-VVP-001, REQ-HFPX-VVP-004)
- HFPX-SYS-REQ-001 SyRS (notably SYS-001, SYS-008)
- HFPX-SIM-STR-001 Digital Engineering Strategy
- HFPX-SIM-SIX-001 6-DOF Simulation (consumer of thrust maps)
- ISS-006 and ISS-007 actions (evidence and budget-interface scope; details TBD)
- Failure-simulation chapter 19.13 (consumer of injection hooks; ID TBD)

## 4. Definitions & Acronyms

- Thrust-response structure: steady plus transient thrust characterisation; values TBD.
- Module-failure injection hooks: defined points at which module failures are injected for failure simulation; scope TBD.
- Fuel/thermal coupling hooks: defined interfaces to fuel-system and thermal models; treatment TBD.
- TBD: to be defined; TBC: to be confirmed.

## 5. System Context

The propulsion model supplies thrust maps and transient responses to the 6-DOF simulation (19.3) and energy-budget consumers under the 19.1 hierarchy. It exposes failure-injection hooks consumed by 19.13 and coupling hooks to fuel and thermal domains. All structures are TBD-valued in this revision and gain gate authority solely through verification via 19.15 hooks.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-MPM-001 | The propulsion model shall define a thrust-response structure comprising steady and transient elements, with structure TBD and values recorded as TBD. | SYS-008; ASX tier; ISS-006 | Analysis |
| REQ-HFPX-MPM-002 | The propulsion model shall expose module-failure injection hooks feeding failure simulation (19.13), with hook definitions and injection scope TBD. | SYS-001; VVP-001; ISS-006 | Inspection |
| REQ-HFPX-MPM-003 | The propulsion model shall define fuel and thermal coupling hooks, with coupled variables and treatment recorded as TBD. | SYS-008; ISS-007; ASX tier | Inspection |
| REQ-HFPX-MPM-004 | The programme shall apply a propulsion data-source rule requiring thrust-response data to be sourced from bench or rig evidence, with datasets and pedigree recorded as TBD. | VVP-001; ISS-006; SYS-001 | Inspection |
| REQ-HFPX-MPM-005 | The propulsion model shall feed the 6-DOF simulation (19.3) and energy-budget consumers as its TBD-valued supplier, with interfaces and feed status TBD, such that no capability or feasibility claim rests on unverified propulsion data. | SYS-001; VVP-004; ISS-007 | Analysis |

## 7. Architecture

Propulsion model architecture (structure only): response layer with steady and transient elements (REQ-HFPX-MPM-001); injection-hook layer (REQ-HFPX-MPM-002) interfacing to 19.13; coupling layer (REQ-HFPX-MPM-003) interfacing to fuel and thermal domains; source layer (REQ-HFPX-MPM-004) binding data to bench/rig pedigree; feed layer (REQ-HFPX-MPM-005) exporting thrust maps to 19.3 and energy budgets. Element boundaries and formats TBD.

## 8. Detailed Design

Thrust-response record TBD: steady structure TBD, transient structure TBD, values TBD throughout. Injection-hook record TBD: hook locations TBD, injectable failure types TBD, interface to 19.13 TBD. Coupling-hook record TBD: fuel-system variables TBD, thermal variables TBD, coupling treatment TBD. Data-source record TBD: bench datasets TBD, rig datasets TBD, pedigree references TBD, uncertainty TBD. Feed record TBD: thrust-map format TBD, energy-budget interface TBD, configuration reference TBD, status TBD.

## 9. Interfaces

- Propulsion model ↔ bench/rig activities: evidence ingested per data-source rule (datasets TBD).
- Propulsion model ↔ 19.3 6-DOF: thrust maps supplied (format TBD).
- Propulsion model ↔ energy budgets (ISS-007): consumption data supplied (tables TBD).
- Propulsion model ↔ 19.13 failure simulation: injection hooks exposed (scope TBD).
- Propulsion model ↔ fuel/thermal domains: coupling hooks exposed (treatment TBD).
- Propulsion model ↔ 19.15 Model Verification: verification methodology and status.

## 10. Operational Concept

Operates evidence-driven: declare response structures TBD → bind to bench/rig sources TBD → expose injection and coupling hooks TBD → export to 19.3 and budgets TBD → submit for verification per 19.15 before any gate use. No thrust or endurance finding is offered as evidence until verified. Cadence TBD.

## 11. Safety

No safety-related claim (including thrust margin, transient behaviour, or failure response) is made from propulsion-model output until verification per 19.15 with independence per VVP-006 (degree TBD). Safety-significant failure combinations are TBD (Vol 13/24 mapping TBD; execution via 19.13 scope TBD).

## 12. Performance

Propulsion model performance indicators TBD (no thresholds baselined): response-structure definition status TBD, hook-definition completeness TBD, source-binding completeness TBD, feed-interface definition status TBD, verification closure TBD. Measurement method and reporting cadence TBD.

## 13. Verification & Validation

This document is verified by Inspection against template, header, and requirement discipline. REQ-HFPX-MPM-001..005 are verified by their stated methods applied to the response, hook, source, and feed records. Verification methodology for the model is owned by 19.15; execution evidence is owned by Vol 22/23. Validation is programme-authority approval at a gated review (review TBD).

## 14. Risks

- Steady/transient structures populated with assumed values later cited as thrust capability; mitigation: REQ-HFPX-MPM-001 TBD-value rule plus REQ-HFPX-MPM-004 bench/rig source rule.
- Failure-injection hooks left undefined while failure tolerance is asserted (ISS-006 risk); mitigation: REQ-HFPX-MPM-002 explicit hook definitions (definitions TBD) feeding 19.13.
- Budget consumers drawing on unverified thrust data (ISS-007 risk); mitigation: REQ-HFPX-MPM-005 no-claim rule with 19.15 hooks.

## 15. Open Issues

Thrust-response structures and values TBD. Injection-hook definitions and scope TBD. Fuel/thermal coupling treatment TBD. Bench/rig datasets and pedigree TBD. Feed interfaces and verification status TBD via 19.15.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on bench/rig evidence activities (TBD), fuel-system and thermal domain definitions (TBD), 19.3 consumer interface (TBD), 19.13 failure-simulation interface (TBD), energy-budget tables per ISS-007 (TBD), 19.1 authority rule, 19.15 verification methodology, and Vol 22/23 execution.

## 18. Traceability

Parents: VVP-001, VVP-004; SYS-001, SYS-008; ASX tier (details TBD); ISS-006, ISS-007 actions. Children: response records, hook records, source records, feed records, verification cases (IDs TBD; rows TBD). RTM: REQ-HFPX-MPM-001..005 → CONCEPT. No capability or feasibility claim in this document rests on an unverified model; authority for any such future claim routes via 19.15.

## 19. Configuration

BL-0.0. Tranche 5 draft, CONCEPT, not baselined. Future changes via change records; any change re-validates affected traceability before gate claims.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 draft (19.5 propulsion structure; requirements REQ-HFPX-MPM-001..005) |
