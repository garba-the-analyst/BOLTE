# Security Requirements — Chapter 01.14

**Document ID:** HFPX-SYS-SEC-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 8 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Capture system security requirements for HFP-X in one tier. This Tranche 8 draft establishes structure only; all mechanisms and values are TBD.

## 2. Scope

Covers protection of command, control, data and ground links against unauthorised access and interference at system level. Detailed mechanisms live in Vol 17. All quantitative values and mechanisms TBD.

## 3. Applicable Documents

- HFPX-SYS-STK-001 Stakeholder Requirements (parent tier)
- HFPX-SYS-REQ-001 SyRS (Chapter 01.6)
- Vol 17 cybersecurity views (not written, authoritative for mechanisms)
- HFP prompt §§8–10 (requirements format, classification, traceability)

## 4. Definitions & Acronyms

- Security requirement ID `REQ-HFPX-SCR-NNN`; verification: Analysis / Inspection / Demonstration / Test
- TBD/TBC: unknown data handling; no invented values
- Vol 17: cybersecurity subsystem volume owning detailed security mechanisms

## 5. System Context

Security requirements bound the attack surface spanning air vehicle, datalinks and ground station:

```text
STAKEHOLDER (STK tier) → SECURITY (this document) → VOL 17 MECHANISMS → V&V
```

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-SCR-001 | The system shall restrict command and control functions to authorised actors only (authorisation mechanisms TBD, owned by Vol 17). | REQ-HFPX-STK-001 | Analysis |
| REQ-HFPX-SCR-002 | The system shall protect command, telemetry and configuration data against unauthorised modification (protection mechanisms TBD, owned by Vol 17). | REQ-HFPX-STK-006 | Analysis + Inspection |
| REQ-HFPX-SCR-003 | The system shall record defined security-relevant events for post-event review (event set and retention TBD, owned by Vol 17). | REQ-HFPX-STK-001 | Inspection |
| REQ-HFPX-SCR-004 | The system security architecture and mechanism set shall be documented and traceable to these requirements (artefact structure TBD, owned by Vol 17). | REQ-HFPX-STK-006 | Inspection |

## 7. Architecture

Allocation (SAD owns authoritative allocation; Vol 17 owns mechanism allocation): SCR-001/SCR-002 → comms + FCS + ground station views; SCR-003 → embedded computing + ground station; SCR-004 → SE artefacts. Allocation table TBD.

## 8. Detailed Design

Not applicable — requirements tier only. Security mechanisms, keys, protocols and hardening details live in Vol 17 and are TBD.

## 9. Interfaces

Security boundaries (air–ground links, servicing ports, software update paths) reference Chapter 01.16; ICD details TBD.

## 10. Operational Concept

Security requirements are exercised through nominal operations and defined misuse/denied-environment threads (threads TBD in V&V Plan).

## 11. Safety

Security failures with safety effect feed system safety requirements (01.10) and the Safety Case; joint safety–security analyses TBD.

## 12. Performance

No security performance value (throughput, latency, capacity) is stated; all such values TBD.

## 13. Verification & Validation

Each requirement states its method above; verification cases and IDs are TBD in the V&V Plan (Vol 22). Analysis via threat and architecture review; Inspection via documentation review. Requirements without a verification method are rejected at SRR.

## 14. Risks

- Mechanisms deferred to Vol 17 while system requirements must bound scope now → mitigation: explicit TBD hooks, Vol 17 traceability required
- Threat landscape evolving → mitigation: CONCEPT status, updates by change record

## 15. Open Issues

- Authorised-actor model, protection mechanisms, event set and retention TBD (Vol 17 actions)
- Threat assessment scope TBD

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on stakeholder security intent (STK tier), Vol 17 mechanism maturity, SAD allocation, safety analyses, V&V Plan cases.

## 18. Traceability

Parents: REQ-HFPX-STK-001, REQ-HFPX-STK-006. Children: Vol 17 security requirements and mechanisms, V&V cases, RTM rows (01.18). RTM seed for SCR-001..004 added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0 (structure only) — Tranche 8 draft, not baselined. Changes require change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 8 draft (Chapter 01.14) |
