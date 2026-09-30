# Leak Detection (Chapter 05.13)

**Document ID:** HFPX-FUEL-LEK-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Hold the fuel leak detection requirements for HFP-X in one chapter. This Tranche 4 draft establishes the requirement set structure, detection-to-annunciation-to-isolation-trigger thread, and test-verification provision; all quantitative values are TBD.

## 2. Scope

Covers Chapter 05.13 Leak Detection: detection coverage, annunciation, isolation-trigger interface, and verification approach for fuel leaks. Detection technology, thresholds, zones, isolation logic, and detailed design are TBD.

> **Hazardous-subsystem boundary.** Content in this document is limited to requirements, architecture, interfaces, test methodology and safety analysis. It shall not contain instructions for constructing, handling, repairing, or operating fuel or propulsion outside appropriate engineering, test, safety and regulatory controls. Any active fuel handling or leak-response activity occurs only under controlled conditions per Vol 13 / Vol 22 / Vol 33.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parents REQ-HFPX-SYS-003, REQ-HFPX-SYS-006)
- FRQ tier (functional requirements, TBD — parent tier)
- SAF tier (safety requirements, TBD) and SCA-006
- HFPX-SYS-ARC-001 SAD (allocation to fuel subsystem, TBD)
- HFPX-FUEL-ISO-001 Fuel Isolation (consumer of isolation trigger, Tranche 4 draft)
- Vol 02 ICDs (fuel ↔ avionics / isolation interfaces, TBD)
- Vol 13 Safety analyses; Vol 22 V&V Plan (not written); Vol 33 Test (controlled conditions)
- HFP prompt §§8–10, 14, 19, 32, 34

## 4. Definitions & Acronyms

- FLK: fuel leak detection thread; requirement IDs `REQ-HFPX-FLK-001..004`
- Detection coverage: zones and leak states within scope of detection (TBD)
- Annunciation: alert that a leak has been detected (threshold and semantics TBD)
- Isolation-trigger interface: boundary output that an isolation function may consume (logic TBD; isolation owned by HFPX-FUEL-ISO-001)
- TBD/TBC/A-XXX: unknown data handling; no invented values
- Verification: Analysis / Inspection / Demonstration / Test

## 5. System Context

Leak detection is a detection branch feeding awareness and isolation:

```text
FUEL ZONES (storage/distribution, TBD) → LEAK DETECTION (this chapter) → ANNUNCIATION → HMI / TELEMETRY
                                                                  ↓
                                              ISOLATION-TRIGGER INTERFACE → ISOLATION (05.14)
```

It detects and reports; isolation authority and action remain with HFPX-FUEL-ISO-001 and the safety path. Allocation to detectors, zones, and computing is TBD in the SAD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-FLK-001 | The fuel system shall provide leak detection coverage for zones and leak states to be determined (TBD). | FRQ tier (TBD), REQ-HFPX-SYS-003 | Test |
| REQ-HFPX-FLK-002 | The fuel system shall provide leak annunciation to the pilot/operator upon detection (threshold and semantics TBD). | REQ-HFPX-SYS-003, SAF tier (TBD) | Demonstration |
| REQ-HFPX-FLK-003 | The fuel system shall provide an isolation-trigger interface that exposes leak-detection status to the isolation function (logic and authority TBD). | REQ-HFPX-SYS-003, SCA-006 | Inspection |
| REQ-HFPX-FLK-004 | Fuel leak detection performance shall be verified by test under controlled conditions (procedures and pass/fail TBD). | SCA-006, REQ-HFPX-SYS-006 | Test |

No leak rate, concentration, threshold, coverage, latency, or pass/fail value in this document is approved; all are TBD.

## 7. Architecture

Logical allocation (starter — SAD owns authoritative allocation): detectors/sensing elements per zone (technology TBD) → detection logic / computation (TBD) → detection state → annunciation + isolation-trigger output. Redundancy, voting, built-in-test, nuisance-rejection, and power/data allocation are TBD. No detector type, count, or placement is baselined.

## 8. Detailed Design

Not applicable — requirements/architecture level only. No detailed design, part selection, schematic, software design, or installation drawing is contained or approved in this revision.

## 9. Interfaces

Interface placeholders (controlled via SAD §9 / Vol 02 ICDs, all TBD): mechanical/installation interface to fuel zones; electrical/data interface to avionics and computing; annunciation interface to HMI / ground station; isolation-trigger interface to HFPX-FUEL-ISO-001 (signals, timing, failure semantics TBD); environmental interfaces per SYS-006. Details are TBD.

## 10. Operational Concept

Detection information is consumed through awareness and safety threads; each requirement maps to ≥1 nominal/off-nominal scenario (mapping TBD in V&V Plan). This document prescribes no leak-response, repair, maintenance, or operating instructions. Any live-fuel detection test occurs only under controlled conditions with approved procedures, simulants where applicable (TBD), and safety controls.

## 11. Safety

Undetected leak, missed annunciation, false isolation trigger, and missed isolation trigger are hazards to be analysed in Vol 13 (FHA/FMEA/FTA); this chapter generates no standalone safety claim. REQ-HFPX-FLK-002/003 support the SYS-003 independent safety path as detection inputs. Hazardous-subsystem boundary applies (see §2).

## 12. Performance

Intentionally TBD. Detection sensitivity, coverage, response time, false-alarm rate, operating envelope, and environmental derating are TBD pending architecture, detector trades, and safety analysis. No performance value in this document is approved.

## 13. Verification & Validation

Each requirement states its method above; verification IDs and cases are TBD in the V&V Plan (Vol 22). Strategy: inspection (interface provision) → demonstration (annunciation) → test (detection coverage and performance, controlled conditions, unmanned first where applicable). Requirements without a verification method are rejected at SRR. Procedures, simulants, and pass/fail criteria are TBD (see HFPX-FUEL-TST-001).

## 14. Risks

- Coverage undefined before zone architecture exists → mitigation: explicit TBD, zone hook retained
- Nuisance alarms vs missed detection trade unresolved → mitigation: thresholds TBD via safety analysis and test
- Isolation-trigger mismatch with isolation consumer → mitigation: ICD coverage gate per review

## 15. Open Issues

- Detection zones, leak states, sensitivity, thresholds (all TBD)
- Detector technology, count, placement, redundancy, BIT (TBD)
- Isolation-trigger semantics, timing, authority; test simulants and pass/fail (TBD)

## 16. Assumptions

- A-TBD: Leak detection is required regardless of final fuel architecture and fuel selection; validation: SRR review
- No assumption is made about detector type, sensitivity, coverage, or isolation response in this revision

## 17. Dependencies

Depends on storage/distribution architecture (05.4/05.5), isolation definition (05.14), avionics/HMI interfaces (Vol 02/07/12), safety analyses (Vol 13, SAF tier, SCA-006), and V&V/test planning (Vol 22/33). FRQ-tier approval gates requirement stability.

## 18. Traceability

Parents: FRQ tier (TBD), REQ-HFPX-SYS-003, REQ-HFPX-SYS-006, SAF tier (TBD), SCA-006 (table above). Children: SAD views, detector specifications (TBD), ICD rows (including isolation trigger), V&V cases, RTM rows. RTM seed for REQ-HFPX-FLK-001..004 is added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0. Tranche 4 draft, CONCEPT, not baselined. Coverage definition, detector selection, or interface definition requires a new revision via change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (Chapter 05.13; HFPX-FUEL-LEK-001) |
