# Final Inspection

**Document ID:** HFPX-QA-FIN-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the structure-only final inspection approach for HFP-X: how completed articles are verified before acceptance, how completion of prior stages is confirmed, and how final records support acceptance. This document owns Chapter 28.5 and does not set technical values.

## 2. Scope

Covers verification of completed production articles, confirmation of configuration and record completeness, and routing to production acceptance (HFPX-QA-PAC-001) or to non-conformance management. Detailed methods, acceptance criteria values, and completion checklists remain TBD.

## 3. Applicable Documents

- HFPX-QA-QMS-001 Quality Management System
- HFPX-QA-INP-001 Inspection Plans
- HFPX-QA-PAC-001 Production Acceptance (TBD)
- HFPX-QA-NCM-001 Non-Conformance Management (TBD)
- HFPX-QA-TRC-001 Traceability (TBD)
- Vol 20 Manufacturing, Vol 25.8 quality liaison (details TBD)

## 4. Definitions & Acronyms

- Final inspection: verification performed on completed articles prior to acceptance
- Completion check: confirmation that required prior inspections, records, and configuration are present (content TBD)
- Acceptance: formal determination governed in HFPX-QA-PAC-001, not in this document
- TBD/TBC: unknown data markers

## 5. System Context

Final inspection closes the production verification chain:

```text
IN-PROCESS COMPLETE (28.4) → FINAL INSPECTION (28.5) → PRODUCTION ACCEPTANCE (28.12)
                                      ↓
                        NON-CONFORMANCE (28.6) / RECORDS + TRACEABILITY (28.11)
```

Final inspection verifies; acceptance decides. No article proceeds to acceptance with unresolved non-conformance except through defined disposition (process TBD).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-ZFI-001 | The programme shall define final inspection scope, responsibilities, and prerequisites, including confirmation of prior-stage completion. Details remain TBD. | Manufacturing quality classification / Vol 20 flow | Inspection |
| REQ-HFPX-ZFI-002 | Final inspection shall verify completed articles against defined design and inspection-plan content. Verification content and methods remain TBD. | HFPX-QA-INP-001 / Vol 20 design definition | Inspection |
| REQ-HFPX-ZFI-003 | Final inspection shall confirm configuration status and record completeness prior to presentation for acceptance. Confirmation content remains TBD. | Vol 28.9 Configuration Control / Vol 28.11 Traceability | Inspection |
| REQ-HFPX-ZFI-004 | Final inspection shall generate records supporting acceptance and retention, including handling of failures found at final stage. Record handling remains TBD. | Quality records classification / HFPX-QA-PAC-001 | Inspection |

## 7. Architecture

Final inspection structure (TBD): prerequisite check, verification steps, configuration and record completeness check, pass and fail routing, record package. Authority for final release to acceptance remains TBD.

## 8. Detailed Design

To be defined. Intended elements include: prerequisite criteria structure (TBD, without values), verification step structure (TBD), completeness check content (TBD), fail routing to non-conformance (TBD), record package structure (TBD). No thresholds, checklists values, or sampling provisions are set in this revision.

## 9. Interfaces

- Final ↔ HFPX-QA-INP-001: plan content for completed articles (TBD)
- Final ↔ HFPX-QA-CCB-001: as-inspected configuration status (TBD)
- Final ↔ HFPX-QA-TRC-001: serial, lot, and as-built linkage (TBD)
- Final ↔ HFPX-QA-NCM-001: failures and unresolved items (TBD)
- Final ↔ HFPX-QA-PAC-001: handover to acceptance (governed in 28.12, TBD)

## 10. Operational Concept

Completed articles undergo prerequisite confirmation, verification, and completeness checks; conforming packages are presented for acceptance while failures are routed to non-conformance management. Re-inspection after rectification follows defined routing (details TBD).

## 11. Safety

Final inspection supports safety by confirming that safety-relevant verification is complete before acceptance presentation. Safety-relevant final checks and independence provisions remain TBD in liaison with the safety programme. No safety values set in this document.

## 12. Performance

Measures of final inspection completeness and first-pass outcomes remain TBD in qualitative form, without targets or thresholds in this revision. No performance values baselined.

## 13. Verification & Validation

This document is verified by inspection against the template checklist. Final inspection implementation is verified by inspection and audit of packages and records (criteria TBD). Validation is programme authority approval (path TBD).

## 14. Risks

- Incomplete prerequisite check → acceptance of unverified work; mitigation: prerequisites per REQ-HFPX-ZFI-001 (TBD)
- Configuration or record gaps at handover → acceptance delays or escapes; mitigation: completeness confirmation per REQ-HFPX-ZFI-003 (TBD)
- Failures handled outside process → loss of control; mitigation: defined fail routing per REQ-HFPX-ZFI-004 (TBD)

## 15. Open Issues

- Scope, responsibilities, and prerequisites (TBD)
- Verification content and methods (TBD)
- Completeness check content (TBD)
- Record package and retention linkage (TBD)

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on HFPX-QA-INP-001, Vol 20 (completion state), HFPX-QA-CCB-001, HFPX-QA-TRC-001, and HFPX-QA-QMS-001. Supports HFPX-QA-PAC-001 and HFPX-QA-NCM-001.

## 18. Traceability

Parent: manufacturing and quality classification; Vol 20 Manufacturing, Vol 25.8 quality liaison. Children: handover to HFPX-QA-PAC-001; failures to HFPX-QA-NCM-001; records to HFPX-QA-TRC-001. RTM: REQ-HFPX-ZFI-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 28.5) |
