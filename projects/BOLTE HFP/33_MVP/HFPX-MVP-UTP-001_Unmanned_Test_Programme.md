# Unmanned-Test Programme

**Document ID:** HFPX-MVP-UTP-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined; Vol 33 separate from production  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the planning framework for the MVP unmanned-test programme, including build-up structure, envelope-progression methodology, and mishap-rule planning inputs. Owns Chapter 33.14.

This document is planning/methodology only. It does not contain test-execution or flight-execution instructions.

## 2. Scope

Covers planning for unmanned demonstrator activities from hover through transition to cruise and integrated mission (sequence TBD), following completed ground-test gates (33.13). Excludes flight-execution procedures, ground-test execution (33.13), transition-demonstration success adjudication (33.15), and production design decisions (governed by 33.20 transition).

Gated progression is mandatory (DDR-001): no stage shall be skipped; human-proximate stages require prior unmanned evidence plus authorisation TBD.

## 3. Applicable Documents

- DDR-001 (unmanned-first); HFPX-MVP-OBJ-001 (Chapter 33.1, MVP-001..MVP-005)
- Future: 33.2 MVP requirements, 33.3 MVP architecture, 33.13 ground-test programme, 33.15 transition demonstration, 33.16 experimental data, 33.19 exit criteria, 33.20 transition
- Vol 23 test programme, including Vol 23.11 hooks (TBD); Vol 13 safety; Vol 06 flight characteristics inputs (as applicable); Vol 19 modelling

## 4. Definitions & Acronyms

- MVP: Minimum Viable Prototype — smallest system that retires the load-bearing risks (ISS-006/007/008)
- Unmanned-test programme: planned set of unmanned demonstrator activities and associated build-up, envelope, and evidence methodology
- Build-up: ordered progression methodology across planned stages; skipping stages is prohibited
- Vol 23.11 hooks: defined interfaces to the referenced test-programme volume (details TBD)
- Mishap rule: planned post-event handling and re-entry methodology (details TBD)

## 5. System Context

Unmanned testing is the central gated path between ground evidence and any human-proximate consideration:

```text
GROUND EVIDENCE (33.13) ── gates ──► UNMANNED-TEST PROGRAMME (33.14) ── evidence ──► TRANSITION DEMO (33.15) / EXIT (33.19)
                                              │
                                              └──── lessons/data only ──► PRODUCTION BASELINE via 33.20 gate ──► (no auto-promotion per MVP-005)
```

> This volume is SEPARATE from the production-aircraft documentation. Production-design transition is governed by 33.20.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-MUT-001 | The unmanned-test programme plan shall define the build-up methodology across planned stages (build-up TBD). | MVP-001; MRQ/MAR tier; VVP thread | Inspection |
| REQ-HFPX-MUT-002 | The unmanned-test programme shall define the envelope-progression methodology from hover through transition to cruise and integrated mission, with no stage skipped (progression TBD). | MVP-001; MRQ/MAR tier; VVP thread | Inspection |
|REQ-HFPX-MUT-003|The unmanned-test programme shall define interface hooks to Vol 23.11 for applicable test capabilities and evidence exchange (hooks TBD).|MVP-004; MRQ/MAR tier; VVP thread|Inspection|
|REQ-HFPX-MUT-004|The unmanned-test programme shall define the mishap-rule methodology governing post-event handling and re-entry into the gated sequence (rule TBD).|MVP-004; MRQ/MAR tier; VVP thread|Inspection|

Gated progression applies to all requirements above: human-proximate stages require prior unmanned evidence plus authorisation TBD.

## 7. Architecture

Unmanned-test programme architecture (planning view, TBD): programme plan structure, build-up taxonomy, envelope-framework linkage, evidence-capture chain to instrumentation (33.12) and experimental data (33.16). Representativeness criteria TBD. No flight-article configuration or execution routing is defined in this document.

## 8. Detailed Design

Not applicable — prototype configuration is 33.4 (TBD); propulsion, avionics, compute, and sensor prototypes are 33.6–33.9 (TBD). This document defines only the planning artefacts and methodology to be produced.

## 9. Interfaces

Planning interfaces: MVP requirements (33.2), MVP architecture (33.3), ground-test planning (33.13), test instrumentation planning (33.12), ground-station planning (33.10), safety-system planning (33.11), experimental data planning (33.16), Vol 23.11 test-programme interfaces (hooks TBD), production baseline via 33.20 data/decision handover only.

## 10. Operational Concept

Gated progression is the operational concept for unmanned testing: each planned stage specifies entrance criteria, required evidence, and exit criteria (all TBD in the programme plan). Build-up proceeds only through satisfied gates; no stage is skipped. Human-proximate stages require prior unmanned evidence plus authorisation TBD. Execution-level conduct, control inputs, and abort execution are excluded.

## 11. Safety

MVP unmanned-test planning is governed by prototype safety system planning (33.11) plus Vol 13 analyses plus range/test safety controls (Vol 23). Recovery-system limits (ISS-008) constrain planned envelopes from the first planned flight. Hazardous-subsystem boundary applies: this document covers requirements, planning methodology, interfaces, and safety-analysis inputs only — no build, operation, test-execution, or flight-execution instructions.

## 12. Performance

No performance targets are set in this document. Envelope thresholds and mission-success thresholds are TBD and linked to MVP exit criteria (33.19, TBD). No speed, range, endurance, altitude, or environmental figure is stated.

## 13. Verification & Validation

This planning document is verified by inspection/review of the programme-plan artefacts (build-up methodology, envelope-progression framework, Vol 23.11 hook definitions, mishap-rule methodology). Execution results are verified separately under the defined methodology; MVP success does not equal production verification (Vol 22, separate).

## 14. Risks

- Undefined build-up → unstructured progression and gate bypass pressure; mitigation: build-up methodology requirement (REQ-HFPX-MUT-001) plus no-skip rule
- Undefined envelope progression → false confidence in transition and cruise readiness; mitigation: ordered progression methodology (REQ-HFPX-MUT-002)
- Unmanaged Vol 23.11 dependencies → range or capability gaps; mitigation: explicit hook definitions (REQ-HFPX-MUT-003)
- Absent mishap rule → inconsistent post-event decisions; mitigation: defined mishap-rule methodology (REQ-HFPX-MUT-004)

## 15. Open Issues

Build-up TBD; hover-to-transition-to-cruise-to-mission progression TBD; Vol 23.11 hooks TBD; mishap rule TBD. Linked TBDs: entrance/exit criteria, instrumentation list (33.12), exit criteria (33.19), ISS-006/007/008 retirement linkage.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on MVP requirements (33.2), MVP architecture (33.3), ground-test evidence planning (33.13), prototype configuration and subsystems (33.4, 33.6–33.9), ground station and safety-system planning (33.10, 33.11), instrumentation planning (33.12), Vol 23 test-programme capability (including Vol 23.11), Vol 13 safety inputs, and regulatory authorisation inputs (Vol 25, as applicable).

## 18. Traceability

Parent: MVP-001..MVP-005 (HFPX-MVP-OBJ-001); MRQ/MAR tier; VVP thread. Children: unmanned-test programme plan artefacts, evidence inputs to 33.15 transition demonstration, data inputs to 33.16, lessons inputs to 33.17, exit-evidence inputs to 33.19. RTM: REQ-HFPX-MUT-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined; Vol 33 items never auto-promote to production baselines (MVP-005, 33.20 gate applies).

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 33.14) |
