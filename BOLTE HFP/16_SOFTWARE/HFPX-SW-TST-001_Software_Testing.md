# Software Testing

**Document ID:** HFPX-SW-TST-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X software testing scope (Chapter 16.16): test levels, coverage policy, regression discipline, and hooks to the integration thread. No test implementation stated.

## 2. Scope

Covers software testing requirements, organisation across unit, integration, and system levels, coverage and regression policy, and planning hooks to Vol 23.8. Excludes verification-case ownership detail (Chapter 16.18), hardware test detail (Vol 08/19), and tool qualification (TBD).

## 3. Applicable Documents

- Parent requirements: SYS-002 thread; WDP/WSA tier; VVP thread
- HFPX-ARC-SW-001 Software Architecture (layering, determinism policy, assurance structured according to DO-178C concepts)
- Vol 23 integration thread, notably Vol 23.8 (hooks, TBD)
- Vol 22 verification thread; Vol 16 sibling software chapters; Vol 19 test facilities
- DO-178C concepts (structured-according-to only, no compliance claimed at this stage)

## 4. Definitions & Acronyms

- Unit testing: testing of individual software units against allocated requirements (scope and environments TBD).
- Integration testing: testing of assembled software items and interfaces (scope and environments TBD).
- System testing: testing of integrated software in representative environments (scope and environments TBD).
- Coverage policy: the required extent and type of test coverage (policy TBD).
- Regression: re-execution of defined tests following change (scope and triggers TBD).

## 5. System Context

Software testing spans the layered software architecture from units through integrated software to system contexts. It consumes software requirements, design descriptions, and code together with test environments (SIL/HIL, rigs) and produces test procedures, results, and coverage records across the lifecycle (all TBD).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-WST-001 | Software testing shall be organised across unit, integration, and system levels (scope per level TBD). | SYS-002; WDP/WSA tier; VVP thread | Inspection |
| REQ-HFPX-WST-002 | Software testing shall observe a defined coverage policy (policy TBD). | SYS-002; WDP/WSA tier; VVP thread | Inspection |
| REQ-HFPX-WST-003 | Software testing shall observe defined regression discipline following software change (scope and triggers TBD). | SYS-002; WDP/WSA tier; VVP thread | Inspection |
| REQ-HFPX-WST-004 | Software testing shall provide hooks to Vol 23.8 integration activities (hooks TBD). | SYS-002; WDP/WSA tier; VVP thread | Inspection |

Software assurance is structured according to DO-178C concepts; no compliance is claimed at this stage and no coverage values are stated.

## 7. Architecture

Testing is organised per HFPX-ARC-SW-001 layering: unit tests against allocated software requirements, integration tests against interfaces and ICDs, and system tests in representative environments. Test-architecture layering, independence provisions, and environment allocation are TBD.

## 8. Detailed Design

Not applicable at this revision. Test plans, procedures, scripts, harnesses, and data are deferred to later Vol 16 and VVP detail. No implementation stated.

## 9. Interfaces

Interfaces to requirements repositories, configuration baselines, test environments (SIL/HIL, rigs), and Vol 23.8 integration activities are TBD. Formats, harnesses, and data-exchange provisions are TBD.

## 10. Operational Concept

Testing executes across the development lifecycle: unit testing during implementation, integration testing during assembly, system testing during integration and pre-flight, and regression testing following change. Entry, exit, and independence provisions per level are TBD.

## 11. Safety

Testing safety inputs, including independence provisions and coverage-adequacy arguments feeding Vol 13, are TBD. No integrity values stated. Verification independence provisions are defined in Chapter 16.18.

## 12. Performance

Test throughput, environment capacity, and schedule provisions are TBD. Budget holders: VVP thread (Vol 22/23). No values stated.

## 13. Verification & Validation

Testing provisions are themselves verified by inspection (level organisation, coverage policy, regression discipline, Vol 23.8 hooks), structured according to DO-178C concepts with no compliance claimed. Test adequacy is assessed via coverage records and independent review (detail TBD) per the VVP thread.

## 14. Risks

- Level-scope gaps (units tested without integration coverage, or vice versa); mitigation: level-organisation requirement WST-001.
- Coverage policy undefined; mitigation: coverage-policy requirement WST-002 with independent review.
- Change without regression; mitigation: regression-discipline requirement WST-003 with Chapter 16.17 change trace.

## 15. Open Issues

Scope per test level TBD. Coverage policy, metrics, and targets TBD. Regression scope and triggers TBD. Hooks to Vol 23.8 TBD. Environments and independence provisions TBD.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on software architecture layering (HFPX-ARC-SW-001), Vol 16 software requirements and ICDs, verification planning (Chapter 16.18), integration planning (Vol 23.8), verification thread (Vol 22), and test facilities (Vol 19).

## 18. Traceability

Parents: SYS-002 thread; WDP/WSA tier; VVP thread. Children: test plans, procedures, results, coverage records (all TBD). RTM: REQ-HFPX-WST-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Chapter 16.16.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 16.16) |
