# Time Synchronisation

**Document ID:** HFPX-AVN-TSY-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define avionics time-synchronisation requirements, architecture, interfaces and verification scaffolding (Chapter 08.16). Establishes structure only; time-source hierarchy, sync accuracy, loss-of-sync behaviour and verification are TBD.

## 2. Scope

Covers time-source hierarchy, synchronisation distribution, sync-accuracy provisions, loss-of-sync behaviour and verification methodology across avionics nodes. Source selections, accuracy values, holdover provisions and protocol selections are TBD. No numeric values are allocated in this document.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (notably REQ-HFPX-SYS-002, REQ-HFPX-SYS-003, REQ-HFPX-SYS-005)
- HFPX-ARC-AVN-001 Avionics Architecture
- VAA tier requirements (TBD)
- Vol 13 — safety analyses (notably SFA/CCA hooks)

## 4. Definitions & Acronyms

- Time-source hierarchy: ordered set of time references for avionics; hierarchy TBD.
- Sync accuracy: agreement of node time references; values TBD.
- Loss of sync: condition where synchronisation cannot be maintained; behaviour TBD.
- Holdover: operation on local time during loss of sync; provisions TBD.
- TBD: To Be Determined.

## 5. System Context

Time synchronisation provides a common time reference across avionics nodes for event correlation, fault records and logging. It consumes source inputs, distributes time across networks, and annunciates loss of sync to health monitoring and logging. All mechanisms and values TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-VTS-001 | The avionics time-source hierarchy shall be defined; all sources and ordering TBD. | REQ-HFPX-SYS-002, REQ-HFPX-SYS-003 | Inspection |
| REQ-HFPX-VTS-002 | Time-sync accuracy provisions shall be defined; accuracy claims TBD. | REQ-HFPX-SYS-003 | Analysis |
| REQ-HFPX-VTS-003 | Loss-of-sync behaviour, including annunciation and holdover provisions, shall be defined; behaviour TBD. | REQ-HFPX-SYS-003, SFA hook | Analysis + Test |
| REQ-HFPX-VTS-004 | Time synchronisation shall be verified; methods and acceptance criteria TBD. | REQ-HFPX-SYS-005, VAA tier | Analysis / Test |

## 7. Architecture

Time-sync architecture (structure only): TIME SOURCES (hierarchy TBD) → DISTRIBUTION (mechanism TBD) → NODE SYNC (accuracy TBD) → LOSS-OF-SYNC HANDLING (annunciation and holdover, TBD), with logging correlation hooks (Ch 08.17, TBD) and SFA/CCA hooks (Vol 13, TBD).

## 8. Detailed Design

Not applicable at CONCEPT. Source implementations, protocols, accuracy budgets, holdover logic and monitoring thresholds are TBD and deferred. No design values stated.

## 9. Interfaces

- From time sources: source inputs — TBD.
- Across avionics networks: time distribution paths — TBD.
- To health/fault logic: loss-of-sync annunciations — TBD.
- To logging (Ch 08.17): correlated timestamps — TBD.
- To verification thread (VAA tier): sync verification hooks — TBD.
- To Vol 13: SFA/CCA hooks — TBD.

## 10. Operational Concept

Time sync supports all avionics operating states including degraded modes. On loss of sync, nodes operate per defined holdover and annunciation provisions pending restoration. No operational sync values are stated.

## 11. Safety

Incorrect timestamps, undetected loss of sync or unbounded holdover drift are hazardous to fault correlation and logging: REQ-HFPX-VTS-002 (accuracy provisions), REQ-HFPX-VTS-003 (loss-of-sync behaviour) and SFA hooks mitigate them. No accuracy claim is made; all capability TBD and unproven at CONCEPT.

## 12. Performance

Sync accuracy, convergence behaviour, holdover endurance and resource budgets are TBD. Budget holder: this document (REQ-HFPX-VTS-001..003) with Vol 13. No values stated.

## 13. Verification & Validation

Verified by inspection (source hierarchy) and analysis/test (accuracy, loss-of-sync behaviour and sync verification) per VAA tier. Cases trace to REQ-HFPX-VTS-001..004; methods and acceptance criteria TBD. No gate skipping.

## 14. Risks

- Time-source dependence with undefined fallback; mitigation: hierarchy with holdover required by REQ-HFPX-VTS-001/003.
- Undetected sync divergence corrupting correlation; mitigation: defined accuracy and loss-of-sync provisions with verification.
- Logging correlation unproven; mitigation: timestamp hooks to Ch 08.17 owned as TBD.

## 15. Open Issues

Time-source hierarchy, sync accuracy, loss-of-sync behaviour and holdover, and verification methods/criteria are all TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SyRS SYS-002/003/005, VAA tier, data-bus provisions (08.06), health monitoring (08.10), data logging (08.17), and Vol 13 SFA/CCA hooks.

## 18. Traceability

Parents: REQ-HFPX-SYS-002, REQ-HFPX-SYS-003, REQ-HFPX-SYS-005; VAA tier; SFA/CCA hooks. Children: detailed sync design, distribution ICDs, holdover logic, V&V evidence (all TBD). RTM: REQ-HFPX-VTS-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 5 draft, not baselined. Chapter 08.16.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 draft (Chapter 08.16) |
