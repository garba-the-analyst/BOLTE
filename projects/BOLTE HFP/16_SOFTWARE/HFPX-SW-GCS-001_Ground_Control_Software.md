# Ground-Control Software

**Document ID:** HFPX-SW-GCS-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X ground-control software scope (Chapter 16.15): ground-station functions, command authority, verification, and release control. No implementation stated.

## 2. Scope

Covers ground-control software requirements, architecture placement, interfaces, and verification planning. Ground-station functional detail is TBD per Vol 11.10. Excludes airborne software detail (Chapters 16.3/16.4 and siblings), communications hardware (Vol 11), and security design detail (Vol 17).

## 3. Applicable Documents

- Parent requirements: SYS-002 thread; WDP/WSA tier; VVP thread
- HFPX-ARC-SW-001 Software Architecture (layering, determinism policy, assurance structured according to DO-178C concepts)
- Vol 11 ground-segment definition, notably Vol 11.10 (ground-station functions, TBD)
- Vol 16 sibling software chapters; Vol 13 safety inputs; Vol 17 security hooks
- DO-178C concepts (structured-according-to only, no compliance claimed at this stage)

## 4. Definitions & Acronyms

- Ground-station functions: software functions hosted at the ground station as defined in Vol 11.10 (functions TBD).
- Command authority: the permitted scope of ground-originated commands versus airborne authority (allocation TBD).
- Release rule: the criterion governing release of ground-control software to operational use (rule TBD).

## 5. System Context

Ground-control software executes on ground-segment computing paths and interfaces with communications software, airborne systems via defined links, health and logging services, and operator displays. It receives operator inputs and downlinked data and produces uplink commands, display outputs, and log outputs across applicable states (states and signals TBD).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-WGS-001 | The ground-control software shall implement ground-station functions as defined in Vol 11.10 (functions TBD). | SYS-002; WDP/WSA tier; VVP thread | Inspection |
| REQ-HFPX-WGS-002 | The ground-control software shall observe defined command authority limits for ground-originated commands (authority TBD). | SYS-002; WDP/WSA tier; VVP thread | Inspection + Analysis |
|REQ-HFPX-WGS-003|Verification of ground-control software shall be defined per the VVP thread (verification approach TBD).|SYS-002; WDP/WSA tier; VVP thread|Inspection|
| REQ-HFPX-WGS-004 | Release of ground-control software to operational use shall observe a defined release rule (rule TBD). | SYS-002; WDP/WSA tier; VVP thread | Inspection |

Software assurance is structured according to DO-178C concepts; no compliance is claimed at this stage and no integrity values are stated.

## 7. Architecture

Ground-control software is structured per HFPX-ARC-SW-001 layering adapted to ground-segment hosting (allocation TBD). Command generation, authority enforcement, display, and logging functions are partitioned per determinism and independence policy (TBD). Languages, operating environments, and tooling are TBD.

## 8. Detailed Design

Not applicable at this revision. Software requirements, design descriptions, command definitions, and code are deferred to later Vol 16 detail and Vol 11.10. No implementation, logic, or parameter values stated.

## 9. Interfaces

Software interfaces to communications links, operator displays, command-authority services, security services (Vol 17), and logging services are TBD. Signatures, timing, message formats, and protocols are TBD and will be detailed in software ICDs and Vol 11.10.

## 10. Operational Concept

Ground-control software operates across pre-flight, flight-support, degraded-link, and maintenance states (behaviour per state TBD). Command authority enforcement and handover between ground and airborne authority are TBD. Training and rehearsal modes are TBD.

## 11. Safety

Ground-control software safety inputs, hazard contributions (including unauthorised-command and authority-exceedance considerations), and independence provisions feed Vol 13 analyses (all TBD). No integrity values stated.

## 12. Performance

Timing (command latency, display refresh), throughput, and resource budgets for ground-control software are TBD. Budget holders: software/compute (Vol 16/08), ground segment (Vol 11). No values stated.

## 13. Verification & Validation

Verified by inspection (ground-station functions, release rule) and inspection plus analysis (command authority), structured according to DO-178C concepts with no compliance claimed. Detailed verification cases, ground-rig environments, and flight-test hooks are TBD per the VVP thread and Vol 19/22/23.

## 14. Risks

- Ground-station functional scope drift ahead of Vol 11.10 maturity; mitigation: TBD-gated requirement WGS-001.
- Command-authority exceedance; mitigation: authority-limit requirement WGS-002 with Vol 13 review.
- Uncontrolled release to operations; mitigation: release-rule requirement WGS-004 with Chapter 16.17 discipline.

## 15. Open Issues

Ground-station function set per Vol 11.10 TBD. Command authority allocation TBD. Verification approach and environments TBD. Release rule and approval workflow TBD.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on Vol 11 ground-segment definition (notably Vol 11.10), software architecture layering (HFPX-ARC-SW-001), communications software (Chapter 16.13), security provisions (Vol 17), configuration management (Chapter 16.17), safety analyses (Vol 13), and VVP planning (Vol 22/23).

## 18. Traceability

Parents: SYS-002 thread; WDP/WSA tier; VVP thread. Children: subsystem software requirements, design descriptions, ICDs, V&V cases (all TBD). RTM: REQ-HFPX-WGS-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Chapter 16.15.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 16.15) |
