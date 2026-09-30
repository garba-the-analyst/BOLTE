# 17.8 Authorisation

**Document ID:** HFPX-CYB-ATZ-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Establish the structure for HFP-X authorisation (Chapter 17.8). This Tranche 6 draft defines the requirement set structure and derivation path; all authorisation controls, permissions and quantitative values are TBD and unselected at this revision.

## 2. Scope

Covers authorisation requirements for HFP-X, including decisions on permitted actions following identity verification. Excludes selection of specific security mechanisms and excludes exploit or vulnerability specifics beyond generic threat classes. Identity verification itself is covered in HFPX-CYB-ATH-001.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parent — security classification)
- Vol 08 / Vol 11 / Vol 16 interface requirements (TBD, parents for authorised boundaries)
- HFPX-CYB-ARC-001 Cybersecurity Architecture (allocation parent)
- HFPX-CYB-ATH-001 Authentication (identity-verification parent)
- HFPX-CYB-IDX-001 Volume 17 index (README.md, Chapter 17.8)
- V&V Plan (Vol 22, not written)

## 4. Definitions & Acronyms

- ATZ: authorisation chapter
- Requirement ID `REQ-HFPX-YAZ-[NNN]`; verification: Analysis / Inspection / Demonstration / Test / Review
- TBD / TBC: unknown data handling; no invented values
- Authorisation: decision on permitted actions for a verified identity; policies and permissions TBD (mechanisms unselected)

## 5. System Context

Authorisation follows identity verification and gates permitted actions:

```text
SYS TIER (security classification) → AUTHENTICATION → AUTHORISATION (this document) → SUBSYSTEM ENFORCEMENT → VERIFICATION (Vol 22)
```

Policies, permissions and boundaries are TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-YAZ-001 | The authorisation design shall require an authorisation decision before a permitted action is executed (actions, permissions and controls TBD; all mechanisms unselected). | HFPX-SYS-REQ-001 (security classification) | Analysis |
| REQ-HFPX-YAZ-002 | The authorisation design shall define where authorisation is enforced across Vol 08 / Vol 11 / Vol 16 boundaries (locations TBD). | HFPX-SYS-REQ-001 (security classification); Vol 08 / Vol 11 / Vol 16 interfaces (TBD) | Inspection |
| REQ-HFPX-YAZ-003 | The authorisation design shall define the rule for handling denied authorisation requests (handling rule TBD). | HFPX-SYS-REQ-001 (security classification) | Analysis |
| REQ-HFPX-YAZ-004 | Authorisation controls shall be traceable to the cybersecurity architecture allocation (tracing TBD). | HFPX-SYS-REQ-001 (security classification) | Inspection |

## 7. Architecture

TBD — authorisation placement, policy groupings and allocation views are undefined at this revision. All security controls TBD (mechanisms unselected).

## 8. Detailed Design

Not applicable — requirements level only. No authorisation mechanisms are selected, and no parameter values are defined at this revision.

## 9. Interfaces

Enforcement boundaries at Vol 08 / Vol 11 / Vol 16 interfaces are TBD. Interface authorisation rules remain TBD until interface requirements exist.

## 10. Operational Concept

Operational handling of authorisation (permission assignment, review, maintenance interactions) is TBD. No operational procedure is approved at this revision.

## 11. Safety

No safety claim is made in this document. Coordination with the safety process (Vol 13) on authorisation with safety relevance is TBD.

## 12. Performance

TBD. No quantitative value is defined or approved at this revision.

## 13. Verification & Validation

Each requirement states its method in §6. Verification cases and evidence records are TBD in the V&V Plan (Vol 22). Requirements without a verification method are rejected at review.

## 14. Risks

- Authorisation written before permissions and interfaces stabilise → high TBD density; mitigation: structure-only status is explicit
- Overlap with authentication and avionics / ground station controls; mitigation: allocation traceability (REQ-HFPX-YAZ-004)
- Mechanism selection ahead of requirements stability; mitigation: all mechanisms remain unselected

## 15. Open Issues

- Permitted actions, enforcement locations and denial-handling rules undefined (REQ-HFPX-YAZ-001..003)
- Allocation tracing undefined (REQ-HFPX-YAZ-004)
- All authorisation controls TBD (mechanisms unselected)

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on system-level security classification (SYS tier), authentication (HFPX-CYB-ATH-001), cybersecurity architecture (HFPX-CYB-ARC-001), Vol 08 / Vol 11 / Vol 16 interface requirements, and V&V Plan cases (Vol 22).

## 18. Traceability

Parents: HFPX-SYS-REQ-001 (security classification); Vol 08 / Vol 11 / Vol 16 interfaces (TBD). Children: authorisation design, enforcement implementations, V&V cases, RTM rows. RTM seed for REQ-HFPX-YAZ-001..004 is added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Control selection and boundary definition require new revisions via change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 17.8, structure only) |
