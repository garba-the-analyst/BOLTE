# MVP Exit Criteria

**Document ID:** HFPX-MVP-EXC-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined; Vol 33 separate from production  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the planning framework for MVP exit criteria, evidence packaging, approval methodology, and the treatment of open critical items. Owns Chapter 33.19.

This document is planning/methodology only. It does not contain test-execution or flight-execution instructions.

## 2. Scope

Covers planning for exit determination against each MVP objective, including retirement/bounding of ISS-006 (control authority), ISS-007 (mass/thrust/energy), and ISS-008 (recovery). Excludes execution-level activity conduct and production certification or qualification decisions (governed separately; production transition is 33.20).

Gated progression is mandatory (DDR-001): no stage shall be skipped; human-proximate stages require prior unmanned evidence plus authorisation TBD; exit is not declared with unresolved critical items (methodology TBD).

## 3. Applicable Documents

- DDR-001 (unmanned-first); HFPX-MVP-OBJ-001 (Chapter 33.1, MVP-001..MVP-005)
- Future: 33.2 MVP requirements, 33.13/33.14/33.15 evidence sources, 33.16 experimental data, 33.17 lessons, 33.18 design iteration, 33.20 transition
- Vol 23 test programme; Vol 13 safety; Vol 19 modelling; Vol 22 V&V (production, separate)

## 4. Definitions & Acronyms

- MVP: Minimum Viable Prototype — smallest system that retires the load-bearing risks (ISS-006/007/008)
- Exit criteria: planned determination methodology for MVP completion per objective (details TBD, including ISS-006/007/008 retirement methodology TBD)
- Evidence package: planned compilation of gate evidence supporting an exit decision (contents TBD)
- Approval: planned authorisation methodology for exit declaration (authority TBD)
- Open critical items: planned category of unresolved findings blocking exit (definition TBD)

## 5. System Context

Exit criteria adjudicate the gated MVP path and bound the handover to production transition:

```text
33.13 + 33.14 + 33.15 + 33.16 + 33.17 + 33.18 ── gated evidence ──► MVP EXIT CRITERIA (33.19) ── decision ──► 33.20 TRANSITION GATE
```

> This volume is SEPARATE from the production-aircraft documentation. Production-design transition is governed by 33.20.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-MEX-001 | The exit plan shall define exit criteria per MVP objective, including retirement/bounding methodology for ISS-006, ISS-007, and ISS-008 (criteria TBD). | MVP-003; MRQ/MAR tier; VVP thread | Inspection |
|REQ-HFPX-MEX-002|The exit plan shall define the evidence-package methodology supporting exit determination (package TBD).|MVP-002; MRQ/MAR tier; VVP thread|Inspection|
|REQ-HFPX-MEX-003|The exit plan shall define the approval methodology for exit declaration (approval TBD).|MVP-003; MRQ/MAR tier; VVP thread|Inspection|
| REQ-HFPX-MEX-004 | The exit plan shall specify that exit is not declared with open critical items (definition and methodology TBD). | MVP-003; MRQ/MAR tier; VVP thread | Inspection |
|REQ-HFPX-MEX-005|The exit plan shall define the linkage methodology from exit outcomes to the 33.20 transition gate (linkage TBD).|MVP-005; MRQ/MAR tier; VVP thread|Inspection|

Gated progression applies to all requirements above: no stage skipped; human-proximate stages require prior unmanned evidence plus authorisation TBD.

## 7. Architecture

Exit-criteria architecture (planning view, TBD): objective-to-criterion mapping, evidence-package structure, approval-chain methodology, open-item tracking linkage. No exit determination is made in this document; thresholds remain TBD.

## 8. Detailed Design

Not applicable — criterion values and package contents are TBD in the exit plan. Evidence-source detail is owned by 33.13–33.16 (TBD); lessons and iteration inputs are 33.17–33.18 (TBD).

## 9. Interfaces

Planning interfaces: MVP objectives and requirements (33.1, 33.2), evidence-source planning (33.13/33.14/33.15/33.16), lessons and iteration planning (33.17/33.18), transition planning (33.20), Vol 13, Vol 19, and Vol 23 inputs as applicable, production baseline via 33.20 data/decision handover only.

## 10. Operational Concept

Gated progression is the operational concept for exit: objectives are closed only through defined criteria and compiled evidence packages reviewed under defined approval methodology (all TBD in the exit plan). No stage is skipped. Human-proximate stages require prior unmanned evidence plus authorisation TBD. Execution-level conduct instructions are excluded.

## 11. Safety

Exit planning requires that safety-relevant evidence, including recovery-system (ISS-008) limits and Vol 13 inputs, is addressed in the evidence package before exit declaration methodology completes. Hazardous-subsystem boundary applies: this document covers requirements, planning methodology, interfaces, and safety-analysis inputs only — no build, operation, test-execution, or flight-execution instructions.

## 12. Performance

No performance targets are set in this document. Exit thresholds per objective, including ISS-006/007/008 retirement thresholds, are TBD. No speed, range, endurance, load, or environmental figure is stated.

## 13. Verification & Validation

This planning document is verified by inspection/review of the exit-plan artefacts (per-objective criteria, evidence-package methodology, approval methodology, open-critical-item rule, transition linkage). Exit declarations are assessed separately under the defined methodology; MVP exit does not equal production verification (Vol 22, separate).

## 14. Risks

- Undefined per-objective criteria → ambiguous completion; mitigation: criterion-definition requirement including ISS-006/007/008 (REQ-HFPX-MEX-001)
- Undefined evidence package → unreviewable exit claims; mitigation: package-methodology requirement (REQ-HFPX-MEX-002)
- Undefined approval → unauthorised exit declaration; mitigation: approval-methodology requirement (REQ-HFPX-MEX-003)
- Exit with open critical items → carried risk; mitigation: explicit no-exit-with-open-critical rule (REQ-HFPX-MEX-004)
- Weak transition linkage → orphaned exit outcomes; mitigation: defined linkage to 33.20 (REQ-HFPX-MEX-005)

## 15. Open Issues

Exit criteria TBD per objective including ISS-006/007/008 retirement methodology TBD; evidence package TBD; approval methodology TBD; open-critical-item definition and methodology TBD; transition linkage TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on MVP objectives and requirements (33.1, 33.2), evidence-source planning (33.13–33.16), lessons and iteration planning (33.17, 33.18), transition planning (33.20), and applicable Vol 13, Vol 19, Vol 22, and Vol 23 inputs.

## 18. Traceability

Parent: MVP-001..MVP-005 (HFPX-MVP-OBJ-001); MRQ/MAR tier; VVP thread. Children: exit-plan artefacts, exit decisions feeding the 33.20 transition gate. RTM: REQ-HFPX-MEX-001..005 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined; Vol 33 items never auto-promote to production baselines (MVP-005, 33.20 gate applies).

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 33.19) |
