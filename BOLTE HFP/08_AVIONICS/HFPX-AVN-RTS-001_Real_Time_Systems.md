# Real-Time Systems

**Document ID:** HFPX-AVN-RTS-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define HFP-X avionics real-time principles (Chapter 08.5): scheduling policy, deadline-miss handling, determinism evidence, and verification approach. No schedules, allocations, or values stated.

## 2. Scope

Covers scheduling policy, deadline-miss handling principles, determinism evidence structure, and verification by analysis and HIL. Excludes task design, allocation, tuning, and quantitative timing values (all TBD).

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parent requirements REQ-HFPX-SYS-002, REQ-HFPX-SYS-003, REQ-HFPX-SYS-005)
- HFPX-SYS-ARC-001 SAD (AVN, HWA, SWA, DAT views)
- HFPX-AVN-ARC-001 Avionics Architecture (Chapter 08.1)
- HFPX-AVN-FLC-001 Flight Computer (Chapter 08.2 context)

## 4. Definitions & Acronyms

- Real-time system: computing behaviour subject to timing obligations.
- Scheduling policy: rules governing execution ordering and pre-emption.
- Deadline miss: failure to complete required behaviour within its timing obligation.
- HIL: hardware-in-the-loop verification concept.

## 5. System Context

Real-time principles apply to flight and safety computing paths and their interfaces across flight and maintenance states. Execution platforms and allocations are TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-VRT-001 | The avionics real-time design shall define a scheduling policy (policy details and execution rates TBD). | REQ-HFPX-SYS-003; SAD SWA view | Analysis |
| REQ-HFPX-VRT-002 | The avionics real-time design shall define deadline-miss handling (detection and response TBD). | REQ-HFPX-SYS-003; SAD SWA view | Analysis |
|REQ-HFPX-VRT-003|The avionics real-time design shall define determinism evidence (artefacts TBD).|REQ-HFPX-SYS-005; SAD SWA view|Inspection|
| REQ-HFPX-VRT-004 | The avionics real-time design shall be verified by analysis and HIL (cases and coverage TBD). | REQ-HFPX-SYS-005; SAD AVN view | Test |

## 7. Architecture

Scheduling and timing concept (details TBD): policy statement, miss-handling principles, and evidence structure. No tasks, priorities, allocations, or values defined.

## 8. Detailed Design

Not applicable at this revision. Task design, allocation, and tuning are deferred to later tranches.

## 9. Interfaces

Timing interfaces: scheduling obligations across software, hardware, and data exchanges. Definitions are TBD.

## 10. Operational Concept

Real-time behaviour is required across flight modes plus built-in test, degraded, and maintenance states. Miss-handling behaviour per mode is TBD.

## 11. Safety

Scheduling discipline, miss handling, and determinism evidence support parent safety intent. No safety values stated.

## 12. Performance

Timing budgets and margins are TBD. No values stated.

## 13. Verification & Validation

Verified by analysis (schedulability and miss-handling arguments, details TBD) and HIL with cases and coverage TBD. Review covers determinism evidence structure.

## 14. Risks

- Timing overruns discovered late; mitigation: early analysis thread with HIL confirmation.
- Miss-handling gaps across modes; mitigation: per-mode handling definitions with review gate.

## 15. Open Issues

Scheduling policy, miss-handling details, determinism artefacts, and verification cases are all TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SyRS, SAD AVN/HWA/SWA/DAT views, Chapters 08.1–08.2, and verification environments.

## 18. Traceability

Parents: REQ-HFPX-SYS-002, REQ-HFPX-SYS-003, REQ-HFPX-SYS-005; SAD AVN/HWA/SWA/DAT views. Children: Vol 08 software/verification detail. RTM: REQ-HFPX-VRT-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 5 draft, not baselined. Chapter 08.5.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 draft (Chapter 08.5) |
