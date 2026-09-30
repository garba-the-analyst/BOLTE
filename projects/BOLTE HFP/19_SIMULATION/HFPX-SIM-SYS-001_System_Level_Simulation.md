# System-Level Simulation

**Document ID:** HFPX-SIM-SYS-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the system-level simulation scope and discipline (Chapter 19.2): mission-thread coverage, interface to budget tables, scenario-coverage rules, and verification of the system-level simulation itself. This document establishes structure only; no capability or feasibility claim rests on any unverified model in this revision.

## 2. Scope

Covers end-to-end mission-thread simulation at system level per CONOPS, consumption of TBD budget tables with infeasibility flagging, scenario-coverage discipline, and the verification approach for the system-level simulation. Excludes domain-model internals (owned by 19.3–19.8), SIL/HIL execution (19.9–19.10), and verification execution (Vol 22/23).

## 3. Applicable Documents

- HFPX-VV-PLN-001 V&V Plan (notably REQ-HFPX-VVP-001, REQ-HFPX-VVP-004)
- HFPX-SYS-REQ-001 SyRS (notably SYS-001, SYS-008)
- HFPX-SIM-STR-001 Digital Engineering Strategy (hierarchy and authority rule)
- CONOPS mission threads (definitions TBD)
- Budget tables per ISS-007 (tables TBD, values TBD)
- ISS-006 and ISS-007 actions (details TBD)

## 4. Definitions & Acronyms

- System-level simulation: integration of domain models and mission logic to exercise CONOPS-derived threads; configuration TBD.
- Budget tables: mass, energy, and related allocation tables consumed by the simulation; content TBD per ISS-007.
- Scenario coverage: defined set of scenarios the system-level simulation is required to exercise; set TBD.
- TBD: to be defined; TBC: to be confirmed.

## 5. System Context

System-level simulation integrates outputs of 19.3–19.8 domain models under the 19.1 hierarchy to exercise mission threads derived from CONOPS and SyRS SYS-001/SYS-008. It consumes budget tables as constraints, flags infeasibility per TBD logic, and is itself subject to verification via 19.15 hooks before any result is offered as gate evidence. No feasibility finding is claimed in this revision.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-MSL-001 | The system-level simulation shall define its scope as the set of mission threads derived per CONOPS, with the thread list recorded as TBD. | SYS-001; SYS-008; ISS-006 | Inspection |
| REQ-HFPX-MSL-002 | The system-level simulation shall consume TBD budget tables as constraints and shall flag infeasibility per TBD flagging logic, with tables, values, and thresholds recorded as TBD per ISS-007. | SYS-008; ISS-007; VVP-001 | Analysis |
| REQ-HFPX-MSL-003 | The programme shall define a scenario-coverage rule for the system-level simulation stating which scenarios shall be exercised and how coverage is recorded, with scenarios and recording method TBD. | VVP-001; SYS-001; ISS-006 | Inspection |
| REQ-HFPX-MSL-004 | The programme shall define the verification approach for the system-level simulation itself, with method, cases, and acceptance criteria TBD via 19.15 hooks, such that no capability or feasibility claim rests on the unverified simulation. | VVP-004; VVP-001; ISS-006 | Inspection |

## 7. Architecture

System-level simulation architecture (structure only): thread driver (REQ-HFPX-MSL-001) invoking domain-model contributions (19.3–19.8, interfaces TBD); budget-constraint interface (REQ-HFPX-MSL-002) consuming TBD tables; scenario manager enforcing the coverage rule (REQ-HFPX-MSL-003); self-verification harness (REQ-HFPX-MSL-004) routed via 19.15. Component boundaries and data flows TBD.

## 8. Detailed Design

Thread list TBD per CONOPS derivation (derivation record TBD). Budget-table consumption logic TBD: table identifiers TBD, value fields TBD, consumption mechanism TBD, infeasibility flagging logic TBD, flag disposition process TBD. Scenario-coverage rule TBD: scenario catalogue TBD, required-versus-optional designation TBD, coverage metric TBD, recording format TBD. Self-verification approach TBD: verification cases TBD, acceptance criteria TBD per case, independence provisions TBD.

## 9. Interfaces

- System-level sim ↔ CONOPS/SyRS: thread derivation from SYS-001/SYS-008.
- System-level sim ↔ budget tables (ISS-007): consumes TBD tables; returns infeasibility flags per TBD logic.
- System-level sim ↔ domain models 19.3–19.8: consumes domain outputs (interfaces TBD).
- System-level sim ↔ 19.1 strategy: fidelity registration and gate authority per REQ-HFPX-MST-003.
- System-level sim ↔ 19.15 Model Verification: self-verification methodology and status.

## 10. Operational Concept

Operates thread-by-thread: select thread TBD → configure budgets TBD → execute scenarios per coverage rule TBD → record results TBD → flag infeasibility TBD → submit for verification per 19.15 before any gate use. No thread result is offered as evidence until the simulation and each contributing domain model are verified per 19.15. Cadence TBD.

## 11. Safety

No safety-related finding is claimed from system-level simulation until the simulation and contributing models are verified per 19.15 with independence per VVP-006 (degree TBD). Safety-significant threads and flag-handling for safety budgets are TBD (Vol 13/24 mapping TBD).

## 12. Performance

System-level simulation performance indicators TBD (no thresholds baselined): thread coverage TBD, budget-conformance flag rate TBD, scenario-coverage completeness TBD, self-verification closure TBD. Measurement method and reporting cadence TBD.

## 13. Verification & Validation

This document is verified by Inspection against template, header, and requirement discipline. REQ-HFPX-MSL-001..004 are verified by their stated methods applied to the scope, interface, coverage, and self-verification records. Verification methodology for the simulation itself is owned by 19.15; execution evidence is owned by Vol 22/23. Validation is programme-authority approval at a gated review (review TBD).

## 14. Risks

- Thread scope left TBD while results are cited as mission feasibility; mitigation: REQ-HFPX-MSL-001 scope gate plus 19.15 no-claim-before-verification posture.
- Budget tables consumed informally with silent infeasibility (ISS-007 risk); mitigation: REQ-HFPX-MSL-002 explicit flagging logic (logic TBD).
- Scenario coverage asserted without a rule; mitigation: REQ-HFPX-MSL-003 coverage rule with recorded completeness (method TBD).

## 15. Open Issues

Mission-thread list TBD. Budget tables, values, thresholds, and flagging logic TBD per ISS-007. Scenario catalogue and coverage-recording method TBD. Self-verification cases and acceptance criteria TBD via 19.15.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on CONOPS and SyRS SYS-001/SYS-008 (threads), ISS-007 budget tables (TBD), 19.1 strategy (hierarchy and authority), domain models 19.3–19.8 (contributions TBD), 19.15 verification methodology (TBD), and Vol 22/23 verification execution (TBD).

## 18. Traceability

Parents: VVP-001, VVP-004; SYS-001, SYS-008; ASX tier (details TBD); ISS-006, ISS-007 actions. Children: scenario records, budget-interface records, and self-verification cases (IDs TBD; rows TBD). RTM: REQ-HFPX-MSL-001..004 → CONCEPT. No capability or feasibility claim in this document rests on an unverified model; authority for any such future claim routes via 19.15.

## 19. Configuration

BL-0.0. Tranche 5 draft, CONCEPT, not baselined. Future changes via change records; any change re-validates affected traceability before gate claims.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 draft (19.2 system-level structure; requirements REQ-HFPX-MSL-001..004) |
