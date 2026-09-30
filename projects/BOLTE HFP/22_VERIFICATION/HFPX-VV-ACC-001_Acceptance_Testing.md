# Acceptance Testing

**Document ID:** HFPX-VV-ACC-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 8 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define acceptance testing for Volume 22.13, covering acceptance criteria, authority, configurations, and records for delivered articles.
Methodology only; detailed acceptance procedures remain with Vol 23 children.

## 2. Scope

Covers acceptance of hardware, software builds, and integrated systems prior to delivery or flight gating.
Development verification remains with Vol 22.5–22.12; range conduct and vehicle handling remain with Vol 23.

## 3. Applicable Documents

- HFPX-VV-PLN-001 VV Plan (REQ-HFPX-VVP-001..006 — acceptance criteria, gating, VCRM)
- HFPX-PGM-SEM-001 SEMP (gated reviews including FCA and PCA provisions TBD)
- HFPX-SYS-REQ-001 SyRS §13, HFPX-SYS-ARC-001 SAD (stub)
- Vol 22.3 (VCRM), Vol 23 (acceptance execution), Vol 25 (certification)

## 4. Definitions & Acronyms

- Acceptance: formal confirmation that a delivered article meets predefined criteria in a controlled configuration
- Acceptance authority: role empowered to grant acceptance; assignment TBD
- Representative article: build and configuration deemed valid for acceptance credit; criteria TBD
- FCA and PCA: functional and physical configuration audits; provisions TBD

## 5. System Context

Acceptance closes verification prior to delivery and gates flight progression:

```text
VERIFY (Vol 22.5–22.12) → ACCEPT (predefined cases) → DELIVER → GATE
        ↑________ VCRM TRACE (acceptance threads) ________↑
        ↑________ AUTHORITY DECISION (provisions TBD) ____↑
```

Acceptance cases are predefined, traced, configuration controlled, and executed on representative articles with independent witness where safety relevant (provisions TBD).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-VAC-001 | Each acceptance thread shall define acceptance criteria before execution, with criteria recorded as TBD per delivered item. | REQ-HFPX-VVP-005 | Demonstration |
| REQ-HFPX-VAC-002 | Acceptance shall be granted by a documented acceptance authority, with authority assignment and decision provisions defined as TBD. | REQ-HFPX-VVP-004 | Demonstration |
| REQ-HFPX-VAC-003 | Each acceptance shall produce retained records with article configuration, environment, and authority decision, with record provisions defined as TBD. | REQ-HFPX-VVP-005 | Demonstration |
| REQ-HFPX-VAC-004 | Each acceptance thread shall be traced in the VCRM to its parent requirement or requirements with representative configuration recorded as TBD per thread. | REQ-HFPX-VVP-002 | Demonstration |

## 7. Architecture

Acceptance organisation, authority, and witness provisions TBD under VV governance with SE coordination.
Thread structure: parent requirement → acceptance case → representative article and configuration → predefined criteria → authority decision → VCRM entry.
Safety relevant acceptance includes independent witness provisions TBD.

## 8. Detailed Design

Acceptance cases are predefined early and matured through CDR, TRR, FCA, and PCA stages; case and procedure IDs TBD in Vol 23 children.
Each acceptance case template shall contain objective, traced parents, method, article and configuration (TBD per case), environment TBD, criteria (TBD per case), and authority and witness claims.
Re-acceptance on article or requirement change follows change control with scope TBD.

## 9. Interfaces

- Acceptance ↔ Development verification (Vol 22.5–22.12 evidence roll-up)
- Acceptance ↔ Vol 23 (acceptance procedures, venues, articles)
- Acceptance ↔ VCRM (Vol 22.3 traceability and closure evidence)
- Acceptance ↔ Certification (Vol 25 defines certification credit; no credit claimed here)

## 10. Operational Concept

Acceptance operates define-to-decide: predefine cases and criteria → configure representative articles → execute → record outcomes → obtain authority decision → archive.
Cadence, venue, and board provisions TBD.

## 11. Safety

Safety relevant acceptance threads are flagged in the VCRM with independent witness provisions TBD.
Acceptance alone does not authorise human flight; human flight requires prior gate closure and FRR authorisation with criteria TBD.

## 12. Performance

Acceptance indicators TBD, with all thresholds TBD: acceptance coverage, criteria definition backlog, record completeness, acceptance closure burn-down.
Measurement method and reporting cadence TBD.

## 13. Verification & Validation

This document is verified by Inspection against the VV Plan and SEMP checklist (header, 20 sections, IDs, parents, allowed methods only).
Validation of the acceptance approach is programme authority approval at gated reviews; certification validation owned by Vol 25.

## 14. Risks

- Criteria left TBD blocking acceptance; mitigation: per-item TBD tracking (assignments TBD)
- Unrepresentative articles weakening acceptance; mitigation: representativeness criteria TBD per thread
- Authority ambiguity delaying decisions; mitigation: documented authority per REQ-HFPX-VAC-002 (assignment TBD)

## 15. Open Issues

Acceptance case IDs TBD. Criteria TBD per item. Authority assignments TBD. Representativeness criteria TBD. FCA and PCA provisions TBD.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on VV Plan acceptance and gating, SEMP gates, SyRS §13, SAD allocation, Vol 22.3 VCRM, Vol 22.5–22.12 evidence, Vol 23 acceptance execution, Safety Case and Vol 25 rules.

## 18. Traceability

Parents: REQ-HFPX-VVP-002, REQ-HFPX-VVP-004, REQ-HFPX-VVP-005. Children: acceptance cases and Vol 23 procedures (IDs TBD; VCRM rows TBD).
RTM: REQ-HFPX-VAC-001..004 → CONCEPT. Coverage tracked in Vol 22.3 VCRM.

## 19. Configuration

BL-0.0. Tranche 8 draft, CONCEPT, not baselined. Future changes via change records; affected VCRM rows re-validated before gate claims.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 8 draft (Vol 22.13 direction; structure only) |
