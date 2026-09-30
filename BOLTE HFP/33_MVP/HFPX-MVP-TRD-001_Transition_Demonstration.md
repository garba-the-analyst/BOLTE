# Transition Demonstration

**Document ID:** HFPX-MVP-TRD-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined; Vol 33 separate from production  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the planning framework for the MVP transition demonstration, including how demonstration objectives, corridor methodology, and success criteria are specified and controlled. Owns Chapter 33.15.

This document is planning/methodology only. It does not contain test-execution or flight-execution instructions.

## 2. Scope

Covers planning for the unmanned transition demonstration as a gated evidence event within the unmanned-first progression (DDR-001). Excludes flight-execution procedures, ground-test execution (33.13), unmanned programme execution (33.14), and production design decisions (governed by 33.20 transition).

Gated progression is mandatory: no stage shall be skipped; no human exposure shall precede the demonstration outcome unless gated criteria and authorisation TBD are satisfied.

## 3. Applicable Documents

- DDR-001 (unmanned-first); HFPX-MVP-OBJ-001 (Chapter 33.1, MVP-001..MVP-005)
- Future: 33.2 MVP requirements, 33.3 MVP architecture, 33.13 ground-test programme, 33.14 unmanned-test programme, 33.16 experimental data, 33.19 exit criteria, 33.20 transition
- Vol 06 flight characteristics, including Vol 06.13 corridor inputs (TBD); Vol 13 safety; Vol 23 test programme; Vol 19 modelling

## 4. Definitions & Acronyms

- MVP: Minimum Viable Prototype — smallest system that retires the load-bearing risks (ISS-006/007/008)
- Transition demonstration: planned gated evidence event addressing hover-to-horizontal-flight transition behaviour (execution excluded)
- Corridor: planned envelope region and boundary methodology for the demonstration (details TBD, Vol 06.13 inputs TBD)
- Success criteria: planned determination methodology for demonstration outcomes (details TBD)

## 5. System Context

Transition demonstration is a gated evidence event fed by ground and unmanned evidence and feeding exit and transition decisions:

```text
GROUND (33.13) + UNMANNED BUILD-UP (33.14) ── gates ──► TRANSITION DEMONSTRATION (33.15) ── evidence ──► EXIT (33.19) / DATA (33.16)
                                                                               │
                                                                               └──── lessons/data only ──► PRODUCTION BASELINE via 33.20 gate ──► (no auto-promotion per MVP-005)
```

> This volume is SEPARATE from the production-aircraft documentation. Production-design transition is governed by 33.20.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-MTD-001 | The transition demonstration plan shall define demonstration objectives linked to MVP objectives (objectives TBD). | MVP-001; MRQ/MAR tier; VVP thread | Inspection |
|REQ-HFPX-MTD-002|The transition demonstration plan shall define the corridor methodology, with inputs from Vol 06.13 (corridor TBD).|MVP-001; MRQ/MAR tier; VVP thread|Inspection|
|REQ-HFPX-MTD-003|The transition demonstration plan shall define success criteria and associated evidence requirements (criteria TBD).|MVP-003; MRQ/MAR tier; VVP thread|Inspection|
| REQ-HFPX-MTD-004 | The transition demonstration plan shall specify that no human exposure occurs before the demonstration outcome and associated gates are satisfied (gating TBD). | MVP-001; MRQ/MAR tier; VVP thread | Inspection |

Gated progression applies to all requirements above: no stage skipped; human-proximate stages require prior unmanned evidence plus authorisation TBD.

## 7. Architecture

Transition-demonstration architecture (planning view, TBD): demonstration plan structure, objective-to-evidence mapping, corridor-framework linkage, evidence-capture chain to instrumentation (33.12) and experimental data (33.16). No flight-article configuration or execution routing is defined in this document.

## 8. Detailed Design

Not applicable — prototype configuration is 33.4 (TBD); corridor characterisation inputs are Vol 06.13 (TBD). This document defines only the planning artefacts and methodology to be produced.

## 9. Interfaces

Planning interfaces: MVP requirements (33.2), MVP architecture (33.3), unmanned-test planning (33.14), instrumentation planning (33.12), experimental data planning (33.16), Vol 06.13 corridor inputs (TBD), Vol 23 test-programme interfaces, production baseline via 33.20 data/decision handover only.

## 10. Operational Concept

Gated progression is the operational concept: the demonstration is entered only through satisfied ground and unmanned gates, and exited only through the defined success-criteria methodology (all TBD in the demonstration plan). No stage is skipped. Human-proximate activity requires prior unmanned demonstration evidence plus authorisation TBD. Execution-level conduct and control inputs are excluded.

## 11. Safety

Transition-demonstration planning is governed by prototype safety system planning (33.11) plus Vol 13 analyses plus range/test safety controls (Vol 23). Recovery-system limits (ISS-008) constrain the planned corridor from the outset. Hazardous-subsystem boundary applies: this document covers requirements, planning methodology, interfaces, and safety-analysis inputs only — no build, operation, test-execution, or flight-execution instructions.

## 12. Performance

No performance targets are set in this document. Corridor bounds and success thresholds are TBD and linked to MVP exit criteria (33.19, TBD). No speed, altitude, load, or environmental figure is stated.

## 13. Verification & Validation

This planning document is verified by inspection/review of the demonstration-plan artefacts (objectives, corridor methodology, success criteria, human-exposure gating). Demonstration outcomes are assessed separately under the defined methodology; MVP success does not equal production verification (Vol 22, separate).

## 14. Risks

- Undefined objectives → unfocused demonstration and weak evidence; mitigation: objective-definition requirement (REQ-HFPX-MTD-001)
- Undefined corridor → inconsistent boundary interpretation; mitigation: corridor methodology with Vol 06.13 inputs (REQ-HFPX-MTD-002)
- Undefined success criteria → disputed demonstration outcome; mitigation: defined criteria and evidence requirements (REQ-HFPX-MTD-003)
- Premature human exposure → unacceptable risk; mitigation: explicit no-exposure-before-demo gating (REQ-HFPX-MTD-004)

## 15. Open Issues

Objectives TBD; corridor TBD (Vol 06.13 inputs TBD); success criteria TBD; no-human-exposure-before-demo gating TBD. Linked TBDs: unmanned build-up evidence (33.14), instrumentation coverage (33.12), exit criteria (33.19), ISS-006/007/008 retirement linkage.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on MVP requirements (33.2), MVP architecture (33.3), ground and unmanned evidence planning (33.13, 33.14), instrumentation planning (33.12), Vol 06.13 corridor inputs, Vol 13 safety inputs, Vol 23 test-programme capability, modelling needs (Vol 19), and regulatory authorisation inputs (Vol 25, as applicable).

## 18. Traceability

Parent: MVP-001..MVP-005 (HFPX-MVP-OBJ-001); MRQ/MAR tier; VVP thread. Children: transition-demonstration plan artefacts, evidence inputs to 33.16 data capture, lessons inputs to 33.17, exit-evidence inputs to 33.19. RTM: REQ-HFPX-MTD-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined; Vol 33 items never auto-promote to production baselines (MVP-005, 33.20 gate applies).

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 33.15) |
