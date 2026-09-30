# Additive Manufacturing

**Document ID:** HFPX-MFG-ADM-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the specification framework for additive manufacturing of HFP-X hardware: what shall be specified, controlled, qualified, and verified, and how approved applications are governed. Owns Chapter 20.6.

## 2. Scope

Covers additive manufacturing from feedstock control through build, post-processing, and verification, limited to approved applications. Approved applications are TBD. Does not set build parameters, post-processing definitions, or dimensional values, and does not provide operator instructions. Applicable specifications, process controls, and qualification practice are TBD.

## 3. Applicable Documents

- HFPX-MFG-PRC-001 Manufacturing Processes
- Vol 03 material and process definitions (documents TBD)
- HFPX-MFG-SPP-001 Special Processes (inventory and qualification, TBD)
- Vol 28 quality management provisions (documents TBD)
- Applicable additive manufacturing and NDT standards (TBD)

## 4. Definitions & Acronyms

- Approved application: hardware scope for which additive manufacturing is permitted (list TBD)
- Feedstock: input material for the additive process (control TBD)
- Post-processing: operations after build required to achieve conforming product (definitions TBD)
- TBD: to be defined; TBC: to be confirmed

## 5. System Context

Additive manufacturing converts approved design definitions into conforming hardware under controlled feedstock, build, post-processing, and verification:

```text
APPROVED APPLICATION → ADDITIVE PROCESS SPECIFICATION → QUALIFIED PROCESS → CONTROLLED BUILD AND POST-PROCESSING → VERIFICATION AND ACCEPTANCE
```

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-DAM-001 | The additive manufacturing process shall be governed by a controlled process specification, limited to approved applications. | Manufacturing classification (HFPX-MFG-STR-001); Vol 03 material/process hooks (TBD); Vol 28 quality hooks (TBD) | Inspection |
| REQ-HFPX-DAM-002 | The additive manufacturing process specification shall define process controls, including feedstock control, build control, post-processing control, and traceability. | Vol 03 material/process hooks (TBD); Vol 28 quality hooks (TBD) | Inspection |
| REQ-HFPX-DAM-003 | The additive manufacturing process shall be qualified before use in production, using representative feedstock, geometry, and post-processing. | Vol 03 material/process hooks (TBD); Vol 28 quality hooks (TBD) | Demonstration |
| REQ-HFPX-DAM-004 | The additive manufacturing process specification shall define verification using Inspection, Demonstration, or Test as applicable. | Vol 03 material/process hooks (TBD); Vol 28 quality hooks (TBD) | Inspection |

## 7. Architecture

Additive scope is organised by application approval → feedstock control → build → post-processing → verification. Application approval authority and verification staging are TBD.

## 8. Detailed Design

To be elaborated (all TBD): specification contents, approved-applications register, feedstock control provisions, build and post-processing control approach, qualification practice and evidence, and requalification conditions. No build parameters or post-processing values are set in this document.

## 9. Interfaces

- MFG-ADM ↔ Vol 03 for material suitability and design-for-additive provisions (TBD)
- MFG-ADM ↔ HFPX-MFG-SPP-001 for special-process inventory and qualification (TBD)
- MFG-ADM ↔ Vol 28 for qualification, inspection and test, nonconformance, and records (TBD)
- MFG-ADM ↔ design volumes for approved-application definition (TBD)

## 10. Operational Concept

Additive work is introduced as: approve application → release process specification → qualify process → build and post-process under control → verify → record. Authority and sequencing are TBD.

## 11. Safety

This document creates no hazardous operations and provides no operating instructions. It requires that powder and feedstock safety, equipment safety, and post-processing safety provisions be defined in applicable process and safety documents. No energetics handling instructions are contained in this document.

## 12. Performance

Additive process measures such as conformity and stability are TBD. No thresholds are baselined at this revision.

## 13. Verification & Validation

Verification of the specification and approved-applications register is by Inspection. Qualification is by Demonstration and, where defined, Test. Product verification is by Inspection and Test as defined.

## 14. Risks

- Use outside approved applications → uncertified characteristics; mitigation: enforce approved-applications control (TBD)
- Uncontrolled feedstock or post-processing → variation; mitigation: define controls and qualification practice (TBD)
- Undetected build anomalies → acceptance risk; mitigation: define verification provisions (TBD)

## 15. Open Issues

- Approved-applications register (TBD)
- Applicable additive specifications register (TBD)
- Qualification practice, verification provisions, and requalification conditions (TBD)

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on HFPX-MFG-PRC-001, Vol 03 definitions (TBD), special-process provisions (TBD), and Vol 28 provisions (TBD). Enables production execution and acceptance for approved applications.

## 18. Traceability

Parent: manufacturing classification (HFPX-MFG-STR-001); Vol 03 material/process hooks (TBD); Vol 28 quality hooks (TBD). Children: qualified additive work instructions and acceptance evidence (TBD). RTM: REQ-HFPX-DAM-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 20.6) |
