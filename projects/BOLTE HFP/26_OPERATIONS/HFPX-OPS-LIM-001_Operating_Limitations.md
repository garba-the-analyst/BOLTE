# Operating Limitations

**Document ID:** HFPX-OPS-LIM-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the operating-limitations structure for Chapter 26.2. Owns limitation inventory, exceedance behaviour, limitation-review rule, display provisions and verification (all TBD, structure only).

## 2. Scope

Covers limitation inventory across envelope, weather, mass, fuel and system-status categories (inventory TBD), exceedance behaviour (TBD), limitation-review rule (TBD) and display per Vol 10 (TBD). Excludes numeric limits, minima, durations and executable instructions (all TBD).

## 3. Applicable Documents

- HFPX-SYS-OPC-001 Operational Concept; HFPX-SYS-CON-001 CONOPS
- HFPX-SYS-STK-001 Stakeholder Requirements (STK-004)
- Vol 07 / Vol 10 / Vol 11 / Vol 23 interfaces (IDs TBD)

## 4. Definitions & Acronyms

- Limitation inventory: structured set of operating limitations (inventory TBD)
- Exceedance behaviour: defined response to limitation exceedance (behaviour TBD)
- Limitation-review rule: rule governing review of limitations (rule TBD)

## 5. System Context

Context TBD. Envelope, weather, mass, fuel and system-status sources TBD. Display and monitoring context per Vol 10 and Vol 11 (TBD). Values and thresholds TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-OLI-001 | Operating limitations shall be captured in a limitation inventory covering envelope, weather, mass, fuel and system-status categories (inventory TBD). | HFPX-SYS-OPC-001 | Inspection |
| REQ-HFPX-OLI-002 | Exceedance behaviour for operating limitations shall be defined (behaviour TBD). | HFPX-SYS-CON-001 | Analysis |
| REQ-HFPX-OLI-003 | Operating limitations shall be subject to a limitation-review rule (rule TBD). | HFPX-SYS-STK-001 (STK-004) | Inspection |
| REQ-HFPX-OLI-004 | Operating limitations shall be displayed per Vol 10 HMI provisions (display TBD). | Vol 10 (ID TBD) | Demonstration |
|REQ-HFPX-OLI-005|Compliance with operating limitations shall be verified (method TBD).|Vol 23 (ID TBD)|Inspection|

## 7. Architecture

Structure only. Limitation-inventory structure TBD. Exceedance-behaviour structure TBD. Review-rule structure TBD. Display structure per Vol 10 TBD.

## 8. Detailed Design

Structure only (steps TBD, values TBD). Limitation items TBD. No limits, minima or durations are stated. No executable flight-operation instructions are given at this revision.

## 9. Interfaces

- Upstream: HFPX-SYS-OPC-001, HFPX-SYS-CON-001 (OPC/CON tier)
- Lateral: Vol 07 control, Vol 10 display/HMI, Vol 11 comms/telemetry, Vol 23 verification (IDs TBD); stakeholder STK-004
- Downstream: Vol 26 procedures Chapters 26.4 onwards (flow TBD)

## 10. Operational Concept

Limitation application in operations TBD. Exceedance handling flow TBD. Display and crew-response structure TBD. No executable operations are directed at this revision.

## 11. Safety

Safety provisions TBD. No hazardous operation instructions are given. Exceedance safety handling TBD and deferred to applicable safety volumes (IDs TBD).

## 12. Performance

Performance TBD. No limits, minima or durations are stated at this revision. Success criteria TBD.

## 13. Verification & Validation

Verification TBD (method TBD, scope TBD). Test methodology deferred to Vol 23 (ID TBD).

## 14. Risks

- Incomplete limitation inventory (inventory TBD); mitigation TBD
- Undefined exceedance behaviour; mitigation TBD

## 15. Open Issues

- Limitation inventory TBD (envelope/weather/mass/fuel/system-status)
- Exceedance behaviour TBD
- Limitation-review rule TBD
- Display provisions TBD (Vol 10)
- Verification method TBD

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on OPC/CON tier (HFPX-SYS-OPC-001, HFPX-SYS-CON-001), stakeholder STK-004, Vol 07/10/11/23 provisions (all TBD).

## 18. Traceability

Parent: OPC/CON tier (HFPX-SYS-OPC-001, HFPX-SYS-CON-001), STK-004, Vol 07/10/11/23 interfaces. Children: Vol 26 procedures. RTM: REQ-HFPX-OLI-001..005 → CONCEPT. Owns Chapter 26.2.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. CONCEPT, Rev A (draft).

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 26.2, structure only) |
