# End-of-Life Management

**Document ID:** HFPX-SUS-EOL-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define how HFP-X end-of-life is declared, planned and executed for products and components leaving active sustainment. Owns Chapter 32.10.

## 2. Scope

Covers end-of-life criteria, end-of-life planning, disposal linkage and records provisions. Does not set technical values. End-of-life criteria are TBD; disposal provisions are TBD; records provisions are TBD.

## 3. Applicable Documents

- HFPX-SUS-PLC-001 Product Lifecycle
- HFPX-SUS-CBL-001 Configuration Baselines
- HFPX-SUS-FLM-001 Fleet Management
- Vol 24 safety assurance concepts (details TBD)
- Vol 27 support concepts (details TBD)
- Vol 28 configuration and records concepts (details TBD)

## 4. Definitions & Acronyms

- End of life: the declared state in which a product or component leaves active sustainment while remaining subject to records and obligations
- Disposal: controlled handling of retired items under applicable provisions
- TBD/TBC: unknown data markers; unknown values are never invented

## 5. System Context

End of life transitions items out of active sustainment:

```text
ACTIVE SUSTAINMENT → EOL DECLARATION → EOL EXECUTION → DISPOSAL (TBD) → ARCHIVED RECORDS
         ↑________ CONFIGURATION CONTROL ________↑
         ↑________ SAFETY ASSURANCE (Vol 24) ____↑
```

Criteria, execution steps and disposal provisions remain TBD at this revision.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-UEL-001 | End-of-life declaration shall follow defined criteria with recorded rationale and approval. | Lifecycle phase definition (TBD) | Inspection |
| REQ-HFPX-UEL-002 | End-of-life execution shall follow a defined plan covering support withdrawal and stakeholder notification. | Vol 27 hooks (TBD) | Inspection |
| REQ-HFPX-UEL-003 | Disposal of end-of-life items shall follow defined provisions with recorded traceability. | Vol 27 / Vol 28 hooks (TBD) | Demonstration |
| REQ-HFPX-UEL-004 | End-of-life records shall be retained under configuration control with defined scope. | Vol 28 hooks (TBD) | Inspection |

## 7. Architecture

End-of-life governance (roles TBD): sustainment authority, design authority, safety liaison and records authority with responsibilities TBD. Disposal facilities and arrangements TBD.

## 8. Detailed Design

Declaration criteria, plan contents, disposal provisions and records scope to be defined (TBD). End-of-life criteria, disposal approach and records provisions are TBD and not baselined at this revision.

## 9. Interfaces

- EOL ↔ lifecycle (32.1) for phase transition alignment
- EOL ↔ fleet (32.3) for affected instance identification
- EOL ↔ safety (Vol 24) for safety-relevant declaration review
- EOL ↔ support (Vol 27) and records (Vol 28) for withdrawal and retention

## 10. Operational Concept

End of life operates as a sequence: declare → plan → execute → dispose → archive records. Declaration authority and execution forums TBD.

## 11. Safety

End-of-life declarations with safety relevance require safety assessment addressing residual obligations (mechanisms TBD, Vol 24 hooks). No safety thresholds are set in this document.

## 12. Performance

End-of-life indicators TBD (plan completeness criteria TBD, records completeness criteria TBD). No thresholds baselined.

## 13. Verification & Validation

This document is verified by inspection against the document template checklist (header, 20 sections, IDs, traceability). Requirements REQ-HFPX-UEL-001..004 verified per §6. Validation: programme authority approval (TBD).

## 14. Risks

- Undefined criteria → premature or delayed declaration; mitigation: define criteria (TBD)
- Unplanned withdrawal → unsupported users; mitigation: execution planning and notification (TBD)
- Incomplete records → lost lifecycle truth; mitigation: records scope definition (TBD)

## 15. Open Issues

Declaration criteria, execution planning, disposal provisions and records scope to be defined. All open details recorded as TBD.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on product lifecycle (32.1), configuration baselines (32.2), fleet management (32.3), Vol 24 safety assurance, Vol 27 support and Vol 28 records.

## 18. Traceability

Parent: lifecycle phase definition, Vol 24 / Vol 27 / Vol 28 hooks. Children: retirement execution fed by end-of-life declarations (32.11). RTM: REQ-HFPX-UEL-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 32.10) |
