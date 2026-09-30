# Fault Recovery

**Document ID:** HFPX-AVN-FRC-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define avionics fault-recovery requirements, architecture, interfaces and verification scaffolding (Chapter 08.13). Establishes structure only; recovery actions, authority, verification and handover to fault-tolerant control are TBD and unproven.

## 2. Scope

Covers avionics fault-recovery inventory, recovery authority, recovery verification methodology, and recovery-to-FTC handover. Detection and isolation logic are owned elsewhere (Ch 08.11, 08.12); control reconfiguration execution is owned by Vol 07.18. Recovery thresholds, timings, sequences and limits are TBD. No numeric values are allocated in this document.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (notably REQ-HFPX-SYS-002, REQ-HFPX-SYS-003, REQ-HFPX-SYS-005)
- HFPX-ARC-AVN-001 Avionics Architecture
- VAA tier requirements (TBD)
- Vol 07.18 — Fault-Tolerant Control handover
- Vol 13 — safety analyses (notably SFA/CCA hooks)

## 4. Definitions & Acronyms

- Fault recovery: avionics actions restoring an operable configuration after fault detection/isolation; inventory TBD.
- Reconfiguration: reassignment of functions/paths after a fault; scope TBD.
- Restart: re-initialisation of an avionics element; scope TBD.
- Reversion: fallback to a reduced or backup mode; scope TBD.
- Recovery authority: entity empowered to command and inhibit recovery; definition TBD.
- FTC handover: transfer of recovery outcome to fault-tolerant control (Vol 07.18); criteria TBD.
- TBD: To Be Determined.

## 5. System Context

Avionics fault recovery sits between fault detection/isolation (Ch 08.11, 08.12) and fault-tolerant control (Vol 07.18). It consumes isolated-fault inputs, commands defined recovery actions under defined authority, and hands over recovered or degraded state to FTC. Safety oversight and independence claims feed SFA/CCA hooks (Vol 13). All logic, authority and timing TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-VFR-001 | The avionics fault-recovery action inventory, including reconfiguration, restart and reversion actions, shall be defined; all actions and conditions TBD. | REQ-HFPX-SYS-002, REQ-HFPX-SYS-003 | Inspection |
| REQ-HFPX-VFR-002 | Recovery authority, including command, inhibit and override provisions, shall be defined; authority allocation TBD. | REQ-HFPX-SYS-003, SFA hook | Inspection |
| REQ-HFPX-VFR-003 | Fault recovery shall be verified by fault-injection; methods, cases and acceptance criteria TBD. | VAA tier | Test |
| REQ-HFPX-VFR-004 | Recovery-to-FTC handover, including conditions, state transfer and timing, shall be defined per Vol 07.18; criteria TBD. | REQ-HFPX-SYS-005, SFA hook | Analysis + Test |

## 7. Architecture

Fault-recovery architecture (structure only): ISOLATED-FAULT INPUTS (from Ch 08.11/08.12, TBD) → RECOVERY-ACTION INVENTORY (reconfiguration, restart, reversion, TBD) under RECOVERY AUTHORITY (TBD) → RECOVERY-TO-FTC HANDOVER (Vol 07.18, TBD), with SFA/CCA hooks (Vol 13, TBD).

## 8. Detailed Design

Not applicable at CONCEPT. Recovery sequences, thresholds, timings, restart scopes, reversion modes and authority implementations are TBD and deferred. No design values stated.

## 9. Interfaces

- From fault detection/isolation (Ch 08.11, 08.12): isolated-fault inputs — TBD.
- To avionics elements: reconfiguration, restart and reversion commands — TBD.
- To recovery authority: command/inhibit/override signals — TBD.
- To FTC (Vol 07.18): handover state and transfer signals — TBD, ICD before CDR.
- To verification thread (VAA tier): fault-injection hooks — TBD.
- To Vol 13: SFA/CCA hooks — TBD.

## 10. Operational Concept

Recovery supports all avionics operating states, including degraded modes. Recovery actions execute under defined authority and hand over to FTC when applicable. No operational recovery values are stated.

## 11. Safety

Failed, spurious or mistimed recovery (wrong action, authority conflict, failed handover) is hazardous: REQ-HFPX-VFR-001 (bounded action inventory), REQ-HFPX-VFR-002 (defined authority) and REQ-HFPX-VFR-004 (handover backstop) plus SFA/CCA hooks mitigate it. No recovery capability claim is made; all behaviour is TBD and unproven at CONCEPT.

## 12. Performance

Recovery coverage, success criteria, latency and resource budgets are TBD. Budget holder: this document (REQ-HFPX-VFR-001..004) with Vol 07.18 and Vol 13. No values stated.

## 13. Verification & Validation

Verified by inspection (action inventory and authority definitions) and test (fault-injection per REQ-HFPX-VFR-003) plus analysis/test for handover (REQ-HFPX-VFR-004) per VAA tier. Cases trace to REQ-HFPX-VFR-001..004; methods and acceptance criteria TBD. No gate skipping.

## 14. Risks

- Recovery-action set unbounded or unverified; mitigation: closed inventory required by REQ-HFPX-VFR-001 with fault-injection verification.
- Authority conflicts or nuisance recovery; mitigation: defined authority with inhibit/override per REQ-HFPX-VFR-002 plus SFA hook.
- Failed handover to FTC; mitigation: defined handover per REQ-HFPX-VFR-004 aligned to Vol 07.18.

## 15. Open Issues

Recovery-action inventory and conditions, recovery authority allocation, fault-injection methods/cases/criteria, and recovery-to-FTC handover criteria are all TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SyRS SYS-002/003/005, VAA tier, fault detection (08.11), fault isolation (08.12), FTC (Vol 07.18), and Vol 13 SFA/CCA hooks.

## 18. Traceability

Parents: REQ-HFPX-SYS-002, REQ-HFPX-SYS-003, REQ-HFPX-SYS-005; VAA tier; SFA/CCA hooks. Children: detailed recovery design, authority ICDs, fault-injection evidence, handover ICD (all TBD). RTM: REQ-HFPX-VFR-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 5 draft, not baselined. Chapter 08.13.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 draft (Chapter 08.13) |
