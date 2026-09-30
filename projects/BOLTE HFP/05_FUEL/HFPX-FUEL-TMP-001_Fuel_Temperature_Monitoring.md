# Fuel Temperature Monitoring (Chapter 05.12)

**Document ID:** HFPX-FUEL-TMP-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Hold the fuel temperature monitoring requirements for HFP-X in one chapter. This Tranche 4 draft establishes the requirement set structure, sensing-to-annunciation-to-protection thread, and thermal-limit hook to Vol 14.6; all quantitative values are TBD.

## 2. Scope

Covers Chapter 05.12 Fuel Temperature Monitoring: temperature sensing, thermal-limit annunciation, and protection interface for the fuel system. Temperature limits, sensor selection, protection logic, and detailed design are TBD; thermal limits proper live in Vol 14.6.

> **Hazardous-subsystem boundary.** Content in this document is limited to requirements, architecture, interfaces, test methodology and safety analysis. It shall not contain instructions for constructing, handling, heating/cooling, or operating fuel or propulsion outside appropriate engineering, test, safety and regulatory controls. Any active fuel handling occurs only under controlled conditions per Vol 13 / Vol 22 / Vol 33.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parents REQ-HFPX-SYS-003, REQ-HFPX-SYS-006)
- FRQ tier (functional requirements, TBD — parent tier)
- SAF tier (safety requirements, TBD) and SCA-006
- Vol 14.6 Thermal limits (owner of thermal-limit values, TBD)
- HFPX-SYS-ARC-001 SAD (allocation to fuel subsystem, TBD)
- Vol 02 ICDs (fuel ↔ avionics / thermal / protection interfaces, TBD)
- Vol 13 Safety analyses; Vol 22 V&V Plan (not written); Vol 33 Test (controlled conditions)
- HFP prompt §§8–10, 14, 19, 32, 34

## 4. Definitions & Acronyms

- FTP: fuel temperature monitoring thread; requirement IDs `REQ-HFPX-FTP-001..003`
- Temperature sensing: measurement of fuel temperature at defined points (locations TBD)
- Thermal-limit annunciation: alert on breach of Vol 14.6 thermal limits (values TBD)
- Protection interface: boundary to a protection function that consumes temperature data (logic TBD)
- TBD/TBC/A-XXX: unknown data handling; no invented values
- Verification: Analysis / Inspection / Demonstration / Test

## 5. System Context

Fuel temperature monitoring is a sensing-and-interface branch of the fuel and thermal systems:

```text
FUEL STORAGE/DISTRIBUTION → TEMPERATURE SENSING (this chapter) → ANNUNCIATION → HMI / TELEMETRY
                                                     ↓
                                          PROTECTION INTERFACE → PROTECTION FUNCTION (TBD)
THERMAL LIMITS (Vol 14.6, TBD) → threshold source
```

It provides awareness and a detection input to protection; limit values are owned by Vol 14.6. Allocation to sensors and computing is TBD in the SAD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-FTP-001 | The fuel system shall sense fuel temperature at points to be determined (TBD) with an accuracy to be determined (TBD). | FRQ tier (TBD), REQ-HFPX-SYS-006 | Test |
| REQ-HFPX-FTP-002 | The fuel system shall provide thermal-limit annunciation when fuel temperature breaches limits defined in Vol 14.6 (values TBD). | REQ-HFPX-SYS-003, SAF tier (TBD) | Demonstration |
| REQ-HFPX-FTP-003 | The fuel system shall provide a protection interface that exposes fuel-temperature status to the protection function (logic and response TBD). | REQ-HFPX-SYS-003, SCA-006 | Inspection |

No temperature value, limit, accuracy, latency, or protection setpoint in this document is approved; all are TBD and limits are owned by Vol 14.6.

## 7. Architecture

