# Fuel System Safety (Chapter 05.15)

**Document ID:** HFPX-FUEL-SAF-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Hold the fuel system safety requirements for HFP-X in one chapter. This Tranche 4 draft establishes the requirement set structure: hazard-analysis obligation, fire-zone and crash-safety interfaces, maintenance-safety hooks, and the fuel-safety verification thread; all quantitative values are TBD. Feeds Vol 13.

## 2. Scope

Covers Chapter 05.15 Fuel System Safety: fuel hazard analysis requirement, fire-zone interfaces, crash-safety principles, maintenance-safety hooks, and safety verification. Analyses, zones, criteria, and detailed design are TBD.

> **Hazardous-subsystem boundary.** Content in this document is limited to requirements, architecture, interfaces, test methodology and safety analysis. It shall not contain instructions for constructing, handling, repairing, or operating fuel or propulsion outside appropriate engineering, test, safety and regulatory controls. Any active fuel handling occurs only under controlled conditions per Vol 13 / Vol 22 / Vol 33.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parents REQ-HFPX-SYS-003, REQ-HFPX-SYS-006)
- FRQ tier (functional requirements, TBD — parent tier)
- SAF tier (safety requirements, TBD) and SCA-006
- Vol 13 Safety analyses and Safety Case (feeds; analyses TBD)
- HFPX-SYS-ARC-001 SAD (allocation to fuel subsystem, TBD)
- Vol 02 ICDs; Vol 14 Thermal/fire-zone inputs (TBD); Vol 21 Maintenance inputs (TBD)
- Vol 22 V&V Plan (not written); Vol 33 Test (controlled conditions)
- HFP prompt §§8–10, 14, 19, 32, 34

## 4. Definitions & Acronyms

- FSF: fuel system safety thread; requirement IDs `REQ-HFPX-FSF-001..005`
- Fuel hazard analysis: systematic identification/evaluation of fuel hazards feeding Vol 13 (method TBD)
- Fire-zone interfaces: boundaries to fire detection/protection zones (TBD)
- Crash-safety principles: requirements-level principles for crash-related fuel safety (criteria TBD)
- Maintenance-safety hooks: provision for safe maintenance without prescribing tasks
- TBD/TBC/A-XXX: unknown data handling; no invented values
- Verification: Analysis / Inspection / Demonstration / Test

## 5. System Context

Fuel system safety is the integrating safety thread for Volume 05:

```text
FUEL ARCHITECTURE (05.3–05.14) → HAZARD ANALYSIS (this chapter, feeds Vol 13) → SAF REQUIREMENTS → DESIGN / TEST
        ↓                                      ↓
FIRE-ZONE INTERFACES ←→ CRASH-SAFETY PRINCIPLES ←→ MAINTENANCE-SAFETY HOOKS
```

This chapter states safety requirements and hooks; analyses and approvals live in Vol 13. Allocation to zones, structures, and functions is TBD in the SAD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-FSF-001 | The programme shall perform a fuel hazard analysis covering the fuel system, feeding Vol 13 (scope and method TBD). | SAF tier (TBD), SCA-006 | Inspection |
| REQ-HFPX-FSF-002 | The fuel system shall define fire-zone interfaces to fire detection and protection functions (zones and signals TBD). | REQ-HFPX-SYS-003, SAF tier (TBD) | Inspection |
| REQ-HFPX-FSF-003 | The fuel system shall implement crash-safety principles for fuel containment and isolation (criteria TBD). | REQ-HFPX-SYS-003, SAF tier (TBD) | Analysis |
| REQ-HFPX-FSF-004 | The fuel system shall provide maintenance-safety hooks enabling safe maintenance (tasks and procedures TBD, controlled conditions). | FRQ tier (TBD), SCA-006 | Inspection |
| REQ-HFPX-FSF-005 | Fuel system safety requirements shall be verified through a defined fuel-safety verification thread (cases and evidence TBD). | SCA-006, REQ-HFPX-SYS-006 | Analysis |

No hazard list, zone definition, criterion, or evidence item in this document is approved; all are TBD.

