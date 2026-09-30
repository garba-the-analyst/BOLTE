# Hardware Verification

**Document ID:** HFPX-VV-HWV-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 8 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define hardware verification for Volume 22.9, covering bench, rig, and integration threads with coverage and records discipline.
Methodology only; detailed procedures and venues remain with Vol 23.

## 2. Scope

Covers component through subsystem hardware verification where hardware is the verification level.
Software, system end-to-end, and safety independent threads are allocated in Vol 22.10–22.12; method assignment per Vol 22.4.

## 3. Applicable Documents

- HFPX-VV-PLN-001 VV Plan (REQ-HFPX-VVP-001..006 — levels, gating, acceptance, VCRM, independence)
- HFPX-PGM-SEM-001 SEMP (gated reviews)
- HFPX-SYS-REQ-001 SyRS §13, HFPX-SYS-ARC-001 SAD (stub)
- Vol 22.3 (VCRM), Vol 22.8 (test methodology), Vol 23 (execution), Vol 13 (hazards)

## 4. Definitions & Acronyms

- Bench verification: verification at component or unit level on controlled fixtures; setup TBD
- Rig verification: verification on subsystem rigs with representative interfaces; fidelity TBD
- Integration verification: verification across hardware interfaces up to system boundary; scope TBD
- Coverage: mapping of hardware requirements to verification threads; threshold TBD

## 5. System Context

Hardware verification matures articles toward system integration through gated levels:

```text
COMPONENT (bench) → SUBSYSTEM (rig) → INTEGRATED HARDWARE → SYSTEM
        ↑________ VCRM TRACE (level: hardware) ________↑
        ↑________ GATED PROGRESSION (criteria TBD) ____↑
```

Level allocation is recorded in the VCRM per thread.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-VHW-001 | The programme shall verify hardware through bench, rig, and integration threads, with thread scope and environments recorded as TBD per hardware thread. | REQ-HFPX-VVP-003 | Test |
| REQ-HFPX-VHW-002 | Hardware verification shall achieve coverage of allocated hardware requirements, with coverage mapping and thresholds recorded as TBD. | REQ-HFPX-VVP-002 | Test |
| REQ-HFPX-VHW-003 | Each hardware verification thread shall define pass and fail criteria before execution, with criteria recorded as TBD per hardware case. | REQ-HFPX-VVP-005 | Test |
| REQ-HFPX-VHW-004 | Each hardware verification thread shall produce retained records with configuration and environment, with record provisions defined as TBD. | REQ-HFPX-VVP-002 | Test |

## 7. Architecture

Hardware verification organisation and rig ownership TBD under VV and ground test governance.
Level structure: bench (component qualification logic TBD), rig (subsystem environments TBD), integration (interface threads per ICD provisions TBD).
VCRM records level, method, executing volume, configuration, and result per thread.

## 8. Detailed Design

Hardware cases are planned early (SRR and PDR) with procedures matured through CDR and TRR in Vol 23; case and procedure IDs TBD.
Each hardware case template shall contain objective, traced parents, method, level, environment and configuration (TBD per case), instrumentation TBD, acceptance criteria (TBD per case), and independence claim where applicable.
Regression on hardware or requirement change re-opens affected rows until re-verified; scope per change record TBD.

## 9. Interfaces

- Hardware verification ↔ Design volumes (Vol 03–18 test articles and design evidence; ICDs per Vol 02 provisions TBD)
- Hardware verification ↔ Vol 23 (procedures, rigs, venues)
- Hardware verification ↔ VCRM (Vol 22.3 traceability)
- Hardware verification ↔ Safety (Vol 13 hazard-derived hardware threads and closure evidence)

## 10. Operational Concept

Hardware verification operates bench-to-integration: plan threads early → develop rigs and procedures → execute through gates → record results → close in VCRM.
Cadence, rig scheduling, and board provisions TBD.

## 11. Safety

Hazard-derived hardware threads are flagged in the VCRM with independence provisions TBD.
Catastrophic hazard closure evidence is independently verified before human flight gates are considered (criterion TBD, owned by Safety Case).

## 12. Performance

Hardware verification indicators TBD, with all thresholds TBD: coverage, criteria definition backlog, procedure maturity, closure burn-down.
Measurement method and reporting cadence TBD.

## 13. Verification & Validation

This document is verified by Inspection against the VV Plan and SEMP checklist (header, 20 sections, IDs, parents, allowed methods only).
Validation of the hardware approach is programme authority approval at gated reviews; certification validation owned by Vol 25.

## 14. Risks

- Rig fidelity shortfalls weakening integration claims; mitigation: environment representativeness criteria TBD
- Criteria left TBD blocking closure; mitigation: per-case TBD tracking (assignments TBD)
- Interface gaps between hardware elements; mitigation: interface verification threads per ICD provisions TBD

## 15. Open Issues

Bench, rig, and integration scope TBD. Coverage thresholds TBD. Pass and fail criteria TBD per case. Rig fidelity TBD. Records tooling TBD.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on VV Plan levels and gating, SEMP gates, SyRS §13, SAD allocation, Vol 22.3 VCRM, Vol 23 rigs and procedures, Vol 13 safety inputs, Vol 25 credit rules.

## 18. Traceability

Parents: REQ-HFPX-VVP-002, REQ-HFPX-VVP-003, REQ-HFPX-VVP-005. Children: hardware cases and Vol 23 procedures (IDs TBD; VCRM rows TBD).
RTM: REQ-HFPX-VHW-001..004 → CONCEPT. Coverage tracked in Vol 22.3 VCRM.

## 19. Configuration

BL-0.0. Tranche 8 draft, CONCEPT, not baselined. Future changes via change records; affected VCRM rows re-validated before gate claims.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 8 draft (Vol 22.9 direction; structure only) |
