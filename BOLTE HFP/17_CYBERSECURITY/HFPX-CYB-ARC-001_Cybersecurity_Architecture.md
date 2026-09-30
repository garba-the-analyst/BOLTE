# 17.1 Cybersecurity Architecture

**Document ID:** HFPX-CYB-ARC-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Establish the structure for the HFP-X cybersecurity architecture (Chapter 17.1). This Tranche 6 draft defines the requirement set structure and derivation path; all security controls, mechanisms, boundaries and quantitative values are TBD and unselected at this revision.

## 2. Scope

Covers cybersecurity architecture requirements for HFP-X, including security domains, allocation of controls to subsystems, and consistency with system-level security classification. Excludes selection of specific security mechanisms, products, or parameter values, which remain TBD. Detailed controls for Chapters 17.2–17.14 are owned by their respective documents.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parent — security classification)
- Vol 08 / Vol 11 / Vol 16 interface requirements (TBD, parents for interface boundaries)
- HFPX-CYB-IDX-001 Volume 17 index (README.md, Chapter 17.1)
- Sibling Volume 17 documents HFPX-CYB-THR-001, HFPX-CYB-ASA-001, HFPX-CYB-AVS-001, HFPX-CYB-CMS-001, HFPX-CYB-GSS-001, HFPX-CYB-ATH-001, HFPX-CYB-ATZ-001, HFPX-CYB-SBT-001, HFPX-CYB-FWS-001, HFPX-CYB-DPR-001, HFPX-CYB-IDS-001, HFPX-CYB-INR-001, HFPX-CYB-VER-001
- V&V Plan (Vol 22, not written)

## 4. Definitions & Acronyms

- CYB: cybersecurity domain; ARC: architecture chapter
- Requirement ID `REQ-HFPX-YAR-[NNN]`; verification: Analysis / Inspection / Demonstration / Test / Review
- TBD / TBC: unknown data handling; no invented values
- Security control: a protective measure or rule; all controls TBD (mechanisms unselected) at this revision
- Generic threat class: a category of adversarial action described without exploit or vulnerability specifics

## 5. System Context

Cybersecurity architecture is the allocation layer between system security needs and subsystem controls:

```text
SYS TIER (security classification) → CYB ARCHITECTURE (this document) → SUBSYSTEM CONTROLS (Vol 17.2–17.14, Vol 08/11/16) → VERIFICATION (Vol 22)
```

Trust boundaries, security domains and data flows are TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-YAR-001|The cybersecurity architecture shall define security domains and trust boundaries for HFP-X (domains and boundaries TBD).|HFPX-SYS-REQ-001 (security classification)|Inspection|
| REQ-HFPX-YAR-002 | The cybersecurity architecture shall allocate cybersecurity controls to subsystems and interfaces (allocation TBD; all mechanisms unselected). | HFPX-SYS-REQ-001 (security classification) | Inspection |
| REQ-HFPX-YAR-003 | The cybersecurity architecture shall maintain traceability from each allocated control to its system-level security parent (mapping TBD). | HFPX-SYS-REQ-001 (security classification) | Inspection |
|REQ-HFPX-YAR-004|The cybersecurity architecture shall remain consistent with Vol 08 / Vol 11 / Vol 16 interface boundaries (interfaces TBD).|HFPX-SYS-REQ-001 (security classification); Vol 08 / Vol 11 / Vol 16 interfaces (TBD)|Inspection|
|REQ-HFPX-YAR-005|The cybersecurity architecture shall define the rule for when the architecture description is updated (update rule TBD).|HFPX-SYS-REQ-001 (security classification)|Inspection|

## 7. Architecture

TBD — security domains, layers, trust boundaries and allocation views are undefined at this revision. No architecture figure is approved. All security controls TBD (mechanisms unselected).

## 8. Detailed Design

Not applicable — architecture level only. No security mechanisms are selected, and no parameter values are defined at this revision.

## 9. Interfaces

Interface boundaries with Vol 08 / Vol 11 / Vol 16 are TBD. Interface requirements, data-flow inventories and boundary protection rules are undefined and shall remain TBD until interface requirements exist.

## 10. Operational Concept

Operational use of the cybersecurity architecture (deployment, configuration management, key roles in operation) is TBD. No operational procedure is approved at this revision.

## 11. Safety

No safety claim is made in this document. Coordination with the safety process (Vol 13) is TBD. Cybersecurity controls shall not be credited for safety functions until assessed through the safety process.

## 12. Performance

TBD. No throughput, latency, availability or resource-overhead value is defined or approved at this revision. No quantitative value is stated in §6.

## 13. Verification & Validation

Each requirement states its method in §6. Verification cases and evidence records are TBD in the V&V Plan (Vol 22). Requirements without a verification method are rejected at review. Review is the primary method at this structure-only revision.

## 14. Risks

- Architecture written before subsystem interfaces and threat model exist → high TBD density; mitigation: structure-only status is explicit
- Orphaned or overlapping controls across Vol 17.2–17.14; mitigation: allocation traceability gate per review (REQ-HFPX-YAR-003)
- Mechanism selection ahead of architecture stability; mitigation: all mechanisms remain unselected until architecture is approved

## 15. Open Issues

- Security domains and trust boundaries undefined (REQ-HFPX-YAR-001)
- Control allocation undefined (REQ-HFPX-YAR-002)
- Update rule undefined (REQ-HFPX-YAR-005)
- All interface boundaries TBD pending Vol 08 / Vol 11 / Vol 16

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on system-level security classification (SYS tier), Vol 08 / Vol 11 / Vol 16 interface requirements, threat model (HFPX-CYB-THR-001), attack surface analysis (HFPX-CYB-ASA-001), and V&V Plan cases (Vol 22).

## 18. Traceability

Parents: HFPX-SYS-REQ-001 (security classification); Vol 08 / Vol 11 / Vol 16 interfaces (TBD). Children: subsystem cybersecurity requirements (Vol 17.2–17.14), architecture views, V&V cases, RTM rows. RTM seed for REQ-HFPX-YAR-001..005 is added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Control selection, domain definition and quantified rules require new revisions via change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 17.1, structure only) |
