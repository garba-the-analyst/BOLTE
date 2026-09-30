# 09.9 Altitude Sensing

**Document ID:** HFPX-NAV-ALT-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the structure for HFP-X altitude (above-ground-level) sensing (Volume 09, Chapter 09.9). This revision establishes section structure and the initial requirement set only; all design detail is TBD.

## 2. Scope

Covers above-ground-level sensing function structure, range/accuracy structure, sensor-to-landing-controller interface structure, and verification structure. Barometric altitude is addressed in Chapter 09.7; landing control in Vol 07.14.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parent SYS-004)
- HFPX functional requirements FUN-003 (parent)
- HFPX SAD DAT/LOG views (parent allocation views)
- HFPX-NAV-ARC-001 Sensor Architecture (09.1)
- Vol 07.14 (landing controller interface)
- _templates/DOCUMENT_TEMPLATE.md (structure)

## 4. Definitions & Acronyms

- NAL: altitude-sensing requirement prefix; AGL: above ground level
- TBD: to be determined; no values are approved at this revision
- Verification methods: Review / Inspection / Analysis / Demonstration / Test (allocated per requirement)

## 5. System Context

Altitude sensing supports REQ-HFPX-SYS-004 by providing above-ground-level measurements critical for hover and landing, within the sensor complement defined by HFPX-NAV-ARC-001 and consumed by the landing controller (Vol 07.14).

```text
SYS-004 → NAV-ARC-001 → NAV-ALT-001 → landing controller (Vol 07.14)
```

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-NAL-001|The altitude sensing function shall provide above-ground-level sensing critical for hover and landing, with sensing principle TBD.|REQ-HFPX-SYS-004, REQ-HFPX-FUN-003, SAD DAT/LOG|Inspection|
|REQ-HFPX-NAL-002|The altitude sensing range and accuracy shall be defined, with range and accuracy TBD.|REQ-HFPX-SYS-004, REQ-HFPX-FUN-003, SAD DAT/LOG|Test|
|REQ-HFPX-NAL-003|The sensor-to-landing-controller interface shall be defined consistent with Vol 07.14, with interface details TBD.|REQ-HFPX-SYS-004, REQ-HFPX-FUN-003, SAD DAT/LOG|Inspection|
|REQ-HFPX-NAL-004|The altitude sensing requirements shall be verified, with verification method and artefacts TBD.|REQ-HFPX-SYS-004, REQ-HFPX-FUN-003, SAD DAT/LOG|Inspection|

No accuracies, ranges, rates, or biases are stated in this revision. No parts are selected at this revision.

## 7. Architecture

_TBD_

Structure placeholder: altitude-sensing placement within the sensor complement TBD; relationship to barometric altitude (09.7), fusion (09.13), and landing controller TBD.

## 8. Detailed Design

_TBD_

Not applicable at this revision — structure only. Sensing principle, packaging, and mounting TBD with no selection made.

## 9. Interfaces

_TBD_

Altitude-sensing data, power, and mechanical interfaces TBD; sensor-to-landing-controller interface per Vol 07.14 TBD. Interface classes to align with HFPX-NAV-ARC-001 and Vol 08.8.

## 10. Operational Concept

_TBD_

Altitude-sensing use in hover and landing TBD. Degraded-mode behaviour TBD.

## 11. Safety

_TBD_

Safety relevance of altitude-sensing loss or degradation in hover/landing TBD. Hazard mitigations TBD (Vol 13 analyses to feed later revisions).

## 12. Performance

_TBD_

All performance values TBD. No range or accuracy figure is stated or approved at this revision.

## 13. Verification & Validation

_TBD_

Verification methods and cases for REQ-HFPX-NAL-001..004 TBD in the V&V Plan. No test values are approved at this revision.

## 14. Risks

- Sensing principle TBD → risk of late hover/landing integration churn; mitigation: principle selection deferred as explicit TBD
- Range/accuracy TBD → risk of late landing-performance gaps; mitigation: TBD captured explicitly, no placeholder values used

## 15. Open Issues

- Above-ground-level sensing function and principle TBD, hover/landing critical (OPEN)
- Range and accuracy TBD (OPEN)
- Sensor-to-landing-controller interface per Vol 07.14 TBD (OPEN)
- Verification methods TBD (OPEN)

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SYS-004, FUN-003, SAD DAT/LOG views, HFPX-NAV-ARC-001, HFPX-NAV-BAR-001, Vol 07.14 landing controller, and fusion Chapter 09.13.

## 18. Traceability

Parents: REQ-HFPX-SYS-004, REQ-HFPX-FUN-003, SAD DAT/LOG views. Children: REQ-HFPX-NAL-001..004; V&V cases TBD; RTM rows TBD.

## 19. Configuration

BL-0.0 (structure only) — Tranche 5 draft, not baselined. Changes require change control; no values in this document are approved.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 structure-only draft (Chapter 09.9) |
