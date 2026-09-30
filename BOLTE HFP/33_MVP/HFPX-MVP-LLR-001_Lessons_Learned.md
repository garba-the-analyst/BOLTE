# Lessons Learned

**Document ID:** HFPX-MVP-LLR-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined; Vol 33 separate from production  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the planning framework for MVP lessons-learned capture, review, action tracking, and records control. Owns Chapter 33.17.

This document is planning/methodology only. It does not contain test-execution or flight-execution instructions.

## 2. Scope

Covers planning for capturing observations from ground-test (33.13), unmanned-test (33.14), transition-demonstration (33.15), experimental-data (33.16), and design-iteration (33.18) activities, and for converting them into tracked actions and controlled records. Excludes execution-level activity conduct and production process decisions (governed by 33.20 transition).

Gated progression is mandatory (DDR-001): no stage shall be skipped; human-proximate stages require prior unmanned evidence plus authorisation TBD; lessons status does not bypass gates.

## 3. Applicable Documents

- DDR-001 (unmanned-first); HFPX-MVP-OBJ-001 (Chapter 33.1, MVP-001..MVP-005)
- Future: 33.2 MVP requirements, 33.13/33.14/33.15/33.16 evidence sources, 33.18 design iteration, 33.19 exit criteria, 33.20 transition
- Vol 23 test programme; Vol 13 safety; Vol 19 modelling

## 4. Definitions & Acronyms

- MVP: Minimum Viable Prototype — smallest system that retires the load-bearing risks (ISS-006/007/008)
- Lessons learned: planned outputs converting observations into findings, actions, and controlled records
- Capture process: planned methodology for recording observations and findings (details TBD)
- Review cadence: planned frequency and entry/exit methodology for lessons reviews (details TBD)
- Action tracking: planned methodology for assigning, following, and closing actions (details TBD)

## 5. System Context

Lessons learned connect MVP evidence to iteration, exit, and controlled transition without entering the production baseline directly:

```text
33.13 / 33.14 / 33.15 / 33.16 ── observations ──► LESSONS LEARNED (33.17) ── actions/records ──► 33.18 ITERATION / 33.19 EXIT / 33.20 HANDOVER
```

> This volume is SEPARATE from the production-aircraft documentation. Production-design transition is governed by 33.20.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-MLL-001 | The lessons-learned plan shall define the capture process for observations and findings across scoped MVP activities (process TBD). | MVP-002; MRQ/MAR tier; VVP thread | Inspection |
|REQ-HFPX-MLL-002|The lessons-learned plan shall define the review cadence and associated entry/exit methodology (cadence TBD).|MVP-002; MRQ/MAR tier; VVP thread|Inspection|
|REQ-HFPX-MLL-003|The lessons-learned plan shall define action-tracking methodology through to closure (methodology TBD).|MVP-003; MRQ/MAR tier; VVP thread|Inspection|
| REQ-HFPX-MLL-004 | The lessons-learned plan shall define records-control methodology for lessons, actions, and decisions (records TBD). | MVP-002; MRQ/MAR tier; VVP thread | Inspection |

Gated progression applies to all requirements above: no stage skipped; human-proximate stages require prior unmanned evidence plus authorisation TBD.

## 7. Architecture

Lessons-learned architecture (planning view, TBD): capture-to-review-to-action-to-record chain, repository structure methodology, linkage to evidence sources (33.13–33.16) and consumers (33.18, 33.19, 33.20). No repository implementation or tooling selection is defined in this document.

## 8. Detailed Design

Not applicable — this document defines only the planning artefacts and methodology to be produced. Evidence-source detail is owned by 33.13–33.16 (TBD); iteration mechanics are 33.18 (TBD).

## 9. Interfaces

Planning interfaces: MVP requirements (33.2), ground/unmanned/demonstration/data planning (33.13/33.14/33.15/33.16), design-iteration planning (33.18), exit-criteria planning (33.19), Vol 23 and Vol 13 inputs as applicable, production baseline via 33.20 data/decision handover only.

## 10. Operational Concept

Gated progression governs lessons use: reviews are entered through defined entry methodology and exited through defined closure methodology (all TBD in the lessons plan); open actions are visible at gates but do not themselves authorise progression. Human-proximate stages require prior unmanned evidence plus authorisation TBD. Execution-level activity conduct is excluded.

## 11. Safety

Lessons-learned planning supports safety learning by routing safety-relevant findings to prototype safety planning (33.11) and Vol 13 analyses; it does not itself authorise activity progression or modify safety controls. Hazardous-subsystem boundary applies: this document covers requirements, planning methodology, interfaces, and safety-analysis inputs only — no build, operation, test-execution, or flight-execution instructions.

## 12. Performance

No performance targets are set in this document. Review-effectiveness and action-closure thresholds are TBD. No quantitative closure-time, coverage, or effectiveness figure is stated.

## 13. Verification & Validation

This planning document is verified by inspection/review of the lessons-plan artefacts (capture process, review cadence, action-tracking methodology, records-control methodology). Effectiveness of lessons application is assessed separately through iteration and exit evidence; MVP lessons do not equal production verification (Vol 22, separate).

## 14. Risks

- Undefined capture → lost learning; mitigation: capture-process requirement (REQ-HFPX-MLL-001)
- Undefined cadence → stale or rushed findings; mitigation: defined review cadence and entry/exit methodology (REQ-HFPX-MLL-002)
- Untracked actions → repeated issues; mitigation: action-tracking methodology through closure (REQ-HFPX-MLL-003)
- uncontrolled records → untraceable decisions; mitigation: records-control methodology (REQ-HFPX-MLL-004)

## 15. Open Issues

Capture process TBD; review cadence TBD; action-tracking methodology TBD; records-control methodology TBD. Linked TBDs: evidence-source readiness (33.13–33.16), iteration linkage (33.18), exit-evidence linkage (33.19).

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on MVP requirements (33.2), evidence-source planning (33.13/33.14/33.15/33.16), design-iteration planning (33.18), exit-criteria planning (33.19), and applicable Vol 23 and Vol 13 inputs.

## 18. Traceability

Parent: MVP-001..MVP-005 (HFPX-MVP-OBJ-001); MRQ/MAR tier; VVP thread. Children: lessons-plan artefacts, action/record inputs to 33.18 iteration, evidence inputs to 33.19 exit, handover inputs to 33.20. RTM: REQ-HFPX-MLL-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined; Vol 33 items never auto-promote to production baselines (MVP-005, 33.20 gate applies).

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 33.17) |
