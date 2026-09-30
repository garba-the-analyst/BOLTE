# Situational Awareness

**Document ID:** HFPX-TRN-SAA-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the syllabus structure for HFP-X situational-awareness training (Chapter 30.9). This Tranche 6 draft establishes structure-only placeholders for requirements, HMI hooks, and assessment; all content values are TBD.

## 2. Scope

Covers situational-awareness training requirement headings, HMI hooks to Vol 10, and assessment headings. Excludes executable instructional content, HMI design, and assessment decisions, which remain TBD in Vol 10 and follow-on revisions.

## 3. Applicable Documents

- HFPX-SYS-HUM-001 Human Factors Requirements (parent REQ-HFPX-HUM-002 HMI and REQ-HFPX-HUM-005 training prerequisites)
- Stakeholder needs STK-002 (human involvement), STK-007 (operator interfaces)
- Vol 10 (HMI / helmet detail, to follow), Vol 26 (operations, to follow)
- HFP prompt §§8–10 (requirements format, classification, traceability)

## 4. Definitions & Acronyms

- TSA: situational-awareness-training requirement tier; ID `REQ-HFPX-TSA-NNN`; verification: Inspection / Demonstration.
- Syllabus structure: objectives, methods, and assessment headings only; all entries TBD.
- TBD/TBC: unknown data; no values invented; detail deferred to follow-on revisions.

## 5. System Context

Situational-awareness training structure refines HUM-002 and HUM-005 into syllabus placeholders:

```text
STK-002/007 + HUM-002/005 → TSA-001..004 → Vol 10 HMI detail → V&V cases
```

No HMI approval or qualification is implied by this document.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-TSA-001 | The programme shall define the situational-awareness training requirement headings within the syllabus structure (requirements TBD; no executable instruction). | STK-002, HUM-005 | Inspection |
| REQ-HFPX-TSA-002 | The programme shall define hooks to Vol 10 HMI provisions informing situational-awareness coverage (HMI detail TBD in Vol 10). | HUM-002 | Inspection |
| REQ-HFPX-TSA-003 | The programme shall define the methods framework headings for situational-awareness training (methods detail TBD). | HUM-005 | Inspection |
| REQ-HFPX-TSA-004 | The programme shall define the assessment framework headings for situational-awareness training (assessment criteria TBD). | HUM-005 | Inspection + Demonstration |

All requirements, HMI hooks, methods, and assessment criteria are TBD; no hours, ratios, scores, or limits are stated.

## 7. Architecture

Starter allocation (SAD owns authoritative mapping): TSA requirements → training system + Vol 10 HMI interfaces + operations interfaces. All TBC.

## 8. Detailed Design

Not applicable — syllabus structure only. Display symbology, scenario content, and instructional sequences are not defined in this revision and remain TBD.

## 9. Interfaces

Interfaces to Vol 10 HMI/helmet provisions, simulator provision (Vol 30.4), and Vol 26 operations are TBD. No interface value or layout is approved.

## 10. Operational Concept

Situational-awareness training structure applies across preparation, flight, and recovery contexts; phase-specific applicability is TBD. This document states structure only and provides no executable instruction.

## 11. Safety

Training-structure gaps feed Vol 13 safety analyses (to follow). No TSA requirement confers qualification or flight approval; safety gating remains via tier 01.10 and the Safety Case.

## 12. Performance

No TSA requirement quantifies performance. All durations and pass criteria are TBD pending follow-on study.

## 13. Verification & Validation

Each requirement states its method above; verification IDs, scenario sets, participant criteria, and pass thresholds are TBD in the V&V Plan (Vol 22) with Vol 10/30 inputs. No training credit is claimed at this revision.

## 14. Risks

- Requirements deferred → late discovery of coverage gaps; mitigation: structure placeholders plus Vol 10 hooks.
- Assessment undefined → unverifiable awareness outcomes; mitigation: explicit TBD assessment headings reviewed at SRR.

## 15. Open Issues

TBC: training requirements, HMI hooks to Vol 10, methods, and assessment framework pending Vol 10/30 work.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on STK-002/007 stability, HUM-002/005 policy, Vol 10/26 detail work, and V&V Plan cases. Changes propagate by change record.

## 18. Traceability

Parents: STK-002/007, HUM-002/005 (see table). Children: Vol 10 HMI training detail, V&V cases, RTM rows. RTM seed for TSA-001..004 added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Detail additions require new revisions via change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 30.9) |
