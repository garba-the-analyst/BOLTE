# 19.13 Failure Simulation

**Document ID:** HFPX-SIM-FSM-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the injected-failure inventory, failure-simulation-to-FTC and FHA flow, pass and fail rules, and unmanned-test correlation rule for HFP-X.
Establishes methodology only; contains no design, build, or operation instructions.
This document owns Chapter 19.13 direction under Volume 19.

## 2. Scope

Covers simulation of failures including module-out, sensor loss, and link loss, trace to fault-tolerance and hazard analysis, verdict rules, and correlation to unmanned testing.
Applies wherever failure behaviour is assessed by simulation before higher gates; detailed runs and procedures are owned by child documents (IDs TBD).
Excludes hazard analysis ownership (Vol 13/24), control design (Chapters 19.2–19.8), HIL fault injection execution (Chapter 19.9), and test execution (Vol 23).

## 3. Applicable Documents

- HFPX-VV-PLN-001 VV Plan, notably REQ-HFPX-VVP-001 (verification method) and REQ-HFPX-VVP-004 (gated progression)
- Volume 19 model chapters 19.2–19.8 (IDs TBD) for plant and control models subjected to injected failures
- MST tier (IDs TBD)
- FTC and FHA sources (IDs TBD) for failure flow endpoints; Vol 13/24 safety volumes for hazard closure
- Vol 23 execution volumes (IDs TBD) for unmanned-test correlation data

## 4. Definitions & Acronyms

- Failure simulation: assessed system response under injected failures; scope TBD
- Injected-failure inventory: the set of simulated failures, including module-out, sensor loss, and link loss; list TBD
- FTC: fault-tolerance claims or cases receiving simulation evidence; IDs TBD
- FHA: functional hazard assessment receiving simulation evidence; IDs TBD
- Correlation: structured comparison of simulation outcomes to unmanned-test observations; method TBD

## 5. System Context

Failure simulation sits within analysis, feeding fault-tolerance and hazard threads and informing unmanned-test readiness:

```text
MODELS + INJECTED FAILURES → FAILURE SIM → FTC / FHA → GATES
                                      ↓
                          CORRELATION WITH UNMANNED TEST
```

Simulation evidence supports analysis of tolerance and hazard handling. Simulation does not close hazards and does not authorise flight.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-MFS-001 | The programme shall define the injected-failure inventory covering module-out, sensor loss, and link loss; failure cases, injection points, and exclusions TBD. | REQ-HFPX-VVP-001 | Inspection |
| REQ-HFPX-MFS-002 | The programme shall define the failure-simulation-to-FTC and failure-simulation-to-FHA flow stating which tolerance and hazard threads receive simulation evidence; mapping TBD. | REQ-HFPX-VVP-001 | Inspection |
| REQ-HFPX-MFS-003 | The programme shall define failure-simulation pass and fail rules; verdict criteria and handling of indeterminate outcomes TBD. | REQ-HFPX-VVP-001 | Analysis |
| REQ-HFPX-MFS-004 | The programme shall define the unmanned-test correlation rule requiring structured comparison of failure-simulation outcomes to unmanned-test observations; method and closure rule TBD. | REQ-HFPX-VVP-004 | Demonstration |

## 7. Architecture

Failure-simulation organisation (roles TBD): analysis lead, model owners per Chapters 19.2–19.8, safety liaison, independent reviewer TBD.
Failure-simulation structure TBD: model set under failure (revisions TBD), failure-injection harness (mechanism TBD), scenario set (IDs TBD), results store with revision trace TBD.
Only recorded revisions support FTC, FHA, or gate claims; revision control TBD.

## 8. Detailed Design

