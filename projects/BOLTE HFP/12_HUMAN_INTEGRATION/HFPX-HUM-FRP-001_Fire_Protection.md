# Fire Protection

**Document ID:** HFPX-HUM-FRP-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define fire-protection requirements for HFP-X pilot integration (Chapter 12.9). This Tranche 6 draft establishes fire-threat, protective-performance, and escape-interface placeholders; all values are TBD.

## 2. Scope

Covers pilot fire-threat inventory, fire protective performance, and escape-interface provisions. Excludes thermal-protection detail (12.8), pilot-protection overview (12.7), and fire-safety substantiation, which is Vol 13 scope including Chapter 13.15.

## 3. Applicable Documents

- HFPX-SYS-HUM-001 Human Factors Requirements (parent HUM tier)
- Stakeholder need STK-002 (human involvement)
- HSA tier (ID TBD — allocation to follow)
- Vol 30 hooks (TBD — training/evaluation inputs to follow)
- Vol 13 fire safety including Chapter 13.15 (TBD), HFPX-HUM-PRT-001 (Chapter 12.7)

## 4. Definitions & Acronyms

- HUM: human-factors requirement tier; IDs `REQ-HFPX-HUM-NNN`.
- UFP: fire-protection requirement tier; IDs `REQ-HFPX-UFP-NNN`; verification TBD.
- TBD/TBC: unknown data; no values invented.

## 5. System Context

Fire protection refines system-level protection needs into testable placeholders:

```text
STK-002 + HUM tier → UFP-001..004 → suit / station fire detail (Vol 13.15) → V&V cases
```

No fire-threat level, performance bound, or duration is approved at this revision.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-UFP-001 | The system shall define the pilot fire-threat inventory across defined phases and conditions (fire-threat inventory TBD; Vol 13.15 detail to follow). | STK-002, REQ-HFPX-HUM-003, HSA tier (ID TBD) | Inspection |
| REQ-HFPX-UFP-002 | The system shall provide fire protective performance within defined bounds (protective performance TBD). | STK-002, REQ-HFPX-HUM-003, HSA tier (ID TBD) | Test |
| REQ-HFPX-UFP-003 | The system shall provide escape-interface provisions supporting pilot escape under defined fire conditions (escape interface TBD). | STK-002, REQ-HFPX-HUM-003, HSA tier (ID TBD) | Inspection |
| REQ-HFPX-UFP-004 | Fire-protection provisions shall be verified against defined criteria (criteria TBD; Vol 30 hook TBD). | STK-002, REQ-HFPX-HUM-003, HSA tier (ID TBD) | Test |

All threats, performance bounds, interfaces, and criteria are TBD. No value is approved.

## 7. Architecture

Starter allocation (SAD owns authoritative mapping): UFP-001 → Vol 13.15 threat definition; UFP-002 → suit/station fire provisions; UFP-003 → escape/egress provisions; UFP-004 → V&V framework with Vol 30 hooks. All TBC.

## 8. Detailed Design

Not applicable — requirements level only. Materials, barriers, extinguishants, and escape hardware are TBD in follow-on revisions.

## 9. Interfaces

Fire interfaces (suit/station/vehicle fire provisions, escape linkages) are TBD in Vol 02 ICDs, Vol 13.15, and Chapter 12.1 register. No interface value or layout is approved.

## 10. Operational Concept

Fire requirements apply across preparation, flight, emergency, and recovery phases; phase-specific applicability is TBD. Unmanned demonstration precedes any crewed evaluation per safety gating.

## 11. Safety

Fire-protection shortfalls and escape failures feed Vol 13 safety analyses (to follow). No UFP requirement confers flight approval; human flight remains gated by tier 01.10 and the Safety Case.

## 12. Performance

No UFP requirement quantifies performance. All fire-related measures are TBD pending Vol 13.15 and follow-on studies.

## 13. Verification & Validation

Each requirement states its method above as TBD; verification IDs, test conditions, participant criteria, and pass thresholds are TBD in the V&V Plan (Vol 22) with Vol 12/13/30 inputs. No fire credit is claimed at this revision.

## 14. Risks

- Fire-threat inventory undefined → protection mis-sizing; mitigation: early UFP-001 placeholder plus Vol 13.15 coordination.
- Escape interface undefined → egress failure under fire; mitigation: UFP-003 placeholder plus review gates.

## 15. Open Issues

TBD: fire-threat inventory, protective performance bounds, escape interface, and verification criteria pending Vol 13.15, HSA-tier, and Vol 30 inputs.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on STK-002 stability, HUM-tier stability (HFPX-SYS-HUM-001), HSA-tier allocation (TBD), Vol 30 hooks (TBD), Vol 13.15 fire work, Chapter 12.7 protection overview, and V&V Plan cases. Changes propagate by change record.

## 18. Traceability

Parents: STK-002, HUM tier (REQ-HFPX-HUM-003), HSA tier (ID TBD), Vol 30 hooks (TBD) — see table. Children: fire specs, Vol 13.15 threat specs, escape specs, V&V cases, RTM rows. RTM seed for UFP-001..004 added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Additions or bound changes require new revisions via change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 12.9) |
