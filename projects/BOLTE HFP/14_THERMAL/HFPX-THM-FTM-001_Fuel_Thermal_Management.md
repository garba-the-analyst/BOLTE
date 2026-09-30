# Fuel Thermal Management

**Document ID:** HFPX-THM-FTM-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X fuel thermal management structure for Chapter 14.6. This Tranche 6 draft establishes fuel temperature limits, heating/cooling drivers, and sensor-interface structure with all values TBD; quantified design follows in later tranches.

## 2. Scope

Covers fuel temperature-limit structure, heating/cooling drivers, and sensor-interface hooks. Excludes quantified fuel-system design, operating instructions, and qualification detail (14.14, Vol 22/23). All values TBD.

## 3. Applicable Documents

- HFPX-SYS-ENV-001 Environmental Requirements (parent REQ-HFPX-SYS-006, ENV tier)
- HFPX-SYS-REQ-001 SyRS (REQ-HFPX-SYS-006 environmental policy)
- Vol 05.12 fuel sensing, Vol 04/05 fuel system provisions (structure only)

## 4. Definitions & Acronyms

- TFM: fuel thermal management requirement tier; ID `REQ-HFPX-TFM-NNN`; verification: TBD (intended Analysis + Test).
- Heating/cooling driver: condition or source affecting fuel temperature; drivers TBD.
- TBD/TBC: unknown data; no values invented.

## 5. System Context

Fuel thermal tier refines SYS-006 and ENV-001/002 into limits, drivers, and sensing:

```text
SYS-006 → ENV-001/002 → TFM-001..004 (limits, drivers, sensing) → Vol 04/05 fuel design → Test (14.14, Vol 22/23)
```

Limits and drivers require fuel-system inputs and programme decisions before any value is approved.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-TFM-001|The system shall maintain fuel within defined temperature limits of [TBD] (limits TBD).|REQ-HFPX-SYS-006; REQ-HFPX-ENV-001, REQ-HFPX-ENV-002|Inspection|
|REQ-HFPX-TFM-002|The system shall define fuel heating and cooling drivers of [TBD] (drivers TBD).|REQ-HFPX-SYS-006|Inspection|
|REQ-HFPX-TFM-003|The system shall provide fuel-temperature sensor interfaces of [TBD] with hooks to Vol 05.12 TBD (detail TBD).|REQ-HFPX-SYS-006|Inspection|
|REQ-HFPX-TFM-004|Each fuel thermal management requirement shall be verified by method of [TBD] with criteria TBD (verification TBD).|REQ-HFPX-SYS-006|Inspection|

No temperature, heat load, flow rate, or limit is stated or implied; all values are TBD.

## 7. Architecture

Starter allocation (SAD owns authoritative mapping): limits → fuel storage/delivery zones TBD; drivers → ambient/engine-heat/operational contributors TBD; sensing → Vol 05.12 interface TBD. All TBC pending subsystem specs.

## 8. Detailed Design

Not applicable — structure level only. Tank insulation, routing, heating/cooling provisions, and sensor selections live in Vol 04/05 and are TBD.

## 9. Interfaces

Fuel-thermal interfaces (tank/bay thermal boundaries, Vol 05.12 sensing interfaces, Vol 04 propulsion fuel interfaces) are TBD in Chapter 01.16 and Vol 02 ICDs. No interface value is approved.

## 10. Operational Concept

Requirements apply across CONOPS phases as applicable; phase applicability matrix is TBD. No operating instruction is given in this revision.

## 11. Safety

Fuel-temperature hazards feed Vol 13 safety analyses (to follow). No limit in this revision is a safety claim; safety credit requires analysed and tested limits via change record.

## 12. Performance

Fuel thermal limits do not quantify performance. Fuel-condition and engine-performance interactions are TBD and owned jointly with Vol 04/05 tiers.

## 13. Verification & Validation

Intended method is Analysis + Test (see table; detail TBD); test conditions and pass criteria are TBD in 14.14 and the V&V Plan (Vol 22). No verification credit is claimed at this revision.

## 14. Risks

- Limits undefined → incompatible fuel-system assumptions; mitigation: single TBD-owned tier with CONCEPT status.
- Sensing assumed without defined interfaces; mitigation: change-controlled Vol 05.12 hooks only.

## 15. Open Issues

Limit definition, driver inventory, Vol 05.12 sensor-interface mapping, and verification method confirmation. RTM seed for TFM-001..004 added with this tranche (Status CONCEPT).

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SYS-006 stability, ENV tier, Vol 04/05 fuel-system inputs, Vol 05.12 sensing, and 14.14 test thread. Changes propagate by change record.

## 18. Traceability

Parents: REQ-HFPX-SYS-006; REQ-HFPX-ENV-001, REQ-HFPX-ENV-002 (see table). Children: Vol 04/05 fuel thermal designs, test cases (14.14, Vol 22/23), RTM rows. RTM seed for TFM-001..004 added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Quantification requires new revisions via change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 14.6; all values TBD) |
