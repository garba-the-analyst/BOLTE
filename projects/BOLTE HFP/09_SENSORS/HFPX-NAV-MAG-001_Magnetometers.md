# 09.5 Magnetometers

**Document ID:** HFPX-NAV-MAG-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the structure for HFP-X magnetometers (Volume 09, Chapter 09.5). This revision establishes section structure and the initial requirement set only; all design detail is TBD.

## 2. Scope

Covers heading-aiding function structure, calibration/compensation structure, interference-source structure, and verification structure. Fusion use lives in Chapter 09.13.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parent SYS-004)
- HFPX functional requirements FUN-003 (parent)
- HFPX SAD DAT/LOG views (parent allocation views)
- HFPX-NAV-ARC-001 Sensor Architecture (09.1)
- _templates/DOCUMENT_TEMPLATE.md (structure)

## 4. Definitions & Acronyms

- NMG: magnetometer requirement prefix
- TBD: to be determined; no values are approved at this revision
- Hard/soft iron: magnetic calibration/compensation terms, details TBD
- Verification methods: Review / Inspection / Analysis / Demonstration / Test (allocated per requirement)

## 5. System Context

Magnetometers support REQ-HFPX-SYS-004 by providing heading-aiding measurements for attitude and navigation estimation, within the sensor complement defined by HFPX-NAV-ARC-001.

```text
SYS-004 → NAV-ARC-001 → NAV-MAG-001 → fusion / flight control
```

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-NMG-001|The magnetometers shall provide heading-aiding function, with function TBD.|REQ-HFPX-SYS-004, REQ-HFPX-FUN-003, SAD DAT/LOG|Inspection|
|REQ-HFPX-NMG-002|The magnetometer calibration and compensation shall be defined, including hard/soft iron aspects TBD.|REQ-HFPX-SYS-004, REQ-HFPX-FUN-003, SAD DAT/LOG|Test|
|REQ-HFPX-NMG-003|The magnetometer design shall address interference sources, including propulsion and electrical sources TBD.|REQ-HFPX-SYS-004, REQ-HFPX-FUN-003, SAD DAT/LOG|Inspection|
|REQ-HFPX-NMG-004|The magnetometer requirements shall be verified, with verification method and artefacts TBD.|REQ-HFPX-SYS-004, REQ-HFPX-FUN-003, SAD DAT/LOG|Inspection|

No accuracies, ranges, rates, or biases are stated in this revision. No parts are selected at this revision.

## 7. Architecture

_TBD_

Structure placeholder: magnetometer placement within the airframe TBD; relationship to heading estimation and fusion TBD.

## 8. Detailed Design

_TBD_

Not applicable at this revision — structure only. Sensing, packaging, mounting, and calibration provisions TBD with no selection made.

## 9. Interfaces

_TBD_

Magnetometer data, power, and mechanical interfaces TBD. Interface classes to align with HFPX-NAV-ARC-001 and Vol 08.8.

## 10. Operational Concept

_TBD_

Magnetometer use across flight phases TBD. Calibration procedures and degraded-mode behaviour TBD.

## 11. Safety

_TBD_

Safety relevance of magnetometer loss or degradation TBD. Hazard mitigations TBD (Vol 13 analyses to feed later revisions).

## 12. Performance

_TBD_

All performance values TBD. No heading, bias, or noise figure is stated or approved at this revision.

## 13. Verification & Validation

_TBD_

Verification methods and cases for REQ-HFPX-NMG-001..004 TBD in the V&V Plan. No test values are approved at this revision.

## 14. Risks

- Calibration/compensation TBD → risk of late heading errors; mitigation: calibration action carried as open issue
- Interference sources TBD → risk of late placement churn; mitigation: propulsion/electrical source survey deferred as explicit TBD

## 15. Open Issues

- Heading-aiding function TBD (OPEN)
- Calibration/compensation including hard/soft iron TBD (OPEN)
- Interference sources including propulsion/electrical TBD (OPEN)
- Verification methods TBD (OPEN)

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SYS-004, FUN-003, SAD DAT/LOG views, HFPX-NAV-ARC-001, propulsion/electrical interference inputs, and fusion Chapter 09.13.

## 18. Traceability

Parents: REQ-HFPX-SYS-004, REQ-HFPX-FUN-003, SAD DAT/LOG views. Children: REQ-HFPX-NMG-001..004; V&V cases TBD; RTM rows TBD.

## 19. Configuration

BL-0.0 (structure only) — Tranche 5 draft, not baselined. Changes require change control; no values in this document are approved.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 structure-only draft (Chapter 09.5) |
