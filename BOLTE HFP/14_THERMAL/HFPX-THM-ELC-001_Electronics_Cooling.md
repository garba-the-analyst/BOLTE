# Electronics Cooling

**Document ID:** HFPX-THM-ELC-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X electronics cooling structure for Chapter 14.5. This Tranche 6 draft establishes cooled-item inventory, cooling approaches, and temperature-limit structure with all values TBD; quantified design follows in later tranches.

## 2. Scope

Covers cooled electronics inventory, cooling approaches, and temperature-limit structure. Excludes quantified thermal design, operating instructions, and qualification detail (14.14, Vol 22/23). All values TBD.

## 3. Applicable Documents

- HFPX-SYS-ENV-001 Environmental Requirements (parent REQ-HFPX-SYS-006, ENV tier)
- HFPX-SYS-REQ-001 SyRS (REQ-HFPX-SYS-006 environmental policy)
- Vol 05 avionics/electrical, Vol 06 enclosures (structure only)
- Vol 19.6 modelling framework (to follow)

## 4. Definitions & Acronyms

- TEC: electronics cooling requirement tier; ID `REQ-HFPX-TEC-NNN`; verification: TBD (intended Analysis + Test).
- Cooled item: electronics assembly requiring thermal control; inventory TBD.
- TBD/TBC: unknown data; no values invented.

## 5. System Context

Electronics cooling tier refines SYS-006 and ENV-001 into items, approaches, and limits:

```text
SYS-006 → ENV-001 → TEC-001..004 (items, approaches, limits) → Vol 05/06 enclosure design → Test (14.14, Vol 22/23)
```

Item inventories and limits require subsystem inputs and programme decisions before any value is approved.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-TEC-001|The system shall define cooled electronics items of [TBD] with inventory TBD (identities TBD).|REQ-HFPX-SYS-006; REQ-HFPX-ENV-001|Inspection|
|REQ-HFPX-TEC-002|The system shall apply defined electronics cooling approaches of [TBD] (approaches TBD).|REQ-HFPX-SYS-006; REQ-HFPX-ENV-001|Inspection|
|REQ-HFPX-TEC-003|The system shall operate cooled electronics within defined temperature limits of [TBD] (limits TBD).|REQ-HFPX-SYS-006; REQ-HFPX-ENV-001|Inspection|
|REQ-HFPX-TEC-004|Each electronics cooling requirement shall be verified by method of [TBD] with criteria TBD (verification TBD).|REQ-HFPX-SYS-006|Inspection|

No temperature, heat load, flow rate, or limit is stated or implied; all values are TBD.

## 7. Architecture

Starter allocation (SAD owns authoritative mapping): items → Vol 05 avionics/electrical assemblies TBD; approaches → conduction/convection provisions TBD; limits → zone/enclosure allocation TBD. All TBC pending subsystem specs.

## 8. Detailed Design

Not applicable — structure level only. Heatsinks, airflow paths, and enclosure designs live in Vol 05/06 and are TBD.

## 9. Interfaces

Cooling interfaces (mounting/thermal paths, airflow boundaries, power/thermal co-interfaces with Vol 05) are TBD in Chapter 01.16 and Vol 02 ICDs. No interface value is approved.

## 10. Operational Concept

Requirements apply across CONOPS phases as applicable; phase applicability matrix is TBD. No operating instruction is given in this revision.

## 11. Safety

Electronics over-temperature hazards feed Vol 13 safety analyses (to follow). No limit in this revision is a safety claim; safety credit requires analysed and tested limits via change record.

## 12. Performance

Cooling provisions do not quantify performance. Thermal derating and availability interactions are TBD and owned jointly with Vol 05 tiers.

## 13. Verification & Validation

Intended method is Analysis + Test (see table; detail TBD); thermal models, test conditions, and pass criteria are TBD in 14.14 and the V&V Plan (Vol 22). No verification credit is claimed at this revision.

## 14. Risks

- Items undefined → uncooled assemblies assumed compatible; mitigation: single TBD-owned tier with CONCEPT status.
- Limits assumed without analysis; mitigation: change-controlled quantification only.

## 15. Open Issues

Cooled-item inventory, cooling-approach selection, temperature-limit definition, and verification method confirmation. RTM seed for TEC-001..004 added with this tranche (Status CONCEPT).

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SYS-006 stability, ENV tier, Vol 05/06 inputs, Vol 19.6 models, and 14.14 test thread. Changes propagate by change record.

## 18. Traceability

Parents: REQ-HFPX-SYS-006; REQ-HFPX-ENV-001 (see table). Children: Vol 05/06 cooling designs, test cases (14.14, Vol 22/23), RTM rows. RTM seed for TEC-001..004 added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Quantification requires new revisions via change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 14.5; all values TBD) |
