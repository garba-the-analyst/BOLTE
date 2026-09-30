# Requirements Traceability Matrix Description — Chapter 01.18

**Document ID:** HFPX-SYS-RTM-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 8 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define how the Requirements Traceability Matrix (RTM) for HFP-X is maintained, gated and used. This Tranche 8 draft establishes structure only; the authoritative matrix rows live in `requirements_traceability_matrix.csv` and are TBD beyond the seed.

## 2. Scope

Covers RTM governance across all Volume 01 requirement tiers (01.1–01.17) through to SAD allocation and V&V cases. VCRM detail is hooked to Vol 22.3. Column schema and coverage rules are defined here.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS and all Volume 01 tiers (01.1–01.17)
- `requirements_traceability_matrix.csv` (authoritative row store; column schema referenced in §6)
- Vol 22.3 VCRM (verification cross-reference hooks, TBD)
- HFP prompt §§8–10 (requirements format, classification, traceability)

## 4. Definitions & Acronyms

- RTM requirement ID `REQ-HFPX-RTM-NNN`; verification: Analysis / Inspection / Demonstration / Test
- TBD/TBC: unknown data handling; no invented values
- VCRM: Verification Cross-Reference Matrix (Vol 22.3); orphan: requirement with missing parent or missing child link where one is required

## 5. System Context

The RTM is the law governing requirement traceability from need to evidence:

```text
PARENTS (MIS/STK/SYS/…) → REQUIREMENTS (01.1–01.17) → RTM ROWS (csv) → SAD → V&V (VCRM Vol 22.3)
```

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-RTM-001 | The project shall maintain the RTM with a column schema matching `requirements_traceability_matrix.csv` (columns TBD in csv header; schema changes by change control). | REQ-HFPX-SYS-008, REQ-HFPX-PGM-002 | Inspection |
| REQ-HFPX-RTM-002 | The project shall maintain the RTM with 100%-of-major-requirements coverage such that every major requirement has a parent link and a child link or explicit deferral (no orphan accepted at review; deferral list TBD). | REQ-HFPX-SYS-008, REQ-HFPX-PGM-002 | Inspection |
| REQ-HFPX-RTM-003 | The project shall reject orphan requirements at each review gate with no parentless or childless major requirement proceeding without a recorded action (orphan rule; action list TBD). | REQ-HFPX-SYS-007, REQ-HFPX-PGM-011 | Inspection |
| REQ-HFPX-RTM-004 | The project shall hook RTM verification columns to Vol 22.3 VCRM cases such that every verifiable requirement maps to ≥1 V&V case or a TBD placeholder (mapping TBD in V&V Plan). | REQ-HFPX-SYS-007, REQ-HFPX-PGM-011 | Inspection |

Traceability to programme planning artefacts PGM-002 and PGM-011 is recorded in §18; formal requirement parents above satisfy the Volume 01 parent rule.

## 7. Architecture

RTM tooling and storage views TBD; SAD references RTM rows for allocation completeness. Tool selection TBD.

## 8. Detailed Design

Not applicable — governance tier only. CSV column implementation and VCRM case detail live in SE tooling and Vol 22 and are TBD.

## 9. Interfaces

RTM exchanges rows with SAD (§9/ICDs), subsystem requirement tools and the V&V Plan; interface formats TBD.

## 10. Operational Concept

RTM coverage is assessed at each review (SRR and successors); gate criteria TBD in SEMP/V&V Plan.

## 11. Safety

RTM coverage includes safety requirements (01.10) feeding the Safety Case; safety trace completeness is gated identically. Analyses TBD.

## 12. Performance

No RTM performance value is stated; tool capacity and scale targets TBD.

## 13. Verification & Validation

Each requirement states its method above; verification cases and IDs are TBD in the V&V Plan (Vol 22.3 VCRM hooks). Inspection via RTM export and coverage-report review. Requirements without a verification method are rejected at SRR.

## 14. Risks

- RTM decaying as Vol 03–18 grow → mitigation: coverage gate per review, orphan-rejection rule
- Schema drift between this description and the csv; mitigation: §6 rule that schema matches csv header, changes by change control

## 15. Open Issues

- CSV column schema finalisation TBD
- VCRM case mapping TBD (Vol 22.3 actions)
- Coverage-gate thresholds and deferral policy TBD

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on all Volume 01 tiers, SAD allocation feedback, V&V Plan / VCRM maturity (Vol 22.3), SE tooling, programme planning inputs PGM-002/PGM-011.

## 18. Traceability

Parents: REQ-HFPX-SYS-007, REQ-HFPX-SYS-008 (Volume 01 parent rule); programme traces: PGM-002, PGM-011. Children: RTM csv rows, SAD allocation rows, V&V/VCRM cases. RTM seed for RTM-001..004 added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0 (structure only) — Tranche 8 draft, not baselined. Changes require change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 8 draft (Chapter 01.18) |
