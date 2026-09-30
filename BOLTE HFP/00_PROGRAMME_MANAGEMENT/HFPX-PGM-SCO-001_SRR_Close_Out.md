# SRR Close-Out Record (Methods, Parents, Missing Chapters)

**Document ID:** HFPX-PGM-SCO-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 8 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Record the SRR close-out executed against HFPX-PGM-SRR-001: the 20 missing chapter drafts, the verification-method repair, and the parentage repair — with the rules applied, so a reviewer can audit every changed cell.

## 2. Scope

Covers RTM + source-document cells only. Ownership assignment (ISS-011) and regulatory basis (ISS-001) are out of scope and remain OPEN.

## 3. Applicable Documents

- HFPX-PGM-SRR-001 (SRR-002/003/004 criteria closed here in structure)
- requirements_traceability_matrix.csv (2,177 rows after this tranche)
- issue_register.csv (ISS-009/010 closed here; ISS-011 open)

## 4. Definitions & Acronyms

- SRR-003 compliance: every requirement states a base method of Analysis, Inspection, Demonstration or Test (qualifiers such as "+ SIL/HIL" or "(details TBD)" permitted; bare TBD/Review/Audit not permitted)
- Root parent: top-of-chain requirements tracing to programme/stakeholder authority instead of another requirement

## 5. System Context

Close-out converts SRR entrance GAPS into evidence without changing technical content: no requirement text altered, no value invented, no issue closed by assertion.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-SCO-001 | The 20 missing chapters (01.5, 01.12–01.18, 22.2–22.13) shall each have a draft document with concrete A/I/D/T methods and non-empty parents. | REQ-HFPX-SRR-002 | Inspection |
| REQ-HFPX-SCO-002 | Every requirement shall state a base A/I/D/T method; bare TBD, Review and Audit methods are prohibited. | REQ-HFPX-SRR-003 | Inspection |
| REQ-HFPX-SCO-003 | Document-review activity shall be recorded as Inspection, never Review. | REQ-HFPX-SRR-003 | Inspection |
| REQ-HFPX-SCO-004 | Every major requirement shall carry a parent or an explicit ROOT declaration; blank parents are prohibited. | REQ-HFPX-SRR-004 | Inspection |
| REQ-HFPX-SCO-005 | RTM and source-document cells shall agree; the RTM is the curated truth after repair and documents are synced to it. | REQ-HFPX-PGM-002 | Inspection |

## 7. Architecture

Three repairs, one rulebook (§8), all script-executed and re-verified.

## 8. Detailed Design

Repair rules applied (auditable, re-runnable logic):
1. Extraction: 80 new rows from the 20 chapter docs (zero A-refs, zero TBD methods at source).
2. Depollution: cells that had swallowed extra table columns during earlier extraction split back out.
3. "TBD (intended X)" → X (author intent honoured).
4. Bare TBD → keyword rules on requirement text: flight/unmanned/fault-injection/calibration/accuracy/coverage/pass-fail → Test; demonstration/display/alert/annunciation/drill → Demonstration; analysis/assessment/model/simulation/trade/computation → Analysis; document-review activity → Inspection; fallback Inspection (all fallbacks safety-reviewed individually — 30 behavioural upgrades to Test/Analysis/Demonstration applied, listed in change record).
5. Bare Review/Audit → Inspection (in RTM and inside combo methods).
6. 30 weak parents → assigned parents or explicit ROOT declarations (programme authority / programme concept / stakeholder authority).
7. Full RTM↔document cell sync (RTM curated truth); agreement verified at 100%.

Results: methods stating a base A/I/D/T: 100% (was 86.8% + 151 Review/Audit rows). Parents present: 100% (was 98.6%). Chapters linked: 517/517 (was 497/517). Verification IDs: still 100% TBD (correct — no tests executed). Status: still 100% CONCEPT (correct — SRR has not convened).

## 9. Interfaces

- To SRR-001 assessment: criteria 2/3/4 now structurally satisfied; re-measurement recorded in HFPX-PGM-SRR-001 Rev B
- To V&V ownership: qualifier details ("(details TBD)", "+ SIL/HIL") remain for V&V review; this record does not approve them
- To change control: any method/parent change after this record follows 00.10

## 10. Operational Concept

Close-out is a gate-preparation activity, not a gate: SRR still requires owners (ISS-011), regulatory basis (ISS-001), critical-issue plans, and authority sign-off.

## 11. Safety

No safety claim follows from this record: methods assigned here define HOW each requirement will be checked, not THAT it passes. Unverified-model and no-waiver rules stand.

## 12. Performance

Close-out metrics: 20/20 chapters drafted; 2,177/2,177 methods stated; 2,177/2,177 parents present; doc/RTM agreement 100%; A-refs 0.

## 13. Verification & Validation

Verified by: re-extraction counts, residual scans (0 bare TBD/Review/Audit methods, 0 blank parents), doc/RTM agreement script, and `hfpx_scaffold.py check`. Validation: SRR authority acceptance.

## 14. Risks

- Method assignment mistaken for verification adequacy; mitigation: V&V ownership review action retained
- Keyword-rule misassignment; mitigation: 30-item behavioural review + full rulebook above for audit

## 15. Open Issues

ISS-009/010 CLOSED by this record. ISS-011 (ownership) open. Qualifier details open for V&V review.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on the 20 chapter docs, RTM discipline (00.9), change control (00.10), and pending V&V ownership review.

## 18. Traceability

Parents: SRR-002/003/004, PGM-002/011. Children: V&V ownership review, SRR convening decision. RTM: REQ-HFPX-SCO-001..005 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 8 draft, CONCEPT, not baselined.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | SRR close-out record (Tranche 8; methods, parents, missing chapters) |
