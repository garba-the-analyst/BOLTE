# Configuration Control

**Document ID:** HFPX-QA-CCB-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the structure-only production configuration control approach for HFP-X: how production configuration is identified, changed under authority, and reflected in build status and records. This document owns Chapter 28.9 and does not set technical values.

## 2. Scope

Covers production-config control linkage between engineering definition and manufacturing execution, including change authority, status accounting, and alignment with inspection, serialisation, traceability, and acceptance. Programme-level configuration management in Vol 00.7 and lifecycle configuration in Vol 32.2 are interfaced, not duplicated. Detailed boards, workflows, and status methods remain TBD.

## 3. Applicable Documents

- HFPX-QA-QMS-001 Quality Management System
- Vol 00.7 Configuration management interfaces (details TBD)
- Vol 32.2 Lifecycle configuration interfaces (details TBD)
- HFPX-QA-SER-001 Serialisation; HFPX-QA-TRC-001 Traceability; HFPX-QA-PAC-001 Production Acceptance (all TBD)
- Vol 20 Manufacturing (execution baseline, TBD)

## 4. Definitions & Acronyms

- Production configuration: defined configuration applicable to manufacture and verification of an article (content TBD)
- Change control: authorised review and approval of changes to production configuration (process TBD)
- Status accounting: recording of applicable configuration and change incorporation for an article or batch (method TBD)
- CCB: Configuration Control Board or equivalent authority (charter TBD)
- TBD/TBC: unknown data markers

## 5. System Context

Production configuration control binds definition to build:

```text
ENGINEERING DEFINITION + Vol 00.7 / 32.2 → PRODUCTION CONFIG CONTROL (28.9) → BUILD + INSPECT + ACCEPT (Vol 20 / 28.2–28.12)
                                                              ↓
                                              STATUS + RECORDS (28.10 / 28.11 / 28.12)
```

No production change is made without authority; no article is presented for acceptance with unresolved configuration mismatch except through defined disposition (process TBD).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-ZCC-001 | The programme shall define production configuration identification, linking articles and batches to applicable definition and changes. Identification details remain TBD. | Vol 00.7 configuration interfaces / manufacturing classification | Inspection |
| REQ-HFPX-ZCC-002 | Production configuration changes shall be controlled through defined authority, with review of impact on manufacture, inspection, and acceptance. Authority and workflow remain TBD. | Vol 00.7 / Vol 32.2 configuration control | Inspection |
| REQ-HFPX-ZCC-003 | The programme shall maintain hooks between production configuration control and Vol 00.7 and Vol 32.2 so that programme and lifecycle configuration remain aligned. Hook details remain TBD. | Vol 00.7 / Vol 32.2 | Inspection |
| REQ-HFPX-ZCC-004 | Production configuration control shall maintain status accounting supporting inspection, traceability, and acceptance. Status content and records linkage remain TBD. | Quality records classification / Vol 28.11 Traceability | Inspection |

## 7. Architecture

Configuration control structure (TBD): configuration identification scheme, change review authority, impact assessment linkage, implementation instruction, status record. Board membership and approval thresholds, if any quantitative form is later proposed, remain TBD with no values baselined in this revision.

## 8. Detailed Design

To be defined. Intended elements include: identification structure (TBD), change request and approval structure (TBD), impact categories covering manufacture, inspection, supplier, and acceptance (TBD), implementation and embodiment records (TBD), status accounting format (TBD). No configuration values or change categories are baselined.

## 9. Interfaces

- Production config ↔ Vol 00.7: programme configuration authority and baselines (TBD)
- Production config ↔ Vol 32.2: lifecycle configuration alignment (TBD)
- Production config ↔ Vol 20: embodiment in manufacture and work instructions (TBD)
- Production config ↔ HFPX-QA-INP-001 / FIN-001: inspection alignment to applicable revision (TBD)
- Production config ↔ HFPX-QA-SER-001 / TRC-001 / PAC-001: status reflected in identity, trace, and acceptance (TBD)

## 10. Operational Concept

Applicable configuration is identified for each build, changes are proposed with impact review, authorised changes are embodied through controlled instructions, and status is recorded so that inspection and acceptance reference the correct configuration. Emergency or urgent change handling, if any, remains TBD and is not assumed.

## 11. Safety

Configuration control protects safety by ensuring safety-relevant changes receive appropriate review and that build status reflects approved definition. Safety review interfaces for production changes remain TBD. No safety values set in this document.

## 12. Performance

Measures of change control health and status accuracy remain TBD in qualitative form, without targets or thresholds in this revision. No performance values baselined.

## 13. Verification & Validation

This document is verified by inspection against the template checklist. Production configuration control is verified by inspection and audit of change records and status accounting (criteria TBD). Validation is programme authority approval (path TBD).

## 14. Risks

- Unidentified configuration → build to wrong definition; mitigation: identification per REQ-HFPX-ZCC-001 (TBD)
- Unauthorised change → uncontrolled production; mitigation: authority per REQ-HFPX-ZCC-002 (TBD)
- Programme-lifecycle divergence → inconsistent baselines; mitigation: hooks per REQ-HFPX-ZCC-003 (TBD)
- Status gaps → unverifiable acceptance; mitigation: status accounting per REQ-HFPX-ZCC-004 (TBD)

## 15. Open Issues

- Identification scheme and applicability rules (TBD)
- Change authority, workflow, and impact scope (TBD)
- Hook details to Vol 00.7 and Vol 32.2 (TBD)
- Status accounting content and records linkage (TBD)

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on Vol 00.7, Vol 32.2, Vol 20, and HFPX-QA-QMS-001. Supports inspection stages, HFPX-QA-SER-001, HFPX-QA-TRC-001, and HFPX-QA-PAC-001.

## 18. Traceability

Parent: manufacturing and quality classification; Vol 00.7, Vol 32.2, Vol 20 Manufacturing, Vol 25.8 quality liaison. Children: aligned execution in Vol 20 and Vol 28 stages; status to HFPX-QA-TRC-001 and HFPX-QA-PAC-001. RTM: REQ-HFPX-ZCC-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 28.9) |
