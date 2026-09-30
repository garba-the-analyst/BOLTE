# Safety Verification

**Document ID:** HFPX-VV-SFV-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 8 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define safety verification for Volume 22.12, covering independent verification of safety requirements, fault injection provisions, hazard closure evidence, and records.
Methodology only; hazard ownership remains with Vol 13 and the Safety Case.

## 2. Scope

Covers safety requirements derived from the hazard log and safety analyses across hardware, software, and system levels.
Detailed hazard analyses remain with Vol 13; test execution detail with Vol 23; certification credit with Vol 25.

## 3. Applicable Documents

- HFPX-VV-PLN-001 VV Plan (REQ-HFPX-VVP-001..006, notably independence rule)
- HFPX-SAFE-CAS-001 Safety Case, Vol 13 (hazards and safety requirements; closure provisions TBD)
- HFPX-PGM-SEM-001 SEMP (gated reviews)
- HFPX-SYS-REQ-001 SyRS §13, Vol 22.3 (VCRM), Vol 23 (execution)

## 4. Definitions & Acronyms

- Safety verification: verification of safety requirements and hazard controls with independence provisions TBD
- Fault injection: deliberate introduction of faults to observe safety behaviour; scope TBD
- Hazard closure: evidence based claim that a hazard control is implemented and effective; criterion TBD
- Independence: separation of safety verifier from design organisation; degree TBD

## 5. System Context

Safety verification forms the independent path alongside design verification:

```text
HAZARDS (Vol 13) → SAFETY REQUIREMENTS → INDEPENDENT VERIFICATION → CLOSURE
        ↑________ VCRM TRACE (safety flagged threads) ________↑
        ↑________ INDEPENDENT VERIFIER (reporting TBD) ______↑
```

Safety threads are flagged in the VCRM with method, level, independence claim, and closure status.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-VFV-001 | Safety verification shall be independent of the design organisation to a degree defined as TBD, with independent verification or test of safety requirements and safety critical cases. | REQ-HFPX-VVP-006 | Test |
| REQ-HFPX-VFV-002 | Safety verification shall include fault injection threads where allocated, with fault scope and environments recorded as TBD per safety thread. | REQ-HFPX-VVP-006 | Test |
| REQ-HFPX-VFV-003 | Each hazard control shall be closed by traced verification evidence interfacing with Vol 13, with closure criteria recorded as TBD per hazard. | REQ-HFPX-VVP-006 | Test |
| REQ-HFPX-VFV-004 | Each safety verification thread shall produce retained records with configuration, environment, and independence claim, with record provisions defined as TBD. | REQ-HFPX-VVP-002 | Test |

## 7. Architecture

Independent safety verifier organisation and reporting path TBD via Safety Review Board provisions TBD.
Thread structure: hazard → safety requirement → independent verification thread (test or analysis TBD per allocation) → fault injection where allocated → closure record → VCRM entry.
Catastrophic hazard threads receive priority handling with criteria TBD.

## 8. Detailed Design

Safety cases are planned early from hazard inputs with procedures matured through CDR, TRR, and pre-flight gates; case and procedure IDs TBD.
Each safety case template shall contain objective, traced hazard and safety requirement parents, method, level, environment and configuration (TBD per case), fault scope TBD, pass and fail criteria (TBD per case), and independence claim.
Regression on hazard or design change re-opens affected rows until re-verified; scope per change record TBD.

## 9. Interfaces

- Safety verification ↔ Vol 13 and Safety Case (hazard inputs; closure evidence back)
- Safety verification ↔ VCRM (Vol 22.3 flagged traceability)
- Safety verification ↔ Vol 23 (fault injection venues and procedures)
- Safety verification ↔ Certification (Vol 25 credit mapping; no credit claimed here)

## 10. Operational Concept

Safety verification operates hazard-to-closure: derive safety threads from hazards → assign independence → execute analysis and test threads → inject faults where allocated → record closure → gate.
Cadence, board membership, and venue provisions TBD.

## 11. Safety

Independence is the governing safety provision of this document per REQ-HFPX-VFV-001 with degree TBD.
Catastrophic hazard closure evidence is independently verified before any human flight gate is considered (criterion TBD, owned by Safety Case).

## 12. Performance

Safety verification indicators TBD, with all thresholds TBD: safety thread coverage, independence completeness, fault injection backlog, hazard closure burn-down.
Measurement method and reporting cadence TBD.

## 13. Verification & Validation

This document is verified by Inspection against the VV Plan and SEMP checklist (header, 20 sections, IDs, parents, allowed methods only).
Validation of the safety approach is programme authority approval at gated reviews with Safety Case concurrence TBD; certification validation owned by Vol 25.

## 14. Risks

- Independence shortfalls weakening safety claims; mitigation: independence rule with degree TBD and board oversight TBD
- Fault coverage gaps for critical behaviours; mitigation: fault scope planning per REQ-HFPX-VFV-002 (scope TBD)
- Hazard closure evidence left TBD blocking gates; mitigation: per-hazard TBD tracking (assignments TBD)

## 15. Open Issues

Independence degree TBD. Fault injection scope TBD. Hazard closure criteria TBD per hazard with Vol 13. Witness rules TBD. Records tooling TBD.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on VV Plan independence and gating, Safety Case and Vol 13 hazards, SEMP gates, SyRS §13, Vol 22.3 VCRM, Vol 19 analysis, Vol 23 execution, Vol 25 credit rules.

## 18. Traceability

Parents: REQ-HFPX-VVP-002, REQ-HFPX-VVP-006. Children: safety verification cases and Vol 23 procedures (IDs TBD; VCRM rows TBD).
RTM: REQ-HFPX-VFV-001..004 → CONCEPT. Coverage tracked in Vol 22.3 VCRM.

## 19. Configuration

BL-0.0. Tranche 8 draft, CONCEPT, not baselined. Future changes via change records; affected VCRM rows re-validated before gate claims.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 8 draft (Vol 22.12 direction; structure only) |
