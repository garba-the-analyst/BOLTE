# Redundancy

**Document ID:** HFPX-AVN-RDY-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define avionics redundancy requirements, architecture, interfaces and verification scaffolding (Chapter 08.14). Establishes structure only; redundancy approach, independence, verification and FTA flow are TBD and unproven.

## 2. Scope

Covers avionics redundancy approach, channel and voting provisions, independence evidence, verification methodology and flow into fault-tree analysis. Fault detection, recovery execution and quantitative availability claims are excluded (owned by Ch 08.11/08.13 and Vol 13). Channel counts, voting logic, switchover provisions and coverage values are TBD. No numeric values are allocated in this document.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (notably REQ-HFPX-SYS-002, REQ-HFPX-SYS-003, REQ-HFPX-SYS-005)
- HFPX-ARC-AVN-001 Avionics Architecture
- VAA tier requirements (TBD)
- Vol 13 — safety analyses (notably FTA, CCA hooks)

## 4. Definitions & Acronyms

- Redundancy approach: means by which avionics tolerates element/path loss; approach TBD, capability unproven.
- Channels: redundant avionics paths or lanes; counts and allocation TBD.
- Voting: comparison/selection among redundant channels; logic TBD.
- Independence: separation of redundant paths against common cause; claims TBD, CCA hooks.
- FTA flow: allocation of redundancy claims into fault-tree analysis (Vol 13); gates TBD.
- TBD: To Be Determined.

## 5. System Context

Avionics redundancy spans compute, sensing-input, data-path and power-feed provisions, interfacing to fault detection/recovery, health monitoring and safety analyses to argue tolerance of defined failures. Redundancy claims are unproven at CONCEPT and require gated analysis and test before any credit.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-VRD-001 | The avionics redundancy approach, including channels and voting provisions, shall be defined; channels TBD, voting TBD. | REQ-HFPX-SYS-002, REQ-HFPX-SYS-003 | Inspection |
| REQ-HFPX-VRD-002 | Independence of redundant avionics paths shall be evidenced; claims TBD with CCA hooks. | REQ-HFPX-SYS-003, CCA hook | Analysis |
| REQ-HFPX-VRD-003 | Redundancy claims shall be verified; method and criteria TBD. | VAA tier | Analysis / Test |
| REQ-HFPX-VRD-004 | Redundancy claims shall flow into FTA; allocation and gates TBD (Vol 13). | REQ-HFPX-SYS-005, SFA hook | Analysis |

## 7. Architecture

Redundancy architecture (structure only): REDUNDANT CHANNELS (counts TBD) with VOTING PROVISIONS (logic TBD) and INDEPENDENCE PROVISIONS (CCA hooks, TBD) → FAULT COVERAGE (via Ch 08.11/08.13, TBD) → FTA ALLOCATION (Vol 13, TBD).

## 8. Detailed Design

Not applicable at CONCEPT. Channel implementations, cross-strapping, voting logic, switchover provisions and independence implementations are TBD and deferred. No design values stated.

## 9. Interfaces

Redundancy interfaces: R-CH (inter-channel boundaries), R-VOT (voting provisions), R-IND (independence provisions), R-FLT (to fault detection/recovery), R-FTA (to Vol 13 FTA). Definitions TBD in ICDs.

## 10. Operational Concept

Redundancy behaviour is reasoned across all avionics operating states including degraded modes; degraded-mode concepts are TBD. No operating values are stated.

## 11. Safety

Loss-of-redundancy, common-cause and voting hazards feed Vol 13 SFA/CCA/FTA. Channel-out capability is explicitly unproven at CONCEPT. Analysis only; REQ-HFPX-VRD-002 (independence with CCA hooks) and REQ-HFPX-VRD-004 (FTA flow) bound claims pending evidence.

## 12. Performance

Redundancy coverage and independence margins are TBD. Budget holder: this document (REQ-HFPX-VRD-001..002) with Vol 13. No values stated.

## 13. Verification & Validation

Verified by inspection (approach definition) and analysis/test (independence and redundancy claims, TBD) per VAA tier and Vol 13 hooks. Cases trace to REQ-HFPX-VRD-001..004; methods and acceptance criteria TBD. No gate skipping.

## 14. Risks

- Channel-out capability unproven; mitigation: explicit unproven status with gated analysis/test before any credit.
- Common-cause dependence collapsing redundancy claims; mitigation: CCA hooks and independence evidence per REQ-HFPX-VRD-002.
- Voting faults masking or inducing failures; mitigation: defined voting provisions with FTA allocation.

## 15. Open Issues

Redundancy approach, channels and voting, independence claims and CCA evidence, verification method/criteria, and redundancy-to-FTA allocation are all TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SyRS SYS-002/003/005, VAA tier, fault detection/recovery (08.11/08.13), Vol 13 FTA/CCA including SFA hooks.

## 18. Traceability

Parents: REQ-HFPX-SYS-002, REQ-HFPX-SYS-003, REQ-HFPX-SYS-005; VAA tier; SFA/CCA hooks. Children: detailed redundancy design, FTA/CCA evidence, integration ICDs, V&V evidence (all TBD). RTM: REQ-HFPX-VRD-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 5 draft, not baselined. Chapter 08.14.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 draft (Chapter 08.14) |
