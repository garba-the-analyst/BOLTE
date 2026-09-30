# Ownership & Critical-Issue Burn-Down Plan (Pre-SRR)

**Document ID:** HFPX-PGM-SRR-002  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 9 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-30

---

## 1. Purpose

Close ISS-011 in structure and give each Critical OPEN issue (ISS-001, 002, 006, 007, 008) a role owner and due gate per REQ-HFPX-SRR-005 and REQ-HFPX-SRR-006, so SRR can be re-assessed. This plan assigns ROLES only — no named individuals — and baselines nothing.

## 2. Scope

Covers role→issue assignment, RACI, and burn-down steps for the 5 Critical issues plus ISS-011. Technical content, budgets, model registration, and regulatory determinations are out of scope (owned by their volumes). No gate is convened by this document.

## 3. Applicable Documents

- HFPX-PGM-SRR-001 Rev B (SRR-005 GAP, SRR-006 PARTIAL finding this plan answers)
- HFPX-PGM-ORG-001 (00.3 — roles TBD, no appointments at this revision)
- HFPX-PGM-REV-001 (00.14 — no-waiver rule REQ-HFPX-GRV-005)
- HFPX-PGM-SCO-001 (methods/parents rulebook)
- HFPX-CERT-RES-001, HFPX-PROP-TRD-001, HFPX-STR-TRD-001, HFPX-AERO-BDG-001, HFPX-SIM-SIX-002, HFPX-SIM-VCS-001, HFPX-SAFE-FSB-001
- Registers: `issue_register.csv`, `change_register.csv` (CHG-001), `decision_log.csv` (DDR-001..003)

## 4. Definitions & Acronyms

- CHENG: Chief Engineer (technical authority, holder TBD)
- CERT: Certification/Regulatory Lead, Vol 25 (holder TBD)
- SYS: Systems Engineering Lead, Vol 01/02 (holder TBD)
- FCS-SIM: Flight Control + Simulation Leads, Vol 07/06/19 (holders TBD)
- PROP-AERO: Propulsion + Aero Leads, Vol 04/06 (holders TBD)
- SAFE: Independent Safety Lead, Vol 13 (holder TBD, independent of delivery)
- VV: V&V Lead, Vol 22 (holder TBD)
- pre-SRR: before SRR convenes; SRR-exit: before SRR can pass; PDR/TRR: later gates for full closure
- TBD: to be determined; TBC: to be confirmed

## 5. System Context

```text
BOLTE AUTHORITY → ROLE HOLDERS (TBD) → BURN-DOWN STEPS (this doc)
  → EVIDENCE IN VOLUMES → SRR-001 RE-MEASUREMENT → SRR CONVENE DECISION
```

Ownership does not create evidence. It creates accountability for evidence.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-SRR-007 | Each Critical OPEN issue (ISS-001, 002, 006, 007, 008) shall have a role owner and due gate recorded in the issue register. | REQ-HFPX-SRR-006 | Inspection |
| REQ-HFPX-SRR-008 | Document owners/approvers shall be assigned as roles at this revision and as named individuals by BOLTE authority before SRR convenes. | REQ-HFPX-SRR-005 | Inspection |
| REQ-HFPX-SRR-009 | Safety concurrence shall be required for burn-down closure of ISS-001, 006, 007 and 008. | REQ-HFPX-SRR-006 | Inspection |
| REQ-HFPX-SRR-010 | No SRR exit, baseline change, or model registration shall be claimed by this plan. | REQ-HFPX-SRR-006 | Inspection |

## 7. Architecture

One plan, two parts: (a) RACI assignment (§8), (b) per-issue burn-down with steps, evidence, and due gate (§8). Register patch + change record carry the assignment; volumes carry the work.

## 8. Detailed Design

### 8.1 RACI (roles only; names TBD by BOLTE)

| Issue | Responsible (does work) | Accountable (owns gate) | Consulted | Informed | Concurrence |
| --- | --- | --- | --- | --- | --- |
| ISS-001 Regulatory basis | CERT | CHENG | SYS, VV | Programme | SAFE |
| ISS-002 Mission vacuum | SYS | CHENG | CERT, VV | Programme | — |
| ISS-006 Control authority | FCS-SIM | CHENG | PROP-AERO, VV | Programme | SAFE |
| ISS-007 Budgets | PROP-AERO | CHENG | FCS-SIM, VV | Programme | SAFE |
| ISS-008 Recovery | SAFE (+ RST team TBD) | CHENG | PROP-AERO, FCS-SIM | Programme | SAFE (self = independent review TBD) |
| ISS-011 Ownership | CHENG | BOLTE authority | All leads | Programme | SAFE |

### 8.2 Burn-down steps (exit = evidence in owning volume, not this doc)

**ISS-001 — Owner: CERT [NAME TBD] — Due: plan pre-SRR, full basis SRR-exit**

1. Obtain Nig.CARs airworthiness part text from authoritative source; file in 25.2.
2. Submit NCAA classification query; record 25.11 engagement plan (owner TBD, date TBD).
3. Revise HFPX-CERT-RES-001 with confirmed-vs-TBD separation; SAFE review for foreign-framework fencing.

