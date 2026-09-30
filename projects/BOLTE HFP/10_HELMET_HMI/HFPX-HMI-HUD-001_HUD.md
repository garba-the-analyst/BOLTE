# HUD

**Document ID:** HFPX-HMI-HUD-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define head-up display requirements for Chapter 10.3. Symbology, readability, and failure behaviour are TBD at this revision.

## 2. Scope

Covers HUD presentation, symbology set, readability criteria, and failure annunciation. Excludes pilot-display content (Chapter 10.4), navigation presentation (Chapter 10.9), and display hardware implementation.

## 3. Applicable Documents

- HFPX-SYS-STK-001 Stakeholder Requirements (REQ-HFPX-STK-007)
- HFPX-SYS-REQ-001 System Requirements (REQ-HFPX-SYS-005) — TBD
- HSA tier requirements — TBD
- HUM tier requirements — TBD
- HFPX-HMI-ARC-001 Helmet Architecture — TBD

## 4. Definitions & Acronyms

- HUD: Head-Up Display
- TBD: To Be Determined
- Further display terms — TBD

## 5. System Context

The HUD presents flight and alert symbology within the pilot field of view. Its content, readability context, and failure handling are TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-HUD-001 | The HUD function shall be defined, with functional content TBD. | REQ-HFPX-STK-007; REQ-HFPX-SYS-005; HSA; HUM | Demonstration |
| REQ-HFPX-HUD-002 | The HUD symbology set shall be defined, with set content TBD. | REQ-HFPX-STK-007; REQ-HFPX-SYS-005; HSA; HUM | Demonstration |
| REQ-HFPX-HUD-003 | The HUD readability criteria shall be defined, with criteria TBD. | REQ-HFPX-STK-007; REQ-HFPX-SYS-005; HSA; HUM | Test |
| REQ-HFPX-HUD-004 | HUD failures shall be annunciated, with annunciation content TBD. | REQ-HFPX-STK-007; REQ-HFPX-SYS-005; HSA; HUM | Test |

## 7. Architecture

Allocation of HUD to the helmet partition — TBD.

## 8. Detailed Design

Detailed HUD design — TBD. No optical, brightness, or dimensional values are stated at this revision.

## 9. Interfaces

HUD data-source interfaces — TBD. Interface to pilot display and warning system — TBD.

## 10. Operational Concept

HUD use across nominal and off-nominal operations — TBD.

## 11. Safety

Failure annunciation hooks — TBD. Misleading-display considerations — TBD.

## 12. Performance

Readability and availability criteria — TBD. No values are stated at this revision.

## 13. Verification & Validation

Verification by demonstration of HUD function and symbology and by test of readability and failure annunciation. Artefacts and acceptance criteria — TBD.

## 14. Risks

- Symbology and readability criteria defined before human-factors input is available; mitigation TBD
- Further risks — TBD

## 15. Open Issues

- HUD functional content TBD
- Symbology set TBD
- Readability criteria TBD
- Failure annunciation content TBD

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on STK-007, SYS-005, HSA tier, HUM tier, HFPX-HMI-ARC-001, and human-factors input. Ownership and sequencing — TBD.

## 18. Traceability

Parents: REQ-HFPX-STK-007; REQ-HFPX-SYS-005; HSA tier; HUM tier. Children: TBD. Requirements REQ-HFPX-HUD-001..004 trace to parents as listed in §6.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Changes require change records once baselined.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 10.3) |
