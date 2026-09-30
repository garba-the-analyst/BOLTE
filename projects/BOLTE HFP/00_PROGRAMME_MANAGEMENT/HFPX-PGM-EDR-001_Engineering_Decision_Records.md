# Engineering Decision Records

**Document ID:** HFPX-PGM-EDR-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define engineering decision records for HFP-X: record content, immutability, traceability linkage and revisit-condition tracking. Owns Chapter 00.16.

## 2. Scope

Covers significant architectural and programme decisions recorded as DDRs, including their linkage to requirements and their evolution over time. Does not set technical values.

## 3. Applicable Documents

- HFPX-PGM-CHR-001 Programme Charter
- HFPX-PGM-SEM-001 SEMP
- HFPX-PGM-GOV-001 Project Governance (decision authority)
- HFPX-PGM-CFG-001 Configuration Management (record control)
- DDR-002 and DDR-003 (structure and identifier decisions)

## 4. Definitions & Acronyms

- DDR: Design Decision Record; significant decision recorded under control
- Revisit condition: stated condition under which a recorded decision is reconsidered
- RTM: Requirements Traceability Matrix
- TBD / TBC: to be determined / to be confirmed

## 5. System Context

Decision records preserve programme rationale:

```text
PROPOSAL → ASSESSMENT → DECISION (DDR) → TRACEABILITY → REVISIT (new DDR)
   ↑________________ NEVER REWRITE ________________↑
```

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-GED-001 | The programme shall record each significant decision as a DDR addressing the prompt §21 fields, with field definitions recorded as TBD at this revision. | REQ-HFPX-PGM-014 | Inspection |
| REQ-HFPX-GED-002 | The programme shall never rewrite a recorded DDR; a contradictory or superseding decision shall be recorded as a new DDR referencing its predecessor. | REQ-HFPX-PGM-014 | Inspection |
| REQ-HFPX-GED-003 | The programme shall link each DDR to affected requirements in the RTM. | REQ-HFPX-PGM-002 | Inspection |
| REQ-HFPX-GED-004 | The programme shall track revisit conditions for each DDR and assess them at applicable gates. | REQ-HFPX-PGM-014 | Inspection |

## 7. Architecture

Decision-record architecture TBD. Elements: DDR register, record store, RTM linkage, revisit-condition tracking. Custodianship and tooling TBD.

## 8. Detailed Design

DDR field structure covering prompt §21 fields, immutability enforcement, RTM-linking method and revisit-condition tracking TBD, consistent with DDR-002 and DDR-003. No decision content values are stated at this revision.

## 9. Interfaces

- To governance (00.2): authority for decisions recorded as DDRs
- To requirements (00.9): DDR-to-RTM linkage
- To configuration and change (00.7/00.10): DDR handling under control and change
- To decision log: living index of DDR state

## 10. Operational Concept

Decisions are proposed, assessed, recorded as DDRs, linked to requirements, and revisited only through new DDRs when revisit conditions are met. Recording workflow and review cadence TBD.

## 11. Safety

Safety-significant decisions shall be recorded with safety authority visibility. Safety decision provisions TBD.

## 12. Performance

Decision-record performance indicators TBD. No thresholds are baselined at this revision.

## 13. Verification & Validation

This document is verified by inspection against the document template checklist at the applicable gate. Validation is by programme authority approval (approver TBD).

## 14. Risks

- Significant decisions left unrecorded, losing rationale; mitigation TBD
- Records edited after the fact, obscuring history; mitigation TBD
- Revisit conditions untracked, leaving stale decisions in force; mitigation TBD

## 15. Open Issues

_TBD_

All open issues are recorded in the issue register. No issue is closed by this revision.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SEMP DDR rule, governance decision authority, RTM discipline (00.9) and decision-log upkeep.

## 18. Traceability

Parent: HFPX-PGM-SEM-001 (REQ-HFPX-PGM-014/002), DDR-002 and DDR-003. Children: DDR register, DDR-to-RTM links, revisit-condition assessments (all TBD). RTM: REQ-HFPX-GED-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 00.16) |
