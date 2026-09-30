# Production-Design Transition

**Document ID:** HFPX-MVP-PDT-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined; Vol 33 separate from production  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the planning framework for transition from MVP evidence to production design, including transition gating, data/decision handover, production re-verification needs, and the non-promotion rule. Owns Chapter 33.20.

This document is planning/methodology only. It does not contain test-execution or flight-execution instructions.

## 2. Scope

Covers planning for the controlled transfer of MVP lessons and data into production-design activities. Excludes production design decisions themselves (owned by the production baseline, Vol 00–32), execution-level activity conduct, and any automatic transfer of prototype components or values into production.

Gated progression is mandatory (DDR-001): no stage shall be skipped; human-proximate stages require prior unmanned evidence plus authorisation TBD; transition does not bypass MVP exit (33.19).

## 3. Applicable Documents

- DDR-001 (unmanned-first); HFPX-MVP-OBJ-001 (Chapter 33.1, MVP-001..MVP-005, including MVP-005 non-promotion rule)
- Future: 33.2 MVP requirements, 33.3 MVP architecture, 33.13–33.18 evidence and iteration sources, 33.19 exit criteria
- Production baseline documents (Vol 00–32, as applicable); Vol 13 safety; Vol 19 modelling; Vol 22 V&V (production); Vol 23 test programme

## 4. Definitions & Acronyms

- MVP: Minimum Viable Prototype — smallest system that retires the load-bearing risks (ISS-006/007/008)
- Production-design transition: planned gated transfer of MVP data and decisions into production-design activities (execution and production decisions excluded)
- Transition gate: planned control point authorising handover (criteria and authority TBD)
- Data/decision handover: planned methodology for packaging and transferring MVP outputs (contents TBD)
- No auto-promotion: the rule that no prototype component or value enters the production baseline except via the transition gate with requirements, verification, and safety review (per MVP-005)

## 5. System Context

Transition is the sole controlled bridge between the separate MVP volume and the production baseline:

```text
MVP VOLUME (Vol 33: 33.13–33.19 evidence + exit) ── transition gate (33.20) ──► PRODUCTION BASELINE (Vol 00–32)
        (separate rigs/airframes; lessons/data only; no auto-promotion per MVP-005)
```

> This volume is SEPARATE from the production-aircraft documentation. Production-design transition is governed by 33.20.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-MPT-001 | The transition plan shall define the transition-gate methodology, including entry criteria and authority (gate TBD). | MVP-005; MRQ/MAR tier; VVP thread | Inspection |
|REQ-HFPX-MPT-002|The transition plan shall define the data/decision handover methodology from MVP sources to production recipients (handover TBD).|MVP-002; MRQ/MAR tier; VVP thread|Inspection|
|REQ-HFPX-MPT-003|The transition plan shall define re-verification methodology for production use of any handed-over MVP output (methodology TBD).|MVP-005; MRQ/MAR tier; VVP thread|Inspection|
| REQ-HFPX-MPT-004 | The transition plan shall specify that no prototype component or value enters the production baseline except via the transition gate, per MVP-005 (rule TBD in implementation detail). | MVP-005; MRQ/MAR tier; VVP thread | Inspection |
|REQ-HFPX-MPT-005|The transition plan shall define the approval methodology for transition decisions (approval TBD).|MVP-005; MRQ/MAR tier; VVP thread|Inspection|

Gated progression applies to all requirements above: no stage skipped; human-proximate stages require prior unmanned evidence plus authorisation TBD.

## 7. Architecture

Transition architecture (planning view, TBD): gate structure, handover-package structure, recipient-mapping methodology, re-verification-needs chain into production V&V (Vol 22). No production design solution or prototype implementation detail is defined in this document.

## 8. Detailed Design

Not applicable — MVP evidence detail is owned by 33.13–33.18 (TBD); exit outcomes are 33.19 (TBD); production design detail is owned by the production baseline volumes. This document defines only the planning artefacts and methodology to be produced.

## 9. Interfaces

Planning interfaces: MVP requirements and architecture (33.2, 33.3), evidence/iteration/exit planning (33.13–33.19), production baseline recipients (Vol 00–32, TBD), production V&V (Vol 22), safety (Vol 13), modelling (Vol 19), test programme (Vol 23), as applicable.

## 10. Operational Concept

Gated progression governs transition: handover is entered only through satisfied MVP exit methodology (33.19, TBD) and exited only through the defined transition-gate approval methodology (TBD in the transition plan). No stage is skipped. Prototype outputs remain inside Vol 33 until the gate is satisfied. Execution-level conduct instructions are excluded.

## 11. Safety

Transition planning requires that handed-over outputs carry defined safety-review inputs (Vol 13, prototype safety planning 33.11) and defined re-verification needs before production use. Hazardous-subsystem boundary applies: this document covers requirements, planning methodology, interfaces, and safety-analysis inputs only — no build, operation, test-execution, or flight-execution instructions.

## 12. Performance

No performance targets are set in this document. Transition-acceptance thresholds are TBD. No quantitative performance, carry-over, or reuse figure is stated.

## 13. Verification & Validation

This planning document is verified by inspection/review of the transition-plan artefacts (gate methodology, handover methodology, re-verification methodology, non-promotion implementation, approval methodology). Production acceptance of handed-over outputs is verified separately under production V&V (Vol 22); MVP evidence does not equal production verification.

## 14. Risks

- Undefined transition gate → uncontrolled handover; mitigation: gate-methodology requirement (REQ-HFPX-MPT-001)
- Undefined handover → lost context or misapplied data/decisions; mitigation: handover-methodology requirement (REQ-HFPX-MPT-002)
- Missing re-verification → prototype evidence mistaken for production proof; mitigation: re-verification methodology (REQ-HFPX-MPT-003)
- Auto-promotion → baseline contamination; mitigation: explicit no-auto-promotion rule per MVP-005 (REQ-HFPX-MPT-004)
- Undefined approval → unauthorised transfer; mitigation: approval-methodology requirement (REQ-HFPX-MPT-005)

## 15. Open Issues

Transition gate TBD; data/decision handover TBD; re-verification methodology for production TBD; no-auto-promotion implementation detail TBD (per MVP-005); approval methodology TBD. Linked TBDs: exit outcomes (33.19), evidence packaging (33.16), production recipient readiness (Vol 00–32, TBD).

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on MVP objectives and requirements (33.1, 33.2), evidence/iteration/exit planning (33.13–33.19), production baseline recipient definitions (Vol 00–32, TBD), and applicable Vol 13, Vol 19, Vol 22, and Vol 23 inputs.

## 18. Traceability

Parent: MVP-001..MVP-005 (HFPX-MVP-OBJ-001, principally MVP-005); MRQ/MAR tier; VVP thread. Children: transition-plan artefacts, controlled handover packages to production recipients. RTM: REQ-HFPX-MPT-001..005 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined; Vol 33 items never auto-promote to production baselines (MVP-005, this 33.20 gate applies).

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 33.20) |
