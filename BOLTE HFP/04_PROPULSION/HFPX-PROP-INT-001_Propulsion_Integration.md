# Propulsion Integration

**Document ID:** HFPX-PROP-INT-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define propulsion integration requirements, architecture, interfaces and verification scaffolding (Chapter 04.16). Establishes structure only; interface ownership, registers, test-procedure ownership and change control are TBD.

## 2. Scope

Limited to requirements, architecture, interfaces, test methodology and safety analysis for airframe/propulsion integration.

> **Hazardous-subsystem boundary.** This document is limited to requirements, architecture, interfaces, test methodology and safety analysis ONLY. It contains NO build, ignition, fuel-test or operation instructions outside controlled conditions.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (notably REQ-HFPX-SYS-001, REQ-HFPX-SYS-003)
- HFPX-ARC-PRP-001 Propulsion Architecture (P-MECH/P-FUEL/P-PWR/P-THM/P-CMD/P-HLTH boundaries)
- PRQ/PAR tier propulsion requirements (TBD)
- Vol 03.6 — airframe/propulsion interface ownership
- Vol 21.3 / Vol 21.13 — interface and integration-test procedure ownership
- Vol 13 — safety analyses (SFA/CCA/FTA hooks)
- Vol 21 — V&V, including VVP-004

## 4. Definitions & Acronyms

- Interface ownership: assigned authority for defining and approving an interface (Vol 03.6, Vol 21.3).
- Interface register: controlled list of fuel/electrical/data interfaces (content TBD).
- Integration-test procedures: procedures proving combined airframe/propulsion behaviour (ownership Vol 21.13, procedures TBD).
- VVP-004: applicable verification planning reference.

## 5. System Context

Propulsion integration binds propulsion modules to airframe structure, fuel, electrical, data, thermal and control neighbours under owned interfaces and gated integration testing.

> **Hazardous-subsystem boundary.** This context describes requirements and architectural boundaries only. No build, ignition, fuel-test or operation instructions are provided.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-PIT-001 | Airframe/propulsion interface ownership shall be defined (Vol 03.6, Vol 21.3). | REQ-HFPX-SYS-001 | Inspection |
| REQ-HFPX-PIT-002 | A fuel/electrical/data interface register for propulsion integration shall be defined (content TBD). | REQ-HFPX-SYS-001, REQ-HFPX-SYS-003 | Inspection |
| REQ-HFPX-PIT-003 | Integration-test procedures ownership shall be defined (Vol 21.13; procedures TBD). | VVP-004 | Inspection |
| REQ-HFPX-PIT-004 | Changes to owned propulsion interfaces shall follow the interface-change rule (rule TBD; no unapproved change). | REQ-HFPX-SYS-003 | Inspection |

## 7. Architecture

Integration architecture (structure only): PROPULSION (TBD) ↔ OWNED INTERFACES [mechanical | fuel | electrical | data | thermal | command/health] (Vol 03.6/21.3, TBD) ↔ AIRFRAME/NEIGHBOUR SYSTEMS → INTEGRATION TEST (Vol 21.13, TBD).

> **Hazardous-subsystem boundary.** Architecture defines requirements and interfaces only, not build, installation, ignition or operating procedures.

## 8. Detailed Design

Not applicable at CONCEPT. Mounting detail, routing, connector selections and installation designs are TBD and deferred. No design values stated.

## 9. Interfaces

Integration interfaces: I-MECH (mounts/loads), I-FUEL, I-PWR (electrical), I-DATA (command/health), I-THM (thermal). Each entry TBD in the interface register and owned ICDs.

> **Hazardous-subsystem boundary.** Interface definitions describe architectural boundaries and analysis inputs only, not build/ignition/fuel-test/operation procedures.

## 10. Operational Concept

Integration is proven under controlled conditions through owned integration-test procedures; installation and mating concepts are TBD. No operating instructions are provided.

## 11. Safety

Interface mismatches, uncontrolled changes and integration escapes feed Vol 13 SFA/CCA/FTA. Change-control integrity claims are TBD. Analysis only; no operating instructions.

> **Hazardous-subsystem boundary.** Safety discussion is limited to requirements and analysis hooks. No build, ignition, fuel-test or operation instructions are provided.

## 12. Performance

Interface-completeness and integration-correctness budgets are TBD. Budget holder: this document with Vol 03.6/21.3. No values stated.

## 13. Verification & Validation

Verified by inspection (ownership, register, change rule per VVP-004) with later integration test under controlled conditions per Vol 21.13. Test methodology only; no operational procedures.

## 14. Risks

- Interface ownership/register TBDs leave mismatches undetected; mitigation: ownership fixed to Vol 03.6/21.3 with explicit TBDs.
- Uncontrolled interface change; mitigation: interface-change rule with no unapproved change.

## 15. Open Issues

Interface ownership allocations, register content, Vol 21.13 procedure set, and interface-change rule wording are all TBD.

## 16. Assumptions

- A-TBD-INT-01: Vol 03.6 and Vol 21.3 can host airframe/propulsion interface ownership; validation: Vol 03/21 review.
- A-TBD-INT-02: Vol 21.13 can host integration-test procedure ownership; validation: Vol 21 review.

## 17. Dependencies

Depends on SyRS SYS-001/003, ARC-PRP-001, PRQ/PAR tier, Vol 03.6, Vol 21.3/21.13, Vol 13 SFA/CCA/FTA, and Vol 21 VVP-004.

## 18. Traceability

Parents: PRQ/PAR tier (TBD); REQ-HFPX-SYS-001, REQ-HFPX-SYS-003; ARC-PRP-001 boundaries; SFA/CCA/FTA hooks (Vol 13); VVP-004. Children: owned ICDs, interface register, Vol 21.13 test evidence. RTM: REQ-HFPX-PIT-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 4 draft, not baselined. Chapter 04.16.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (Chapter 04.16) |
