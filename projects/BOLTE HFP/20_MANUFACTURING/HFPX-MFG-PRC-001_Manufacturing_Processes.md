# Manufacturing Processes

**Document ID:** HFPX-MFG-PRC-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the governing framework for HFP-X manufacturing processes: how processes are specified, controlled, qualified, and verified. Owns Chapter 20.3 and parents the process-specific documents in this volume.

## 2. Scope

Covers process specification structure, process controls, qualification, and verification principles across all manufacturing processes. Does not set process parameters or instruct operators in process execution. Applicable specifications, process controls, and qualification arrangements are TBD.

## 3. Applicable Documents

- HFPX-MFG-STR-001 Manufacturing Strategy
- HFPX-MFG-PAR-001 Production Architecture
- Vol 03 material and process definitions (documents TBD)
- Vol 28 quality management provisions (documents TBD)
- Applicable manufacturing and quality standards (TBD)

## 4. Definitions & Acronyms

- Process specification: controlled document defining process requirements, controls, and qualification
- Process control: documented means to ensure repeatability and conformity (details TBD)
- Qualification: demonstration that a process can repeatedly produce conforming product (arrangements TBD)
- TBD: to be defined; TBC: to be confirmed

## 5. System Context

Process framework connects design definition to conforming product:

```text
DESIGN DEFINITION → PROCESS SPECIFICATION → QUALIFIED PROCESS → CONTROLLED PRODUCTION → VERIFICATION AND ACCEPTANCE
```

This document governs the framework; process-specific documents govern CNC, composite, additive, machining, welding and joining, surface treatment, heat treatment, and special processes.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-DPR-001 | The manufacturing process framework shall require that each production process be governed by a controlled process specification. | Manufacturing classification (HFPX-MFG-STR-001); Vol 03 material/process hooks (TBD); Vol 28 quality hooks (TBD) | Inspection |
| REQ-HFPX-DPR-002 | The manufacturing process framework shall require that process controls be defined for each specified process. | Vol 03 material/process hooks (TBD); Vol 28 quality hooks (TBD) | Inspection |
| REQ-HFPX-DPR-003 | The manufacturing process framework shall require that each production process be qualified before use in production. | Vol 03 material/process hooks (TBD); Vol 28 quality hooks (TBD) | Demonstration |
| REQ-HFPX-DPR-004 | The manufacturing process framework shall require that process verification methods be defined using Inspection, Demonstration, or Test as applicable. | Vol 03 material/process hooks (TBD); Vol 28 quality hooks (TBD) | Inspection |

## 7. Architecture

Process governance is organised by framework (this document) → process-family specifications (CNC, composite, additive, machining, joining, surface, heat, special) → qualified work instructions. Specification hierarchy and approval authorities are TBD.

## 8. Detailed Design

To be elaborated (all TBD): specification template and contents, control elements, qualification scope and evidence, requalification conditions, and linkage to Vol 03 materials and Vol 28 quality provisions. No process parameters are set in this document.

## 9. Interfaces

- MFG-PRC ↔ Vol 03 for material behaviour and process compatibility (TBD)
- MFG-PRC ↔ Vol 28 for process qualification, nonconformance, and records (TBD)
- MFG-PRC ↔ process-family documents for family-specific specification and control
- MFG-PRC ↔ tooling and supplier documents for process execution context

## 10. Operational Concept

Processes are introduced as: specify → control → qualify → release for production → monitor → requalify when required. Release authority and monitoring provisions are TBD.

## 11. Safety

This document creates no hazardous operations. It requires that process-specific safety provisions be defined in applicable process specifications and safety volumes. No energetics handling instructions are contained in this document.

## 12. Performance

Process capability and stability measures are TBD. No thresholds are baselined at this revision.

## 13. Verification & Validation

Verification is by Inspection of framework definition and by Inspection, Demonstration, or Test of process qualification as defined in process-family documents. Validation is by programme authority approval.

## 14. Risks

- Unspecified processes used in production → uncontrolled variation; mitigation: require controlled specifications before production (TBD)
- Qualification gaps → nonconforming product; mitigation: enforce qualification and requalification provisions (TBD)
- Weak records → loss of traceability; mitigation: align with Vol 28 records provisions (TBD)

## 15. Open Issues

- Process specification register and hierarchy (TBD)
- Qualification and requalification provisions (TBD)
- Process monitoring provisions (TBD)

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on HFPX-MFG-STR-001, HFPX-MFG-PAR-001, Vol 03 definitions (TBD), and Vol 28 provisions (TBD). Enables process-family, special-process, supplier, tooling, and acceptance documents.

## 18. Traceability

Parent: manufacturing classification (HFPX-MFG-STR-001); Vol 03 material/process hooks (TBD); Vol 28 quality hooks (TBD). Children: process-family documents in this volume and HFPX-MFG-SPP-001. RTM: REQ-HFPX-DPR-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 20.3) |
