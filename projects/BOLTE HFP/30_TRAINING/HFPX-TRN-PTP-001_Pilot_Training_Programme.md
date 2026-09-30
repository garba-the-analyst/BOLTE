# Pilot Training Programme

**Document ID:** HFPX-TRN-PTP-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the syllabus structure for the HFP-X pilot training programme (Chapter 30.1). This Tranche 6 draft establishes structure-only placeholders for objectives, phases, methods, and assessment; all content values are TBD.

## 2. Scope

Covers the structure of pilot training syllabus placeholders including phases (including simulator), qualification hooks, and unmanned-first alignment. Excludes executable flight-training instructions, detailed curricula, simulator requirements (Vol 30.4), and qualification decisions, which remain TBD in Vol 26.3 and follow-on revisions.

## 3. Applicable Documents

- HFPX-SYS-HUM-001 Human Factors Requirements (parent REQ-HFPX-HUM-005 training and competency prerequisites)
- Stakeholder need STK-002 (human involvement)
- Vol 12 (life support / occupant interfaces, to follow), Vol 26.3 (qualification, to follow)
- HFP prompt §§8–10 (requirements format, classification, traceability)

## 4. Definitions & Acronyms

- TTP: pilot-training-programme requirement tier; ID `REQ-HFPX-TTP-NNN`; verification: Inspection / Demonstration / Analysis.
- Syllabus structure: objectives, phases, methods, and assessment headings only; all entries TBD.
- TBD/TBC: unknown data; no values invented; detail deferred to follow-on revisions.
- Unmanned-first: sequencing principle whereby unmanned demonstration precedes any crewed evaluation; applicability TBD.

## 5. System Context

Pilot training structure refines HUM-005 into syllabus placeholders:

```text
STK-002 + HUM-005 → TTP-001..005 → Vol 26.3 qualification → V&V cases
```

No human-flight approval is implied by this document; human flight remains gated by tier 01.10.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-TTP-001 | The programme shall define the pilot training syllabus structure with objectives, phases, methods, and assessment headings (all content TBD; no executable instruction). | STK-002, HUM-005 | Inspection |
| REQ-HFPX-TTP-002 | The programme shall define the training phase structure, including simulator-based phases (phase set and sequencing TBD; simulator detail Vol 30.4). | HUM-005 | Inspection |
| REQ-HFPX-TTP-003 | The programme shall define qualification hooks to Vol 26.3, identifying prerequisite and authorisation interfaces (criteria TBD in Vol 26.3). | HUM-005 | Inspection |
| REQ-HFPX-TTP-004 | The programme shall align the syllabus structure with the unmanned-first principle, identifying where unmanned demonstration precedes crewed evaluation (alignment TBD). | STK-002, HUM-005 | Inspection |
| REQ-HFPX-TTP-005 | The programme shall define the methods and assessment framework headings for pilot training (objectives, methods, and assessment detail TBD). | HUM-005 | Inspection + Demonstration |

All phases, objectives, methods, and assessment criteria are TBD; no hours, ratios, scores, or limits are stated.

## 7. Architecture

Starter allocation (SAD owns authoritative mapping): TTP requirements → training system / operations organisation + simulator interfaces + Vol 26.3 qualification interfaces. All TBC.

## 8. Detailed Design

Not applicable — syllabus structure only. Lesson plans, briefings, manoeuvre sequences, and instructional content are not defined in this revision and remain TBD.

## 9. Interfaces

Interfaces to qualification (Vol 26.3), simulator provision (Vol 30.4, Vol 19), life-support/occupant interfaces (Vol 12), and operations (Vol 26) are TBD. No interface value or layout is approved.

## 10. Operational Concept

Pilot training syllabus structure applies across preparation, flight, and recovery contexts; phase-specific applicability is TBD. This document states structure only and provides no executable flight-training instruction.

## 11. Safety

Training-structure gaps feed Vol 13 safety analyses (to follow). No TTP requirement confers flight approval; human flight remains gated by tier 01.10 (SAF-005) and the Safety Case.

## 12. Performance

No TTP requirement quantifies performance. All durations, throughput, pass criteria, and workload-related measures are TBD pending follow-on study.

## 13. Verification & Validation

Each requirement states its method above; verification IDs, scenario sets, participant criteria, and pass thresholds are TBD in the V&V Plan (Vol 22) with Vol 26/30 inputs. No training credit is claimed at this revision.

## 14. Risks

- Syllabus detail deferred → late discovery of training gaps; mitigation: structure placeholders plus qualification gates.
- Simulator/qualification interfaces undefined → misalignment with Vol 19/26.3; mitigation: explicit TBD hooks reviewed at SRR.

## 15. Open Issues

TBC: syllabus objectives, phase set including simulator, qualification hooks to Vol 26.3, unmanned-first alignment, and methods/assessment framework pending Vol 26/30 work.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on STK-002 stability, HUM-005 policy, safety gating (01.10), Vol 12/19/26 detail work, and V&V Plan cases. Changes propagate by change record.

## 18. Traceability

Parents: STK-002, HUM-005 (see table). Children: Vol 26.3 qualification criteria, Vol 30.4 simulator training detail, V&V cases, RTM rows. RTM seed for TTP-001..005 added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Detail additions require new revisions via change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 30.1) |
