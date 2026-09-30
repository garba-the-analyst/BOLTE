# 19.9 Hardware-in-the-Loop

**Document ID:** HFPX-SIM-HIL-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the Hardware-in-the-Loop scope, promotion criteria, real-time performance criteria, and fault-injection scope for HFP-X simulation.
Establishes methodology and gating only; contains no hardware build, integration, or operation instructions.
This document owns Chapter 19.9 direction under Volume 19.

## 2. Scope

Covers HIL testing with flight computer and safety computer in the loop, HIL entry and promotion discipline, real-time execution criteria, and HIL fault-injection scope.
Applies from early integration through gated progression toward unmanned testing; detailed procedures and cases are owned by child documents (IDs TBD).
Excludes software-only verification (owned by Chapter 19.10), model development (owned by Chapters 19.2–19.8), and test execution conduct (owned by Vol 23).

## 3. Applicable Documents

- HFPX-VV-PLN-001 VV Plan, notably REQ-HFPX-VVP-001 (verification method) and REQ-HFPX-VVP-004 (gated sim to SIL to HIL to unmanned testing, no gate skipping)
- Volume 19 model chapters 19.2–19.8 (IDs TBD) for models and flight-control laws exercised in HIL
- MST tier (IDs TBD)
- Vol 23 execution volumes (IDs TBD) for HIL rig operation and results capture
- Vol 25 certification volumes (IDs TBD) — no certification credit claimed in this revision

## 4. Definitions & Acronyms

- HIL: Hardware-in-the-Loop — closed-loop simulation with representative flight hardware executing in the loop
- SIL: Software/System Integration Laboratory
- Promotion: formal gate decision to progress between verification levels, with entrance criteria, completed evidence, and recorded decision
- Real-time: execution paced to wall-clock with bounded timing behaviour; bounds TBD
- Fault injection: intentional introduction of simulated failures to observe system response; scope TBD

## 5. System Context

HIL sits on the right-hand side of the programme V-model between SIL and unmanned testing:

```text
MODELS → SIL → HIL → UNMANNED TESTING
   ↑________ VCRM TRACEABILITY ________↑
   ↑________ GATED PROGRESSION ________↑
```

HIL exercises flight computer and safety computer hardware against simulated plant and environment models. HIL does not replace SIL, analysis, or flight testing and does not authorise flight.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-MHL-001 | The programme shall define the HIL scope with flight computer and safety computer in the loop; hardware list, interfaces, and simulated counterparts TBD. | REQ-HFPX-VVP-001 | Inspection |
| REQ-HFPX-MHL-002 | The programme shall define HIL-to-SIL promotion criteria governing entry to HIL from SIL and re-entry to SIL from HIL; criteria TBD. | REQ-HFPX-VVP-004 | Demonstration |
| REQ-HFPX-MHL-003 | The programme shall define HIL real-time performance criteria; timing bounds, measurement method, and acceptance thresholds TBD. | REQ-HFPX-VVP-001 | Test |
| REQ-HFPX-MHL-004 | The programme shall define the HIL fault-injection scope; injected faults, injection points, and exclusions TBD. | REQ-HFPX-VVP-001 | Inspection |

## 7. Architecture

HIL organisation (roles TBD): HIL lead, simulation backbone owner, flight computer and safety computer providers, independent reviewer TBD.
HIL rig structure TBD: simulation backbone hosting plant and environment models from Chapters 19.2–19.8, interface to flight computer hardware (configuration TBD), interface to safety computer hardware (configuration TBD), recording and timing infrastructure TBD.
Only configurations recorded as TBD-closed in child documents support gate claims; rig configuration control TBD.

## 8. Detailed Design

