# Design Iteration

**Document ID:** HFPX-MVP-DIT-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined; Vol 33 separate from production  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the planning framework for MVP design iteration, including how iteration triggers, change control, re-verification, and records are specified and controlled. Owns Chapter 33.18.

This document is planning/methodology only. It does not contain test-execution or flight-execution instructions.

## 2. Scope

Covers planning for prototype-only iteration driven by ground-test (33.13), unmanned-test (33.14), transition-demonstration (33.15), experimental-data (33.16), and lessons-learned (33.17) outputs. Excludes production design changes (governed by 33.20 transition) and execution-level modification instructions.

Gated progression is mandatory (DDR-001): no stage shall be skipped; human-proximate stages require prior unmanned evidence plus authorisation TBD; iteration does not bypass gates.

## 3. Applicable Documents

- DDR-001 (unmanned-first); HFPX-MVP-OBJ-001 (Chapter 33.1, MVP-001..MVP-005, including MVP-005 non-promotion rule)
- Future: 33.2 MVP requirements, 33.3 MVP architecture, 33.4 prototype configuration, 33.13/33.14/33.15 evidence sources, 33.16 data, 33.17 lessons, 33.19 exit criteria, 33.20 transition
- Vol 23 test programme; Vol 13 safety; Vol 19 modelling; Vol 22 V&V (production, separate)

## 4. Definitions & Acronyms

- MVP: Minimum Viable Prototype — smallest system that retires the load-bearing risks (ISS-006/007/008)
- Design iteration: planned prototype-only change cycle from trigger through change control to re-verification and records update
- Iteration triggers: planned entry conditions initiating an iteration cycle (details TBD)
- Change control: planned methodology for approving, recording, and bounding prototype changes (details TBD)
- Re-verification: planned methodology for re-establishing affected evidence after a change (details TBD)

## 5. System Context

Design iteration operates inside Vol 33 only and reaches production solely through the controlled transition gate:

```text
EVIDENCE + LESSONS (33.13–33.17) ── triggers ──► DESIGN ITERATION (33.18, prototype only) ── re-verified evidence ──► 33.19 EXIT
                                                                          │
                                                                          └──── lessons/data only ──► PRODUCTION BASELINE via 33.20 gate ──► (no auto-promotion per MVP-005)
```

> This volume is SEPARATE from the production-aircraft documentation. Production-design transition is governed by 33.20.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-MDI-001 | The design-iteration plan shall define iteration triggers linked to scoped evidence and lessons sources (triggers TBD). | MVP-003; MRQ/MAR tier; VVP thread | Inspection |
|REQ-HFPX-MDI-002|The design-iteration plan shall define change-control methodology for prototype-only changes (methodology TBD).|MVP-005; MRQ/MAR tier; VVP thread|Inspection|
|REQ-HFPX-MDI-003|The design-iteration plan shall define re-verification methodology for affected evidence after each iteration (methodology TBD).|MVP-003; MRQ/MAR tier; VVP thread|Inspection|
| REQ-HFPX-MDI-004 | The design-iteration plan shall define records-control methodology for iteration decisions, changes, and re-verification outcomes (records TBD). | MVP-002; MRQ/MAR tier; VVP thread | Inspection |

Gated progression applies to all requirements above: no stage skipped; human-proximate stages require prior unmanned evidence plus authorisation TBD.

## 7. Architecture

Design-iteration architecture (planning view, TBD): trigger-to-change-to-reverify-to-record cycle, configuration-delta methodology, linkage to prototype configuration (33.4) and evidence sources (33.13–33.16). No modification design or implementation detail is defined in this document.

## 8. Detailed Design

Not applicable — prototype configuration detail is 33.4 (TBD); subsystem prototype detail is 33.6–33.9 (TBD). This document defines only the planning artefacts and methodology to be produced.

## 9. Interfaces

Planning interfaces: MVP requirements (33.2), MVP architecture (33.3), prototype configuration planning (33.4), evidence-source planning (33.13/33.14/33.15/33.16), lessons-learned planning (33.17), exit-criteria planning (33.19), Vol 13 and Vol 19 inputs as applicable, production baseline via 33.20 data/decision handover only.

## 10. Operational Concept

Gated progression governs iteration: triggers are evaluated at defined control points (TBD in the iteration plan); approved changes re-enter the gated sequence at the methodology-defined point and do not skip gates. Human-proximate stages require prior unmanned evidence plus authorisation TBD. Execution-level modification, build, and test-conduct instructions are excluded.

## 11. Safety

Design-iteration planning is governed by prototype safety planning (33.11) plus Vol 13 analyses; safety impact assessment methodology is planned before any prototype change is accepted. Hazardous-subsystem boundary applies: this document covers requirements, planning methodology, interfaces, and safety-analysis inputs only — no build, modification-execution, test-execution, or flight-execution instructions.

## 12. Performance

No performance targets are set in this document. Iteration-acceptance and re-verification thresholds are TBD and linked to MVP exit criteria (33.19, TBD). No quantitative performance figure is stated.

## 13. Verification & Validation

This planning document is verified by inspection/review of the iteration-plan artefacts (trigger definitions, change-control methodology, re-verification methodology, records-control methodology). Iteration outcomes are assessed separately through gate evidence; MVP iteration does not equal production verification (Vol 22, separate).

## 14. Risks

- Undefined triggers → ad-hoc or missed iteration; mitigation: trigger-definition requirement (REQ-HFPX-MDI-001)
- Weak change control → uncontrolled prototype divergence; mitigation: defined change-control methodology (REQ-HFPX-MDI-002)
- Skipped re-verification → invalidated evidence; mitigation: defined re-verification methodology (REQ-HFPX-MDI-003)
- Poor records → untraceable iteration history; mitigation: records-control methodology (REQ-HFPX-MDI-004)
- Prototype-to-production leakage → baseline contamination; mitigation: MVP-005 plus 33.20 gate (no auto-promotion)

## 15. Open Issues

Iteration triggers TBD; change-control methodology TBD; re-verification methodology TBD; records-control methodology TBD. Linked TBDs: evidence-source readiness (33.13–33.16), lessons linkage (33.17), exit-evidence linkage (33.19), transition boundary (33.20).

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on MVP requirements (33.2), MVP architecture (33.3), prototype configuration planning (33.4), evidence-source and lessons planning (33.13–33.17), exit-criteria planning (33.19), and applicable Vol 13, Vol 19, and Vol 23 inputs.

## 18. Traceability

Parent: MVP-001..MVP-005 (HFPX-MVP-OBJ-001); MRQ/MAR tier; VVP thread. Children: iteration-plan artefacts, re-verified evidence inputs to 33.19 exit, handover inputs to 33.20. RTM: REQ-HFPX-MDI-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined; Vol 33 items never auto-promote to production baselines (MVP-005, 33.20 gate applies).

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 33.18) |
