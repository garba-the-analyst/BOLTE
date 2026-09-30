# Machining

**Document ID:** HFPX-MFG-MCH-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the specification framework for conventional machining of HFP-X hardware: what shall be specified, controlled, qualified, and verified. Owns Chapter 20.7.

## 2. Scope

Covers machining from setup definition through material removal and verification, within approved design definition and tooling control. Excludes CNC programme governance where allocated to HFPX-MFG-CNC-001; allocation boundary is TBD. Does not set machining parameters or dimensional values, and does not provide operator instructions. Applicable specifications, process controls, and qualification arrangements are TBD.

## 3. Applicable Documents

- HFPX-MFG-PRC-001 Manufacturing Processes
- HFPX-MFG-CNC-001 CNC Manufacturing (boundary, TBD)
- HFPX-MFG-TOL-001 Production Tooling (tooling control, TBD)
- Vol 03 material and process definitions (documents TBD)
- Vol 28 quality management provisions (documents TBD)
- Applicable machining and inspection standards (TBD)

## 4. Definitions & Acronyms

- Machining: material removal by mechanical means under controlled setup and tooling (scope TBD)
- Setup: defined configuration of workpiece, fixture, tooling, and datum (control TBD)
- TBD: to be defined; TBC: to be confirmed

## 5. System Context

Machining converts stock and preforms into conforming geometry under controlled setup, tooling, and verification:

```text
DESIGN DEFINITION → MACHINING SPECIFICATION → QUALIFIED SETUP AND TOOLING → CONTROLLED EXECUTION → INSPECTION AND ACCEPTANCE
```

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-DMC-001 | The machining process shall be governed by a controlled process specification. | Manufacturing classification (HFPX-MFG-STR-001); Vol 03 material/process hooks (TBD); Vol 28 quality hooks (TBD) | Inspection |
| REQ-HFPX-DMC-002 | The machining process specification shall define process controls, including setup control, tooling control, and handling control. | Vol 03 material/process hooks (TBD); Vol 28 quality hooks (TBD) | Inspection |
| REQ-HFPX-DMC-003 | The machining process shall be qualified before use in production, using representative material and geometry. | Vol 03 material/process hooks (TBD); Vol 28 quality hooks (TBD) | Demonstration |
| REQ-HFPX-DMC-004 | The machining process specification shall define verification using Inspection, Demonstration, or Test as applicable. | Vol 03 material/process hooks (TBD); Vol 28 quality hooks (TBD) | Inspection |

## 7. Architecture

Machining scope is organised by setup definition → tooling → execution → verification. Allocation with CNC manufacturing and verification staging are TBD.

## 8. Detailed Design

To be elaborated (all TBD): specification contents, setup definition approach, tooling linkage, handling provisions, qualification scope and evidence, and requalification conditions. No machining parameters or dimensional values are set in this document.

## 9. Interfaces

- MFG-MCH ↔ HFPX-MFG-CNC-001 for machining allocation boundary (TBD)
- MFG-MCH ↔ Vol 03 for material and design definition (TBD)
- MFG-MCH ↔ HFPX-MFG-TOL-001 for fixtures, tooling, and calibration hooks (TBD)
- MFG-MCH ↔ Vol 28 for qualification, inspection, nonconformance, and records (TBD)

## 10. Operational Concept

Machining work is introduced as: release setup and tooling definition → qualify process → execute under control → verify → record. Authority and sequencing are TBD.

## 11. Safety

This document creates no hazardous operations and provides no operating instructions. It requires that machine safety and handling provisions be defined in applicable process and safety documents. No energetics handling instructions are contained in this document.

## 12. Performance

Machining process measures such as conformity and stability are TBD. No thresholds are baselined at this revision.

## 13. Verification & Validation

Verification of the specification is by Inspection. Qualification is by Demonstration and, where defined, Test. Product verification is by Inspection as defined in the specification and acceptance documents.

## 14. Risks

- Uncontrolled setups → nonconforming geometry; mitigation: controlled setup definition (TBD)
- Unqualified process use → variation; mitigation: enforce qualification before production (TBD)
- Tooling variation → loss of repeatability; mitigation: link to controlled tooling provisions (TBD)

## 15. Open Issues

- Applicable machining specifications register (TBD)
- Allocation boundary with CNC manufacturing (TBD)
- Qualification scope and requalification conditions (TBD)

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on HFPX-MFG-PRC-001, Vol 03 definitions (TBD), Vol 28 provisions (TBD), and tooling control (TBD). Enables production execution and acceptance.

## 18. Traceability

Parent: manufacturing classification (HFPX-MFG-STR-001); Vol 03 material/process hooks (TBD); Vol 28 quality hooks (TBD). Children: qualified machining work instructions and acceptance evidence (TBD). RTM: REQ-HFPX-DMC-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 20.7) |
