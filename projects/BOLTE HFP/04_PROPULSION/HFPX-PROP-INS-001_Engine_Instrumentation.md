# Engine Instrumentation

**Document ID:** HFPX-PROP-INS-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define engine instrumentation requirements, architecture, interfaces and verification scaffolding for HFP-X propulsion (Chapter 04.10). Establishes structure only; sensed-parameter sets, accuracies, sampling and calibration procedures are TBD.

## 2. Scope

Limited to requirements, architecture, interfaces, test methodology and safety analysis for propulsion instrumentation.

> **Hazardous-subsystem boundary.** This document is limited to requirements, architecture, interfaces, test methodology and safety analysis ONLY. It contains NO build, ignition, fuel-test or operation instructions outside controlled conditions.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (notably REQ-HFPX-SYS-001, REQ-HFPX-SYS-003)
- HFPX-ARC-PRP-001 Propulsion Architecture (notably REQ-HFPX-PRP-003)
- PRQ/PAR tier propulsion requirements (TBD)
- Vol 09.17 — calibration provisions
- Vol 13 — safety analyses (SFA/CCA/FTA hooks)
- Vol 21 — V&V, including VVP-004

## 4. Definitions & Acronyms

- Engine instrumentation: sensors and signal paths that observe propulsion state for monitoring, control and safety.
- Sensed parameters: speed, temperature, pressure, vibration and others — full list TBD.
- Calibration hooks: provisions enabling calibration without defining procedures or values.
- VVP-004: applicable verification planning reference.

## 5. System Context

Propulsion instrumentation observes engine/module state and supplies data to control, monitoring, fault detection and safety paths within airframe, power and data constraints.

> **Hazardous-subsystem boundary.** This context describes requirements and architectural boundaries only. No build, ignition, fuel-test or operation instructions are provided.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-PIN-001 | The propulsion system shall define the sensed-parameter list for engine instrumentation, including speed, temperature, pressure and vibration (full list TBD). | REQ-HFPX-SYS-001, REQ-HFPX-PRP-003 | Inspection |
| REQ-HFPX-PIN-002 | Sensor accuracy for each sensed parameter shall be defined (values TBD). | REQ-HFPX-SYS-003, REQ-HFPX-PRP-003 | Analysis |
| REQ-HFPX-PIN-003 | Sampling and refresh behaviour for engine instrumentation shall be defined (rates and timing TBD). | REQ-HFPX-SYS-003, REQ-HFPX-PRP-003 | Analysis |
| REQ-HFPX-PIN-004 | Engine instrumentation shall provide calibration hooks traceable to Vol 09.17 (methods and intervals TBD). | VVP-004 | Inspection |

## 7. Architecture

Instrumentation architecture (structure only): SENSORS (types and locations TBD) → SIGNAL CONDITIONING (TBD) → DISTRIBUTION to control / monitoring / safety paths (TBD) → CALIBRATION HOOKS (Vol 09.17).

> **Hazardous-subsystem boundary.** Architecture defines requirements and interfaces only, not build, installation, ignition or operating procedures.

## 8. Detailed Design

Not applicable at CONCEPT. Sensor part numbers, mounting detail, wiring detail and conditioning designs are TBD and deferred. No design values stated.

## 9. Interfaces

Instrumentation interfaces: sensor-to-conditioning, conditioning-to-control, conditioning-to-monitoring, conditioning-to-safety-path, and calibration interface to Vol 09.17 provisions. Connector, protocol and ICD details TBD.

> **Hazardous-subsystem boundary.** Interface definitions describe architectural boundaries and analysis inputs only, not build/ignition/fuel-test/operation procedures.

## 10. Operational Concept

Instrumentation supports pre-test checks, controlled ground testing and (later) flight phases by supplying sensed data to monitoring and safety logic. Operational use concepts are TBD and limited to controlled conditions; no operating instructions are provided.

## 11. Safety

Instrumentation failures and mis-sensing feed Vol 13 SFA/CCA/FTA. Independence and integrity claims are TBD and subject to safety analysis. Analysis only; no operating instructions.

> **Hazardous-subsystem boundary.** Safety discussion is limited to requirements and analysis hooks. No build, ignition, fuel-test or operation instructions are provided.

## 12. Performance

Sensed-parameter coverage, accuracy and sampling/refresh budgets are TBD. Budget holder: this document (REQ-HFPX-PIN-001..003). No values stated.

## 13. Verification & Validation

Verified by inspection (parameter list, calibration hooks per VVP-004) and analysis (accuracy and sampling concepts). Later test phases TBD under controlled conditions per Vol 21. Test methodology only; no operational procedures.

## 14. Risks

- Sensed-parameter list delay stalls monitoring/fault-detection dependents; mitigation: structure-only requirements with explicit TBDs.
- Accuracy/sampling TBDs leave control and safety claims unproven; mitigation: trace to analysis and gated VVP-004 evidence.

## 15. Open Issues

Sensed-parameter full list, per-parameter accuracy, sampling/refresh definitions, and Vol 09.17 calibration hook details are all TBD.

## 16. Assumptions

- A-TBD-INS-01: Speed/temperature/pressure/vibration partition is stable scaffolding pending detailed trade; validation: architecture review.
- A-TBD-INS-02: Vol 09.17 can host calibration provisions for propulsion instrumentation; validation: Vol 09 review.

## 17. Dependencies

Depends on SyRS SYS-001/003, ARC-PRP-001, PRQ/PAR tier, Vol 09.17 calibration provisions, Vol 13 SFA/CCA/FTA, and Vol 21 VVP-004.

## 18. Traceability

Parents: PRQ/PAR tier (TBD); REQ-HFPX-SYS-001, REQ-HFPX-SYS-003; REQ-HFPX-PRP-003; SFA/CCA/FTA hooks (Vol 13); VVP-004. Children: monitoring (04.11), fault detection (04.14), integration ICDs, V&V evidence. RTM: REQ-HFPX-PIN-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 4 draft, not baselined. Chapter 04.10.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (Chapter 04.10) |
