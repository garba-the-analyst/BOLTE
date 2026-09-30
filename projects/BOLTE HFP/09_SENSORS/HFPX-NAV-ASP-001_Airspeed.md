# 09.8 Airspeed

**Document ID:** HFPX-NAV-ASP-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the structure for HFP-X airspeed sensing (Volume 09, Chapter 09.8). This revision establishes section structure and the initial requirement set only; all design detail is TBD.

## 2. Scope

Covers airspeed function structure, low-speed/hover limitation structure, icing/contamination consideration structure, and verification structure. Air-data use in control laws lives with flight control volumes.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parent SYS-004)
- HFPX functional requirements FUN-003 (parent)
- HFPX SAD DAT/LOG views (parent allocation views)
- HFPX-NAV-ARC-001 Sensor Architecture (09.1)
- _templates/DOCUMENT_TEMPLATE.md (structure)

## 4. Definitions & Acronyms

- NAS: airspeed requirement prefix
- TBD: to be determined; no values are approved at this revision
- Verification methods: Review / Inspection / Analysis / Demonstration / Test (allocated per requirement)

## 5. System Context

Airspeed sensing supports REQ-HFPX-SYS-004 by providing air-data measurements for flight control and navigation, within the sensor complement defined by HFPX-NAV-ARC-001.

```text
SYS-004 → NAV-ARC-001 → NAV-ASP-001 → flight control / fusion
```

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-NAS-001|The airspeed function shall be provided, with probe principle TBD.|REQ-HFPX-SYS-004, REQ-HFPX-FUN-003, SAD DAT/LOG|Inspection|
|REQ-HFPX-NAS-002|The airspeed low-speed and hover limitations shall be defined, with limitations TBD.|REQ-HFPX-SYS-004, REQ-HFPX-FUN-003, SAD DAT/LOG|Inspection|
|REQ-HFPX-NAS-003|The airspeed design shall address icing and contamination considerations, with considerations TBD.|REQ-HFPX-SYS-004, REQ-HFPX-FUN-003, SAD DAT/LOG|Inspection|
|REQ-HFPX-NAS-004|The airspeed requirements shall be verified, with verification method and artefacts TBD.|REQ-HFPX-SYS-004, REQ-HFPX-FUN-003, SAD DAT/LOG|Inspection|

No accuracies, ranges, rates, or biases are stated in this revision. No parts are selected at this revision.

## 7. Architecture

_TBD_

Structure placeholder: airspeed sensing placement within the sensor complement TBD; relationship to air-data estimation TBD.

## 8. Detailed Design

_TBD_

Not applicable at this revision — structure only. Probe principle, packaging, and mounting TBD with no selection made.

## 9. Interfaces

_TBD_

Airspeed data, power, pneumatic, and mechanical interfaces TBD. Interface classes to align with HFPX-NAV-ARC-001 and Vol 08.8.

## 10. Operational Concept

_TBD_

Airspeed use across flight phases TBD, including low-speed and hover regimes TBD. Degraded-mode behaviour TBD.

## 11. Safety

_TBD_

Safety relevance of airspeed loss or degradation TBD. Hazard mitigations TBD (Vol 13 analyses to feed later revisions).

## 12. Performance

_TBD_

All performance values TBD. No accuracy, range, or threshold figure is stated or approved at this revision.

## 13. Verification & Validation

_TBD_

Verification methods and cases for REQ-HFPX-NAS-001..004 TBD in the V&V Plan. No test values are approved at this revision.

## 14. Risks

- Low-speed/hover limitations TBD → risk of late control-law input gaps; mitigation: limitation characterisation carried as open issue
- Icing/contamination TBD → risk of late environmental findings; mitigation: considerations captured as explicit TBD requirement

## 15. Open Issues

- Airspeed function and probe principle TBD (OPEN)
- Low-speed/hover limitations TBD (OPEN)
- Icing/contamination considerations TBD (OPEN)
- Verification methods TBD (OPEN)

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SYS-004, FUN-003, SAD DAT/LOG views, HFPX-NAV-ARC-001, and flight-control air-data consumers.

## 18. Traceability

Parents: REQ-HFPX-SYS-004, REQ-HFPX-FUN-003, SAD DAT/LOG views. Children: REQ-HFPX-NAS-001..004; V&V cases TBD; RTM rows TBD.

## 19. Configuration

BL-0.0 (structure only) — Tranche 5 draft, not baselined. Changes require change control; no values in this document are approved.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 structure-only draft (Chapter 09.8) |
