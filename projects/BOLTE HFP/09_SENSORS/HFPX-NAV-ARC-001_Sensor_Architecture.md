# 09.1 Sensor Architecture

**Document ID:** HFPX-NAV-ARC-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the structure for the HFP-X sensor architecture (Volume 09, Chapter 09.1). This revision establishes section structure and the initial requirement set only; all design detail is TBD.

## 2. Scope

Covers the sensor complement structure, primary/backup allocation structure, interface-class structure, and installation-constraint structure for navigation and flight sensing. Detailed sensor chapters are 09.2–09.9 and follow in this tranche; Chapters 09.10–09.17 are out of scope for this document.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parent SYS-004)
- HFPX functional requirements FUN-003 (parent)
- HFPX SAD DAT/LOG views (parent allocation views)
- Vol 08.8 (avionics interface classes)
- Vol 21.7 (installation constraints)
- _templates/DOCUMENT_TEMPLATE.md (structure)

## 4. Definitions & Acronyms

- NAV: navigation/sensors domain; NSA: sensor architecture requirement prefix
- TBD: to be determined; no values are approved at this revision
- Primary/backup: allocation roles to be defined; no redundancy values are stated herein
- Verification methods: Review / Inspection / Analysis / Demonstration / Test (allocated per requirement)

## 5. System Context

This document supports REQ-HFPX-SYS-004 (navigation sufficient for controlled flight) by structuring the sensor complement that feeds flight control, navigation, and safety functions. It is a parent-structure document for Chapters 09.2–09.9.

```text
SYS-004 → HFPX-NAV-ARC-001 → IMU / Gyro / Accel / Mag / GNSS / Baro / Airspeed / Altitude Sensing
```

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-NSA-001|The sensor architecture shall define the sensor complement, enumerating sensor classes with specific implementations TBD and no parts selected.|REQ-HFPX-SYS-004, REQ-HFPX-FUN-003, SAD DAT/LOG|Inspection|
|REQ-HFPX-NSA-002|The sensor architecture shall define primary/backup allocation for navigation sensors, with allocation TBD.|REQ-HFPX-SYS-004, REQ-HFPX-FUN-003, SAD DAT/LOG|Inspection|
|REQ-HFPX-NSA-003|The sensor architecture shall define sensor interface classes consistent with Vol 08.8, with details TBD.|REQ-HFPX-SYS-004, REQ-HFPX-FUN-003, SAD DAT/LOG|Inspection|
|REQ-HFPX-NSA-004|The sensor architecture shall comply with installation constraints per Vol 21.7, with constraints TBD.|REQ-HFPX-SYS-004, REQ-HFPX-FUN-003, SAD DAT/LOG|Inspection|
|REQ-HFPX-NSA-005|The sensor architecture shall be verified by review, with review artefacts TBD.|REQ-HFPX-SYS-004, REQ-HFPX-FUN-003, SAD DAT/LOG|Inspection|

No accuracies, ranges, rates, or biases are stated in this revision. No parts are selected at this revision.

## 7. Architecture

_TBD_

Structure placeholder: sensor classes (inertial, magnetic, GNSS, barometric, air data, altitude sensing) enumerate the complement; roles and redundancy topology TBD; allocation to DAT/LOG views TBD.

## 8. Detailed Design

_TBD_

Not applicable at this revision — structure only. Detailed design is deferred to Chapters 09.2–09.9 and later revisions.

## 9. Interfaces

_TBD_

Interface classes TBD, consistent with Vol 08.8. Signal, power, and data interface details TBD. No interface values are approved at this revision.

## 10. Operational Concept

_TBD_

Operational use of the sensor complement (nominal and degraded modes) TBD. Handover and degraded-mode behaviour TBD in child chapters.

## 11. Safety

_TBD_

Safety relevance of sensor loss or degradation TBD. Safety requirements and hazard mitigations TBD (Vol 13 analyses to feed later revisions).

## 12. Performance

_TBD_

All performance values TBD. No accuracy, range, rate, bias, or availability figure is stated or approved at this revision.

## 13. Verification & Validation

_TBD_

Architecture verification is by review per REQ-HFPX-NSA-005. Review scope, entry criteria, and artefacts TBD. Child-requirement verification methods TBD in the V&V Plan.

## 14. Risks

- Sensor complement defined as classes only → risk of late interface churn; mitigation: freeze interface classes with Vol 08.8 in a later revision
- Primary/backup allocation TBD → risk of single-point sensitivity; mitigation: allocation action carried as open issue

## 15. Open Issues

- Sensor class list to be confirmed against FUN-003 threads (OPEN)
- Primary/backup allocation criteria TBD (OPEN)
- Vol 08.8 interface-class alignment TBD (OPEN)
- Vol 21.7 installation-constraint capture TBD (OPEN)

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SYS-004, FUN-003, SAD DAT/LOG views, Vol 08.8 interface definitions, Vol 21.7 installation constraints, and child Chapters 09.2–09.9.

## 18. Traceability

Parents: REQ-HFPX-SYS-004, REQ-HFPX-FUN-003, SAD DAT/LOG views. Children: REQ-HFPX-NSA-001..005; child sensor chapters 09.2–09.9; V&V cases TBD; RTM rows TBD.

## 19. Configuration

BL-0.0 (structure only) — Tranche 5 draft, not baselined. Changes require change control; no values in this document are approved.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 structure-only draft (Chapter 09.1) |
