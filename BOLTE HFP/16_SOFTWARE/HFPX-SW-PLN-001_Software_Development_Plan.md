# Software Development Plan

**Document ID:** HFPX-SW-PLN-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X Software Development Plan (Chapter 16.1): lifecycle scaffolding, standards structure, roles, tooling, and assurance-level scaffolding. No implementation, tools, or values selected.

## 2. Scope

Covers software lifecycle definition, standards scaffolding structured according to DO-178C concepts, role and tooling scaffolding, and assurance-level scaffolding for Vol 16. Excludes detailed processes, tool selection and qualification, staffing assignments, and schedule (all TBD).

## 3. Applicable Documents

- SYS-002 (parent system requirements)
- HFPX-ARC-SW-001 Software Architecture (parent requirements REQ-HFPX-SWA-001..004)
- DO-178C concepts (structured-according-to only, no compliance claimed)
- Vol 16 sibling documents (Chapters 16.2..16.9 structure only)
- VVP thread (verification and validation thread, details TBD)

## 4. Definitions & Acronyms

- Lifecycle: sequence of software planning, development, verification, and configuration processes (scope TBD).
- Standards scaffolding: planned set of software standards and plans structured according to DO-178C concepts (contents TBD, no compliance claimed).
- Deterministic bounded control: primary flight control executes with predictable behaviour and bounded response (bounds TBD).
- Advisory-only AI: AI functions, if present, are segregated advisory outputs that never override pilot or safety authority.

## 5. System Context

The Software Development Plan governs all Vol 16 software items. It receives system requirements (SYS-002), software architecture constraints (SWA tier), and safety inputs, and produces lifecycle, standards, role, tooling, and assurance scaffolding for flight, safety, firmware, driver, algorithm, navigation, and control software items.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-WDP-001 | The software development plan shall define the software lifecycle processes and artefacts (scope TBD). | SYS-002; REQ-HFPX-SWA-004; VVP | Inspection |
| REQ-HFPX-WDP-002 | Software standards scaffolding shall be structured according to DO-178C concepts (no compliance claimed at this stage). | SYS-002; REQ-HFPX-SWA-003; VVP | Inspection |
| REQ-HFPX-WDP-003 | The plan shall define software roles and responsibilities (TBD). | SYS-002; REQ-HFPX-SWA-004; VVP | Inspection |
| REQ-HFPX-WDP-004 | The plan shall define software tooling and environment controls (TBD). | SYS-002; REQ-HFPX-SWA-004; VVP | Inspection |
| REQ-HFPX-WDP-005 | Software assurance levels shall remain TBD and unassigned at this revision. | SYS-002; REQ-HFPX-SWA-003; VVP | Inspection |

## 7. Architecture

Lifecycle scaffolding (processes, artefacts, sequencing TBD) aligned to the layered software architecture. Standards scaffolding follows DO-178C structure without compliance claim or level assignment. Primary flight control is constrained to deterministic, bounded, verifiable behaviour; AI functions, if present, reside in a segregated advisory partition only. Roles, tooling, and environments are placeholders pending allocation.

## 8. Detailed Design

Not applicable at this revision. Lifecycle workflows, standards contents, role assignments, and tool selections are deferred. No implementation stated.

## 9. Interfaces

Plan interfaces: requirements management, configuration management, verification thread, and safety assessment inputs. Ownership, formats, and protocols TBD; detailed in Vol 16 interface artefacts and software ICDs.

## 10. Operational Concept

The plan applies across development, verification, and maintenance states. Safety and verification independence provisions remain in effect whenever software artefacts are produced or changed; advisory AI outputs are display and test-logging only.

## 11. Safety

Determinism, boundedness, verifiability, and advisory-only AI are lifecycle constraints carried from the SWA tier. Assurance scaffolding is structured according to DO-178C concepts with no integrity values stated and no compliance claimed. Safety assessment linkage feeds Vol 13.

## 12. Performance

No performance values stated. Lifecycle throughput, effort, and schedule budgets are TBD. Budget holders: software planning (Vol 16), systems (SYS-002). No timing figures stated.

## 13. Verification & Validation

Verified by inspection and review of lifecycle definition, standards scaffolding, role and tooling scaffolding, and unassigned assurance levels. Validated later via VVP thread audits and artefact reviews (details TBD).

## 14. Risks

- Lifecycle scope creep before baselining; mitigation: Tranche 6 structure-only discipline with TBD placeholders.
- Assurance scaffolding mistaken for compliance; mitigation: explicit structured-according-to-only statement with no compliance claim (WDP-002).

## 15. Open Issues

Lifecycle phases, standards contents, role assignments, tool selections, and assurance-level targets all TBD. Traceability tooling and qualification approach TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SYS-002 system requirements, SWA tier architecture (REQ-HFPX-SWA-001..004), safety inputs (Vol 13), and VVP thread definition. Sibling Vol 16 items consume this plan.

## 18. Traceability

Parents: SYS-002; SWA tier (REQ-HFPX-SWA-001..004); VVP thread. Children: Vol 16 software items, software standards, V&V cases. RTM: REQ-HFPX-WDP-001..005 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Chapter 16.1.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 16.1) |
