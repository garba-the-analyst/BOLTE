# Rain

**Document ID:** HFPX-THM-RAN-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X rain structure for Chapter 14.11. This Tranche 6 draft establishes rain/ingress definition, engine/sensor effects, operating-limit structure, and verification structure with all values TBD; quantified envelopes follow in later tranches.

## 2. Scope

Covers rain/ingress definition, engine and sensor effect structure, and operating-limit structure. Excludes quantified rates/durations, operating instructions, and qualification detail (14.14, Vol 22/23). All values TBD.

## 3. Applicable Documents

- HFPX-SYS-ENV-001 Environmental Requirements (parent REQ-HFPX-SYS-006, ENV-003)
- HFPX-SYS-REQ-001 SyRS (REQ-HFPX-SYS-006 environmental policy)
- HFPX-THM-ENC-001 Environmental Conditions (condition inventory, TBD)
- Vol 04 propulsion, Vol 05 sensors (structure only)

## 4. Definitions & Acronyms

- TRN: rain requirement tier; ID `REQ-HFPX-TRN-NNN`; verification: TBD (intended Analysis + Test).
- Rain/ingress: precipitation exposure plus water-ingress associations; values TBD.
- TBD/TBC: unknown data; no values invented.

## 5. System Context

Rain tier refines SYS-006, ENV-003, and TEN inventory into definition, effects, and limits:

```text
SYS-006 → ENV-003 → TRN-001..004 (definition, effects, limits) → Airframe/propulsion/sensor specs → Qualification (14.14, Vol 22/23)
```

Rates and effects require surveys, models, and programme decisions before any value is approved.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-TRN-001|The system shall define rain and ingress exposure of [TBD] with rates and durations TBD (values TBD).|REQ-HFPX-SYS-006; REQ-HFPX-ENV-003|Inspection|
|REQ-HFPX-TRN-002|The system shall define rain effects on engines and sensors of [TBD] (effects TBD).|REQ-HFPX-SYS-006|Inspection|
|REQ-HFPX-TRN-003|The system shall operate within defined rain operating limits of [TBD] (limits TBD).|REQ-HFPX-SYS-006; REQ-HFPX-ENV-003|Inspection|
|REQ-HFPX-TRN-004|Each rain requirement shall be verified by method of [TBD] with criteria TBD (verification TBD).|REQ-HFPX-SYS-006|Inspection|

No rain rate, duration, ingress bound, or operating limit is stated or implied; all values are TBD.

## 7. Architecture

Starter allocation (SAD owns authoritative mapping): definition → exposure envelope TBD; effects → Vol 04 engine / Vol 05 sensor mappings TBD; limits → operating-envelope rules TBD. All TBC pending subsystem specs.

## 8. Detailed Design

Not applicable — structure level only. Seals, drains, inlets, and sensor-protection designs live in Vol 03–05 and are TBD.

## 9. Interfaces

Rain interfaces (sealing/drainage boundaries, inlet and sensor exposures) are TBD in Chapter 01.16 and Vol 02 ICDs with Vol 04/05 counterparts. No interface value is approved.

## 10. Operational Concept

Requirements apply across CONOPS phases as applicable; phase applicability matrix is TBD. Operations outside defined limits (TBD) are prohibited pending quantified revisions; no operating instruction is given beyond this structuring rule.

## 11. Safety

Rain-induced hazards feed Vol 13 safety analyses (to follow). No limit in this revision is a safety claim; safety credit requires analysed and tested limits via change record.

## 12. Performance

Rain definitions do not quantify performance. Engine/sensor performance interactions under rain are TBD and owned jointly with Vol 04/05 tiers.

## 13. Verification & Validation

Intended method is Analysis + Test (see table; detail TBD); rates, durations, and pass criteria are TBD in 14.14 and the V&V Plan (Vol 22). No verification credit is claimed at this revision.

## 14. Risks

- Exposure undefined → incompatible inlet/sealing assumptions; mitigation: single TBD-owned tier with CONCEPT status.
- Over-testing to unapproved levels; mitigation: change-controlled quantification only.

## 15. Open Issues

Exposure definition, engine/sensor effect mapping, operating-limit rules, and verification method confirmation. RTM seed for TRN-001..004 added with this tranche (Status CONCEPT).

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SYS-006 stability, ENV-003, TEN inventory, Vol 04/05 inputs, and V&V Plan strategy. Changes propagate by change record.

## 18. Traceability

Parents: REQ-HFPX-SYS-006; REQ-HFPX-ENV-003 (see table). Children: airframe/propulsion/sensor rain provisions, qualification cases (14.14, Vol 22/23), RTM rows. RTM seed for TRN-001..004 added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Quantification requires new revisions via change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 14.11; all values TBD) |
