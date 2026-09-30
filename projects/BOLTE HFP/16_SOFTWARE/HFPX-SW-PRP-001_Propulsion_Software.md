# Propulsion Software

**Document ID:** HFPX-SW-PRP-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X propulsion software scope (Chapter 16.10): engine-control software functions, limit-protection behaviour, verification approach, and the analysis-only boundary where propulsion is involved. No implementation stated.

## 2. Scope

Covers propulsion software requirements, architecture placement, interfaces, and verification planning for engine-control and limit-protection functions. Engine-control functional detail is TBD per Vol 04.9. Excludes propulsion hardware design (Vol 04), flight-control laws (Vol 07), and tool qualification (TBD).

## 3. Applicable Documents

- Parent requirements: SYS-002 thread; WDP/WSA tier; VVP thread
- HFPX-ARC-SW-001 Software Architecture (layering, determinism policy, assurance structured according to DO-178C concepts)
- Vol 04 propulsion definition, notably Vol 04.9 (engine-control detail, TBD)
- Vol 16 sibling software chapters; Vol 13 safety inputs; Vol 22/23 verification threads
- DO-178C concepts (structured-according-to only, no compliance claimed at this stage)

## 4. Definitions & Acronyms

- Engine-control software: software implementing propulsion command, regulation, and sequencing functions (functions TBD per Vol 04.9).
- Limit protection: software behaviour enforcing propulsion operating limits (limits and responses TBD).
- Analysis-only boundary: scope in which propulsion-involved behaviour is addressed by analysis rather than by software execution claims (boundary TBD).

## 5. System Context

Propulsion software executes within the layered software architecture and interfaces with propulsion hardware, power and control services, health monitoring, and logging. It receives command and state inputs and produces propulsion command and status outputs across applicable flight and maintenance states (states and signals TBD).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-WPS-001 | The propulsion software shall implement engine-control software functions as defined in Vol 04.9 (functions TBD). | SYS-002; WDP/WSA tier; VVP thread | Inspection |
| REQ-HFPX-WPS-002 | The propulsion software shall implement limit-protection behaviour for propulsion operating limits (limits and responses TBD). | SYS-002; WDP/WSA tier; VVP thread | Analysis + Test |
|REQ-HFPX-WPS-003|Verification of propulsion software shall be defined per the VVP thread (verification approach TBD).|SYS-002; WDP/WSA tier; VVP thread|Inspection|
| REQ-HFPX-WPS-004 | The propulsion software scope shall observe an analysis-only boundary where propulsion is involved (boundary TBD). | SYS-002; WDP/WSA tier; VVP thread | Inspection |

Software assurance is structured according to DO-178C concepts; no compliance is claimed at this stage and no integrity or DAL-equivalent values are stated.

## 7. Architecture

Propulsion software resides in the application/services layers defined by HFPX-ARC-SW-001 (allocation TBD). Engine-control and limit-protection partitions, redundancy, and determinism treatment are TBD. Advisory or adaptive functions, if present, are segregated and never silently override pilot or safety authority. Languages, RTOS selection, and partitioning mechanisms are TBD.

## 8. Detailed Design

Not applicable at this revision. Software requirements, design descriptions, algorithms, and code are deferred to later Vol 16 detail. No implementation, logic, or parameter values stated.

## 9. Interfaces

Software interfaces to propulsion hardware services, sensor/actuator APIs, bus and logging services, and mode/health signalling are TBD. Signatures, timing, and protocols are TBD and will be detailed in software ICDs and Vol 04.9.

## 10. Operational Concept

Propulsion software operates across power-up, flight-mode, degraded-mode, and maintenance states (behaviour per state TBD). Limit protection remains governed by defined authority and annunciation chains (TBD). Advisory output, if any, is display and logging only.

## 11. Safety

Propulsion software safety inputs, hazard contributions, and independence provisions feed Vol 13 analyses (all TBD). No integrity values stated. Determinism, boundedness, and partition independence remain architecture constraints per HFPX-ARC-SW-001.

## 12. Performance

Timing, memory, and throughput budgets for propulsion software are TBD. Budget holders: software/compute (Vol 16/08), propulsion (Vol 04). No values stated.

## 13. Verification & Validation

Verified by inspection (requirements and architecture placement) and analysis plus test (limit-protection behaviour), structured according to DO-178C concepts with no compliance claimed. Detailed verification cases, environments (SIL/HIL), and flight-test hooks are TBD per the VVP thread and Vol 19/22/23.

## 14. Risks

- Engine-control functional scope creep ahead of Vol 04.9 maturity; mitigation: TBD-gated requirement WPS-001.
- Limit-protection incompleteness; mitigation: analysis and test requirement WPS-002 with Vol 13 review.
- Verification approach undefined; mitigation: VVP-thread planning requirement WPS-003.

## 15. Open Issues

Engine-control function inventory per Vol 04.9 TBD. Limit values and protection responses TBD. Verification approach and environments TBD. Analysis-only boundary definition TBD.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on Vol 04 propulsion definition (notably Vol 04.9), software architecture layering (HFPX-ARC-SW-001), control and health interfaces (Vol 07/16), safety analyses (Vol 13), and VVP planning (Vol 22/23).

## 18. Traceability

Parents: SYS-002 thread; WDP/WSA tier; VVP thread. Children: subsystem software requirements, design descriptions, ICDs, V&V cases (all TBD). RTM: REQ-HFPX-WPS-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Chapter 16.10.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 16.10) |
