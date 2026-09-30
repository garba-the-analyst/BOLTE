# Propulsion Fault Detection

**Document ID:** HFPX-PROP-FLT-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define propulsion fault-detection requirements, architecture, interfaces and verification scaffolding (Chapter 04.14). Establishes structure only; detectable faults, thresholds, latency and annunciation/isolation interfaces are TBD.

## 2. Scope

Limited to requirements, architecture, interfaces, test methodology and safety analysis for propulsion fault detection.

> **Hazardous-subsystem boundary.** This document is limited to requirements, architecture, interfaces, test methodology and safety analysis ONLY. It contains NO build, ignition, fuel-test or operation instructions outside controlled conditions.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (notably REQ-HFPX-SYS-001, REQ-HFPX-SYS-003)
- HFPX-ARC-PRP-001 Propulsion Architecture (notably REQ-HFPX-PRP-003, REQ-HFPX-PRP-004)
- PRQ/PAR tier propulsion requirements (TBD)
- HFPX-PROP-INS-001 / HFPX-PROP-MON-001 (data sources)
- Vol 08.11 / Vol 08.12 — annunciation / isolation interfaces
- Vol 13 — safety analyses (SFA/CCA/FTA hooks)
- Vol 21 — V&V, including VVP-004

## 4. Definitions & Acronyms

- Detectable fault list: faults the propulsion system is required to detect (list TBD).
- Detection thresholds: conditions distinguishing fault from nominal (values TBD).
- Detection latency: time from fault occurrence to declared detection (bound TBD).
- Vol 08.11/08.12: owning views for annunciation and isolation interfaces.

## 5. System Context

Fault detection consumes instrumentation and monitoring outputs, declares faults against thresholds within latency bounds, and feeds annunciation and isolation paths within control and safety constraints.

> **Hazardous-subsystem boundary.** This context describes requirements and architectural boundaries only. No build, ignition, fuel-test or operation instructions are provided.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-PFD-001 | The propulsion system shall define the detectable fault list (list TBD). | REQ-HFPX-SYS-001, REQ-HFPX-PRP-004 | Inspection |
| REQ-HFPX-PFD-002 | Detection thresholds for each detectable fault shall be defined (values TBD). | REQ-HFPX-SYS-003, REQ-HFPX-PRP-003 | Analysis |
| REQ-HFPX-PFD-003 | Detection latency for each detectable fault shall be defined (bounds TBD). | REQ-HFPX-SYS-003 | Analysis / Test |
| REQ-HFPX-PFD-004 | Fault annunciation and isolation interfaces shall be defined (provisions TBD, Vol 08.11/08.12). | REQ-HFPX-SYS-003, REQ-HFPX-PRP-004 | Inspection |

## 7. Architecture

Fault-detection architecture (structure only): INPUTS (instrumentation/monitoring, TBD) → THRESHOLD EVALUATION (TBD) → DECLARATION within latency bound (TBD) → ANNUNCIATION/ISOLATION (Vol 08.11/08.12, TBD).

> **Hazardous-subsystem boundary.** Architecture defines requirements and interfaces only, not build, installation, ignition or operating procedures.

## 8. Detailed Design

Not applicable at CONCEPT. Detection algorithms, threshold sets and timing implementations are TBD and deferred. No design values stated.

## 9. Interfaces

Fault-detection interfaces: F-IN (sensed/monitored inputs), F-ANN (annunciation to Vol 08.11), F-ISO (isolation to Vol 08.12), F-SAF (to safety/FTA views). Definitions TBD in ICDs.

> **Hazardous-subsystem boundary.** Interface definitions describe architectural boundaries and analysis inputs only, not build/ignition/fuel-test/operation procedures.

## 10. Operational Concept

Fault detection is exercised under controlled ground testing and reasoned for (later) flight phases; fault-response sequencing concepts are TBD. No operating instructions are provided.

## 11. Safety

Missed detections, false detections and late detections feed Vol 13 SFA/CCA/FTA. Coverage and integrity claims are TBD. Analysis only; no operating instructions.

> **Hazardous-subsystem boundary.** Safety discussion is limited to requirements and analysis hooks. No build, ignition, fuel-test or operation instructions are provided.

## 12. Performance

Fault coverage, threshold and latency budgets are TBD. Budget holder: this document (REQ-HFPX-PFD-001..003). No values stated.

## 13. Verification & Validation

Verified by inspection (fault list, interface definitions per VVP-004) and analysis/test (thresholds and latency under controlled conditions, TBD). Test methodology only; no operational procedures.

## 14. Risks

- Fault-list and threshold TBDs leave coverage unproven; mitigation: structure-only requirements with explicit TBDs and SFA review.
- Latency TBDs leave safety-path timeliness unproven; mitigation: gated analysis/test before any credit.

## 15. Open Issues

Detectable fault list, per-fault thresholds, per-fault latency bounds, and Vol 08.11/08.12 annunciation/isolation interface details are all TBD.

## 16. Assumptions

- A-TBD-FLT-01: Instrumentation/monitoring can supply fault-detection inputs; validation: HFPX-PROP-INS-001 / MON-001 review.
- A-TBD-FLT-02: Vol 08.11/08.12 can own annunciation/isolation interfaces; validation: Vol 08 review.

## 17. Dependencies

Depends on SyRS SYS-001/003, ARC-PRP-001, PRQ/PAR tier, HFPX-PROP-INS-001/MON-001, Vol 08.11/08.12, Vol 13 SFA/CCA/FTA, and Vol 21 VVP-004.

## 18. Traceability

Parents: PRQ/PAR tier (TBD); REQ-HFPX-SYS-001, REQ-HFPX-SYS-003; REQ-HFPX-PRP-003, REQ-HFPX-PRP-004; SFA/CCA/FTA hooks (Vol 13); VVP-004. Children: detailed detection design, Vol 08.11/08.12 interfaces, V&V evidence. RTM: REQ-HFPX-PFD-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 4 draft, not baselined. Chapter 04.14.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (Chapter 04.14) |
