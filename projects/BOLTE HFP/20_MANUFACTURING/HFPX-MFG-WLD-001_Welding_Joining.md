# Welding / Joining

**Document ID:** HFPX-MFG-WLD-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the specification framework for welding and joining of HFP-X hardware: what shall be specified, controlled, qualified, and verified. Owns Chapter 20.8.

## 2. Scope

Covers welding and joining from joint definition through preparation, execution, and verification, as applicable to approved joint configurations. Joint qualification provisions and NDT hooks are TBD. Does not set joint parameters or dimensional values, and does not provide operator instructions. Applicable specifications, process controls, and qualification arrangements are TBD.

## 3. Applicable Documents

- HFPX-MFG-PRC-001 Manufacturing Processes
- Vol 03 material and process definitions (documents TBD)
- HFPX-MFG-SPP-001 Special Processes (inventory and qualification, TBD)
- Vol 28 quality management provisions (documents TBD)
- Applicable welding, joining, and NDT standards (TBD)

## 4. Definitions & Acronyms

- Joint: approved configuration by which parts are welded or joined (definitions TBD)
- Joint qualification: demonstration that a joint configuration produced by a specified process meets its definition (provisions TBD)
- NDT: non-destructive testing (hooks TBD)
- TBD: to be defined; TBC: to be confirmed

## 5. System Context

Welding and joining converts prepared parts into conforming assemblies under qualified procedures, controlled execution, and verification:

```text
JOINT DEFINITION → JOINING SPECIFICATION → JOINT QUALIFICATION → CONTROLLED EXECUTION → VERIFICATION AND ACCEPTANCE
```

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-DWD-001 | The welding and joining process shall be governed by a controlled process specification. | Manufacturing classification (HFPX-MFG-STR-001); Vol 03 material/process hooks (TBD); Vol 28 quality hooks (TBD) | Inspection |
| REQ-HFPX-DWD-002 | The welding and joining process specification shall define process controls, including joint preparation control, execution control, and traceability. | Vol 03 material/process hooks (TBD); Vol 28 quality hooks (TBD) | Inspection |
| REQ-HFPX-DWD-003 | Each production joint configuration shall be qualified before use in production, using representative materials and configurations. | Vol 03 material/process hooks (TBD); Vol 28 quality hooks (TBD) | Demonstration |
| REQ-HFPX-DWD-004 | The welding and joining process specification shall define verification using Inspection, Demonstration, or Test as applicable, including NDT hooks. | Vol 03 material/process hooks (TBD); Vol 28 quality hooks (TBD) | Inspection |

## 7. Architecture

Joining scope is organised by joint definition → procedure specification → joint qualification → controlled execution → verification. Qualification authority and verification staging are TBD.

## 8. Detailed Design

To be elaborated (all TBD): specification contents, joint register, preparation and execution control approach, joint qualification scope and evidence, NDT hooks, and requalification conditions. No joint parameters or values are set in this document.

## 9. Interfaces

- MFG-WLD ↔ Vol 03 for material compatibility and joint design provisions (TBD)
- MFG-WLD ↔ HFPX-MFG-SPP-001 for special-process inventory and qualification (TBD)
- MFG-WLD ↔ Vol 28 for qualification, inspection and NDT, nonconformance, and records (TBD)
- MFG-WLD ↔ design volumes for joint configuration definition (TBD)

## 10. Operational Concept

Joining work is introduced as: define joint → release procedure specification → qualify joint → execute under control → verify → record. Authority and sequencing are TBD.

## 11. Safety

This document creates no hazardous operations and provides no operating instructions. It requires that joining safety provisions, including equipment and environment safety, be defined in applicable process and safety documents. No energetics handling instructions are contained in this document.

## 12. Performance

Joining process measures such as conformity and stability are TBD. No thresholds are baselined at this revision.

## 13. Verification & Validation

Verification of the specification is by Inspection. Joint qualification is by Demonstration and, where defined, Test. Product verification is by Inspection and Test as defined, including NDT hooks (TBD).

## 14. Risks

- Unqualified joints in production → uncertain integrity; mitigation: enforce joint qualification before production (TBD)
- Uncontrolled preparation or execution → variation; mitigation: define controls and traceability (TBD)
- Undetected joint defects → acceptance risk; mitigation: define verification including NDT hooks (TBD)

## 15. Open Issues

- Applicable welding and joining specifications register (TBD)
- Joint qualification provisions and register (TBD)
- NDT hooks, verification provisions, and requalification conditions (TBD)

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on HFPX-MFG-PRC-001, Vol 03 definitions (TBD), special-process provisions (TBD), and Vol 28 provisions (TBD). Enables production execution and acceptance.

## 18. Traceability

Parent: manufacturing classification (HFPX-MFG-STR-001); Vol 03 material/process hooks (TBD); Vol 28 quality hooks (TBD). Children: qualified joining procedures and acceptance evidence (TBD). RTM: REQ-HFPX-DWD-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 20.8) |
