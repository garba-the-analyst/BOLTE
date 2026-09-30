# 19.12 Monte Carlo Analysis

**Document ID:** HFPX-SIM-MTC-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the Monte Carlo dispersion inventory, sample-size and method criteria, success criteria, and flow to verified requirements for HFP-X.
Establishes methodology only; contains no design or operation instructions.
This document owns Chapter 19.12 direction under Volume 19.

## 2. Scope

Covers dispersed trajectory and behaviour analysis over mass, thrust, aerodynamic, and wind variations and propagation of results to requirement verification.
Applies wherever statistical analysis supports gate or requirement claims; detailed runs and post-processing are owned by child documents (IDs TBD).
Excludes model development (owned by Chapters 19.2–19.8), environmental definition (owned by Chapter 19.14), and test execution (owned by Vol 23).

## 3. Applicable Documents

- HFPX-VV-PLN-001 VV Plan, notably REQ-HFPX-VVP-001 (verification method) and REQ-HFPX-VVP-004 (gated progression)
- Volume 19 model chapters 19.2–19.8 (IDs TBD) for trajectory, aerodynamic, propulsion, and control models dispersed in analysis
- MST tier (IDs TBD)
- Vol 22 VCRM (ID TBD) for requirement flow; Vol 23 (IDs TBD) for validation data interfaces
- Vol 25 certification volumes (IDs TBD) — no certification credit claimed in this revision

## 4. Definitions & Acronyms

- Monte Carlo analysis: repeated simulation over dispersed inputs to characterise outcome distributions; method TBD
- Dispersion variable: an input varied across runs, including mass, thrust, aerodynamic, and wind terms; distributions TBD
- Sample size: number of runs and sampling approach; criteria TBD
- Success criteria: rules mapping outcome distributions to requirement verdicts; thresholds TBD
- Requirement flow: trace from analysis results to verified parent requirements; mapping TBD

## 5. System Context

Monte Carlo analysis sits within analysis on the left-to-centre of the programme V-model, informing requirement verification before higher gates:

```text
MODELS → MONTE CARLO → REQUIREMENT VERDICTS → GATES
   ↑________ VCRM TRACEABILITY ________↑
```

Dispersed models produce outcome distributions that are assessed against success criteria and traced to requirements. Analysis does not authorise flight.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-MMC-001 | The programme shall define the dispersion-variable inventory covering mass, thrust, aerodynamic, and wind terms; variables, ranges, and distributions TBD. | REQ-HFPX-VVP-001 | Analysis |
| REQ-HFPX-MMC-002 | The programme shall define Monte Carlo sample-size and method criteria; sampling method, size rule, and convergence rule TBD. | REQ-HFPX-VVP-001 | Analysis |
| REQ-HFPX-MMC-003 | The programme shall define Monte Carlo success criteria mapping outcome distributions to verdicts; thresholds and handling of edge outcomes TBD. | REQ-HFPX-VVP-001 | Analysis |
| REQ-HFPX-MMC-004 | The programme shall define the Monte-Carlo-to-requirement flow stating which requirements Monte Carlo verifies; mapping TBD in the VCRM. | REQ-HFPX-VVP-001 | Inspection |

## 7. Architecture

Analysis organisation (roles TBD): analysis lead, model owners per Chapters 19.2–19.8, independent reviewer TBD.
Analysis structure TBD: dispersed model set (revisions TBD), sampling harness (mechanism TBD), scenario set (IDs TBD), results store with revision trace TBD.
Only recorded analysis revisions support verification claims; revision control TBD.

## 8. Detailed Design

Dispersion elaboration TBD per REQ-HFPX-MMC-001: variable list TBD, distribution forms TBD, correlation treatment TBD, excluded variations TBD with rationale TBD.
Method elaboration TBD per REQ-HFPX-MMC-002: sampling scheme TBD, size determination TBD, convergence assessment TBD, repeatability control TBD.
Success elaboration TBD per REQ-HFPX-MMC-003: verdict rules TBD, outcome metrics TBD, treatment of outliers TBD.
Flow elaboration TBD per REQ-HFPX-MMC-004: verified requirement list TBD, VCRM rows TBD, evidence packaging TBD.
No values are baselined in this revision.

## 9. Interfaces

- Monte Carlo ↔ Models (Chapters 19.2–19.8): model revisions and validity bounds feed dispersed runs
- Monte Carlo ↔ Environment (Chapter 19.14): environment variable definitions feed dispersion setup where overlapping
- Monte Carlo ↔ VCRM (Vol 22.3): results traced to parent requirements with no orphans; rows TBD
- Monte Carlo ↔ Safety (Vol 13/24): safety-relevant threads identified for independent review; degree of independence TBD

## 10. Operational Concept

Monte Carlo operates analysis-to-verdict: record model revisions → configure dispersions and sampling per recorded criteria → execute runs → assess against success criteria → trace verdicts to requirements.
Re-analysis is required after any change invalidating recorded inputs, with scope defined per change record (details TBD).
Cadence, staffing, and tooling TBD in child documents.

## 11. Safety

Safety-relevant Monte Carlo threads receive independent review to a degree TBD, with review records feeding hazard-closure evidence paths owned by the Safety Case.
Statistical evidence alone does not close catastrophic-hazard threads and does not authorise human flight.
Any advisory-function influence on analysed threads shall identify the deterministic bounded function actually verified; method TBD.

## 12. Performance

Analysis performance indicators TBD; no thresholds baselined: run completion TBD, convergence closure TBD, verdict traceability TBD, re-analysis backlog TBD.
Measurement method and reporting cadence TBD in child documents.

## 13. Verification & Validation

This document is verified at gated reviews against the document template checklist (header, structure, IDs, method on every requirement, TBD discipline).
Monte Carlo cases (IDs TBD) shall each define objective, traced parent requirement, dispersed set, method, configuration, and acceptance criteria TBD per case before execution.
Validation of the analysis approach is programme-authority approval at gated reviews; certification validation is owned by Vol 25 with no claims here.

## 14. Risks

- Dispersion inventory incomplete or distributions unsupported, producing misleading verdicts; mitigation: inventory review with validity-bounds check (method TBD)
- Sample-size and convergence criteria left TBD, blocking verdict defensibility; mitigation: per-case TBD tracking with owning role and due gate (assignments TBD)
- Results claimed against untraced requirements; mitigation: REQ-HFPX-MMC-004 VCRM flow with no-orphan rule

## 15. Open Issues

Dispersion variables and distributions TBD. Sampling method, size, and convergence TBD. Success thresholds TBD. Verified-requirement mapping TBD. Tooling and revision control TBD. All analysis case IDs TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on VV Plan methodology, models from Chapters 19.2–19.8, environment definitions (Chapter 19.14), MST tier direction (IDs TBD), Vol 22 VCRM discipline, and Vol 25 credit rules.

## 18. Traceability

Parents: REQ-HFPX-VVP-001 (verification method); REQ-HFPX-VVP-004 (gated progression context); MST tier (IDs TBD); model chapters 19.2–19.8 (IDs TBD).
Children: Monte Carlo cases and result records (IDs TBD; rows TBD in VCRM).
RTM: REQ-HFPX-MMC-001..004 → CONCEPT. No orphaned requirements; no orphaned verification cases per REQ-HFPX-VVP-002 principle.

## 19. Configuration

BL-0.0. Tranche 5 draft, CONCEPT, not baselined. Future changes via change records; any change re-validates affected traceability before verification claims.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 draft (Chapter 19.12 Monte Carlo dispersions, method, success criteria, requirement flow; structure only) |
