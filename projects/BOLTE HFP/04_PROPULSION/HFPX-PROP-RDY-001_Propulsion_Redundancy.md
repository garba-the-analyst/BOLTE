# Propulsion Redundancy

**Document ID:** HFPX-PROP-RDY-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define propulsion redundancy requirements, architecture, interfaces and verification scaffolding (Chapter 04.13). Establishes structure only; redundancy approach, independence, verification and FTA flow are TBD and unproven.

## 2. Scope

Limited to requirements, architecture, interfaces, test methodology and safety analysis for propulsion redundancy.

> **Hazardous-subsystem boundary.** This document is limited to requirements, architecture, interfaces, test methodology and safety analysis ONLY. It contains NO build, ignition, fuel-test or operation instructions outside controlled conditions.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (notably REQ-HFPX-SYS-001, REQ-HFPX-SYS-003)
- HFPX-ARC-PRP-001 Propulsion Architecture (notably REQ-HFPX-PRP-004)
- PRQ/PAR tier propulsion requirements (TBD)
- Vol 13 — safety analyses (notably FTA, CCA hooks)
- Vol 21 — V&V, including VVP-004

## 4. Definitions & Acronyms

- Redundancy approach: means by which propulsion tolerates module/path loss (approach TBD; module-out capability unproven).
- Independence: separation of redundant paths against common cause (claims TBD, CCA hooks).
- FTA flow: allocation of redundancy claims into fault-tree analysis (Vol 13).
- VVP-004: applicable verification planning reference.

## 5. System Context

Redundancy spans propulsion modules, distribution, control and monitoring paths, interfacing to fault detection, emergency modes and safety analyses to argue tolerance of defined failures.

> **Hazardous-subsystem boundary.** This context describes requirements and architectural boundaries only. No build, ignition, fuel-test or operation instructions are provided.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-PDY-001 | The propulsion system shall define the redundancy approach (scope TBD; module-out capability unproven). | REQ-HFPX-SYS-001, REQ-HFPX-PRP-004 | Inspection |
| REQ-HFPX-PDY-002 | Independence of redundant propulsion paths shall be defined (claims TBD, CCA hooks). | REQ-HFPX-SYS-003, REQ-HFPX-PRP-004 | Analysis |
| REQ-HFPX-PDY-003 | Redundancy claims shall be verified (method and criteria TBD). | VVP-004 | Analysis / Test |
| REQ-HFPX-PDY-004 | Redundancy claims shall flow into FTA (allocation and gates TBD, Vol 13). | REQ-HFPX-SYS-003, REQ-HFPX-PRP-004 | Analysis |

## 7. Architecture

Redundancy architecture (structure only): REDUNDANT PATHS (TBD) with INDEPENDENCE PROVISIONS (CCA hooks, TBD) → FAULT COVERAGE (via 04.14, TBD) → EMERGENCY MODES (via 04.15, TBD) → FTA ALLOCATION (Vol 13, TBD).

> **Hazardous-subsystem boundary.** Architecture defines requirements and interfaces only, not build, installation, ignition or operating procedures.

## 8. Detailed Design

Not applicable at CONCEPT. Redundant element counts, cross-strapping, switchover logic and independence implementations are TBD and deferred. No design values stated.

## 9. Interfaces

Redundancy interfaces: R-PATH (inter-path boundaries), R-IND (independence provisions), R-FLT (to fault detection), R-EMG (to emergency modes), R-FTA (to Vol 13 FTA). Definitions TBD in ICDs.

> **Hazardous-subsystem boundary.** Interface definitions describe architectural boundaries and analysis inputs only, not build/ignition/fuel-test/operation procedures.

## 10. Operational Concept

Redundancy behaviour is reasoned across controlled ground testing and (later) flight phases; degraded-mode concepts are TBD. No operating instructions are provided.

## 11. Safety

Loss-of-redundancy, common-cause and switchover hazards feed Vol 13 SFA/CCA/FTA. Module-out capability is explicitly unproven at CONCEPT. Analysis only; no operating instructions.

> **Hazardous-subsystem boundary.** Safety discussion is limited to requirements and analysis hooks. No build, ignition, fuel-test or operation instructions are provided.

## 12. Performance

Redundancy coverage and independence margins are TBD. Budget holder: this document (REQ-HFPX-PDY-001..002) with Vol 13. No values stated.

## 13. Verification & Validation

Verified by inspection (approach definition) and analysis/test (independence and redundancy claims, TBD) per VVP-004 and Vol 21 under controlled conditions. Test methodology only; no operational procedures.

## 14. Risks

- Module-out capability unproven; mitigation: explicit unproven status with gated analysis/test before any credit.
- Common-cause dependence collapsing redundancy claims; mitigation: CCA hooks and independence analysis.

## 15. Open Issues

Redundancy approach and scope, independence claims and CCA evidence, verification method/criteria, and redundancy-to-FTA allocation are all TBD.

## 16. Assumptions

- A-TBD-RDY-01: A redundant-path partition can be defined independent of final chain selection; validation: architecture review.
- A-TBD-RDY-02: Vol 13 FTA/CCA can host redundancy claims; validation: Vol 13 review.

## 17. Dependencies

Depends on SyRS SYS-001/003, ARC-PRP-001, PRQ/PAR tier, fault detection (04.14), emergency modes (04.15), Vol 13 FTA/CCA, and Vol 21 VVP-004.

## 18. Traceability

Parents: PRQ/PAR tier (TBD); REQ-HFPX-SYS-001, REQ-HFPX-SYS-003; REQ-HFPX-PRP-004; CCA/FTA hooks (Vol 13); VVP-004. Children: detailed redundancy design, FTA/CCA evidence, integration ICDs, V&V evidence. RTM: REQ-HFPX-PDY-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 4 draft, not baselined. Chapter 04.13.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (Chapter 04.13) |
