# Competency Assessment

**Document ID:** HFPX-TRN-CPA-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the structure for HFP-X competency assessment (Chapter 30.11). This Tranche 6 draft establishes structure-only placeholders for assessment criteria, re-assessment, and records; all values are TBD.

## 2. Scope

Covers competency-assessment criteria headings, re-assessment headings, and records headings supporting the training syllabus. Excludes assessment execution, pass/fail decisions, and authorisation, which remain TBD in Vol 26 and follow-on revisions.

## 3. Applicable Documents

- HFPX-SYS-HUM-001 Human Factors Requirements (parent REQ-HFPX-HUM-005 training and competency prerequisites)
- Stakeholder need STK-002 (human involvement)
- Vol 26 (operations / qualification, to follow), Vol 22 (V&V Plan, to follow)
- HFP prompt §§8–10 (requirements format, classification, traceability)

## 4. Definitions & Acronyms

- TCA: competency-assessment requirement tier; ID `REQ-HFPX-TCA-NNN`; verification: Inspection / Demonstration.
- Competency: demonstrated training outcome set; criteria TBD.
- TBD/TBC: unknown data; no values invented; detail deferred to follow-on revisions.

## 5. System Context

Competency assessment structure refines HUM-005 into assessment placeholders:

```text
STK-002 + HUM-005 → TCA-001..004 → Vol 26 qualification detail → V&V cases
```

No competency award or authorisation is implied by this document.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-TCA-001 | The programme shall define the competency-assessment criteria headings supporting the training syllabus (criteria TBD; no executable instruction). | STK-002, HUM-005 | Inspection |
| REQ-HFPX-TCA-002 | The programme shall define the re-assessment headings, including triggers and framework headings (detail TBD). | HUM-005 | Inspection |
| REQ-HFPX-TCA-003 | The programme shall define the competency-records headings, including retention and traceability headings (detail TBD). | HUM-005 | Inspection |
| REQ-HFPX-TCA-004 | The programme shall define hooks to Vol 26 qualification for authorisation interfaces informed by assessment outcomes (detail TBD in Vol 26). | HUM-005 | Inspection + Demonstration |

All assessment criteria, re-assessment provisions, and records provisions are TBD; no hours, ratios, scores, or limits are stated.

## 7. Architecture

Starter allocation (SAD owns authoritative mapping): TCA requirements → training / assessment system + Vol 26 qualification interfaces + records interfaces. All TBC.

## 8. Detailed Design

Not applicable — assessment structure only. Check sheets, scoring rubrics, test items, and record formats are not defined in this revision and remain TBD.

## 9. Interfaces

Interfaces to Vol 26 qualification, Vol 22 V&V, and Vol 30 syllabus chapters are TBD. No interface value or layout is approved.

## 10. Operational Concept

Competency assessment structure applies across initial, recurrent, and re-assessment contexts; context-specific applicability is TBD. This document states structure only and provides no executable assessment instruction.

## 11. Safety

Assessment-structure gaps feed Vol 13 safety analyses (to follow). No TCA requirement confers competency or flight approval; safety gating remains via tier 01.10 and the Safety Case.

## 12. Performance

No TCA requirement quantifies performance. All thresholds, intervals, and pass criteria are TBD pending follow-on study.

## 13. Verification & Validation

Each requirement states its method above; verification IDs, scenario sets, assessor criteria, and pass thresholds are TBD in the V&V Plan (Vol 22) with Vol 26/30 inputs. No assessment credit is claimed at this revision.

## 14. Risks

- Criteria deferred → inconsistent assessment outcomes; mitigation: structure placeholders plus Vol 26 qualification gates.
- Records undefined → loss of competency traceability; mitigation: explicit TBD records headings reviewed at SRR.

## 15. Open Issues

TBC: assessment criteria, re-assessment provisions, records provisions, and Vol 26 hooks pending Vol 22/26/30 work.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on STK-002 stability, HUM-005 policy, Vol 22/26 detail work, and V&V Plan cases. Changes propagate by change record.

## 18. Traceability

Parents: STK-002, HUM-005 (see table). Children: Vol 26 qualification criteria, V&V cases, RTM rows. RTM seed for TCA-001..004 added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Detail additions require new revisions via change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 30.11) |