**ISS-002 — Owners: CHENG / SYS [NAMES TBD] — Due: pre-SRR**

1. Draft 01.1 Mission, 01.3 CONOPS, 01.4 Stakeholder.
2. Derive SyRS top-level from above; RTM parent links updated.

**ISS-006 — Owner: FCS-SIM [NAMES TBD], Concurrence: SAFE — Due: plan SRR-exit, closure PDR**

1. Define 19.3 input-data families (mass/aero/propulsion TBD list).
2. VV approval of VCS tolerances (1e-4 m, 1e-6 m, 1e-12 quat, 1e-6 energy, 0.5 m cross-check — all TBC).
3. Authority-data comparison + 19.15 register entry. Until then: UNVERIFIED, barred from gates.

**ISS-007 — Owner: PROP-AERO [NAMES TBD], Concurrence: SAFE — Due: SRR-exit**

1. Replace or retain TBD mass lines only via `06_AERODYNAMICS/hfpx_budgets.py` rerun (hand edits prohibited).
2. Installed-SFC measurement plan (Vol 04.17) + margin policy (07.17). Cruise stays TBD until drag exists.

**ISS-008 — Owner: SAFE [NAME TBD] — Due: plan SRR-exit, closure TRR/FRR staged**

1. Canopy aero + timeline allocations + human tolerance criteria TBD list (FSB-001 data needs).
2. RST component → system → unmanned demonstration with data capture. Hover case carried by stabilisation/impact/escape (effectiveness TBD).

**ISS-011 — Owner: CHENG [BOLTE authority to name] — Due: pre-SRR**

1. BOLTE names CHENG, SAFE, CERT, VV (minimum 4 signatures).
2. Remaining Vol owners named per 00.3; approvers independent of authors for safety/V&V threads.

## 9. Interfaces

- To `issue_register.csv`: Owners/Due Dates patched by this tranche (see CHG-001); issue text unchanged.
- To `change_register.csv`: CHG-001 records this plan + register patch; New Baseline BL-0.0 (unchanged).
- To Vol 25/01/19/06/04/13/22: work proceeds there; this doc tracks accountability only.
- To SRR-001: re-measurement input for criteria 5/6; does not convene SRR.

## 10. Operational Concept

BOLTE names 4 leads → leads execute volume work → VV/SAFE review qualifiers and tolerances → CHENG re-runs SRR-001 measurement → convene decision. No step skipped, no waiver per REQ-HFPX-GRV-005.

## 11. Safety

No safety claim follows from assignment. Hazard log remains open (0 hazards logged — population is SAFE work, not done here). UNVERIFIED-model ban (19.15) and no-waiver rule stand. Safety independence (ORG-001 §11) preserved: SAFE concurs but does not deliver ISS-006/007 propulsion work.

## 12. Performance

Plan performance: 5/5 Critical issues with role + due gate (was 0/5 with owner); 1/1 ownership issue with assignment path (was GAP). Verification IDs still 100% TBD (correct). Status still 100% CONCEPT (correct).

## 13. Verification & Validation

Verified by inspection: issue_register Owners/Due Dates non-TBD for ISS-001/002/006/007/008/011; CHG-001 present; `hfpx_scaffold.py check` still passes (ID patterns preserved). Validation: BOLTE authority approval of roles + CHENG acceptance.

## 14. Risks

- Names assigned nominally without authority → decisions stall; mitigation: 00.3 delegation + RACI enforcement.
- Assignment mistaken for evidence → premature SRR; mitigation: SRR-010 + SRR-001 re-measurement required.
- SAFE overloaded (owns ISS-008 + concurs on 3 others); mitigation: independent review support TBD, staffing in 00.3.

## 15. Open Issues

ISS-001/002/005/006/007/008/011 remain OPEN (owners now assigned as roles, names TBD). ISS-003/004 remain OPEN (High, selection DDRs deferred — not in SRR-002 scope). ISS-009/010 stay CLOSED. Qualifier details + tolerance approval remain for VV review.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on BOLTE authority assignment, Vol 25 engagement, Vol 01 drafts, Vol 19.15 methodology, Vol 04/06/07 measurement plans, and Vol 13 RST thread.

## 18. Traceability

Parents: REQ-HFPX-SRR-005/006, REQ-HFPX-PGM-001/003/013. Children: volume evidence, VV qualifier review, tolerance approval, SRR-001 re-measurement. RTM: REQ-HFPX-SRR-007..010 → CONCEPT (to be added to RTM at next RTM curation; RTM structure untouched by this tranche pending 00.9 review).

## 19. Configuration

BL-0.0 (structure only). Tranche 9 draft, CONCEPT, not baselined. No technical requirement, value, or gate status changed. Future changes via 00.10 change control. Proposed DDR-004 (ownership mapping) deferred to BOLTE approval — no DDR recorded by this revision.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-30 | Initial ownership + Critical burn-down plan (Tranche 9; roles + due gates; CHG-001) |
