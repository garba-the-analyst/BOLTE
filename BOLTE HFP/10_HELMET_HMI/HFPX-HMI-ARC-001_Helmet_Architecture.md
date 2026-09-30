# Helmet Architecture

**Document ID:** HFPX-HMI-ARC-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the smart-helmet subsystem partition and architectural relationships for Chapter 10.1. Allocation of functions to helmet subsystems and external volumes is TBD at this revision.

## 2. Scope

Covers the helmet subsystem partition, data and power interface hooks, HMI-to-FCS and HMI-to-communications flow hooks, and safety-alert path independence for HFP-X. Excludes detailed design of helmet subsystems (Chapters 10.2–10.17) and external avionics, power, and communications design (Vol 08, Vol 15, Vol 11).

## 3. Applicable Documents

- HFPX-SYS-STK-001 Stakeholder Requirements (REQ-HFPX-STK-007)
- HFPX-SYS-REQ-001 System Requirements (REQ-HFPX-SYS-005) — TBD
- HSA tier requirements — TBD
- HUM tier requirements — TBD
- Vol 08 Avionics — TBD
- Vol 15 Power — TBD
- Vol 10 Chapters 10.2–10.17 — TBD

## 4. Definitions & Acronyms

- HMI: Human-Machine Interface
- FCS: Flight Control System
- TBD: To Be Determined
- Further helmet terms and acronyms — TBD

## 5. System Context

The smart helmet is the pilot-worn HMI node that presents status, warning, and emergency guidance and carries voice, tracking, and vision functions. Its subsystem boundaries and its relationships to FCS, communications, avionics, and power are TBD and are structured by this document.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-HAR-001|The helmet subsystem partition shall be defined, allocating functions to helmet subsystems, with partition content TBD.|REQ-HFPX-STK-007; REQ-HFPX-SYS-005; HSA; HUM|Inspection|
|REQ-HFPX-HAR-002|The helmet data interfaces shall be defined, with interface content and counterpart allocation TBD (Vol 08 hook TBD).|REQ-HFPX-STK-007; REQ-HFPX-SYS-005; HSA; HUM|Inspection|
|REQ-HFPX-HAR-003|The helmet power interfaces shall be defined, with interface content and counterpart allocation TBD (Vol 15 hook TBD).|REQ-HFPX-STK-007; REQ-HFPX-SYS-005; HSA; HUM|Inspection|
|REQ-HFPX-HAR-004|The HMI-to-FCS and HMI-to-communications information flow shall be defined, with flow content TBD.|REQ-HFPX-STK-007; REQ-HFPX-SYS-005; HSA; HUM|Inspection|
|REQ-HFPX-HAR-005|The safety-alert path through the helmet shall be independent as defined, with independence criteria TBD.|REQ-HFPX-STK-007; REQ-HFPX-SYS-005; HSA; HUM|Inspection|

## 7. Architecture

Helmet subsystem partition and allocation to Chapters 10.2–10.17 — TBD. Relationship to system-level architecture — TBD.

## 8. Detailed Design

Not applicable at this revision — architecture structure only. Detailed design — TBD.

## 9. Interfaces

Data interface hooks to Vol 08 — TBD. Power interface hooks to Vol 15 — TBD. HMI-to-FCS and HMI-to-communications flow interfaces — TBD.

## 10. Operational Concept

Helmet architecture use across nominal and off-nominal operations — TBD.

## 11. Safety

Safety-alert path independence hooks — TBD. Further safety input from Vol 13 — TBD.

## 12. Performance

Performance criteria for the helmet architecture — TBD. No values are stated at this revision.

## 13. Verification & Validation

Verification by review of the partition, interface definitions, information flow, and independence definition against the requirements in §6. Verification artefacts and acceptance criteria — TBD.

## 14. Risks

- Subsystem partition defined before external interface owners are assigned; mitigation TBD
- Further risks — TBD

## 15. Open Issues

- Helmet subsystem partition content TBD
- Data and power interface content and owners TBD
- HMI-to-FCS and HMI-to-communications flow content TBD
- Safety-alert independence criteria TBD

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on STK-007, SYS-005, HSA tier, HUM tier, Vol 08 avionics interfaces, Vol 15 power interfaces, and FCS and communications definitions. Ownership and sequencing — TBD.

## 18. Traceability

Parents: REQ-HFPX-STK-007; REQ-HFPX-SYS-005; HSA tier; HUM tier. Children: TBD. Requirements REQ-HFPX-HAR-001..005 trace to parents as listed in §6.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Changes require change records once baselined.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 10.1) |
