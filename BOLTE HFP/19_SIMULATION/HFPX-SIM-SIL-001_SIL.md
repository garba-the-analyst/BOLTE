# 19.10 Software-in-the-Loop

**Document ID:** HFPX-SIM-SIL-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the Software-in-the-Loop scope, SIL-to-HIL promotion criteria, regression-on-change rule, and SIL coverage rule for HFP-X simulation.
Establishes methodology and gating only; contains no software build or operation instructions.
This document owns Chapter 19.10 direction under Volume 19.

## 2. Scope

Covers SIL execution of flight laws and models, promotion from SIL to HIL, regression discipline on change, and coverage expectations for SIL campaigns.
Applies from early law and model integration through HIL entrance; detailed cases and procedures are owned by child documents (IDs TBD).
Excludes hardware participation (owned by Chapter 19.9), model development (owned by Chapters 19.2–19.8), and test execution conduct (owned by Vol 23).

## 3. Applicable Documents

- HFPX-VV-PLN-001 VV Plan, notably REQ-HFPX-VVP-001 (verification method) and REQ-HFPX-VVP-004 (gated sim to SIL to HIL to unmanned testing, no gate skipping)
- Volume 19 model chapters 19.2–19.8 (IDs TBD), notably flight-control simulation per Chapter 19.8 and trajectory dynamics per Chapter 19.3
- MST tier (IDs TBD)
- Vol 23 execution volumes (IDs TBD) for results capture
- Vol 25 certification volumes (IDs TBD) — no certification credit claimed in this revision

## 4. Definitions & Acronyms

- SIL: Software/System Integration Laboratory — closed-loop simulation with flight software executing against simulated plant
- Laws: flight-control laws exercised in SIL; versions TBD
- Promotion: formal gate decision to progress between verification levels, with entrance criteria, completed evidence, and recorded decision
- Regression: re-execution of affected verification cases after change; scope TBD per change record
- Coverage: extent of SIL exercising over laws, models, and scenarios; metric TBD

## 5. System Context

SIL sits on the right-hand side of the programme V-model between analysis models and HIL:

```text
MODELS → SIL → HIL → UNMANNED TESTING
   ↑________ VCRM TRACEABILITY ________↑
   ↑________ GATED PROGRESSION ________↑
```

SIL integrates laws with models from Chapters 19.3 and 19.8 and supporting models from Chapters 19.2–19.8. SIL does not replace analysis, HIL, or flight testing and does not authorise flight.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-MSW-001 | The programme shall define the SIL scope covering flight laws and models per Chapters 19.3 and 19.8 with supporting models per Chapters 19.2–19.8; versions and configurations TBD. | REQ-HFPX-VVP-001 | Inspection |
| REQ-HFPX-MSW-002 | The programme shall define SIL-to-HIL promotion criteria governing progression from SIL to HIL; criteria TBD. | REQ-HFPX-VVP-004 | Demonstration |
| REQ-HFPX-MSW-003 | The programme shall apply a regression-on-change rule requiring re-verification of affected SIL cases after any change to laws, models, or SIL configuration; scope defined per change record, details TBD. | REQ-HFPX-VVP-001 | Analysis |
| REQ-HFPX-MSW-004 | The programme shall define the SIL coverage rule stating required extent of exercising over laws, models, and scenarios; metric and thresholds TBD. | REQ-HFPX-VVP-001 | Analysis |

## 7. Architecture

SIL organisation (roles TBD): SIL lead, law owner, model owners per Chapters 19.2–19.8, independent reviewer TBD.
SIL structure TBD: law build under test (version TBD), model backbone (revisions TBD), scenario suite (IDs TBD), recording and configuration control infrastructure TBD.
Only recorded configurations support gate claims; configuration control mechanism TBD.

## 8. Detailed Design

