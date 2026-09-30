# Transition Procedures

**Document ID:** HFPX-OPS-TRN-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the transition-procedure structure for Chapter 26.7. Owns transition-procedure structure, entry/exit/abort structure, human-exposure gating and verification (all TBD; methodology only).

## 2. Scope

Covers transition-procedure structure (TBD), entry/exit/abort structure (TBD) and preclusion of human exposure before unmanned evidence (TBD). Methodology only; excludes executable flight-operation instructions and values (all TBD).

## 3. Applicable Documents

- HFPX-SYS-OPC-001 Operational Concept; HFPX-SYS-CON-001 CONOPS
- HFPX-SYS-STK-001 Stakeholder Requirements (STK-004)
- Vol 07 / Vol 10 / Vol 11 / Vol 23 interfaces (IDs TBD)

## 4. Definitions & Acronyms

- Transition: conversion between hover and cruise regimes (detail TBD)
- Entry/exit/abort: structured conditions for transition phases (conditions TBD)
- Unmanned evidence: gated flight evidence preceding human exposure (evidence TBD)

## 5. System Context

Context TBD. Control-law switching, HMI, telemetry and range interfaces TBD. Values and thresholds TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-OTP-001 | Transition procedures shall define transition-procedure structure (structure TBD; methodology only). | HFPX-SYS-CON-001 | Inspection |
| REQ-HFPX-OTP-002 | Transition procedures shall define entry, exit and abort structure (conditions TBD). | Vol 07 (ID TBD) | Analysis |
| REQ-HFPX-OTP-003 | Transition procedures shall preclude human exposure before unmanned evidence (evidence TBD). | HFPX-SYS-STK-001 (STK-004) | Inspection |
|REQ-HFPX-OTP-004|Transition procedures shall be verified (method TBD; methodology only).|Vol 23 (ID TBD)|Inspection|

## 7. Architecture

Structure only. Transition-procedure branch TBD. Entry/exit/abort branch TBD. Human-exposure gating branch TBD. Methodology only.

## 8. Detailed Design

Structure only (steps TBD, values TBD). Transition phases TBD. Control-law switching TBD. No executable flight-operation instructions are given at this revision.

## 9. Interfaces

- Upstream: HFPX-SYS-OPC-001, HFPX-SYS-CON-001 (OPC/CON tier)
- Lateral: Vol 07 control, Vol 10 HMI, Vol 11 comms/telemetry, Vol 23 verification (IDs TBD); stakeholder STK-004

## 10. Operational Concept

Transition flow TBD (methodology only). Entry, conversion and exit structure TBD. Abort flow TBD. No executable operations are directed at this revision.

## 11. Safety

Safety provisions TBD. No hazardous operation instructions are given. Transition-abort safety handling TBD.

## 12. Performance

Performance TBD. No limits, minima or durations are stated at this revision. Success criteria TBD.

## 13. Verification & Validation

Verification TBD (method TBD, scope TBD; methodology only). Test methodology deferred to Vol 23 (ID TBD).

## 14. Risks

- Undefined transition structure; mitigation TBD
- Entry/exit/abort conditions undefined; mitigation TBD

## 15. Open Issues

- Transition-procedure structure TBD
- Entry/exit/abort conditions TBD
- Human-exposure gating evidence TBD
- Verification method TBD

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on OPC/CON tier (HFPX-SYS-OPC-001, HFPX-SYS-CON-001), stakeholder STK-004, Vol 07/10/11/23 provisions (all TBD).

## 18. Traceability

Parent: OPC/CON tier (HFPX-SYS-OPC-001, HFPX-SYS-CON-001), STK-004, Vol 07/23 interfaces. Children: downstream Vol 26 procedures. RTM: REQ-HFPX-OTP-001..004 → CONCEPT. Owns Chapter 26.7.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. CONCEPT, Rev A (draft).

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 26.7, structure only) |
