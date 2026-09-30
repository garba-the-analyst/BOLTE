# Prototype Ground Station

**Document ID:** HFPX-MVP-PGS-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined; Vol 33 separate from production  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the prototype ground station's functions, abort authority, staffing, and record methodology for commanding, monitoring, and gating controlled tests. Owns Chapter 33.10.

## 2. Scope

Covers ground-station function definition with Vol 11 hooks; abort-authority and command methodology; staffing and roles; and telemetry/record methodology. Test methodology and gating only — no build/ignition/operation instructions for high-energy propulsion outside controlled conditions.

Vol 33 is SEPARATE from production baselines. No ground-station choice here constrains production design; reuse is governed by the 33.20 transition gate only.

## 3. Applicable Documents

- HFPX-MVP-OBJ-001 MVP Objectives (MVP-001..005, DDR-001 risk note)
- HFPX-MVP-REQ-001 MVP System Requirements (Chapter 33.2; REQ-HFPX-MRQ-001..006)
- HFPX-MVP-ARC-001 MVP Architecture (Chapter 33.3; MAR-003 ground-station segment)
- HFPX-MVP-CFG-001 Prototype Configuration (Chapter 33.4; ground station under index control)
- Future: 33.5 experimental components, 33.7 avionics, 33.11 safety system, 33.12 instrumentation, 33.13/33.14 test programmes, 33.19 exit criteria, 33.20 transition; Vol 11 ground systems (including 11.10 functions); Vol 13 safety; Vol 23 test programme

## 4. Definitions & Acronyms

- MGS: MVP Ground-Station Requirement — prototype ground-station obligation in this document (does not set production ground-system requirements)
- Ground-station function: a commanded, monitoring, or recording duty performed by the prototype ground station (functions TBD per Vol 11.10)
- Abort authority: the defined role and rule set that may command test termination (authority and criteria TBD)
- Staffing: the defined roles, responsibilities, and readiness required to conduct a gated test (staffing TBD)
- 33.20 transition gate: sole route for ground-station lessons to inform production; no auto-promotion

## 5. System Context

The prototype ground station commands and gates the demonstrator from the ground:

```text
MRQ-001/MRQ-004/MRQ-005/MRQ-006 + MAR-003 ── allocation ──► MGS-001..004 (this document, Ch 33.10)
        │                                                                │
        ▼                                                                ▼
  avionics link (33.7) + safety chain (33.11) ◄── command/monitor ──► gates (33.13/33.14) + records (33.12)
```

> This volume is SEPARATE from the production-aircraft documentation. Production-design transition is governed by 33.20.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-MGS-001 | The MVP prototype ground-station functions shall be defined with hooks to Vol 11 ground-system functions covering command, monitoring, telemetry, and recording duties (functions TBD per Vol 11.10). | MVP-001, MRQ-004, MAR-003 | Inspection |
| REQ-HFPX-MGS-002 | The MVP prototype ground station abort authority shall be defined with command methodology, decision criteria, and authorising roles for test termination (authority and criteria TBD). | MVP-004, MRQ-005, MAR-004 | Demonstration |
| REQ-HFPX-MGS-003 | The MVP prototype ground-station staffing shall be defined with roles, responsibilities, and readiness required for each gated test (staffing and readiness TBD). | MVP-001, MRQ-006 | Inspection |
| REQ-HFPX-MGS-004 | The MVP prototype ground station shall record command, telemetry, and decision data for each gated test to a defined record standard with retention (standard and retention TBD, hooks to 33.12). | MVP-002, MRQ-004 | Inspection |

All link parameters, display contents, staffing counts, timing values, and record-field values are TBD.

## 7. Architecture

Ground-station architecture (placeholder): command/monitor/record chain linked to avionics (33.7) with abort paths coordinated with the safety chain (33.11) and data feeds to instrumentation records (33.12). Layouts, link diagrams, console definitions, and authority wiring TBD; all prototype-only.

## 8. Detailed Design

Not applicable — no console layout, link parameter, display design, or procedure script is baselined here. All design values TBD in later tranches, if at all, and remain prototype-only.

## 9. Interfaces

Ground-station interfaces: avionics command/telemetry link (33.7), safety-chain abort coordination (33.11), instrumentation records (33.12), range/test infrastructure (Vol 23), regulatory authorisation (Vol 25), configuration index for ground-station hardware/software identity (33.4). Production ground-system interface is lessons/data handover via the 33.20 transition gate only.

## 10. Operational Concept

Test methodology and gating only. Gated tests proceed only with the defined functions staffed, abort authority present and empowered, and recording active (readiness TBD); loss of abort capability or recording invokes abort rules (criteria TBD). No build/ignition/operation instructions outside controlled conditions.

## 11. Safety

Ground-station abort authority is a safety-gating function, not a safety clearance. Abort logic, coordination with the independent safety chain, and authority limits are per 33.11/Vol 13 methodology (criteria TBD). Hazardous-subsystem boundary: functions, authority, staffing, records, and methodology only.

## 12. Performance

No ground-station performance targets are set. Link availability, latency, display, and staffing values are TBD. Success is gating support (command/monitor/abort/record available per gate), not numeric performance.

## 13. Verification & Validation

- MGS-001: Inspection (function list exists with Vol 11.10 hooks — TBD)
- MGS-002: Demonstration (abort authority defined and exercised in ground/SIL/HIL and unmanned tests — criteria TBD)
- MGS-003: Inspection (staffing roles, responsibilities, and readiness recorded per gated test — TBD)
- MGS-004: Inspection (command/telemetry/decision records present per gated test — standard TBD)
- MVP ground-station verification does not constitute production ground-system verification (separate baseline).

## 14. Risks

- Undefined functions → missing command/monitor/record coverage during a gate; mitigation: MGS-001 function list TBD before gated tests
- Ambiguous abort authority → delayed or disputed termination; mitigation: MGS-002 authority and criteria TBD with demonstration
- Understaffed or unready console during a gate; mitigation: MGS-003 readiness required for gating
- Lost decision records → exit claim unverifiable in 33.19; mitigation: MGS-004 record standard TBD + gate inspection

## 15. Open Issues

- Ground-station function list and Vol 11.10 hooks for MGS-001: TBD
- Abort authority, command methodology, decision criteria, and authorising roles for MGS-002: TBD
- Staffing roles, responsibilities, and readiness standard for MGS-003: TBD
- Record standard, fields, and retention for MGS-004: TBD

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on 33.3 ground-station allocation, 33.4 ground-station configuration identity, 33.7 link definitions, 33.11 abort/safety coordination, 33.12 record hooks, Vol 11.10 function provisions, 33.13/33.14 stage definitions, 33.19 exit evidence needs, 33.20 handover requirements.

## 18. Traceability

Parents: MVP-001 (gated demonstration), MVP-002 (evidence), MVP-004 (controlled safety progression), MRQ-004/MRQ-005/MRQ-006 (data capture, safety functions, gating), MAR-003/MAR-004 (ground-station and safety-chain segments), DDR-001. Children: 33.13/33.14 gate conduct records, 33.19 exit evidence, 33.20 handover dispositions. RTM: REQ-HFPX-MGS-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined; Vol 33 separate from production baselines. Prototype ground-station definitions never auto-promote; production effect only via the 33.20 transition gate.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 33.10) |
