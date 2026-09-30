# Pilot Protection

**Document ID:** HFPX-HUM-PRT-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define pilot-protection requirements for HFP-X (Chapter 12.7). This Tranche 6 draft establishes impact/thermal/fire/noise protection-function placeholders and interface placeholders; all values are TBD.

## 2. Scope

Covers pilot protection functions for impact, thermal, fire, and noise effects, plus protection interfaces. Excludes thermal-protection detail (12.8), fire-protection detail (12.9), and safety-case substantiation, which is Vol 13 scope.

## 3. Applicable Documents

- HFPX-SYS-HUM-001 Human Factors Requirements (parent HUM tier)
- Stakeholder need STK-002 (human involvement)
- HSA tier (ID TBD — allocation to follow)
- Vol 30 hooks (TBD — training/evaluation inputs to follow)
- Vol 13 safety (TBD interfaces), HFPX-HUM-ARC-001 (Chapter 12.1)

## 4. Definitions & Acronyms

- HUM: human-factors requirement tier; IDs `REQ-HFPX-HUM-NNN`.
- UPR: pilot-protection requirement tier; IDs `REQ-HFPX-UPR-NNN`; verification TBD.
- TBD/TBC: unknown data; no values invented.

## 5. System Context

Pilot protection refines system-level protection needs into testable placeholders:

```text
STK-002 + HUM tier → UPR-001..004 → suit / station protection detail → Vol 13 analyses → V&V cases
```

No protection level or threshold is approved at this revision.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-UPR-001 | The system shall provide pilot protection functions against defined impact effects (protection functions TBD). | STK-002, REQ-HFPX-HUM-003, HSA tier (ID TBD) | Test |
| REQ-HFPX-UPR-002 | The system shall provide pilot protection functions against defined thermal, fire, and noise effects (protection functions TBD). | STK-002, REQ-HFPX-HUM-003, HSA tier (ID TBD) | Test |
| REQ-HFPX-UPR-003 | Pilot-protection provisions shall interface to defined vehicle and safety provisions (interfaces TBD; Vol 13 coordination to follow). | STK-002, REQ-HFPX-HUM-003, HSA tier (ID TBD) | Inspection |
| REQ-HFPX-UPR-004 | Protection functions shall be verified against defined criteria (criteria TBD; Vol 30 hook TBD). | STK-002, REQ-HFPX-HUM-003, HSA tier (ID TBD) | Test |

All functions, interfaces, and criteria are TBD. No value is approved.

## 7. Architecture

Starter allocation (SAD owns authoritative mapping): UPR-001/002 → suit, helmet, and station protection provisions; UPR-003 → vehicle/safety interfaces (Vol 13); UPR-004 → V&V framework with Vol 30 hooks. All TBC.

## 8. Detailed Design

Not applicable — requirements level only. Materials, constructions, and hardware selection are TBD in follow-on revisions including Chapters 12.8/12.9.

## 9. Interfaces

Protection interfaces (suit/station/vehicle couplings, Vol 13 safety interfaces) are TBD in Vol 02 ICDs and Chapter 12.1 register. No interface value or layout is approved.

## 10. Operational Concept

Protection requirements apply across preparation, flight, emergency, and recovery phases; phase-specific applicability is TBD. Unmanned demonstration precedes any crewed evaluation per safety gating.

## 11. Safety

Protection shortfalls feed Vol 13 safety analyses (FHA/FMEA/FTA, to follow). No UPR requirement confers flight approval; human flight remains gated by tier 01.10 and the Safety Case.

## 12. Performance

No UPR requirement quantifies performance. All protection measures are TBD pending follow-on studies.

## 13. Verification & Validation

Each requirement states its method above as TBD; verification IDs, test conditions, participant criteria, and pass thresholds are TBD in the V&V Plan (Vol 22) with Vol 12/13/30 inputs. No protection credit is claimed at this revision.

## 14. Risks

- Protection functions undefined → late safety findings; mitigation: early UPR placeholders plus Vol 13 coordination.
- Interfaces undefined → integration rework; mitigation: UPR-003 placeholder plus review gates.

## 15. Open Issues

TBD: impact/thermal/fire/noise protection functions, protection interfaces, and verification criteria pending Vol 13, HSA-tier, and Vol 30 inputs.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on STK-002 stability, HUM-tier stability (HFPX-SYS-HUM-001), HSA-tier allocation (TBD), Vol 30 hooks (TBD), Vol 13 safety work, Chapters 12.8/12.9 detail, and V&V Plan cases. Changes propagate by change record.

## 18. Traceability

Parents: STK-002, HUM tier (REQ-HFPX-HUM-003), HSA tier (ID TBD), Vol 30 hooks (TBD) — see table. Children: protection specs, Vol 13 analyses, Chapters 12.8/12.9 detail, V&V cases, RTM rows. RTM seed for UPR-001..004 added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Additions or function changes require new revisions via change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 12.7) |
