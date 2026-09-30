# 17.9 Secure Boot

**Document ID:** HFPX-CYB-SBT-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Establish the structure for HFP-X secure boot (Chapter 17.9). This Tranche 6 draft defines the requirement set structure and derivation path; all secure boot controls, stages and quantitative values are TBD and unselected at this revision.

## 2. Scope

Covers secure boot requirements for HFP-X, including verification of boot integrity before execution proceeds. Excludes selection of specific security mechanisms and excludes exploit or vulnerability specifics beyond generic threat classes. Firmware update and lifecycle handling is covered in HFPX-CYB-FWS-001.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parent — security classification)
- Vol 08 / Vol 11 / Vol 16 interface requirements (TBD, parents for affected boundaries)
- HFPX-CYB-ARC-001 Cybersecurity Architecture (allocation parent)
- HFPX-CYB-THR-001 Threat Model; HFPX-CYB-FWS-001 Firmware Security
- HFPX-CYB-IDX-001 Volume 17 index (README.md, Chapter 17.9)
- V&V Plan (Vol 22, not written)

## 4. Definitions & Acronyms

- SBT: secure boot chapter
- Requirement ID `REQ-HFPX-YSB-[NNN]`; verification: Analysis / Inspection / Demonstration / Test / Review
- TBD / TBC: unknown data handling; no invented values
- Secure boot: verification of boot-stage integrity before execution proceeds; stages and methods TBD (mechanisms unselected)

## 5. System Context

Secure boot anchors trust at start-up for downstream functions:

```text
SYS TIER (security classification) → CYB ARCHITECTURE → SECURE BOOT (this document) → FIRMWARE + SUBSYSTEM FUNCTIONS → VERIFICATION (Vol 22)
```

Boot stages, trust anchors and failure responses are TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-YSB-001 | The secure boot design shall verify boot-stage integrity before execution proceeds (stages and controls TBD; all mechanisms unselected). | HFPX-SYS-REQ-001 (security classification) | Analysis |
| REQ-HFPX-YSB-002 | The secure boot design shall define where secure boot applies across subsystems (applicability TBD). | HFPX-SYS-REQ-001 (security classification) | Inspection |
| REQ-HFPX-YSB-003 | The secure boot design shall define the rule for handling failed boot verification (handling rule TBD). | HFPX-SYS-REQ-001 (security classification) | Analysis |
| REQ-HFPX-YSB-004 | Secure boot controls shall be traceable to the cybersecurity architecture allocation (tracing TBD). | HFPX-SYS-REQ-001 (security classification) | Inspection |

## 7. Architecture

TBD — boot chains, trust anchors and allocation views are undefined at this revision. All security controls TBD (mechanisms unselected).

## 8. Detailed Design

Not applicable — requirements level only. No secure boot mechanisms are selected, and no parameter values are defined at this revision. No specific cryptographic mechanisms are stated.

## 9. Interfaces

Affected boundaries at Vol 08 / Vol 11 / Vol 16 interfaces are TBD. Boot-related interface rules remain TBD until interface requirements exist.

## 10. Operational Concept

Operational handling of secure boot (recovery, maintenance interactions) is TBD. No operational procedure is approved at this revision.

## 11. Safety

No safety claim is made in this document. Coordination with the safety process (Vol 13) on boot behaviour with safety relevance is TBD.

## 12. Performance

TBD. No quantitative value is defined or approved at this revision.

## 13. Verification & Validation

Each requirement states its method in §6. Verification cases and evidence records are TBD in the V&V Plan (Vol 22). Requirements without a verification method are rejected at review.

## 14. Risks

- Secure boot written before computing architecture stabilises → high TBD density; mitigation: structure-only status is explicit
- Overlap with firmware security; mitigation: allocation traceability (REQ-HFPX-YSB-004) and interface with HFPX-CYB-FWS-001
- Mechanism selection ahead of requirements stability; mitigation: all mechanisms remain unselected

## 15. Open Issues

- Boot stages, applicability and failure-handling rules undefined (REQ-HFPX-YSB-001..003)
- Allocation tracing undefined (REQ-HFPX-YSB-004)
- All secure boot controls TBD (mechanisms unselected)

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on system-level security classification (SYS tier), cybersecurity architecture (HFPX-CYB-ARC-001), firmware security (HFPX-CYB-FWS-001), Vol 08 / Vol 11 / Vol 16 interface requirements, and V&V Plan cases (Vol 22).

## 18. Traceability

Parents: HFPX-SYS-REQ-001 (security classification); Vol 08 / Vol 11 / Vol 16 interfaces (TBD). Children: secure boot design, V&V cases, RTM rows. RTM seed for REQ-HFPX-YSB-001..004 is added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Control selection and stage definition require new revisions via change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 17.9, structure only) |
