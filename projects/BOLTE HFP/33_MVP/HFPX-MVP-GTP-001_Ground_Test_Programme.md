# Ground-Test Programme

**Document ID:** HFPX-MVP-GTP-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined; Vol 33 separate from production  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the planning framework for the MVP ground-test programme, including how scope, entrance/exit criteria, and pass/fail methodology are specified and controlled. Owns Chapter 33.13.

This document is planning/methodology only. It does not contain test-execution or flight-execution instructions.

## 2. Scope

Covers planning for ground-based verification activities supporting the unmanned-first demonstrator progression (DDR-001): simulation → SIL → HIL → subsystem → integrated propulsion, prior to unmanned hover. Excludes test-execution procedures, flight-execution activities (33.14), transition demonstration execution (33.15), and production design decisions (governed by 33.20 transition).

Gated progression is mandatory: no stage shall be skipped; human-proximate stages require prior unmanned evidence plus authorisation TBD.

## 3. Applicable Documents

- DDR-001 (unmanned-first); HFPX-MVP-OBJ-001 (Chapter 33.1, MVP-001..MVP-005)
- Future: 33.2 MVP requirements, 33.3 MVP architecture, 33.14 unmanned-test programme, 33.19 exit criteria, 33.20 transition
- Vol 23 test programme, including Vol 23.2 hooks (TBD); Vol 13 safety; Vol 19 modelling; Vol 22 V&V (production, separate)

## 4. Definitions & Acronyms

- MVP: Minimum Viable Prototype — smallest system that retires the load-bearing risks (ISS-006/007/008)
- Ground-test programme: planned set of ground-based verification activities and associated entrance/exit and pass/fail methodology
- Gates: mandatory evidence thresholds; skipping gates is prohibited
- Vol 23.2 hooks: defined interfaces to the referenced test-programme volume (details TBD)

## 5. System Context

MVP ground testing sits within the gated Vol 33 demonstrator path and feeds unmanned flight readiness without entering the production baseline:

```text
GROUND-TEST PROGRAMME (33.13) ── evidence ──► UNMANNED-TEST PROGRAMME (33.14)
         │                                            │
         └──── lessons/data only ──► PRODUCTION BASELINE via 33.20 gate ──► (no auto-promotion per MVP-005)
```

> This volume is SEPARATE from the production-aircraft documentation. Production-design transition is governed by 33.20.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-MGT-001 | The ground-test programme plan shall define the scope of ground-based verification activities supporting MVP objectives (scope TBD). | MVP-001; MRQ/MAR tier; VVP thread | Inspection |
| REQ-HFPX-MGT-002 | Each ground-test stage shall define entrance criteria and exit criteria, and no stage shall be skipped (criteria TBD). | MVP-001; MRQ/MAR tier; VVP thread | Inspection |
|REQ-HFPX-MGT-003|The ground-test programme shall define pass/fail determination methodology for each scoped activity (methodology TBD).|MVP-003; MRQ/MAR tier; VVP thread|Inspection|
|REQ-HFPX-MGT-004|The ground-test programme shall define interface hooks to Vol 23.2 for applicable ground-test capabilities and evidence exchange (hooks TBD).|MVP-004; MRQ/MAR tier; VVP thread|Inspection|

Gated progression applies to all requirements above: human-proximate stages require prior unmanned evidence plus authorisation TBD.

## 7. Architecture

Ground-test programme architecture (planning view, TBD): programme plan structure, stage taxonomy, criteria framework, evidence-capture chain to instrumentation (33.12) and experimental data (33.16). Representativeness criteria TBD. No execution rig configuration is defined in this document.

## 8. Detailed Design

Not applicable — detailed test-article configuration is 33.4 (TBD); experimental components are 33.5 (TBD). This document defines only the planning artefacts and methodology to be produced.

## 9. Interfaces

Planning interfaces: MVP requirements (33.2), MVP architecture (33.3), test instrumentation planning (33.12), experimental data planning (33.16), unmanned-test programme planning (33.14), Vol 23.2 test-programme interfaces (hooks TBD), production baseline via 33.20 data/decision handover only.

## 10. Operational Concept

Gated progression is the operational concept for ground testing: each planned stage specifies entrance criteria, required evidence, and exit criteria (all TBD in the programme plan). No stage is skipped. Human-proximate stages require prior unmanned evidence plus authorisation TBD. Abort-rule methodology is planned at programme level; execution-level abort instructions are excluded.

## 11. Safety

MVP ground-test planning is governed by prototype safety system planning (33.11) plus Vol 13 analyses plus range/test safety controls (Vol 23). Hazardous-subsystem boundary applies: this document covers requirements, planning methodology, interfaces, and safety-analysis inputs only — no build, ignition, operation, test-execution, or flight-execution instructions.

## 12. Performance

No performance targets are set in this document. Ground-test success thresholds are defined through the pass/fail methodology (TBD) and linked to MVP exit criteria (33.19, TBD). No speed, load, endurance, or environmental figure is stated.

## 13. Verification & Validation

This planning document is verified by inspection/review of the programme-plan artefacts (scope definition, entrance/exit framework, pass/fail methodology, Vol 23.2 hook definitions). Ground-test execution results are verified separately under the defined methodology; MVP success does not equal production verification (Vol 22, separate).

## 14. Risks

- Undefined scope → incomplete evidence for gates; mitigation: scope-definition requirement (REQ-HFPX-MGT-001)
- Weak entrance/exit criteria → premature stage progression; mitigation: mandatory gate framework with no skipping (REQ-HFPX-MGT-002)
- Ambiguous pass/fail methodology → disputed outcomes; mitigation: defined determination methodology (REQ-HFPX-MGT-003)
- Unmanaged Vol 23.2 dependencies → capability or evidence gaps; mitigation: explicit hook definitions (REQ-HFPX-MGT-004)

## 15. Open Issues

Scope TBD; entrance/exit criteria TBD; pass/fail methodology TBD; Vol 23.2 hooks TBD. Linked TBDs: representativeness criteria, instrumentation list (33.12), exit criteria (33.19), ISS-006/007/008 retirement linkage.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on MVP requirements (33.2), MVP architecture (33.3), prototype configuration (33.4), test instrumentation planning (33.12), Vol 23 test-programme capability (including Vol 23.2), Vol 13 safety inputs, modelling needs (Vol 19), and regulatory authorisation inputs (Vol 25, as applicable).

## 18. Traceability

Parent: MVP-001..MVP-005 (HFPX-MVP-OBJ-001); MRQ/MAR tier; VVP thread. Children: ground-test programme plan artefacts, evidence inputs to 33.14 readiness, data inputs to 33.16, lessons inputs to 33.17, exit-evidence inputs to 33.19. RTM: REQ-HFPX-MGT-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined; Vol 33 items never auto-promote to production baselines (MVP-005, 33.20 gate applies).

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 33.13) |
