# Fuel Isolation (Chapter 05.14)

**Document ID:** HFPX-FUEL-ISO-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Hold the fuel isolation requirements for HFP-X in one chapter. This Tranche 4 draft establishes the requirement set structure, isolation functions, authority (including emergency), verification, and fail-safe-direction provision; all quantitative values and the fail-safe direction are TBD.

## 2. Scope

Covers Chapter 05.14 Fuel Isolation: isolation valves/functions, isolation authority including emergency authority, isolation verification, and fail-safe direction. Valve selection, placement, timing, authority logic, and detailed design are TBD.

> **Hazardous-subsystem boundary.** Content in this document is limited to requirements, architecture, interfaces, test methodology and safety analysis. It shall not contain instructions for constructing, actuating, maintaining, or operating fuel isolation or propulsion outside appropriate engineering, test, safety and regulatory controls. Any active fuel handling or isolation actuation occurs only under controlled conditions per Vol 13 / Vol 22 / Vol 33.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parents REQ-HFPX-SYS-003, REQ-HFPX-SYS-006)
- FRQ tier (functional requirements, TBD — parent tier)
- SAF tier (safety requirements, TBD) and SCA-006
- HFPX-SYS-ARC-001 SAD (allocation to fuel subsystem, TBD)
- HFPX-FUEL-LEK-001 Leak Detection (isolation-trigger source, Tranche 4 draft)
- Vol 02 ICDs (fuel ↔ FCS / avionics / isolation-command interfaces, TBD)
- Vol 13 Safety analyses; Vol 22 V&V Plan (not written); Vol 33 Test (controlled conditions)
- HFP prompt §§8–10, 14, 19, 32, 34

## 4. Definitions & Acronyms

- FIS: fuel isolation thread; requirement IDs `REQ-HFPX-FIS-001..004`
- Isolation valves/functions: means of interrupting fuel flow or isolating zones (implementation TBD)
- Isolation authority: entities/logic permitted to command isolation, including emergency authority (TBD)
- Isolation verification: confirmation that isolation has been achieved (method TBD)
- Fail-safe direction: behaviour on loss of power/command (to be determined, not assumed)
- TBD/TBC/A-XXX: unknown data handling; no invented values
- Verification: Analysis / Inspection / Demonstration / Test

## 5. System Context

Fuel isolation is an action branch of the fuel safety thread:

```text
DETECTION (leak/pressure/temperature, Ch 05.11–05.13) → AUTHORITY LOGIC (TBD) → ISOLATION (this chapter)
COMMAND (normal/emergency, TBD) ──────────────────────↗                                    ↓
                                                                              ISOLATION VERIFICATION → HMI / SAFETY PATH
```

Isolation executes commands from authorised sources; command sources and arbitration are TBD. Allocation to valves, actuators, and computing is TBD in the SAD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-FIS-001 | The fuel system shall provide isolation valves/functions at locations to be determined (TBD). | FRQ tier (TBD), REQ-HFPX-SYS-003 | Inspection |
| REQ-HFPX-FIS-002 | The fuel system shall implement isolation authority, including emergency isolation authority to be determined (TBD), from sources to be determined (TBD). | REQ-HFPX-SYS-003, SAF tier (TBD) | Demonstration |
| REQ-HFPX-FIS-003 | The fuel system shall provide isolation verification that confirms isolation state (method and criteria TBD). | SCA-006, SAF tier (TBD) | Test |
| REQ-HFPX-FIS-004 | The fuel system shall implement a fail-safe direction on loss of power or command that is to be determined (TBD, not assumed). | REQ-HFPX-SYS-003, SCA-006 | Analysis |

No valve count, placement, timing, authority assignment, verification criterion, or fail-safe state in this document is approved; all are TBD. The fail-safe direction is explicitly undetermined and shall not be assumed.

## 7. Architecture

