# Prototype Safety System

**Document ID:** HFPX-MVP-PSS-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined; Vol 33 separate from production  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the independent prototype safety chain — including stabilisation and recovery-trigger functions — and its verification methodology for gating controlled tests. Owns Chapter 33.11.

## 2. Scope

Covers safety-chain independence; stabilisation-function definition; recovery-trigger-function definition; and safety-function verification methodology. Test methodology and gating only — no build/ignition/operation instructions for high-energy propulsion outside controlled conditions.

Vol 33 is SEPARATE from production baselines. No safety-system choice here certifies any flight or constrains production safety design; reuse is governed by the 33.20 transition gate only.

## 3. Applicable Documents

- HFPX-MVP-OBJ-001 MVP Objectives (MVP-001..005, DDR-001 risk note)
- HFPX-MVP-REQ-001 MVP System Requirements (Chapter 33.2; REQ-HFPX-MRQ-005 safety-gating, MRQ-006)
- HFPX-MVP-ARC-001 MVP Architecture (Chapter 33.3; MAR-004 safety chain)
- HFPX-MVP-CFG-001 Prototype Configuration (Chapter 33.4; safety-system configuration under index control)
- Future: 33.5 experimental components, 33.7–33.10 command/data segments, 33.12 instrumentation, 33.13/33.14 test programmes, 33.19 exit criteria, 33.20 transition; Vol 13 safety; Vol 23 range safety

## 4. Definitions & Acronyms

- MSS: MVP Safety-System Requirement — prototype safety obligation in this document (does not set production safety requirements)
- Independent chain: prototype safety functions separable from nominal control and data paths to a defined methodology (independence criteria TBD)
- Stabilisation function: prototype function bounding attitude/rate excursions within a gated envelope (logic and thresholds TBD)
- Recovery-trigger function: prototype function initiating the defined recovery sequence when trigger conditions hold (logic and thresholds TBD)
- 33.20 transition gate: sole route for safety lessons to inform production; no auto-promotion

## 5. System Context

The prototype safety chain gates every controlled test independently of nominal paths:

```text
MRQ-005/MRQ-006 + MAR-004 ── allocation ──► MSS-001..004 (this document, Ch 33.11)
        │                                              │
        ▼                                              ▼
  nominal paths (33.7/33.8/33.9) ── independence ──► ground station abort (33.10) + gates (33.13/33.14)
```

> This volume is SEPARATE from the production-aircraft documentation. Production-design transition is governed by 33.20.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-MSS-001 | The MVP prototype safety system shall provide a safety chain with defined independence from nominal control and data paths covering separation, authority, and failure-behaviour methodology (independence criteria TBD). | MVP-004, MRQ-005, MAR-004, DDR-001 | Analysis |
| REQ-HFPX-MSS-002 | The MVP prototype safety system shall provide a stabilisation function with defined logic and thresholds bounding excursions within each gated envelope (logic and thresholds TBD). | MVP-004, MRQ-005, MAR-004 | Demonstration |
| REQ-HFPX-MSS-003 | The MVP prototype safety system shall provide a recovery-trigger function with defined logic and thresholds initiating the defined recovery sequence (logic, thresholds, and sequence TBD; ISS-008 limits apply). | MVP-004, MRQ-005, MAR-004 | Demonstration |
| REQ-HFPX-MSS-004 | The MVP prototype safety-system functions shall be verified by a defined methodology across ground, SIL, HIL, and unmanned stages with coverage and entrance criteria for each stage (methodology and coverage TBD). | MVP-004, MRQ-005 | Test |

All logic parameters, thresholds, timing values, and envelope values are TBD.

## 7. Architecture

Safety architecture (placeholder): independent chain observing nominal paths (33.7/33.8/33.9) with stabilisation and recovery-trigger outputs coordinated with ground-station abort (33.10) and recorded via instrumentation (33.12). Block diagrams, signal lists, authority wiring, and separation provisions TBD; all prototype-only.

## 8. Detailed Design

Not applicable — no safety logic, threshold, schematic, or sequence design is baselined here. All design values TBD in later tranches, if at all, and remain prototype-only with no certification claim.

## 9. Interfaces

Safety interfaces: nominal-path observation taps (33.7/33.8/33.9), ground-station abort coordination (33.10), propulsion-chain safety interfaces (33.6), instrumentation recording (33.12), range-safety coordination (Vol 23), hazard analyses (Vol 13), configuration index for safety-logic revision (33.4). Production safety interface is lessons/data handover via the 33.20 transition gate only.

## 10. Operational Concept

Test methodology and gating only. No gated test proceeds without its required safety-chain revision, stabilisation coverage, and recovery-trigger arming at the defined standard (TBD); any safety-system change invokes the 33.4 change rule with review per Vol 13 methodology and may require re-verification and re-gating. No build/ignition/operation instructions outside controlled conditions.

## 11. Safety

This system provides prototype risk reduction for controlled testing only — not clearance, certification, or production safety substantiation. Hazard analysis is Vol 13; range safety is Vol 23; recovery-system limits (ISS-008) constrain MVP envelopes from the first flight. Hazardous-subsystem boundary: chain definition, function logic, verification methodology, and gating only.

## 12. Performance

No safety-system performance targets are set. Response-time, threshold, and coverage values are TBD. Success is gated verification coverage (each function demonstrated per stage methodology), not numeric performance.

## 13. Verification & Validation

- MSS-001: Analysis (independence methodology applied with separation/authority/failure-behaviour evidence — criteria TBD)
- MSS-002: Demonstration (stabilisation response in ground/SIL/HIL and unmanned tests — logic/thresholds TBD)
- MSS-003: Demonstration (recovery-trigger response initiating the defined sequence — logic/thresholds TBD, ISS-008)
- MSS-004: Test (stage methodology executed with coverage records and entrance-criteria evidence — TBD)
- MVP safety verification does not constitute production safety verification or certification (separate baselines).

## 14. Risks

- Insufficient independence → common-cause loss of nominal and safety paths; mitigation: MSS-001 independence methodology TBD before gated flights
- Undefined stabilisation/recovery-trigger logic → late or missed safety action; mitigation: MSS-002/MSS-003 logic and thresholds TBD with demonstration
- Unverified safety revision flies in a gate; mitigation: MSS-004 stage methodology + 33.4 revision control
- Prototype safety functions mistaken for production safety substantiation; mitigation: 33.20 transition gate, no auto-promotion per MVP-005

## 15. Open Issues

- Independence criteria, separation method, authority, and failure-behaviour methodology for MSS-001: TBD
- Stabilisation logic, thresholds, and envelope mapping for MSS-002: TBD
- Recovery-trigger logic, thresholds, recovery sequence, and ISS-008 limit mapping for MSS-003: TBD
- Verification methodology, stage coverage, and entrance criteria for MSS-004: TBD

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on 33.3 safety-chain allocation, 33.4 safety-logic revision control, 33.5 component instances, 33.7–33.10 nominal/abort partners, 33.12 recording hooks, 33.13/33.14 stage definitions, 33.19 exit evidence needs, Vol 13 hazard methodology, Vol 23 range provisions, 33.20 handover requirements.

## 18. Traceability

Parents: MVP-004 (controlled safety progression), MRQ-005/MRQ-006 (safety functions and gating), MAR-004 (safety chain), DDR-001. Children: 33.13/33.14 safety-gate records, 33.19 exit evidence, 33.20 handover dispositions. RTM: REQ-HFPX-MSS-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined; Vol 33 separate from production baselines. Prototype safety definitions never auto-promote and grant no clearance; production effect only via the 33.20 transition gate.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 33.11) |
