# Propulsion Ground Testing

**Document ID:** HFPX-PROP-GND-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define propulsion ground-testing requirements, architecture, interfaces and verification scaffolding (Chapter 04.17). Establishes structure only; test thread, pass/fail criteria, data capture and flight-credit rules are TBD.

## 2. Scope

Limited to requirements, architecture, interfaces, test methodology and safety analysis for propulsion ground testing under controlled conditions.

> **Hazardous-subsystem boundary.** This document is limited to requirements, architecture, interfaces, test methodology and safety analysis ONLY. It contains NO build, ignition, fuel-test or operation instructions outside controlled conditions.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (notably REQ-HFPX-SYS-001, REQ-HFPX-SYS-003)
- HFPX-ARC-PRP-001 Propulsion Architecture
- PRQ/PAR tier propulsion requirements (TBD)
- HFPX-PROP-INS-001 / MON-001 / THM-001 / FLT-001 / EMG-001 (test subjects and data sources)
- Vol 13 — safety analyses (SFA/CCA/FTA hooks)
- Vol 21 — V&V, including VVP-004

## 4. Definitions & Acronyms

- Ground-test thread: bench → rig → integrated progression under controlled conditions (procedures TBD).
- Pass/fail criteria: conditions determining test success (criteria TBD).
- Data capture: recording of test data for evaluation and traceability (provisions TBD).
- Test-to-flight-credit rule: gate prohibiting flight credit without gated evidence.
- VVP-004: applicable verification planning reference.

## 5. System Context

Ground testing exercises propulsion articles from bench through rig to integrated configurations under controlled conditions, capturing data to gate any future flight credit without authorising flight itself.

> **Hazardous-subsystem boundary.** This context describes requirements and test methodology only. No build, ignition, fuel-test or operation instructions outside controlled conditions are provided.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-PGT-001 | The programme shall define the propulsion ground-test thread from bench to rig to integrated configurations under controlled conditions (procedures TBD). | REQ-HFPX-SYS-003, VVP-004 | Inspection |
| REQ-HFPX-PGT-002 | Pass/fail criteria for each ground-test stage shall be defined (criteria TBD). | REQ-HFPX-SYS-003 | Inspection |
| REQ-HFPX-PGT-003 | Data-capture provisions for ground testing shall be defined (scope and retention TBD). | REQ-HFPX-SYS-003, VVP-004 | Inspection |
| REQ-HFPX-PGT-004 | No flight credit shall be claimed from ground testing without gated evidence (gate TBD). | REQ-HFPX-SYS-001, REQ-HFPX-SYS-003 | Inspection |

## 7. Architecture

Test architecture (structure only): BENCH (TBD) → RIG (TBD) → INTEGRATED ARTICLE under controlled conditions (TBD) → DATA CAPTURE (TBD) → GATE REVIEW (no flight credit without gated evidence).

> **Hazardous-subsystem boundary.** Architecture defines test methodology and gates only, not build, ignition, fuel-test or operating procedures.

## 8. Detailed Design

Not applicable at CONCEPT. Rig designs, article configurations, facility provisions and detailed procedures are TBD and deferred. No design values stated.

## 9. Interfaces

Test interfaces: G-ART (article under test), G-RIG (rig/facility boundary), G-DATA (data-capture interface), G-GATE (evidence-to-gate interface to Vol 21). Definitions TBD.

> **Hazardous-subsystem boundary.** Interface definitions describe test-methodology boundaries and analysis inputs only, not build/ignition/fuel-test/operation procedures.

## 10. Operational Concept

Ground testing is conducted only under controlled conditions with TBD safety controls and procedures; it does not authorise flight operations. Concepts for sequencing and safety interlocks are TBD.

## 11. Safety

Test hazards, article failures and test escapes feed Vol 13 SFA/CCA/FTA and facility safety reviews. Controls are TBD and subject to approval before any testing. Analysis only; no operating instructions.

> **Hazardous-subsystem boundary.** Safety discussion is limited to requirements and analysis hooks. No build, ignition, fuel-test or operation instructions outside controlled conditions are provided.

## 12. Performance

Test coverage and data-completeness budgets are TBD. Budget holder: this document (REQ-HFPX-PGT-001..003) with Vol 21. No values stated.

## 13. Verification & Validation

Verified by inspection (thread definition, criteria, data-capture provisions and flight-credit gate per VVP-004). Test methodology only; execution awaits controlled-conditions approval with no flight credit implied.

## 14. Risks

- Undefined thread/criteria/data capture leaves evidence ungated; mitigation: structure-only requirements with explicit TBDs and VVP-004 gating.
- Premature flight credit from incomplete ground evidence; mitigation: test-to-flight-credit rule prohibiting credit without gated evidence.

## 15. Open Issues

Ground-test thread procedures, stage pass/fail criteria, data-capture scope/retention, and flight-credit gate definition are all TBD.

## 16. Assumptions

- A-TBD-GND-01: Bench → rig → integrated progression is stable scaffolding; validation: Vol 21 review.
- A-TBD-GND-02: Vol 21 can host gate criteria for test-to-flight credit; validation: Vol 21 review.

## 17. Dependencies

Depends on SyRS SYS-001/003, ARC-PRP-001, PRQ/PAR tier, HFPX-PROP-INS/MON/THM/FLT/EMG-001 inputs, Vol 13 SFA/CCA/FTA, and Vol 21 VVP-004.

## 18. Traceability

Parents: PRQ/PAR tier (TBD); REQ-HFPX-SYS-001, REQ-HFPX-SYS-003; ARC-PRP-001; SFA/CCA/FTA hooks (Vol 13); VVP-004. Children: detailed test plans/procedures, data-capture implementations, gate evidence. RTM: REQ-HFPX-PGT-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 4 draft, not baselined. Chapter 04.17.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (Chapter 04.17) |
