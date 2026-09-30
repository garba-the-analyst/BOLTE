# 09.3 Gyroscopes

**Document ID:** HFPX-NAV-GYR-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the structure for HFP-X gyroscopes (Volume 09, Chapter 09.3). This revision establishes section structure and the initial requirement set only; all design detail is TBD.

## 2. Scope

Covers rate-sensing functions, performance structure, technology structure, and verification structure for gyroscopes. IMU integration is addressed in Chapter 09.2; fusion in 09.13.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parent SYS-004)
- HFPX functional requirements FUN-003 (parent)
- HFPX SAD DAT/LOG views (parent allocation views)
- HFPX-NAV-ARC-001 Sensor Architecture (09.1)
- HFPX-NAV-IMU-001 IMU (09.2)
- _templates/DOCUMENT_TEMPLATE.md (structure)

## 4. Definitions & Acronyms

- NGY: gyroscope requirement prefix
- TBD: to be determined; no values are approved at this revision
- Verification methods: Review / Inspection / Analysis / Demonstration / Test (allocated per requirement)

## 5. System Context

Gyroscopes support REQ-HFPX-SYS-004 by providing angular-rate sensing for attitude estimation and stabilisation, within the IMU and sensor complement defined by HFPX-NAV-ARC-001 and HFPX-NAV-IMU-001.

```text
SYS-004 → NAV-ARC-001 → NAV-IMU-001 → NAV-GYR-001 → fusion / flight control
```

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-NGY-001|The gyroscopes shall provide angular rate-sensing functions, with functions TBD.|REQ-HFPX-SYS-004, REQ-HFPX-FUN-003, SAD DAT/LOG|Inspection|
|REQ-HFPX-NGY-002|The gyroscope performance shall be defined, with all performance values TBD.|REQ-HFPX-SYS-004, REQ-HFPX-FUN-003, SAD DAT/LOG|Inspection|
|REQ-HFPX-NGY-003|The gyroscope technology shall be defined, with technology TBD and no technology selected.|REQ-HFPX-SYS-004, REQ-HFPX-FUN-003, SAD DAT/LOG|Inspection|
|REQ-HFPX-NGY-004|The gyroscope requirements shall be verified, with verification method and artefacts TBD.|REQ-HFPX-SYS-004, REQ-HFPX-FUN-003, SAD DAT/LOG|Inspection|

No accuracies, ranges, rates, or biases are stated in this revision. No parts are selected and no technology is selected at this revision.

## 7. Architecture

_TBD_

Structure placeholder: gyroscope placement within IMU and airframe TBD; axes and redundancy topology TBD.

## 8. Detailed Design

_TBD_

Not applicable at this revision — structure only. Technology, packaging, and mounting TBD with no selection made.

## 9. Interfaces

_TBD_

Gyroscope data, power, and mechanical interfaces TBD. Interface classes to align with HFPX-NAV-ARC-001 and Vol 08.8.

## 10. Operational Concept

_TBD_

Gyroscope use across flight phases TBD. Start-up, alignment, and degraded-mode behaviour TBD.

## 11. Safety

_TBD_

Safety relevance of gyroscope loss or degradation TBD. Hazard mitigations TBD (Vol 13 analyses to feed later revisions).

## 12. Performance

_TBD_

All performance values TBD. No rate, bias, noise, or stability figure is stated or approved at this revision.

## 13. Verification & Validation

_TBD_

Verification methods and cases for REQ-HFPX-NGY-001..004 TBD in the V&V Plan. No test values are approved at this revision.

## 14. Risks

- Rate-sensing functions TBD → risk of late attitude-estimation rework; mitigation: function action carried as open issue
- Technology TBD → risk of late interface change; mitigation: no selection made at this revision, selection deferred with explicit TBD

## 15. Open Issues

- Rate-sensing function list TBD (OPEN)
- Performance values TBD (OPEN)
- Technology options TBD with no selection (OPEN)
- Verification methods TBD (OPEN)

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SYS-004, FUN-003, SAD DAT/LOG views, HFPX-NAV-ARC-001, HFPX-NAV-IMU-001, and fusion Chapter 09.13.

## 18. Traceability

Parents: REQ-HFPX-SYS-004, REQ-HFPX-FUN-003, SAD DAT/LOG views. Children: REQ-HFPX-NGY-001..004; V&V cases TBD; RTM rows TBD.

## 19. Configuration

BL-0.0 (structure only) — Tranche 5 draft, not baselined. Changes require change control; no values in this document are approved.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 structure-only draft (Chapter 09.3) |
