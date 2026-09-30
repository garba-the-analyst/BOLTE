# Simulator Training

**Document ID:** HFPX-TRN-SIM-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the syllabus structure for HFP-X simulator training (Chapter 30.4). This Tranche 6 draft establishes structure-only placeholders for objectives, simulator use, and assessment; all content and device values are TBD.

## 2. Scope

Covers the structure of simulator training syllabus placeholders including simulator requirements, fidelity headings, and Vol 19 hooks. Excludes executable simulator drills, device specifications, and qualification decisions, which remain TBD in Vol 19 and follow-on revisions.

## 3. Applicable Documents

- HFPX-SYS-HUM-001 Human Factors Requirements (parent REQ-HFPX-HUM-005 training and competency prerequisites)
- Stakeholder need STK-002 (human involvement)
- Vol 19 (simulation / test facilities, to follow), Vol 26 (operations, to follow)
- HFP prompt §§8–10 (requirements format, classification, traceability)

## 4. Definitions & Acronyms

- TSM: simulator-training requirement tier; ID `REQ-HFPX-TSM-NNN`; verification: Inspection / Demonstration.
- Syllabus structure: objectives, methods, and assessment headings only; all entries TBD.
- Fidelity: degree of simulator representativeness; criteria TBD.
- TBD/TBC: unknown data; no values invented; detail deferred to follow-on revisions.

## 5. System Context

Simulator training structure refines HUM-005 into syllabus placeholders:

```text
STK-002 + HUM-005 → TSM-001..004 → Vol 19 simulator detail → V&V cases
```

No device qualification or training credit is implied by this document.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-TSM-001 | The programme shall define the simulator training syllabus structure with objectives, simulator-use headings, and assessment headings (all content TBD; no executable instruction). | STK-002, HUM-005 | Inspection |
| REQ-HFPX-TSM-002 | The programme shall define the simulator requirements headings supporting the syllabus, including device roles and capability headings (requirements TBD; detail Vol 19). | HUM-005 | Inspection |
| REQ-HFPX-TSM-003 | The programme shall define fidelity headings for simulator provision, identifying fidelity dimensions to be specified (criteria TBD; detail Vol 19). | HUM-005 | Inspection + Analysis |
| REQ-HFPX-TSM-004 | The programme shall define hooks to Vol 19 for simulator provision, availability, and configuration interfaces (detail TBD in Vol 19). | HUM-005 | Inspection |

All simulator requirements, fidelity criteria, and assessment criteria are TBD; no hours, ratios, scores, or limits are stated.

## 7. Architecture

Starter allocation (SAD owns authoritative mapping): TSM requirements → training system + Vol 19 simulator facilities + operations interfaces. All TBC.

## 8. Detailed Design

Not applicable — syllabus structure only. Simulator scenarios, scripts, session sequences, and device design are not defined in this revision and remain TBD.

## 9. Interfaces

Interfaces to Vol 19 simulator facilities, Vol 10 HMI representations, and Vol 26 operations are TBD. No interface value or layout is approved.

## 10. Operational Concept

Simulator training syllabus structure applies across preparation and rehearsal contexts; scenario-specific applicability is TBD. This document states structure only and provides no executable simulator instruction.

## 11. Safety

Training-structure gaps feed Vol 13 safety analyses (to follow). No TSM requirement confers device qualification or flight approval; safety gating remains via tier 01.10 and the Safety Case.

## 12. Performance

No TSM requirement quantifies performance. All durations, throughput, fidelity measures, and pass criteria are TBD pending follow-on study.

## 13. Verification & Validation

Each requirement states its method above; verification IDs, scenario sets, participant criteria, and pass thresholds are TBD in the V&V Plan (Vol 22) with Vol 19/30 inputs. No training credit is claimed at this revision.

## 14. Risks

- Simulator requirements deferred → late discovery of fidelity shortfalls; mitigation: structure placeholders plus Vol 19 hooks.
- Fidelity criteria undefined → negative training risk; mitigation: explicit TBD fidelity headings reviewed at SRR.

## 15. Open Issues

TBC: syllabus objectives, simulator requirements, fidelity dimensions, and Vol 19 hooks pending Vol 19/30 work.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on STK-002 stability, HUM-005 policy, Vol 19/26 detail work, and V&V Plan cases. Changes propagate by change record.

## 18. Traceability

Parents: STK-002, HUM-005 (see table). Children: Vol 19 simulator requirements, V&V cases, RTM rows. RTM seed for TSM-001..004 added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Detail additions require new revisions via change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 30.4) |
