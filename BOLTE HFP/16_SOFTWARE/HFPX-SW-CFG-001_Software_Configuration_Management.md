# Software Configuration Management

**Document ID:** HFPX-SW-CFG-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X software configuration management scope (Chapter 16.17): versioning and branching, baseline control, change trace, and release records. No tooling selected.

## 2. Scope

Covers SCM requirements for all Vol 16 software items including requirements, design descriptions, code, tests, and verification artefacts. Excludes programme-level configuration control (TBD), hardware configuration (Vol 08), and detailed release approval workflows beyond software records (TBD).

## 3. Applicable Documents

- Parent requirements: SYS-002 thread; WDP/WSA tier; VVP thread
- HFPX-ARC-SW-001 Software Architecture (versioning and traceability discipline)
- Vol 16 sibling software chapters; Vol 22/23 VVP threads
- DO-178C concepts for configuration control and traceability (structured-according-to only, no compliance claimed at this stage)

## 4. Definitions & Acronyms

- Versioning: unique identification of software items and releases (scheme TBD).
- Branching: controlled divergence and merging of software lines of development (policy TBD).
- Baseline: a controlled, immutable reference set of software items (rule TBD).
- Change trace: linkage from change requests through affected items to verification (mechanism TBD).
- Release records: recorded evidence of a software release and its contents (contents TBD).

## 5. System Context

SCM governs software items across the layered architecture from requirements through code to verification artefacts. It interfaces with development, testing (Chapter 16.16), verification (Chapter 16.18), and VVP baselines, producing controlled baselines and release records across the lifecycle (all TBD).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-WCF-001 | Software configuration management shall provide versioning and branching control for software items (scheme TBD). | SYS-002; WDP/WSA tier; VVP thread | Inspection |
| REQ-HFPX-WCF-002 | Software configuration management shall enforce a defined baseline rule for software items (rule TBD). | SYS-002; WDP/WSA tier; VVP thread | Inspection |
| REQ-HFPX-WCF-003 | Software configuration management shall provide change trace from change requests through affected items to verification (mechanism TBD). | SYS-002; WDP/WSA tier; VVP thread | Inspection |
| REQ-HFPX-WCF-004 | Software configuration management shall produce release records for software releases (contents TBD). | SYS-002; WDP/WSA tier; VVP thread | Inspection |

Software assurance is structured according to DO-178C concepts; no compliance is claimed at this stage.

## 7. Architecture

SCM is organised around controlled repositories, baseline promotion, and trace linkage per HFPX-ARC-SW-001 versioning and traceability discipline. Repository structure, access control, branching model, and promotion gates are TBD. No tools selected.

## 8. Detailed Design

Not applicable at this revision. SCM plans, procedures, repository definitions, and tool configurations are deferred to later Vol 16 detail. No implementation stated.

## 9. Interfaces

Interfaces to requirements repositories, development environments, test and verification environments, and VVP baselines are TBD. Formats, identifiers, and data-exchange provisions are TBD.

## 10. Operational Concept

SCM operates across the development lifecycle: item creation and versioning, baseline establishment, change processing with trace, and release with records. Baselines support testing, verification, and integration activities per the VVP thread. Promotion and approval workflows are TBD.

## 11. Safety

SCM safety inputs, including integrity of baselines supporting safety claims and independence provisions feeding Vol 13, are TBD. No integrity values stated.

## 12. Performance

Repository capacity, availability, and throughput provisions are TBD. Budget holders: software/compute (Vol 16/08). No values stated.

## 13. Verification & Validation

SCM provisions are verified by inspection (versioning/branching control, baseline rule, change trace, release records), structured according to DO-178C concepts with no compliance claimed. Audits of baselines and trace completeness are TBD per the VVP thread.

## 14. Risks

- Uncontrolled variants proliferating across teams; mitigation: versioning and branching requirement WCF-001.
- Baseline drift invalidating verification credit; mitigation: baseline-rule requirement WCF-002.
- Untraced change escaping to release; mitigation: change-trace and release-record requirements WCF-003/WCF-004.

## 15. Open Issues

Versioning and branching scheme TBD. Baseline rule and promotion gates TBD. Change-trace mechanism TBD. Release-record contents and retention TBD. Tooling TBD.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on software architecture traceability discipline (HFPX-ARC-SW-001), Vol 16 software item definitions, testing and verification planning (Chapters 16.16/16.18), and VVP baselines (Vol 22/23).

## 18. Traceability

Parents: SYS-002 thread; WDP/WSA tier; VVP thread. Children: SCM plans, baselines, change records, release records (all TBD). RTM: REQ-HFPX-WCF-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Chapter 16.17.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 16.17) |
