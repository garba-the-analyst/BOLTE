# 17.7 Authentication

**Document ID:** HFPX-CYB-ATH-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Establish the structure for HFP-X authentication (Chapter 17.7). This Tranche 6 draft defines the requirement set structure and derivation path; all authentication controls, identities and quantitative values are TBD and unselected at this revision.

## 2. Scope

Covers authentication requirements for HFP-X, including verification of claimed identities for actors and subsystems before granting interaction. Excludes selection of specific security mechanisms and excludes exploit or vulnerability specifics beyond generic threat classes. Authorisation decisions are covered in HFPX-CYB-ATZ-001.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parent — security classification)
- Vol 08 / Vol 11 / Vol 16 interface requirements (TBD, parents for authenticated boundaries)
- HFPX-CYB-ARC-001 Cybersecurity Architecture (allocation parent)
- HFPX-CYB-THR-001 Threat Model; HFPX-CYB-ASA-001 Attack Surface Analysis
- HFPX-CYB-IDX-001 Volume 17 index (README.md, Chapter 17.7)
- V&V Plan (Vol 22, not written)

## 4. Definitions & Acronyms

- ATH: authentication chapter
- Requirement ID `REQ-HFPX-YAT-[NNN]`; verification: Analysis / Inspection / Demonstration / Test / Review
- TBD / TBC: unknown data handling; no invented values
- Authentication: verification of a claimed identity prior to interaction; methods and identities TBD (mechanisms unselected)

## 5. System Context

Authentication supports all interaction decisions across the system:

```text
SYS TIER (security classification) → CYB ARCHITECTURE → AUTHENTICATION (this document) → AUTHORISATION + SUBSYSTEM CONTROLS → VERIFICATION (Vol 22)
```

Identities, boundaries and methods are TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-YAT-001 | The authentication design shall require verification of claimed identity before interaction (identities, interactions and controls TBD; all mechanisms unselected). | HFPX-SYS-REQ-001 (security classification) | Analysis |
| REQ-HFPX-YAT-002 | The authentication design shall define where authentication is required across Vol 08 / Vol 11 / Vol 16 boundaries (locations TBD). | HFPX-SYS-REQ-001 (security classification); Vol 08 / Vol 11 / Vol 16 interfaces (TBD) | Inspection |
| REQ-HFPX-YAT-003 | The authentication design shall define the rule for handling failed identity verification (handling rule TBD; no specific mechanisms selected). | HFPX-SYS-REQ-001 (security classification) | Analysis |
| REQ-HFPX-YAT-004 | Authentication controls shall be traceable to the cybersecurity architecture allocation (tracing TBD). | HFPX-SYS-REQ-001 (security classification) | Inspection |

## 7. Architecture

TBD — authentication placement, identity groupings and allocation views are undefined at this revision. All security controls TBD (mechanisms unselected).

## 8. Detailed Design

Not applicable — requirements level only. No authentication mechanisms are selected, and no parameter values are defined at this revision. No specific cryptographic mechanisms are stated.

## 9. Interfaces

Authenticated boundaries at Vol 08 / Vol 11 / Vol 16 interfaces are TBD. Interface authentication rules remain TBD until interface requirements exist.

## 10. Operational Concept

Operational handling of authentication (enrolment, revocation, maintenance interactions) is TBD. No operational procedure is approved at this revision.

## 11. Safety

No safety claim is made in this document. Coordination with the safety process (Vol 13) on authentication with safety relevance is TBD.

## 12. Performance

TBD. No quantitative value is defined or approved at this revision.

## 13. Verification & Validation

Each requirement states its method in §6. Verification cases and evidence records are TBD in the V&V Plan (Vol 22). Requirements without a verification method are rejected at review.

## 14. Risks

- Authentication written before identities and interfaces stabilise → high TBD density; mitigation: structure-only status is explicit
- Overlap with authorisation and communications security; mitigation: allocation traceability (REQ-HFPX-YAT-004)
- Mechanism selection ahead of requirements stability; mitigation: all mechanisms remain unselected

## 15. Open Issues

- Identities, required locations and failure-handling rules undefined (REQ-HFPX-YAT-001..003)
- Allocation tracing undefined (REQ-HFPX-YAT-004)
- All authentication controls TBD (mechanisms unselected)

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on system-level security classification (SYS tier), cybersecurity architecture (HFPX-CYB-ARC-001), threat model and attack surface analysis, Vol 08 / Vol 11 / Vol 16 interface requirements, and V&V Plan cases (Vol 22).

## 18. Traceability

Parents: HFPX-SYS-REQ-001 (security classification); Vol 08 / Vol 11 / Vol 16 interfaces (TBD). Children: authentication design, authorisation inputs, V&V cases, RTM rows. RTM seed for REQ-HFPX-YAT-001..004 is added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Control selection and boundary definition require new revisions via change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 17.7, structure only) |
