# Functional Requirements

**Document ID:** HFPX-SYS-FUN-001  
**Revision:** B (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 2 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define system-level functional requirements for HFP-X (Chapter 01.7). This Tranche 2 draft establishes the functional decomposition — what the system shall do — without allocating design solutions or quantified performance, which remain TBD in subsystem volumes.

## 2. Scope

Covers core flight and mission-support functions: lift/thrust generation, attitude/velocity control, navigation/state estimation, health monitoring/fault response, and comms/telemetry. Excludes quantified performance (01.8), environmental limits (01.9), safety assurance detail (01.10), and human-factors detail (01.11).

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parent system requirements, esp. REQ-HFPX-SYS-001/002/004/005)
- HFPX-SYS-CON-001 CONOPS (operational threads, REQ-HFPX-CON-001/004)
- HFPX-SYS-ARC-001 SAD (stub; allocates functions to SYS-01..SYS-23)
- HFP prompt §§8–10 (requirements format, classification, traceability)

## 4. Definitions & Acronyms

- FUN: functional requirement tier; ID `REQ-HFPX-FUN-NNN`; verification: Analysis / Inspection / Demonstration / Test.
- TBD/TBC: unknown data; no values invented.
- FCS: flight control system; HMI: human-machine interface; fault response: detection plus defined system reaction, details TBD.

## 5. System Context

Functional tier derives system functions from SyRS and CONOPS threads:

```text
SYS-001/002/004/005 + CON-001/004 → FUN-001..005 → Subsystem functions (Vol 03–18) → V&V cases
```

These functions are necessary and collectively reviewed for sufficiency at SRR; completeness is TBC pending trades.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-FUN-001 | The system shall provide a lift/thrust generation function supporting controlled VTOL hover, transition, cruise, and landing per CONOPS threads (magnitudes TBD). | REQ-HFPX-SYS-001, REQ-HFPX-CON-001 | Test (unmanned first) |
| REQ-HFPX-FUN-002 | The system shall provide an attitude and velocity control function that stabilises and manoeuvres the vehicle within the defined envelope using deterministic primary control (limits TBD). | REQ-HFPX-SYS-002, REQ-HFPX-CON-004 | Analysis + Test |
| REQ-HFPX-FUN-003 | The system shall provide a navigation and state-estimation function fusing inertial, GNSS, barometric, and air-data sources to supply position, velocity, and attitude estimates (accuracies TBD). | REQ-HFPX-SYS-004, REQ-HFPX-CON-001 | Analysis + Test |
| REQ-HFPX-FUN-004 | The system shall provide a health-monitoring and fault-response function that detects defined faults and commands a defined safe response including warning annunciation (thresholds and responses TBD). | REQ-HFPX-SYS-005, REQ-HFPX-SYS-002 | Demonstration + Test |
| REQ-HFPX-FUN-005 | The system shall provide a communications and telemetry function exchanging command, status, warning, and flight data between the vehicle, pilot/operator interfaces, and ground station (rates and ranges TBD). | REQ-HFPX-SYS-005, REQ-HFPX-CON-004 | Demonstration |

## 7. Architecture

Starter allocation (SAD owns authoritative mapping): FUN-001 → propulsion/aero/airframe; FUN-002 → FCS + AI monitoring (advisory only); FUN-003 → navigation/sensors/computing; FUN-004 → FCS/safety computer/health management; FUN-005 → comms/helmet/ground station.

## 8. Detailed Design

Not applicable — functional level only. Subsystem functional decomposition and design solutions live in Vol 03–18 and are TBD.

## 9. Interfaces

Functional interfaces TBD in Chapter 01.16 and Vol 02 ICDs. Placeholders: propulsion command, sensor data bus, pilot/operator command paths, telemetry downlink, ground-station uplink. No interface values are approved.

## 10. Operational Concept

Each function maps to ≥1 CONOPS thread (nominal and off-nominal). Thread-to-function mapping table is TBD in the V&V Plan; unmanned demonstration precedes any human flight per safety gating.

## 11. Safety

Functional failures feed Vol 13 safety analyses (FHA/FMEA/FTA, to follow). FUN-002 and FUN-004 carry safety significance: deterministic control and fault response assumptions are TBD and require validation via safety analyses by change record.

## 12. Performance

No functional requirement in this document quantifies performance. All response times, accuracies, endurances, and capacities are TBD and owned by the performance tier (01.8) and budgets/models via ISS-007.

## 13. Verification & Validation

Each requirement states its method above; verification IDs and cases are TBD in the V&V Plan (Vol 22). Strategy: analysis of functional logic, ground demonstration, then unmanned flight test. Requirements without a verification method are rejected at SRR.

## 14. Risks

- Functions defined before envelopes/budgets exist → allocation churn; mitigation: CONCEPT status explicit, SAD feedback loop per review.
- Fault-response scope creep without FHA input; mitigation: gate FUN-004 detail on Vol 13 analyses.

## 15. Open Issues

ISS-002 (SyRS completeness), ISS-003/004 (trades shape functional allocation), ISS-006/007/008 (feasibility unknowns propagate into subsystem functions). Functional completeness is TBC pending SRR.

## 16. Assumptions


_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on CONOPS stability, stakeholder approval (STK), SAD allocation feedback, safety analyses (Vol 13), and V&V Plan cases. Changes to SYS-001/002/004/005 propagate to this tier by change record.

## 18. Traceability

Parents: REQ-HFPX-SYS-001/002/004/005, REQ-HFPX-CON-001/004 (see table). Children: subsystem functional requirements (Vol 03–18), SAD views, V&V cases, RTM rows. RTM seed for FUN-001..005 added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0 (structure only) — Tranche 2 draft, not baselined. Changes require change control; quantified or allocated detail requires new revisions.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 2 draft (Chapter 01.7) |
| B | 2026-09-29 | Assumptions removed; all unknowns recorded as TBD (no assumptions raised or relied upon). |