Logical allocation (starter — SAD owns authoritative allocation): authority/arbitration logic (TBD) → actuators/valves per zone (TBD) → position/state feedback → verification logic → annunciation to HMI / safety path. Redundancy, independence from primary control, power segregation, manual/emergency paths, and failure semantics are TBD. No valve type, count, or placement is baselined.

## 8. Detailed Design

Not applicable — requirements/architecture level only. No detailed design, part selection, schematic, software design, or installation drawing is contained or approved in this revision.

## 9. Interfaces

Interface placeholders (controlled via SAD §9 / Vol 02 ICDs, all TBD): fluid/mechanical interface to storage/distribution (05.4/05.5); command interface from authorised sources including emergency path; trigger interface from leak detection (05.13) and pressure/temperature monitoring (05.11/05.12); feedback/verification interface to avionics and HMI; power interface including loss-of-power behaviour (TBD per REQ-HFPX-FIS-004); environmental interfaces per SYS-006. Details are TBD.

## 10. Operational Concept

Isolation is exercised through safety threads; each requirement maps to ≥1 nominal/off-nominal scenario (mapping TBD in V&V Plan). This document prescribes no actuation, maintenance, emergency-response, or operating instructions. Any live-fuel isolation actuation referenced for verification occurs only under controlled conditions with approved procedures and safety controls.

## 11. Safety

Failed, spurious, incomplete, or unverified isolation are hazards to be analysed in Vol 13 (FHA/FMEA/FTA); this chapter generates no standalone safety claim. REQ-HFPX-FIS-002/004 support the SYS-003 independent safety path; independence and arbitration are TBD via safety analysis. Fail-safe direction shall be determined by analysis, not assumed. Hazardous-subsystem boundary applies (see §2).

## 12. Performance

Intentionally TBD. Isolation time, leakage after isolation, operating envelope, and environmental derating are TBD pending architecture, valve trades, and safety analysis. No performance value in this document is approved.

## 13. Verification & Validation

Each requirement states its method above; verification IDs and cases are TBD in the V&V Plan (Vol 22). Strategy: analysis (fail-safe determination) → inspection (valve/function provision) → demonstration (authority including emergency) → test (verification of isolation state, controlled conditions). Requirements without a verification method are rejected at SRR. Procedures and pass/fail criteria are TBD (see HFPX-FUEL-TST-001).

## 14. Risks

- Valve locations and authority undefined before architecture exists → mitigation: explicit TBD, authority requirement retained
- Fail-safe direction assumed prematurely → mitigation: REQ-HFPX-FIS-004 explicitly TBD, analysis-gated
- Spurious vs failed isolation trade unresolved → mitigation: safety analysis and verification gate

## 15. Open Issues

- Valve/function locations, types, counts, timing (all TBD)
- Normal and emergency authority sources, arbitration, independence (TBD)
- Verification method/criteria; fail-safe direction determination (TBD, analysis-gated)

## 16. Assumptions

- A-TBD: Fuel isolation is required regardless of final fuel architecture; validation: SRR review
- No assumption is made about valve type, placement, timing, authority, verification method, or fail-safe direction in this revision

## 17. Dependencies

Depends on storage/distribution architecture (05.4/05.5), detection threads (05.11–05.13), command/HMI interfaces (Vol 02/07/12), safety analyses (Vol 13, SAF tier, SCA-006), and V&V/test planning (Vol 22/33). FRQ-tier approval gates requirement stability.

## 18. Traceability

Parents: FRQ tier (TBD), REQ-HFPX-SYS-003, REQ-HFPX-SYS-006, SAF tier (TBD), SCA-006 (table above). Children: SAD views, valve/actuator specifications (TBD), ICD rows (command, trigger, feedback), V&V cases, RTM rows. RTM seed for REQ-HFPX-FIS-001..004 is added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0. Tranche 4 draft, CONCEPT, not baselined. Valve selection, authority definition, or fail-safe determination requires a new revision via change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (Chapter 05.14; HFPX-FUEL-ISO-001) |