HIL scope elaboration TBD per REQ-HFPX-MHL-001: hardware identity TBD, interface definitions TBD, model versions TBD, test article representativeness TBD.
Promotion elaboration TBD per REQ-HFPX-MHL-002: entrance criteria TBD, required SIL evidence TBD, exit criteria TBD, decision authority TBD.
Real-time elaboration TBD per REQ-HFPX-MHL-003: timing metrics TBD, instrumentation TBD, acceptance rule TBD.
Fault-injection elaboration TBD per REQ-HFPX-MHL-004: fault list TBD, injection mechanism TBD, safety interlocks TBD.
No values are baselined in this revision.

## 9. Interfaces

- HIL ↔ SIL (Chapter 19.10): SIL evidence feeds HIL entrance; HIL findings feed SIL re-entry
- HIL ↔ Models (Chapters 19.2–19.8): model versions and validity bounds feed HIL configuration
- HIL ↔ Safety (Vol 13/24): safety-relevant HIL threads identified for independent review; degree of independence TBD
- HIL ↔ Test execution (Vol 23): rig procedures, results, and anomaly handling owned by Vol 23; this document defines scope and criteria only

## 10. Operational Concept

HIL operates gate-to-gate: define scope and criteria early → configure rig per recorded revision → execute witnessed runs → capture evidence → gate decision before progression to unmanned testing.
No gate skipping is permitted per REQ-HFPX-VVP-004; each gate requires entrance criteria, completed evidence, and formal recorded decision.
Cadence, staffing, and tooling TBD in child documents.

## 11. Safety

Safety computer participation in HIL does not constitute safety verification closure; closure evidence and independence are owned by the Safety Case and Vol 22/24 paths.
HIL fault injection shall respect rig safety constraints TBD; interlocks and abort behaviours TBD.
No human-flight claim is made from HIL evidence in this revision.

## 12. Performance

HIL performance indicators TBD; no thresholds baselined: real-time compliance TBD, run repeatability TBD, rig availability TBD, evidence closure burn-down TBD.
Measurement method and reporting cadence TBD in child documents.

## 13. Verification & Validation

This document is verified at gated reviews against the document template checklist (header, structure, IDs, method on every requirement, TBD discipline, no-skipping alignment).
HIL verification cases (IDs TBD) shall each define objective, traced parent requirement, method, configuration under test, and acceptance criteria TBD per case before execution.
Validation of the HIL approach is programme-authority approval at gated reviews; certification validation is owned by Vol 25 with no claims here.

## 14. Risks

- Rig configuration drift from SIL-validated models producing invalid HIL evidence; mitigation: configuration record per run with model revision trace (mechanism TBD)
- Pressure to enter HIL without SIL closure; mitigation: REQ-HFPX-MHL-002 promotion criteria with formal gate records
- Real-time criteria left TBD indefinitely, blocking closure; mitigation: per-criterion TBD tracking with owning role and due gate (assignments TBD)

## 15. Open Issues

HIL hardware list TBD. Interface definitions TBD. HIL-to-SIL promotion criteria TBD. Real-time bounds and measurement TBD. Fault-injection inventory and mechanism TBD. Rig tooling and configuration control TBD. All verification case IDs TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on VV Plan gated progression, SIL evidence (Chapter 19.10), models and laws from Chapters 19.2–19.8, MST tier direction (IDs TBD), Vol 23 rig and execution capability, and Vol 25 credit rules.

## 18. Traceability

Parents: REQ-HFPX-VVP-001 (verification method); REQ-HFPX-VVP-004 (gated progression, no skipping); MST tier (IDs TBD); model chapters 19.2–19.8 (IDs TBD).
Children: HIL verification cases and procedures (IDs TBD; rows TBD in VCRM).
RTM: REQ-HFPX-MHL-001..004 → CONCEPT. No orphaned requirements; no orphaned verification cases per REQ-HFPX-VVP-002 principle.

## 19. Configuration

BL-0.0. Tranche 5 draft, CONCEPT, not baselined. Future changes via change records; any change re-validates affected traceability before gate claims.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 draft (Chapter 19.9 HIL scope, promotion, real-time, fault injection; structure only) |
