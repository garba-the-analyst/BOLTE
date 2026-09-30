# Surface Treatment

**Document ID:** HFPX-MFG-SFT-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the specification framework for surface treatment of HFP-X hardware: what shall be specified, controlled, qualified, and verified. Owns Chapter 20.9.

## 2. Scope

Covers surface treatment from surface preparation through treatment and verification, as applicable to approved surface definitions. Does not set treatment selections, bath or media definitions, or acceptance values, and does not provide operator instructions. Applicable specifications, process controls, and qualification arrangements are TBD.

## 3. Applicable Documents

- HFPX-MFG-PRC-001 Manufacturing Processes
- Vol 03 material and process definitions (documents TBD)
- HFPX-MFG-SPP-001 Special Processes (inventory and qualification, TBD)
- Vol 28 quality management provisions (documents TBD)
- Applicable surface treatment and inspection standards (TBD)

## 4. Definitions & Acronyms

- Surface treatment: controlled alteration of a surface to achieve a specified definition (scope TBD)
- Surface preparation: operations required before treatment to achieve a conforming basis (definitions TBD)
- TBD: to be defined; TBC: to be confirmed

## 5. System Context

Surface treatment converts prepared surfaces into conforming definitions under controlled treatment and verification:

```text
SURFACE DEFINITION → TREATMENT SPECIFICATION → QUALIFIED PROCESS → CONTROLLED EXECUTION → VERIFICATION AND ACCEPTANCE
```

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-DSR-001 | The surface treatment process shall be governed by a controlled process specification. | Manufacturing classification (HFPX-MFG-STR-001); Vol 03 material/process hooks (TBD); Vol 28 quality hooks (TBD) | Inspection |
| REQ-HFPX-DSR-002 | The surface treatment process specification shall define process controls, including preparation control, treatment control, handling control, and traceability. | Vol 03 material/process hooks (TBD); Vol 28 quality hooks (TBD) | Inspection |
| REQ-HFPX-DSR-003 | The surface treatment process shall be qualified before use in production, using representative materials and configurations. | Vol 03 material/process hooks (TBD); Vol 28 quality hooks (TBD) | Demonstration |
| REQ-HFPX-DSR-004 | The surface treatment process specification shall define verification using Inspection, Demonstration, or Test as applicable. | Vol 03 material/process hooks (TBD); Vol 28 quality hooks (TBD) | Inspection |

## 7. Architecture

Surface scope is organised by preparation → treatment → handling → verification. Treatment allocation, masking provisions, and verification staging are TBD.

## 8. Detailed Design

To be elaborated (all TBD): specification contents, preparation approach, treatment control approach, handling provisions, qualification scope and evidence, and requalification conditions. No treatment parameters or acceptance values are set in this document.

## 9. Interfaces

- MFG-SFT ↔ Vol 03 for material compatibility and surface definitions (TBD)
- MFG-SFT ↔ HFPX-MFG-SPP-001 for special-process inventory and qualification (TBD)
- MFG-SFT ↔ Vol 28 for qualification, inspection and test, nonconformance, and records (TBD)
- MFG-SFT ↔ design volumes for surface definition allocation (TBD)

## 10. Operational Concept

Surface work is introduced as: confirm surface definition → release treatment specification → qualify process → treat under control → verify → record. Authority and sequencing are TBD.

## 11. Safety

This document creates no hazardous operations and provides no operating instructions. It requires that chemical, environmental, and handling safety provisions be defined in applicable process and safety documents. No energetics handling instructions are contained in this document.

## 12. Performance

Surface process measures such as conformity and stability are TBD. No thresholds are baselined at this revision.

## 13. Verification & Validation

Verification of the specification is by Inspection. Qualification is by Demonstration and, where defined, Test. Product verification is by Inspection and Test as defined.

## 14. Risks

- Incompatible treatment selection → material degradation; mitigation: align treatment with Vol 03 definitions (TBD)
- Unqualified treatment use → variation; mitigation: enforce qualification before production (TBD)
- Handling damage after treatment → loss of conformity; mitigation: define handling control (TBD)

## 15. Open Issues

- Applicable surface treatment specifications register (TBD)
- Treatment allocation to hardware (TBD)
- Qualification scope, verification provisions, and requalification conditions (TBD)

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on HFPX-MFG-PRC-001, Vol 03 definitions (TBD), special-process provisions (TBD), and Vol 28 provisions (TBD). Enables production execution and acceptance.

## 18. Traceability

Parent: manufacturing classification (HFPX-MFG-STR-001); Vol 03 material/process hooks (TBD); Vol 28 quality hooks (TBD). Children: qualified surface treatment procedures and acceptance evidence (TBD). RTM: REQ-HFPX-DSR-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 20.9) |
