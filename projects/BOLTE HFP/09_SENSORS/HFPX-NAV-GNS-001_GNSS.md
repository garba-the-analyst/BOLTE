# 09.6 GNSS

**Document ID:** HFPX-NAV-GNS-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the structure for HFP-X GNSS (Volume 09, Chapter 09.6). This revision establishes section structure and the initial requirement set only; all design detail is TBD.

## 2. Scope

Covers position/velocity/time function structure, denial/degradation behaviour structure, antenna/installation structure, and verification structure. Fusion and dead-reckoning integration live in Chapter 09.13.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parent SYS-004)
- HFPX functional requirements FUN-003 (parent)
- HFPX SAD DAT/LOG views (parent allocation views)
- HFPX-NAV-ARC-001 Sensor Architecture (09.1)
- _templates/DOCUMENT_TEMPLATE.md (structure)

## 4. Definitions & Acronyms

- GNSS: global navigation satellite system; NGN: GNSS requirement prefix
- TBD: to be determined; no values are approved at this revision
- Dead reckoning: navigation without GNSS, handover details TBD
- Verification methods: Review / Inspection / Analysis / Demonstration / Test (allocated per requirement)

## 5. System Context

GNSS supports REQ-HFPX-SYS-004 by providing position, velocity, and time measurements for navigation, within the sensor complement defined by HFPX-NAV-ARC-001.

```text
SYS-004 → NAV-ARC-001 → NAV-GNS-001 → fusion / flight control
```

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-NGN-001|The GNSS shall provide position, velocity, and time function, with function TBD.|REQ-HFPX-SYS-004, REQ-HFPX-FUN-003, SAD DAT/LOG|Inspection|
|REQ-HFPX-NGN-002|The GNSS denial and degradation behaviour shall be defined, including dead-reckoning handover TBD.|REQ-HFPX-SYS-004, REQ-HFPX-FUN-003, SAD DAT/LOG|Inspection|
|REQ-HFPX-NGN-003|The GNSS antenna and installation shall be defined, with antenna and installation TBD.|REQ-HFPX-SYS-004, REQ-HFPX-FUN-003, SAD DAT/LOG|Inspection|
|REQ-HFPX-NGN-004|The GNSS requirements shall be verified, with verification method and artefacts TBD.|REQ-HFPX-SYS-004, REQ-HFPX-FUN-003, SAD DAT/LOG|Inspection|

No accuracies, ranges, rates, or biases are stated in this revision. No parts are selected at this revision.

## 7. Architecture

_TBD_

Structure placeholder: GNSS placement within the sensor complement TBD; relationship to fusion and dead reckoning TBD.

## 8. Detailed Design

_TBD_

Not applicable at this revision — structure only. Receiver, antenna, and installation provisions TBD with no selection made.

## 9. Interfaces

_TBD_

GNSS data, power, RF, and mechanical interfaces TBD. Interface classes to align with HFPX-NAV-ARC-001 and Vol 08.8.

## 10. Operational Concept

_TBD_

GNSS use across flight phases TBD. Denied/degraded operations and handover to dead reckoning TBD.

## 11. Safety

_TBD_

Safety relevance of GNSS denial or degradation TBD. Hazard mitigations TBD (Vol 13 analyses to feed later revisions).

## 12. Performance

_TBD_

All performance values TBD. No accuracy, availability, or continuity figure is stated or approved at this revision.

## 13. Verification & Validation

_TBD_

Verification methods and cases for REQ-HFPX-NGN-001..004 TBD in the V&V Plan. No test values are approved at this revision.

## 14. Risks

- Denial/degradation behaviour TBD → risk of late navigation-gap findings; mitigation: dead-reckoning handover action carried as open issue
- Antenna/installation TBD → risk of late signal-performance churn; mitigation: installation survey deferred as explicit TBD

## 15. Open Issues

- Position/velocity/time function TBD (OPEN)
- Denial/degradation behaviour including dead-reckoning handover TBD (OPEN)
- Antenna and installation TBD (OPEN)
- Verification methods TBD (OPEN)

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SYS-004, FUN-003, SAD DAT/LOG views, HFPX-NAV-ARC-001, and fusion/dead-reckoning Chapter 09.13.

## 18. Traceability

Parents: REQ-HFPX-SYS-004, REQ-HFPX-FUN-003, SAD DAT/LOG views. Children: REQ-HFPX-NGN-001..004; V&V cases TBD; RTM rows TBD.

## 19. Configuration

BL-0.0 (structure only) — Tranche 5 draft, not baselined. Changes require change control; no values in this document are approved.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 structure-only draft (Chapter 09.6) |
