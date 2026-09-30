# Concept of Operations (CONOPS)

**Document ID:** HFPX-SYS-CON-001  
**Revision:** B (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 1 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Walk through HFP-X missions step by step — nominal and off-nominal — so requirements, architecture and test plans share one scenario baseline. Owns Chapter 01.3.

## 2. Scope

Covers the 15 flight modes end to end for the unmanned demonstrator and (gated) human objective. Excludes detailed procedures (Vol 26), test scripts (Vol 23) and design values (all TBD).

## 3. Applicable Documents

- HFPX-SYS-MIS-001 Mission Definition; HFPX-SYS-OPC-001 Operational Concept; HFPX-SYS-STK-001 Stakeholder Requirements
- HFPX-SYS-REQ-001 SyRS (stub); HFPX-SYS-ARC-001 SAD (stub); HFPX-MVP-OBJ-001 MVP Objectives
- HFP prompt §§13, 17 (flight modes, MVP progression)

## 4. Definitions & Acronyms

- Nominal: planned mission thread; Off-nominal: faults, aborts, emergency stabilisation/recovery, safe/aborted state
- SIL/HIL: software/hardware-in-the-loop; 6-DOF: six-degree-of-freedom flight model

## 5. System Context

Scenario actors: air vehicle (SYS-01..SYS-23), operator/pilot, ground crew, ground station, range. Scenario preconditions: authorised range, qualified personnel (criteria TBD), vehicle configured per 33.4/Vol 21, envelopes TBD.

## 6. Requirements

| ID | Requirement (shall) | Verification |
| --- | --- | --- |
| REQ-HFPX-CON-001 | CONOPS shall define the nominal thread: pre-flight → start → ground idle → hover → hover manoeuvre → transition → horizontal acceleration → cruise → horizontal deceleration → reverse transition → landing → shutdown. | Inspection |
| REQ-HFPX-CON-002 | CONOPS shall define off-nominal threads for propulsion fault, control degradation, comms/telemetry loss, navigation degradation and recovery-system deployment (thresholds TBD). | Analysis |
| REQ-HFPX-CON-003 | Transition and reverse-transition scenarios shall state entry/exit conditions, control-law switching and abort criteria (values TBD, laws TBD). | Analysis + Test |
| REQ-HFPX-CON-004 | Every scenario shall identify the detecting system, the mitigating system and the crew/operator action. | Inspection |
| REQ-HFPX-CON-005 | Human-carrying scenarios shall be gated on completed unmanned scenarios for the same segment (DDR-001). | Inspection |

## 7. Architecture

State machine (starter, thresholds TBD):

```text
PRE-FLIGHT → START → GROUND IDLE → HOVER ⇄ HOVER MANOEUVRE → TRANSITION → CRUISE
   ↓             ↓          ↓           ↓            ↓              ↓         ↓
 ABORT ←──── EMERGENCY STABILISATION ←──────────────┴──────────────┴──→ EMERGENCY RECOVERY → SAFE/ABORTED
```

Control-law sets for hover, transition and cruise are distinct (prompt §13) and owned by Vol 07 / SAD control view.

## 8. Detailed Design

Nominal thread (starter — detail TBD in Vol 26): pre-flight inspection → fuel/power checks → engine start → ground idle health check → lift to hover → hover manoeuvre box → transition run → cruise leg → reverse transition → vertical landing → shutdown → post-flight. Off-nominal threads: any fault → detect (health monitoring, Vol 08/16) → stabilise (safety computer) → abort to hover/landing or deploy recovery (Vol 13) → safe state. Timings, speeds, altitudes: TBD.

## 9. Interfaces

Scenario interfaces: HMI alerts (Vol 10.11/10.12), telemetry displays (Vol 11), flight-termination/abort authority (TBD, Vol 13/23), range safety (Vol 23/25).

## 10. Operational Concept

This document is the scenario layer of the operational concept: if a scenario cannot be walked here (actor, trigger, response, end state), the corresponding requirement, interface or test cannot be written downstream.

## 11. Safety

Scenarios assume no recovery capability until proven (ISS-008). Low-altitude hover scenarios are the limiting safety case and shall drive envelope constraints. No hazardous test/operation instructions are given (prompt §§14, 34); test methodology lives in Vol 23 under gated progression.

## 12. Performance

Scenario performance (durations, distances, altitudes, speeds) is TBD. Success criteria for each scenario are TBD and will be set with verification IDs in the SyRS/V&V Plan.

## 13. Verification & Validation

CONOPS verified by stakeholder walkthrough and SRR inspection (every flight mode has ≥1 scenario; every scenario has detection/mitigation/action). Later validated by unmanned flight (Vol 33.14/33.15) matching scenario threads.

## 14. Risks

- Scenario–design mismatch (scenarios assume capability the design lacks, e.g. transition authority ISS-006); mitigation: 6-DOF model gates scenario approval
- Comms-loss mid-transition undefined; mitigation: Vol 11.9 behaviour + FHA (Vol 13.4)

## 15. Open Issues

ISS-002 (CONOPS unapproved), ISS-006 (transition authority), ISS-008 (recovery). New TBDs: abort authority, flight-termination, range criteria.

## 16. Assumptions


_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on flight-control architecture (Vol 07), safety analyses (Vol 13), comms design (Vol 11), envelope models (Vol 06/19), test range (Vol 23).

## 18. Traceability

Parent: Mission (MIS) + Operational Concept (OPC). Children: SyRS functional/performance requirements, SAD functional/logical views, V&V scenarios, Vol 26 procedures. RTM: REQ-HFPX-CON-001..005 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 1 draft, CONCEPT, not baselined.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 1 draft (Chapter 01.3) |
| B | 2026-09-29 | Assumptions removed; all unknowns recorded as TBD (no assumptions raised or relied upon). |
