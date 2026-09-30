# 09.10 Temperature Sensors

**Document ID:** HFPX-NAV-TMP-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the structure and subsystem requirements for temperature sensing within Volume 09 Navigation, Sensors and Instrumentation, Chapter 09.10. This revision establishes requirement placeholders only; all quantitative values are TBD. No design approval or part selection is implied.

## 2. Scope

Covers temperature sensing functions that support navigation, propulsion, fuel, and avionics compensation and monitoring. Includes sensed locations, accuracy, compensation use, and verification structure.

Out of scope: selection of sensor parts or suppliers; detailed circuit design; software implementation; environmental qualification. No parts are selected at this revision.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parents REQ-HFPX-SYS-004 and related functional tier, including FUN-003 where applicable)
- HFPX-NAV-IDX-001 Volume 09 index / README (Chapter 09.10)
- Volume 04 propulsion monitoring references (for propulsion temperature interfaces, details TBD)
- Volume 05 fuel system references (for fuel temperature interfaces, details TBD)
- Volume 08 avionics references (for avionics temperature interfaces, details TBD)
- HFPX-VV-PLN-001 V&V Plan (not written, verification cases TBD)
- Safety analyses references Vol 13 (SFA/CCA/FTA hooks, details TBD)

## 4. Definitions & Acronyms

_TBD_

- TMP: Temperature Sensors chapter (09.10)
- NTS: temperature sensor requirement prefix (REQ-HFPX-NTS)
- TBD: to be determined; TBC: to be confirmed
- Verification methods: Analysis / Inspection / Demonstration / Test (allocation per requirement TBD)

## 5. System Context

Temperature sensing supports REQ-HFPX-SYS-004 navigation and related system functions by providing thermal measurements used for compensation and health awareness across air, propulsion, fuel, and avionics domains.

Context TBD. Allocation to SYS-07/08 sensor functions TBD. Relationship to functional tier FUN-003 TBD. All interfaces and envelopes TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-NTS-001|The temperature sensing function shall sense temperature at locations TBD, including air, propulsion, fuel, and avionics locations TBD.|REQ-HFPX-SYS-004, FUN-003|Inspection|
|REQ-HFPX-NTS-002|The temperature sensing function shall meet measurement accuracy requirements TBD.|REQ-HFPX-SYS-004, FUN-003|Test|
|REQ-HFPX-NTS-003|The temperature sensing function shall provide measurements for compensation use TBD.|REQ-HFPX-SYS-004, FUN-003|Inspection|
|REQ-HFPX-NTS-004|The temperature sensing function shall be verified by means TBD.|REQ-HFPX-SYS-004, FUN-003|Inspection|

No quantitative values are stated. All thresholds, ranges, accuracies, and test conditions are TBD.

## 7. Architecture

_TBD_

Sensor architecture, channel allocation, and processing location are TBD. Relationship to Volume 09 sensor architecture (09.1) TBD. Structure only at this revision.

## 8. Detailed Design

_TBD_

No detailed design is defined. No sensor technology, range, package, or supplier is selected. No parts are selected at this revision.

## 9. Interfaces

_TBD_

Interfaces to air data, propulsion, fuel, avionics, and data acquisition functions TBD. Connector, signal, and protocol details TBD.

## 10. Operational Concept

_TBD_

Use of temperature measurements across flight phases and ground operations TBD, including compensation application TBD.

## 11. Safety

_TBD_

Safety relevance of temperature sensing TBD. Hooks to SFA/CCA and FTA/FMEA as applicable TBD. No safety claim is made at this revision.

## 12. Performance

_TBD_

All performance values including accuracy, response, and operating envelope TBD. No value in this document is approved.

## 13. Verification & Validation

_TBD_

Verification means for REQ-HFPX-NTS-001..004 TBD. V&V cases, facilities, and acceptance criteria TBD in the V&V Plan.

## 14. Risks

- TBD density high: locations, accuracy, and compensation use undefined; mitigation: structure placeholders established, detailed definition in later revisions
- Interface mismatch with propulsion/fuel/avionics consumers; mitigation: ICD hooks TBD

## 15. Open Issues

- Sensed location list TBD (air/propulsion/fuel/avionics)
- Accuracy requirements TBD
- Compensation use definition TBD
- Verification means TBD

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on: functional tier FUN-003 stability; Volume 04/05/08 interface definitions; sensor architecture 09.1; V&V Plan cases; safety analyses Vol 13 outputs.

## 18. Traceability

Parents: REQ-HFPX-SYS-004, FUN-003. Children: TBD (design, ICDs, V&V cases, RTM rows). RTM seed for REQ-HFPX-NTS-001..004 is added with this tranche (Status CONCEPT). Hooks to SFA/CCA where safety relevance is determined TBD.

## 19. Configuration

BL-0.0. Tranche 5 draft, CONCEPT, not baselined. Changes require change control in later revisions.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 draft (Chapter 09.10) |
