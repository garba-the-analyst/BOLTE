# 03.4 Secondary Structure

**Document ID:** HFPX-STR-SEC-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the secondary-structure scope for HFP-X: which items are secondary, the failure-consequence rule that keeps them secondary, inspection provisions, and verification. This revision establishes structure and traceability only; no sizing or values are stated.

## 2. Scope

Covers Chapter 03.4 Secondary Structure. Secondary structure comprises non-primary items such as fairings, covers, and enclosures (item list TBD). Primary structure is owned by Chapter 03.3; philosophy by Chapter 03.2.

## 3. Applicable Documents

- HFPX-SYS-ARC-001 SAD, physical view (parent architecture)
- HFPX-SYS-REQ-001 SyRS (SYS tier parent requirements, via SAD)
- HFPX-STR-ARC-001 Airframe Architecture (Chapter 03.1)
- HFPX-STR-PHI-001 Structural Design Philosophy (Chapter 03.2)
- Volume 06 loads inputs (TBD)

## 4. Definitions & Acronyms

- Secondary structure: structural items outside primary load paths
- Failure-consequence rule: criterion confirming an item may remain secondary (rule TBD)
- Inspection hook: a provision enabling future inspection access or method (detail TBD)
- TBD: to be determined; TBC: to be confirmed

## 5. System Context

Secondary structure encloses, protects, or streamlines primary structure and systems without carrying primary load paths. It receives architectural boundaries from Chapter 03.1 and classification rules from Chapter 03.2, with load inputs from Volume 06 (TBD).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-SSS-001|The secondary structural items shall be identified and recorded.|SYS tier via SAD physical view|Inspection|
|REQ-HFPX-SSS-002|A failure-consequence rule confirming secondary classification shall be defined and applied to each secondary item.|SYS tier via SAD physical view|Inspection|
|REQ-HFPX-SSS-003|Inspection provisions for secondary structure shall be identified and recorded.|SYS tier via SAD physical view|Inspection|
|REQ-HFPX-SSS-004|Verification of secondary structure shall be defined, linking analysis and inspection methodology.|SYS tier via SAD physical view|Inspection|

## 7. Architecture

Secondary-structure breakdown (TBD): item identification, failure-consequence classification per the Chapter 03.2 philosophy, attachment to primary structure, and inspection provisions (TBD). Items remain secondary only while satisfying the failure-consequence rule.

## 8. Detailed Design

Not applicable at this revision. No geometry, panel sizes, thicknesses, or attachment details are stated. Item definitions and drawings are TBD.

## 9. Interfaces

Secondary-structure interfaces are TBD: attachment interfaces to primary structure (Chapter 03.3); loads inputs via Chapter 03.13 and Volume 06 (TBD); access interfaces for inspection and maintenance (Volumes 21 and 23, TBD). Interface methodology: record each interface and owner by review.

## 10. Operational Concept

Secondary structure supports ground handling, flight, and maintenance phases (TBD). Methodology: confirm by review that removal, access, and retention provisions cover the operational phases. No phase values are stated.

## 11. Safety

Safety methodology: apply the failure-consequence rule to confirm that secondary-item failure does not impair primary capability or create a hazard inconsistent with Volume 13 analyses (TBD). No safety values are stated.

## 12. Performance

Performance methodology only: describe retention, stiffness, and durability behaviours to be demonstrated by analysis and inspection methodology. No performance values are stated.

## 13. Verification & Validation

Verification by review at this revision: check item identification, failure-consequence rule application, inspection provisions, and verification definition against Section 6. Later verification methodology: analysis review, inspection, and retention demonstration by test methodology (Chapter 03.20). No pass/fail values are stated.

## 14. Risks

- Secondary items migrating to primary roles without reclassification; mitigation: failure-consequence rule applied per REQ-HFPX-SSS-002
- Inaccessible items preventing inspection; mitigation: inspection provisions recorded per REQ-HFPX-SSS-003

## 15. Open Issues

- Secondary item identification (TBD)
- Failure-consequence rule definition (TBD)
- Inspection provisions (TBD)
- Verification definition detail (TBD)

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SYS-tier requirements via the SAD physical view, Chapters 03.1 and 03.2, Chapter 03.13 load treatment, and Volume 06 loads inputs (TBD).

## 18. Traceability

Parent: SYS tier via SAD physical view. Children: secondary-item analysis and inspection artefacts. RTM: REQ-HFPX-SSS-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 03.4) |
