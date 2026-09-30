# Fuel Pressure Monitoring (Chapter 05.11)

**Document ID:** HFPX-FUEL-PRS-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Hold the fuel pressure monitoring requirements for HFP-X in one chapter. This Tranche 4 draft establishes the requirement set structure, sensing-to-annunciation-to-protection thread; all quantitative values are TBD.

## 2. Scope

Covers Chapter 05.11 Fuel Pressure Monitoring: pressure sensing, exceedance annunciation, and protection interface for the fuel system. Pressure limits, sensor selection, protection logic, and detailed design are TBD.

> **Hazardous-subsystem boundary.** Content in this document is limited to requirements, architecture, interfaces, test methodology and safety analysis. It shall not contain instructions for constructing, handling, pressurising, or operating fuel or propulsion outside appropriate engineering, test, safety and regulatory controls. Any active fuel handling occurs only under controlled conditions per Vol 13 / Vol 22 / Vol 33.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parents REQ-HFPX-SYS-003, REQ-HFPX-SYS-006)
- FRQ tier (functional requirements, TBD — parent tier)
- SAF tier (safety requirements, TBD) and SCA-006
- HFPX-SYS-ARC-001 SAD (allocation to fuel subsystem, TBD)
- Vol 02 ICDs (fuel ↔ avionics / protection interfaces, TBD)
- Vol 13 Safety analyses; Vol 22 V&V Plan (not written); Vol 33 Test (controlled conditions)
- HFP prompt §§8–10, 14, 19, 32, 34

## 4. Definitions & Acronyms

- FPS: fuel pressure sensing thread; requirement IDs `REQ-HFPX-FPS-001..003`
- Pressure sensing: measurement of fuel pressure at defined points (locations TBD)
- Exceedance annunciation: alert on pressure outside defined bounds (limits TBD)
- Protection interface: boundary to a protection function that consumes pressure data (logic TBD)
- TBD/TBC/A-XXX: unknown data handling; no invented values
- Verification: Analysis / Inspection / Demonstration / Test

## 5. System Context

Fuel pressure monitoring is a sensing-and-interface branch of the fuel system:

```text
FUEL DISTRIBUTION → PRESSURE SENSING (this chapter) → ANNUNCIATION → HMI / TELEMETRY
                                              ↓
                                   PROTECTION INTERFACE → PROTECTION FUNCTION (TBD)
```

It provides awareness and a detection input to protection; it does not itself relieve pressure or command isolation. Allocation to sensors, manifolds, and computing is TBD in the SAD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-FPS-001 | The fuel system shall sense fuel pressure at points to be determined (TBD) with an accuracy to be determined (TBD). | FRQ tier (TBD), REQ-HFPX-SYS-006 | Test |
| REQ-HFPX-FPS-002 | The fuel system shall provide fuel-pressure exceedance annunciation when pressure exceeds bounds to be determined (TBD). | REQ-HFPX-SYS-003, SAF tier (TBD) | Demonstration |
| REQ-HFPX-FPS-003 | The fuel system shall provide a protection interface that exposes fuel-pressure status to the protection function (logic and response TBD). | REQ-HFPX-SYS-003, SCA-006 | Inspection |

No pressure value, limit, accuracy, latency, or protection setpoint in this document is approved; all are TBD.

## 7. Architecture

Logical allocation (starter — SAD owns authoritative allocation): pressure sensing elements (TBD) → signal conditioning / computation (TBD) → pressure estimate → annunciation logic + protection-interface output. Redundancy, voting, sensor diagnostics, and power/data allocation are TBD. No sensor type, count, or placement is baselined.

## 8. Detailed Design

Not applicable — requirements/architecture level only. No detailed design, part selection, schematic, software design, or installation drawing is contained or approved in this revision.

## 9. Interfaces

Interface placeholders (controlled via SAD §9 / Vol 02 ICDs, all TBD): fluid/mechanical interface to distribution and metering (05.5/05.8); electrical/data interface to avionics and computing; annunciation interface to HMI / ground station; protection interface (signals, timing, failure semantics TBD); environmental interfaces per SYS-006. Details are TBD.

## 10. Operational Concept

Pressure information is consumed through awareness and protection threads; each requirement maps to ≥1 nominal/off-nominal scenario (mapping TBD in V&V Plan). This document prescribes no pressurisation, venting, maintenance, or operating instructions. Any live-fuel activity referenced for verification occurs only under controlled conditions with approved procedures and safety controls.

## 11. Safety

Pressure-sensing loss, mis-indication, and missed exceedance are hazards to be analysed in Vol 13 (FHA/FMEA); this chapter generates no standalone safety claim. REQ-HFPX-FPS-002/003 support the SYS-003 independent safety path as detection inputs; protection authority remains with the protection function. Hazardous-subsystem boundary applies (see §2).

## 12. Performance

Intentionally TBD. Pressure range, accuracy, update rate, latency, operating envelope, and environmental derating are TBD pending budgets, models, and sensor trades. No performance value in this document is approved.

## 13. Verification & Validation

Each requirement states its method above; verification IDs and cases are TBD in the V&V Plan (Vol 22). Strategy: inspection (interface provision) → demonstration (annunciation) → test (sensing accuracy, unmanned first, controlled conditions). Requirements without a verification method are rejected at SRR. Test procedures and pass/fail criteria are TBD (see HFPX-FUEL-TST-001).

## 14. Risks

- Sensing points and ranges undefined before distribution design exists → mitigation: explicit TBD, interface requirement retained
- Nuisance or missed exceedance alerts → mitigation: bounds/hysteresis TBD via safety analysis
- Protection-interface mismatch with consumer function → mitigation: ICD coverage gate per review

## 15. Open Issues

- Sensing locations, ranges, accuracies, latencies (all TBD)
- Exceedance bounds, hysteresis, annunciation semantics (TBD)
- Protection-interface signals, timing, failure semantics, consumer authority (TBD)

## 16. Assumptions

- A-TBD: Fuel-pressure monitoring is required regardless of final pump/distribution architecture; validation: SRR review
- No assumption is made about sensor type, range, limits, or protection response in this revision

## 17. Dependencies

Depends on distribution/metering architecture (05.5/05.8), protection-function definition (TBD, SAF tier), avionics/HMI interfaces (Vol 02/07/12), safety analyses (Vol 13, SCA-006), and V&V/test planning (Vol 22/33). FRQ-tier approval gates requirement stability.

## 18. Traceability

Parents: FRQ tier (TBD), REQ-HFPX-SYS-003, REQ-HFPX-SYS-006, SAF tier (TBD), SCA-006 (table above). Children: SAD views, pressure-sensor specifications (TBD), ICD rows, V&V cases, RTM rows. RTM seed for REQ-HFPX-FPS-001..003 is added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0. Tranche 4 draft, CONCEPT, not baselined. Quantification, sensor selection, or interface definition requires a new revision via change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (Chapter 05.11; HFPX-FUEL-PRS-001) |
