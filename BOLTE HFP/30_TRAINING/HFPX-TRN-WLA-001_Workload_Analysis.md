# Workload Analysis

**Document ID:** HFPX-TRN-WLA-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the structure for HFP-X workload analysis supporting training (Chapter 30.7). This Tranche 6 draft establishes structure-only placeholders for methods, task coverage, and design feedback; all values and thresholds are TBD.

## 2. Scope

Covers workload-analysis method headings, task-set headings, limit headings, and design-feedback headings informing the training syllabus. Excludes workload measurement execution, limit-setting, and design decisions, which remain TBD in Vol 10/30 and follow-on revisions.

## 3. Applicable Documents

- HFPX-SYS-HUM-001 Human Factors Requirements (parent REQ-HFPX-HUM-001 workload provisions)
- Stakeholder need STK-002 (human involvement)
- Vol 10 (HMI / workload detail, to follow), Vol 26 (operations task detail, to follow)
- HFP prompt §§8–10 (requirements format, classification, traceability)

## 4. Definitions & Acronyms

- TWA: workload-analysis requirement tier; ID `REQ-HFPX-TWA-NNN`; verification: Inspection / Analysis.
- Workload: operator demand across nominal and defined off-nominal tasks; scales and limits TBD.
- TBD/TBC: unknown data; no values invented; detail deferred to follow-on revisions.

## 5. System Context

Workload analysis structure refines HUM-001 into analysis placeholders:

```text
STK-002 + HUM-001 → TWA-001..004 → Vol 10/30 detail → design feedback + V&V cases
```

No workload limit or design change is approved by this document.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-TWA-001 | The programme shall define the workload-analysis method headings supporting training, including task coverage headings (methods and task set TBD). | STK-002, HUM-001 | Inspection |
| REQ-HFPX-TWA-002 | The programme shall define the workload limit headings to be populated by analysis (limits TBD; no values stated). | HUM-001 | Inspection + Analysis |
| REQ-HFPX-TWA-003 | The programme shall define the design-feedback headings by which workload findings inform HMI and syllabus structure (feedback mechanism TBD). | HUM-001, HUM-002 | Inspection |
| REQ-HFPX-TWA-004 | The programme shall define the assessment headings by which workload considerations enter training assessment (assessment detail TBD). | HUM-005 | Inspection + Demonstration |

All methods, task sets, limits, and assessment criteria are TBD; no hours, ratios, scores, or limits are stated.

## 7. Architecture

Starter allocation (SAD owns authoritative mapping): TWA requirements → analysis function + training system + HMI / operations interfaces. All TBC.

## 8. Detailed Design

Not applicable — analysis structure only. Scales, questionnaires, task timelines, and data sets are not defined in this revision and remain TBD.

## 9. Interfaces

Interfaces to Vol 10 HMI design, Vol 26 task definitions, and Vol 22 V&V methods are TBD. No interface value or layout is approved.

## 10. Operational Concept

Workload analysis structure applies across preparation, flight, and recovery task contexts; task-specific applicability is TBD. This document states structure only and provides no executable instruction.

## 11. Safety

Analysis gaps feed Vol 13 safety analyses (to follow). No TWA requirement sets a limit or confers approval; safety gating remains via tier 01.10 and the Safety Case.

## 12. Performance

No TWA requirement quantifies performance. All workload scales, thresholds, and pass criteria are TBD pending follow-on study.

## 13. Verification & Validation

Each requirement states its method above; verification IDs, task scenarios, participant criteria, and pass thresholds are TBD in the V&V Plan (Vol 22) with Vol 10/30 inputs. No workload credit is claimed at this revision.

## 14. Risks

- Methods deferred → incomparable workload findings; mitigation: structure placeholders reviewed at SRR.
- Limits undefined → unbounded design expectations; mitigation: explicit TBD limit headings plus Vol 10 analysis gates.

## 15. Open Issues

TBC: analysis methods, task set, limit headings, and design-feedback mechanism pending Vol 10/26/30 work.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on STK-002 stability, HUM-001 policy, Vol 10/26 detail work, and V&V Plan cases. Changes propagate by change record.

## 18. Traceability

Parents: STK-002, HUM-001/002/005 (see table). Children: Vol 10/30 workload detail, design-feedback records, V&V cases, RTM rows. RTM seed for TWA-001..004 added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Detail additions require new revisions via change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 30.7) |
