# Fault Management

**Document ID:** HFPX-SW-FTM-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X fault-management software scope (Chapter 16.12): detect-to-isolate-to-recover chain, authority provisions, fault-injection verification, and flight-control hooks. No implementation stated.

## 2. Scope

Covers fault-management software requirements, architecture placement, interfaces, and verification planning. Fault-tolerant control detail is TBD per Vol 07.18. Excludes hardware redundancy design (Vol 08), safety analysis detail (Vol 13), and detailed display design (Vol 10).

## 3. Applicable Documents

- Parent requirements: SYS-002 thread; WDP/WSA tier; VVP thread
- HFPX-ARC-SW-001 Software Architecture (layering, determinism policy, assurance structured according to DO-178C concepts)
- Vol 07 control definition, notably Vol 07.18 (fault-tolerant control hooks, TBD)
- Vol 13 safety inputs; Vol 16 sibling software chapters; Vol 22/23 verification threads
- DO-178C concepts (structured-according-to only, no compliance claimed at this stage)

## 4. Definitions & Acronyms

- Detect-isolate-recover chain: progression from fault detection through isolation to recovery action (steps and criteria TBD).
- Authority: the permitted scope of automatic fault-management action versus crew or ground intervention (allocation TBD).
- Fault injection: deliberate introduction of faults to verify detection, isolation, and recovery behaviour (scope and environments TBD).
- FTC hooks: interfaces to fault-tolerant control functions per Vol 07.18 (TBD).

## 5. System Context

Fault-management software executes within the layered software architecture and interfaces with health monitoring, control, propulsion, communications, and display/logging services. It receives health and state inputs and produces isolation commands, recovery actions, and status outputs across nominal and degraded states (states and signals TBD).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-WFM-001 | The fault-management software shall implement a detect-to-isolate-to-recover chain for handled faults (chain and criteria TBD). | SYS-002; WDP/WSA tier; VVP thread | Analysis + Test |
| REQ-HFPX-WFM-002 | The fault-management software shall observe defined authority limits for automatic detection, isolation, and recovery actions (authority TBD). | SYS-002; WDP/WSA tier; VVP thread | Inspection + Analysis |
| REQ-HFPX-WFM-003 | Verification of fault-management behaviour shall include fault injection (scope and environments TBD). | SYS-002; WDP/WSA tier; VVP thread | Test |
| REQ-HFPX-WFM-004 | The fault-management software shall provide hooks to fault-tolerant control functions per Vol 07.18 (hooks TBD). | SYS-002; WDP/WSA tier; VVP thread | Inspection |

Software assurance is structured according to DO-178C concepts; no compliance is claimed at this stage and no integrity values are stated.

## 7. Architecture

Fault-management software resides in the application/services layers defined by HFPX-ARC-SW-001, coordinated with the safety layer as applicable (allocation TBD). Detection, isolation, recovery, and authority-enforcement functions are partitioned per determinism and independence policy (TBD). Languages, RTOS selection, and partitioning mechanisms are TBD.

## 8. Detailed Design

Not applicable at this revision. Software requirements, design descriptions, fault lists, recovery sequences, and code are deferred to later Vol 16 detail. No implementation, logic, or parameter values stated.

## 9. Interfaces

Software interfaces to health-monitoring outputs, control FTC hooks (Vol 07.18), actuator and mode services, annunciation consumers, and logging services are TBD. Signatures, timing, and protocols are TBD and will be detailed in software ICDs.

## 10. Operational Concept

Fault management operates across power-up, flight-mode, degraded-mode, and maintenance states (behaviour per state TBD). Automatic recovery remains bounded by authority limits with crew and ground override provisions as defined (TBD). Recovery sequencing and reconfiguration policy are TBD.

## 11. Safety

Fault-management software safety inputs, hazard contributions, incorrect-recovery and authority-exceedance considerations feed Vol 13 analyses (all TBD). No integrity values stated. Determinism, boundedness, and partition independence remain architecture constraints per HFPX-ARC-SW-001.

## 12. Performance

Timing (detection latency, isolation and recovery response), memory, and throughput budgets for fault management are TBD. Budget holders: software/compute (Vol 16/08), control (Vol 07). No values stated.

## 13. Verification & Validation

Verified by analysis and test (chain behaviour, authority enforcement) including fault injection, structured according to DO-178C concepts with no compliance claimed. Detailed verification cases, SIL/HIL environments, and flight-test hooks are TBD per the VVP thread and Vol 19/22/23.

## 14. Risks

- Incomplete fault chain (detection without assured isolation or recovery); mitigation: end-to-end chain requirement WFM-001.
- Authority exceedance by automatic recovery; mitigation: authority-limit requirement WFM-002 with Vol 13 review.
- Verification without representative fault injection; mitigation: fault-injection requirement WFM-003.

## 15. Open Issues

Detect-isolate-recover chain steps and criteria TBD. Authority allocation TBD. Fault-injection scope, environments, and pass criteria TBD. FTC hooks per Vol 07.18 TBD.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on control definition including Vol 07.18, software architecture layering (HFPX-ARC-SW-001), health monitoring (Chapter 16.11), safety analyses (Vol 13), and VVP planning (Vol 22/23).

## 18. Traceability

Parents: SYS-002 thread; WDP/WSA tier; VVP thread. Children: subsystem software requirements, design descriptions, ICDs, V&V cases (all TBD). RTM: REQ-HFPX-WFM-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Chapter 16.12.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 16.12) |
