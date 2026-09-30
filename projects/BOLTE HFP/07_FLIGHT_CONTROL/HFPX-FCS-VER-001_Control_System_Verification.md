# Control System Verification

**Document ID:** HFPX-FCS-VER-001  
**Revision:** B (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 3 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X control-system verification thread (Chapter 07.19): the ordered sim → SIL → HIL → unmanned-test sequence for laws, mixing, and allocation with no gate skipping, verification-case traceability, per-case acceptance criteria ownership, and regression policy on law changes.

## 2. Scope

Covers verification ownership and methodology for control laws (FCR/FCL), mixing (FMX), allocation (FAC), and fault-tolerant control (FFT) for the production-aircraft concept. All cases, criteria, thresholds, gains, margins, and limits are TBD. Verification ownership and methods only — no numeric values are allocated in this document.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (REQ-HFPX-SYS-001, SYS-002, SYS-003)
- HFPX-SYS-ARC-001 SAD (ARC-004)
- HFPX-ARC-CTL-001 Control Architecture (CTL-001, CTL-002, CTL-003, CTL-004)
- Vol 07 law/mixing/allocation/authority/FTC documents (Ch 07.15–07.18); HFPX-VVP-001/004 V&V (VVP-001, VVP-004)
- HFPX-SFA-001 Safety Architecture (SFA-001); Vol 19 (modelling/SIL/HIL); Vol 33 (flight test)

## 4. Definitions & Acronyms

- Verification thread: ordered sequence sim → SIL → HIL → unmanned test; gates between stages, no skipping.
- Verification case: a defined check tracing to one or more of FCR/FCL/FMX/FAC/FFT requirements; contents TBD.
- Acceptance criteria: per-case pass/fail definition; all TBD per case.
- Regression: re-verification required after law (or paired mixing/allocation) changes; scope TBD.
- FCR/FCL/FMX/FAC/FFT: requirement families for laws, mixing, allocation, fault-tolerance. TBD: To Be Determined.

## 5. System Context

The verification thread consumes control-law, mixing, allocation, authority, and FTC definitions plus models (Vol 19) and produces staged evidence: desktop-sim results, SIL results, HIL results, and unmanned-test results. Each stage gates the next. Safety evidence (SFA-001) and authority gates (ISS-006, HFPX-FCS-AUT-001) draw on this thread. Trace from cases to parent requirements is maintained throughout.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-FVV-001 | Control laws, mixing, and allocation shall be verified through the ordered thread sim → SIL → HIL → unmanned test with no gate skipping; stage entry/exit criteria TBD. | VVP-001, CTL-001, CTL-002 | Analysis + Test |
| REQ-HFPX-FVV-002 | Each verification case shall trace to one or more of FCR/FCL/FMX/FAC/FFT requirements; case list and trace TBD. | VVP-004, ARC-004 | Inspection |
| REQ-HFPX-FVV-003 | Acceptance criteria shall be defined per verification case; all criteria TBD per case. | VVP-001, VVP-004 | Inspection |
| REQ-HFPX-FVV-004 | A regression policy shall require defined re-verification on any control-law change (including paired mixing/allocation changes); scope and triggers TBD. | VVP-004, ARC-004, CTL-001 | Inspection |

## 7. Architecture

Verification thread owned by FCS V&V (owner TBD) with four gated stages: desktop sim (models TBD), SIL (setup TBD), HIL (rig TBD), unmanned test (range/vehicle TBD). A trace manager links cases to FCR/FCL/FMX/FAC/FFT; a criteria ledger holds per-case acceptance definitions (TBD); a regression controller maps law changes to re-verification scope. Structure and ownership only — no numeric content.

## 8. Detailed Design

Not applicable at Tranche 3 draft level. Stage configurations, case definitions, criteria values, and regression scope tables are TBD (Vol 07, Vol 19, Vol 33).

## 9. Interfaces

- From Vol 07 designs: laws, mixing, allocation, authority, FTC definitions under verification — TBD.
- From Vol 19: sim/SIL/HIL models and rigs — TBD.
- To Vol 33 / flight test: unmanned-test articles and procedures — TBD.
- To safety/V&V (SFA-001, VVP-001/004): evidence artefacts and trace exports — TBD.

## 10. Operational Concept

Verification executes in order for every law/mixing/allocation release: sim first, then SIL, then HIL, then unmanned test. Failure at any stage blocks progression (no gate skipping). Regression runs the same thread over the affected scope after any law change. No operational test values are stated.

## 11. Safety

Skipped gates, untraced cases, undefined acceptance, or unregressed law changes are hazardous (unverified control reaching flight): REQ-HFPX-FVV-001 (no gate skipping), REQ-HFPX-FVV-002 (full trace), REQ-HFPX-FVV-003 (per-case acceptance), and REQ-HFPX-FVV-004 (regression) plus the safety path (SFA-001) mitigate it. No verification claim is made; all cases and criteria TBD.

## 12. Performance

Sim fidelity targets, SIL/HIL coverage metrics, test-point counts, and schedule budgets are TBD. No allocation value is stated. Methods for metric definition are TBD (Vol 19/33).

## 13. Verification & Validation

This document defines the verification thread; it is itself verified by inspection of case trace (FVV-002), criteria ledger completeness (FVV-003), gate records (FVV-001), and regression records (FVV-004) per VVP-004. Validation of control behaviour closes in unmanned flight (Vol 33). Acceptance criteria for this thread's own artefacts are TBD.

## 14. Risks

- Gate skipping under schedule pressure; mitigation: REQ-HFPX-FVV-001 explicit no-skip rule with recorded gate evidence.
- Trace gaps between cases and FCR/FCL/FMX/FAC/FFT; mitigation: REQ-HFPX-FVV-002 trace requirement, ledger TBD.
- Unregressed law changes reaching flight; mitigation: REQ-HFPX-FVV-004 regression policy, scope TBD.

## 15. Open Issues

Stage entry/exit criteria TBD; case list and trace TBD; per-case acceptance criteria TBD; regression scope/triggers TBD; thread owner TBD; sim/SIL/HIL/test configurations TBD.

## 16. Assumptions


_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SAD (ARC-004), Control Architecture (CTL-001..004), Vol 07 designs (laws, HFPX-FCS-MIX-001, HFPX-FCS-ALC-001, HFPX-FCS-AUT-001, HFPX-FCS-FTC-001), safety view (SFA-001), V&V thread (VVP-001/004), Vol 19 (SIL/HIL), Vol 33 (flight test).

## 18. Traceability

Parents: SYS-001, SYS-002, SYS-003; ARC-004; CTL-001, CTL-002, CTL-003, CTL-004; SFA-001; VVP-001, VVP-004. Children: verification cases, criteria ledger, gate/regression records (all TBD). RTM: REQ-HFPX-FVV-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 3 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 3 draft (Chapter 07.19) |
| B | 2026-09-29 | Assumptions removed; all unknowns recorded as TBD (no assumptions raised or relied upon). |
