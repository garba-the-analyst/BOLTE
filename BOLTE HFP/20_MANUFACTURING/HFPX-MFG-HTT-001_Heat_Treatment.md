# Heat Treatment

**Document ID:** HFPX-MFG-HTT-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the specification framework for heat treatment of HFP-X hardware: what shall be specified, controlled, qualified, and verified. Owns Chapter 20.10.

## 2. Scope

Covers heat treatment from condition verification through thermal processing and verification, as applicable to approved material and temper definitions. Does not set thermal cycles, atmospheres, or acceptance values, and does not provide operator instructions. Applicable specifications, process controls, and qualification arrangements are TBD.

## 3. Applicable Documents

- HFPX-MFG-PRC-001 Manufacturing Processes
- Vol 03 material and process definitions (documents TBD)
- HFPX-MFG-SPP-001 Special Processes (inventory and qualification, TBD)
- Vol 28 quality management provisions (documents TBD)
- Applicable heat treatment and test standards (TBD)

## 4. Definitions & Acronyms

- Heat treatment: controlled thermal processing to achieve a specified material condition (scope TBD)
- Thermal processing record: documented evidence linking hardware to its qualified cycle (contents TBD)
- TBD: to be defined; TBC: to be confirmed

## 5. System Context

Heat treatment converts verified input condition into specified material condition under qualified cycles and verification:

```text
MATERIAL DEFINITION → HEAT TREATMENT SPECIFICATION → QUALIFIED CYCLE → CONTROLLED EXECUTION → VERIFICATION AND ACCEPTANCE
```

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-DHT-001 | The heat treatment process shall be governed by a controlled process specification. | Manufacturing classification (HFPX-MFG-STR-001); Vol 03 material/process hooks (TBD); Vol 28 quality hooks (TBD) | Inspection |
| REQ-HFPX-DHT-002 | The heat treatment process specification shall define process controls, including input condition control, cycle control, equipment control, and traceability. | Vol 03 material/process hooks (TBD); Vol 28 quality hooks (TBD) | Inspection |
| REQ-HFPX-DHT-003 | The heat treatment process shall be qualified before use in production, using representative materials and configurations. | Vol 03 material/process hooks (TBD); Vol 28 quality hooks (TBD) | Demonstration |
| REQ-HFPX-DHT-004 | The heat treatment process specification shall define verification using Inspection, Demonstration, or Test as applicable. | Vol 03 material/process hooks (TBD); Vol 28 quality hooks (TBD) | Inspection |

## 7. Architecture

Heat treatment scope is organised by input verification → thermal processing → verification. Equipment qualification, load configuration control, and verification staging are TBD.

## 8. Detailed Design

To be elaborated (all TBD): specification contents, input condition provisions, cycle definition and control approach, equipment control and uniformity provisions, qualification scope and evidence, and requalification conditions. No thermal values or acceptance values are set in this document.

## 9. Interfaces

- MFG-HTT ↔ Vol 03 for material conditions and compatibility (TBD)
- MFG-HTT ↔ HFPX-MFG-SPP-001 for special-process inventory and qualification (TBD)
- MFG-HTT ↔ Vol 28 for qualification, inspection and test, nonconformance, and records (TBD)
- MFG-HTT ↔ design volumes for condition allocation (TBD)

## 10. Operational Concept

Heat treatment is introduced as: confirm material definition → release treatment specification → qualify cycle and equipment → process under control → verify → record. Authority and sequencing are TBD.

## 11. Safety

This document creates no hazardous operations and provides no operating instructions. It requires that thermal equipment safety and handling provisions be defined in applicable process and safety documents. No energetics handling instructions are contained in this document.

## 12. Performance

Heat treatment process measures such as conformity and stability are TBD. No thresholds are baselined at this revision.

## 13. Verification & Validation

Verification of the specification is by Inspection. Qualification is by Demonstration and, where defined, Test. Product verification is by Inspection and Test as defined.

## 14. Risks

- Incorrect input condition → nonconforming outcome; mitigation: define input condition control (TBD)
- Unqualified cycle or equipment → variation; mitigation: enforce qualification before production (TBD)
- Loss of traceability → acceptance gaps; mitigation: define processing records (TBD)

## 15. Open Issues

- Applicable heat treatment specifications register (TBD)
- Equipment control and qualification provisions (TBD)
- Qualification scope, verification provisions, and requalification conditions (TBD)

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on HFPX-MFG-PRC-001, Vol 03 definitions (TBD), special-process provisions (TBD), and Vol 28 provisions (TBD). Enables production execution and acceptance.

## 18. Traceability

Parent: manufacturing classification (HFPX-MFG-STR-001); Vol 03 material/process hooks (TBD); Vol 28 quality hooks (TBD). Children: qualified heat treatment procedures and acceptance evidence (TBD). RTM: REQ-HFPX-DHT-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 20.10) |
