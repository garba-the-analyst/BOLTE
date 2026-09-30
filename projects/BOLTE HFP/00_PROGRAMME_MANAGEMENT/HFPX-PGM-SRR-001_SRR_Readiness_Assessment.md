# SRR Readiness Assessment (Pre-SRR)

**Document ID:** HFPX-PGM-SRR-001  
**Revision:** B (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 7 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Assess whether the HFP-X programme may convene the System Requirements Review (SRR), by mapping concrete SRR entrance evidence against the current baseline. This is a pre-SRR assessment, not the SRR itself, and it does not pass or baseline anything.

## 2. Scope

Covers SRR entrance readiness only: document coverage, requirements discipline, issue posture, ownership, and regulatory basis. PDR/CDR and later gates are out of scope. All values below are measured from the live tree on 2026-09-29.

## 3. Applicable Documents

- HFPX-PGM-REV-001 Design Reviews (gate framework; SRR criteria TBD there — this document proposes concrete SRR criteria for approval)
- HFPX-PGM-SEM-001 SEMP; HFPX-PGM-CHR-001 Charter
- HFPX-SYS-REQ-001 SyRS; HFPX-SYS-ARC-001 SAD; HFPX-VV-PLN-001; HFPX-SAFE-CAS-001
- HFPX-PGM-BSL-001 Master Technical Baseline (BL-0.0)
- Registers: RTM (2069 rows), issue register (8 OPEN), assumption register (empty by policy), decision log (DDR-001..003), hazard log, risk register (RSK-001..006)

## 4. Definitions & Acronyms

- SRR: System Requirements Review — confirms mission, stakeholder needs and system requirements are complete, consistent, traceable and verifiable before architecture freeze
- Pre-SRR: readiness check; SRR convenes only when entrance criteria are met
- Evidence statuses: SATISFIED (evidence exists and adequate), PARTIAL (exists but incomplete), GAP (missing)

## 5. System Context

SRR sits between requirements capture and architecture commitment:

```text
MISSION/CONOPS/STAKEHOLDER → SyRS → [SRR GATE] → SAD freeze → PDR
```

A premature SRR baselines requirements that cannot be verified and forces expensive rework. A delayed SRR stalls architecture. This assessment recommends timing, not content.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-SRR-001 | SRR shall convene only with mission, CONOPS, stakeholder, SyRS, SAD, V&V Plan and Safety Case drafts plus an opened hazard log and a maintained RTM. | REQ-HFPX-PGM-013 | Inspection |
| REQ-HFPX-SRR-002 | Every documentation chapter (517) shall have a draft document before SRR exit. | REQ-HFPX-PGM-002 | Inspection |
| REQ-HFPX-SRR-003 | Every requirement shall state its verification method (Analysis, Inspection, Demonstration, Test) before SRR exit. | REQ-HFPX-PGM-011 | Inspection |
| REQ-HFPX-SRR-004 | Every major requirement shall trace to a parent with no orphans before SRR exit. | REQ-HFPX-PGM-002 | Inspection |
| REQ-HFPX-SRR-005 | Document owners and approvers shall be assigned before SRR convenes. | REQ-HFPX-PGM-013 | Inspection |
| REQ-HFPX-SRR-006 | Each Critical open issue shall carry a burn-down plan with owner and due gate before SRR exit; SRR shall close as pass, pass-with-actions, or fail-repeat, never by waiver. | REQ-HFPX-PGM-003 | Inspection |

## 7. Architecture

Assessment structure: evidence inventory (§8) → criterion verdicts (§8) → gaps-to-actions (§14) → recommendation (§10). No architecture content.

## 8. Detailed Design

Measured evidence (tree state 2026-09-29):

| # | Entrance evidence (per SRR-001..006) | Status | Finding |
| --- | --- | --- | --- |
| 1 | Mission/CONOPS/stakeholder/SyRS/SAD/V&V/Safety Case drafts + hazard log + RTM | SATISFIED | All 7 backbone-family drafts exist; hazard log opened; RTM maintained (2069 rows) |
| 2 | All 517 chapters drafted (SRR-002) | SATISFIED (Rev B) | 517/517 linked. The 20 missing chapters were drafted in Tranche 8; ISS-009 CLOSED per HFPX-PGM-SCO-001 |
| 3 | Verification method on every requirement (SRR-003) | SATISFIED-structure (Rev B) | 100% state a base A/I/D/T method per the SCO-001 rulebook (bare TBD/Review/Audit eliminated; doc/RTM agreement 100%). Qualifier details remain for V&V ownership review; ISS-010 CLOSED for methods |
| 4 | No orphaned major requirements (SRR-004) | SATISFIED (Rev B) | 100% carry a parent or explicit ROOT declaration per SCO-001; ISS-010 CLOSED |
| 5 | Owners/approvers assigned (SRR-005) | GAP | All 498 documents carry Owner TBD / Approver TBD. Recorded as ISS-011 |
| 6 | Critical-issue burn-down plans (SRR-006) | PARTIAL (Rev B) | 9 issues OPEN (5 Critical: ISS-001, 002, 006, 007, 008; 4 High). Work products exist for ISS-001 (RES memo), 003/004 (conditional trades), 006 (6-DOF core + 5/5 PASS cases, UNVERIFIED), 007 (first-issue budgets), 008 (recovery parametrics). ISS-009/010 CLOSED. ISS-002/005/011 await owners; no issue has an owner or due gate |

Supporting posture: 498 HFPX documents, all Status CONCEPT; 0 requirements baselined; 0 verification IDs assigned (all TBD — correct pre-test); 6 registers valid (`hfpx_scaffold.py check` passes); 5/5 backbone documents drafted; 0 assumptions raised (policy); risk register seeded (RSK-001..006); DDR-001..003 adopted, no propulsion/airframe decision taken (correct — trades in progress).

## 9. Interfaces

- To 00.14 (REV-001): this document proposes the concrete SRR criteria that REV-001 leaves TBD; approval of the criteria is itself a pre-SRR action
- To 00.9/00.10: RTM gaps flow to requirements management and change control
- To 22.2–22.13 authors: 12 missing V&V chapters are the largest single gap
- To Vol 01 tier authors: 7 missing requirement tiers are the second gap

## 10. Operational Concept

Recommendation (Rev B): **STILL DO NOT CONVENE SRR — but the blockers are now ownership and authority, not documentation.** Structural close-out is done (criteria 1–4 satisfied). Remaining: assign owners/approvers (ISS-011), determine regulatory basis (ISS-001), put named owners and due gates on all Critical burn-downs, and hold V&V ownership review of method qualifiers. Then re-run this assessment and convene.

## 11. Safety

A premature SRR is a safety risk: baselining unverifiable requirements propagates into architecture, control laws and test conduct. The SRR-006 no-waiver rule and the 19.15 unregistered-model prohibition are the backstops. No safety claim is made here.

## 12. Performance

Readiness metrics (Rev B): chapters linked 517/517 (100%); methods stated 2,195/2,195 (100% base A/I/D/T); parents traced 2,195/2,195 (100% incl. ROOTs); verification IDs 100% TBD (correct — no tests executed); status 100% CONCEPT (correct — SRR not convened); issues 9 OPEN / 2 CLOSED; assumptions 0. SRR exit thresholds TBD (proposed: 100% / 100% / 100% / named owners + due gates for all Critical).

## 13. Verification & Validation

This assessment is verified by re-running the measurement script (counts reproducible from the tree) and inspection of the cited registers. Validation: programme-authority acceptance of the recommendation and of the proposed SRR criteria.

## 14. Risks

- SRR convened for schedule optics with gaps open → baselined gaps become architecture defects; mitigation: SRR-005/SRR-006 entrance enforcement
- Close-out treated as box-ticking (methods filled without thought) → V&V debt; mitigation: V&V Plan ownership review of the 273 TBD methods
- Ownership assigned nominally without authority → decisions stall post-SRR; mitigation: 00.3 role definitions with real delegation

## 15. Open Issues

ISS-009 (20 chapters without docs — CLOSED Rev B), ISS-010 (273 TBD methods + 30 weak parents — CLOSED Rev B), ISS-011 (owners/approvers TBD — OPEN, now the critical path). ISS-001/002/005/008 remain OPEN with partial plans and no owners.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on Vol 01 tier drafts (01.5, 01.12–01.18), Vol 22 drafts (22.2–22.13), V&V ownership review, BOLTE authority assignment, Tranche-7 trade/model/budget outputs, and Vol 25 regulatory research.

## 18. Traceability

Parents: REQ-HFPX-PGM-002/003/011/013. Children: the 20 missing chapter drafts, 273 method assignments, 30 parentage fixes, ownership assignments, issue burn-down plans. RTM: REQ-HFPX-SRR-001..006 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 7 draft, CONCEPT, not baselined. Re-assessment required after close-out actions before SRR convenes.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial pre-SRR readiness assessment (Tranche 7) |
| B | 2026-09-29 | Re-measurement after Tranche-8 close-out (criteria 2/3/4 satisfied; ISS-009/010 closed; HOLD maintained on ownership/authority) |
