# Flight Algorithms

**Document ID:** HFPX-SW-ALG-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X flight-algorithm software item (Chapter 16.7): algorithm-inventory scaffolding, primary-path AI exclusion, verification scaffolding, and versioning discipline. No algorithms or values stated.

## 2. Scope

Covers flight-algorithm inventory, advisory-only AI segregation, verification scaffolding, and versioning scaffolding. Excludes algorithm design, tuning, pseudo-code, and performance values (all TBD).

## 3. Applicable Documents

- SYS-002 (parent system requirements)
- HFPX-ARC-SW-001 Software Architecture (parent requirements REQ-HFPX-SWA-001..004)
- DO-178C concepts (structured-according-to only, no compliance claimed)
- HFPX-SW-ARC-001 Software Architecture (structure only); Vol 07 control laws; Vol 09 estimation references
- VVP thread (verification and validation thread, details TBD)

## 4. Definitions & Acronyms

- Flight algorithms: application-layer computations supporting control, navigation, and mode management (inventory TBD).
- Primary path: deterministic bounded execution chain from sensing through control to actuation.
- Advisory-only AI: AI functions, if present, are segregated advisory outputs excluded from the primary path.

## 5. System Context

Flight algorithms execute in the application layer, consuming sensor-driver, navigation, and command inputs and producing control, navigation, and display outputs. Primary-path algorithms operate under deterministic bounded verifiable policy with independent safety monitoring.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-WAL-001 | The flight-algorithm inventory shall be defined (algorithms TBD). | SYS-002; REQ-HFPX-SWA-001; VVP | Inspection |
| REQ-HFPX-WAL-002 | No AI function shall reside in the primary flight path; AI, if present, shall be advisory-only in a segregated partition. | SYS-002; REQ-HFPX-SWA-002; VVP | Inspection |
| REQ-HFPX-WAL-003 | Flight algorithms shall be verified by review and test (details TBD). | SYS-002; REQ-HFPX-SWA-002; VVP | Inspection + Test |
| REQ-HFPX-WAL-004 | Flight algorithms shall enforce versioning and traceability discipline per Vol 16 (scheme TBD). | SYS-002; REQ-HFPX-SWA-004; VVP | Inspection |

## 7. Architecture

Application-layer algorithm set (inventory TBD) partitioned into deterministic bounded primary-path algorithms and segregated advisory-only AI, if present. Primary-path behaviour is independently verifiable; advisory outputs are display and test-logging only. Assurance scaffolding is structured according to DO-178C concepts with no compliance claim.

## 8. Detailed Design

Not applicable at this revision. Algorithm requirements, design descriptions, and code are deferred. No implementation stated.

## 9. Interfaces

Algorithm interfaces: sensor-data inputs, navigation inputs, command inputs, control-law outputs, display and logging outputs. Signatures, timing, and protocols TBD; detailed in software ICDs.

## 10. Operational Concept

Algorithms execute across flight-mode, degraded-mode, and maintenance states. Mode-dependent algorithm selection and advisory-output handling are TBD.

## 11. Safety

Primary-path determinism, boundedness, and AI exclusion are safety constraints carried from the SWA tier. Algorithm safety inputs feed Vol 13. No integrity values stated.

## 12. Performance

Execution-time budgets, memory budgets, and throughput budgets are TBD. Budget holders: algorithms and platform (Vol 16), control and navigation consumers. No timing figures stated.

## 13. Verification & Validation

Verified by review (inventory, AI-exclusion argument) and test (functional and robustness test scaffolding). Inspection covers versioning and traceability. Validated later via SIL and HIL campaigns per the VVP thread.

## 14. Risks

- AI logic leaking into the primary path; mitigation: segregation plus AI-exclusion review requirement (WAL-002).
- Algorithm inventory gaps versus control and navigation needs; mitigation: inventory inspection tied to Vol 07 and Vol 09 (WAL-001).

## 15. Open Issues

Algorithm inventory, AI segregation mechanism, verification scope, and versioning scheme all TBD. Tuning and performance characterisation deferred.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SYS-002 system requirements, SWA tier architecture, Vol 16 plan and architecture items, control laws (Vol 07), and sensor and estimation definitions (Vol 09).

## 18. Traceability

Parents: SYS-002; SWA tier (REQ-HFPX-SWA-001..004); VVP thread. Children: algorithm requirements, design, code, V&V cases. RTM: REQ-HFPX-WAL-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Chapter 16.7.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 16.7) |
