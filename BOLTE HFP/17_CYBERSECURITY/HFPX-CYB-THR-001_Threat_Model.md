# 17.2 Threat Model

**Document ID:** HFPX-CYB-THR-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Establish the structure for the HFP-X threat model (Chapter 17.2). This Tranche 6 draft defines the requirement set structure and derivation path; threat-actor classes, trust boundaries, threat enumerations and all security controls are TBD at this revision.

## 2. Scope

Covers threat-model requirements for HFP-X, including threat-actor classes, trust boundaries, generic threat classes and model maintenance. Excludes selection of specific security mechanisms and excludes exploit or vulnerability specifics beyond generic threat classes.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parent — security classification)
- Vol 08 / Vol 11 / Vol 16 interface requirements (TBD, parents for interface boundaries)
- HFPX-CYB-ARC-001 Cybersecurity Architecture (allocation parent)
- HFPX-CYB-IDX-001 Volume 17 index (README.md, Chapter 17.2)
- V&V Plan (Vol 22, not written)

## 4. Definitions & Acronyms

- THR: threat model chapter
- Requirement ID `REQ-HFPX-YTM-[NNN]`; verification: Analysis / Inspection / Demonstration / Test / Review
- TBD / TBC: unknown data handling; no invented values
- Threat-actor class: a category of adversary described generically; classes TBD
- Trust boundary: a boundary across which data or control passes between different trust levels; boundaries TBD
- Generic threat class: a category of adversarial action described without exploit or vulnerability specifics

## 5. System Context

The threat model informs architecture and all downstream controls:

```text
SYS TIER (security classification) → THREAT MODEL (this document) → CYB ARCHITECTURE + CONTROLS (Vol 17.1, 17.3–17.14) → VERIFICATION (Vol 22)
```

Actors, boundaries and enumerations are TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-YTM-001|The threat model shall define threat-actor classes for HFP-X (threat-actor classes TBD; no exploit or vulnerability specifics).|HFPX-SYS-REQ-001 (security classification)|Inspection|
|REQ-HFPX-YTM-002|The threat model shall define trust boundaries for HFP-X, consistent with Vol 08 / Vol 11 / Vol 16 interfaces (trust boundaries TBD).|HFPX-SYS-REQ-001 (security classification); Vol 08 / Vol 11 / Vol 16 interfaces (TBD)|Inspection|
|REQ-HFPX-YTM-003|The threat model shall enumerate generic threat classes against the defined trust boundaries (enumeration TBD; generic classes only).|HFPX-SYS-REQ-001 (security classification)|Inspection|
|REQ-HFPX-YTM-004|The threat model shall define the rule for when the threat model is updated (model-update rule TBD).|HFPX-SYS-REQ-001 (security classification)|Inspection|

## 7. Architecture

TBD — threat-model views, diagrams and boundary decompositions are undefined at this revision. All security controls TBD (mechanisms unselected).

## 8. Detailed Design

Not applicable — model level only. No threat-actor classes, trust boundaries or generic threat-class enumerations are approved at this revision. No exploit or vulnerability specifics are stated.

## 9. Interfaces

Trust boundaries at Vol 08 / Vol 11 / Vol 16 interfaces are TBD. Interface-related threats are covered only as generic threat classes; details remain TBD until interface requirements exist.

## 10. Operational Concept

Operational use of the threat model (how the model informs operations and maintenance) is TBD. No operational procedure is approved at this revision.

## 11. Safety

No safety claim is made in this document. Coordination with the safety process (Vol 13) on threats with safety relevance is TBD.

## 12. Performance

TBD. No quantitative value is defined or approved at this revision.

## 13. Verification & Validation

Each requirement states its method in §6. The verification method at this revision is Review. Verification cases and evidence records are TBD in the V&V Plan (Vol 22).

## 14. Risks

- Threat model written before interfaces and architecture stabilise → high TBD density; mitigation: structure-only status is explicit
- Incomplete actor or boundary coverage; mitigation: model-update rule (REQ-HFPX-YTM-004) and review gate
- Drift between threat model and downstream controls; mitigation: traceability to HFPX-CYB-ARC-001

## 15. Open Issues

- Threat-actor classes undefined (REQ-HFPX-YTM-001)
- Trust boundaries undefined (REQ-HFPX-YTM-002)
- Generic threat-class enumeration undefined (REQ-HFPX-YTM-003)
- Model-update rule undefined (REQ-HFPX-YTM-004)

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on system-level security classification (SYS tier), cybersecurity architecture (HFPX-CYB-ARC-001), Vol 08 / Vol 11 / Vol 16 interface requirements, and V&V Plan review cases (Vol 22).

## 18. Traceability

Parents: HFPX-SYS-REQ-001 (security classification); Vol 08 / Vol 11 / Vol 16 interfaces (TBD). Children: attack surface analysis, subsystem controls (Vol 17.3–17.14), V&V review cases, RTM rows. RTM seed for REQ-HFPX-YTM-001..004 is added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Actor classes, boundaries, enumerations and update rules require new revisions via change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 17.2, structure only) |
