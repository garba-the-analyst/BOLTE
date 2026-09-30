# Software Verification

**Document ID:** HFPX-VV-SWV-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 8 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define software verification for Volume 22.10, covering unit, integration, and system level software threads with coverage and independence discipline.
Methodology only; detailed software assurance and procedures interface with Vol 16.16 and Vol 23.

## 2. Scope

Covers deterministic control software and advisory functions where software is the verification level, including separation provisions TBD.
Hardware, system end-to-end, and safety threads are allocated in Vol 22.9, Vol 22.11, and Vol 22.12.

## 3. Applicable Documents

- HFPX-VV-PLN-001 VV Plan (REQ-HFPX-VVP-001..006 — levels, VCRM, acceptance, independence)
- HFPX-PGM-SEM-001 SEMP (gated reviews)
- HFPX-SYS-REQ-001 SyRS §13, HFPX-SYS-ARC-001 SAD (stub)
- Vol 16.16 (software assurance detail TBD), Vol 22.3 (VCRM), Vol 23 (execution), Vol 13 (hazards)

## 4. Definitions & Acronyms

- Unit verification: verification of software units in isolation; scope TBD
- Integration verification: verification across software interfaces and with target environments; scope TBD
- System level software verification: verification of software behaviour in system context; scope TBD
- Independence: separation between software developer and verifier; degree TBD

## 5. System Context

Software verification matures code toward system integration with separation of deterministic control from advisory functions:

```text
UNIT → INTEGRATION → SYSTEM LEVEL (software) → SYSTEM (Vol 22.11)
  ↑________ VCRM TRACE (level: software) ________↑
  ↑________ INDEPENDENCE (degree TBD) ___________↑
```

Level allocation and coverage are recorded in the VCRM per thread.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-VSW-001 | The programme shall verify software through unit, integration, and system level threads interfacing with Vol 16.16, with thread scope and environments recorded as TBD per software thread. | REQ-HFPX-VVP-003 | Test |
| REQ-HFPX-VSW-002 | Software verification shall achieve coverage of allocated software requirements, with coverage mapping and thresholds recorded as TBD. | REQ-HFPX-VVP-002 | Test |
| REQ-HFPX-VSW-003 | Software verification of safety requirements and safety critical threads shall satisfy independence provisions, with independence degree defined as TBD. | REQ-HFPX-VVP-006 | Test |
| REQ-HFPX-VSW-004 | Each software verification thread shall define pass and fail criteria and records provisions before credit, with criteria and records recorded as TBD per thread. | REQ-HFPX-VVP-005 | Test |

## 7. Architecture

Software verification organisation and verifier roles TBD under VV and software governance.
Thread structure: parent requirement → software build and configuration → test level and environment (SIL and HIL where applicable TBD) → measured result → VCRM entry.
Advisory versus deterministic separation provisions TBD with Vol 16.16.

## 8. Detailed Design

Software cases are planned early with procedures matured through CDR and TRR; case and procedure IDs TBD in Vol 16.16 and Vol 23 children.
Each software case template shall contain objective, traced parents, method, level, build and configuration (TBD per case), environment TBD, pass and fail criteria (TBD per case), and independence claim where applicable.
Regression on software or requirement change re-opens affected rows until re-verified; scope per change record TBD.

## 9. Interfaces

- Software verification ↔ Vol 16.16 (assurance practice, builds, environments)
- Software verification ↔ Vol 23 (SIL, HIL, and execution venues)
- Software verification ↔ VCRM (Vol 22.3 traceability)
- Software verification ↔ Safety (Vol 13 hazard-derived software threads and closure evidence)

## 10. Operational Concept

Software verification operates unit-to-system: plan threads early → develop cases, builds, and environments → execute through gated levels → record results → close in VCRM.
Cadence, build cadence alignment, and board provisions TBD.

## 11. Safety

Safety critical software threads are flagged in the VCRM with independence provisions TBD per VV Plan rules.
AI outputs are advisory only in early flight; any AI influenced thread identifies the deterministic bounded function actually verified with details TBD.

## 12. Performance

Software verification indicators TBD, with all thresholds TBD: coverage, criteria definition backlog, independence completeness, closure burn-down.
Measurement method and reporting cadence TBD.

## 13. Verification & Validation

This document is verified by Inspection against the VV Plan and SEMP checklist (header, 20 sections, IDs, parents, allowed methods only).
Validation of the software approach is programme authority approval at gated reviews; certification validation owned by Vol 25.

## 14. Risks

- Coverage gaps across units and interfaces; mitigation: coverage mapping per REQ-HFPX-VSW-002 (threshold TBD)
- Verifier dependence on development organisation; mitigation: independence provisions per REQ-HFPX-VSW-003 (degree TBD)
- Criteria left TBD blocking credit; mitigation: per-thread TBD tracking (assignments TBD)

## 15. Open Issues

Unit, integration, and system scope TBD with Vol 16.16. Coverage thresholds TBD. Independence degree TBD. Criteria TBD per thread. Environment fidelity TBD.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on VV Plan levels and gating, SEMP gates, SyRS §13, SAD allocation, Vol 16.16 assurance, Vol 22.3 VCRM, Vol 23 execution, Vol 13 safety inputs, Vol 25 credit rules.

## 18. Traceability

Parents: REQ-HFPX-VVP-002, REQ-HFPX-VVP-003, REQ-HFPX-VVP-005, REQ-HFPX-VVP-006. Children: software cases in Vol 16.16 and Vol 23 (IDs TBD; VCRM rows TBD).
RTM: REQ-HFPX-VSW-001..004 → CONCEPT. Coverage tracked in Vol 22.3 VCRM.

## 19. Configuration

BL-0.0. Tranche 8 draft, CONCEPT, not baselined. Future changes via change records; affected VCRM rows re-validated before gate claims.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 8 draft (Vol 22.10 direction; structure only) |
