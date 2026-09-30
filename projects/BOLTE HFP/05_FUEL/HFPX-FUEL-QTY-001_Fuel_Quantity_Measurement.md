# Fuel Quantity Measurement (Chapter 05.10)

**Document ID:** HFPX-FUEL-QTY-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Hold the fuel quantity measurement requirements for HFP-X in one chapter. This Tranche 4 draft establishes the requirement set structure, sensing-to-annunciation thread, and calibration-hook provision; all quantitative values are TBD. Backbone-adjacent supporting document for Volume 05.

## 2. Scope

Covers Chapter 05.10 Fuel Quantity Measurement: quantity sensing, low-quantity annunciation, and calibration provisions for the fuel system. Quantitative accuracy, thresholds, sensor selection, and detailed design are TBD.

> **Hazardous-subsystem boundary.** Content in this document is limited to requirements, architecture, interfaces, test methodology and safety analysis. It shall not contain instructions for constructing, handling, or operating fuel or propulsion outside appropriate engineering, test, safety and regulatory controls. Any active fuel handling occurs only under controlled conditions per Vol 13 / Vol 22 / Vol 33.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parents REQ-HFPX-SYS-003, REQ-HFPX-SYS-006)
- FRQ tier (functional requirements, TBD — parent tier)
- SAF tier (safety requirements, TBD) and SCA-006
- HFPX-SYS-ARC-001 SAD (allocation to fuel subsystem, TBD)
- Vol 02 ICDs (fuel ↔ avionics / FCS / HMI interfaces, TBD)
- Vol 13 Safety analyses; Vol 22 V&V Plan (not written); Vol 33 Test (controlled conditions)
- HFP prompt §§8–10, 14, 19, 32, 34

## 4. Definitions & Acronyms

- FQT: fuel quantity thread; requirement IDs `REQ-HFPX-FQT-001..003`
- Quantity sensing: measurement of fuel quantity remaining (method TBD)
- Low-quantity annunciation: crew/operator alert that quantity has fallen to a defined state (threshold TBD)
- Calibration hooks: provision for calibration without prescribing procedure
- TBD/TBC/A-XXX: unknown data handling; no invented values
- Verification: Analysis / Inspection / Demonstration / Test

## 5. System Context

Fuel quantity measurement is a sensing branch of the fuel system:

```text
FUEL STORAGE → QUANTITY SENSING (this chapter) → AVIONICS/FCS → HMI / GROUND STATION
                          ↓
              LOW-QUANTITY ANNUNCIATION → SAFETY PATH (SYS-003)
```

It informs operational awareness and the independent safety path; it does not command fuel flow. Allocation to physical sensors, tanks, and computing is TBD in the SAD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-FQT-001 | The fuel system shall measure fuel quantity remaining with an accuracy to be determined (TBD). | FRQ tier (TBD), REQ-HFPX-SYS-006 | Test |
| REQ-HFPX-FQT-002 | The fuel system shall provide low-quantity annunciation to the pilot/operator when fuel quantity reaches a threshold to be determined (TBD). | REQ-HFPX-SYS-003, SAF tier (TBD) | Demonstration |
| REQ-HFPX-FQT-003 | The fuel system shall provide calibration hooks for fuel quantity measurement (method and interval TBD). | FRQ tier (TBD), SCA-006 | Inspection |

No quantitative accuracy, threshold, hysteresis, latency, or calibration value in this document is approved; all are TBD.

## 7. Architecture

Logical allocation (starter — SAD owns authoritative allocation): sensing elements (TBD, in tanks) → signal conditioning / computation (TBD) → quantity estimate → annunciation logic → HMI / telemetry. Redundancy, voting, failure annunciation, and power/data allocation are TBD. No sensor type, count, or placement is baselined.

## 8. Detailed Design

Not applicable — requirements/architecture level only. No detailed design, part selection, schematic, software design, or installation drawing is contained or approved in this revision.

## 9. Interfaces

Interface placeholders (controlled via SAD §9 / Vol 02 ICDs, all TBD): mechanical/fluid interface to fuel storage (05.4); electrical/data interface to avionics and computing; annunciation interface to HMI / helmet / ground station; calibration interface (connector/protocol TBD); environmental interfaces per SYS-006. Interface details, pin-outs, and protocols are TBD.

## 10. Operational Concept

Quantity information is consumed through operational awareness threads; each requirement maps to ≥1 nominal/off-nominal scenario (mapping TBD in V&V Plan). This document prescribes no fuel-handling, servicing, or operating instructions. Any live-fuel activity referenced for verification occurs only under controlled conditions with approved procedures, range, and safety controls.

## 11. Safety

Quantity mis-indication and loss of annunciation are hazards to be analysed in Vol 13 (FHA/FMEA); this chapter generates no standalone safety claim. REQ-HFPX-FQT-002 supports the SYS-003 independent safety path as a detection input; authority and response remain with the safety path. Hazardous-subsystem boundary applies (see §2).

## 12. Performance

Intentionally TBD. Quantity accuracy, update rate, latency, operating envelope, and environmental derating are TBD pending budgets, models, and sensor trades. No performance value in this document is approved.

## 13. Verification & Validation

Each requirement states its method above; verification IDs and cases are TBD in the V&V Plan (Vol 22). Strategy: analysis/inspection (design, calibration-hook provision) → demonstration (annunciation) → test (accuracy, unmanned first, controlled conditions). Requirements without a verification method are rejected at SRR. Test procedures and pass/fail criteria are TBD (see HFPX-FUEL-TST-001).

## 14. Risks

- Sensing accuracy unproven before sensor trade and tank geometry exist → mitigation: explicit TBD, calibration-hook requirement retained
- Nuisance or missed low-quantity alerts → mitigation: threshold/hysteresis TBD via safety analysis, demonstration required
- Orphaned interfaces as Vol 03–18 grow → mitigation: ICD coverage gate per review

## 15. Open Issues

- Threshold, accuracy, hysteresis, latency values (all TBD)
- Sensor technology, count, placement, redundancy (TBD)
- Calibration method/interval and in-service verification (TBD)

## 16. Assumptions

- A-TBD: A quantity-sensing provision is required regardless of final fuel selection; validation: SRR review
- No assumption is made about sensor type, accuracy, or threshold in this revision

## 17. Dependencies

Depends on fuel storage architecture (05.4), avionics/HMI interfaces (Vol 02/07/12), safety analyses (Vol 13, SAF tier, SCA-006), and V&V/test planning (Vol 22/33). FRQ-tier approval gates requirement stability.

## 18. Traceability

Parents: FRQ tier (TBD), REQ-HFPX-SYS-003, REQ-HFPX-SYS-006, SAF tier (TBD), SCA-006 (table above). Children: SAD views, quantity-sensor specifications (TBD), ICD rows, V&V cases, RTM rows. RTM seed for REQ-HFPX-FQT-001..003 is added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0. Tranche 4 draft, CONCEPT, not baselined. Quantification or sensor selection requires a new revision via change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (Chapter 05.10; HFPX-FUEL-QTY-001) |
