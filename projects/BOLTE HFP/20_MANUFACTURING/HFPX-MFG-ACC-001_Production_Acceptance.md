# Production Acceptance

**Document ID:** HFPX-MFG-ACC-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the specification framework for HFP-X production acceptance: how conforming product is verified, accepted, and recorded. Owns Chapter 20.14 with hooks to Vol 28.12.

## 2. Scope

Covers acceptance planning, acceptance verification, acceptance decisions, and acceptance records for production hardware. Acceptance criteria are TBD per item. Records provisions are TBD. Does not set acceptance values. Applicable specifications, process controls, and qualification arrangements are TBD.

## 3. Applicable Documents

- HFPX-MFG-STR-001 Manufacturing Strategy
- HFPX-MFG-PAR-001 Production Architecture
- Vol 28.12 acceptance and records provisions (documents TBD)
- Vol 03 design definitions subject to acceptance (documents TBD)
- Applicable inspection and test standards (TBD)

## 4. Definitions & Acronyms

- Acceptance: formal determination that product conforms to its definition (criteria TBD per item)
- Acceptance record: retained evidence supporting the acceptance decision (provisions TBD)
- TBD: to be defined; TBC: to be confirmed

## 5. System Context

Acceptance closes the production loop:

```text
CONTROLLED PRODUCTION → VERIFICATION → ACCEPTANCE DECISION → ACCEPTANCE RECORDS → DELIVERY OR INTEGRATION
```

This document governs acceptance structure; Vol 28.12 governs quality acceptance and records provisions.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-DAC-001 | Production acceptance shall be governed by defined acceptance criteria per item. | Manufacturing classification (HFPX-MFG-STR-001); Vol 03 material/process hooks (TBD); Vol 28.12 hooks (TBD) | Inspection |
| REQ-HFPX-DAC-002 | Production acceptance shall be performed using Inspection, Demonstration, or Test as applicable to the item. | Vol 03 material/process hooks (TBD); Vol 28.12 hooks (TBD) | Inspection |
| REQ-HFPX-DAC-003 | Production acceptance decisions and associated records shall be retained under configuration control. | Manufacturing classification (HFPX-MFG-STR-001); Vol 28.12 hooks (TBD) | Inspection |
| REQ-HFPX-DAC-004 | Nonconforming product identified during acceptance shall be controlled under Vol 28 nonconformance provisions. | Manufacturing classification (HFPX-MFG-STR-001); Vol 28 quality hooks (TBD) | Inspection |

## 7. Architecture

Acceptance is organised by criteria definition → verification → decision → records → disposition. Acceptance authority and staging within production flow are TBD.

## 8. Detailed Design

To be elaborated (all TBD): acceptance plan structure, criteria definition per item, verification allocation, decision authority, nonconformance linkage, and records contents and retention. No acceptance values are set in this document.

## 9. Interfaces

- MFG-ACC ↔ Vol 28.12 for acceptance, nonconformance, and records provisions (TBD)
- MFG-ACC ↔ Vol 03 for design definitions subject to acceptance (TBD)
- MFG-ACC ↔ process-family and tooling documents for verification context
- MFG-ACC ↔ HFPX-MFG-SUP-001 for incoming and supplier acceptance

## 10. Operational Concept

Acceptance operates as: define criteria → verify product → decide → record → disposition to integration, delivery, or nonconformance control. Sequencing and authority are TBD.

## 11. Safety

This document creates no hazardous operations. It requires that acceptance-related safety provisions be defined in applicable process and safety documents. No energetics handling instructions are contained in this document.

## 12. Performance

Acceptance measures such as conformity and record completeness are TBD. No thresholds are baselined at this revision.

## 13. Verification & Validation

Verification of the acceptance framework is by Inspection. Product acceptance is by Inspection, Demonstration, or Test as defined per item. Records completeness is verified by Inspection.

## 14. Risks

- Undefined criteria → inconsistent acceptance; mitigation: define criteria per item (TBD)
- Incomplete records → loss of conformity evidence; mitigation: define records provisions with Vol 28.12 (TBD)
- Uncontrolled nonconformance → escape; mitigation: enforce Vol 28 nonconformance control (TBD)

## 15. Open Issues

- Acceptance criteria per item (TBD)
- Acceptance records contents and retention (TBD)
- Hooks to Vol 28.12 and staging in production flow (TBD)

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on HFPX-MFG-STR-001, HFPX-MFG-PAR-001, Vol 03 definitions (TBD), and Vol 28.12 provisions (TBD). Enables delivery, integration, and operational use decisions.

## 18. Traceability

Parent: manufacturing classification (HFPX-MFG-STR-001); Vol 03 material/process hooks (TBD); Vol 28.12 hooks (TBD). Children: item acceptance evidence and records (TBD). RTM: REQ-HFPX-DAC-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 20.14) |
