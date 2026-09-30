# Test Instrumentation

**Document ID:** HFPX-MVP-TIN-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined; Vol 33 separate from production  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the test-instrumentation dataset, its accuracy methodology, its installation hooks, and its data ownership so that every gated test produces validatable evidence. Owns Chapter 33.12.

## 2. Scope

Covers measurand-inventory definition; accuracy and calibration methodology; installation hooks with Vol 23 provisions; and data ownership, retention, and handover methodology. Test methodology and gating only — no build/ignition/operation instructions for high-energy propulsion outside controlled conditions.

Vol 33 is SEPARATE from production baselines. No instrumentation choice here constrains production design; reuse is governed by the 33.20 transition gate only.

## 3. Applicable Documents

- HFPX-MVP-OBJ-001 MVP Objectives (MVP-001..005, DDR-001 risk note)
- HFPX-MVP-REQ-001 MVP System Requirements (Chapter 33.2; REQ-HFPX-MRQ-004 data capture)
- HFPX-MVP-ARC-001 MVP Architecture (Chapter 33.3; MAR-005 instrumentation provisions)
- HFPX-MVP-CFG-001 Prototype Configuration (Chapter 33.4; instrumentation fit under index control)
- Future: 33.5 experimental components, 33.7–33.11 data producers/safety chain, 33.13/33.14 test programmes, 33.16 experimental data, 33.19 exit criteria, 33.20 transition; Vol 09 sensing; Vol 19 modelling; Vol 23 test programme (including 23.16 hooks)

## 4. Definitions & Acronyms

- MTI: MVP Test-Instrumentation Requirement — instrumentation obligation in this document (does not set production instrumentation requirements)
- Measurand inventory: the controlled list of quantities captured as gate evidence with sampling and recording provisions (inventory TBD)
- Accuracy methodology: the defined method establishing trust in each measurand for model validation (method and values TBD)
- Instrumentation hooks: structural, power, data-bus, mounting, and software provisions reserved for test sensors and recording (hooks TBD per Vol 23.16)
- Data ownership: the defined custodian, retention, access, and handover rules for recorded evidence (rules TBD)
- 33.20 transition gate: sole route for instrumentation lessons and data to inform production; no auto-promotion

## 5. System Context

Test instrumentation is the evidence backbone of the demonstrator programme:

```text
MRQ-004 + MAR-005 ── allocation ──► MTI-001..004 (this document, Ch 33.12)
        │                                        │
        ▼                                        ▼
  data producers (33.6–33.11) ── hooks ──► records ──► 33.16 data / 33.19 exit / 33.20 gate
```

> This volume is SEPARATE from the production-aircraft documentation. Production-design transition is governed by 33.20.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-MTI-001 | The MVP test instrumentation shall provide a measurand inventory covering flight, propulsion, structural, thermal, and control data relied upon for model validation with sampling and recording provisions (inventory TBD). | MVP-002, MRQ-004, MAR-005 | Inspection |
| REQ-HFPX-MTI-002 | The MVP test instrumentation measurands relied upon for gate evidence shall meet a defined accuracy and calibration methodology with documented limits (method and values TBD). | MVP-002, MRQ-004, MAR-005 | Inspection |
| REQ-HFPX-MTI-003 | The MVP test articles shall provide instrumentation hooks with structural, power, data-bus, mounting, and software provisions defined with Vol 23 test provisions (hooks TBD per Vol 23.16). | MRQ-004, MAR-005, DDR-001 | Inspection |
| REQ-HFPX-MTI-004 | The MVP recorded evidence shall have defined data ownership, retention, access, and handover rules covering each gated test through exit and transition dispositions (rules TBD). | MVP-002, MRQ-004 | Inspection |

All measurand lists, sampling values, accuracy values, calibration values, hook quantities, and retention periods are TBD.

## 7. Architecture

