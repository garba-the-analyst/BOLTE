# Software Verification

**Document ID:** HFPX-SW-VER-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X software verification scope (Chapter 16.18): verification-case inventory, trace to requirements, independence provisions, and hooks to the verification thread. No verification implementation stated.

## 2. Scope

Covers software verification requirements, organisation, independence, and planning hooks to Vol 22.10. Excludes test execution detail (Chapter 16.16), hardware verification (Vol 08/19), and tool qualification (TBD).

## 3. Applicable Documents

- Parent requirements: SYS-002 thread; WDP/WSA tier; VVP thread
- HFPX-ARC-SW-001 Software Architecture (layering, determinism policy, assurance structured according to DO-178C concepts)
- Vol 22 verification thread, notably Vol 22.10 (hooks, TBD)
- Vol 23 integration thread; Vol 16 sibling software chapters; Vol 19 test facilities
- DO-178C concepts (structured-according-to only, no compliance claimed at this stage)

## 4. Definitions & Acronyms

- Verification case: a defined verification activity with objective, method, and pass criteria (inventory TBD).
- Trace: linkage from software requirements through design and code to verification cases and results (mechanism TBD).
- Independence: separation between development and verification responsibilities (provisions TBD).
- Hooks: defined interfaces to Vol 22.10 verification activities (TBD).

## 5. System Context

Software verification spans the layered software architecture from requirements reviews through code verification to integration verification. It consumes software requirements, design descriptions, code, and configuration baselines and produces verification cases, procedures, results, and trace records across the lifecycle (all TBD).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-WVR-001 | Software verification shall maintain a verification-case inventory covering software requirements (inventory TBD). | SYS-002; WDP/WSA tier; VVP thread | Inspection |
| REQ-HFPX-WVR-002 | Software verification shall provide trace from software requirements to verification cases and results (mechanism TBD). | SYS-002; WDP/WSA tier; VVP thread | Inspection |
| REQ-HFPX-WVR-003 | Software verification shall observe defined independence provisions (provisions TBD). | SYS-002; WDP/WSA tier; VVP thread | Inspection |
| REQ-HFPX-WVR-004 | Software verification shall provide hooks to Vol 22.10 verification activities (hooks TBD). | SYS-002; WDP/WSA tier; VVP thread | Inspection |

Software assurance is structured according to DO-178C concepts; no compliance is claimed at this stage and no integrity values are stated.

## 7. Architecture

Verification is organised per HFPX-ARC-SW-001 layering: requirements reviews, design reviews, code verification, and integration verification with independence provisions. Verification-architecture layering, method allocation (review, analysis, test), and environment allocation are TBD.

## 8. Detailed Design

Not applicable at this revision. Verification plans, cases, procedures, and results are deferred to later Vol 16 and Vol 22 detail. No implementation stated.

## 9. Interfaces

Interfaces to requirements repositories, configuration baselines, test environments (SIL/HIL, rigs), and Vol 22.10 verification activities are TBD. Formats and data-exchange provisions are TBD.

## 10. Operational Concept

Verification executes across the development lifecycle: early reviews and analysis during requirements and design, code verification during implementation, and requirements-based testing during integration. Independence is enforced as defined per activity (TBD). Re-verification following change is governed with Chapter 16.17 change trace.

## 11. Safety

Verification safety inputs, including independence adequacy and coverage-adequacy arguments feeding Vol 13, are TBD. No integrity values stated. Determinism and partition-independence claims are verified per HFPX-ARC-SW-001.

## 12. Performance

Verification throughput, environment capacity, and schedule provisions are TBD. Budget holders: VVP thread (Vol 22/23). No values stated.

## 13. Verification & Validation

Verification provisions are themselves verified by inspection (case inventory, trace, independence, Vol 22.10 hooks), structured according to DO-178C concepts with no compliance claimed. Adequacy is assessed via trace completeness and independent review (detail TBD) per the VVP thread.

## 14. Risks

- Requirements without verification cases; mitigation: case-inventory requirement WVR-001.
- Trace collapse across requirements, design, code, and results; mitigation: trace requirement WVR-002 with Chapter 16.17 discipline.
- Lack of independence undermining assurance; mitigation: independence requirement WVR-003.

## 15. Open Issues

Verification-case inventory TBD. Trace mechanism and completeness criteria TBD. Independence provisions per activity TBD. Hooks to Vol 22.10 TBD. Environments TBD.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on software architecture layering (HFPX-ARC-SW-001), Vol 16 software requirements, design descriptions, and ICDs, configuration management (Chapter 16.17), testing organisation (Chapter 16.16), verification thread (notably Vol 22.10), and test facilities (Vol 19).

## 18. Traceability

Parents: SYS-002 thread; WDP/WSA tier; VVP thread. Children: verification plans, cases, procedures, results, trace records (all TBD). RTM: REQ-HFPX-WVR-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Chapter 16.18.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 16.18) |
