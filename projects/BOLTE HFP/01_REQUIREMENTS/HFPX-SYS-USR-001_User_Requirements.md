# User Requirements — Chapter 01.5

**Document ID:** HFPX-SYS-USR-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 8 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Capture user-level needs for HFP-X as verifiable requirements bridging Stakeholder Requirements (01.4) and System Requirements (01.6). This Tranche 8 draft establishes structure only; all quantitative values are TBD.

## 2. Scope

Covers operator, pilot and maintainer user needs for nominal and off-nominal operations. Derived design and subsystem detail lives in Vol 03–18. All values TBD.

## 3. Applicable Documents

- HFPX-SYS-STK-001 Stakeholder Requirements (parent tier)
- HFPX-SYS-REQ-001 SyRS (Chapter 01.6)
- HFPX-SYS-CON-001 CONOPS (operational threads)
- HFP prompt §§8–10 (requirements format, classification, traceability)

## 4. Definitions & Acronyms

- User requirement ID `REQ-HFPX-USR-NNN`; verification: Analysis / Inspection / Demonstration / Test
- TBD/TBC: unknown data handling; no invented values
- CONOPS threads: nominal and off-nominal scenarios from HFPX-SYS-CON-001

## 5. System Context

User requirements translate stakeholder intent (STK-002 operational use, STK-007 operator interface) into verifiable user-facing system behaviour, allocated downstream via SyRS and SAD:

```text
STAKEHOLDER (STK-002, STK-007) → USER (this document) → SYSTEM (SyRS) → SUBSYSTEM → V&V
```

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-USR-001 | The system shall provide user controls enabling execution of defined CONOPS nominal flight threads (control details and limits TBD). | REQ-HFPX-STK-002 | Demonstration |
| REQ-HFPX-USR-002 | The system shall provide user displays presenting flight status, warnings and emergency guidance (display content and thresholds TBD). | REQ-HFPX-STK-007 | Demonstration |
| REQ-HFPX-USR-003 | The system shall provide user interfaces for pre-flight, post-flight and turnaround tasks (task list and layout TBD). | REQ-HFPX-STK-007 | Inspection |
| REQ-HFPX-USR-004 | The system shall alert the user to off-nominal conditions requiring user action (alert conditions and timing TBD). | REQ-HFPX-STK-002 | Demonstration |

## 7. Architecture

Allocation (SAD owns authoritative allocation): USR-001/USR-004 → FCS + pilot interface + comms; USR-002/USR-003 → helmet/HMI + ground station. Allocation table TBD.

## 8. Detailed Design

Not applicable — requirements tier only. Subsystem design lives in Vol 03–18 and is TBD.

## 9. Interfaces

User-interface boundaries (helmet, HMI, ground station) reference Chapter 01.16; ICD details TBD.

## 10. Operational Concept

Each user requirement maps to ≥1 CONOPS thread (mapping table TBD in V&V Plan).

## 11. Safety

User actions affecting safety are constrained by system safety requirements (01.10); no safety claim is made in this document. Analyses TBD.

## 12. Performance

No performance quantification in this tier; values TBD and owned by Chapter 01.8.

## 13. Verification & Validation

Each requirement states its method above; verification cases and IDs are TBD in the V&V Plan (Vol 22). Demonstration via ground rig or simulator; Inspection via document and HMI review. Requirements without a verification method are rejected at SRR.

## 14. Risks

- User needs evolving with CONOPS maturity → mitigation: explicit CONCEPT status, change control for revisions
- HMI detail deferred → mitigation: structure-first approach, SRR exit requires only requirement set completeness

## 15. Open Issues

- Mapping of USR requirements to CONOPS threads TBD
- HMI and control layout TBD pending human factors tier (01.11)

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on STK-002/STK-007 stability, CONOPS threads, human factors requirements (01.11), SAD allocation, V&V Plan cases.

## 18. Traceability

Parents: REQ-HFPX-STK-002, REQ-HFPX-STK-007. Children: SyRS requirements, SAD views, V&V cases, RTM rows (01.18). RTM seed for USR-001..004 added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0 (structure only) — Tranche 8 draft, not baselined. Changes require change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 8 draft (Chapter 01.5) |
