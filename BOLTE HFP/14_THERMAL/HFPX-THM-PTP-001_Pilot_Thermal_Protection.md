# Pilot Thermal Protection

**Document ID:** HFPX-THM-PTP-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X pilot thermal protection structure for Chapter 14.4. This Tranche 6 draft establishes pilot thermal environment, protective performance, and monitoring structure with all values TBD; quantified design follows in later tranches.

## 2. Scope

Covers pilot thermal environment definition, protective performance structure, and monitoring hooks. Excludes quantified physiological limits, operating instructions, and qualification detail (14.14, Vol 22/23). All values TBD.

## 3. Applicable Documents

- HFPX-SYS-ENV-001 Environmental Requirements (parent REQ-HFPX-SYS-006, ENV tier)
- HFPX-SYS-REQ-001 SyRS (REQ-HFPX-SYS-006 environmental policy)
- Vol 12.8 pilot protection, Vol 06 airframe provisions (structure only)
- Vol 13 safety analyses (to follow)

## 4. Definitions & Acronyms

- TTP: pilot thermal protection requirement tier; ID `REQ-HFPX-TPT-NNN`; verification: TBD (intended Analysis + Test).
- Pilot thermal environment: cockpit/station thermal conditions affecting the pilot; values TBD.
- TBD/TBC: unknown data; no values invented.

## 5. System Context

Pilot protection tier refines SYS-006 and the ENV tier into environment, performance, and monitoring:

```text
SYS-006 → ENV-001/002 → TTP-001..004 (environment, performance, monitoring) → Vol 12.8 / Vol 06 design → Test (14.14, Vol 22/23)
```

Environment bounds and protective performance require subsystem inputs and programme decisions before any value is approved.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-TPT-001 | The system shall define the pilot thermal environment of [TBD] with conditions and phases TBD (values TBD). | REQ-HFPX-SYS-006; REQ-HFPX-ENV-001, REQ-HFPX-ENV-002 | Inspection |
| REQ-HFPX-TPT-002 | The system shall provide pilot thermal protective performance of [TBD] with interfaces to Vol 12.8 TBD (performance TBD). | REQ-HFPX-SYS-006; REQ-HFPX-ENV-001 | Test |
| REQ-HFPX-TPT-003 | The system shall provide pilot thermal monitoring of [TBD] with parameters and thresholds TBD (detail TBD). | REQ-HFPX-SYS-006 | Inspection |
| REQ-HFPX-TPT-004 | Each pilot thermal protection requirement shall be verified by method of [TBD] with criteria TBD (verification TBD). | REQ-HFPX-SYS-006 | Test |

No temperature, heat load, flow rate, or limit is stated or implied; all values are TBD.

## 7. Architecture

Starter allocation (SAD owns authoritative mapping): environment → station thermal zones TBD; protection → Vol 12.8 garments/enclosures/conditioning provisions TBD; monitoring → sensing/display hooks TBD. All TBC pending subsystem specs.

## 8. Detailed Design

Not applicable — structure level only. Protective equipment, conditioning hardware, and sensor selections live in Vol 06/12 and are TBD.

## 9. Interfaces

Pilot thermal interfaces (Vol 12.8 protection boundaries, Vol 06 conditioning interfaces, monitoring/display interfaces) are TBD in Chapter 01.16 and Vol 02 ICDs. No interface value is approved.

## 10. Operational Concept

Requirements apply across CONOPS phases as applicable; phase applicability matrix is TBD. No operating instruction is given in this revision.

## 11. Safety

Pilot thermal hazards feed Vol 13 safety analyses (to follow). No protective performance in this revision is a safety claim; safety credit requires analysed and tested limits via change record.

## 12. Performance

Pilot thermal provisions do not quantify performance. Endurance and operability interactions under thermal stress are TBD and owned jointly with Vol 12 tiers.

## 13. Verification & Validation

Intended method is Analysis + Test (see table; detail TBD); environment definitions, performance criteria, and monitoring thresholds are TBD in 14.14 and the V&V Plan (Vol 22). No verification credit is claimed at this revision.

## 14. Risks

- Environment undefined → incompatible protection assumptions; mitigation: single TBD-owned tier with CONCEPT status.
- Monitoring assumed without defined thresholds; mitigation: change-controlled quantification only.

## 15. Open Issues

Environment definition, Vol 12.8 protective performance mapping, monitoring parameter set, and verification method confirmation. RTM seed for TTP-001..004 added with this tranche (Status CONCEPT).

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SYS-006 stability, ENV tier, Vol 06/12 inputs, Vol 13 safety analyses, and 14.14 test thread. Changes propagate by change record.

## 18. Traceability

Parents: REQ-HFPX-SYS-006; REQ-HFPX-ENV-001, REQ-HFPX-ENV-002 (see table). Children: Vol 12.8 / Vol 06 protective designs, test cases (14.14, Vol 22/23), RTM rows. RTM seed for TTP-001..004 added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Quantification requires new revisions via change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 14.4; all values TBD) |
