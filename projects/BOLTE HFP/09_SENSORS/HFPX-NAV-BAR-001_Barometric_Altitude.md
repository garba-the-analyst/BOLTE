# 09.7 Barometric Altitude

**Document ID:** HFPX-NAV-BAR-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the structure for HFP-X barometric altitude sensing (Volume 09, Chapter 09.7). This revision establishes section structure and the initial requirement set only; all design detail is TBD.

## 2. Scope

Covers barometric altitude function structure, accuracy structure, temperature-compensation structure, and verification structure. Fusion with other altitude sources lives in Chapter 09.13.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parent SYS-004)
- HFPX functional requirements FUN-003 (parent)
- HFPX SAD DAT/LOG views (parent allocation views)
- HFPX-NAV-ARC-001 Sensor Architecture (09.1)
- _templates/DOCUMENT_TEMPLATE.md (structure)

## 4. Definitions & Acronyms

- NBA: barometric altitude requirement prefix
- TBD: to be determined; no values are approved at this revision
- Verification methods: Review / Inspection / Analysis / Demonstration / Test (allocated per requirement)

## 5. System Context

Barometric altitude supports REQ-HFPX-SYS-004 by providing pressure-based altitude measurements for vertical navigation and control, within the sensor complement defined by HFPX-NAV-ARC-001.

```text
SYS-004 → NAV-ARC-001 → NAV-BAR-001 → fusion / flight control
```

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-NBA-001|The barometric altitude function shall be provided, with function TBD.|REQ-HFPX-SYS-004, REQ-HFPX-FUN-003, SAD DAT/LOG|Inspection|
|REQ-HFPX-NBA-002|The barometric altitude accuracy shall be defined, with accuracy TBD.|REQ-HFPX-SYS-004, REQ-HFPX-FUN-003, SAD DAT/LOG|Test|
|REQ-HFPX-NBA-003|The barometric altitude temperature compensation shall be defined, with compensation TBD.|REQ-HFPX-SYS-004, REQ-HFPX-FUN-003, SAD DAT/LOG|Inspection|
|REQ-HFPX-NBA-004|The barometric altitude requirements shall be verified, with verification method and artefacts TBD.|REQ-HFPX-SYS-004, REQ-HFPX-FUN-003, SAD DAT/LOG|Inspection|

No accuracies, ranges, rates, or biases are stated in this revision. No parts are selected at this revision.

## 7. Architecture

_TBD_

Structure placeholder: barometric sensing placement within the sensor complement TBD; relationship to static-pressure sources and fusion TBD.

## 8. Detailed Design

_TBD_

Not applicable at this revision — structure only. Sensing, packaging, porting, and mounting TBD with no selection made.

## 9. Interfaces

_TBD_

Barometric data, power, pneumatic, and mechanical interfaces TBD. Interface classes to align with HFPX-NAV-ARC-001 and Vol 08.8.

## 10. Operational Concept

_TBD_

Barometric altitude use across flight phases TBD. Calibration, setting procedures, and degraded-mode behaviour TBD.

## 11. Safety

_TBD_

Safety relevance of barometric altitude loss or degradation TBD. Hazard mitigations TBD (Vol 13 analyses to feed later revisions).

## 12. Performance

_TBD_

All performance values TBD. No accuracy or stability figure is stated or approved at this revision.

## 13. Verification & Validation

_TBD_

Verification methods and cases for REQ-HFPX-NBA-001..004 TBD in the V&V Plan. No test values are approved at this revision.

## 14. Risks

- Accuracy TBD → risk of late vertical-loop rework; mitigation: accuracy action carried as open issue
- Temperature compensation TBD → risk of late environmental findings; mitigation: compensation provisions deferred as explicit TBD

## 15. Open Issues

- Altitude function TBD (OPEN)
- Accuracy TBD (OPEN)
- Temperature compensation TBD (OPEN)
- Verification methods TBD (OPEN)

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SYS-004, FUN-003, SAD DAT/LOG views, HFPX-NAV-ARC-001, and fusion Chapter 09.13.

## 18. Traceability

Parents: REQ-HFPX-SYS-004, REQ-HFPX-FUN-003, SAD DAT/LOG views. Children: REQ-HFPX-NBA-001..004; V&V cases TBD; RTM rows TBD.

## 19. Configuration

BL-0.0 (structure only) — Tranche 5 draft, not baselined. Changes require change control; no values in this document are approved.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 structure-only draft (Chapter 09.7) |
