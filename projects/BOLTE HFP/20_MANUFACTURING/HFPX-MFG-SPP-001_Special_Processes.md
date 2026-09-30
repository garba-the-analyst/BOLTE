# Special Processes

**Document ID:** HFPX-MFG-SPP-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the specification framework for HFP-X special processes: how they are inventoried, specified, qualified, approved, and revalidated. Owns Chapter 20.12.

## 2. Scope

Covers identification and governance of special processes across all manufacturing families. Special-process inventory, qualification and approval provisions, and revalidation provisions are TBD. Does not set process parameters or provide operator instructions. Applicable specifications, process controls, and qualification arrangements are TBD.

## 3. Applicable Documents

- HFPX-MFG-PRC-001 Manufacturing Processes
- Vol 03 material and process definitions (documents TBD)
- Vol 28 quality management provisions (documents TBD)
- Applicable special-process and qualification standards (TBD)

## 4. Definitions & Acronyms

- Special process: process whose outcome cannot be fully verified by subsequent inspection and therefore requires qualification and control (inventory TBD)
- Qualification and approval: demonstration and authorisation for production use (provisions TBD)
- Revalidation: renewal of qualification after defined conditions (provisions TBD)
- TBD: to be defined; TBC: to be confirmed

## 5. System Context

Special-process governance assures processes that inspection alone cannot assure:

```text
PROCESS IDENTIFICATION → SPECIAL-PROCESS DESIGNATION → SPECIFICATION → QUALIFICATION AND APPROVAL → CONTROLLED USE → REVALIDATION
```

This document governs designation and control; process-family documents govern family-specific specification and verification.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-DSP-001 | The special-process framework shall require that special processes be identified and maintained in a controlled inventory. | Manufacturing classification (HFPX-MFG-STR-001); Vol 03 material/process hooks (TBD); Vol 28 quality hooks (TBD) | Inspection |
| REQ-HFPX-DSP-002 | Each special process shall be governed by a controlled process specification defining controls and traceability. | Vol 03 material/process hooks (TBD); Vol 28 quality hooks (TBD) | Inspection |
| REQ-HFPX-DSP-003 | Each special process shall be qualified and approved before use in production, using representative materials and configurations. | Vol 03 material/process hooks (TBD); Vol 28 quality hooks (TBD) | Demonstration |
| REQ-HFPX-DSP-004 | The special-process framework shall require revalidation after defined conditions and define verification using Inspection, Demonstration, or Test as applicable. | Vol 03 material/process hooks (TBD); Vol 28 quality hooks (TBD) | Inspection |

## 7. Architecture

Special-process governance is organised by inventory → specification → qualification and approval → controlled use → monitoring → revalidation. Designation criteria, approval authority, and monitoring provisions are TBD.

## 8. Detailed Design

To be elaborated (all TBD): designation criteria, inventory structure, specification contents, qualification and approval scope and evidence, personnel and equipment qualification hooks, and revalidation conditions. No process parameters are set in this document.

## 9. Interfaces

- MFG-SPP ↔ Vol 03 for material and process suitability (TBD)
- MFG-SPP ↔ process-family documents for family-specific specification and control
- MFG-SPP ↔ Vol 28 for qualification, approval, nonconformance, and records (TBD)
- MFG-SPP ↔ supplier and tooling documents for execution context (TBD)

## 10. Operational Concept

Special processes are introduced as: designate → specify → qualify and approve → use under control → monitor → revalidate when required. Authority and sequencing are TBD.

## 11. Safety

This document creates no hazardous operations and provides no operating instructions. It requires that special-process safety provisions be defined in applicable process and safety documents. No energetics handling instructions are contained in this document.

## 12. Performance

Special-process measures such as conformity and stability are TBD. No thresholds are baselined at this revision.

## 13. Verification & Validation

Verification of the framework and inventory is by Inspection. Qualification and revalidation are by Demonstration and, where defined, Test. Product verification is by Inspection and Test as defined.

## 14. Risks

- Unidentified special processes → uncontrolled characteristics; mitigation: complete inventory and designation criteria (TBD)
- Use without approval → nonconforming product; mitigation: enforce qualification and approval before production (TBD)
- Lapsed qualification → drift; mitigation: define revalidation provisions (TBD)

## 15. Open Issues

- Special-process inventory and designation criteria (TBD)
- Qualification and approval provisions (TBD)
- Revalidation conditions and verification provisions (TBD)

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on HFPX-MFG-PRC-001, Vol 03 definitions (TBD), and Vol 28 provisions (TBD). Enables qualified use of special processes in production and acceptance.

## 18. Traceability

Parent: manufacturing classification (HFPX-MFG-STR-001); Vol 03 material/process hooks (TBD); Vol 28 quality hooks (TBD). Children: qualified special-process procedures and acceptance evidence (TBD). RTM: REQ-HFPX-DSP-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 20.12) |
