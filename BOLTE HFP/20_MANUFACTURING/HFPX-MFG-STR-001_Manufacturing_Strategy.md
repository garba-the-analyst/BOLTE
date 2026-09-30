# Manufacturing Strategy

**Document ID:** HFPX-MFG-STR-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the manufacturing strategy for HFP-X: make-versus-procure principles, industrialisation approach, and governance that connects design definition to repeatable production under configuration and quality control. Owns Chapter 20.1.

## 2. Scope

Covers manufacturing classification, industrialisation sequencing, and alignment between engineering, manufacturing, supply chain, and quality. Does not define process parameters, tooling designs, or acceptance values. Applicable specifications, process controls, and qualification arrangements are TBD.

## 3. Applicable Documents

- HFPX-PGM-CHR-001 Programme Charter (authority, TBD)
- Vol 03 material and process definitions (documents TBD)
- Vol 28 quality management provisions (documents TBD)
- Vol 00 programme management provisions (documents TBD)
- Applicable manufacturing, materials, and quality standards (TBD)

## 4. Definitions & Acronyms

- MFG: Manufacturing
- Industrialisation: progression from development definition to stable production capability
- Special process: process whose outcome cannot be fully verified by subsequent inspection and therefore requires qualification and control (inventory TBD)
- TBD: to be defined; TBC: to be confirmed

## 5. System Context

Manufacturing strategy sits between design definition and production execution:

```text
DESIGN DEFINITION (Vol 03 and design volumes) → MANUFACTURING STRATEGY → PRODUCTION ARCHITECTURE → PROCESSES → QUALITY AND ACCEPTANCE (Vol 28)
```

This document governs intent and principles; downstream documents govern architecture, processes, suppliers, tooling, and acceptance.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-DMS-001 | The manufacturing strategy shall define the manufacturing classification for HFP-X hardware and its relationship to design authority and production authority. | Manufacturing classification (this document); Vol 28 quality hooks (TBD) | Inspection |
| REQ-HFPX-DMS-002 | The manufacturing strategy shall define make-versus-procure principles and the relationship between in-house production, supplier production, and special processes. | Manufacturing classification (this document); Vol 03 material/process hooks (TBD); Vol 28 quality hooks (TBD) | Inspection |
| REQ-HFPX-DMS-003 | The manufacturing strategy shall define the industrialisation approach from development definition through production readiness, including entry conditions for production. | Manufacturing classification (this document); Vol 28 quality hooks (TBD) | Inspection |
| REQ-HFPX-DMS-004 | The manufacturing strategy shall require that manufacturing processes be specified, controlled, and qualified before use in production. | Vol 03 material/process hooks (TBD); Vol 28 quality hooks (TBD) | Inspection |
| REQ-HFPX-DMS-005 | The manufacturing strategy shall require that production acceptance and associated records be defined and retained under configuration control. | Manufacturing classification (this document); Vol 28 quality hooks (TBD) | Inspection |

## 7. Architecture

Manufacturing governance (roles TBD) aligns design authority, production authority, supply chain, and quality. Production capability is organised by strategy → architecture → processes → tooling → acceptance, with change control at each transition (details TBD).

## 8. Detailed Design

Strategy elements to be elaborated (all TBD): classification scheme, industrialisation stages and gates, production readiness criteria, linkage to Vol 03 design definition and Vol 28 quality provisions, and treatment of special processes, tooling, and supplier work. No process parameters are set in this document.

## 9. Interfaces

- MFG-STR ↔ Vol 03 for material and process definition (TBD)
- MFG-STR ↔ Vol 28 for quality management and acceptance (TBD)
- MFG-STR ↔ Vol 00 for programme governance and configuration control (TBD)
- MFG-STR ↔ downstream MFG documents for architecture, processes, suppliers, tooling, and acceptance

## 10. Operational Concept

Strategy is applied as: classify hardware → assign production responsibility → specify and qualify processes → control tooling and suppliers → verify and accept product. Sequencing and readiness decisions are TBD.

## 11. Safety

This document creates no hazardous operations. It requires that manufacturing safety provisions, process hazards, and handling constraints be addressed in applicable process specifications and safety volumes before production. No energetics handling instructions are contained in this document.

## 12. Performance

Manufacturing performance indicators and readiness metrics are TBD. No thresholds are baselined at this revision.

## 13. Verification & Validation

Verification is by Inspection of strategy definition and traceability to parent hooks. Validation is by programme authority approval. Process-level verification is governed in downstream MFG documents by Inspection, Demonstration, or Test as applicable.

## 14. Risks

- Undefined classification → inconsistent allocation of production responsibility; mitigation: complete classification definition (TBD)
- Industrialisation without qualified processes → unstable production; mitigation: enforce process specification and qualification before production (TBD)
- Weak linkage to quality provisions → acceptance gaps; mitigation: align with Vol 28 provisions (TBD)

## 15. Open Issues

- Manufacturing classification criteria (TBD)
- Make-versus-procure decisions (TBD)
- Industrialisation gates and readiness criteria (TBD)
- Applicable specifications register (TBD)

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on programme authority (Vol 00, TBD), Vol 03 material and process definitions (TBD), and Vol 28 quality provisions (TBD). Enables downstream production architecture, processes, supplier, tooling, and acceptance documents.

## 18. Traceability

Parent: manufacturing classification (this document); Vol 03 material/process hooks (TBD); Vol 28 quality hooks (TBD). Children: HFPX-MFG-PAR-001, HFPX-MFG-PRC-001, and downstream MFG process, supplier, tooling, and acceptance documents. RTM: REQ-HFPX-DMS-001..005 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 20.1) |