Inventory elaboration TBD per REQ-HFPX-MFS-001: failure list TBD, injection mechanism TBD, timing and duration TBD, excluded failures TBD with rationale TBD.
Flow elaboration TBD per REQ-HFPX-MFS-002: receiving FTC threads TBD, receiving FHA threads TBD, evidence packaging TBD, VCRM and hazard-log rows TBD.
Verdict elaboration TBD per REQ-HFPX-MFS-003: pass criteria TBD, fail criteria TBD, indeterminate handling TBD.
Correlation elaboration TBD per REQ-HFPX-MFS-004: compared quantities TBD, comparison method TBD, discrepancy handling TBD, closure authority TBD.
No values are baselined in this revision.

## 9. Interfaces

- Failure sim ↔ Models (Chapters 19.2–19.8): model revisions and validity bounds feed failure runs
- Failure sim ↔ FTC/FHA (IDs TBD) and Vol 13/24: evidence flows to tolerance and hazard threads; closure owned by safety authorities
- Failure sim ↔ HIL (Chapter 19.9): simulated failures inform HIL fault-injection scope where applicable; execution separation maintained
- Failure sim ↔ Unmanned test (Vol 23): test observations feed correlation; correlation does not replace test verdicts

## 10. Operational Concept

Failure simulation operates inventory-to-verdict-to-correlation: record models and inventory revision → execute injected-failure runs → assess against pass and fail rules → trace to FTC/FHA → correlate with unmanned-test observations where applicable.
Re-assessment is required after any change invalidating recorded inputs, with scope defined per change record (details TBD).
Cadence, staffing, and tooling TBD in child documents.

## 11. Safety

Safety-relevant failure threads receive independent review to a degree TBD, with review records feeding hazard-closure evidence paths owned by the Safety Case.
Simulation evidence alone does not close hazard threads and does not authorise human flight.
Failure handling credited in safety threads shall identify the deterministic bounded function actually assessed; method TBD.

## 12. Performance

Failure-simulation performance indicators TBD; no thresholds baselined: inventory coverage TBD, verdict closure TBD, FTC/FHA trace completeness TBD, correlation closure TBD.
Measurement method and reporting cadence TBD in child documents.

## 13. Verification & Validation

This document is verified at gated reviews against the document template checklist (header, structure, IDs, method on every requirement, TBD discipline).
Failure-simulation cases (IDs TBD) shall each define objective, traced parent requirement and receiving FTC/FHA thread, injected failure, configuration, and acceptance criteria TBD per case before execution.
Validation of the failure-simulation approach is programme-authority approval at gated reviews; certification validation is owned by Vol 25 with no claims here.

## 14. Risks

- Injected-failure inventory incomplete, leaving credible failures unassessed; mitigation: inventory review against FTC/FHA sources (method TBD)
- Pass and fail rules left TBD, blocking verdict defensibility; mitigation: per-case TBD tracking with owning role and due gate (assignments TBD)
- Simulation-to-test divergence undetected without correlation discipline; mitigation: REQ-HFPX-MFS-004 correlation rule with discrepancy handling (method TBD)

## 15. Open Issues

Injected-failure list and injection points TBD. FTC/FHA mapping TBD. Pass and fail criteria TBD. Correlation method and closure rule TBD. Tooling and revision control TBD. All failure-simulation case IDs TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on VV Plan methodology, models from Chapters 19.2–19.8, MST tier direction (IDs TBD), FTC/FHA sources and Vol 13/24 hazard closure paths, HIL fault-injection scope (Chapter 19.9), and Vol 23 unmanned-test data.

## 18. Traceability

Parents: REQ-HFPX-VVP-001 (verification method); REQ-HFPX-VVP-004 (gated progression context); MST tier (IDs TBD); model chapters 19.2–19.8 (IDs TBD).
Children: failure-simulation cases and result records (IDs TBD; rows TBD in VCRM and hazard log).
RTM: REQ-HFPX-MFS-001..004 → CONCEPT. No orphaned requirements; no orphaned verification cases per REQ-HFPX-VVP-002 principle.

## 19. Configuration

BL-0.0. Tranche 5 draft, CONCEPT, not baselined. Future changes via change records; any change re-validates affected traceability before verification claims.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 draft (Chapter 19.13 failure inventory, FTC/FHA flow, verdicts, correlation; structure only) |
