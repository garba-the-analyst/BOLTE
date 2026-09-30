# Operational Concept

**Document ID:** HFPX-SYS-OPC-001  
**Revision:** B (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 1 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Describe how HFP-X is operated at a high level: actors, roles, environments and operating principles. Owns Chapter 01.2; detail scenarios live in CONOPS (01.3).

## 2. Scope

Covers nominal operations (pre-flight through post-flight) and the principles for off-nominal handling (abort, emergency stabilisation, recovery). Applies to both the unmanned demonstrator (near-term) and the human-carrying objective (long-term, gated). Envelopes and limits are TBD.

## 3. Applicable Documents

- HFPX-SYS-MIS-001 Mission Definition; HFPX-SYS-CON-001 CONOPS; HFPX-SYS-STK-001 Stakeholder Requirements
- HFPX-SYS-REQ-001 SyRS (stub); HFPX-OPS-xxx future volumes (Vol 26 Operations, Vol 30 Training)
- HFP prompt §§12–13 (system breakdown, flight modes)

## 4. Definitions & Acronyms

- PIC/Operator: pilot-in-command (human) or remote operator (demonstrator) — authority TBD
- Ground station: monitoring/command/telemetry node (SYS-18)
- Flight modes (15): pre-flight, engine start, ground idle, hover, hover manoeuvre, transition, horizontal acceleration, cruise, horizontal deceleration, reverse transition, landing, shutdown, emergency stabilisation, emergency recovery, safe/aborted state

## 5. System Context

```text
PILOT/OPERATOR ↔ SMART HELMET/HMI ↔ FLIGHT CONTROL ↔ PROPULSION/AIRFRAME
       ↕                  ↕                    ↕
GROUND STATION ↔ TELEMETRY/COMMS ↔ SAFETY COMPUTER ↔ RECOVERY SYSTEM
```

All links are monitored; loss-of-link behaviour is TBD (Vol 11.9). Human-system integration per Vol 12/Vol 30.

## 6. Requirements

| ID | Requirement (shall) | Verification |
| --- | --- | --- |
| REQ-HFPX-OPC-001 | Operations shall define distinct hover, transition and horizontal-flight procedures; hover and horizontal flight shall not be assumed to share control laws. | Inspection |
| REQ-HFPX-OPC-002 | Every flight shall be conducted within a defined operating envelope (limits TBD) with pre-flight, start, hover, transition, cruise, landing and shutdown procedures. | Demonstration |
| REQ-HFPX-OPC-003 | Every flight shall maintain telemetry to the ground station with defined loss-of-link behaviour (TBD). | Demonstration |
| REQ-HFPX-OPC-004 | Emergency stabilisation, emergency recovery and safe/aborted states shall be defined operating states with entry/exit criteria (TBD). | Analysis |
| REQ-HFPX-OPC-005 | Human-carrying operations shall require qualified pilot, controlled range and flight authorisation (criteria TBD, Vol 25/26/30). | Inspection |

## 7. Architecture

Operational nodes: air vehicle, pilot/operator, ground crew, ground station, range authority. Node responsibilities TBD except the principle that the safety system can command stabilisation/recovery independently of the primary control path (detail in SAD safety view).

## 8. Detailed Design

Not applicable — procedures (Vol 26), training (Vol 30) and envelope data (Vol 06/19) are TBD.

## 9. Interfaces

- HMI: helmet/HUD, audio, alerts (Vol 10); pilot controls (Vol 12)
- Comms/telemetry: Vol 11; navigation/sensors: Vol 09; operations procedures: Vol 26; training: Vol 30

## 10. Operational Concept

This document *is* the high-level concept: operate only inside TBD envelopes, only through gated progression (DDR-001), with ground monitoring on every flight and explicit emergency states. Scenario detail is in CONOPS.

## 11. Safety

Off-nominal handling is a first-class operating principle, not an add-on. Recovery effectiveness at low altitude/hover is unproven (ISS-008); operating envelopes shall be constrained until Vol 13 analysis exists. No hazardous operating instructions are given here (prompt §34).

## 12. Performance

Operating envelopes (wind, visibility, temperature, altitude, endurance) are TBD. No minima/maxima stated.

## 13. Verification & Validation

Verified by inspection (procedures exist and match flight modes) and demonstration (ground rehearsals, Vol 23 ground tests). Validated by stakeholder walkthrough at SRR.

## 14. Risks

- Envelope unknown → procedures are placeholders; mitigation: Vol 06/19 modelling before TRR
- Operator overload (prone flight + HUD + propulsion monitoring); mitigation: human-factors programme (Vol 30.7–30.9)

## 15. Open Issues

ISS-002 (ops concept unapproved), plus TBD: operating limitations (26.2), weather limitations (26.11), comms procedures (26.13).

## 16. Assumptions


_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on CONOPS scenarios, HMI design (Vol 10), comms design (Vol 11), envelope models (Vol 06/19), regulatory authorisation (Vol 25).

## 18. Traceability

Parent: Mission (REQ-HFPX-MIS-001..004). Children: CONOPS scenarios, SyRS operational requirements, Vol 26 procedures, Vol 30 training. RTM: REQ-HFPX-OPC-001..005 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 1 draft, CONCEPT, not baselined.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 1 draft (Chapter 01.2) |
| B | 2026-09-29 | Assumptions removed; all unknowns recorded as TBD (no assumptions raised or relied upon). |
