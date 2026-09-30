# Wind

**Document ID:** HFPX-THM-WND-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X wind structure for Chapter 14.13. This Tranche 6 draft establishes wind-environment definition, operating limits, ground-operations coverage, and verification structure with all values TBD; quantified envelopes follow in later tranches.

## 2. Scope

Covers wind-environment definition, operating limits, and ground-operations provisions. Excludes quantified thresholds, operating instructions, and qualification detail (14.14, Vol 22/23); performance wind limits owned by 01.8. All values TBD.

## 3. Applicable Documents

- HFPX-SYS-ENV-001 Environmental Requirements (parent REQ-HFPX-SYS-006, ENV-004)
- HFPX-SYS-REQ-001 SyRS (REQ-HFPX-SYS-006 environmental policy)
- HFPX-THM-ENC-001 Environmental Conditions (condition inventory, TBD)
- Vol 06.17 wind/aero environment (structure only; values TBD)

## 4. Definitions & Acronyms

- TWN: wind requirement tier; ID `REQ-HFPX-TWN-NNN`; verification: TBD (intended Analysis + Test).
- Wind environment: steady/gust exposure across ground and flight phases; values TBD.
- TBD/TBC: unknown data; no values invented.

## 5. System Context

Wind tier refines SYS-006, ENV-004, and TEN inventory into environment, limits, and ground ops:

```text
SYS-006 → ENV-004 → TWN-001..004 (environment, limits, ground ops) → FCS/aero specs → Qualification (14.14, Vol 22/23)
```

Thresholds require surveys, models, and programme decisions before any value is approved.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-TWN-001|The system shall define the wind environment of [TBD] with interfaces to Vol 06.17 TBD (values TBD).|REQ-HFPX-SYS-006; REQ-HFPX-ENV-004|Inspection|
|REQ-HFPX-TWN-002|The system shall operate within defined wind operating limits of [TBD] (limits TBD).|REQ-HFPX-SYS-006; REQ-HFPX-ENV-004|Inspection|
|REQ-HFPX-TWN-003|The system shall define ground-operations wind provisions of [TBD] (provisions TBD).|REQ-HFPX-SYS-006|Inspection|
|REQ-HFPX-TWN-004|Each wind requirement shall be verified by method of [TBD] with criteria TBD (verification TBD).|REQ-HFPX-SYS-006|Inspection|

No wind speed, gust value, duration, or operating limit is stated or implied; all values are TBD.

## 7. Architecture

Starter allocation (SAD owns authoritative mapping): environment → Vol 06.17 wind model TBD; limits → ground/flight envelope rules TBD; ground ops → tie-down/handling provisions TBD. All TBC pending aero inputs.

## 8. Detailed Design

Not applicable — structure level only. FCS laws, restraints, and ground-equipment provisions live in Vol 06 and are TBD.

## 9. Interfaces

Wind interfaces (Vol 06.17 aero-environment boundary, FCS interfaces, ground-ops/GSE interfaces) are TBD in Chapter 01.16 and Vol 02 ICDs. No interface value is approved.

## 10. Operational Concept

Requirements apply across CONOPS ground, flight, and post-flight phases as applicable; phase applicability matrix is TBD. Operations outside defined limits (TBD) are prohibited pending quantified revisions; no operating instruction is given beyond this structuring rule.

## 11. Safety

Wind-induced hazards feed Vol 13 safety analyses (to follow). No limit in this revision is a safety claim; safety credit requires analysed and tested limits via change record.

## 12. Performance

Wind definitions do not quantify performance. Performance wind limits are owned by 01.8; interactions are TBD and owned jointly.

## 13. Verification & Validation

Intended method is Analysis + Test (see table; detail TBD); thresholds, test conditions, and pass criteria are TBD in 14.14 and the V&V Plan (Vol 22). No verification credit is claimed at this revision.

## 14. Risks

- Environment undefined → incompatible FCS/aero assumptions; mitigation: single TBD-owned tier with CONCEPT status.
- Over-testing to unapproved levels; mitigation: change-controlled quantification only.

## 15. Open Issues

Vol 06.17 environment mapping, operating-limit rules, ground-ops provisions, and verification method confirmation. RTM seed for TWN-001..004 added with this tranche (Status CONCEPT).

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SYS-006 stability, ENV-004, TEN inventory, Vol 06.17 inputs, and V&V Plan strategy. Changes propagate by change record.

## 18. Traceability

Parents: REQ-HFPX-SYS-006; REQ-HFPX-ENV-004 (see table). Children: FCS/aero wind provisions, qualification cases (14.14, Vol 22/23), RTM rows. RTM seed for TWN-001..004 added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Quantification requires new revisions via change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 14.13; all values TBD) |
