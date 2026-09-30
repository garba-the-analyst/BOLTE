# Helmet Software

**Document ID:** HFPX-SW-HMI-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X helmet software scope (Chapter 16.14): display and alerting implementation, prioritisation, verification, and versioning. No implementation stated.

## 2. Scope

Covers helmet software requirements, architecture placement, interfaces, and verification planning. Display and alerting functional detail is TBD per Vol 10. Excludes helmet hardware and optics (Vol 10), control and safety logic (Vol 07/13), and communications protocols (Vol 11).

## 3. Applicable Documents

- Parent requirements: SYS-002 thread; WDP/WSA tier; VVP thread
- HFPX-ARC-SW-001 Software Architecture (layering, determinism policy, assurance structured according to DO-178C concepts)
- Vol 10 HMI definition (display and alerting functions, TBD)
- Vol 16 sibling software chapters; Vol 13 safety inputs
- DO-178C concepts (structured-according-to only, no compliance claimed at this stage)

## 4. Definitions & Acronyms

- Display implementation: software rendering of symbology, status, and guidance cues defined in Vol 10 (contents TBD).
- Alerting implementation: software generation of cautions, warnings, and advisories defined in Vol 10 (set and logic TBD).
- Prioritisation: ordering and suppression rules applied when multiple alerts or display elements compete (rules TBD).
- Versioning: identification and control of helmet software releases (scheme TBD).

## 5. System Context

Helmet software executes within the layered software architecture and interfaces with navigation, health, fault-management, communications, and logging services. It receives display-source and alert-source inputs and produces rendered display, audio or visual alert outputs, and log outputs across applicable states (states and signals TBD).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-WHS-001 | The helmet software shall implement display and alerting functions as defined in Vol 10 (functions TBD). | SYS-002; WDP/WSA tier; VVP thread | Inspection + Test |
| REQ-HFPX-WHS-002 | The helmet software shall apply prioritisation to competing alerts and display elements (rules TBD). | SYS-002; WDP/WSA tier; VVP thread | Analysis + Test |
|REQ-HFPX-WHS-003|Verification of helmet software shall be defined per the VVP thread (verification approach TBD).|SYS-002; WDP/WSA tier; VVP thread|Inspection|
| REQ-HFPX-WHS-004 | The helmet software shall be subject to versioning control (scheme TBD). | SYS-002; WDP/WSA tier; VVP thread | Inspection |

Software assurance is structured according to DO-178C concepts; no compliance is claimed at this stage and no integrity values are stated.

## 7. Architecture

Helmet software resides in the application/services layers defined by HFPX-ARC-SW-001 (allocation TBD). Rendering, alert generation, prioritisation, and version-identification functions are partitioned per determinism and independence policy (TBD). Languages, RTOS selection, graphics services, and partitioning mechanisms are TBD.

## 8. Detailed Design

Not applicable at this revision. Software requirements, design descriptions, symbology logic, and code are deferred to later Vol 16 detail and Vol 10. No implementation, layout, or parameter values stated.

## 9. Interfaces

Software interfaces to display sources, alert sources, audio/visual output services, configuration services, and logging services are TBD. Signatures, timing, and formats are TBD and will be detailed in software ICDs and Vol 10.

## 10. Operational Concept

Helmet software operates across power-up, flight-mode, degraded-mode, and maintenance states (behaviour per state TBD). Prioritised alerting remains available in degraded states as defined (TBD). Night, degraded-visibility, and failure-state presentations are TBD per Vol 10.

## 11. Safety

Helmet software safety inputs, hazard contributions (including misleading-display and missed-alert considerations), and independence provisions feed Vol 13 analyses (all TBD). No integrity values stated. Determinism, boundedness, and partition independence remain architecture constraints per HFPX-ARC-SW-001.

## 12. Performance

Timing (render latency, alert latency), memory, and throughput budgets for helmet software are TBD. Budget holders: software/compute (Vol 16/08), HMI (Vol 10). No values stated.

## 13. Verification & Validation

Verified by inspection and test (display/alerting implementation, versioning) and analysis plus test (prioritisation), structured according to DO-178C concepts with no compliance claimed. Detailed verification cases, HMI rig environments, and flight-test hooks are TBD per the VVP thread and Vol 19/22/23.

## 14. Risks

- Display/alerting scope drift ahead of Vol 10 maturity; mitigation: TBD-gated requirement WHS-001.
- Alert overload or suppression errors; mitigation: prioritisation requirement WHS-002 with Vol 13 review.
- Uncontrolled helmet software variants; mitigation: versioning requirement WHS-004 with Chapter 16.17 discipline.

## 15. Open Issues

Display and alerting function set per Vol 10 TBD. Prioritisation and suppression rules TBD. Verification approach and environments TBD. Versioning scheme TBD.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on Vol 10 HMI definition, software architecture layering (HFPX-ARC-SW-001), health and fault-management sources (Chapters 16.11/16.12), configuration management (Chapter 16.17), safety analyses (Vol 13), and VVP planning (Vol 22/23).

## 18. Traceability

Parents: SYS-002 thread; WDP/WSA tier; VVP thread. Children: subsystem software requirements, design descriptions, ICDs, V&V cases (all TBD). RTM: REQ-HFPX-WHS-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Chapter 16.14.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 16.14) |
