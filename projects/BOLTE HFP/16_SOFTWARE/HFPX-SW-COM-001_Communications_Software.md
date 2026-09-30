# Communications Software

**Document ID:** HFPX-SW-COM-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X communications software scope (Chapter 16.13): protocol implementation, loss-of-link behaviour, security hooks, and verification planning. No implementation stated.

## 2. Scope

Covers communications software requirements, stack placement, interfaces, and verification planning. Protocol detail is TBD per Vol 11, including loss-of-link detail per Vol 11.9. Excludes communications hardware and spectrum matters (Vol 11), security design detail (Vol 17), and ground-station functions (Chapter 16.15).

## 3. Applicable Documents

- Parent requirements: SYS-002 thread; WDP/WSA tier; VVP thread
- HFPX-ARC-SW-001 Software Architecture (layering, determinism policy, assurance structured according to DO-178C concepts)
- Vol 11 communications definition, notably Vol 11.9 (loss-of-link, TBD)
- Vol 17 security hooks (TBD); Vol 16 sibling software chapters
- DO-178C concepts (structured-according-to only, no compliance claimed at this stage)

## 4. Definitions & Acronyms

- Protocol implementation: software realisation of communications protocols defined in Vol 11 (protocols TBD).
- Loss of link: condition in which defined communications connectivity is unavailable (criteria and responses TBD per Vol 11.9).
- Security hooks: interfaces by which communications software supports Vol 17 security provisions (mechanisms TBD).

## 5. System Context

Communications software executes within the platform/services layers defined by HFPX-ARC-SW-001 and interfaces with flight software, ground-control software, health and fault services, and logging. It receives transmit requests and link inputs and produces received data, link status, and log outputs across applicable states (states and signals TBD).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-WCM-001 | The communications software shall implement protocols as defined in Vol 11 (protocols TBD). | SYS-002; WDP/WSA tier; VVP thread | Inspection + Test |
| REQ-HFPX-WCM-002 | The communications software shall implement loss-of-link behaviour as defined in Vol 11.9 (criteria and responses TBD). | SYS-002; WDP/WSA tier; VVP thread | Analysis + Test |
| REQ-HFPX-WCM-003 | The communications software shall provide security hooks as defined in Vol 17 (mechanisms TBD). | SYS-002; WDP/WSA tier; VVP thread | Inspection |
|REQ-HFPX-WCM-004|Verification of communications software shall be defined per the VVP thread (verification approach TBD).|SYS-002; WDP/WSA tier; VVP thread|Inspection|

Software assurance is structured according to DO-178C concepts; no compliance is claimed at this stage and no integrity values are stated.

## 7. Architecture

Communications software resides in the platform/services layers defined by HFPX-ARC-SW-001 (allocation TBD). Protocol stacks, link supervision, buffering, and security-hook integration are partitioned per determinism and independence policy (TBD). Languages, RTOS selection, stacks, and partitioning mechanisms are TBD.

## 8. Detailed Design

Not applicable at this revision. Software requirements, design descriptions, state machines, and code are deferred to later Vol 16 detail. No implementation, logic, or parameter values stated.

## 9. Interfaces

Software interfaces to Vol 11 link services, flight and ground applications, security services (Vol 17), and logging services are TBD. Signatures, timing, message formats, and protocols are TBD and will be detailed in software ICDs and Vol 11.

## 10. Operational Concept

Communications software operates across power-up, flight-mode, degraded-mode (including loss of link), and maintenance states (behaviour per state TBD). Link supervision, fallback behaviour, and re-establishment sequencing are TBD per Vol 11.9.

## 11. Safety

Communications software safety inputs, hazard contributions (including loss-of-link and corrupted-data considerations), and independence provisions feed Vol 13 analyses (all TBD). No integrity values stated. Determinism, boundedness, and partition independence remain architecture constraints per HFPX-ARC-SW-001.

## 12. Performance

Timing (latency, jitter), throughput, buffering, and resource budgets for communications software are TBD. Budget holders: software/compute (Vol 16/08), communications (Vol 11). No values stated.

## 13. Verification & Validation

Verified by inspection and test (protocols, security hooks) and analysis plus test (loss-of-link behaviour), structured according to DO-178C concepts with no compliance claimed. Detailed verification cases, link-test environments, and flight-test hooks are TBD per the VVP thread and Vol 19/22/23.

## 14. Risks

- Protocol drift ahead of Vol 11 maturity; mitigation: TBD-gated requirement WCM-001.
- Undefined loss-of-link behaviour; mitigation: Vol 11.9 behaviour requirement WCM-002.
- Security-hook gaps; mitigation: Vol 17 hook requirement WCM-003 with security review.

## 15. Open Issues

Protocol set per Vol 11 TBD. Loss-of-link criteria, responses, and re-establishment per Vol 11.9 TBD. Security-hook mechanisms per Vol 17 TBD. Verification approach and environments TBD.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on Vol 11 communications definition (notably Vol 11.9), Vol 17 security provisions, software architecture layering (HFPX-ARC-SW-001), ground-control coordination (Chapter 16.15), safety analyses (Vol 13), and VVP planning (Vol 22/23).

## 18. Traceability

Parents: SYS-002 thread; WDP/WSA tier; VVP thread. Children: subsystem software requirements, design descriptions, ICDs, V&V cases (all TBD). RTM: REQ-HFPX-WCM-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Chapter 16.13.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 16.13) |
