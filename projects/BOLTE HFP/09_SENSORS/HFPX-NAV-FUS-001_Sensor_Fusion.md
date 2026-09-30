# 09.13 Sensor Fusion

**Document ID:** HFPX-NAV-FUS-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the structure and subsystem requirements for sensor fusion within Volume 09, Chapter 09.13. This revision establishes requirement placeholders only; fusion functions, algorithm class, integrity, degraded-sensor handling, and verification are TBD. No algorithm selection or design approval is implied.

## 2. Scope

Covers fusion functions for attitude, velocity, and position, algorithm class definition, integrity monitoring, degraded-sensor handling, and fusion verification structure.

Out of scope: implementation of navigation algorithms (09.14); detailed filter design; software coding; sensor part selection. No algorithm is selected and no parts are selected at this revision.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parents REQ-HFPX-SYS-004 and related functional tier, including FUN-003 where applicable)
- HFPX-NAV-IDX-001 Volume 09 index / README (Chapter 09.13)
- Volume 09 sensor chapters 09.2 through 09.12 (fusion inputs, details TBD)
- HFPX-NAV-ALG-001 Navigation Algorithms (tier link TBD, Chapter 09.14)
- HFPX-VV-PLN-001 V&V Plan (not written, verification cases TBD)
- Safety analyses references Vol 13 (SFA/CCA/FTA hooks, details TBD); VFD/VHM monitoring hooks TBD

## 4. Definitions & Acronyms

_TBD_

- FUS: Sensor Fusion chapter (09.13)
- NSF: sensor fusion requirement prefix (REQ-HFPX-NSF)
- TBD: to be determined; TBC: to be confirmed
- Verification methods: Analysis / Inspection / Demonstration / Test (allocation per requirement TBD)

## 5. System Context

Sensor fusion combines data from inertial, GNSS, barometric, air data, and other sensor sources to produce navigation estimates used by flight control and monitoring functions.

Context TBD. Allocation TBD. Relationship to functional tier FUN-003 and to navigation algorithms tier NNA TBD. All input definitions and output consumers TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-NSF-001 | The sensor fusion function shall provide fusion functions TBD, including attitude, velocity, and position functions TBD. | REQ-HFPX-SYS-004, FUN-003 | Analysis + Test (simulation + test, details TBD) |
| REQ-HFPX-NSF-002 | The sensor fusion function shall implement an algorithm class TBD; no algorithm selection is made at this revision. | REQ-HFPX-SYS-004, FUN-003 | Analysis (details TBD) |
| REQ-HFPX-NSF-003 | The sensor fusion function shall provide integrity monitoring TBD. | REQ-HFPX-SYS-004, FUN-003, VFD/VHM hooks TBD | Analysis + Test (details TBD) |
| REQ-HFPX-NSF-004 | The sensor fusion function shall implement degraded-sensor handling TBD. | REQ-HFPX-SYS-004, FUN-003, SFA/CCA hooks TBD | Analysis + Test (details TBD) |
| REQ-HFPX-NSF-005 | The sensor fusion function shall be verified by means TBD, including simulation and test TBD. | REQ-HFPX-SYS-004, FUN-003 | Analysis + Test (simulation + test, details TBD) |

No quantitative values are stated. All functions, thresholds, and test conditions are TBD. No algorithm selection is made.

## 7. Architecture

_TBD_

Fusion placement, partitioning, and data flow TBD. Relationship to sensor architecture (09.1) and navigation algorithms (09.14) TBD. Structure only at this revision.

## 8. Detailed Design

_TBD_

No detailed design is defined. No algorithm, library, or implementation is selected. No parts are selected at this revision.

## 9. Interfaces

_TBD_

Input interfaces from Volume 09 sensors TBD. Output interfaces to flight control, navigation algorithms, and monitoring (VFD/VHM hooks) TBD. ICD details TBD.

## 10. Operational Concept

_TBD_

Fusion behaviour across flight phases, initialisation, and degraded-sensor conditions TBD.

## 11. Safety

_TBD_

Safety relevance TBD. Hooks to SFA/CCA, FTA/FMEA, and VFD/VHM TBD. Integrity and degraded-sensor claims TBD. No safety claim is made at this revision.

## 12. Performance

_TBD_

All performance values TBD. No value in this document is approved.

## 13. Verification & Validation

_TBD_

Verification for REQ-HFPX-NSF-001..005 by simulation and test TBD. Simulation environment, scenarios, facilities, and acceptance criteria TBD in the V&V Plan.

## 14. Risks

- TBD density high: fusion functions and algorithm class undefined; mitigation: placeholders established, selection deferred to later revisions
- Integrity and degraded-sensor handling undefined; mitigation: SFA/CCA and VFD/VHM hooks TBD

## 15. Open Issues

- Fusion functions TBD (attitude / velocity / position)
- Algorithm class TBD (no selection)
- Integrity monitoring TBD
- Degraded-sensor handling TBD
- Fusion verification TBD (simulation + test)

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on: functional tier FUN-003; sensor input definitions (09.2 through 09.12); navigation algorithms tier NNA (09.14); V&V simulation capability; safety analyses Vol 13 outputs; VFD/VHM monitoring definitions.

## 18. Traceability

Parents: REQ-HFPX-SYS-004, FUN-003. Tier links: NSF to NNA TBD. Hooks: VFD/VHM, SFA/CCA TBD. Children: TBD (design, V&V cases, RTM rows). RTM seed for REQ-HFPX-NSF-001..005 is added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0. Tranche 5 draft, CONCEPT, not baselined. Changes require change control in later revisions.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 draft (Chapter 09.13) |
