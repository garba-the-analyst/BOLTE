# Control Authority

**Document ID:** HFPX-FCS-AUT-001  
**Revision:** B (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 3 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X control-authority framework (Chapter 07.17): authority-budget ownership and method, margin policy, the shortfall-to-design-change rule, and evidence gates that must pass before transition attempts (linked to ISS-006).

## 2. Scope

Covers 6-DOF authority budgeting across axes, flight regimes, and failure cases for the production-aircraft concept. All budgets, margins, thresholds, and limits are TBD. Authority ownership and methods only — no numeric values are allocated in this document.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (REQ-HFPX-SYS-001, SYS-002, SYS-003)
- HFPX-SYS-ARC-001 SAD (ARC-004)
- HFPX-ARC-CTL-001 Control Architecture (CTL-003 — authority margins; CTL-002)
- HFPX-FCS-MIX-001 Propulsion Mixing (Ch 07.15); HFPX-FCS-ALC-001 Thrust Allocation (Ch 07.16)
- HFPX-SFA-001 Safety Architecture (SFA-001); HFPX-VVP-001/004 V&V (VVP-001, VVP-004)
- ISS-006 (control authority margins); Vol 19 (modelling/SIL/HIL)

## 4. Definitions & Acronyms

- Authority budget: allocated control capability per axis/mode/failure case above trim and manoeuvre demand; values and method TBD (6-DOF).
- Authority margin: remaining capability above demand; policy and values TBD (ISS-006).
- Shortfall: budgeted authority below policy-required margin; triggers design change per §7.
- 6-DOF: six degrees of freedom (three forces, three moments). ISS: Issue. TBD: To Be Determined.

## 5. System Context

Authority budgeting constrains laws, allocation, and mixing: budgets flow from this framework into allocation/mixing design, while demand estimates (trim, manoeuvre, gust, failure transients — all TBD) flow back for margin assessment. The safety computer enforces margin-related monitoring. Transition-regime authority is the sizing concern and gates transition attempts.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-FAU-001 | Authority budgets per axis, flight mode, and failure case shall be defined using a 6-DOF method; method, budgets, and data are TBD. | CTL-003, ARC-004 | Analysis |
| REQ-HFPX-FAU-002 | An authority-margins policy (required margins, accounting method, failure-case coverage) shall be defined; policy and values TBD under ISS-006. | CTL-003, SFA-001 | Analysis |
| REQ-HFPX-FAU-003 | Any authority shortfall against the margins policy shall trigger a recorded design change (laws, allocation, configuration, or requirements); change process TBD. | ARC-004, SFA-001 | Inspection |
| REQ-HFPX-FAU-004 | Authority evidence gates shall be defined and passed before any transition attempt; gate criteria and evidence are TBD under ISS-006. | CTL-003, VVP-001, VVP-004 | Analysis + Test |

## 7. Architecture

Authority framework owned by FCS/analysis (owner TBD): budget-definition block (6-DOF method TBD), margin-policy block (ISS-006), shortfall-detection → design-change routing block, and evidence-gate block feeding the flight-test/transition decision. Budgets constrain allocation/mixing; margins are monitored by the safety path. Structure and ownership only — no numeric content.

## 8. Detailed Design

Not applicable at Tranche 3 draft level. Budget method, demand models, margin values, shortfall thresholds, and gate criteria are TBD (Vol 07, Vol 13, Vol 19).

## 9. Interfaces

- To allocation/mixing (HFPX-FCS-ALC-001, HFPX-FCS-MIX-001): authority budgets/constraints — TBD.
- From aero/propulsion trades (Vol 03–06): effectiveness and demand inputs — TBD.
- To safety computer (SFA-001): margin-monitoring definitions — TBD.
- To verification thread (HFPX-FCS-VER-001, VVP-001/004): authority evidence artefacts — TBD.

## 10. Operational Concept

Authority framework applies to all flight modes; hover and transition size the budgets, failure cases size the margins. No transition attempt proceeds without passing REQ-HFPX-FAU-004 gates. Degraded modes operate under reduced budgets defined by the same method (TBD).

## 11. Safety

Insufficient authority or unrecognised shortfall is hazardous: REQ-HFPX-FAU-002 (margin policy), REQ-HFPX-FAU-003 (shortfall → design change, no silent acceptance), and REQ-HFPX-FAU-004 (gates before transition) plus the safety path (SFA-001) mitigate it. No controllability claim is made; all margins TBD pending ISS-006 and Vol 07/13 analysis.

## 12. Performance

Trim/manoeuvre demand models, gust allowances, transient budgets, and handling-quality mappings are TBD. No allocation value is stated. Methods for budgeting are TBD.

## 13. Verification & Validation

Per HFPX-FCS-VER-001: authority verified by analysis (6-DOF budgets, margin computation — methods TBD) supported by SIL/HIL and unmanned-test evidence for gates. Cases trace to FAU-001..004; acceptance criteria TBD per case under ISS-006. No gate skipping.

## 14. Risks

- ISS-006: authority margins unknown until aero/propulsion trades close; mitigation: budget/method owners assigned, evidence gates block transition, stub status explicit.
- Demand growth erodes margins late; mitigation: REQ-HFPX-FAU-003 shortfall rule forces recorded design change.
- 6-DOF coupling underestimated; mitigation: method required to cover 6-DOF (TBD), validated per Vol 19.

## 15. Open Issues

ISS-006 (authority margins); budget method TBD; budgets/margins/thresholds TBD; shortfall change process TBD; evidence-gate criteria TBD; authority owner TBD.

## 16. Assumptions


_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SAD (ARC-004), Control Architecture (CTL-002, CTL-003), mixing/allocation (HFPX-FCS-MIX-001, HFPX-FCS-ALC-001), FTC (HFPX-FCS-FTC-001), safety view (SFA-001), verification thread (VVP-001/004, HFPX-FCS-VER-001), aero/propulsion trades (Vol 03–06, ISS-003/004/007), Vol 19 (SIL/HIL).

## 18. Traceability

Parents: SYS-001, SYS-002, SYS-003; ARC-004; CTL-002, CTL-003; SFA-001; VVP-001, VVP-004. Children: authority budgets, margin policy, gate criteria (all TBD), V&V cases. RTM: REQ-HFPX-FAU-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 3 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 3 draft (Chapter 07.17) |
| B | 2026-09-29 | Assumptions removed; all unknowns recorded as TBD (no assumptions raised or relied upon). |
