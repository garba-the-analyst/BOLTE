# Production Architecture

**Document ID:** HFPX-MFG-PAR-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the production architecture for HFP-X: how production capability is structured, segmented, and governed from incoming material through fabrication, integration, and acceptance. Owns Chapter 20.2.

## 2. Scope

Covers production segmentation, facility and line organisation principles, and flow from material receipt through acceptance. Does not define process parameters, facility selections, or capacity values. Applicable specifications, process controls, and qualification arrangements are TBD.

## 3. Applicable Documents

- HFPX-MFG-STR-001 Manufacturing Strategy
- Vol 03 material and process definitions (documents TBD)
- Vol 28 quality management provisions (documents TBD)
- Applicable manufacturing and quality standards (TBD)

## 4. Definitions & Acronyms

- Production architecture: structure of production stages, responsibilities, and flows
- Work centre: logical production grouping for a defined scope of work (definitions TBD)
- TBD: to be defined; TBC: to be confirmed

## 5. System Context

Production architecture translates strategy into executable structure:

```text
MANUFACTURING STRATEGY → PRODUCTION ARCHITECTURE → PROCESSES AND WORK INSTRUCTIONS → TOOLING AND SUPPLIERS → ACCEPTANCE
```

Architecture defines where and under what controls work is performed; process documents define how each process is specified and qualified.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-DPA-001 | The production architecture shall define production stages and their sequence from incoming material through fabrication, integration, and acceptance. | Manufacturing classification (HFPX-MFG-STR-001); Vol 28 quality hooks (TBD) | Inspection |
| REQ-HFPX-DPA-002 | The production architecture shall define responsibility allocation across in-house work centres and supplier work, including handover boundaries. | Manufacturing classification (HFPX-MFG-STR-001); Vol 28 quality hooks (TBD) | Inspection |
| REQ-HFPX-DPA-003 | The production architecture shall require that each production stage operate under specified processes, controlled tooling, and configuration control. | Vol 03 material/process hooks (TBD); Vol 28 quality hooks (TBD) | Inspection |
| REQ-HFPX-DPA-004 | The production architecture shall define the relationship between production flow, verification points, and acceptance. | Manufacturing classification (HFPX-MFG-STR-001); Vol 28 quality hooks (TBD) | Inspection |

## 7. Architecture

Production is segmented into incoming control, fabrication, joining and treatment, integration, verification, and acceptance. Stage boundaries, handover artefacts, and control responsibilities are TBD.

## 8. Detailed Design

To be elaborated (all TBD): stage definitions, flow diagrams, work centre organisation, handover documentation, configuration control points, and linkage to process specifications and acceptance provisions. No facility, rate, or capacity values are set in this document.

## 9. Interfaces

- MFG-PAR ↔ HFPX-MFG-STR-001 for classification and industrialisation principles
- MFG-PAR ↔ Vol 03 for material and process definition (TBD)
- MFG-PAR ↔ Vol 28 for quality and acceptance provisions (TBD)
- MFG-PAR ↔ downstream process, tooling, supplier, and acceptance documents

## 10. Operational Concept

Production operates as: receive and control material → fabricate → join and treat → integrate → verify → accept. Stage entry and exit conditions are TBD.

## 11. Safety

This document creates no hazardous operations. It requires that stage-level safety provisions and handling constraints be defined in applicable process and safety documents before production. No energetics handling instructions are contained in this document.

## 12. Performance

Production flow performance measures are TBD. No thresholds are baselined at this revision.

## 13. Verification & Validation

Verification is by Inspection of architecture definition and traceability. Stage and process verification is governed in downstream documents by Inspection, Demonstration, or Test as applicable.

## 14. Risks

- Undefined stage boundaries → handover gaps; mitigation: complete stage and artefact definitions (TBD)
- Uncontrolled allocation between in-house and supplier work → responsibility ambiguity; mitigation: define allocation and boundaries (TBD)
- Architecture without verification points → late defect discovery; mitigation: align flow with verification and acceptance (TBD)

## 15. Open Issues

- Production stage definitions and flow (TBD)
- Work centre organisation (TBD)
- Handover artefacts and configuration points (TBD)

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on HFPX-MFG-STR-001, Vol 03 definitions (TBD), and Vol 28 provisions (TBD). Enables process, supplier, tooling, and acceptance documents.

## 18. Traceability

Parent: manufacturing classification (HFPX-MFG-STR-001); Vol 03 material/process hooks (TBD); Vol 28 quality hooks (TBD). Children: HFPX-MFG-PRC-001 and downstream process and acceptance documents. RTM: REQ-HFPX-DPA-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 20.2) |
