# Emergency Procedures

**Document ID:** HFPX-OPS-EMG-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X operations-level emergency procedures framework (Chapter 26.10): emergency-action structure, authority hooks, rehearsal structure and verification structure. All actions, authorities and methods are TBD.

## 2. Scope

Covers operations-level emergency actions at structure-only level, including action placeholders, authority hooks to Vol 13.8, rehearsal hooks and verification approach. Excludes executable flight-operation instructions, trigger values, response sequences and authority values — all TBD. No executable flight-operation instructions are given in this document.

## 3. Applicable Documents

- HFPX-SYS-CON-001 CONOPS (off-nominal threads); OPC tier (allocation TBD); OLI tier Vol 26.2 (allocation TBD)
- Vol 13 safety hooks including Vol 13.8 authority (allocation TBD); Vol 23 test hooks (allocation TBD); Vol 11 comms hooks (allocation TBD)
- HFP prompt operations and MVP progression sections (values TBD)

## 4. Definitions & Acronyms

- Operations-level emergency actions: operator and crew responses to declared emergencies (actions TBD).
- Authority: power to direct abort, stabilisation, recovery or termination (authority TBD, Vol 13.8 hook).
- Rehearsal: practice of emergency roles and handover (scope TBD).
- OLI: operating limitations tier (Vol 26.2, allocation TBD).

## 5. System Context

Emergency procedures sit above system-level fault responses as the crew and operator layer, used with the vehicle, ground station, safety path and range. Detecting systems, mitigating systems and crew actions per CONOPS are TBD and owned with OPC, CON, OLI, Vol 13 and Vol 23.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-OEP-001|The operations volume shall define the operations-level emergency-action structure (actions TBD).|OPC tier, CON tier (HFPX-SYS-CON-001), OLI tier (Vol 26.2, allocation TBD)|Inspection|
|REQ-HFPX-OEP-002|Emergency procedures shall define authority hooks consistent with the Vol 13.8 authority (authority TBD).|CON tier, Vol 13 hook including Vol 13.8 (allocation TBD)|Inspection|
|REQ-HFPX-OEP-003|Emergency procedures shall define the rehearsal structure for roles and handover (scope TBD).|OPC tier, Vol 23 hook (allocation TBD)|Demonstration|
|REQ-HFPX-OEP-004|Emergency procedures shall define the verification structure for actions, authority and rehearsal (methods TBD).|OPC tier, Vol 23 hook (allocation TBD)|Demonstration|

## 7. Architecture

Procedure framework with placeholders for declaration, stabilisation, recovery or abort, handover and safe-state branches (all TBD), linked to CON off-nominal threads and Vol 13.8 authority hooks. Structure only; triggers, sequences and values are TBD in later Vol 26 detail.

## 8. Detailed Design

Not applicable at Tranche 6 draft level. Emergency steps, trigger values, response sequences, authority matrices and rehearsal scripts are TBD. No executable flight-operation instructions are stated; detailed procedures will be owned in later Vol 26 revisions.

## 9. Interfaces

Interfaces to OLI bounds, CONOPS off-nominal threads, safety monitoring and authority, HMI alerts, telemetry, comms and range safety artefacts are TBD. Each shall be captured in an ICD before CDR (method TBD).

## 10. Operational Concept

Emergencies follow detect, stabilise, recover or abort to a safe state within the CONOPS thread (thresholds TBD), with operator and crew roles and handover represented as structure only under Vol 13.8 authority (TBD). All validation is unmanned first. No executable flight-operation instructions are given.

## 11. Safety

Undefined response, unclear authority or unrehearsed handover is hazardous: bounded action structure (OEP-001), explicit authority hooks (OEP-002) and rehearsal structure (OEP-003) plus the independent safety path mitigate it. No capability claim is made; all triggers TBD pending Vol 13 analysis and unmanned test.

## 12. Performance

Response timelines, stabilisation performance, handover latencies and crew workload budgets are TBD. No time, rate or margin values are stated.

## 13. Verification & Validation

Verified by inspection and analysis of action structure, authority hooks and rehearsal plans and validated by unmanned progression and rehearsal records (methods TBD, Vol 23). Fault-injection hooks cover off-nominal cases (methods TBD).

## 14. Risks

- Authority ambiguity between operator, crew, safety path and range; mitigation: explicit Vol 13.8 hook and handover stub, TBD.
- Rehearsal scope TBD — roles may be unproven at first use; mitigation: rehearsal stub explicit, verification unmanned first.

## 15. Open Issues

Emergency-action structure TBD; Vol 13.8 authority allocation TBD; rehearsal scope and methods TBD; verification scope and methods TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on OPC tier, CON tier (HFPX-SYS-CON-001), OLI tier (Vol 26.2), Vol 13 safety view including Vol 13.8, Vol 11 comms and Vol 23 test progression.

## 18. Traceability

Parents: OPC tier; CON tier (HFPX-SYS-CON-001); OLI tier (Vol 26.2); Vol 11, Vol 13 including Vol 13.8 and Vol 23 hooks (allocations TBD). Children: Vol 26 detailed emergency procedures, V&V cases. RTM: REQ-HFPX-OEP-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 26.10) |