Logical allocation (starter — SAD owns authoritative allocation): temperature sensing elements (TBD) → signal conditioning / computation (TBD) → temperature estimate → annunciation logic (thresholds from Vol 14.6) + protection-interface output. Redundancy, voting, sensor diagnostics, and power/data allocation are TBD. No sensor type, count, or placement is baselined.

## 8. Detailed Design

Not applicable — requirements/architecture level only. No detailed design, part selection, schematic, software design, or installation drawing is contained or approved in this revision.

## 9. Interfaces

Interface placeholders (controlled via SAD §9 / Vol 02 ICDs, all TBD): fluid/mechanical interface to storage and distribution (05.4/05.5); electrical/data interface to avionics and computing; threshold interface to Vol 14.6 thermal limits; annunciation interface to HMI / ground station; protection interface (signals, timing, failure semantics TBD); environmental interfaces per SYS-006. Details are TBD.

## 10. Operational Concept

Temperature information is consumed through awareness and protection threads; each requirement maps to ≥1 nominal/off-nominal scenario (mapping TBD in V&V Plan). This document prescribes no thermal conditioning, maintenance, or operating instructions. Any live-fuel activity referenced for verification occurs only under controlled conditions with approved procedures and safety controls.

## 11. Safety

Temperature-sensing loss, mis-indication, and missed thermal-limit breach are hazards to be analysed in Vol 13 (FHA/FMEA); this chapter generates no standalone safety claim. REQ-HFPX-FTP-002/003 support the SYS-003 independent safety path as detection inputs; protection authority remains with the protection function. Hazardous-subsystem boundary applies (see §2).

## 12. Performance

Intentionally TBD. Temperature range, accuracy, update rate, latency, operating envelope, and environmental derating are TBD pending budgets, models, Vol 14.6 limits, and sensor trades. No performance value in this document is approved.

## 13. Verification & Validation

Each requirement states its method above; verification IDs and cases are TBD in the V&V Plan (Vol 22). Strategy: inspection (interface provision, Vol 14.6 trace) → demonstration (annunciation) → test (sensing accuracy, controlled conditions). Requirements without a verification method are rejected at SRR. Test procedures and pass/fail criteria are TBD (see HFPX-FUEL-TST-001).

## 14. Risks

- Sensing points and ranges undefined before storage/distribution and thermal design exist → mitigation: explicit TBD, Vol 14.6 hook retained
- Nuisance or missed thermal-limit alerts → mitigation: limits/hysteresis TBD via Vol 14.6 and safety analysis
- Protection-interface mismatch with consumer function → mitigation: ICD coverage gate per review

## 15. Open Issues

- Sensing locations, ranges, accuracies, latencies (all TBD)
- Vol 14.6 thermal-limit values, hysteresis, annunciation semantics (TBD)
- Protection-interface signals, timing, failure semantics, consumer authority (TBD)

## 16. Assumptions

- A-TBD: Fuel-temperature monitoring is required regardless of final fuel and thermal architecture; validation: SRR review
- No assumption is made about sensor type, range, limits, or protection response in this revision; limits are owned by Vol 14.6

## 17. Dependencies

Depends on storage/distribution architecture (05.4/05.5), Vol 14.6 thermal limits, protection-function definition (TBD, SAF tier), avionics/HMI interfaces (Vol 02/07/12), safety analyses (Vol 13, SCA-006), and V&V/test planning (Vol 22/33). FRQ-tier approval gates requirement stability.

## 18. Traceability

Parents: FRQ tier (TBD), REQ-HFPX-SYS-003, REQ-HFPX-SYS-006, SAF tier (TBD), SCA-006, Vol 14.6 limits (table above). Children: SAD views, temperature-sensor specifications (TBD), ICD rows, V&V cases, RTM rows. RTM seed for REQ-HFPX-FTP-001..003 is added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0. Tranche 4 draft, CONCEPT, not baselined. Quantification, sensor selection, or interface definition requires a new revision via change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (Chapter 05.12; HFPX-FUEL-TMP-001) |
