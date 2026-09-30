# Navigation Software

**Document ID:** HFPX-SW-NAV-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X navigation software item (Chapter 16.8): estimation-implementation scaffolding, GNSS-denied provisions scaffolding, verification scaffolding, and versioning discipline. No algorithms or values stated.

## 2. Scope

Covers navigation estimation implementation aligned to Vol 09.14, GNSS-denied provisions, verification scaffolding, and versioning scaffolding. Excludes estimator design, tuning, sensor fusion details, and performance values (all TBD).

## 3. Applicable Documents

- SYS-002 (parent system requirements)
- HFPX-ARC-SW-001 Software Architecture (parent requirements REQ-HFPX-SWA-001..004)
- DO-178C concepts (structured-according-to only, no compliance claimed)
- Vol 09.14 estimation definitions; HFPX-SW-ARC-001 Software Architecture (structure only)
- VVP thread (verification and validation thread, details TBD)

## 4. Definitions & Acronyms

- Navigation software: application-layer item implementing estimation and navigation outputs (implementation TBD).
- Estimation implementation: software realisation of Vol 09.14 estimation functions (scope TBD).
- GNSS-denied provisions: TBD fallback behaviour when satellite navigation is unavailable.

## 5. System Context

Navigation software consumes sensor-driver outputs and command and health inputs and produces position, velocity, attitude, and integrity-status outputs to control, display, safety, and logging consumers. It executes under deterministic bounded policy with independent safety monitoring.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-WNS-001 | Navigation estimation implementation shall be defined consistent with Vol 09.14 (implementation TBD). | SYS-002; REQ-HFPX-SWA-001; VVP | Inspection |
| REQ-HFPX-WNS-002 | GNSS-denied provisions shall be defined (behaviour TBD). | SYS-002; REQ-HFPX-SWA-001; VVP | Inspection |
| REQ-HFPX-WNS-003 | Navigation software shall be verified by review and test (details TBD). | SYS-002; REQ-HFPX-SWA-002; VVP | Inspection + Test |
| REQ-HFPX-WNS-004 | Navigation software shall enforce versioning and traceability discipline per Vol 16 (scheme TBD). | SYS-002; REQ-HFPX-SWA-004; VVP | Inspection |

## 7. Architecture

Application-layer navigation item implementing Vol 09.14 estimation scope with GNSS-denied placeholders. Execution supporting primary control is deterministic, bounded, and verifiable; AI functions, if present, remain advisory-only in a segregated partition. Assurance scaffolding is structured according to DO-178C concepts with no compliance claim.

## 8. Detailed Design

Not applicable at this revision. Estimator requirements, design descriptions, and code are deferred. No implementation stated.

## 9. Interfaces

Navigation interfaces: sensor-data inputs, GNSS inputs, command inputs, state and integrity outputs, display and logging outputs. Signatures, timing, and protocols TBD; detailed in software ICDs and Vol 09.

## 10. Operational Concept

Navigation executes across power-up alignment, flight-mode, degraded-mode including GNSS-denied operation, and maintenance states. Alignment sequencing and degraded-mode switching are TBD; advisory AI output is display and test-logging only.

## 11. Safety

Navigation integrity provisions and GNSS-denied behaviour feed Vol 13. Determinism, boundedness, and independence from advisory functions are safety constraints. No integrity values stated.

## 12. Performance

Accuracy budgets, integrity bounds, timing budgets, and throughput budgets are TBD. Budget holders: navigation software (Vol 16), estimation owners (Vol 09.14). No timing figures stated.

## 13. Verification & Validation

Verified by review (Vol 09.14 alignment, GNSS-denied provisions) and test (functional and robustness test scaffolding). Inspection covers versioning and traceability. Validated later via SIL and HIL campaigns and flight test per the VVP thread.

## 14. Risks

- Estimation-to-implementation misalignment with Vol 09.14; mitigation: alignment review requirement (WNS-001).
- Undefined GNSS-denied behaviour; mitigation: explicit GNSS-denied provisions requirement (WNS-002).

## 15. Open Issues

Estimation implementation scope, GNSS-denied behaviour, verification scope, and versioning scheme all TBD. Sensor set and fusion approach per Vol 09.14 TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SYS-002 system requirements, SWA tier architecture, Vol 09.14 estimation definitions, Vol 16 plan and architecture items, and sensor-driver provisions (Chapter 16.6).

## 18. Traceability

Parents: SYS-002; SWA tier (REQ-HFPX-SWA-001..004); VVP thread. Children: navigation requirements, design, code, V&V cases. RTM: REQ-HFPX-WNS-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Chapter 16.8.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 16.8) |
