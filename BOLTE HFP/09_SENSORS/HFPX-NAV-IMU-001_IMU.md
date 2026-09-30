# 09.2 IMU

**Document ID:** HFPX-NAV-IMU-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the structure for the HFP-X inertial measurement unit (Volume 09, Chapter 09.2). This revision establishes section structure and the initial requirement set only; all design detail is TBD.

## 2. Scope

Covers IMU functions, performance structure, redundancy structure, and verification structure. Gyroscope and accelerometer detail lives in Chapters 09.3 and 09.4 respectively; sensor fusion lives in 09.13.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parent SYS-004)
- HFPX functional requirements FUN-003 (parent)
- HFPX SAD DAT/LOG views (parent allocation views)
- HFPX-NAV-ARC-001 Sensor Architecture (09.1)
- _templates/DOCUMENT_TEMPLATE.md (structure)

## 4. Definitions & Acronyms

- IMU: inertial measurement unit; NIM: IMU requirement prefix
- TBD: to be determined; no values are approved at this revision
- Verification methods: Review / Inspection / Analysis / Demonstration / Test (allocated per requirement)

## 5. System Context

The IMU supports REQ-HFPX-SYS-004 by providing the inertial sensing basis for attitude, velocity, and position estimation, within the sensor complement defined by HFPX-NAV-ARC-001.

```text
SYS-004 → NAV-ARC-001 → NAV-IMU-001 → fusion / flight control
```

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-NIM-001|The IMU shall provide inertial measurement functions, with functions TBD.|REQ-HFPX-SYS-004, REQ-HFPX-FUN-003, SAD DAT/LOG|Inspection|
|REQ-HFPX-NIM-002|The IMU performance shall be defined, with bias, noise, and all other performance values TBD.|REQ-HFPX-SYS-004, REQ-HFPX-FUN-003, SAD DAT/LOG|Inspection|
|REQ-HFPX-NIM-003|The IMU redundancy arrangement shall be defined, with redundancy TBD.|REQ-HFPX-SYS-004, REQ-HFPX-FUN-003, SAD DAT/LOG|Inspection|
|REQ-HFPX-NIM-004|The IMU requirements shall be verified, with verification method and artefacts TBD.|REQ-HFPX-SYS-004, REQ-HFPX-FUN-003, SAD DAT/LOG|Inspection|

No accuracies, ranges, rates, or biases are stated in this revision. No parts are selected at this revision.

## 7. Architecture

_TBD_

Structure placeholder: IMU placement within the sensor complement TBD; relationship to gyroscopes (09.3), accelerometers (09.4), and fusion (09.13) TBD.

## 8. Detailed Design

_TBD_

Not applicable at this revision — structure only. Sensing axes, packaging, and internal partitioning TBD with no parts selected.

## 9. Interfaces

_TBD_

IMU data, power, and mechanical interfaces TBD. Interface classes to align with HFPX-NAV-ARC-001 and Vol 08.8.

## 10. Operational Concept

_TBD_

IMU use across flight phases (preflight, hover, transition, cruise, landing) TBD. Degraded-mode behaviour TBD.

## 11. Safety

_TBD_

Safety relevance of IMU loss or degradation TBD. Hazard mitigations TBD (Vol 13 analyses to feed later revisions).

## 12. Performance

_TBD_

All performance values TBD, including bias, noise, and drift-related parameters. No performance figure is stated or approved at this revision.

## 13. Verification & Validation

_TBD_

Verification methods and cases for REQ-HFPX-NIM-001..004 TBD in the V&V Plan. No test values are approved at this revision.

## 14. Risks

- Functions TBD → risk of late scope growth; mitigation: function list action carried as open issue
- Performance TBD → risk to fusion and control design inputs; mitigation: TBD captured explicitly, no placeholder values used

## 15. Open Issues

- IMU function list TBD (OPEN)
- Performance parameters including bias and noise TBD (OPEN)
- Redundancy arrangement TBD (OPEN)
- Verification methods TBD (OPEN)

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SYS-004, FUN-003, SAD DAT/LOG views, HFPX-NAV-ARC-001, and sibling Chapters 09.3, 09.4, and 09.13.

## 18. Traceability

Parents: REQ-HFPX-SYS-004, REQ-HFPX-FUN-003, SAD DAT/LOG views. Children: REQ-HFPX-NIM-001..004; V&V cases TBD; RTM rows TBD.

## 19. Configuration

BL-0.0 (structure only) — Tranche 5 draft, not baselined. Changes require change control; no values in this document are approved.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 structure-only draft (Chapter 09.2) |
