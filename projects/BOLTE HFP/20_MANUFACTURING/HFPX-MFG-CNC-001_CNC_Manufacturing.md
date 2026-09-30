# CNC Manufacturing

**Document ID:** HFPX-MFG-CNC-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the specification framework for CNC manufacturing of HFP-X hardware: what shall be specified, controlled, qualified, and verified. Owns Chapter 20.4.

## 2. Scope

Covers CNC manufacturing from programming definition through machining execution and in-process verification, within the bounds of approved design definition and tooling control. Does not set cutting parameters, programmes, or dimensional values, and does not provide operator instructions. Applicable specifications, process controls, and qualification arrangements are TBD.

## 3. Applicable Documents

- HFPX-MFG-PRC-001 Manufacturing Processes
- HFPX-MFG-TOL-001 Production Tooling (tooling control, TBD)
- Vol 03 material and process definitions (documents TBD)
- Vol 28 quality management provisions (documents TBD)
- Applicable CNC, programming, and inspection standards (TBD)

## 4. Definitions & Acronyms

- CNC: computer numerical control
- CNC programme: controlled definition from which CNC operations are executed (management TBD)
- In-process verification: verification performed during or between CNC operations (methods TBD)
- TBD: to be defined; TBC: to be confirmed

## 5. System Context

CNC manufacturing converts qualified design definition into conforming geometry under controlled programmes, tooling, and verification:

```text
DESIGN DEFINITION → CNC PROGRAMME → QUALIFIED CNC PROCESS → CONTROLLED EXECUTION → INSPECTION AND ACCEPTANCE
```

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-DCN-001 | The CNC manufacturing process shall be governed by a controlled process specification. | Manufacturing classification (HFPX-MFG-STR-001); Vol 03 material/process hooks (TBD); Vol 28 quality hooks (TBD) | Inspection |
| REQ-HFPX-DCN-002 | The CNC manufacturing process specification shall define process controls, including programme control, tooling control, and setup control. | Vol 03 material/process hooks (TBD); Vol 28 quality hooks (TBD) | Inspection |
| REQ-HFPX-DCN-003 | The CNC manufacturing process shall be qualified before use in production, using representative material and geometry. | Vol 03 material/process hooks (TBD); Vol 28 quality hooks (TBD) | Demonstration |
| REQ-HFPX-DCN-004 | The CNC manufacturing process specification shall define verification using Inspection, Demonstration, or Test as applicable. | Vol 03 material/process hooks (TBD); Vol 28 quality hooks (TBD) | Inspection |

## 7. Architecture

CNC scope is organised by programme definition → setup and tooling → execution → in-process verification → final verification. Programme approval, tooling linkage, and verification staging are TBD.

## 8. Detailed Design

To be elaborated (all TBD): specification contents, programme generation and approval, tooling and fixture linkage, setup definition, in-process controls, qualification scope and evidence, and requalification conditions. No parameters, programmes, or dimensional values are set in this document.

## 9. Interfaces

- MFG-CNC ↔ Vol 03 for material machinability and design definition (TBD)
- MFG-CNC ↔ HFPX-MFG-TOL-001 for fixtures, cutting tool management, and calibration hooks (TBD)
- MFG-CNC ↔ Vol 28 for qualification, inspection, nonconformance, and records (TBD)
- MFG-CNC ↔ HFPX-MFG-MCH-001 for machining boundary and allocation

## 10. Operational Concept

CNC work is introduced as: release programme and setup definition → qualify process → execute under control → verify → record. Authority and sequencing are TBD.

## 11. Safety

This document creates no hazardous operations and provides no operating instructions. It requires that machine safety, handling, and environmental provisions be defined in applicable process and safety documents. No energetics handling instructions are contained in this document.

## 12. Performance

CNC process measures such as conformity and stability are TBD. No thresholds are baselined at this revision.

## 13. Verification & Validation

Verification of the specification is by Inspection. Qualification is by Demonstration and, where defined, Test. Product verification is by Inspection as defined in the specification and acceptance documents.

## 14. Risks

- Uncontrolled programmes → nonconforming geometry; mitigation: controlled programme definition and approval (TBD)
- Unqualified process use → variation; mitigation: enforce qualification before production (TBD)
- Tooling variation → loss of repeatability; mitigation: link to controlled tooling provisions (TBD)

## 15. Open Issues

- Applicable CNC specifications register (TBD)
- Programme control and approval provisions (TBD)
- Qualification scope and requalification conditions (TBD)

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on HFPX-MFG-PRC-001, Vol 03 definitions (TBD), Vol 28 provisions (TBD), and tooling control (TBD). Enables production execution and acceptance.

## 18. Traceability

Parent: manufacturing classification (HFPX-MFG-STR-001); Vol 03 material/process hooks (TBD); Vol 28 quality hooks (TBD). Children: qualified CNC work instructions and acceptance evidence (TBD). RTM: REQ-HFPX-DCN-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 20.4) |
