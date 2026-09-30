# First-Issue Mass / Thrust / Energy Budgets

**Document ID:** HFPX-AERO-BDG-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 7 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Publish the first computed issue of HFP-X mass, thrust and energy budgets per the 06.15 schemas, directly attacking ISS-007. Every value carries a basis tag; reference-class values are TBC for HFP-X, and lines without basis remain TBD.

## 2. Scope

Reference-class hover budgets only (T = W, published SFC path). Cruise endurance is TBD (drag TBD). No line in this document is a design baseline or a clearance.

## 3. Applicable Documents

- HFPX-AERO-CRZ-001 Cruise (budget schemas §12; first-issue action owned there — this document discharges the computation, approval still TBD)
- HFPX-PROP-TRD-001 Propulsion Energy Trade Study (reference data and citations reused here)
- HFPX-AERO-SIX-001 (mass/thrust interfaces); HFPX-SIM-SIX-001 (budget consumers)
- Computation: `06_AERODYNAMICS/hfpx_budgets.py` (re-runnable); tables: `06_AERODYNAMICS/budgets/*.csv`
- Sources (retrieved 2026-09-29): ASTM D1655/AFQRJOS (Jet A-1 LHV ≥42.8 MJ/kg); PBS Aerospace TJ100 (SFC 0.116 kg/N/h) and TJ40 (395 N, 3.3 kg); Gravity Industries suit (≈27 kg system, ≈1400–1700 N total)

## 4. Definitions & Acronyms

- Basis tags: PUBLISHED (authoritative source), REF-CLASS (published reference-system value, TBC for HFP-X), OPERATOR (operator input, not design), TBD (no basis), TBC (to be confirmed for HFP-X)
- First issue: computed starting point for iteration, not approval

## 5. System Context

Budgets sit between reference data and design commitment:

```text
PUBLISHED DATA + REF-CLASS → FIRST-ISSUE BUDGETS (this doc, TBC) → DESIGN ITERATION → BASELINED BUDGETS (gated)
```

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-BDG-001 | Mass, thrust and energy budgets shall be maintained as computed tables with per-line basis and status, re-issued by script rerun, never by hand edit. | REQ-HFPX-SYS-008 | Inspection |
| REQ-HFPX-BDG-002 | The mass rollup shall span 110–150 kg liftoff (reference-class, TBC) with airframe, avionics, helmet/suit lines held TBD for lack of basis. | REQ-HFPX-MIS-007 | Analysis |
| REQ-HFPX-BDG-003 | The thrust budget shall show hover T/W 1.34–1.83 on a 5×TJ40-class reference installation (TBC), with margin policy and transition requirement TBD. | REQ-HFPX-SYS-001 | Analysis |
| REQ-HFPX-BDG-004 | The energy budget shall show 2.8–7.2 min reference-class hover endurance on 8–15 kg Jet A-1 (TBC), reproducing the Gravity-class order of magnitude as a consistency check, not a claim. | REQ-HFPX-MIS-007 | Analysis |
| REQ-HFPX-BDG-005 | Cruise endurance shall remain TBD until drag (06.5/06.6) and installed SFC exist; no cruise figure shall be carried before then. | REQ-HFPX-SYS-008 | Inspection |

## 7. Architecture

Budget set: `budgets/mass_budget.csv`, `thrust_budget.csv`, `energy_budget.csv` — columns Budget line, Low, High, Unit, Basis, Status. Generator script is the single source; CSVs are never hand-edited.

## 8. Detailed Design

Computed results (script output, TBC): liftoff 110–150 kg; hover thrust 1079–1471 N vs 1975 N reference available; fuel flow 125–171 kg/h; endurance 2.8–7.2 min on 8–15 kg fuel; fuel energy carried 342–642 MJ. Battery-electric sanity line: ≈700–1000 kg pack for 5-min hover (REF-CLASS, confirms trade-study infeasibility finding). Cruise: TBD. Airframe/avionics/suit mass lines: TBD. Transition thrust: TBD (needs 6-DOF corridor, ISS-006).

## 9. Interfaces

- To 06.15 schemas: this issue populates the schema lines; schema rules (sign conventions, cadence) still TBD there
- To Vol 04/07: installed-SFC and allocation updates flow here by change record
- To Vol 03: airframe mass line awaits ISS-004 outcome
- To Vol 19: budgets feed 19.2/19.3 input-data families

## 10. Operational Concept

Budget cycle: populate from cited data → review at gate → replace TBC lines with measured/modelled values → re-issue by script → baseline only at SRR-or-later gate (TBD). Hand edits prohibited.

## 11. Safety

No safety or clearance claim rests on these budgets: T/W 1.34–1.83 is a reference-class arithmetic result, not controllability evidence (ISS-006 stands). Hazardous-subsystem boundary observed: analysis only.

## 12. Performance

Budget performance: mass rollup complete except TBD lines; thrust arithmetic closed for hover; energy closed for hover; cruise open. Margins: TBD (no margin policy set).

## 13. Verification & Validation

Script re-runnable (`python3 06_AERODYNAMICS/hfpx_budgets.py` reproduces all figures); verified by inspection of code-to-table trace and hand-check of hover arithmetic (T = W, flow = SFC × T, endurance = fuel/flow). Validation: gate review of bases and TBC lines.

## 14. Risks

- TBC lines mistaken for baselined values; mitigation: Status column + BDG-001 script-only rule + CONCEPT status
- SFC optimism (max-thrust catalogue SFC applied across hover); mitigation: installed-SFC measurement action (Vol 04.17 hooks), range carried, not point value
- Cruise endurance demanded before drag exists; mitigation: BDG-005 prohibition

## 15. Open Issues

Airframe/avionics/suit mass lines TBD. Installed SFC TBD. T/W margin policy TBD. Transition thrust TBD. Cruise drag/endurance TBD. ISS-007 stays OPEN until baselined budgets at a gate (this issue is evidence, not closure).

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on 06.15 schemas, trade-study reference data, Vol 03/04/07 for TBC replacement values, and 19.15-style evidence discipline before any gate use.

## 18. Traceability

Parents: SYS-001/008, MIS-007, PRF tier, 06.15 schemas. Children: re-issued budgets, 19.2/19.3 inputs, gate evidence. RTM: REQ-HFPX-BDG-001..005 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 7 draft, CONCEPT, not baselined. Budget re-issues are revisions of this document via script rerun + change record.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | First-issue budgets (Tranche 7; computed by hfpx_budgets.py) |
