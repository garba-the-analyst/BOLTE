# Composite Manufacturing

**Document ID:** HFPX-MFG-CMP-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the specification framework for composite manufacturing of HFP-X hardware: what shall be specified, controlled, qualified, and verified. Owns Chapter 20.5 and interfaces to Vol 03.11.

## 2. Scope

Covers composite manufacturing from material control through layup, cure and consolidation, finishing, and verification, as applicable to approved composite applications. Does not set material selections, layup definitions, cure definitions, or dimensional values, and does not provide operator instructions. Applicable specifications, process controls, and qualification arrangements are TBD.

## 3. Applicable Documents

- HFPX-MFG-PRC-001 Manufacturing Processes
- Vol 03.11 composite material and process definitions (documents TBD)
- HFPX-MFG-SPP-001 Special Processes (inventory and qualification, TBD)
- Vol 28 quality management provisions (documents TBD)
- Applicable composite and NDT standards (TBD)

## 4. Definitions & Acronyms

- Layup: placement of composite constituents prior to cure and consolidation (definitions TBD)
- Cure and consolidation: transformation of laid-up constituents into consolidated structure (definitions TBD)
- NDT: non-destructive testing (hooks TBD)
- TBD: to be defined; TBC: to be confirmed

## 5. System Context

Composite manufacturing converts approved Vol 03.11 definitions into conforming structure under controlled environment, tooling, and verification:

```text
VOL 03.11 DEFINITION → COMPOSITE PROCESS SPECIFICATION → QUALIFIED PROCESS → CONTROLLED PRODUCTION → VERIFICATION AND ACCEPTANCE
```

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-DCM-001 | The composite manufacturing process shall be governed by a controlled process specification consistent with Vol 03.11 definitions. | Manufacturing classification (HFPX-MFG-STR-001); Vol 03.11 hooks (TBD); Vol 28 quality hooks (TBD) | Inspection |
| REQ-HFPX-DCM-002 | The composite manufacturing process specification shall define process controls, including material control, environment control, tooling control, and traceability. | Vol 03.11 hooks (TBD); Vol 28 quality hooks (TBD) | Inspection |
| REQ-HFPX-DCM-003 | The composite manufacturing process shall be qualified before use in production, using representative materials and configurations. | Vol 03.11 hooks (TBD); Vol 28 quality hooks (TBD) | Demonstration |
| REQ-HFPX-DCM-004 | The composite manufacturing process specification shall define verification using Inspection, Demonstration, or Test as applicable, including NDT hooks. | Vol 03.11 hooks (TBD); Vol 28 quality hooks (TBD) | Inspection |

## 7. Architecture

Composite scope is organised by material control → layup → cure and consolidation → finishing → verification. Environment, tooling, and verification staging are TBD.

## 8. Detailed Design

To be elaborated (all TBD): specification contents, material storage and life control linkage to Vol 03.11, environment provisions, tooling provisions, cure and consolidation control approach, qualification scope and evidence, and requalification conditions. No material values, layup definitions, or cure definitions are set in this document.

## 9. Interfaces

- MFG-CMP ↔ Vol 03.11 for composite materials, allowables basis, and process compatibility (TBD)
- MFG-CMP ↔ HFPX-MFG-SPP-001 for special-process inventory and qualification (TBD)
- MFG-CMP ↔ HFPX-MFG-TOL-001 for composite tooling control (TBD)
- MFG-CMP ↔ Vol 28 for qualification, inspection and NDT, nonconformance, and records (TBD)

## 10. Operational Concept

Composite work is introduced as: confirm Vol 03.11 definition → release process specification → qualify process → produce under control → verify → record. Authority and sequencing are TBD.

## 11. Safety

This document creates no hazardous operations and provides no operating instructions. It requires that material handling safety, environment safety, and equipment safety provisions be defined in applicable process and safety documents. No energetics handling instructions are contained in this document.

## 12. Performance

Composite process measures such as conformity and stability are TBD. No thresholds are baselined at this revision.

## 13. Verification & Validation

Verification of the specification is by Inspection. Qualification is by Demonstration and, where defined, Test. Product verification is by Inspection and Test as defined, including NDT hooks (TBD).

## 14. Risks

- Material outside control → nonconforming structure; mitigation: define material control linked to Vol 03.11 (TBD)
- Unqualified cure and consolidation → inconsistent properties; mitigation: enforce qualification before production (TBD)
- Undetected defects → acceptance risk; mitigation: define verification including NDT hooks (TBD)

## 15. Open Issues

- Applicable composite specifications register (TBD)
- Vol 03.11 interface definitions (TBD)
- Qualification scope, NDT hooks, and requalification conditions (TBD)

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on HFPX-MFG-PRC-001, Vol 03.11 definitions (TBD), special-process provisions (TBD), and Vol 28 provisions (TBD). Enables production execution and acceptance.

## 18. Traceability

Parent: manufacturing classification (HFPX-MFG-STR-001); Vol 03.11 hooks (TBD); Vol 28 quality hooks (TBD). Children: qualified composite work instructions and acceptance evidence (TBD). RTM: REQ-HFPX-DCM-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 20.5) |
