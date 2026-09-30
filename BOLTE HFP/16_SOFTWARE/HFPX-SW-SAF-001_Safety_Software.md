# Safety Software

**Document ID:** HFPX-SW-SAF-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X safety software item (Chapter 16.4): independence scaffolding, monitoring-function scaffolding, assurance scaffolding, and fault-injection verification scaffolding. No implementation or values stated.

## 2. Scope

Covers safety-software independence, monitoring functions, assurance scaffolding structured according to DO-178C concepts, and fault-injection verification scaffolding. Excludes detailed requirements, design, code, thresholds, and mechanism selection (all TBD).

## 3. Applicable Documents

- SYS-002 (parent system requirements)
- HFPX-ARC-SW-001 Software Architecture (parent requirements REQ-HFPX-SWA-001..004)
- DO-178C concepts (structured-according-to only, no compliance claimed)
- HFPX-SW-ARC-001 Software Architecture, HFPX-SW-PLN-001 Software Development Plan (structure only)
- Vol 13 safety inputs; VVP thread (details TBD)

## 4. Definitions & Acronyms

- Safety software: independent software item implementing monitoring, stabilisation, and recovery functions (contents TBD).
- Independence: separation of safety software from flight software such that flight faults do not defeat safety action (mechanism TBD).
- Monitoring functions: TBD set of limit, consistency, and health monitors owned by safety software.
- Fault injection: deliberate introduction of faults in test to exercise safety response (scope TBD).

## 5. System Context

Safety software resides in the safety partition alongside primary flight software. It receives sensor, command, navigation, and health inputs and produces independent stabilisation, recovery, and annunciation outputs whenever powered in flight, without reliance on the flight partition.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-WSS-001 | Safety software shall be independent from flight software (mechanism TBD). | SYS-002; REQ-HFPX-SWA-002; VVP | Analysis + Test |
|REQ-HFPX-WSS-002|Safety software monitoring functions shall be defined (functions and thresholds TBD).|SYS-002; REQ-HFPX-SWA-001; VVP|Inspection|
| REQ-HFPX-WSS-003 | Safety software assurance scaffolding shall be structured according to DO-178C concepts (no compliance claimed at this stage). | SYS-002; REQ-HFPX-SWA-003; VVP | Inspection |
| REQ-HFPX-WSS-004 | Safety software shall be verified by fault-injection test and review (scope TBD). | SYS-002; REQ-HFPX-SWA-002; VVP | Test |

## 7. Architecture

Safety partition hosts independent monitoring, stabilisation, and recovery logic (functions TBD). Independence is enforced by partitioning provisions (mechanism TBD) with deterministic, bounded, verifiable execution. AI functions, if present, remain in a segregated advisory partition and never assume safety authority. Assurance artefacts follow DO-178C structure with no compliance claim.

## 8. Detailed Design

Not applicable at this revision. Safety software requirements, design descriptions, and code are deferred. No implementation stated.

## 9. Interfaces

Safety software interfaces: sensor and health inputs, flight-partition status inputs, independent actuation-path outputs, annunciation and logging outputs. Signatures, timing, and protocols TBD; detailed in software ICDs.

## 10. Operational Concept

Safety software is available whenever powered in flight and across degraded-mode and maintenance states. Monitoring, stabilisation, and recovery sequencing are TBD; advisory AI output is display and test-logging only.

## 11. Safety

Independence, determinism, boundedness, and fault-injection verification are safety constraints carried from the SWA tier and Vol 13 inputs. Monitoring thresholds and recovery authority are TBD. No integrity values stated.

## 12. Performance

Response-time budgets, memory budgets, and throughput budgets are TBD. Budget holders: safety software (Vol 16), safety assessment (Vol 13). No timing figures stated.

## 13. Verification & Validation

Verified by analysis (independence argument), review (monitoring-function definition, DO-178C-structured scaffolding), and fault-injection test. Validated later via integrated SIL and HIL campaigns and flight test per the VVP thread.

## 14. Risks

- Independence defeat through shared resources; mitigation: partitioning provisions plus independence analysis and fault-injection verification (WSS-001, WSS-004).
- Monitoring-function gaps; mitigation: function-definition review tied to Vol 13 safety inputs (WSS-002).

## 15. Open Issues

Partitioning mechanism, monitoring-function inventory, thresholds, recovery authority, assurance targets, and fault-injection scope all TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SYS-002 system requirements, SWA tier architecture, Vol 16 plan and architecture items, Vol 13 safety analyses, and platform partitioning provisions.

## 18. Traceability

Parents: SYS-002; SWA tier (REQ-HFPX-SWA-001..004); VVP thread. Children: safety software requirements, design, code, fault-injection cases. RTM: REQ-HFPX-WSS-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Chapter 16.4.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 16.4) |
he 6 draft (Chapter 16.3) |
