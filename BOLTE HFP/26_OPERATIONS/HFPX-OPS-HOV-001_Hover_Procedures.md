# Hover Procedures

**Document ID:** HFPX-OPS-HOV-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the hover-procedure structure for Chapter 26.6. Owns hover-procedure structure, abort structure, unmanned-first rule and verification (all TBD; methodology only).

## 2. Scope

Covers hover-procedure structure (TBD), abort structure (TBD) and unmanned-first rule (TBD). Methodology only; excludes executable flight-operation instructions and values (all TBD).

## 3. Applicable Documents

- HFPX-SYS-OPC-001 Operational Concept; HFPX-SYS-CON-001 CONOPS
- HFPX-SYS-STK-001 Stakeholder Requirements (STK-004)
- Vol 07 / Vol 10 / Vol 11 / Vol 23 interfaces (IDs TBD)

## 4. Definitions & Acronyms

- Hover procedure: structured phases for hover operations (structure TBD)
- Abort: defined exit from hover to a safe state (criteria TBD)
- Unmanned-first rule: gating of human exposure on unmanned evidence (rule TBD)

## 5. System Context

Context TBD. Control laws, HMI, telemetry and range interfaces TBD. Values and thresholds TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-OHP-001 | Hover procedures shall define hover-procedure structure (structure TBD; methodology only). | HFPX-SYS-CON-001 | Inspection |
| REQ-HFPX-OHP-002 | Hover procedures shall define abort structure (criteria TBD). | Vol 07 (ID TBD) | Analysis |
| REQ-HFPX-OHP-003 | Hover procedures shall enforce an unmanned-first rule (rule TBD; no human exposure before unmanned evidence). | HFPX-SYS-STK-001 (STK-004) | Inspection |
|REQ-HFPX-OHP-004|Hover procedures shall be verified (method TBD; methodology only).|Vol 23 (ID TBD)|Inspection|

## 7. Architecture

Structure only. Hover-procedure branch TBD. Abort branch TBD. Unmanned-first gating branch TBD. Methodology only.

## 8. Detailed Design

Structure only (steps TBD, values TBD). Hover phases TBD. Abort detail TBD. No executable flight-operation instructions are given at this revision.

## 9. Interfaces

- Upstream: HFPX-SYS-OPC-001, HFPX-SYS-CON-001 (OPC/CON tier)
- Lateral: Vol 07 control, Vol 10 HMI, Vol 11 comms/telemetry, Vol 23 verification (IDs TBD); stakeholder STK-004

## 10. Operational Concept

Hover flow TBD (methodology only). Entry, hold and exit structure TBD. Abort flow TBD. No executable operations are directed at this revision.

## 11. Safety

Safety provisions TBD. No hazardous operation instructions are given. Hover-abort safety handling TBD.

## 12. Performance

Performance TBD. No limits, minima or durations are stated at this revision. Success criteria TBD.

## 13. Verification & Validation

Verification TBD (method TBD, scope TBD; methodology only). Test methodology deferred to Vol 23 (ID TBD).

## 14. Risks

- Undefined hover structure; mitigation TBD
- Abort handling undefined; mitigation TBD

## 15. Open Issues

- Hover-procedure structure TBD
- Abort structure TBD
- Unmanned-first rule TBD
- Verification method TBD

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on OPC/CON tier (HFPX-SYS-OPC-001, HFPX-SYS-CON-001), stakeholder STK-004, Vol 07/10/11/23 provisions (all TBD).

## 18. Traceability

Parent: OPC/CON tier (HFPX-SYS-OPC-001, HFPX-SYS-CON-001), STK-004, Vol 07/23 interfaces. Children: downstream Vol 26 procedures. RTM: REQ-HFPX-OHP-001..004 → CONCEPT. Owns Chapter 26.6.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. CONCEPT, Rev A (draft).

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 26.6, structure only) |
