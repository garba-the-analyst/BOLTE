# Human Factors Requirements

**Document ID:** HFPX-SYS-HUM-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 2 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define system-level human-factors requirements for HFP-X (Chapter 01.11). This Tranche 2 draft establishes workload, HMI, ergonomics, monitoring, and training requirement placeholders; detail follows in Vol 10/12/30 with all values TBD.

## 2. Scope

Covers pilot/operator workload limits, helmet/HMI legibility, prone-restraint/ergonomics, physiological monitoring, and training/competency (all thresholds TBD). Excludes detailed HMI design, suit design, and training curricula, which are Vol 10/12/30 scope.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parent REQ-HFPX-SYS-005 operator-interface policy)
- Stakeholder needs STK-002/007 (human involvement and operator interfaces)
- Vol 10 (HMI/helmet detail, to follow), Vol 12 (life support/suit, to follow), Vol 30 (training, to follow)
- HFP prompt §§8–10 (requirements format, classification, traceability)

## 4. Definitions & Acronyms

- HUM: human-factors requirement tier; ID `REQ-HFPX-HUM-NNN`; verification: Analysis / Inspection / Demonstration / Test.
- HMI: human-machine interface including helmet display and pilot/operator controls; legibility criteria TBD.
- TBD/TBC: unknown data; no values invented; detail owned by Vol 10/12/30.

## 5. System Context

Human-factors tier refines SYS-005 and stakeholder needs into testable placeholders:

```text
STK-002/007 + SYS-005 → HUM-001..005 → Vol 10/12/30 detail → Demonstration and test cases
```

Human flight is additionally gated by safety tier 01.10; no human-flight approval is implied by this document.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-HUM-001 | The system shall keep pilot/operator workload within defined limits of [TBD] across nominal and defined off-nominal tasks (limits and task set TBD; detail Vol 10/30). | STK-002, SYS-005 | Analysis + Demonstration |
| REQ-HFPX-HUM-002 | The system shall provide helmet/HMI symbology and alerts legible and interpretable within [TBD] under defined lighting, vibration, and workload conditions (criteria TBD; detail Vol 10). | STK-007, SYS-005 | Demonstration + Test |
| REQ-HFPX-HUM-003 | The system shall provide prone-restraint and ergonomics supporting defined posture, reach, visibility, and comfort bounds of [TBD] for the intended occupant range (bounds TBD; detail Vol 12). | STK-002, SYS-005 | Demonstration |
| REQ-HFPX-HUM-004 | The system shall provide physiological monitoring with defined parameters of [TBD] and annunciation of defined exceedances to the pilot/operator and ground station (parameters TBD; detail Vol 10/12). | STK-002, STK-007 | Demonstration |
| REQ-HFPX-HUM-005 | The system shall define and enforce training and competency prerequisites of [TBD] before any human flight, including currency and authorisation criteria (criteria TBD; detail Vol 30). | STK-002, SYS-005 | Inspection + Demonstration |

Detail for HUM-001/002 → Vol 10; HUM-003/004 → Vol 12 (with Vol 10 for annunciation); HUM-005 → Vol 30.

## 7. Architecture

Starter allocation (SAD owns authoritative mapping): HUM-001/002 → helmet/HMI/pilot interface + ground station; HUM-003 → airframe/restraint/suit interfaces; HUM-004 → sensors/avionics/ground station; HUM-005 → training system/operations. All TBC.

## 8. Detailed Design

Not applicable — system level only. HMI layouts, restraint geometry, sensor selection, and curricula live in Vol 10/12/30 and are TBD.

## 9. Interfaces

Human-system interfaces (helmet, controls, displays, suit couplings, telemetry presentation) are TBD in Chapter 01.16 and Vol 02 ICDs. No interface value or layout is approved.

## 10. Operational Concept

Human-factors requirements apply across CONOPS preparation, flight, and recovery phases; phase-specific workload and monitoring applicability is TBD in Vol 10/30. Unmanned demonstration precedes any crewed evaluation per safety gating.

## 11. Safety

Human-factors failures and workload exceedances feed Vol 13 safety analyses (FHA/FMEA/FTA, to follow). No HUM requirement confers flight approval; human flight remains gated by tier 01.10 (SAF-005) and the Safety Case.

## 12. Performance

No HUM requirement quantifies performance. All workload scales, legibility times, ergonomic bounds, monitoring thresholds, and training hours are TBD pending Vol 10/12/30 studies.

## 13. Verification & Validation

Each requirement states its method above; verification IDs, task scenarios, participant criteria, and pass thresholds are TBD in the V&V Plan (Vol 22) with Vol 10/12/30 inputs. No human-factors credit is claimed at this revision.

## 14. Risks

- HMI/ergonomics detail deferred → late discovery of workload issues; mitigation: early Vol 10/12 placeholders plus demonstration gates.
- Training scope undefined → unqualified human flight pressure; mitigation: HUM-005 gating plus SAF-005 safety gate.

## 15. Open Issues

ISS-002 (SyRS completeness), plus TBC: workload task set, legibility criteria, occupant-range bounds, monitoring parameter set, and competency criteria pending Vol 10/12/30.

## 16. Assumptions

- A-TBD-05: Five placeholders cover Tranche 2 human-factors scaffolding; validation: SRR review.
- Assumption that prone-posture concept remains the reference configuration; validation: Vol 12 ergonomic review.

## 17. Dependencies

Depends on STK-002/007 stability, SYS-005 policy, safety gating (01.10), Vol 10/12/30 detail work, and V&V Plan cases. Changes propagate by change record.

## 18. Traceability

Parents: STK-002/007, SYS-005 (see table). Children: Vol 10/12/30 detailed requirements, subsystem HMI/ergonomic specs, V&V cases, RTM rows. RTM seed for HUM-001..005 added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0 (structure only) — Tranche 2 draft, not baselined. Detail additions from Vol 10/12/30 require new revisions via change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 2 draft (Chapter 01.11) |
