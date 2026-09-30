# Prototype Avionics

**Document ID:** HFPX-MVP-PAV-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined; Vol 33 separate from production  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the prototype avionics suite, its test-grade use policy, and its interfaces for hosting command, telemetry, and data-capture methodology in controlled testing. Owns Chapter 33.7.

## 2. Scope

Covers prototype avionics suite definition; COTS/test-grade use policy; internal and external avionics interfaces; and the prototype-only status of all avionics choices. Test methodology and gating only — no build/ignition/operation instructions for high-energy propulsion outside controlled conditions.

Vol 33 is SEPARATE from production baselines. No avionics choice here constrains production design; reuse is governed by the 33.20 transition gate only.

## 3. Applicable Documents

- HFPX-MVP-OBJ-001 MVP Objectives (MVP-001..005, DDR-001 risk note)
- HFPX-MVP-REQ-001 MVP System Requirements (Chapter 33.2; REQ-HFPX-MRQ-001..006)
- HFPX-MVP-ARC-001 MVP Architecture (Chapter 33.3; MAR-003 avionics/compute/sensors/ground-station segments)
- HFPX-MVP-CFG-001 Prototype Configuration (Chapter 33.4; avionics under index control)
- Future: 33.5 experimental components, 33.8 flight computer, 33.9 sensors, 33.10 ground station, 33.11 safety system, 33.12 instrumentation, 33.13/33.14 test programmes, 33.20 transition; Vol 13 safety

## 4. Definitions & Acronyms

- MPA: MVP Prototype-Avionics Requirement — prototype avionics obligation in this document (does not set production avionics requirements)
- Prototype avionics suite: the set of test-grade avionics units, harnesses, and software identifiers hosted on the demonstrator (suite TBD)
- COTS/test-grade policy: the rule governing use of commercial or test-grade avionics as non-certified prototype items (policy TBD)
- Avionics interface: command, telemetry, power, or data exchange point between avionics and other MVP segments (interfaces TBD)
- 33.20 transition gate: sole route for avionics lessons to inform production; no auto-promotion

## 5. System Context

Prototype avionics hosts the command/telemetry/data path for the demonstrator only:

```text
MRQ-001/MRQ-004 + MAR-003 ── allocation ──► MPA-001..004 (this document, Ch 33.7)
        │                                              │
        ▼                                              ▼
  flight computer (33.8) + sensors (33.9) ◄── interfaces ──► ground station (33.10) + instrumentation (33.12)
```

> This volume is SEPARATE from the production-aircraft documentation. Production-design transition is governed by 33.20.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-MPA-001 | The MVP prototype avionics suite shall be defined as a controlled list of units, harnesses, and software identifiers hosted on the demonstrator (suite contents and revisions TBD). | MVP-001, MRQ-001, MAR-003 | Inspection |
| REQ-HFPX-MPA-002 | The MVP programme shall govern COTS and test-grade avionics use by a defined policy establishing prototype-only status with no certification or production-design claim (policy TBD). | MVP-005, MRQ-004, MAR-003 | Inspection |
| REQ-HFPX-MPA-003 | The MVP prototype avionics interfaces shall be defined for command, telemetry, power, and data exchange with the flight computer, sensors, ground station, safety chain, and instrumentation (interface definitions TBD). | MRQ-004, MAR-003 | Inspection |
| REQ-HFPX-MPA-004 | The MVP prototype avionics shall be explicitly non-representative of production avionics and shall inform production only via lessons and data through the 33.20 transition gate (per MVP-005). | MVP-005, MAR-003, DDR-001 | Inspection |

All part identities, revisions, signal lists, timing values, and performance figures are TBD.

## 7. Architecture

Avionics architecture (placeholder): suite instances connected via defined interfaces to flight computer (33.8), sensors (33.9), ground station (33.10), safety chain (33.11), and instrumentation hooks (33.12). Block diagrams, wiring, protocols, and redundancy provisions TBD; all prototype-only.

## 8. Detailed Design

Not applicable — no avionics schematic, layout, protocol parameter, or setpoint is baselined here. All design values TBD in later tranches, if at all, and remain prototype-only.

## 9. Interfaces

Avionics interfaces: flight-computer hosting (33.8), sensor inputs (33.9), ground-station command/telemetry (33.10), safety-chain separation (33.11), instrumentation taps (33.12), configuration index (33.4). Production avionics interface is lessons/data handover via the 33.20 transition gate only.

## 10. Operational Concept

Test methodology and gating only. Avionics configurations used in gated tests are those recorded in the configuration index with as-built state at the required standard (TBD); interface or suite changes invoke the 33.4 change rule and may require re-gating. No build/ignition/operation instructions outside controlled conditions.

## 11. Safety

Avionics supports safety gating (command/telemetry availability for abort decisions) but grants no clearance. Avionics failure behaviour and separation from the safety chain are per 33.11/Vol 13 methodology (criteria TBD). Hazardous-subsystem boundary: suite definition, policy, interfaces, and methodology only.

## 12. Performance

No avionics performance targets are set. Latency, throughput, availability, and accuracy values are TBD. Success is evidence support (command/telemetry/data captured per gate), not numeric performance.

## 13. Verification & Validation

- MPA-001: Inspection (suite list exists with units, harnesses, software identifiers — TBD)
- MPA-002: Inspection (COTS/test-grade policy exists and asserts prototype-only status — TBD)
- MPA-003: Inspection (interface definitions exist for all listed exchanges — TBD)
- MPA-004: Inspection (non-representativeness stated; no production promotion path except 33.20 record)
- MVP avionics verification does not constitute production avionics verification (separate baseline).

## 14. Risks

- Undefined suite → unrecorded avionics changes between tests; mitigation: MPA-001 suite list TBD before gated flights
- Test-grade units mistaken for production solutions; mitigation: MPA-002 policy + MPA-004 non-representativeness per MVP-005
- Undefined interfaces → integration faults and lost data; mitigation: MPA-003 interface definitions TBD before gated flights
- Avionics shortcuts masking control-margin issues (ISS-006); mitigation: gate evidence review + 33.19 exit criteria TBD

## 15. Open Issues

- Prototype avionics suite contents, revisions, and ownership for MPA-001: TBD
- COTS/test-grade use policy, acceptance checks, and limitations for MPA-002: TBD
- Interface definitions, signal lists, and protocol selections for MPA-003: TBD
- Non-representativeness limits and lesson-capture method for MPA-004: TBD

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on 33.3 segment allocation, 33.4 configuration control, 33.5 component instances, 33.8/33.9/33.10 interface partners, 33.11 separation criteria, 33.12 instrumentation needs, 33.13/33.14 stage definitions, 33.20 handover requirements.

## 18. Traceability

Parents: MVP-001 (gated demonstration), MVP-002 (evidence), MVP-005 (no auto-promotion), MRQ-001/MRQ-004 (demonstration and data capture), MAR-003 (avionics/compute/sensors/ground-station segments), DDR-001. Children: 33.8/33.9/33.10 interface implementations, 33.13/33.14 gate records, 33.19 exit evidence, 33.20 handover dispositions. RTM: REQ-HFPX-MPA-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined; Vol 33 separate from production baselines. Prototype avionics definitions never auto-promote; production effect only via the 33.20 transition gate.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 33.7) |
