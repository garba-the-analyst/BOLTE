# Engine Thermal Management

**Document ID:** HFPX-PROP-THM-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define engine thermal-management requirements, architecture, interfaces and verification scaffolding for HFP-X propulsion (Chapter 04.12). Establishes structure only; heat-rejection paths, limits, protection provisions and verification details are TBD.

## 2. Scope

Limited to requirements, architecture, interfaces, test methodology and safety analysis for propulsion thermal management.

> **Hazardous-subsystem boundary.** This document is limited to requirements, architecture, interfaces, test methodology and safety analysis ONLY. It contains NO build, ignition, fuel-test or operation instructions outside controlled conditions.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (notably REQ-HFPX-SYS-001, REQ-HFPX-SYS-003)
- HFPX-ARC-PRP-001 Propulsion Architecture (notably REQ-HFPX-PRP-003)
- PRQ/PAR tier propulsion requirements (TBD)
- Vol 14.2 / Vol 14.3 — pilot / structure thermal protection
- Vol 13 — safety analyses (SFA/CCA/FTA hooks)
- Vol 21 — V&V, including VVP-004

## 4. Definitions & Acronyms

- Heat-rejection paths: routes by which propulsion heat is rejected to environment or sinks (set TBD).
- Temperature limits: allowable thermal envelopes for propulsion hardware and neighbours (values TBD).
- Thermal protection: provisions protecting pilot and structure from propulsion heat (design TBD, Vol 14.2/14.3).
- VVP-004: applicable verification planning reference.

## 5. System Context

Thermal management constrains propulsion heat within hardware, pilot and structure limits across ground-test and (later) flight environments, interfacing to airframe, thermal and safety views.

> **Hazardous-subsystem boundary.** This context describes requirements and architectural boundaries only. No build, ignition, fuel-test or operation instructions are provided.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-PTH-001 | The propulsion system shall define heat-rejection paths for engine thermal management (set TBD). | REQ-HFPX-SYS-001, REQ-HFPX-PRP-003 | Inspection |
| REQ-HFPX-PTH-002 | Temperature limits for propulsion hardware and interfaces shall be defined (values TBD). | REQ-HFPX-SYS-003 | Analysis |
| REQ-HFPX-PTH-003 | Thermal protection of pilot and structure from propulsion heat shall be defined (provisions TBD, Vol 14.2/14.3). | REQ-HFPX-SYS-001, REQ-HFPX-SYS-003 | Analysis |
| REQ-HFPX-PTH-004 | Thermal management shall be verified by thermal model and test (models, rigs and criteria TBD). | VVP-004 | Analysis / Test |

## 7. Architecture

Thermal architecture (structure only): HEAT SOURCES (TBD) → REJECTION PATHS (TBD) → SINKS/ENVIRONMENT (TBD) → PROTECTION PROVISIONS for pilot/structure (Vol 14.2/14.3, TBD) → MONITORING HOOKS (limits TBD).

> **Hazardous-subsystem boundary.** Architecture defines requirements and interfaces only, not build, installation, ignition or operating procedures.

## 8. Detailed Design

Not applicable at CONCEPT. Materials, insulation, ducting, sinks and protection implementations are TBD and deferred. No design values stated.

## 9. Interfaces

Thermal interfaces: T-SRC (source boundaries), T-REJ (rejection-path boundaries), T-PROT (pilot/structure protection interfaces per Vol 14.2/14.3), T-MON (thermal monitoring hooks). Definitions TBD in ICDs.

> **Hazardous-subsystem boundary.** Interface definitions describe architectural boundaries and analysis inputs only, not build/ignition/fuel-test/operation procedures.

## 10. Operational Concept

Thermal behaviour is evaluated across controlled ground testing and (later) flight phases; warm-up, sustained-operation and cool-down concepts are TBD. No operating instructions are provided.

## 11. Safety

Over-temperature hazards, protection failures and thermal propagation feed Vol 13 SFA/CCA/FTA. Protection integrity claims are TBD. Analysis only; no operating instructions.

> **Hazardous-subsystem boundary.** Safety discussion is limited to requirements and analysis hooks. No build, ignition, fuel-test or operation instructions are provided.

## 12. Performance

Heat-rejection budgets, temperature envelopes and protection margins are TBD. Budget holders: this document with Vol 14.2/14.3. No values stated.

## 13. Verification & Validation

Verified by analysis (thermal model, TBD) and test under controlled conditions (criteria TBD) per VVP-004 and Vol 21. Test methodology only; no operational procedures.

## 14. Risks

- Heat-rejection and limit TBDs leave hardware and occupant safety unproven; mitigation: structure-only requirements with explicit TBDs and Vol 14.2/14.3 review.
- Model/test fidelity TBD; mitigation: gated thermal-model-plus-test verification rule.

## 15. Open Issues

Heat-rejection path set, temperature limits, pilot/structure protection provisions (Vol 14.2/14.3), and thermal model/test definitions are all TBD.

## 16. Assumptions

- A-TBD-THM-01: Thermal-model-plus-test is an acceptable verification thread; validation: Vol 21 review.
- A-TBD-THM-02: Vol 14.2/14.3 can host pilot/structure thermal-protection ownership; validation: Vol 14 review.

## 17. Dependencies

Depends on SyRS SYS-001/003, ARC-PRP-001, PRQ/PAR tier, Vol 14.2/14.3 protection views, Vol 13 SFA/CCA/FTA, and Vol 21 VVP-004.

## 18. Traceability

Parents: PRQ/PAR tier (TBD); REQ-HFPX-SYS-001, REQ-HFPX-SYS-003; REQ-HFPX-PRP-003; SFA/CCA/FTA hooks (Vol 13); VVP-004. Children: detailed thermal design, Vol 14.2/14.3 provisions, integration ICDs, V&V evidence. RTM: REQ-HFPX-PTH-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 4 draft, not baselined. Chapter 04.12.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (Chapter 04.12) |
