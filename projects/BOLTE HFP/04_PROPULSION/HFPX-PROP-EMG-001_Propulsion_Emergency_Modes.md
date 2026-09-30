# Propulsion Emergency Modes

**Document ID:** HFPX-PROP-EMG-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define propulsion emergency-mode requirements, architecture, interfaces and verification scaffolding (Chapter 04.15). Establishes structure only; mode set, entry/exit criteria, authority and fault-injection verification are TBD.

## 2. Scope

Limited to requirements, architecture, interfaces, test methodology and safety analysis for propulsion emergency modes.

> **Hazardous-subsystem boundary.** This document is limited to requirements, architecture, interfaces, test methodology and safety analysis ONLY. It contains NO build, ignition, fuel-test or operation instructions outside controlled conditions.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (notably REQ-HFPX-SYS-001, REQ-HFPX-SYS-003)
- HFPX-ARC-PRP-001 Propulsion Architecture (notably REQ-HFPX-PRP-004)
- PRQ/PAR tier propulsion requirements (TBD)
- HFPX-PROP-FLT-001 (fault-detection source), HFPX-PROP-RDY-001 (redundancy context)
- Vol 13 — safety analyses (SFA/CCA/FTA hooks)
- Vol 21 — V&V, including VVP-004

## 4. Definitions & Acronyms

- Emergency-mode set: defined degraded/protective propulsion behaviours (set TBD).
- Mode-entry/exit criteria: conditions governing transitions into and out of emergency modes (TBD).
- Safety computer: candidate authority for emergency-mode decisions (TBD).
- Fault-injection test: verification by injecting faults under controlled conditions (procedures TBD).

## 5. System Context

Emergency modes receive fault declarations, arbitrate protective propulsion behaviour under defined authority, and coordinate with redundancy, monitoring and safety views.

> **Hazardous-subsystem boundary.** This context describes requirements and architectural boundaries only. No build, ignition, fuel-test or operation instructions are provided.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-PEM-001 | The propulsion system shall define the emergency-mode set (set TBD). | REQ-HFPX-SYS-001, REQ-HFPX-PRP-004 | Inspection |
| REQ-HFPX-PEM-002 | Mode-entry and mode-exit criteria for each emergency mode shall be defined (criteria TBD). | REQ-HFPX-SYS-003 | Analysis |
| REQ-HFPX-PEM-003 | Emergency-mode authority shall be defined (safety computer TBD). | REQ-HFPX-SYS-003, REQ-HFPX-PRP-004 | Inspection |
| REQ-HFPX-PEM-004 | Emergency modes shall be verified by fault-injection test under controlled conditions (procedures and criteria TBD). | VVP-004 | Test |

## 7. Architecture

Emergency-mode architecture (structure only): FAULT INPUTS (from 04.14, TBD) → MODE ARBITRATION under defined authority (safety computer TBD) → EMERGENCY BEHAVIOURS (set TBD) → EXIT/RECOVERY (criteria TBD).

> **Hazardous-subsystem boundary.** Architecture defines requirements and interfaces only, not build, installation, ignition or operating procedures.

## 8. Detailed Design

Not applicable at CONCEPT. Mode logic, arbitration implementation and recovery designs are TBD and deferred. No design values stated.

## 9. Interfaces

Emergency-mode interfaces: E-FLT (fault inputs), E-AUTH (authority interface to safety computer, TBD), E-CMD (emergency commands to propulsion), E-ANN (annunciation of mode state). Definitions TBD in ICDs.

> **Hazardous-subsystem boundary.** Interface definitions describe architectural boundaries and analysis inputs only, not build/ignition/fuel-test/operation procedures.

## 10. Operational Concept

Emergency modes are reasoned for controlled ground testing and (later) flight phases; sequencing and recovery concepts are TBD. No operating instructions are provided.

## 11. Safety

Wrong-mode, missed-mode and stuck-in-mode hazards feed Vol 13 SFA/CCA/FTA. Authority independence and integrity claims are TBD. Analysis only; no operating instructions.

> **Hazardous-subsystem boundary.** Safety discussion is limited to requirements and analysis hooks. No build, ignition, fuel-test or operation instructions are provided.

## 12. Performance

Mode coverage and transition-correctness budgets are TBD. Budget holder: this document (REQ-HFPX-PEM-001..003). No values stated.

## 13. Verification & Validation

Verified by inspection (mode set, authority per VVP-004), analysis (entry/exit criteria) and fault-injection test under controlled conditions (TBD). Test methodology only; no operational procedures.

## 14. Risks

- Mode-set and authority TBDs leave protective behaviour unproven; mitigation: structure-only requirements with explicit TBDs and safety-path review.
- Fault-injection fidelity TBD; mitigation: gated controlled-conditions test before any credit.

## 15. Open Issues

Emergency-mode set, entry/exit criteria, safety-computer authority, and fault-injection test procedures/criteria are all TBD.

## 16. Assumptions

- A-TBD-EMG-01: Fault detection can supply mode-entry inputs; validation: HFPX-PROP-FLT-001 review.
- A-TBD-EMG-02: A safety computer may host emergency-mode authority; validation: safety architecture review.

## 17. Dependencies

Depends on SyRS SYS-001/003, ARC-PRP-001, PRQ/PAR tier, HFPX-PROP-FLT-001/RDY-001, Vol 13 SFA/CCA/FTA, and Vol 21 VVP-004.

## 18. Traceability

Parents: PRQ/PAR tier (TBD); REQ-HFPX-SYS-001, REQ-HFPX-SYS-003; REQ-HFPX-PRP-004; SFA/CCA/FTA hooks (Vol 13); VVP-004. Children: detailed mode logic, authority ICDs, fault-injection evidence. RTM: REQ-HFPX-PEM-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 4 draft, not baselined. Chapter 04.15.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (Chapter 04.15) |
