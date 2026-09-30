# Supplier Requirements

**Document ID:** HFPX-MFG-SUP-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define supplier requirements for HFP-X production: how supplier work is specified, controlled, flowed down, and verified. Owns Chapter 20.11 with hooks to 00.13 and 28.8.

## 2. Scope

Covers supplier selection principles, requirement flow-down, supplier process control, and supplier verification and records. Flow-down provisions are TBD. Does not select suppliers or set commercial terms. Applicable specifications, process controls, and qualification arrangements are TBD.

## 3. Applicable Documents

- HFPX-MFG-STR-001 Manufacturing Strategy
- HFPX-MFG-PAR-001 Production Architecture
- Vol 00.13 supply and procurement provisions (documents TBD)
- Vol 28.8 supplier quality provisions (documents TBD)
- Vol 03 material and process definitions (documents TBD)
- Applicable supplier quality standards (TBD)

## 4. Definitions & Acronyms

- Flow-down: allocation of applicable requirements to supplier work scope (provisions TBD)
- Supplier work: production or processing performed outside in-house work centres (scope TBD)
- TBD: to be defined; TBC: to be confirmed

## 5. System Context

Supplier requirements extend production control across organisational boundaries:

```text
PRODUCTION ARCHITECTURE → SUPPLIER REQUIREMENTS → FLOWED-DOWN SPECIFICATIONS → SUPPLIER VERIFICATION → ACCEPTANCE
```

This document governs requirements and control; Vol 00.13 and Vol 28.8 govern procurement and supplier quality provisions.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-DSU-001 | The supplier requirements shall define how production requirements are flowed down to supplier work scope. | Manufacturing classification (HFPX-MFG-STR-001); Vol 00.13 hooks (TBD); Vol 28.8 hooks (TBD) | Inspection |
| REQ-HFPX-DSU-002 | The supplier requirements shall require that supplier processes be specified, controlled, and qualified before use in production. | Vol 03 material/process hooks (TBD); Vol 28.8 hooks (TBD) | Inspection |
| REQ-HFPX-DSU-003 | The supplier requirements shall define supplier verification and record provisions for supplied product and processes. | Manufacturing classification (HFPX-MFG-STR-001); Vol 28.8 hooks (TBD) | Inspection |
| REQ-HFPX-DSU-004 | The supplier requirements shall define the relationship between supplier control, incoming control, nonconformance handling, and acceptance. | Manufacturing classification (HFPX-MFG-STR-001); Vol 28 quality hooks (TBD) | Inspection |

## 7. Architecture

Supplier control is organised by work allocation → flow-down → supplier qualification and process qualification → execution oversight → incoming verification and acceptance. Selection authority and oversight levels are TBD.

## 8. Detailed Design

To be elaborated (all TBD): flow-down structure and artefacts, supplier process qualification provisions, oversight and audit hooks to Vol 28.8, procurement hooks to Vol 00.13, and records provisions. No supplier selections or commercial values are set in this document.

## 9. Interfaces

- MFG-SUP ↔ Vol 00.13 for procurement and contractual provisions (TBD)
- MFG-SUP ↔ Vol 28.8 for supplier quality, audit, and approval provisions (TBD)
- MFG-SUP ↔ Vol 03 for flowed-down material and process definitions (TBD)
- MFG-SUP ↔ HFPX-MFG-ACC-001 for incoming verification and acceptance

## 10. Operational Concept

Supplier work is introduced as: allocate work → flow down requirements → qualify supplier and processes → oversee execution → verify on receipt → record. Authority and sequencing are TBD.

## 11. Safety

This document creates no hazardous operations. It requires that supplier safety and handling provisions be flowed down through applicable specifications and safety documents. No energetics handling instructions are contained in this document.

## 12. Performance

Supplier performance measures are TBD. No thresholds are baselined at this revision.

## 13. Verification & Validation

Verification is by Inspection of flow-down definition and records provisions. Supplier process qualification is by Demonstration and, where defined, Test. Product verification is by Inspection and Test on receipt as defined.

## 14. Risks

- Incomplete flow-down → uncontrolled supplier work; mitigation: complete flow-down provisions (TBD)
- Unqualified supplier processes → nonconforming supply; mitigation: enforce qualification before production (TBD)
- Weak incoming verification → defect escape; mitigation: align with acceptance provisions (TBD)

## 15. Open Issues

- Flow-down structure and artefacts (TBD)
- Hooks to Vol 00.13 and Vol 28.8 (TBD)
- Supplier qualification and oversight provisions (TBD)

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on HFPX-MFG-STR-001, HFPX-MFG-PAR-001, Vol 00.13 provisions (TBD), Vol 03 definitions (TBD), and Vol 28.8 provisions (TBD). Enables supplier execution and acceptance.

## 18. Traceability

Parent: manufacturing classification (HFPX-MFG-STR-001); Vol 03 material/process hooks (TBD); Vol 00.13 and Vol 28.8 hooks (TBD). Children: flowed-down supplier specifications and acceptance evidence (TBD). RTM: REQ-HFPX-DSU-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 20.11) |
