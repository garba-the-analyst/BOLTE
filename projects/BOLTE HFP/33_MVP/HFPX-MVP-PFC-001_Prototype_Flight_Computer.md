# Prototype Flight Computer

**Document ID:** HFPX-MVP-PFC-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined; Vol 33 separate from production  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the prototype flight computer, its determinism methodology, and its HIL hooks for hosting control-law testing in controlled conditions. Owns Chapter 33.8.

## 2. Scope

Covers prototype compute-platform definition; determinism (timing-behaviour) methodology; HIL hooks to the modelling environment; and the prototype-only status of all flight-computer choices. Test methodology and gating only — no build/ignition/operation instructions for high-energy propulsion outside controlled conditions.

Vol 33 is SEPARATE from production baselines. No flight-computer choice here constrains production design; reuse is governed by the 33.20 transition gate only.

## 3. Applicable Documents

- HFPX-MVP-OBJ-001 MVP Objectives (MVP-001..005, DDR-001 risk note)
- HFPX-MVP-REQ-001 MVP System Requirements (Chapter 33.2; REQ-HFPX-MRQ-001..006)
- HFPX-MVP-ARC-001 MVP Architecture (Chapter 33.3; MAR-003 compute segment)
- HFPX-MVP-CFG-001 Prototype Configuration (Chapter 33.4; software build under index control)
- Future: 33.5 experimental components, 33.7 avionics, 33.9 sensors, 33.11 safety system, 33.12 instrumentation, 33.13/33.14 test programmes, 33.20 transition; Vol 13 safety; Vol 19 modelling (including 19.9 HIL)

## 4. Definitions & Acronyms

- MPC: MVP Prototype-Compute Requirement — prototype flight-computer obligation in this document (does not set production compute requirements)
- Prototype flight computer: test-grade compute platform hosting prototype control laws and test software (platform TBD)
- Determinism methodology: the defined method for characterising timing behaviour relied upon by gated tests (method and values TBD)
- HIL hooks: hardware, software, and interface provisions connecting the prototype computer to hardware-in-the-loop testing (hooks TBD, Vol 19.9)
- 33.20 transition gate: sole route for compute lessons to inform production; no auto-promotion

## 5. System Context

The prototype flight computer hosts control-law evidence within the avionics chain:

```text
MRQ-001/MRQ-004 + MAR-003 ── allocation ──► MPC-001..004 (this document, Ch 33.8)
        │                                              │
        ▼                                              ▼
  avionics (33.7) + sensors (33.9) ◄── hosting ──► HIL environment (Vol 19.9) + gates (33.13/33.14)
```

> This volume is SEPARATE from the production-aircraft documentation. Production-design transition is governed by 33.20.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-MPC-001 | The MVP prototype flight computer shall be defined as a controlled platform with hardware and software-build identity for each gated test (platform and build TBD, under 33.4 control). | MVP-001, MRQ-001, MAR-003 | Inspection |
| REQ-HFPX-MPC-002 | The MVP prototype flight computer timing behaviour relied upon by gated tests shall be characterised by a defined determinism methodology with documented limits (method, metrics, and values TBD). | MRQ-001, MAR-003, DDR-001 | Analysis |
| REQ-HFPX-MPC-003 | The MVP prototype flight computer shall provide HIL hooks to the Vol 19 modelling environment with defined hardware, software, and interface provisions (hooks TBD per Vol 19.9). | MVP-002, MRQ-004, MAR-003 | Inspection |
| REQ-HFPX-MPC-004 | The MVP prototype flight computer and its software shall be explicitly non-representative of production compute and shall inform production only via lessons and data through the 33.20 transition gate (per MVP-005). | MVP-005 | Inspection |

All processor identities, timing values, load figures, and performance values are TBD.

## 7. Architecture

Compute architecture (placeholder): prototype computer hosted in the avionics chain with sensor inputs (33.9), command/telemetry via avionics (33.7), safety-chain separation (33.11), and HIL connections (Vol 19.9). Block diagrams, signal lists, and timing budgets TBD; all prototype-only.

## 8. Detailed Design

Not applicable — no processor selection parameter, schematic, timing budget, or software design is baselined here. All design values TBD in later tranches, if at all, and remain prototype-only.

## 9. Interfaces

Compute interfaces: avionics hosting (33.7), sensor inputs (33.9), ground-station command/telemetry path (33.10), safety-chain separation (33.11), instrumentation taps (33.12), HIL environment (Vol 19.9), configuration index for software-build identity (33.4). Production compute interface is lessons/data handover via the 33.20 transition gate only.

## 10. Operational Concept

Test methodology and gating only. Gated tests run only on the recorded software build with determinism limits characterised per MPC-002; build or timing-behaviour changes invoke the 33.4 change rule and may require re-gating including HIL repetition (criteria TBD). No build/ignition/operation instructions outside controlled conditions.

## 11. Safety

Compute supports safety gating (deterministic-enough behaviour for abort decisions within characterised limits) but grants no clearance. Compute failure behaviour and separation from the safety chain are per 33.11/Vol 13 methodology (criteria TBD). Hazardous-subsystem boundary: platform definition, determinism methodology, hooks, and gating only.

## 12. Performance

No compute performance targets are set. Throughput, latency, jitter, and load values are TBD. Success is characterised timing behaviour sufficient to support gate evidence (limits TBD), not numeric performance.

## 13. Verification & Validation

- MPC-001: Inspection (platform and software-build identity recorded for each gated test — TBD)
- MPC-002: Analysis (determinism methodology applied with documented limits — method and values TBD)
- MPC-003: Inspection (HIL hooks exist per Vol 19.9 provisions — list TBD)
- MPC-004: Inspection (non-representativeness stated; no production promotion path except 33.20 record)
- MVP compute verification does not constitute production compute verification (separate baseline).

## 14. Risks

- Uncharacterised timing behaviour → control-margin evidence (ISS-006) uninterpretable; mitigation: MPC-002 determinism methodology TBD before gated flights
- Unrecorded software-build changes between tests; mitigation: MPC-001 build identity + 33.4 change rule
- Missing HIL hooks → HIL evidence gap before flight stages; mitigation: MPC-003 hooks TBD with Vol 19.9
- Prototype compute mistaken for production architecture; mitigation: MPC-004 non-representativeness per MVP-005

## 15. Open Issues

- Compute platform and software-build identification for MPC-001: TBD
- Determinism methodology, metrics, limits, and characterisation method for MPC-002: TBD
- HIL hook list and Vol 19.9 interface provisions for MPC-003: TBD
- Non-representativeness limits and lesson-capture method for MPC-004: TBD

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on 33.3 compute allocation, 33.4 software-build control, 33.5 component instances, 33.7 avionics hosting, 33.9 sensor inputs, 33.11 separation criteria, 33.12 data taps, Vol 19.9 HIL capability, 33.13/33.14 stage definitions, 33.20 handover requirements.

## 18. Traceability

Parents: MVP-001 (gated demonstration), MVP-002 (evidence), MVP-005 (no auto-promotion), MRQ-001/MRQ-004 (demonstration and data capture), MAR-003 (compute segment), DDR-001. Children: HIL test records (Vol 19.9), 33.13/33.14 gate records, 33.19 exit evidence, 33.20 handover dispositions. RTM: REQ-HFPX-MPC-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined; Vol 33 separate from production baselines. Prototype compute definitions never auto-promote; production effect only via the 33.20 transition gate.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 33.8) |
