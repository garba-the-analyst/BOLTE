# 17.3 Attack Surface Analysis

**Document ID:** HFPX-CYB-ASA-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Establish the structure for the HFP-X attack surface analysis (Chapter 17.3). This Tranche 6 draft defines the requirement set structure and derivation path; the surface inventory, reduction rules, review cadence and all security controls are TBD at this revision.

## 2. Scope

Covers attack-surface requirements for HFP-X, including the surface inventory (categories include RF links, physical ports and supply-chain interfaces — inventory TBD), surface-reduction rules and review cadence. Excludes selection of specific security mechanisms and excludes exploit or vulnerability specifics beyond generic threat classes.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parent — security classification)
- Vol 08 / Vol 11 / Vol 16 interface requirements (TBD, parents for interface boundaries)
- HFPX-CYB-ARC-001 Cybersecurity Architecture (allocation parent)
- HFPX-CYB-THR-001 Threat Model (threat parent)
- HFPX-CYB-IDX-001 Volume 17 index (README.md, Chapter 17.3)
- V&V Plan (Vol 22, not written)

## 4. Definitions & Acronyms

- ASA: attack surface analysis chapter
- Requirement ID `REQ-HFPX-YAS-[NNN]`; verification: Analysis / Inspection / Demonstration / Test / Review
- TBD / TBC: unknown data handling; no invented values
- Attack surface: the set of reachable interfaces and entry points described generically; inventory TBD
- Supply-chain interface: a point at which supplied items, data or tools enter the system; details TBD

## 5. System Context

Attack surface analysis connects the threat model to interface and control decisions:

```text
THREAT MODEL → ATTACK SURFACE ANALYSIS (this document) → ARCHITECTURE + CONTROLS → VERIFICATION (Vol 22)
```

The inventory, reduction rules and cadence are TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-YAS-001|The attack surface analysis shall maintain a surface inventory for HFP-X (inventory TBD; categories include RF links, physical ports and supply-chain interfaces).|HFPX-SYS-REQ-001 (security classification); Vol 08 / Vol 11 / Vol 16 interfaces (TBD)|Inspection|
| REQ-HFPX-YAS-002 | Each surface inventory entry shall be traced to its owning interface or boundary (tracing TBD). | HFPX-SYS-REQ-001 (security classification) | Inspection |
|REQ-HFPX-YAS-003|The attack surface analysis shall define surface-reduction rules for HFP-X (reduction rule TBD; all mechanisms unselected).|HFPX-SYS-REQ-001 (security classification)|Inspection|
|REQ-HFPX-YAS-004|The attack surface analysis shall define the review cadence for the surface inventory (review cadence TBD).|HFPX-SYS-REQ-001 (security classification)|Inspection|

## 7. Architecture

TBD — inventory structure, views and boundary mappings are undefined at this revision. All security controls TBD (mechanisms unselected).

## 8. Detailed Design

Not applicable — analysis level only. No inventory entries, reduction mechanisms or parameter values are approved at this revision.

## 9. Interfaces

Surface entries at Vol 08 / Vol 11 / Vol 16 interfaces, including RF links, physical ports and supply-chain interfaces, are TBD as categories only. Interface details remain TBD until interface requirements exist.

## 10. Operational Concept

Operational handling of attack-surface changes (how inventory updates propagate to operations and maintenance) is TBD.

## 11. Safety

No safety claim is made in this document. Coordination with the safety process (Vol 13) on surface entries with safety relevance is TBD.

## 12. Performance

TBD. No quantitative value is defined or approved at this revision.

## 13. Verification & Validation

Each requirement states its method in §6. The verification method at this revision is predominantly Review. Verification cases and evidence records are TBD in the V&V Plan (Vol 22).

## 14. Risks

- Inventory written before interfaces stabilise → high TBD density; mitigation: structure-only status is explicit
- Untracked surface growth; mitigation: reduction rules and review cadence (REQ-HFPX-YAS-003, REQ-HFPX-YAS-004)
- Drift between inventory and threat model; mitigation: traceability to HFPX-CYB-THR-001

## 15. Open Issues

- Surface inventory undefined (REQ-HFPX-YAS-001, REQ-HFPX-YAS-002)
- Surface-reduction rule undefined (REQ-HFPX-YAS-003)
- Review cadence undefined (REQ-HFPX-YAS-004)

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on system-level security classification (SYS tier), threat model (HFPX-CYB-THR-001), cybersecurity architecture (HFPX-CYB-ARC-001), Vol 08 / Vol 11 / Vol 16 interface requirements, and V&V Plan review cases (Vol 22).

## 18. Traceability

Parents: HFPX-SYS-REQ-001 (security classification); Vol 08 / Vol 11 / Vol 16 interfaces (TBD). Children: subsystem controls informed by surface entries, V&V review cases, RTM rows. RTM seed for REQ-HFPX-YAS-001..004 is added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Inventory, reduction rules and cadence require new revisions via change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 17.3, structure only) |
