# Supplier Management

**Document ID:** HFPX-PGM-SUP-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define supplier management for HFP-X: supplier requirements, incoming inspection, supplier quality and non-conformance handling. Owns Chapter 00.13.

## 2. Scope

Covers supplied items, supplier-provided evidence and supplier interfaces to build, integration and verification. Detailed build and quality provisions are owned by manufacturing and quality volumes. Does not set technical values.

## 3. Applicable Documents

- HFPX-PGM-CHR-001 Programme Charter
- HFPX-PGM-SEM-001 SEMP
- HFPX-PGM-IFM-001 Interface Management (supplier interface boundaries)
- HFPX-PGM-CHG-001 Change Management (supplier-change linkage)
- Manufacturing and quality provisions (incoming-inspection hooks Vol 28.3; supplier-quality hooks Vol 28.8)

## 4. Definitions & Acronyms

- Supplier: external provider of items, services or evidence
- Incoming inspection: examination of supplied items prior to acceptance
- Non-conformance: supplied item or evidence not meeting its requirements
- TBD / TBC: to be determined / to be confirmed

## 5. System Context

Supplier management links external supply to internal assurance:

```text
SUPPLIER REQUIREMENTS → SUPPLY → INCOMING INSPECTION → ACCEPTANCE
    → INTEGRATION → VERIFICATION
    ↑__ SUPPLIER QUALITY __↑__ NON-CONFORMANCE FLOW __↑
```

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-GSP-001 | The programme shall define supplier requirements, with scope and flow-down provisions recorded as TBD at this revision. | REQ-HFPX-PGM-001 | Inspection |
| REQ-HFPX-GSP-002 | The programme shall subject supplied items to incoming-inspection provisions linked to Vol 28.3, with acceptance criteria recorded as TBD at this revision. | REQ-HFPX-PGM-002 | Inspection |
| REQ-HFPX-GSP-003 | The programme shall apply supplier-quality provisions linked to Vol 28.8, with oversight and evidence provisions recorded as TBD at this revision. | REQ-HFPX-PGM-004 | Inspection |
| REQ-HFPX-GSP-004 | The programme shall control non-conforming supplied items through a defined non-conformance flow, with disposition provisions recorded as TBD at this revision. | REQ-HFPX-PGM-012 | Demonstration |

## 7. Architecture

Supplier management architecture TBD. Elements: supplier register, requirement flow-down, inspection points, quality oversight, non-conformance records. Roles and tooling TBD.

## 8. Detailed Design

Supplier requirement structure, incoming-inspection linkage, supplier-quality linkage and non-conformance procedure TBD. Supplied evidence shall be traceable to its requirements. No acceptance thresholds are stated at this revision.

## 9. Interfaces

- To interface management (00.11): supplier-owned interface boundaries
- To configuration (00.7): supplied-item baselines
- To change (00.10): supplier-change impact assessment
- To manufacturing and quality volumes: inspection and quality execution
- To V&V: supplied-item verification linkage

## 10. Operational Concept

Supplier requirements are flowed down, supply is inspected on receipt, quality is overseen, and non-conformances are dispositioned through the defined flow. Oversight cadence TBD.

## 11. Safety

Safety-critical supplied items shall receive proportionate oversight with safety authority visibility. Safety provisions TBD.

## 12. Performance

Supplier performance indicators TBD. No thresholds are baselined at this revision.

## 13. Verification & Validation

This document is verified by inspection against the document template checklist at the applicable gate. Validation is by programme authority approval (approver TBD).

## 14. Risks

- Supplier requirements incomplete, allowing unsuitable supply; mitigation TBD
- Inspection gaps accepting non-conforming items; mitigation TBD
- Non-conformance backlog affecting integration; mitigation TBD

## 15. Open Issues

_TBD_

All open issues are recorded in the issue register. No issue is closed by this revision.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on interface boundaries (00.11), manufacturing and quality provisions, configuration baselines (00.7) and V&V needs.

## 18. Traceability

Parent: HFPX-PGM-CHR-001 (REQ-HFPX-PGM-001/002/004) and HFPX-PGM-SEM-001 (REQ-HFPX-PGM-012). Children: supplier register, inspection records, non-conformance records (all TBD). RTM: REQ-HFPX-GSP-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 00.13) |
