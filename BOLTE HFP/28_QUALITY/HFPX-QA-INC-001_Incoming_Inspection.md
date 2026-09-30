# Incoming Inspection

**Document ID:** HFPX-QA-INC-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the structure-only incoming inspection approach for HFP-X: how supplied articles are verified before use in production, how supplier quality linkage is maintained, and how records support traceability. This document owns Chapter 28.3 and does not set technical values.

## 2. Scope

Covers receipt, verification, segregation pending inspection, and release or rejection of incoming articles. Includes interfaces to supplier quality (HFPX-QA-SUQ-001) and to Vol 20 manufacturing flow. Detailed inspection methods, acceptance criteria values, and handling provisions remain TBD.

## 3. Applicable Documents

- HFPX-QA-QMS-001 Quality Management System
- HFPX-QA-INP-001 Inspection Plans
- HFPX-QA-SUQ-001 Supplier Quality (structure-only, TBD)
- HFPX-QA-NCM-001 Non-Conformance Management (for rejected articles, TBD)
- Vol 00.13 Supplier-related interfaces (details TBD)
- Vol 20.11 Supplier and procurement interfaces within manufacturing (details TBD)

## 4. Definitions & Acronyms

- Incoming inspection: verification performed after receipt and before production use
- Receipt status: pending, released, or rejected state of an incoming article (process TBD)
- Supplier linkage: relationship between purchase definition, supplier evidence, and incoming verification (details TBD)
- TBD/TBC: unknown data markers

## 5. System Context

Incoming inspection gates the entry of supplied articles into production:

```text
SUPPLIER (Vol 00.13 / 20.11 / 28.8) → RECEIPT → INCOMING INSPECTION (28.3) → RELEASED TO PRODUCTION (Vol 20)
                                            ↓
                                   REJECTION → NON-CONFORMANCE (28.6) + RECORDS / TRACEABILITY (28.11)
```

Inspection does not replace supplier control; it verifies conformance at receipt within defined scope (scope TBD).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-ZII-001 | The programme shall define incoming inspection scope and responsibilities, including receipt control, verification activities, and release authority. Details remain TBD. | Manufacturing quality classification / Vol 20 flow | Inspection |
| REQ-HFPX-ZII-002 | Incoming inspection shall verify supplied articles against defined purchase and design definition, using inspection plans where applicable. Verification content and methods remain TBD. | Vol 20.11 procurement interfaces / HFPX-QA-INP-001 | Inspection |
| REQ-HFPX-ZII-003 | The programme shall maintain linkage between supplier quality provisions (Vol 00.13, Vol 20.11, HFPX-QA-SUQ-001) and incoming inspection, so that supplier evidence and receipt verification are coordinated. Linkage details remain TBD. | Vol 00.13 supplier interfaces / HFPX-QA-SUQ-001 | Inspection |
| REQ-HFPX-ZII-004 | Incoming inspection shall generate records supporting traceability and disposition, including release and rejection records. Record types and retention linkage remain TBD. | Quality records classification / Vol 28.11 Traceability | Inspection |

## 7. Architecture

Incoming inspection structure (TBD): receipt and identification, pending segregation area and status control (process TBD), verification steps per plan, release and rejection routing, record set. Roles for receipt, inspection, and release authority remain TBD.

## 8. Detailed Design

To be defined. Intended elements include: receipt process (TBD), status identification method (TBD), verification step structure (TBD, without values), coordination with supplier evidence such as certificates where applicable (scope TBD), rejection routing to non-conformance (TBD), record template references (TBD). No sampling provisions, thresholds, or time values are set in this revision.

## 9. Interfaces

- Incoming ↔ HFPX-QA-SUQ-001: supplier controls, evidence, and escalation (TBD)
- Incoming ↔ Vol 00.13 / Vol 20.11: purchase definition and supplier interfaces (TBD)
- Incoming ↔ HFPX-QA-INP-001: plan-driven verification content (TBD)
- Incoming ↔ HFPX-QA-NCM-001: rejected-article handling (TBD)
- Incoming ↔ HFPX-QA-TRC-001: lot, batch, and serial linkage where applicable (TBD)

## 10. Operational Concept

Supplied articles are received, identified, held pending verification as defined, inspected per plan linkage, and either released to production or routed to non-conformance management. Handling of urgent release, partial release, or delegated verification, if any, remains TBD and is not assumed.

## 11. Safety

Incoming verification supports safety by preventing unverified articles from entering production. Safety-relevant incoming characteristics and any additional controls for safety-critical articles remain TBD in liaison with the safety programme. No safety values set in this document.

## 12. Performance

Measures of incoming inspection effectiveness and record completeness remain TBD, without targets or thresholds in this revision. No performance values baselined.

## 13. Verification & Validation

This document is verified by inspection against the template checklist. Incoming inspection implementation is verified by inspection and audit of records and status control (criteria TBD). Validation is programme authority approval (path TBD).

## 14. Risks

- Uncontrolled receipt → unverified articles in production; mitigation: receipt and status control per REQ-HFPX-ZII-001 (TBD)
- Disconnect from supplier evidence → duplicated or missed verification; mitigation: linkage per REQ-HFPX-ZII-003 (TBD)
- Incomplete records → untraceable provenance; mitigation: record structure per REQ-HFPX-ZII-004 (TBD)

## 15. Open Issues

- Incoming scope, responsibilities, and release authority (TBD)
- Verification content and method assignment (TBD)
- Supplier linkage details to Vol 00.13, Vol 20.11, and HFPX-QA-SUQ-001 (TBD)
- Record set and retention linkage (TBD)

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on Vol 00.13, Vol 20.11, HFPX-QA-SUQ-001 (supplier definition), HFPX-QA-INP-001 (plans), and HFPX-QA-QMS-001 (QMS framework). Supports Vol 20 production flow, HFPX-QA-NCM-001, HFPX-QA-TRC-001, and HFPX-QA-PAC-001.

## 18. Traceability

Parent: manufacturing and quality classification; Vol 20 / Vol 20.11, Vol 00.13 supplier interfaces, Vol 25.8 quality liaison. Children: execution records to HFPX-QA-TRC-001; rejections to HFPX-QA-NCM-001; evidence to HFPX-QA-PAC-001. RTM: REQ-HFPX-ZII-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 28.3) |
