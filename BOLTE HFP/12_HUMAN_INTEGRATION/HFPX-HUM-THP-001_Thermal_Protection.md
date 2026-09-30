# Thermal Protection

**Document ID:** HFPX-HUM-THP-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define thermal-protection requirements for HFP-X pilot integration (Chapter 12.8). This Tranche 6 draft establishes thermal-environment, protective-performance, and monitoring placeholders; all values are TBD.

## 2. Scope

Covers pilot thermal environment definition, thermal protective performance, and thermal monitoring provisions. Excludes fire-protection detail (12.9), pilot-protection overview (12.7), and thermal-sources design, which is Vol 14 scope including Chapter 14.4.

## 3. Applicable Documents

- HFPX-SYS-HUM-001 Human Factors Requirements (parent HUM tier)
- Stakeholder need STK-002 (human involvement)
- HSA tier (ID TBD — allocation to follow)
- Vol 30 hooks (TBD — evaluation inputs to follow)
- Vol 14 thermal environment including Chapter 14.4 (TBD), HFPX-HUM-PRT-001 (Chapter 12.7)

## 4. Definitions & Acronyms

- HUM: human-factors requirement tier; IDs `REQ-HFPX-HUM-NNN`.
- UTP: thermal-protection requirement tier; IDs `REQ-HFPX-UTP-NNN`; verification TBD.
- TBD/TBC: unknown data; no values invented.

## 5. System Context

Thermal protection refines system-level protection needs into testable placeholders:

```text
STK-002 + HUM tier → UTP-001..004 → suit / station thermal detail (Vol 14.4) → V&V cases
```

No thermal level, threshold, or duration is approved at this revision.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-UTP-001 | The system shall define the pilot thermal environment across defined phases and conditions (thermal environment TBD; Vol 14.4 detail to follow). | STK-002, REQ-HFPX-HUM-003, HSA tier (ID TBD) | Inspection |
| REQ-HFPX-UTP-002 | The system shall provide thermal protective performance within defined bounds (protective performance TBD). | STK-002, REQ-HFPX-HUM-003, HSA tier (ID TBD) | Test |
| REQ-HFPX-UTP-003 | The system shall provide thermal monitoring provisions with defined annunciation (monitoring provisions TBD). | STK-002, REQ-HFPX-HUM-004, HSA tier (ID TBD) | Demonstration |
| REQ-HFPX-UTP-004 | Thermal-protection provisions shall be verified against defined criteria (criteria TBD; Vol 30 hook TBD). | STK-002, REQ-HFPX-HUM-003, HSA tier (ID TBD) | Test |

All environments, performance bounds, monitoring provisions, and criteria are TBD. No value is approved.

## 7. Architecture

Starter allocation (SAD owns authoritative mapping): UTP-001 → Vol 14.4 environment definition; UTP-002 → suit/station thermal provisions; UTP-003 → monitoring/avionics; UTP-004 → V&V framework with Vol 30 hooks. All TBC.

## 8. Detailed Design

Not applicable — requirements level only. Materials, insulation/cooling provisions, sensor selection, and hardware detail are TBD in follow-on revisions.

## 9. Interfaces

Thermal interfaces (suit/station/vehicle thermal couplings, monitoring signals) are TBD in Vol 02 ICDs, Vol 14.4, and Chapter 12.1 register. No interface value or layout is approved.

## 10. Operational Concept

Thermal requirements apply across preparation, flight, and recovery phases; phase-specific applicability is TBD. Unmanned demonstration precedes any crewed evaluation per safety gating.

## 11. Safety

Thermal-protection shortfalls and monitoring failures feed Vol 13 safety analyses (to follow). No UTP requirement confers flight approval; human flight remains gated by tier 01.10 and the Safety Case.

## 12. Performance

No UTP requirement quantifies performance. All thermal measures are TBD pending Vol 14.4 and follow-on studies.

## 13. Verification & Validation

Each requirement states its method above as TBD; verification IDs, test conditions, participant criteria, and pass thresholds are TBD in the V&V Plan (Vol 22) with Vol 12/14/30 inputs. No thermal credit is claimed at this revision.

## 14. Risks

- Thermal environment undefined → protection mis-sizing; mitigation: early UTP-001 placeholder plus Vol 14.4 coordination.
- Monitoring undefined → undetected exceedance; mitigation: UTP-003 placeholder plus avionics coordination.

## 15. Open Issues

TBD: thermal environment, protective performance bounds, monitoring provisions, and verification criteria pending Vol 14.4, HSA-tier, and Vol 30 inputs.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on STK-002 stability, HUM-tier stability (HFPX-SYS-HUM-001), HSA-tier allocation (TBD), Vol 30 hooks (TBD), Vol 14.4 environment work, Chapter 12.7 protection overview, and V&V Plan cases. Changes propagate by change record.

## 18. Traceability

Parents: STK-002, HUM tier (REQ-HFPX-HUM-003, REQ-HFPX-HUM-004), HSA tier (ID TBD), Vol 30 hooks (TBD) — see table. Children: thermal specs, Vol 14.4 environment specs, monitoring specs, V&V cases, RTM rows. RTM seed for UTP-001..004 added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Additions or bound changes require new revisions via change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 12.8) |
