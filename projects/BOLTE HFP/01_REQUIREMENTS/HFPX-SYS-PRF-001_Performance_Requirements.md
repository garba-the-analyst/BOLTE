# Performance Requirements

**Document ID:** HFPX-SYS-PRF-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 2 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define system-level performance requirement placeholders for HFP-X (Chapter 01.8). This Tranche 2 draft reserves the requirement structure only; no threshold or objective value is approved and every quantity remains TBD pending budgets and models.

## 2. Scope

Covers placeholder performance topics: hover endurance, payload capability, wind operating limits, availability, and control-response behaviour. Excludes design solutions, environmental qualification detail (01.9), and verification cases (Vol 22). All values TBD.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (esp. REQ-HFPX-SYS-008 placeholder policy, REQ-HFPX-MIS-007)
- HFPX-SYS-MIS-001 Mission Requirements (parent need for quantified capability)
- Budgets/models actions under ISS-007 (Vol 06/19, to follow)
- HFP prompt §§8–10, §§19, 32 (requirements format, unknown-data handling)

## 4. Definitions & Acronyms

- PRF: performance requirement tier; ID `REQ-HFPX-PRF-NNN`; verification: Analysis / Inspection / Demonstration / Test.
- PLACEHOLDER: requirement text is structural only; threshold TBD; not approved for design or test.
- TBD/TBC: unknown data; values require budgets/models via change record.

## 5. System Context

Performance tier quantifies SyRS placeholder policy SYS-008:

```text
MIS-007 + SYS-008 → PRF-001..005 (placeholders) → Budgets/models (Vol 06/19) → Quantified revisions
```

No allocation to subsystems is authoritative until budgets exist; SAD will allocate quantified revisions when approved.

## 6. Requirements

No value in this section is approved. All thresholds are explicitly TBD and require budgets/models (ISS-007) via change record before use in design, analysis, or test.

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-PRF-001 | The system shall achieve a hover endurance capability of [TBD] under defined conditions (PLACEHOLDER — threshold TBD, conditions TBD). | REQ-HFPX-MIS-007, REQ-HFPX-SYS-008 | Analysis + Test |
| REQ-HFPX-PRF-002 | The system shall carry a payload capability of [TBD] within the defined envelope (PLACEHOLDER — threshold TBD, envelope TBD). | REQ-HFPX-MIS-007, REQ-HFPX-SYS-008 | Analysis + Test |
| REQ-HFPX-PRF-003 | The system shall operate within defined wind limits of [TBD], including gust handling of [TBD] (PLACEHOLDER — thresholds TBD). | REQ-HFPX-MIS-007, REQ-HFPX-SYS-008 | Analysis + Test |
| REQ-HFPX-PRF-004 | The system shall achieve an operational availability of [TBD] under defined support conditions (PLACEHOLDER — threshold TBD, conditions TBD). | REQ-HFPX-MIS-007, REQ-HFPX-SYS-008 | Analysis + Demonstration |
| REQ-HFPX-PRF-005 | The system shall achieve a control-response behaviour within [TBD] of defined command inputs (PLACEHOLDER — threshold TBD, input set TBD). | REQ-HFPX-MIS-007, REQ-HFPX-SYS-008 | Analysis + Test |

## 7. Architecture

No allocation is authoritative at this revision. Starter expectation (SAD to confirm after quantification): PRF-001/002 → propulsion/fuel/airframe budgets; PRF-003 → FCS/aero; PRF-004 → maintenance/support; PRF-005 → FCS/computing. All TBC.

## 8. Detailed Design

Not applicable — placeholder level only. Design solutions and sizing analyses live in Vol 03–18 and Vol 19 and are TBD.

## 9. Interfaces

Performance interfaces (power, data latency, servicing throughput) are TBD in Chapter 01.16 and Vol 02 ICDs. No interface value is approved in this revision.

## 10. Operational Concept

Placeholders will be exercised through CONOPS threads once quantified; until then no operational claim is made. Unmanned demonstration precedes any human-flight performance validation per safety gating.

## 11. Safety

Unquantified performance shall not be used as a safety claim. Performance-safety interactions (e.g. margins, reserves) are TBD and require Vol 13 safety analyses by change record before any flight envelope is declared.

## 12. Performance

This section is the requirement set itself (§6). All thresholds TBD; budgets and 6-DOF results (Vol 06/19) are the only approved path to quantification. Invented figures are prohibited.

## 13. Verification & Validation

Each requirement states its intended method above; verification IDs, cases, success criteria, and instrumentation are TBD in the V&V Plan (Vol 22). No verification credit is claimed at this revision.

## 14. Risks

- Pressure to treat placeholders as targets → premature sizing; mitigation: explicit PLACEHOLDER marking and CONCEPT status.
- Budgets/models delayed (ISS-007) → tier stays unquantified; mitigation: SRR exit requires structure only, not values.

## 15. Open Issues

ISS-007 (budgets/models needed to quantify PRF-001..005 — OPEN), ISS-002 (SyRS completeness), ISS-006/008 (feasibility unknowns). Quantification requires change records, not inline edits.

## 16. Assumptions

- A-TBD-02: Five placeholder topics are sufficient scaffolding for Tranche 2; validation: SRR review.
- Assumption that budgets/models path (ISS-007) will define conditions and thresholds; validation: Vol 06/19 plans.

## 17. Dependencies

Depends on mission-needs stability (MIS-007), SYS-008 policy, budgets/models (Vol 06/19), SAD allocation feedback, and V&V Plan cases. Changes to budgets propagate to this tier by change record.

## 18. Traceability

Parents: REQ-HFPX-MIS-007, REQ-HFPX-SYS-008 (see table). Children: quantified PRF revisions, subsystem performance budgets (Vol 03–18, 06), V&V cases, RTM rows. RTM seed for PRF-001..005 added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0 (structure only) — Tranche 2 draft, not baselined. Quantification requires new revisions via change control; inline value edits without a change record are prohibited.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 2 draft (Chapter 01.8; all thresholds TBD placeholders) |