SIL scope elaboration TBD per REQ-HFPX-MSW-001: law identity TBD, model revisions TBD, interface definitions TBD, representativeness statement TBD.
Promotion elaboration TBD per REQ-HFPX-MSW-002: entrance criteria TBD, required SIL evidence TBD, exit criteria TBD, decision authority TBD.
Regression elaboration TBD per REQ-HFPX-MSW-003: change categories TBD, affected-case selection method TBD, re-verification closure rule TBD.
Coverage elaboration TBD per REQ-HFPX-MSW-004: coverage metric TBD, required extent TBD, gap-handling rule TBD.
No values are baselined in this revision.

## 9. Interfaces

- SIL ↔ Models (Chapters 19.2–19.8): model revisions and validity bounds feed SIL configuration
- SIL ↔ HIL (Chapter 19.9): SIL evidence feeds HIL entrance; HIL findings feed SIL re-entry per promotion criteria
- SIL ↔ Safety (Vol 13/24): safety-relevant SIL threads identified for independent review; degree of independence TBD
- SIL ↔ VCRM (Vol 22.3): SIL cases traced to parent requirements with no orphans; rows TBD

## 10. Operational Concept

SIL operates gate-to-gate: define scope, coverage, and regression rules early → configure law and model revisions per recorded revision → execute suite → capture evidence → gate decision before HIL entry.
No gate skipping is permitted per REQ-HFPX-VVP-004; each gate requires entrance criteria, completed evidence, and formal recorded decision.
Cadence, staffing, and tooling TBD in child documents.

## 11. Safety

Safety-relevant SIL threads receive independent review to a degree TBD, with review records feeding hazard-closure evidence paths owned by the Safety Case.
SIL evidence alone does not close catastrophic-hazard threads and does not authorise human flight.
Advisory functions are separated from deterministic bounded functions actually verified; separation detail TBD.

## 12. Performance

SIL performance indicators TBD; no thresholds baselined: suite pass rate TBD, coverage closure TBD, regression backlog TBD, evidence closure burn-down TBD.
Measurement method and reporting cadence TBD in child documents.

## 13. Verification & Validation

This document is verified at gated reviews against the document template checklist (header, structure, IDs, method on every requirement, TBD discipline, no-skipping alignment).
SIL verification cases (IDs TBD) shall each define objective, traced parent requirement, method, configuration under test, and acceptance criteria TBD per case before execution.
Validation of the SIL approach is programme-authority approval at gated reviews; certification validation is owned by Vol 25 with no claims here.

## 14. Risks

- Law and model revision drift producing invalid SIL evidence; mitigation: revision record per run with trace to source volumes (mechanism TBD)
- Pressure to enter HIL without SIL closure; mitigation: REQ-HFPX-MSW-002 promotion criteria with formal gate records
- Regression scope left undefined after change, allowing silent invalidation; mitigation: REQ-HFPX-MSW-003 per-change affected-case review (method TBD)

## 15. Open Issues

SIL law and model versions TBD. SIL-to-HIL promotion criteria TBD. Regression selection method TBD. Coverage metric and required extent TBD. Suite tooling and configuration control TBD. All verification case IDs TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on VV Plan gated progression, models and laws from Chapters 19.2–19.8, MST tier direction (IDs TBD), HIL entrance needs (Chapter 19.9), Vol 22 VCRM discipline, and Vol 25 credit rules.

## 18. Traceability

Parents: REQ-HFPX-VVP-001 (verification method); REQ-HFPX-VVP-004 (gated progression, no skipping); MST tier (IDs TBD); model chapters 19.2–19.8 (IDs TBD).
Children: SIL verification cases and procedures (IDs TBD; rows TBD in VCRM).
RTM: REQ-HFPX-MSW-001..004 → CONCEPT. No orphaned requirements; no orphaned verification cases per REQ-HFPX-VVP-002 principle.

## 19. Configuration

BL-0.0. Tranche 5 draft, CONCEPT, not baselined. Future changes via change records; any change re-validates affected traceability before gate claims.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 draft (Chapter 19.10 SIL scope, promotion, regression, coverage; structure only) |
