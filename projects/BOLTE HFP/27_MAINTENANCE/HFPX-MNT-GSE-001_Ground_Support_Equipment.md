# Ground Support Equipment

**Document ID:** HFPX-MNT-GSE-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Specify ground support equipment for HFP-X maintenance, covering Chapter 27.13 Ground Support Equipment. This document owns GSE identification, calibration, availability, and usage-recording specifications.

## 2. Scope

Covers GSE required to support maintenance, including calibration, availability, and usage recording. GSE inventory TBD. Calibration TBD. Records TBD. Maintenance specifications only; no implementation design is implied.

## 3. Applicable Documents

- HFPX-SYS-STK-001 Stakeholder Requirements, including REQ-HFPX-STK-005
- HFPX-MNT-PRG-001 Maintenance Programme
- Maintainability classification (details TBD)
- Vol 24 RAMS artefacts (hooks TBD)
- Vol 28 ILS artefacts (hooks TBD)

## 4. Definitions & Acronyms

- GSE: ground support equipment enabling maintenance access, handling, test, and servicing
- Calibration: the defined assurance of measurement accuracy for applicable GSE
- Remaining terms TBD

## 5. System Context

GSE enables maintainers to execute tasks safely and consistently. Availability and accuracy of GSE constrain maintenance readiness; support integration is expected with Vol 28 (details TBD).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-LGE-001 | Ground support equipment required to support maintenance shall be identified (GSE inventory TBD). | REQ-HFPX-STK-005 | Inspection |
| REQ-HFPX-LGE-002 | Calibration needs for applicable ground support equipment shall be defined (calibration TBD). | REQ-HFPX-STK-005 | Inspection |
| REQ-HFPX-LGE-003 | Availability and serviceability needs for ground support equipment shall be defined (details TBD). | REQ-HFPX-STK-005 | Inspection |
| REQ-HFPX-LGE-004 | Ground support equipment usage associated with maintenance actions shall be recorded in accordance with the maintenance records process (records TBD). | REQ-HFPX-STK-005 | Inspection |

## 7. Architecture

GSE support structure TBD. Allocation of GSE to maintenance tasks TBD. Relationship to Vol 28 support structures TBD.

## 8. Detailed Design

Not applicable — GSE specification only. No design implementation is implied or authorised by this document.

## 9. Interfaces

- Interface to maintenance programme HFPX-MNT-PRG-001 (TBD)
- Interface to maintenance tasks employing GSE (TBD)
- Interface to maintenance records specification (TBD)
- Interface to Vol 24 and Vol 28 artefacts (TBD)

## 10. Operational Concept

GSE is provisioned, maintained, deployed to tasks, and accounted for through records. Operational flow TBD.

## 11. Safety

Safety implications of unserviceable or uncalibrated GSE TBD. Controls preventing use of unserviceable GSE TBD.

## 12. Performance

GSE availability expectations TBD. No limits are stated at this revision.

## 13. Verification & Validation

| Requirement | Method | Notes |
| --- | --- | --- |
| REQ-HFPX-LGE-001..004 | Inspection | GSE inventory, calibration, availability, and recording inspected (artefacts TBD) |
| GSE deployment and use | Demonstration | Deployment of GSE to maintenance tasks demonstrated where exercised (scope TBD) |

## 14. Risks

- Undefined GSE inventory may delay task readiness; mitigation TBD
- Undefined calibration may undermine measurement-dependent tasks; mitigation TBD

## 15. Open Issues

- GSE inventory TBD
- Calibration TBD
- Availability and serviceability TBD
- Records TBD

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

- REQ-HFPX-STK-005 stakeholder maintainability need
- HFPX-MNT-PRG-001 maintenance programme (TBD)
- Maintainability classification (details TBD)
- Vol 24 and Vol 28 inputs (TBD)

## 18. Traceability

Parents: REQ-HFPX-STK-005. Children: GSE specifications and associated verification cases (TBD). Hooks to Vol 24 and Vol 28 artefacts TBD.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Changes after issue require change records (process TBD).

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial draft (Chapter 27.13) |
