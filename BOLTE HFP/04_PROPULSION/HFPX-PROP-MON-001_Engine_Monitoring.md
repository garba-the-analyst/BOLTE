# Engine Monitoring

**Document ID:** HFPX-PROP-MON-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define engine monitoring requirements, architecture, interfaces and verification scaffolding for HFP-X propulsion (Chapter 04.11). Establishes structure only; health parameters, limits, annunciation and recording provisions are TBD.

## 2. Scope

Limited to requirements, architecture, interfaces, test methodology and safety analysis for propulsion health monitoring.

> **Hazardous-subsystem boundary.** This document is limited to requirements, architecture, interfaces, test methodology and safety analysis ONLY. It contains NO build, ignition, fuel-test or operation instructions outside controlled conditions.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (notably REQ-HFPX-SYS-001, REQ-HFPX-SYS-003)
- HFPX-ARC-PRP-001 Propulsion Architecture (notably REQ-HFPX-PRP-003, REQ-HFPX-PRP-004)
- PRQ/PAR tier propulsion requirements (TBD)
- HFPX-PROP-INS-001 Engine Instrumentation (sensed-data source)
- Vol 13 — safety analyses (SFA/CCA/FTA hooks)
- Vol 21 — V&V, including VVP-004

## 4. Definitions & Acronyms

- Health parameters: monitored quantities and derived states indicating propulsion health (set and limits TBD).
- Exceedance annunciation: signalling that a health parameter has crossed its defined limit (mechanism TBD).
- Safety path: independent path receiving monitoring outputs for protective action (authority TBD).
- VVP-004: applicable verification planning reference.

## 5. System Context

Engine monitoring consumes instrumentation data, evaluates health against limits, annunciates exceedances, records data and feeds the safety path within control and safety constraints.

> **Hazardous-subsystem boundary.** This context describes requirements and architectural boundaries only. No build, ignition, fuel-test or operation instructions are provided.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-PMN-001 | The propulsion system shall define engine health parameters and associated limits (set and values TBD). | REQ-HFPX-SYS-001, REQ-HFPX-PRP-003 | Inspection |
| REQ-HFPX-PMN-002 | The monitoring function shall annunciate health-parameter exceedances (mechanism and thresholds TBD). | REQ-HFPX-SYS-003, REQ-HFPX-PRP-003 | Analysis |
| REQ-HFPX-PMN-003 | The monitoring function shall provide data-recording hooks for health and exceedance data (format, rate and retention TBD). | REQ-HFPX-SYS-003 | Inspection |
| REQ-HFPX-PMN-004 | The monitoring function shall interface to the safety path for protective action (authority and protocol TBD). | REQ-HFPX-SYS-003, REQ-HFPX-PRP-004 | Analysis |

## 7. Architecture

Monitoring architecture (structure only): INPUTS (from HFPX-PROP-INS-001, TBD) → LIMIT EVALUATION (TBD) → ANNUNCIATION (TBD) + RECORDING HOOKS (TBD) → SAFETY-PATH INTERFACE (TBD, Vol 13).

> **Hazardous-subsystem boundary.** Architecture defines requirements and interfaces only, not build, installation, ignition or operating procedures.

## 8. Detailed Design

Not applicable at CONCEPT. Limit sets, evaluation logic, annunciation implementation and recording designs are TBD and deferred. No design values stated.

## 9. Interfaces

Monitoring interfaces: M-IN (instrumentation data), M-ANN (exceedance annunciation to crew/logic), M-REC (recording hooks), M-SAF (monitoring-to-safety-path). Definitions TBD in ICDs.

> **Hazardous-subsystem boundary.** Interface definitions describe architectural boundaries and analysis inputs only, not build/ignition/fuel-test/operation procedures.

## 10. Operational Concept

Monitoring evaluates health across controlled ground testing and (later) flight phases; exceedance response and crew/safety-path interactions are TBD. No operating instructions are provided.

## 11. Safety

Monitoring gaps, missed exceedances and spurious annunciations feed Vol 13 SFA/CCA/FTA. Safety-path authority and independence claims are TBD. Analysis only; no operating instructions.

> **Hazardous-subsystem boundary.** Safety discussion is limited to requirements and analysis hooks. No build, ignition, fuel-test or operation instructions are provided.

## 12. Performance

Health-parameter coverage, limit budgets, annunciation behaviour and recording budgets are TBD. Budget holder: this document (REQ-HFPX-PMN-001..003). No values stated.

## 13. Verification & Validation

Verified by inspection (parameter/limit definition, recording hooks, safety-path interface per VVP-004) and analysis (annunciation concept). Later test phases TBD under controlled conditions per Vol 21. Test methodology only; no operational procedures.

## 14. Risks

- Health-parameter and limit TBDs leave fault coverage unproven; mitigation: structure-only requirements with explicit TBDs and SFA review.
- Annunciation/safety-path ambiguity; mitigation: interface ownership fixed to safety-path review under Vol 13.

## 15. Open Issues

Health-parameter set and limits, exceedance annunciation mechanism, data-recording hook details, and monitoring-to-safety-path authority/protocol are all TBD.

## 16. Assumptions

- A-TBD-MON-01: Instrumentation outputs will be available as monitoring inputs; validation: HFPX-PROP-INS-001 review.
- A-TBD-MON-02: Vol 13 can host monitoring-to-safety-path authority definitions; validation: Vol 13 review.

## 17. Dependencies

Depends on SyRS SYS-001/003, ARC-PRP-001, PRQ/PAR tier, HFPX-PROP-INS-001, Vol 13 SFA/CCA/FTA, and Vol 21 VVP-004.

## 18. Traceability

Parents: PRQ/PAR tier (TBD); REQ-HFPX-SYS-001, REQ-HFPX-SYS-003; REQ-HFPX-PRP-003, REQ-HFPX-PRP-004; SFA/CCA/FTA hooks (Vol 13); VVP-004. Children: fault detection (04.14), emergency modes (04.15), integration ICDs, V&V evidence. RTM: REQ-HFPX-PMN-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 4 draft, not baselined. Chapter 04.11.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (Chapter 04.11) |