Instrumentation architecture (placeholder): measurand inventory allocated to taps on 33.6–33.11 segments via Vol 23.16 hooks, feeding recording and the 33.16 dataset for Vol 19 model validation. Data-flow diagrams, bus allocations, recorder provisions, and hook layouts TBD; all prototype-only.

## 8. Detailed Design

Not applicable — no sensor selection parameter, hook drawing, bus parameter, recorder setting, or database schema is baselined here. All design values TBD in later tranches, if at all, and remain prototype-only.

## 9. Interfaces

Instrumentation interfaces: data-producer taps (33.6 propulsion, 33.7/33.8/33.9 avionics/compute/sensors, 33.10 ground-station records, 33.11 safety records), calibration provisions (Vol 09.17 where applicable), range/test infrastructure and hooks (Vol 23.16), model-validation consumers (Vol 19; 33.16), configuration index for instrumentation fit and calibration record (33.4). Production instrumentation interface is lessons/data handover via the 33.20 transition gate only.

## 10. Operational Concept

Test methodology and gating only. Gated tests proceed only with the required measurand inventory, hook fit, calibration, and recording active at the defined standard (TBD); instrumentation changes or calibration lapses invoke the 33.4 change rule and may require re-gating. No build/ignition/operation instructions outside controlled conditions.

## 11. Safety

Instrumentation supports safety gating (evidence that envelopes and safety-function responses hold) but grants no clearance. Instrumentation failure behaviour and data-validity limits are per 33.11/Vol 13 methodology (criteria TBD). Hazardous-subsystem boundary: dataset definition, accuracy methodology, hooks, records, and gating only.

## 12. Performance

No instrumentation performance targets are set. Sampling, accuracy, latency, capacity, and retention values are TBD. Success is dataset completeness and trust per gate (thresholds TBD in 33.19), not numeric performance.

## 13. Verification & Validation

- MTI-001: Inspection (measurand inventory exists with sampling/recording provisions covering all relied-upon domains — TBD)
- MTI-002: Inspection (accuracy/calibration methodology applied with documented limits — TBD)
- MTI-003: Inspection (hook provisions exist per Vol 23.16 list — TBD)
- MTI-004: Inspection (ownership, retention, access, and handover rules recorded and followed per gated test — TBD)
- MVP instrumentation verification does not constitute production instrumentation verification (separate baseline).

## 14. Risks

- Incomplete measurand inventory → models unvalidatable after flights; mitigation: MTI-001 inventory TBD before first gated flight
- Untrusted accuracy → false validation claims; mitigation: MTI-002 accuracy methodology TBD before gated flights
- Missing hooks → late retrofit disturbing configuration control; mitigation: MTI-003 hooks TBD with Vol 23.16 before gated flights
- Unclear ownership/retention → evidence lost before exit/transition; mitigation: MTI-004 rules TBD with gate inspection

## 15. Open Issues

- Measurand inventory, sampling, and recording provisions for MTI-001: TBD
- Accuracy methodology, calibration standards, limits, and records for MTI-002: TBD
- Hook list, provisions, and Vol 23.16 interface definitions for MTI-003: TBD
- Data ownership, retention, access, and handover rules for MTI-004: TBD

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on 33.3 instrumentation allocation, 33.4 fit/calibration record control, 33.5 component instances, 33.6–33.11 tap definitions, Vol 09.17 calibration provisions, Vol 19 validation needs, Vol 23.16 hook provisions, 33.13/33.14 stage data needs, 33.16 dataset curation, 33.19 exit thresholds, 33.20 handover requirements.

## 18. Traceability

Parents: MVP-002 (evidence), MVP-005 (no auto-promotion), MRQ-004 (data capture), MAR-005 (instrumentation provisions), DDR-001. Children: 33.13/33.14 dataset records, 33.16 experimental-data curation, 33.19 exit evidence, 33.20 handover dispositions. RTM: REQ-HFPX-MTI-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined; Vol 33 separate from production baselines. Prototype instrumentation definitions never auto-promote; production effect only via the 33.20 transition gate.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 33.12) |
