# Flight Software

**Document ID:** HFPX-SW-FLT-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X flight software item (Chapter 16.3): deterministic bounded execution scaffolding, timing-budget scaffolding, versioning discipline, and SIL and HIL verification scaffolding. No code or values stated.

## 2. Scope

Covers primary flight software behaviour, timing-budget scaffolding, versioning and traceability scaffolding, and verification scaffolding. Excludes detailed requirements, design, source code, timing values, and tool selection (all TBD).

## 3. Applicable Documents

- SYS-002 (parent system requirements)
- HFPX-ARC-SW-001 Software Architecture (parent requirements REQ-HFPX-SWA-001..004)
- DO-178C concepts (structured-according-to only, no compliance claimed)
- HFPX-SW-ARC-001 Software Architecture, HFPX-SW-PLN-001 Software Development Plan (structure only)
- VVP thread (verification and validation thread, details TBD)

## 4. Definitions & Acronyms

- Flight software: software item implementing primary flight functions under the Vol 16 architecture (contents TBD).
- Deterministic bounded execution: predictable behaviour with bounded response (bounds TBD).
- WCET scaffolding: placeholder for worst-case execution time budgeting and analysis (values TBD).
- SIL and HIL: software-in-the-loop and hardware-in-the-loop verification environments (details TBD).

## 5. System Context

Flight software executes application-layer flight functions on the computing paths, receiving command, navigation, and health inputs and producing actuator, display, and logging outputs. It operates under the flight and safety partition scheme with independent safety monitoring.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-WFS-001 | Flight software shall be deterministic and bounded and independently verifiable (bounds TBD). | SYS-002; REQ-HFPX-SWA-002; VVP | Analysis + Test |
| REQ-HFPX-WFS-002 | Flight software timing budgets including WCET provisions shall be defined (values TBD). | SYS-002; REQ-HFPX-SWA-002; VVP | Analysis |
| REQ-HFPX-WFS-003 | Flight software shall enforce versioning and traceability discipline per Vol 16 (scheme TBD). | SYS-002; REQ-HFPX-SWA-004; VVP | Inspection |
| REQ-HFPX-WFS-004 | Flight software shall be verified by SIL and HIL test and review (details TBD). | SYS-002; REQ-HFPX-SWA-002; VVP | Test |

## 7. Architecture

Flight software item sits in the application layer under the Vol 16 layering and partitioning scheme. Execution is deterministic, bounded, and verifiable by policy; timing budgets and WCET provisions are placeholders. AI functions, if present, are excluded from the primary flight path and confined to a segregated advisory partition. Assurance artefacts are structured according to DO-178C concepts with no compliance claim.

## 8. Detailed Design

Not applicable at this revision. Flight software requirements, design descriptions, and code are deferred. No implementation stated.

## 9. Interfaces

Flight software interfaces: command inputs, navigation inputs, health inputs, actuator outputs, display and logging outputs, inter-partition APIs. Signatures, timing, and protocols TBD; detailed in software ICDs.

## 10. Operational Concept

Flight software executes across power-up, flight-mode, degraded-mode, and maintenance states. Degraded-mode behaviour and mode transitions are TBD; advisory AI output is display and test-logging only.

## 11. Safety

Determinism, boundedness, and verifiability are safety constraints on flight software. Partition independence from safety software is required (mechanism TBD). Safety assessment linkage feeds Vol 13. No integrity values stated.

## 12. Performance

Timing budgets, WCET values, jitter bounds, memory budgets, and throughput budgets are TBD. Budget holders: software and compute (Vol 16), control and navigation consumers. No timing figures stated.

## 13. Verification & Validation

Verified by analysis (determinism argument, timing-budget analysis) and test (SIL and HIL, test-log review). Inspection covers versioning and traceability discipline. Validated later via integrated SIL and HIL campaigns and flight test per the VVP thread.

## 14. Risks

- Timing-budget overrun discovered late; mitigation: WCET scaffolding and analysis requirement from Tranche 6 (WFS-002).
- Traceability collapse from requirements to code and test; mitigation: versioning and traceability discipline (WFS-003).

## 15. Open Issues

Flight function inventory, determinism bounds, WCET method and values, versioning scheme, and SIL and HIL scope all TBD. Language, RTOS, and toolchain selections TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SYS-002 system requirements, SWA tier architecture, Vol 16 plan and architecture items, platform selection, and control, navigation, and algorithm definitions (Vol 07, Vol 09, Chapters 16.7..16.9).

## 18. Traceability

Parents: SYS-002; SWA tier (REQ-HFPX-SWA-001..004); VVP thread. Children: flight software requirements, design, code, SIL and HIL cases. RTM: REQ-HFPX-WFS-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Chapter 16.3.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 16.3) |
