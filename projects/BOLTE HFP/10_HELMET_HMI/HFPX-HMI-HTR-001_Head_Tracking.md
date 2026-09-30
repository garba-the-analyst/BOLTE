# Head Tracking

**Document ID:** HFPX-HMI-HTR-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define head-tracking requirements for Chapter 10.7. Tracking function, criteria, and loss-of-track behaviour are TBD at this revision.

## 2. Scope

Covers head-tracking function, accuracy and timing criteria, and loss-of-track behaviour. Excludes vision-assist consumers and display implementation.

## 3. Applicable Documents

- HFPX-SYS-STK-001 Stakeholder Requirements (REQ-HFPX-STK-007)
- HFPX-SYS-REQ-001 System Requirements (REQ-HFPX-SYS-005) — TBD
- HSA tier requirements — TBD
- HUM tier requirements — TBD
- HFPX-HMI-ARC-001 Helmet Architecture — TBD

## 4. Definitions & Acronyms

- TBD: To Be Determined
- Further tracking terms — TBD

## 5. System Context

Head tracking supports orientation of displayed and sensed functions relative to pilot head motion. Its function and failure handling are TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-HTT-001|The head-tracking function shall be defined, with functional content TBD.|REQ-HFPX-STK-007; REQ-HFPX-SYS-005; HSA; HUM|Inspection|
|REQ-HFPX-HTT-002|The head-tracking accuracy criteria shall be defined, with criteria TBD.|REQ-HFPX-STK-007; REQ-HFPX-SYS-005; HSA; HUM|Test|
|REQ-HFPX-HTT-003|The head-tracking timing criteria shall be defined, with criteria TBD.|REQ-HFPX-STK-007; REQ-HFPX-SYS-005; HSA; HUM|Inspection|
|REQ-HFPX-HTT-004|The loss-of-track behaviour shall be defined, with behaviour content TBD.|REQ-HFPX-STK-007; REQ-HFPX-SYS-005; HSA; HUM|Inspection|

## 7. Architecture

Allocation of head tracking to the helmet partition — TBD.

## 8. Detailed Design

Detailed tracking design — TBD. No values are stated at this revision.

## 9. Interfaces

Interfaces to display and sensing consumers — TBD.

## 10. Operational Concept

Tracking use across nominal and off-nominal operations — TBD.

## 11. Safety

Effect of track loss on displayed guidance — TBD. Further safety input — TBD.

## 12. Performance

Tracking performance criteria — TBD. No values are stated at this revision.

## 13. Verification & Validation

Verification methods and acceptance criteria — TBD.

## 14. Risks

- Accuracy and timing criteria defined before consumer needs are assigned; mitigation TBD
- Further risks — TBD

## 15. Open Issues

- Tracking function TBD
- Accuracy criteria TBD
- Timing criteria TBD
- Loss-of-track behaviour TBD

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on STK-007, SYS-005, HSA tier, HUM tier, HFPX-HMI-ARC-001, and display consumer definitions. Ownership and sequencing — TBD.

## 18. Traceability

Parents: REQ-HFPX-STK-007; REQ-HFPX-SYS-005; HSA tier; HUM tier. Children: TBD. Requirements REQ-HFPX-HTT-001..004 trace to parents as listed in §6.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Changes require change records once baselined.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 10.7) |
