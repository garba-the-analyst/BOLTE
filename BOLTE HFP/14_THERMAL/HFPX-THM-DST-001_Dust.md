# Dust

**Document ID:** HFPX-THM-DST-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X dust structure for Chapter 14.12. This Tranche 6 draft establishes dust/erosion definition, filtration hooks, operating-limit structure, and verification structure with all values TBD; quantified envelopes follow in later tranches.

## 2. Scope

Covers dust/erosion definition, filtration hooks, and operating-limit structure. Excludes quantified concentrations/durations, operating instructions, and qualification detail (14.14, Vol 22/23). All values TBD.

## 3. Applicable Documents

- HFPX-SYS-ENV-001 Environmental Requirements (parent REQ-HFPX-SYS-006, ENV-003)
- HFPX-SYS-REQ-001 SyRS (REQ-HFPX-SYS-006 environmental policy)
- HFPX-THM-ENC-001 Environmental Conditions (condition inventory, TBD)
- Vol 05.7 filtration/air provisions (structure only; hooks TBD)

## 4. Definitions & Acronyms

- TDU: dust requirement tier; ID `REQ-HFPX-TDU-NNN`; verification: TBD (intended Analysis + Test).
- Dust/erosion: particulate exposure plus erosion associations; values TBD.
- TBD/TBC: unknown data; no values invented.

## 5. System Context

Dust tier refines SYS-006, ENV-003, and TEN inventory into definition, filtration, and limits:

```text
SYS-006 → ENV-003 → TDU-001..004 (definition, filtration, limits) → Vol 05.7 / airframe specs → Qualification (14.14, Vol 22/23)
```

Concentrations and effects require surveys and programme decisions before any value is approved.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-TDU-001|The system shall define dust and erosion exposure of [TBD] with concentrations and durations TBD (values TBD).|REQ-HFPX-SYS-006; REQ-HFPX-ENV-003|Inspection|
|REQ-HFPX-TDU-002|The system shall define filtration provisions of [TBD] with hooks to Vol 05.7 TBD (detail TBD).|REQ-HFPX-SYS-006|Inspection|
|REQ-HFPX-TDU-003|The system shall operate within defined dust operating limits of [TBD] (limits TBD).|REQ-HFPX-SYS-006; REQ-HFPX-ENV-003|Inspection|
|REQ-HFPX-TDU-004|Each dust requirement shall be verified by method of [TBD] with criteria TBD (verification TBD).|REQ-HFPX-SYS-006|Inspection|

No dust concentration, duration, erosion bound, or operating limit is stated or implied; all values are TBD.

## 7. Architecture

Starter allocation (SAD owns authoritative mapping): definition → exposure envelope TBD; filtration → Vol 05.7 provisions TBD; limits → operating-envelope rules TBD. All TBC pending subsystem specs.

## 8. Detailed Design

Not applicable — structure level only. Filters, seals, inlets, and erosion-protection designs live in Vol 03–05 and are TBD.

## 9. Interfaces

Dust interfaces (inlet exposures, Vol 05.7 filtration boundaries, sealing interfaces) are TBD in Chapter 01.16 and Vol 02 ICDs. No interface value is approved.

## 10. Operational Concept

Requirements apply across CONOPS phases as applicable; phase applicability matrix is TBD. Operations outside defined limits (TBD) are prohibited pending quantified revisions; no operating instruction is given beyond this structuring rule.

## 11. Safety

Dust-induced hazards feed Vol 13 safety analyses (to follow). No limit in this revision is a safety claim; safety credit requires analysed and tested limits via change record.

## 12. Performance

Dust definitions do not quantify performance. Engine/sensor performance interactions under dust are TBD and owned jointly with Vol 04/05 tiers.

## 13. Verification & Validation

Intended method is Analysis + Test (see table; detail TBD); concentrations, durations, and pass criteria are TBD in 14.14 and the V&V Plan (Vol 22). No verification credit is claimed at this revision.

## 14. Risks

- Exposure undefined → incompatible filtration assumptions; mitigation: single TBD-owned tier with CONCEPT status.
- Over-testing to unapproved levels; mitigation: change-controlled quantification only.

## 15. Open Issues

Exposure definition, Vol 05.7 filtration-hook mapping, operating-limit rules, and verification method confirmation. RTM seed for TDU-001..004 added with this tranche (Status CONCEPT).

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SYS-006 stability, ENV-003, TEN inventory, Vol 05.7 inputs, and V&V Plan strategy. Changes propagate by change record.

## 18. Traceability

Parents: REQ-HFPX-SYS-006; REQ-HFPX-ENV-003 (see table). Children: filtration/erosion provisions, qualification cases (14.14, Vol 22/23), RTM rows. RTM seed for TDU-001..004 added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Quantification requires new revisions via change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 14.12; all values TBD) |
