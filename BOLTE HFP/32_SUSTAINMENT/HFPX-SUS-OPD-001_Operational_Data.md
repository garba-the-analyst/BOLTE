# Operational Data

**Document ID:** HFPX-SUS-OPD-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define how HFP-X operational data is collected, managed and exploited to support sustainment decisions. Owns Chapter 32.4.

## 2. Scope

Covers operational data collection, data management, data quality and sustainment exploitation. Does not set technical values, sampling schemes or analytical thresholds. Data collection means are TBD; hooks to Vol 23.17 and 33.16 apply.

## 3. Applicable Documents

- HFPX-SUS-PLC-001 Product Lifecycle
- Vol 23 data and instrumentation concepts (23.17 hooks, details TBD)
- MVP and prototyping data concepts (33.16 hooks, details TBD)
- Vol 24 safety assurance concepts (details TBD)
- Vol 28 configuration and records concepts (details TBD)

## 4. Definitions & Acronyms

- Operational data: data generated during operation and maintenance of the fielded product
- Data exploitation: analysis and use of operational data to inform sustainment decisions
- TBD/TBC: unknown data markers; unknown values are never invented

## 5. System Context

Operational data feeds sustainment understanding:

```text
FIELDED PRODUCT → DATA COLLECTION (TBD) → DATA MANAGEMENT → SUSTAINMENT DECISIONS
       ↑________ Vol 23.17 INSTRUMENTATION HOOKS ________↑
       ↑________ 33.16 PROTOTYPE DATA HOOKS _____________↑
```

Collection scope, means and retention remain TBD at this revision.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-UOD-001 | Operational data relevant to sustainment shall be collected under a defined collection scope. | Lifecycle phase definition (TBD) | Demonstration |
| REQ-HFPX-UOD-002 | Operational data shall be managed with defined quality, integrity and traceability controls. | Vol 23.17 hooks (TBD) | Inspection |
| REQ-HFPX-UOD-003 | Operational data exploitation shall inform fleet, reliability and improvement decisions with recorded linkage. | Vol 27 / Vol 28 hooks (TBD) | Analysis |
| REQ-HFPX-UOD-004 | Operational data with safety relevance shall be made available to safety assurance under defined controls. | Vol 24 hooks, 33.16 hooks (TBD) | Demonstration |

## 7. Architecture

Data management architecture (roles, repositories and tooling TBD): collection sources, storage, access control and analysis functions with interfaces to Vol 23.17 concepts and prototype data environments (33.16 hooks).

## 8. Detailed Design

Data taxonomy, collection scope, quality rules, retention provisions and exploitation workflows to be defined (TBD). Data collection approach is TBD and not baselined at this revision.

## 9. Interfaces

- Data ↔ instrumentation and acquisition (Vol 23.17) for source alignment
- Data ↔ prototype environments (33.16) for early-learning linkage
- Data ↔ fleet management (32.3) and reliability growth (32.5) for consumers
- Data ↔ safety (Vol 24) and records (Vol 28) for assurance and retention

## 10. Operational Concept

Data operates as a sustainment loop: define scope → collect → assure quality → analyse → decide → record. Collection events and analysis forums TBD.

## 11. Safety

Safety-relevant operational data handling requires integrity and access provisions TBD (Vol 24 hooks). No safety thresholds are set in this document.

## 12. Performance

Data management indicators TBD (completeness criteria TBD, integrity criteria TBD). No thresholds baselined.

## 13. Verification & Validation

This document is verified by inspection against the document template checklist (header, 20 sections, IDs, traceability). Requirements REQ-HFPX-UOD-001..004 verified per §6. Validation: programme authority approval (TBD).

## 14. Risks

- Undefined collection scope → missing sustainment evidence; mitigation: scope definition (TBD)
- Poor data quality → flawed decisions; mitigation: quality and integrity controls (TBD)
- Uncontrolled dissemination → mishandled sensitive data; mitigation: access provisions (TBD)

## 15. Open Issues

Collection scope and means, taxonomy, quality rules, retention and Vol 23.17/33.16 interface details to be defined. All open details recorded as TBD.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on Vol 23.17 instrumentation concepts, 33.16 prototype data concepts, product lifecycle (32.1), Vol 24 safety assurance and Vol 28 records.

## 18. Traceability

Parent: lifecycle phase definition, Vol 23.17 / 33.16 / Vol 24 / Vol 28 hooks. Children: fleet, reliability growth and improvement consumers (32.3, 32.5, 32.6). RTM: REQ-HFPX-UOD-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 32.4) |
