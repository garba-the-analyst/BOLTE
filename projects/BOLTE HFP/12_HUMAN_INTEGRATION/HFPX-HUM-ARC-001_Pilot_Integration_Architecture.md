# Pilot Integration Architecture

**Document ID:** HFPX-HUM-ARC-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the pilot-vehicle integration architecture for HFP-X (Chapter 12.1). This Tranche 6 draft establishes the integration partition, reference configuration, and interface-register placeholders; all values and details are TBD.

## 2. Scope

Covers the pilot-vehicle integration partition, prone/semi-prone configuration definition, and the pilot-integration interface register. Excludes anthropometry detail (12.2), restraint design (12.3), ergonomics detail (12.5), and HSI programme detail (12.14), which are owned by their respective chapters.

## 3. Applicable Documents

- HFPX-SYS-HUM-001 Human Factors Requirements (parent HUM tier)
- Stakeholder need STK-002 (human involvement)
- HSA tier (ID TBD — allocation to follow)
- Vol 30 hooks (TBD — training/HSI inputs to follow)
- Vol 02 ICDs (TBD), Vol 03 airframe interfaces (TBD)

## 4. Definitions & Acronyms

- HUM: human-factors requirement tier; IDs `REQ-HFPX-HUM-NNN`.
- UAR: pilot-integration-architecture requirement tier; IDs `REQ-HFPX-UAR-NNN`; verification: Review / Demonstration.
- TBD/TBC: unknown data; no values invented.
- ICD: Interface Control Document.

## 5. System Context

Pilot integration refines system-level human-factors requirements into an architecture placeholder:

```text
STK-002 + HUM tier → UAR-001..005 → Vol 03 / Vol 07 / Vol 10 / Vol 12 detail → Review + human-factors evaluation
```

No configuration or interface is approved at this revision.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-UAR-001 | The pilot-vehicle integration architecture shall define the pilot-vehicle integration partition, including pilot, suit, restraint, and vehicle responsibilities (partition TBD). | STK-002, REQ-HFPX-HUM-003, HSA tier (ID TBD) | Inspection + Demonstration (human-factors evaluation; details TBD) |
| REQ-HFPX-UAR-002 | The architecture shall define the reference pilot configuration, including prone/semi-prone arrangement (configuration TBD). | STK-002, REQ-HFPX-HUM-003, HSA tier (ID TBD) | Inspection + Demonstration (human-factors evaluation; details TBD) |
| REQ-HFPX-UAR-003 | The architecture shall maintain a pilot-integration interface register covering suit, restraint, controls, and vehicle interfaces (register TBD). | STK-002, REQ-HFPX-HUM-003, HSA tier (ID TBD) | Inspection (register completeness; details TBD) |
| REQ-HFPX-UAR-004 | The architecture shall allocate pilot-integration functions to subsystems with traceability to HUM-tier parents (allocation TBD). | STK-002, REQ-HFPX-HUM-001, HSA tier (ID TBD) | Inspection (allocation completeness; details TBD) |
| REQ-HFPX-UAR-005 | The pilot-vehicle integration architecture shall be subject to human-factors evaluation against defined integration criteria (criteria TBD; Vol 30 hook TBD). | STK-002, REQ-HFPX-HUM-001, HSA tier (ID TBD) | Inspection + Demonstration (human-factors evaluation; details TBD) |

All partitions, configurations, registers, and criteria are TBD. No value is approved.

## 7. Architecture

Starter allocation (SAD owns authoritative mapping): UAR-001/004 → system architecture and subsystem allocation; UAR-002 → airframe/suit/restraint configuration; UAR-003 → Vol 02 ICDs; UAR-005 → HSI/human-factors evaluation framework with Vol 30 hooks. All TBC.

## 8. Detailed Design

Not applicable — architecture level only. Geometry, layouts, hardware selection, and ICD detail are TBD in follow-on revisions.

## 9. Interfaces

Pilot-integration interfaces (suit couplings, restraint attachments, control/display linkages, vehicle structural interfaces) are TBD in Chapter 12.1 interface register and Vol 02 ICDs. No interface value or layout is approved.

## 10. Operational Concept

Pilot-integration architecture applies across preparation, flight, and recovery phases; phase-specific applicability is TBD. Unmanned demonstration precedes any crewed evaluation per safety gating.

## 11. Safety

Pilot-integration failures and misallocations feed Vol 13 safety analyses (to follow). No UAR requirement confers flight approval; human flight remains gated by tier 01.10 and the Safety Case.

## 12. Performance

No UAR requirement quantifies performance. All integration performance aspects are TBD pending follow-on studies.

## 13. Verification & Validation

Each requirement states its method above; verification IDs, review criteria, evaluation scenarios, participant criteria, and pass thresholds are TBD in the V&V Plan (Vol 22) with Vol 12/30 inputs. No integration credit is claimed at this revision.

## 14. Risks

- Integration partition undefined → late discovery of responsibility gaps; mitigation: early register placeholder plus review gates.
- Reference configuration undecided → rework across suit/restraint/controls; mitigation: UAR-002 placeholder plus architecture review.

## 15. Open Issues

TBD: integration partition, prone/semi-prone configuration decision, interface-register contents, allocation mapping, and evaluation criteria pending Vol 03/07/10/30 inputs.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on STK-002 stability, HUM-tier stability (HFPX-SYS-HUM-001), HSA-tier allocation (TBD), Vol 30 hooks (TBD), Vol 02/03 interface work, and V&V Plan cases. Changes propagate by change record.

## 18. Traceability

Parents: STK-002, HUM tier (REQ-HFPX-HUM-001, REQ-HFPX-HUM-003), HSA tier (ID TBD), Vol 30 hooks (TBD) — see table. Children: subsystem integration specs, Vol 02 ICDs, V&V cases, RTM rows. RTM seed for UAR-001..005 added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Additions or allocation changes require new revisions via change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 12.1) |
