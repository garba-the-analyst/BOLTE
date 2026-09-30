# Low Temperature

**Document ID:** HFPX-THM-LTM-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X low-temperature structure for Chapter 14.9. This Tranche 6 draft establishes low-temperature definition, start/operability structure, storage provisions, and verification structure with all values TBD; quantified envelopes follow in later tranches.

## 2. Scope

Covers operating low-temperature definition, start/operability structure, and storage provisions. Excludes quantified limit values, operating instructions, and qualification detail (14.14, Vol 22/23). All values TBD.

## 3. Applicable Documents

- HFPX-SYS-ENV-001 Environmental Requirements (parent REQ-HFPX-SYS-006, ENV-002/005)
- HFPX-SYS-REQ-001 SyRS (REQ-HFPX-SYS-006 environmental policy)
- HFPX-THM-ENC-001 Environmental Conditions (condition inventory, TBD)
- HFPX-VV-PLN-001 V&V Plan (not written; will own qualification cases)

## 4. Definitions & Acronyms

- TLT: low-temperature requirement tier; ID `REQ-HFPX-TLT-NNN`; verification: TBD (intended Analysis + Test).
- Low-temperature definition: bound plus soak/start associations; values TBD.
- TBD/TBC: unknown data; no values invented.

## 5. System Context

Low-temperature tier refines SYS-006, ENV-002/005, and TEN inventory into definition, operability, and storage:

```text
SYS-006 → ENV-002/005 → TLT-001..004 (definition, operability, storage) → Subsystem specs → Qualification (14.14, Vol 22/23)
```

Bounds require models, surveys, and programme decisions before any limit is approved.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-TLT-001|The system shall define a low-temperature operating definition of [TBD] including soak associations TBD (values TBD).|REQ-HFPX-SYS-006; REQ-HFPX-ENV-002|Inspection|
|REQ-HFPX-TLT-002|The system shall define start and operability behaviour at low temperature of [TBD] (behaviour TBD).|REQ-HFPX-SYS-006|Inspection|
|REQ-HFPX-TLT-003|The system shall withstand defined low-temperature storage conditions of [TBD] and remain serviceable (bounds TBD).|REQ-HFPX-SYS-006; REQ-HFPX-ENV-005|Inspection|
|REQ-HFPX-TLT-004|Each low-temperature requirement shall be verified by method of [TBD] with criteria TBD (verification TBD).|REQ-HFPX-SYS-006|Inspection|

No temperature, duration, start value, or storage bound is stated or implied; all values are TBD.

## 7. Architecture

Starter allocation (SAD owns authoritative mapping): definition → operating bound plus soak TBD; operability → start aids/protection rules TBD; storage → packaging/GSE provisions TBD. All TBC pending subsystem specs.

## 8. Detailed Design

Not applicable — structure level only. Pre-heat, insulation, lubricant/fuel provisions, and packaging designs live in Vol 03–18 and are TBD.

## 9. Interfaces

Low-temperature interfaces (GSE conditioning, enclosure boundaries, start-aid interfaces) are TBD in Chapter 01.16 and Vol 02 ICDs. No interface value is approved.

## 10. Operational Concept

Requirements apply across CONOPS phases as applicable; phase applicability matrix is TBD. Operations outside defined limits (TBD) are prohibited pending quantified revisions; no operating instruction is given beyond this structuring rule.

## 11. Safety

Cold-induced hazards feed Vol 13 safety analyses (to follow). No definition in this revision is a safety claim; safety credit requires analysed and tested limits via change record.

## 12. Performance

Low-temperature definitions do not quantify performance. Start-time and operability interactions are TBD and owned jointly with performance tiers.

## 13. Verification & Validation

Intended method is Analysis + Test (see table; detail TBD); levels, soak durations, start demonstrations, and pass criteria are TBD in 14.14 and the V&V Plan (Vol 22). No verification credit is claimed at this revision.

## 14. Risks

- Bounds undefined → incompatible subsystem assumptions; mitigation: single TBD-owned tier with CONCEPT status.
- Over-testing to unapproved levels; mitigation: change-controlled quantification only.

## 15. Open Issues

Definition completeness, start/operability rules, storage bounds, and verification method confirmation. RTM seed for TLT-001..004 added with this tranche (Status CONCEPT).

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SYS-006 stability, ENV-002/005, TEN inventory, subsystem inputs, and V&V Plan strategy. Changes propagate by change record.

## 18. Traceability

Parents: REQ-HFPX-SYS-006; REQ-HFPX-ENV-002, REQ-HFPX-ENV-005 (see table). Children: subsystem specs, qualification cases (14.14, Vol 22/23), RTM rows. RTM seed for TLT-001..004 added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Quantification requires new revisions via change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 14.9; all values TBD) |
