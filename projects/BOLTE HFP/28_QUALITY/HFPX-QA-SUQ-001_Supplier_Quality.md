# Supplier Quality

**Document ID:** HFPX-QA-SUQ-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the structure-only supplier quality approach for HFP-X: how supplier quality expectations are flowed down, monitored, and linked to incoming verification and corrective action. This document owns Chapter 28.8 and does not set technical values.

## 2. Scope

Covers supplier quality provisions applicable to production articles, including evaluation and monitoring intent, flow-down of requirements, coordination with procurement interfaces in Vol 00.13 and Vol 20.11, and linkage to incoming inspection and corrective actions. Detailed evaluation criteria, surveillance methods, and contractual provisions remain TBD.

## 3. Applicable Documents

- HFPX-QA-QMS-001 Quality Management System
- HFPX-QA-INC-001 Incoming Inspection
- HFPX-QA-NCM-001 Non-Conformance Management; HFPX-QA-CRA-001 Corrective Actions (TBD)
- Vol 00.13 Supplier-related interfaces (details TBD)
- Vol 20.11 Supplier and procurement interfaces within manufacturing (details TBD)
- Vol 25.8 Certification and quality liaison (TBD)

## 4. Definitions & Acronyms

- Supplier: external provider of articles or processes used in HFP-X production (scope TBD)
- Flow-down: communication of applicable requirements to suppliers (mechanism TBD)
- Supplier monitoring: oversight of supplier quality performance and issues (method TBD)
- TBD/TBC: unknown data markers

## 5. System Context

Supplier quality connects procurement to production control:

```text
REQUIREMENTS + PROCUREMENT (Vol 00.13 / 20.11) → SUPPLIER QUALITY (28.8) → INCOMING INSPECTION (28.3)
                                                              ↓
                                              NON-CONFORMANCE (28.6) + CORRECTIVE ACTION (28.7)
```

Supplier control and receipt verification are complementary; neither is assumed to replace the other.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-ZSQ-001 | The programme shall define supplier quality expectations and their flow-down to suppliers, including linkage to purchase definition. Flow-down content and mechanism remain TBD. | Vol 00.13 supplier interfaces / Vol 20.11 procurement | Inspection |
| REQ-HFPX-ZSQ-002 | The programme shall define supplier evaluation and monitoring provisions supporting selection and continued oversight. Criteria and methods remain TBD. | Procurement quality classification | Inspection |
| REQ-HFPX-ZSQ-003 | Supplier quality provisions shall coordinate with incoming inspection so that supplier evidence and receipt verification are aligned. Coordination details remain TBD. | HFPX-QA-INC-001 / Vol 20.11 | Inspection |
| REQ-HFPX-ZSQ-004 | Supplier-related non-conformances and issues shall route to non-conformance management and, where systemic, to corrective action. Routing criteria remain TBD. | HFPX-QA-NCM-001 / HFPX-QA-CRA-001 | Inspection |

## 7. Architecture

Supplier quality structure (TBD): expectation set, evaluation file, monitoring record, evidence coordination with incoming inspection, issue escalation path. Responsibilities across procurement, quality, and manufacturing remain TBD.

## 8. Detailed Design

To be defined. Intended elements include: flow-down statement structure (TBD), evaluation provision structure without prescribing criteria (TBD), monitoring approach without prescribing frequency or metrics (TBD), evidence types coordinated at receipt (scope TBD), escalation to NCM and corrective action (TBD). No ratings, thresholds, or surveillance values are set in this revision.

## 9. Interfaces

- Supplier quality ↔ Vol 00.13 / Vol 20.11: procurement definition and contractual channels (TBD)
- Supplier quality ↔ HFPX-QA-INC-001: evidence-to-verification coordination (TBD)
- Supplier quality ↔ HFPX-QA-NCM-001 / CRA-001: issue and action routing (TBD)
- Supplier quality ↔ HFPX-QA-TRC-001: supplier lot and provenance linkage (TBD)
- Supplier quality ↔ Vol 25.8: regulatory expectations affecting suppliers (TBD)

## 10. Operational Concept

Expectations are flowed down through procurement channels, supplier standing is evaluated and monitored as defined, receipt evidence is coordinated with incoming inspection, and supplier issues are contained and acted upon through NCM and corrective action paths. Delegated verification or source inspection, if any, remains TBD and is not assumed.

## 11. Safety

Supplier quality supports safety by controlling quality of supplied articles, including safety-relevant items identified in liaison with the safety programme. Additional controls for safety-critical suppliers or articles remain TBD. No safety values set in this document.

## 12. Performance

Measures of supplier quality oversight remain TBD in qualitative form, without targets, ratings, or thresholds in this revision. No performance values baselined.

## 13. Verification & Validation

This document is verified by inspection against the template checklist. Supplier quality implementation is verified by inspection and audit of flow-down, evaluation records, and issue routing (criteria TBD). Validation is programme authority approval (path TBD).

## 14. Risks

- Expectations not flowed down → suppliers working to incomplete definition; mitigation: flow-down per REQ-HFPX-ZSQ-001 (TBD)
- Evaluation gaps → unsuitable sourcing; mitigation: evaluation provisions per REQ-HFPX-ZSQ-002 (TBD)
- Evidence-verification mismatch → gaps or duplication at receipt; mitigation: coordination per REQ-HFPX-ZSQ-003 (TBD)
- Supplier issues uncontained → production impact; mitigation: routing per REQ-HFPX-ZSQ-004 (TBD)

## 15. Open Issues

- Flow-down content and mechanism (TBD)
- Evaluation and monitoring criteria and methods (TBD)
- Coordination details with incoming inspection (TBD)
- Routing criteria to NCM and corrective action (TBD)

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on Vol 00.13, Vol 20.11, HFPX-QA-QMS-001, and procurement definition. Supports HFPX-QA-INC-001, HFPX-QA-NCM-001, HFPX-QA-CRA-001, and HFPX-QA-TRC-001.

## 18. Traceability

Parent: manufacturing and quality classification; Vol 00.13, Vol 20 / Vol 20.11, Vol 25.8 quality liaison. Children: verification in HFPX-QA-INC-001; issues to HFPX-QA-NCM-001 and HFPX-QA-CRA-001. RTM: REQ-HFPX-ZSQ-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 28.8) |
