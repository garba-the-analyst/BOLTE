# Prototype Sensors

**Document ID:** HFPX-MVP-PSN-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined; Vol 33 separate from production  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the prototype sensor complement, its calibration methodology, and its data-quality methodology for supporting gate evidence in controlled testing. Owns Chapter 33.9.

## 2. Scope

Covers prototype sensor-complement definition; calibration methodology with Vol 09 hooks; data-quality methodology; and installation/interface provisions with 33.12 hooks. Test methodology and gating only — no build/ignition/operation instructions for high-energy propulsion outside controlled conditions.

Vol 33 is SEPARATE from production baselines. No sensor choice here constrains production design; reuse is governed by the 33.20 transition gate only.

## 3. Applicable Documents

- HFPX-MVP-OBJ-001 MVP Objectives (MVP-001..005, DDR-001 risk note)
- HFPX-MVP-REQ-001 MVP System Requirements (Chapter 33.2; REQ-HFPX-MRQ-001..006)
- HFPX-MVP-ARC-001 MVP Architecture (Chapter 33.3; MAR-003 sensor segment, MAR-005 instrumentation provisions)
- HFPX-MVP-CFG-001 Prototype Configuration (Chapter 33.4; sensors under index control)
- Future: 33.5 experimental components, 33.7 avionics, 33.8 flight computer, 33.11 safety system, 33.12 instrumentation, 33.13/33.14 test programmes, 33.20 transition; Vol 09 sensing (including 09.17 calibration); Vol 13 safety

## 4. Definitions & Acronyms

- MPS: MVP Prototype-Sensor Requirement — prototype sensor obligation in this document (does not set production sensor requirements)
- Sensor complement: the controlled list of prototype sensors hosted on the demonstrator and test articles (complement TBD)
- Calibration methodology: the defined method establishing sensor trust for gate evidence, with Vol 09 hooks (method and values TBD per Vol 09.17)
- Data-quality methodology: the defined method for flagging validity, dropouts, and limits of sensor data used as evidence (method TBD)
- 33.20 transition gate: sole route for sensor lessons to inform production; no auto-promotion

## 5. System Context

Prototype sensors feed control, safety decisions, and recorded evidence for the demonstrator only:

```text
MRQ-001/MRQ-004 + MAR-003/MAR-005 ── allocation ──► MPS-001..004 (this document, Ch 33.9)
        │                                                        │
        ▼                                                        ▼
  flight computer (33.8) + avionics (33.7) ◄── data ──► instrumentation dataset (33.12) + gates (33.13/33.14)
```

> This volume is SEPARATE from the production-aircraft documentation. Production-design transition is governed by 33.20.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-MPS-001 | The MVP prototype sensor complement shall be defined as a controlled list of sensors with identity and installation for each test article and test event (complement and installation TBD). | MVP-002, MRQ-004, MAR-003 | Inspection |
| REQ-HFPX-MPS-002 | The MVP prototype sensors relied upon for gate evidence shall be calibrated by a defined methodology with hooks to Vol 09 calibration provisions (method and values TBD per Vol 09.17). | MVP-002, MRQ-004 | Inspection |
| REQ-HFPX-MPS-003 | The MVP prototype sensor data used as gate evidence shall carry defined data-quality characterisation covering validity, dropouts, and limits (method TBD). | MRQ-004, MAR-005 | Inspection |
| REQ-HFPX-MPS-004 | The MVP prototype sensor interfaces and installation provisions shall be defined with hooks to the 33.12 instrumentation dataset including mounting, power, data-bus, and software provisions (list TBD). | MRQ-004, MAR-005, DDR-001 | Inspection |

All sensor identities, ranges, accuracies, rates, and calibration values are TBD.

## 7. Architecture

Sensor architecture (placeholder): complement instances feeding flight computer (33.8) and avionics (33.7) with taps to the instrumentation dataset (33.12) and safety chain where allocated (33.11). Block diagrams, signal lists, and mounting provisions TBD; all prototype-only.

## 8. Detailed Design

Not applicable — no sensor selection parameter, mounting drawing, signal conditioning, or calibration coefficient is baselined here. All design values TBD in later tranches, if at all, and remain prototype-only.

## 9. Interfaces

Sensor interfaces: flight-computer/avionics inputs (33.7/33.8), safety-chain inputs where allocated (33.11), instrumentation dataset hooks (33.12), calibration provisions (Vol 09.17), configuration index for sensor identity and calibration record (33.4). Production sensor interface is lessons/data handover via the 33.20 transition gate only.

## 10. Operational Concept

Test methodology and gating only. Gated tests proceed only with the recorded sensor complement at the required calibration and data-quality standard (TBD); sensor or calibration changes invoke the 33.4 change rule and may require re-gating. No build/ignition/operation instructions outside controlled conditions.

## 11. Safety

Sensors support safety gating (data for abort and recovery-trigger decisions within characterised quality limits) but grant no clearance. Sensor failure behaviour and quality limits are per 33.11/Vol 13 methodology (criteria TBD). Hazardous-subsystem boundary: complement definition, calibration methodology, quality methodology, and gating only.

## 12. Performance

No sensor performance targets are set. Range, accuracy, rate, latency, and drift values are TBD. Success is evidence support (calibrated data with characterised quality per gate), not numeric performance.

## 13. Verification & Validation

- MPS-001: Inspection (complement list exists with identity and installation per test article/event — TBD)
- MPS-002: Inspection (calibration methodology applied with Vol 09.17 hooks and records — TBD)
- MPS-003: Inspection (data-quality characterisation present for evidence data — method TBD)
- MPS-004: Inspection (interface and installation provisions with 33.12 hooks defined — list TBD)
- MVP sensor verification does not constitute production sensor verification (separate baseline).

## 14. Risks

- Uncalibrated sensors feeding gate evidence → false model validation; mitigation: MPS-002 calibration methodology TBD before gated flights
- Unflagged bad data admitted as evidence; mitigation: MPS-003 data-quality characterisation TBD before gated flights
- Undefined complement → unrecorded sensor changes between tests; mitigation: MPS-001 complement list + 33.4 change rule
- Prototype sensors mistaken for production sensing solution; mitigation: 33.20 transition gate, no auto-promotion per MVP-005

## 15. Open Issues

- Sensor complement, identity, installation, and ownership for MPS-001: TBD
- Calibration methodology, standards, intervals, records, and Vol 09.17 hooks for MPS-002: TBD
- Data-quality methodology, validity flags, dropout handling, and limits for MPS-003: TBD
- Interface definitions and 33.12 hook list for MPS-004: TBD

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on 33.3 sensor allocation, 33.4 sensor/calibration record control, 33.5 component instances, 33.7/33.8 data consumers, 33.11 data needs for safety decisions, 33.12 dataset definition, Vol 09.17 calibration provisions, 33.13/33.14 stage definitions, 33.20 handover requirements.

## 18. Traceability

Parents: MVP-002 (evidence), MVP-005 (no auto-promotion), MRQ-004 (data capture), MAR-003/MAR-005 (sensors and instrumentation provisions), DDR-001. Children: 33.12 dataset entries, 33.13/33.14 gate records, 33.19 exit evidence, 33.20 handover dispositions. RTM: REQ-HFPX-MPS-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined; Vol 33 separate from production baselines. Prototype sensor definitions never auto-promote; production effect only via the 33.20 transition gate.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 33.9) |
