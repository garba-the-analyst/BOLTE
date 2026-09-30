# Landing Procedures

**Document ID:** HFPX-OPS-LND-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X landing procedures framework (Chapter 26.9): landing-procedure structure, abort structure, unmanned-first gating and verification structure. All structures, criteria and methods are TBD.

## 2. Scope

Covers landing procedures at structure-only level from approach and descent through touchdown and shutdown, including procedure structure, abort hooks and verification approach. Excludes executable flight-operation instructions, profile values, threshold values and capability values — all TBD. No executable flight-operation instructions are given in this document.

## 3. Applicable Documents

- HFPX-SYS-CON-001 CONOPS (nominal and off-nominal threads); OPC tier (allocation TBD); OLI tier Vol 26.2 (allocation TBD)
- Vol 07 flight control hooks (landing control laws, allocation TBD); Vol 13 safety hooks (allocation TBD); Vol 23 test hooks (allocation TBD)
- HFP prompt operations and MVP progression sections (values TBD)

## 4. Definitions & Acronyms

- Landing-procedure structure: the ordered set of procedure placeholders for descent, touchdown and shutdown (structure TBD).
- Abort: discontinuation of landing and return to a hold or alternate state (criteria and capability TBD).
- Unmanned-first: gating of human exposure on completed unmanned progression (gating TBD).
- OLI: operating limitations tier (Vol 26.2, allocation TBD).

## 5. System Context

Landing procedures sit within the operations volume as the terminal-phase procedure set, used by operator, pilot and ground crew with the vehicle, ground station and range. Entry conditions, envelopes, vehicle configuration and abort authority are TBD and owned with OPC, CON, OLI, Vol 07, Vol 13 and Vol 23.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-OLP-001|The operations volume shall define the landing-procedure structure for descent through touchdown and shutdown (structure TBD).|OPC tier, CON tier (HFPX-SYS-CON-001), OLI tier (Vol 26.2, allocation TBD)|Inspection|
|REQ-HFPX-OLP-002|The landing procedures shall define the abort structure with criteria and handover (abort TBD).|CON tier, OLI tier, Vol 13 hook (allocation TBD)|Inspection|
|REQ-HFPX-OLP-003|Landing procedures shall be gated on unmanned-first progression before any human exposure (gating TBD).|CON tier, Vol 23 hook (allocation TBD)|Test|
|REQ-HFPX-OLP-004|The landing procedures shall define the verification structure for procedures and aborts (methods TBD).|OPC tier, Vol 23 hook (allocation TBD)|Inspection|

## 7. Architecture

Procedure framework with placeholders for approach, descent, touchdown, shutdown and abort branches (all TBD), linked to OLI bounds, CON threads and Vol 07 control hooks. Structure only; sequencing, decision logic and values are TBD in later Vol 26 detail.

## 8. Detailed Design

Not applicable at Tranche 6 draft level. Procedure steps, profiles, thresholds, abort sequences and checklists are TBD. No executable flight-operation instructions are stated; detailed procedures will be owned in later Vol 26 revisions.

## 9. Interfaces

Interfaces to OLI bounds, CONOPS threads, flight control laws, navigation and height sensing, safety monitoring, ground station displays and test range artefacts are TBD. Each shall be captured in an ICD before CDR (method TBD).

## 10. Operational Concept

Landing supports nominal vertical landing and aborted landing within the CONOPS thread (profiles TBD). Normal and off-nominal paths are represented as structure only with abort handover to the safety path (capability TBD). All validation is unmanned first. No executable flight-operation instructions are given.

## 11. Safety

Hard touchdown, tip-over, cutoff failure or failed abort is hazardous: bounded procedure structure (OLP-001), explicit abort hooks (OLP-002) and unmanned-first gating (OLP-003) plus the independent safety path mitigate it. No controllability or margin claim is made; all thresholds TBD pending Vol 07 and Vol 13 analysis and unmanned test.

## 12. Performance

Descent profiles, touchdown performance, abort capability bounds and crew workload budgets are TBD. No altitudes, rates or margin values are stated.

## 13. Verification & Validation

Verified by inspection and analysis of procedure structure and abort hooks and validated by unmanned progression (methods TBD, Vol 23). Abort and failure cases are covered by fault-injection hooks (methods TBD).

## 14. Risks

- Procedure to design mismatch (procedures assume capability the design lacks); mitigation: explicit TBD hooks to Vol 07 and Vol 13, TBD.
- Abort capability TBD — go-around may not be achievable in all states; mitigation: capability stub explicit, verification unmanned first.

## 15. Open Issues

Landing-procedure structure TBD; abort criteria and handover TBD; unmanned-first gating TBD; verification scope and methods TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on OPC tier, CON tier (HFPX-SYS-CON-001), OLI tier (Vol 26.2), Vol 07 landing control, Vol 13 safety view and Vol 23 test progression.

## 18. Traceability

Parents: OPC tier; CON tier (HFPX-SYS-CON-001); OLI tier (Vol 26.2); Vol 07, Vol 13 and Vol 23 hooks (allocations TBD). Children: Vol 26 detailed landing procedures, V&V cases. RTM: REQ-HFPX-OLP-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 26.9) |
