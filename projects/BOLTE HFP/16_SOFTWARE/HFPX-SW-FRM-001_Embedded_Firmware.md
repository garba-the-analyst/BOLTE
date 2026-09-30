# Embedded Firmware

**Document ID:** HFPX-SW-FRM-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X embedded firmware item (Chapter 16.5): inventory scaffolding, update-rule scaffolding, versioning discipline, and verification scaffolding. No implementation or values stated.

## 2. Scope

Covers firmware inventory, update rules, versioning and traceability, and verification scaffolding for embedded firmware. Excludes device selection, image contents, update mechanism design, and tool qualification (all TBD).

## 3. Applicable Documents

- SYS-002 (parent system requirements)
- HFPX-ARC-SW-001 Software Architecture (parent requirements REQ-HFPX-SWA-001..004)
- DO-178C concepts (structured-according-to only, no compliance claimed)
- HFPX-SW-ARC-001 Software Architecture, HFPX-SW-PLN-001 Software Development Plan (structure only)
- VVP thread (verification and validation thread, details TBD)

## 4. Definitions & Acronyms

- Embedded firmware: low-level software bound to programmable devices and board support functions (inventory TBD).
- Update rule: policy governing when and how firmware may be updated (TBD).
- Versioning: identification and traceability discipline for firmware images and devices (scheme TBD).

## 5. System Context

Embedded firmware underpins the platform layer, exposing sensor, actuator, bus, and logging services to application-layer flight and safety software. It operates under deterministic bounded primary-control policy with configuration control across development and maintenance states.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-WEF-001 | The embedded firmware inventory shall be defined (devices and images TBD). | SYS-002; REQ-HFPX-SWA-001; VVP | Inspection |
| REQ-HFPX-WEF-002 | Firmware update rules shall be defined (policy TBD). | SYS-002; REQ-HFPX-SWA-004; VVP | Inspection |
| REQ-HFPX-WEF-003 | Firmware shall enforce versioning and traceability discipline per Vol 16 (scheme TBD). | SYS-002; REQ-HFPX-SWA-004; VVP | Inspection |
| REQ-HFPX-WEF-004 | Embedded firmware shall be verified by review and test (details TBD). | SYS-002; REQ-HFPX-SWA-002; VVP | Inspection + Test |

## 7. Architecture

Platform-layer firmware items (inventory TBD) with update-rule placeholders and versioning discipline. Primary-control paths using firmware remain deterministic, bounded, and verifiable; AI functions, if present, remain advisory-only and segregated from primary and safety authority. Assurance scaffolding is structured according to DO-178C concepts with no compliance claim.

## 8. Detailed Design

Not applicable at this revision. Firmware requirements, design descriptions, images, and update mechanisms are deferred. No implementation stated.

## 9. Interfaces

Firmware interfaces: device programming interfaces, board-support APIs, sensor and actuator service APIs, update and rollback interfaces. Signatures, timing, and protocols TBD; detailed in software ICDs.

## 10. Operational Concept

Firmware executes at power-up, in flight-mode and degraded-mode, and in maintenance states. Update sequencing, rollback behaviour, and compatibility checks are TBD.

## 11. Safety

Firmware integrity and update safety feed Vol 13. Determinism, boundedness, and independence provisions apply where firmware supports primary or safety paths. No integrity values stated.

## 12. Performance

Timing, memory-footprint, and throughput budgets are TBD. Budget holders: platform and firmware (Vol 16). No timing figures stated.

## 13. Verification & Validation

Verified by review (inventory, update rules, versioning discipline) and test (functional and regression test scaffolding). Validated later via integrated SIL and HIL campaigns per the VVP thread.

## 14. Risks

- Uncontrolled firmware updates defeating configuration control; mitigation: update-rule and versioning requirements (WEF-002, WEF-003).
- Firmware inventory gaps across boards and devices; mitigation: inventory inspection requirement (WEF-001).

## 15. Open Issues

Device and image inventory, update policy and mechanism, versioning scheme, and verification scope all TBD. Toolchain and programming provisions TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SYS-002 system requirements, SWA tier architecture, Vol 16 plan and architecture items, and hardware and device selection.

## 18. Traceability

Parents: SYS-002; SWA tier (REQ-HFPX-SWA-001..004); VVP thread. Children: firmware requirements, images, update procedures, V&V cases. RTM: REQ-HFPX-WEF-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Chapter 16.5.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 16.5) |
