# Communications Procedures

**Document ID:** HFPX-OPS-CPR-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X communications procedures framework (Chapter 26.13): phraseology and frequency structure, loss-of-link drill structure, records structure and verification structure. All phraseology, frequencies, behaviours and methods are TBD.

## 2. Scope

Covers communications procedures at structure-only level for operator, crew, ground station and range coordination, including phraseology placeholders, frequency hooks, loss-of-link drill hooks to Vol 11.9 and records hooks. Excludes executable flight-operation instructions, phraseology text, frequency values and drill sequences — all TBD. No executable flight-operation instructions are given in this document.

## 3. Applicable Documents

- HFPX-SYS-CON-001 CONOPS (actors and interfaces); OPC tier (allocation TBD); OLI tier Vol 26.2 (allocation TBD)
- Vol 11 comms hooks including Vol 11.9 loss of link (allocation TBD); Vol 13 safety hooks (allocation TBD); Vol 23 test hooks (allocation TBD)
- HFP prompt operations and MVP progression sections (values TBD)

## 4. Definitions & Acronyms

- Phraseology and frequencies: standard words and channels for coordination (both TBD).
- Loss-of-link drills: practiced responses to comms or telemetry loss (behaviour TBD, Vol 11.9 hook).
- Records: retained comms logs and drill records (retention TBD).
- OLI: operating limitations tier (Vol 26.2, allocation TBD).

## 5. System Context

Communications procedures link operator, pilot, ground crew, ground station and range across nominal and off-nominal threads. Link designs, handover rules, alerting and range protocols are TBD and owned with OPC, CON, OLI, Vol 11 and Vol 13.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-OCM-001|The operations volume shall define the phraseology and frequency structure (phraseology and frequencies TBD).|OPC tier, CON tier (HFPX-SYS-CON-001), OLI tier (Vol 26.2, allocation TBD)|Inspection|
|REQ-HFPX-OCM-002|Communications procedures shall define the loss-of-link drill structure consistent with the Vol 11.9 hook (behaviour TBD).|CON tier, Vol 11 hook including Vol 11.9 (allocation TBD)|Demonstration|
|REQ-HFPX-OCM-003|Communications procedures shall define the records structure for logs and drill records (retention TBD).|OPC tier, Vol 27 and Vol 28 hooks (allocations TBD)|Demonstration|
|REQ-HFPX-OCM-004|Communications procedures shall define the verification structure for phraseology, drills and records (methods TBD).|OPC tier, Vol 23 hook (allocation TBD)|Demonstration|

## 7. Architecture

Procedure framework with placeholders for nominal coordination, handover, loss-of-link branches and records capture (all TBD), linked to CON threads and Vol 11.9 behaviour hooks. Structure only; scripts, channels and logic are TBD in later Vol 26 detail.

## 8. Detailed Design

Not applicable at Tranche 6 draft level. Phraseology lists, frequency plans, drill scripts and log formats are TBD. No executable flight-operation instructions are stated; detailed procedures will be owned in later Vol 26 revisions.

## 9. Interfaces

Interfaces to OLI bounds, CONOPS actors, Vol 11 links and telemetry, HMI displays, recording systems and range nets are TBD. Each shall be captured in an ICD before CDR (method TBD).

## 10. Operational Concept

Comms support nominal coordination and handover plus off-nominal loss-of-link handling within the CONOPS thread (thresholds TBD), with drills and handover to the safety path represented as structure only under Vol 11.9 hooks (TBD). All validation is unmanned first. No executable flight-operation instructions are given.

## 11. Safety

Lost, unclear or misrouted comms during critical phases is hazardous: bounded phraseology structure (OCM-001), explicit loss-of-link drill hooks (OCM-002) and records hooks (OCM-003) plus the independent safety path mitigate it. No availability or latency claim is made; all behaviours TBD pending Vol 11 and Vol 13 analysis and unmanned test.

## 12. Performance

Link availability, handover latencies, drill timing and recording completeness budgets are TBD. No time, rate or margin values are stated.

## 13. Verification & Validation

Verified by inspection and analysis of phraseology structure, drill hooks and records hooks and validated by unmanned progression and drill records (methods TBD, Vol 23). Loss-of-link cases are covered by fault-injection hooks with Vol 11 (methods TBD).

## 14. Risks

- Link-loss behaviour TBD — mid-phase loss may be undefined; mitigation: explicit Vol 11.9 hook and drill stub, TBD.
- Phraseology TBD — coordination errors possible before detail matures; mitigation: phraseology stub explicit, verification by rehearsal records.

## 15. Open Issues

Phraseology and frequencies TBD; loss-of-link drill behaviour TBD with Vol 11.9 hook; records retention TBD; verification scope and methods TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on OPC tier, CON tier (HFPX-SYS-CON-001), OLI tier (Vol 26.2), Vol 11 comms including Vol 11.9, Vol 13 safety view, Vol 23 test progression and Vol 27 and Vol 28 records hooks.

## 18. Traceability

Parents: OPC tier; CON tier (HFPX-SYS-CON-001); OLI tier (Vol 26.2); Vol 11 including Vol 11.9, Vol 13, Vol 23, Vol 27 and Vol 28 hooks (allocations TBD). Children: Vol 26 detailed comms procedures, V&V cases. RTM: REQ-HFPX-OCM-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 26.13) |
