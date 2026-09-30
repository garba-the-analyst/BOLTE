# Concept of Operations

**Document ID:** HFPX-OPS-CON-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the operations-level Concept of Operations for Chapter 26.1. Owns operations CONOPS ownership, scenario coverage, CONOPS-to-procedure flow and validation provisions (all TBD, structure only).

## 2. Scope

Covers operations-level CONOPS ownership (TBD), scenario coverage (TBD), CONOPS-to-procedure flow to Vol 26 procedures (TBD) and validation (TBD). Excludes executable flight-operation instructions, design values and verification detail (all TBD).

## 3. Applicable Documents

- HFPX-SYS-OPC-001 Operational Concept; HFPX-SYS-CON-001 CONOPS (HFPX-SYS-CON-001_CONOPS.md style baseline)
- HFPX-SYS-STK-001 Stakeholder Requirements (STK-004)
- Vol 07 / Vol 10 / Vol 11 / Vol 23 interfaces (IDs TBD); Vol 30 training hooks (TBD)

## 4. Definitions & Acronyms

- CONOPS: Concept of Operations
- Operations-level CONOPS: Vol 26 scenario ownership layer under SYS OPC/CON tier (detail TBD)
- Scenario coverage: set of nominal and off-nominal threads owned at operations level (coverage TBD)
- CONOPS-to-procedure flow: trace from scenarios to Vol 26 procedures (flow TBD)

## 5. System Context

Actors: air vehicle, operator/pilot, ground crew, ground station, range (roles TBD). Preconditions: authorised range, qualified personnel, configured vehicle (all TBD). Envelopes, thresholds and values: TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-OCO-001 | The operations CONOPS shall define operations-level CONOPS ownership (ownership TBD). | HFPX-SYS-OPC-001 | Inspection |
| REQ-HFPX-OCO-002 | The operations CONOPS shall define scenario coverage (coverage TBD). | HFPX-SYS-CON-001 | Inspection |
| REQ-HFPX-OCO-003 | The operations CONOPS shall define the CONOPS-to-procedure flow to Vol 26 procedures (flow TBD). | HFPX-SYS-CON-001 | Inspection |
| REQ-HFPX-OCO-004 | The operations CONOPS shall define validation of operations scenarios (method TBD). | HFPX-SYS-STK-001 (STK-004) | Inspection |

## 7. Architecture

Structure only. Operations CONOPS structure headings TBD. Ownership mapping to OPC/CON tier TBD. Trace structure to Vol 26 procedures TBD. No design decisions at this revision.

## 8. Detailed Design

Structure only (steps TBD, values TBD). Procedure detail TBD. No executable flight-operation instructions are given at this revision.

## 9. Interfaces

- Upstream: HFPX-SYS-OPC-001, HFPX-SYS-CON-001 (OPC/CON tier)
- Downstream: Vol 26 procedures Chapters 26.4 onwards (flow TBD)
- Lateral: Vol 07 control, Vol 10 HMI, Vol 11 comms/telemetry, Vol 23 test (IDs TBD); stakeholder STK-004

## 10. Operational Concept

This document is the operations-level scenario layer. CONOPS-to-procedure flow TBD. Scenario threads, actors, triggers, responses and end states TBD. No executable operations are directed at this revision.

## 11. Safety

Safety provisions TBD. No hazardous operation instructions are given. Unmanned-first progression referenced; gating TBD. FHA and safety analyses deferred to applicable safety volumes (IDs TBD).

## 12. Performance

Performance TBD. No limits, minima or durations are stated at this revision. Success criteria TBD.

## 13. Verification & Validation

Validation TBD. Verification by inspection of coverage and flow (scope TBD). Test methodology deferred to Vol 23 (ID TBD).

## 14. Risks

- Scenario-coverage gap (coverage TBD); mitigation TBD
- CONOPS-to-procedure flow mismatch; mitigation TBD

## 15. Open Issues

- Operations-level CONOPS ownership TBD
- Scenario coverage TBD
- CONOPS-to-procedure flow TBD
- Validation method TBD

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on OPC/CON tier (HFPX-SYS-OPC-001, HFPX-SYS-CON-001), stakeholder STK-004, Vol 07/10/11/23 provisions (all TBD).

## 18. Traceability

Parent: OPC/CON tier (HFPX-SYS-OPC-001, HFPX-SYS-CON-001), STK-004. Children: Vol 26 procedures. RTM: REQ-HFPX-OCO-001..004 → CONCEPT. Owns Chapter 26.1.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. CONCEPT, Rev A (draft).

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 26.1, structure only) |
