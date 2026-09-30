# Production Acceptance

**Document ID:** HFPX-QA-PAC-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the structure-only production acceptance approach for HFP-X: how completed articles are accepted against defined criteria using inspection evidence, configuration status, and traceability. This document owns Chapter 28.12 and does not set technical values.

## 2. Scope

Covers acceptance criteria framework per item (criteria TBD), acceptance authority and records, and hooks to Vol 20.14 production acceptance interfaces within manufacturing. Includes coordination with final inspection, configuration control, serialisation, and traceability. Detailed criteria, tests, and acceptance provisions remain TBD.

## 3. Applicable Documents

- HFPX-QA-QMS-001 Quality Management System
- HFPX-QA-FIN-001 Final Inspection
- HFPX-QA-CCB-001 Configuration Control; HFPX-QA-SER-001 Serialisation; HFPX-QA-TRC-001 Traceability (all TBD)
- Vol 20.14 Production acceptance interfaces within manufacturing (details TBD)
- Vol 25.8 Certification and quality liaison (TBD)

## 4. Definitions & Acronyms

- Production acceptance: formal determination that an article is acceptable per defined criteria (criteria TBD)
- Acceptance criteria: defined conditions for acceptance per item (content TBD)
- Acceptance record: evidence of acceptance decision and its basis (content TBD)
- TBD/TBC: unknown data markers

## 5. System Context

Production acceptance is the terminal production quality gate:

```text
FINAL INSPECTION (28.5) + CONFIG STATUS (28.9) + IDENTITY (28.10) + TRACE (28.11) → PRODUCTION ACCEPTANCE (28.12) → DELIVERY / NEXT PHASE (TBD)
                                    ↓
                         Vol 20.14 MANUFACTURING ACCEPTANCE HOOKS (TBD)
```

Inspection verifies; acceptance decides and records the decision.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-ZPA-001 | The programme shall define acceptance criteria per item, referencing design definition, inspection evidence, and configuration status. Criteria remain TBD per item. | Vol 20.14 manufacturing acceptance / design definition | Inspection |
| REQ-HFPX-ZPA-002 | Production acceptance shall maintain hooks to Vol 20.14 so that quality acceptance and manufacturing acceptance provisions remain aligned. Hook details remain TBD. | Vol 20.14 | Inspection |
| REQ-HFPX-ZPA-003 | Production acceptance shall confirm completeness of inspection, configuration, traceability, and non-conformance resolution prior to acceptance. Confirmation content remains TBD. | HFPX-QA-FIN-001 / HFPX-QA-CCB-001 / HFPX-QA-TRC-001 / HFPX-QA-NCM-001 | Inspection |
| REQ-HFPX-ZPA-004 | Production acceptance shall generate and retain acceptance records supporting delivery and audit. Record content and retention linkage remain TBD. | Quality records classification | Inspection |

## 7. Architecture

Acceptance structure (TBD): criteria reference per item, prerequisite completeness check, acceptance authority, decision recording, rejection and re-presentation loop. Acceptance authority independence where required remains TBD.

## 8. Detailed Design

To be defined. Intended elements include: criteria framework structure without values (TBD), per-item criteria sheets (content TBD), completeness check content (TBD), authority matrix (TBD), acceptance record package structure (TBD), re-presentation provisions after rectification (TBD). No acceptance values, thresholds, or test provisions are set in this revision.

## 9. Interfaces

- Acceptance ↔ HFPX-QA-FIN-001: verified packages presented for acceptance (TBD)
- Acceptance ↔ Vol 20.14: manufacturing acceptance alignment (TBD)
- Acceptance ↔ HFPX-QA-CCB-001 / SER-001 / TRC-001: configuration, identity, and trace basis (TBD)
- Acceptance ↔ HFPX-QA-NCM-001: unresolved-item handling (TBD)
- Acceptance ↔ Vol 25.8: certification liaison where acceptance evidence supports compliance (TBD)

## 10. Operational Concept

Completed packages are presented with evidence and status, completeness is confirmed, the acceptance decision is made under defined authority and recorded, and accepted articles proceed per delivery provisions while rejected articles return through defined routing. Conditional acceptance, if any, remains TBD and is not assumed.

## 11. Safety

Production acceptance protects safety by ensuring safety-relevant verification and resolution are confirmed before acceptance. Safety-relevant acceptance provisions and any independent acceptance requirements remain TBD in liaison with the safety programme. No safety values set in this document.

## 12. Performance

Measures of acceptance completeness and record integrity remain TBD in qualitative form, without targets or thresholds in this revision. No performance values baselined.

## 13. Verification & Validation

This document is verified by inspection against the template checklist. Production acceptance implementation is verified by inspection and audit of criteria linkage, completeness checks, and acceptance records (criteria TBD). Validation is programme authority approval (path TBD).

## 14. Risks

- Undefined per-item criteria → inconsistent acceptance; mitigation: criteria framework per REQ-HFPX-ZPA-001 (TBD)
- Manufacturing-quality misalignment → disputed acceptance; mitigation: hooks per REQ-HFPX-ZPA-002 (TBD)
- Incomplete prerequisites → acceptance of unresolved work; mitigation: completeness confirmation per REQ-HFPX-ZPA-003 (TBD)
- Missing records → unverifiable decisions; mitigation: records per REQ-HFPX-ZPA-004 (TBD)

## 15. Open Issues

- Acceptance criteria per item (TBD)
- Hook details to Vol 20.14 (TBD)
- Completeness confirmation content (TBD)
- Acceptance records and retention linkage (TBD)

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on HFPX-QA-FIN-001, HFPX-QA-CCB-001, HFPX-QA-SER-001, HFPX-QA-TRC-001, HFPX-QA-NCM-001, Vol 20.14, and HFPX-QA-QMS-001. Supports delivery and Vol 25.8 compliance linkage.

## 18. Traceability

Parent: manufacturing and quality classification; Vol 20 / Vol 20.14 Manufacturing, Vol 25.8 quality liaison. Children: acceptance records as terminal production quality evidence; handover to delivery or next phase (TBD). RTM: REQ-HFPX-ZPA-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 28.12) |
