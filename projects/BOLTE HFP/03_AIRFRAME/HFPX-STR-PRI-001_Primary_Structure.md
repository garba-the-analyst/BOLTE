# 03.3 Primary Structure

**Document ID:** HFPX-STR-PRI-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the primary-structure scope for HFP-X: which items are primary, which load cases govern them, who owns their analysis, and how they are verified. This revision establishes structure and traceability only; no sizing or values are stated.

## 2. Scope

Covers Chapter 03.3 Primary Structure. Primary structure comprises load-path-critical items whose failure would impair structural capability (item list TBD). Philosophy is governed by Chapter 03.2; load cases by Chapter 03.13; substantiation by Chapters 03.14–03.20.

## 3. Applicable Documents

- HFPX-SYS-ARC-001 SAD, physical view (parent architecture)
- HFPX-SYS-REQ-001 SyRS (SYS tier parent requirements, via SAD)
- HFPX-STR-ARC-001 Airframe Architecture (Chapter 03.1)
- HFPX-STR-PHI-001 Structural Design Philosophy (Chapter 03.2)
- Volume 06 loads inputs (TBD)

## 4. Definitions & Acronyms

- Primary structure: structural items essential to carrying primary load paths
- Load case: a defined combination of loads and conditions for analysis (cases TBD)
- FEA: finite element analysis (ownership TBD)
- TBD: to be determined; TBC: to be confirmed

## 5. System Context

Primary structure reacts flight, ground, propulsion, and pilot-induced loads and passes them through owned load paths defined in Chapter 03.1. Inputs: SYS-tier requirements via the SAD physical view; philosophy from Chapter 03.2; load cases from Chapter 03.13 and Volume 06 (TBD).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-SPS-001|The primary structural items shall be identified and recorded.|SYS tier via SAD physical view|Inspection|
|REQ-HFPX-SPS-002|The load cases governing primary structure shall be identified, consistent with Chapter 03.13.|SYS tier via SAD physical view; Vol 06 loads inputs TBD|Inspection|
|REQ-HFPX-SPS-003|Analysis ownership for primary structure, including FEA ownership, shall be defined and recorded.|SYS tier via SAD physical view|Inspection|
|REQ-HFPX-SPS-004|Verification of primary structure shall be defined, linking analysis and test methodology.|SYS tier via SAD physical view|Inspection|

## 7. Architecture

Primary-structure breakdown (TBD): item identification, assignment to load paths from Chapter 03.1, governing load cases (TBD per Chapter 03.13), and analysis ownership including FEA (TBD). Categorisation follows the philosophy in Chapter 03.2.

## 8. Detailed Design

Not applicable at this revision. No geometry, member sizes, section properties, or joint details are stated. Item definitions and drawings are TBD.

## 9. Interfaces

Primary-structure interfaces are TBD: to Chapter 03.13 load cases; to Chapters 03.9 and 03.10 for joints and materials; to Chapters 03.6 and 03.7 for mounted and lifting-surface loads; to Volume 06 loads inputs (TBD). Interface methodology: record each interface and owner by review.

## 10. Operational Concept

Primary structure supports all flight and ground phases (TBD). Methodology: map governing load cases to phases and confirm coverage by review. No phase values are stated.

## 11. Safety

Safety methodology: classify primary items per the Chapter 03.2 philosophy; require failure-consequence treatment consistent with Volume 13 safety analyses (TBD). No safety values are stated.

## 12. Performance

Performance methodology only: describe strength, stiffness, stability, and durability behaviours to be demonstrated by analysis and test methodology (Chapters 03.14–03.20). No performance values are stated.

## 13. Verification & Validation

Verification by review at this revision: check item identification, load-case linkage, analysis ownership, and verification definition against Section 6. Later verification methodology: analysis review (including FEA methodology review), inspection, and test witnessing per Chapters 03.13–03.20. No pass/fail values are stated.

## 14. Risks

- Primary items unidentified while loads mature; mitigation: CONCEPT status explicit, item list tracked as TBD
- Analysis ownership unclear; mitigation: ownership recorded per REQ-HFPX-SPS-003

## 15. Open Issues

- Primary item identification (TBD)
- Governing load cases per Chapter 03.13 (TBD)
- FEA and analysis ownership (TBD)
- Verification definition detail (TBD)

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SYS-tier requirements via the SAD physical view, Chapters 03.1 and 03.2, Chapter 03.13 load cases, and Volume 06 loads inputs (TBD).

## 18. Traceability

Parent: SYS tier via SAD physical view. Children: analysis and test artefacts in Chapters 03.13–03.20. RTM: REQ-HFPX-SPS-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 03.3) |
