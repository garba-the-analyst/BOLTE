# System Verification

**Document ID:** HFPX-VV-SYV-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 8 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define system verification for Volume 22.11, covering system level cases, environments, interface threads, and records across hardware and software integration.
Methodology only; detailed procedures remain with Vol 23.

## 2. Scope

Covers end-to-end and interface verification at system level through gated progression including SIL, HIL, and unmanned stages where allocated.
Component verification remains with Vol 22.9 and Vol 22.10; safety independent threads with Vol 22.12; acceptance with Vol 22.13.

## 3. Applicable Documents

- HFPX-VV-PLN-001 VV Plan (REQ-HFPX-VVP-001..006 — levels, gating, acceptance, VCRM)
- HFPX-PGM-SEM-001 SEMP (gated reviews)
- HFPX-SYS-REQ-001 SyRS §13, HFPX-SYS-ARC-001 SAD (stub)
- Vol 22.3 (VCRM), Vol 23 (execution), Vol 13 (hazards), Vol 02 interface provisions TBD

## 4. Definitions & Acronyms

- System verification: verification of integrated hardware and software against system requirements in representative environments
- Interface thread: verification across system interfaces including ICD defined threads; scope TBD
- End-to-end thread: verification across operational mission threads; scope TBD
- Environment: system level test configuration and external conditions; detail TBD

## 5. System Context

System verification integrates lower level evidence into system claims through gated stages:

```text
HARDWARE + SOFTWARE → INTEGRATE → SYSTEM VERIFY → ACCEPT
        ↑________ VCRM TRACE (level: system) ________↑
        ↑________ GATED STAGES (criteria TBD) _______↑
```

System threads include interface, functional, and mission threads with allocation TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-VSV-001 | The programme shall verify system requirements through system level cases including interface and end-to-end threads, with case scope recorded as TBD per system thread. | REQ-HFPX-VVP-003 | Demonstration |
| REQ-HFPX-VSV-002 | Each system verification thread shall be executed in a documented environment and configuration, with environment and configuration recorded as TBD per thread. | REQ-HFPX-VVP-004 | Test |
| REQ-HFPX-VSV-003 | Each system verification thread shall define pass and fail criteria before execution, with criteria recorded as TBD per system case. | REQ-HFPX-VVP-005 | Test |
|REQ-HFPX-VSV-004|Each system verification thread shall produce retained records with configuration, environment, and result status traced in the VCRM, with record provisions defined as TBD.|REQ-HFPX-VVP-002|Demonstration + Test|

## 7. Architecture

System verification organisation and integration lead roles TBD under VV governance.
Thread structure: parent system requirement → integrated article and build → environment (SIL, HIL, unmanned where allocated TBD) → observed and measured outcomes → VCRM entry.
Interface threads map to ICD provisions TBD.

## 8. Detailed Design

System cases are planned at SRR and PDR with procedures matured through CDR, TRR, and FRR stages; case and procedure IDs TBD in Vol 23 children.
Each system case template shall contain objective, traced parents, method, level, environment and configuration (TBD per case), pass and fail criteria (TBD per case), and independence claim where applicable.
Regression on system or interface change re-opens affected rows until re-verified; scope per change record TBD.

## 9. Interfaces

- System verification ↔ Hardware and Software verification (Vol 22.9 and Vol 22.10 evidence roll-up)
- System verification ↔ Vol 23 (SIL, HIL, ground, and unmanned execution)
- System verification ↔ VCRM (Vol 22.3 traceability and gate evidence)
- System verification ↔ Safety and Certification (Vol 13, Safety Case, Vol 25)

## 10. Operational Concept

System verification operates integrate-to-prove: integrate articles and builds → configure environments → execute interface and mission threads through gates → record outcomes → close in VCRM.
Sequencing, venues, and board provisions TBD.

## 11. Safety

System threads covering hazard controls are flagged in the VCRM with independence provisions TBD.
System verification does not authorise human flight; human flight gating requires FRR authorisation with criteria TBD and Safety Case ownership.

## 12. Performance

System verification indicators TBD, with all thresholds TBD: thread coverage, environment readiness, criteria definition backlog, closure burn-down.
Measurement method and reporting cadence TBD.

## 13. Verification & Validation

This document is verified by Inspection against the VV Plan and SEMP checklist (header, 20 sections, IDs, parents, allowed methods only).
Validation of the system approach is programme authority approval at gated reviews; certification validation owned by Vol 25.

## 14. Risks

- Environment fidelity shortfalls weakening system claims; mitigation: environment criteria per REQ-HFPX-VSV-002 (detail TBD)
- Interface gaps between subsystems; mitigation: ICD based interface threads (scope TBD)
- Criteria left TBD blocking closure; mitigation: per-case TBD tracking (assignments TBD)

## 15. Open Issues

System case IDs TBD. Environments TBD. Interface thread scope TBD. Criteria TBD per case. FRR entrance criteria TBD.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on VV Plan levels and gating, SEMP gates, SyRS §13, SAD allocation, Vol 22.3 VCRM, Vol 22.9 and Vol 22.10 evidence, Vol 23 execution, Safety Case and Vol 25 rules.

## 18. Traceability

Parents: REQ-HFPX-VVP-002, REQ-HFPX-VVP-003, REQ-HFPX-VVP-004, REQ-HFPX-VVP-005. Children: system cases and Vol 23 procedures (IDs TBD; VCRM rows TBD).
RTM: REQ-HFPX-VSV-001..004 → CONCEPT. Coverage tracked in Vol 22.3 VCRM.

## 19. Configuration

BL-0.0. Tranche 8 draft, CONCEPT, not baselined. Future changes via change records; affected VCRM rows re-validated before gate claims.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 8 draft (Vol 22.11 direction; structure only) |
