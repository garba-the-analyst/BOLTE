# MVP Objectives

**Document ID:** HFPX-MVP-OBJ-001  
**Revision:** B (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 1 draft, not baselined; Vol 33 separate from production  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define what the Minimum Viable Prototype must prove, in what order, and what "done" looks like — without letting prototype shortcuts leak into the production baseline. Owns Chapter 33.1.

## 2. Scope

Covers the unmanned-first demonstrator programme: simulation → SIL → HIL → subsystem → integrated propulsion → unmanned hover → transition → horizontal flight → integrated mission → tethered human → controlled human flight → envelope expansion (DDR-001). Excludes production design decisions (governed by 33.20 transition).

## 3. Applicable Documents

- DDR-001 (unmanned-first); HFPX-SYS-MIS-001/OPC-001/CON-001/STK-001 (mission sources)
- HFPX-SYS-REQ-001 SyRS (stub); HFPX-SYS-ARC-001 SAD (stub)
- Future: 33.2 MVP requirements, 33.3 MVP architecture, 33.13/33.14 test programmes, 33.19 exit criteria, 33.20 transition; Vol 23 test programme; Vol 13 safety

## 4. Definitions & Acronyms

- MVP: Minimum Viable Prototype — smallest system that retires the load-bearing risks (ISS-006/007/008)
- Gates: mandatory evidence thresholds; skipping gates is prohibited (prompt §17)
- Tethered human: restrained/human-proximate testing only after unmanned transition evidence (criteria TBD)

## 5. System Context

MVP sits beside, not inside, the production baseline:

```text
PRODUCTION BASELINE (BL-0.x, Vol 00–32) ←── lessons/data only ── MVP (Vol 33, separate rigs/airframes)
         ↑                                              ↑
    33.20 transition gate                        unmanned demonstrator + ground station + instrumentation
```

> This volume is SEPARATE from the production-aircraft documentation (schema note). Production-design transition is governed by 33.20.

## 6. Requirements

| ID | Requirement (shall) | Verification |
| --- | --- | --- |
| REQ-HFPX-MVP-001 | The MVP shall demonstrate unmanned hover, transition and horizontal flight before any human-proximate testing. | Test |
| REQ-HFPX-MVP-002 | The MVP shall collect flight, propulsion, structural, thermal and control data sufficient to validate first-order models (data set TBD). | Inspection |
| REQ-HFPX-MVP-003 | The MVP shall retire or bound ISS-006 (control authority), ISS-007 (mass/thrust/energy) and ISS-008 (recovery) to defined exit criteria (criteria TBD, 33.19). | Analysis + Test |
| REQ-HFPX-MVP-004 | Prototype propulsion and safety testing shall progress only through controlled ground → unmanned stages under appropriate engineering, test, safety and regulatory controls. | Demonstration |
| REQ-HFPX-MVP-005 | No prototype component or value shall enter the production baseline except via 33.20 transition with requirements, verification and safety review. | Inspection |

## 7. Architecture

MVP architecture (placeholder, detailed in 33.3): representative airframe (mass/inertia representative per DDR-001 risk note, method TBC), prototype propulsion (33.6), prototype avionics/compute/sensors (33.7–33.9), prototype ground station (33.10), prototype safety system (33.11), test instrumentation (33.12). Representativeness criteria TBD.

## 8. Detailed Design

Not applicable — prototype configuration is 33.4 (TBD). Experimental components list is 33.5 (TBD).

## 9. Interfaces

MVP interfaces: range/test infrastructure (Vol 23), telemetry/instrumentation (33.12), ground station (33.10), production baseline via 33.20 data/decision handover only.

## 10. Operational Concept

Gated progression (prompt §17) is the operational concept: each stage has entrance criteria, required evidence and abort rules (all TBD in 33.13/33.14). Tethered-human and controlled-human stages require FRR-level authorisation (criteria TBD).

## 11. Safety

MVP safety is governed by prototype safety system (33.11) + Vol 13 analyses + range safety (Vol 23). Recovery-system limits (ISS-008) constrain MVP envelopes from the first flight. Hazardous-subsystem boundary applies: requirements/architecture/modelling/simulation/interfaces/test-methodology/safety analysis only — no build/ignition/operation instructions outside controlled conditions (prompt §§14, 34).

## 12. Performance

MVP performance targets are TBD and instrument-relative (e.g. "demonstrate transition", not "cruise at X"). No speed/range/endurance figure is set. Exit thresholds live in 33.19 (TBD).

## 13. Verification & Validation

MVP objectives verified by: gate evidence review (did each stage produce its data set?), model validation (Vol 19), lessons-learned capture (33.17). MVP success does not equal production verification; production V&V is separate (Vol 22).

## 14. Risks

- Demonstrator non-representativeness (DDR-001 risk) → false confidence; mitigation: representativeness criteria + method TBC before first flight
- Prototype shortcuts (parts, software, safety) mistaken for production solutions; mitigation: MVP-005 + 33.20 gate
- Schedule pressure to skip gates; mitigation: gates are programme requirements (REQ-HFPX-PGM-003, MVP-001)

## 15. Open Issues

ISS-006/007/008 (MVP exists to retire these). New TBDs: representativeness method, instrumentation list, range selection, exit criteria (33.19).

## 16. Assumptions


_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on modelling (Vol 19), ground-test capability (33.13), avionics/compute prototypes (33.7/33.8), regulatory authorisation (Vol 25), range safety (Vol 23).

## 18. Traceability

Parent: Charter PGM-003, Mission MIS-006, DDR-001. Children: 33.2 MVP requirements, 33.3 architecture, 33.13/33.14 programmes, 33.19 exit criteria, 33.20 transition. RTM: REQ-HFPX-MVP-001..005 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 1 draft, CONCEPT, not baselined; Vol 33 items never auto-promote to production baselines.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 1 draft (Chapter 33.1) |
| B | 2026-09-29 | Assumptions removed; all unknowns recorded as TBD (no assumptions raised or relied upon). |
