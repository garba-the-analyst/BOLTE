# Product Retirement

**Document ID:** HFPX-SUS-RET-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define how HFP-X products are retired and decommissioned at the close of the product lifecycle with controlled records. Owns Chapter 32.11.

## 2. Scope

Covers retirement planning, decommissioning governance and retirement records. Does not set technical values. Retirement process detail is TBD; decommissioning provisions are TBD; records provisions are TBD.

## 3. Applicable Documents

- HFPX-SUS-PLC-001 Product Lifecycle
- HFPX-SUS-EOL-001 End-of-Life Management
- HFPX-SUS-FLM-001 Fleet Management
- Vol 24 safety assurance concepts (details TBD)
- Vol 27 support concepts (details TBD)
- Vol 28 configuration and records concepts (details TBD)

## 4. Definitions & Acronyms

- Retirement: the controlled removal of a product from service at lifecycle close
- Decommissioning: activities rendering a retired product safe and non-operational
- TBD/TBC: unknown data markers; unknown values are never invented

## 5. System Context

Retirement closes the product lifecycle:

```text
END OF LIFE → RETIREMENT PLANNING → DECOMMISSIONING (TBD) → RECORDS ARCHIVE
     ↑________ CONFIGURATION CONTROL ________↑
     ↑________ SAFETY ASSURANCE (Vol 24) ____↑
```

Planning scope, decommissioning steps and records scope remain TBD at this revision.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-URT-001 | Product retirement shall follow a defined retirement process with recorded approval. | Lifecycle phase definition (TBD) | Inspection |
| REQ-HFPX-URT-002 | Decommissioning of retired products shall follow defined provisions addressing safety and controlled handling. | Vol 24 hooks (TBD) | Demonstration |
| REQ-HFPX-URT-003 | Retirement execution shall maintain traceability between retired instances, baselines and retirement records. | Vol 28 hooks (TBD) | Demonstration |
| REQ-HFPX-URT-004 | Retirement records shall be retained under configuration control with defined scope. | Vol 28 hooks (TBD) | Inspection |

## 7. Architecture

Retirement governance (roles TBD): retirement authority, safety liaison, fleet coordination and records authority with responsibilities TBD. Decommissioning facilities and arrangements TBD.

## 8. Detailed Design

Retirement plan contents, decommissioning steps, acceptance provisions and records scope to be defined (TBD). Retirement process, decommissioning approach and records provisions are TBD and not baselined at this revision.

## 9. Interfaces

- Retirement ↔ end of life (32.10) for declaration linkage
- Retirement ↔ fleet (32.3) for instance accountability
- Retirement ↔ safety (Vol 24) for decommissioning safety review
- Retirement ↔ support (Vol 27) and records (Vol 28) for closure and archive

## 10. Operational Concept

Retirement operates as a sequence: plan → approve → decommission → verify closure → archive records. Planning authority and closure forums TBD.

## 11. Safety

Retirement and decommissioning with safety relevance require safety assessment and closure concurrence (mechanisms TBD, Vol 24 hooks). No safety thresholds are set in this document.

## 12. Performance

Retirement indicators TBD (plan completeness criteria TBD, records completeness criteria TBD). No thresholds baselined.

## 13. Verification & Validation

This document is verified by inspection against the document template checklist (header, 20 sections, IDs, traceability). Requirements REQ-HFPX-URT-001..004 verified per §6. Validation: programme authority approval (TBD).

## 14. Risks

- Undefined retirement process → uncontrolled closure; mitigation: define process (TBD)
- Unsafe decommissioning → residual hazard; mitigation: safety-reviewed provisions (TBD)
- Incomplete retirement records → lost accountability; mitigation: records scope definition (TBD)

## 15. Open Issues

Retirement process steps, decommissioning provisions, closure criteria and records scope to be defined. All open details recorded as TBD.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on product lifecycle (32.1), end-of-life management (32.10), fleet management (32.3), Vol 24 safety assurance, Vol 27 support and Vol 28 records.

## 18. Traceability

Parent: lifecycle phase definition, Vol 24 / Vol 27 / Vol 28 hooks. Children: none at this revision; retirement records archive closes traceability. RTM: REQ-HFPX-URT-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 32.11) |
