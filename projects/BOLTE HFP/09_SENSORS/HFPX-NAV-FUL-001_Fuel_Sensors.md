# 09.12 Fuel Sensors

**Document ID:** HFPX-NAV-FUL-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the structure and subsystem requirements for fuel sensing within Volume 09, Chapter 09.12. This revision establishes requirement placeholders only; all parameter lists, accuracies, and verification details are TBD. No design approval or part selection is implied.

## 2. Scope

Covers fuel sensor parameter definition including quantity, pressure, and temperature aspects, interface to consumers, accuracy, and verification structure.

Out of scope: fuel system design (Vol 05); detailed sensor design; supplier selection. No parts are selected at this revision.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parents REQ-HFPX-SYS-004 and related functional tier, including FUN-003 where applicable)
- HFPX-NAV-IDX-001 Volume 09 index / README (Chapter 09.12)
- Vol 05.10 through Vol 05.12 fuel system references (hooks TBD)
- HFPX-VV-PLN-001 V&V Plan (not written, verification cases TBD)
- Safety analyses references Vol 13 (SFA/CCA/FTA hooks, details TBD)

## 4. Definitions & Acronyms

_TBD_

- FUL: Fuel Sensors chapter (09.12)
- NFS: fuel sensor requirement prefix (REQ-HFPX-NFS)
- TBD: to be determined; TBC: to be confirmed
- Verification methods: Analysis / Inspection / Demonstration / Test (allocation per requirement TBD)

## 5. System Context

Fuel sensing supports fuel awareness by providing fuel quantity, pressure, and temperature related measurements to navigation, propulsion, and monitoring consumers.

Context TBD. Allocation TBD. Relationship to functional tier FUN-003 TBD. Hooks to Vol 05.10 through Vol 05.12 TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-NFS-001|The fuel sensing function shall provide a parameter inventory TBD, including quantity, pressure, and temperature aspects per Vol 05.10 through Vol 05.12 hooks TBD.|REQ-HFPX-SYS-004, FUN-003|Inspection|
|REQ-HFPX-NFS-002|The fuel sensing function shall interface to consuming functions TBD.|REQ-HFPX-SYS-004, FUN-003|Inspection|
|REQ-HFPX-NFS-003|The fuel sensing function shall meet measurement accuracy requirements TBD.|REQ-HFPX-SYS-004, FUN-003|Test|
|REQ-HFPX-NFS-004|The fuel sensing function shall be verified by means TBD.|REQ-HFPX-SYS-004, FUN-003|Inspection|

No quantitative values are stated. All parameters, accuracies, and test conditions are TBD.

## 7. Architecture

_TBD_

Channel allocation and processing location TBD. Relationship to Volume 09 sensor architecture (09.1) TBD. Structure only at this revision.

## 8. Detailed Design

_TBD_

No detailed design is defined. No sensor technology or supplier is selected. No parts are selected at this revision.

## 9. Interfaces

_TBD_

Interfaces to fuel system (Vol 05.10 through Vol 05.12) and to data consumers TBD. Signal, protocol, and ICD details TBD.

## 10. Operational Concept

_TBD_

Use of fuel sensor outputs across flight phases, refuelling, and ground operations TBD.

## 11. Safety

_TBD_

Safety relevance TBD. Hooks to SFA/CCA and FTA/FMEA as applicable TBD. Hooks to VFD/VHM monitoring TBD. No safety claim is made at this revision.

## 12. Performance

_TBD_

All performance values TBD. No value in this document is approved.

## 13. Verification & Validation

_TBD_

Verification means for REQ-HFPX-NFS-001..004 TBD. V&V cases and acceptance criteria TBD in the V&V Plan.

## 14. Risks

- TBD density high: parameter inventory and consumer interface undefined; mitigation: Vol 05.10 through Vol 05.12 hooks established as placeholders
- Interface mismatch with fuel system and consumers; mitigation: ICD definition in later revisions

## 15. Open Issues

- Parameter inventory TBD (quantity / pressure / temperature per Vol 05.10 through Vol 05.12)
- Interface definition TBD
- Accuracy requirements TBD
- Verification means TBD

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on: functional tier FUN-003; Vol 05.10 through Vol 05.12 definitions; sensor architecture 09.1; V&V Plan cases; safety analyses Vol 13 outputs.

## 18. Traceability

Parents: REQ-HFPX-SYS-004, FUN-003. Children: TBD (design, ICDs, V&V cases, RTM rows). RTM seed for REQ-HFPX-NFS-001..004 is added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0. Tranche 5 draft, CONCEPT, not baselined. Changes require change control in later revisions.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 draft (Chapter 09.12) |
