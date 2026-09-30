# 09.11 Engine Sensors

**Document ID:** HFPX-NAV-ENG-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the structure and subsystem requirements for engine sensing within Volume 09, Chapter 09.11. This revision establishes requirement placeholders only; all parameter lists, accuracies, and verification details are TBD. No design approval or part selection is implied.

## 2. Scope

Covers engine sensor parameter definition, interface to monitoring functions, accuracy, and verification structure.

Out of scope: propulsion design (Vol 04); detailed sensor design; supplier selection. No parts are selected at this revision.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parents REQ-HFPX-SYS-004 and related functional tier, including FUN-003 where applicable)
- HFPX-NAV-IDX-001 Volume 09 index / README (Chapter 09.11)
- Vol 04.10 propulsion parameters reference (hooks TBD)
- Vol 04.11 and Vol 08.10 monitoring references (interface hooks TBD)
- HFPX-VV-PLN-001 V&V Plan (not written, verification cases TBD)
- Safety analyses references Vol 13 (SFA/CCA/FTA hooks, details TBD)

## 4. Definitions & Acronyms

_TBD_

- ENG: Engine Sensors chapter (09.11)
- NES: engine sensor requirement prefix (REQ-HFPX-NES)
- TBD: to be determined; TBC: to be confirmed
- Verification methods: Analysis / Inspection / Demonstration / Test (allocation per requirement TBD)

## 5. System Context

Engine sensing supports propulsion awareness and monitoring by providing engine parameters to monitoring and navigation-related consumers.

Context TBD. Allocation TBD. Relationship to functional tier FUN-003 TBD. Hooks to Vol 04.10 parameter definitions TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-NES-001|The engine sensing function shall provide a parameter inventory TBD, consistent with Vol 04.10 hooks TBD.|REQ-HFPX-SYS-004, FUN-003|Inspection|
|REQ-HFPX-NES-002|The engine sensing function shall interface to monitoring functions TBD, consistent with Vol 04.11 and Vol 08.10 hooks TBD.|REQ-HFPX-SYS-004, FUN-003|Inspection|
|REQ-HFPX-NES-003|The engine sensing function shall meet measurement accuracy requirements TBD.|REQ-HFPX-SYS-004, FUN-003|Test|
|REQ-HFPX-NES-004|The engine sensing function shall be verified by means TBD.|REQ-HFPX-SYS-004, FUN-003|Inspection|

No quantitative values are stated. All parameters, accuracies, and test conditions are TBD.

## 7. Architecture

_TBD_

Channel allocation, sampling responsibility, and processing location TBD. Relationship to Volume 09 sensor architecture (09.1) TBD. Structure only at this revision.

## 8. Detailed Design

_TBD_

No detailed design is defined. No sensor technology or supplier is selected. No parts are selected at this revision.

## 9. Interfaces

_TBD_

Interfaces to Vol 04 propulsion and Vol 04.11 / Vol 08.10 monitoring TBD. Signal, protocol, and ICD details TBD.

## 10. Operational Concept

_TBD_

Use of engine sensor outputs across flight phases and ground operations TBD.

## 11. Safety

_TBD_

Safety relevance TBD. Hooks to SFA/CCA and FTA/FMEA as applicable TBD. Hooks to VFD/VHM monitoring TBD. No safety claim is made at this revision.

## 12. Performance

_TBD_

All performance values TBD. No value in this document is approved.

## 13. Verification & Validation

_TBD_

Verification means for REQ-HFPX-NES-001..004 TBD. V&V cases and acceptance criteria TBD in the V&V Plan.

## 14. Risks

- TBD density high: parameter inventory and monitoring interface undefined; mitigation: Vol 04.10 / 04.11 / 08.10 hooks established as placeholders
- Interface mismatch with monitoring consumers; mitigation: ICD definition in later revisions

## 15. Open Issues

- Parameter inventory TBD (hooks to Vol 04.10)
- Interface to monitoring TBD (Vol 04.11 / 08.10)
- Accuracy requirements TBD
- Verification means TBD

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on: functional tier FUN-003; Vol 04.10 parameter definitions; Vol 04.11 and Vol 08.10 monitoring definitions; sensor architecture 09.1; V&V Plan cases; safety analyses Vol 13 outputs.

## 18. Traceability

Parents: REQ-HFPX-SYS-004, FUN-003. Children: TBD (design, ICDs, V&V cases, RTM rows). RTM seed for REQ-HFPX-NES-001..004 is added with this tranche (Status CONCEPT). Monitoring hooks to Vol 04.11 / 08.10 TBD.

## 19. Configuration

BL-0.0. Tranche 5 draft, CONCEPT, not baselined. Changes require change control in later revisions.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 draft (Chapter 09.11) |
