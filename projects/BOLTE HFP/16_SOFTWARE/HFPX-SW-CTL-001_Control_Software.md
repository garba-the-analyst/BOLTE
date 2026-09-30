# Control Software

**Document ID:** HFPX-SW-CTL-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X control software item (Chapter 16.9): control-law implementation scaffolding, mode-switching scaffolding, gain-free structure discipline, and FVV-thread verification scaffolding. No laws, gains, or values stated.

## 2. Scope

Covers control-law implementation aligned to Vol 07, switching provisions, versioning and traceability scaffolding, and verification scaffolding. Excludes law design, gains, tuning, and timing values (all TBD).

## 3. Applicable Documents

- SYS-002 (parent system requirements)
- HFPX-ARC-SW-001 Software Architecture (parent requirements REQ-HFPX-SWA-001..004)
- DO-178C concepts (structured-according-to only, no compliance claimed)
- Vol 07 control-law definitions; HFPX-SW-ARC-001 Software Architecture (structure only)
- VVP thread; FVV thread (flight verification thread, details TBD)

## 4. Definitions & Acronyms

- Control software: application-layer item implementing Vol 07 control laws in software (implementation TBD).
- Switching: TBD transition logic between control modes and laws.
- FVV thread: flight verification thread consuming control-software verification evidence (details TBD).

## 5. System Context

Control software consumes navigation, command, sensor-driver, and health inputs and produces actuator commands, mode annunciation, and logging outputs. It forms the deterministic bounded primary-control path under independent safety monitoring.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-WCS-001 | Control-law implementation shall be defined consistent with Vol 07 laws (implementation TBD, no numeric gains stated). | SYS-002; REQ-HFPX-SWA-001; VVP | Inspection |
| REQ-HFPX-WCS-002 | Control switching provisions shall be defined (modes and transitions TBD). | SYS-002; REQ-HFPX-SWA-002; VVP | Inspection |
| REQ-HFPX-WCS-003 | Control software shall be deterministic and bounded and independently verifiable (bounds TBD). | SYS-002; REQ-HFPX-SWA-002; VVP | Analysis + Test |
| REQ-HFPX-WCS-004 | Control software shall be verified within the FVV thread by review and test (details TBD). | SYS-002; REQ-HFPX-SWA-002; VVP | Inspection + Test |

## 7. Architecture

Application-layer control item implementing Vol 07 law scope with switching placeholders and no numeric gains stated. Primary-control execution is deterministic, bounded, and verifiable by policy; AI functions, if present, remain advisory-only in a segregated partition and never assume control authority. Assurance scaffolding is structured according to DO-178C concepts with no compliance claim.

## 8. Detailed Design

Not applicable at this revision. Control software requirements, design descriptions, and code are deferred to Vol 16 implementation stages. No implementation stated.

## 9. Interfaces

Control interfaces: navigation inputs, command inputs, sensor-data inputs, health inputs, actuator command outputs, mode annunciation and logging outputs. Signatures, timing, and protocols TBD; detailed in software ICDs and Vol 07.

## 10. Operational Concept

Control software executes across flight-mode, degraded-mode, and maintenance states. Switching sequencing, fallback laws, and pilot-override handling are TBD; advisory AI output is display and test-logging only.

## 11. Safety

Determinism, boundedness, switching safety, and advisory-only AI segregation are safety constraints carried from the SWA tier and Vol 07. Safety assessment linkage feeds Vol 13. No integrity values stated.

## 12. Performance

Stability margins, handling budgets, timing budgets, and throughput budgets are TBD and owned by Vol 07 and Vol 16 jointly. No timing figures and no numeric gains stated.

## 13. Verification & Validation

Verified by review (Vol 07 alignment, switching definition) and analysis plus test (determinism argument, functional test) within the FVV thread. Validated later via SIL and HIL campaigns and flight test per the VVP thread.

## 14. Risks

- Law-to-implementation misalignment with Vol 07; mitigation: alignment review requirement (WCS-001).
- Unsafe switching transients; mitigation: switching-definition and determinism requirements with FVV-thread verification (WCS-002..WCS-004).

## 15. Open Issues

Law implementation scope, switching logic, determinism bounds, FVV-thread scope, and versioning scheme all TBD. Gains, tuning, and timing characterisation deferred with no values stated.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SYS-002 system requirements, SWA tier architecture, Vol 07 control laws, Vol 16 plan and architecture items, and navigation and sensor-driver provisions (Chapters 16.6, 16.8).

## 18. Traceability

Parents: SYS-002; SWA tier (REQ-HFPX-SWA-001..004); VVP thread (including FVV thread). Children: control software requirements, design, code, FVV cases. RTM: REQ-HFPX-WCS-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Chapter 16.9.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 16.9) |