## 7. Architecture

Logical allocation (starter — SAD owns authoritative allocation): fuel architecture views → hazard-analysis scope → derived safety requirements → fire-zone boundary outputs, crash-safety principle allocation (structure/isolation), maintenance-hook provision → verification thread. Zoning, segregation, redundancy, and independence are TBD. No zone, material, or structural solution is baselined.

## 8. Detailed Design

Not applicable — requirements/architecture level only. No detailed design, material selection, structural design, procedure, or installation drawing is contained or approved in this revision.

## 9. Interfaces

Interface placeholders (controlled via SAD §9 / Vol 02 ICDs, all TBD): analysis interface to Vol 13 (inputs/outputs, evidence); fire-zone interfaces to detection/protection functions (signals, timing TBD); structural/crash interface to airframe (Vol 03, criteria TBD); maintenance interface to Vol 21 (hooks, access TBD); verification interface to Vol 22 (cases TBD); environmental interfaces per SYS-006. Details are TBD.

## 10. Operational Concept

Safety requirements are exercised through hazard-driven scenarios; each requirement maps to ≥1 nominal/off-nominal scenario (mapping TBD in V&V Plan / Vol 13). This document prescribes no handling, maintenance-task, emergency-response, or operating instructions. Any live-fuel activity referenced for verification occurs only under controlled conditions with approved procedures and safety controls.

## 11. Safety

This chapter is the fuel contribution to system safety: REQ-HFPX-FSF-001 generates the analysis obligation; REQ-HFPX-FSF-002..004 state interface/principle/hook obligations; REQ-HFPX-FSF-005 closes the verification thread. No safety claim is approved in this revision; claims await Vol 13 analyses (FHA/FMEA/FTA) and Safety Case evidence. Hazardous-subsystem boundary applies (see §2).

## 12. Performance

Intentionally TBD. Safety targets, integrity levels, zone criteria, crash loads, and envelope values are TBD pending Vol 13 and system safety targets. No performance or target value in this document is approved.

## 13. Verification & Validation

Each requirement states its method above; verification IDs and cases are TBD in the V&V Plan (Vol 22) and Vol 13. Strategy: inspection (analysis completion, interface/hook provision) → analysis (crash-safety principles, verification-thread closure). Requirements without a verification method are rejected at SRR. Evidence items and acceptance criteria are TBD.

## 14. Risks

- Hazard analysis scope incomplete before architecture stabilises → mitigation: explicit TBD scope, Vol 13 feed retained
- Fire-zone and crash interfaces defined late → mitigation: interface requirements retained as placeholders, ICD gate per review
- Maintenance hooks missed → mitigation: hook requirement retained, Vol 21 coordination

## 15. Open Issues

- Hazard-analysis scope, method, schedule (all TBD)
- Fire zones, signals, consumer functions (TBD)
- Crash-safety criteria and allocation; maintenance-hook details; verification-thread cases (TBD)

## 16. Assumptions

- A-TBD: Fuel system safety requires dedicated hazard analysis feeding Vol 13 regardless of final architecture; validation: SRR review
- No assumption is made about hazards, zones, criteria, targets, or evidence in this revision

## 17. Dependencies

Depends on full fuel architecture (05.3–05.14, 05.16–05.17), Vol 13 analyses and Safety Case (SAF tier, SCA-006), structural/thermal inputs (Vol 03/14), maintenance inputs (Vol 21), and V&V planning (Vol 22). FRQ-tier approval gates requirement stability.

## 18. Traceability

Parents: FRQ tier (TBD), REQ-HFPX-SYS-003, REQ-HFPX-SYS-006, SAF tier (TBD), SCA-006 (table above). Children: Vol 13 analyses, SAD views, ICD rows, V&V cases, RTM rows. RTM seed for REQ-HFPX-FSF-001..005 is added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0. Tranche 4 draft, CONCEPT, not baselined. Analysis completion, interface definition, or criterion approval requires a new revision via change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (Chapter 05.15; HFPX-FUEL-SAF-001) |
