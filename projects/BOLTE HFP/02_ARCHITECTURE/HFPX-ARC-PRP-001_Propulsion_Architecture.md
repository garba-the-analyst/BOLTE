# Propulsion Architecture

**Document ID:** HFPX-ARC-PRP-001  
**Revision:** B (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 2 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X propulsion architecture (Chapter 02.8): distributed thrust functions, allocation/mixing ownership, monitoring/thermal hooks and redundancy/fault-response ownership. Establishes structure only; propulsion chain selection is pending.

## 2. Scope

Limited to requirements, architecture, interfaces and safety analysis scaffolding for distributed arm/rear/ankle thrust functions. Explicitly excludes instructions for constructing, igniting or operating human-carrying high-energy propulsion outside appropriate controls. Chain details, counts and values TBD (ISS-003 trade not started).

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parent requirements REQ-HFPX-SYS-001..008)
- HFPX-SYS-ARC-001 SAD (parent requirements REQ-HFPX-ARC-001..005)
- Vol 06 (propulsion detail), Vol 07 (control/allocation), Vol 05 (fuel), Vol 13 (safety), Vol 17 (thermal)

## 4. Definitions & Acronyms

- Thrust allocation/mixing: conversion of FCS commands into per-effector thrust demands (ownership Vol 07).
- Distributed thrust: lift/control force from multiple arm, rear and ankle effectors (counts/positions TBD).
- ISS-003: propulsion-chain trade (energy source → thrust), not started.

## 5. System Context

Propulsion architecture converts stored energy into controlled thrust within airframe, thermal, fuel and control constraints. It receives allocation commands and produces lift, attitude moments and health status across hover/transition/cruise modes.

> **Hazardous-subsystem boundary.** This document is limited to requirements, architecture, interfaces and safety analysis. It contains no instructions for building, igniting or operating human-carrying high-energy propulsion outside appropriate controls.

## 6. Requirements

| ID | Requirement (shall) | Verification |
| --- | --- | --- |
| REQ-HFPX-PRP-001 | The propulsion architecture shall define distributed arm, rear, and ankle thrust functions (counts and positions TBD). | Inspection |
| REQ-HFPX-PRP-002 | Thrust-allocation/mixing ownership shall reside with the control architecture (Vol 07). | Inspection |
| REQ-HFPX-PRP-003 | The propulsion architecture shall define propulsion monitoring and thermal hooks (thresholds TBD). | Analysis |
| REQ-HFPX-PRP-004 | The propulsion architecture shall define redundancy and fault-response ownership for propulsion faults (details TBD, ISS-003 trade not started). | Analysis |

## 7. Architecture

Energy→thrust chain (structure only; chain type, counts and values TBD):

```text
STORED ENERGY (TBD, ISS-003) → CONDITIONING/DISTRIBUTION (TBD) → EFFECTORS [arm | rear | ankle] (TBD)
   → THRUST + MOMENTS (hover/transition/cruise demands from Vol 07 allocation)
   → MONITORING (health/thermal hooks → fault logic) → FAULT RESPONSE (ownership TBD, Vol 13)
```

Allocation/mixing is owned by Vol 07; propulsion executes demands and reports capability/health. Thermal hooks feed Vol 17; fuel interfaces feed Vol 05. Redundancy concept and degraded-mode behaviour await ISS-003 trade and Vol 13 analysis.

## 8. Detailed Design

Not applicable at this level. Effector designs, plumbing/routing, mounts and control effector sizing are deferred to Vol 06 (with Vol 03/05/07/17 inputs). No design values stated.

## 9. Interfaces

Propulsion interfaces: P-CMD (allocation demands from Vol 07), P-HLTH (health/thermal status to fault logic), P-FUEL (energy/mass flow, Vol 05), P-MECH (mounts/loads, Vol 03), P-PWR (electrical feeds/control power, Vol 15), P-THM (thermal interfaces, Vol 17). Definitions TBD in ICDs (02.17).

> **Hazardous-subsystem boundary.** Interface definitions here describe architectural boundaries and analysis inputs only, not build/ignition/operation procedures.

## 10. Operational Concept

Propulsion functions execute across all flight modes; hover stresses vertical thrust and control margins, transition stresses re-allocation dynamics, cruise stresses efficiency and thermal behaviour. Start-up/shutdown and emergency sequencing concepts are TBD under Vol 06/07/13 control.

## 11. Safety

Propulsion fault detection, redundancy and abort/recovery commanding feed Vol 13 FHA/FMEA/FTA. Independent safety-path authority over propulsion (limits, shutdown, recovery) is preserved per ARC-003. Analysis only; no operating instructions.

## 12. Performance

Thrust, control-authority, efficiency and thermal budgets are TBD. Budget holders: propulsion (Vol 06, ISS-007), control authority (Vol 07, ISS-006), thermal (Vol 17). No values stated.

## 13. Verification & Validation

Verified by inspection (function definition, ownership) and analysis (monitoring/redundancy concepts). Validated later via modelling, rig test, SIL/HIL and unmanned flight (Vol 19/33). Test methodology only; no operational procedures.

## 14. Risks

- ISS-003 trade delay stalls propulsion-dependent views; mitigation: structure-only architecture with explicit TBDs.
- Allocation/monitoring ownership ambiguity; mitigation: ownership fixed to Vol 07 with Vol 13 fault-response review.

## 15. Open Issues

ISS-003 (propulsion chain unknown — trade not started), effector counts/positions, monitoring thresholds, redundancy scope and fault-response details all TBD.

## 16. Assumptions


_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on ISS-003 trade, control allocation (Vol 07), fuel/thermal/power inputs (Vol 05/17/15), airframe mounts (Vol 03), and safety analyses (Vol 13).

## 18. Traceability

Parents: SyRS REQ-HFPX-SYS-001..008; SAD REQ-HFPX-ARC-001..005 (notably ARC-001/002/003/004). Children: Vol 03–18 subsystem docs (esp. Vol 05/06/07/13/17), ICDs. RTM: REQ-HFPX-PRP-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 2 draft, not baselined. Chapter 02.8.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 2 draft (Chapter 02.8) |
| B | 2026-09-29 | Assumptions removed; all unknowns recorded as TBD (no assumptions raised or relied upon). |
