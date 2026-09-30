# Production Tooling

**Document ID:** HFPX-MFG-TOL-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the specification framework for HFP-X production tooling: how tooling is specified, controlled, maintained, and verified. Owns Chapter 20.13.

## 2. Scope

Covers jigs, fixtures, moulds, dies, and measurement-supporting tooling used in production, as applicable. Tooling control provisions and calibration hooks are TBD. Does not define tooling designs or dimensional values. Applicable specifications, process controls, and qualification arrangements are TBD.

## 3. Applicable Documents

- HFPX-MFG-PRC-001 Manufacturing Processes
- HFPX-MFG-PAR-001 Production Architecture
- Vol 03 design definitions requiring tooling (documents TBD)
- Vol 28 quality and calibration provisions (documents TBD)
- Applicable tooling and measurement standards (TBD)

## 4. Definitions & Acronyms

- Production tooling: controlled means used to locate, form, hold, or verify product during production (scope TBD)
- Tooling control: identification, configuration, maintenance, and release of tooling (provisions TBD)
- Calibration hooks: linkage to measurement control for tooling used in verification (provisions TBD)
- TBD: to be defined; TBC: to be confirmed

## 5. System Context

Tooling control assures repeatability across production:

```text
DESIGN DEFINITION → TOOLING DEFINITION → CONTROLLED TOOLING → QUALIFIED PROCESSES → VERIFIED PRODUCT
```

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-DPT-001 | Production tooling shall be defined and controlled under configuration control. | Manufacturing classification (HFPX-MFG-STR-001); Vol 03 material/process hooks (TBD); Vol 28 quality hooks (TBD) | Inspection |
| REQ-HFPX-DPT-002 | The production tooling provisions shall define tooling controls, including identification, maintenance, storage, handling, and release. | Vol 03 material/process hooks (TBD); Vol 28 quality hooks (TBD) | Inspection |
| REQ-HFPX-DPT-003 | Production tooling used in verification shall be linked to calibration provisions. | Vol 03 material/process hooks (TBD); Vol 28 quality hooks (TBD) | Inspection |
| REQ-HFPX-DPT-004 | Production tooling shall be verified before release for production using Inspection, Demonstration, or Test as applicable. | Vol 03 material/process hooks (TBD); Vol 28 quality hooks (TBD) | Demonstration |

## 7. Architecture

Tooling scope is organised by definition → manufacture or procurement → verification → release → maintenance → re-verification. Ownership, maintenance authority, and re-verification conditions are TBD.

## 8. Detailed Design

To be elaborated (all TBD): tooling register, definition contents, control provisions, maintenance approach, calibration hooks, and verification and re-verification scope. No tooling designs or values are set in this document.

## 9. Interfaces

- MFG-TOL ↔ Vol 03 for tooling-related design definitions (TBD)
- MFG-TOL ↔ process-family documents for tooling use context
- MFG-TOL ↔ Vol 28 for configuration, calibration, nonconformance, and records (TBD)
- MFG-TOL ↔ HFPX-MFG-SUP-001 for supplier-provided tooling (TBD)

## 10. Operational Concept

Tooling is introduced as: define → obtain → verify → release → maintain → re-verify when required. Authority and sequencing are TBD.

## 11. Safety

This document creates no hazardous operations and provides no operating instructions. It requires that tooling safety and handling provisions be defined in applicable process and safety documents. No energetics handling instructions are contained in this document.

## 12. Performance

Tooling measures such as availability and conformity are TBD. No thresholds are baselined at this revision.

## 13. Verification & Validation

Verification of tooling definition and control is by Inspection. Tooling release and re-verification are by Inspection, Demonstration, or Test as applicable.

## 14. Risks

- Uncontrolled tooling → nonconforming product; mitigation: enforce tooling control and configuration (TBD)
- Degraded tooling in use → drift; mitigation: define maintenance and re-verification (TBD)
- Uncalibrated verification tooling → false acceptance; mitigation: link to calibration provisions (TBD)

## 15. Open Issues

- Tooling register and control provisions (TBD)
- Calibration hooks and measurement linkage (TBD)
- Verification and re-verification scope (TBD)

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on HFPX-MFG-PRC-001, HFPX-MFG-PAR-001, Vol 03 definitions (TBD), and Vol 28 provisions (TBD). Enables controlled production and acceptance.

## 18. Traceability

Parent: manufacturing classification (HFPX-MFG-STR-001); Vol 03 material/process hooks (TBD); Vol 28 quality hooks (TBD). Children: released tooling and acceptance evidence (TBD). RTM: REQ-HFPX-DPT-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 20.13) |
