# 09.16 Sensor Fault Detection

**Document ID:** HFPX-NAV-FDT-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the structure and subsystem requirements for sensor fault detection within Volume 09, Chapter 09.16. This revision establishes requirement placeholders only; detectable faults, detection methods, annunciation, and handover to fault-tolerant control are TBD. No design approval is implied.

## 2. Scope

Covers detectable-fault inventory, detection methods including thresholds and latency aspects, annunciation, and handover to fault-tolerant control.

Out of scope: FTC design (Vol 07.18); detailed detector implementation; hardware selection. No parts are selected at this revision.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parents REQ-HFPX-SYS-004 and related functional tier, including FUN-003 where applicable)
- HFPX-NAV-IDX-001 Volume 09 index / README (Chapter 09.16)
- Vol 07.18 fault-tolerant control reference (handover hooks TBD)
- VFD/VHM monitoring references (hooks TBD)
- HFPX-VV-PLN-001 V&V Plan (not written, verification cases TBD)
- Safety analyses references Vol 13 (SFA/CCA/FTA/FMEA hooks, details TBD)

## 4. Definitions & Acronyms

_TBD_

- FDT: Sensor Fault Detection chapter (09.16)
- NFD: fault detection requirement prefix (REQ-HFPX-NFD)
- TBD: to be determined; TBC: to be confirmed
- VFD/VHM: fault detection and health monitoring hooks TBD; FTC: fault-tolerant control (Vol 07.18)
- Verification methods: Analysis / Inspection / Demonstration / Test (allocation per requirement TBD)

## 5. System Context

Sensor fault detection supports integrity by identifying sensor faults and passing defined outputs to annunciation and fault-tolerant control consumers.

Context TBD. Allocation TBD. Relationship to functional tier FUN-003, to fusion (NSF) and algorithms (NNA) tiers, and to VFD/VHM TBD. Handover to Vol 07.18 TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-NFD-001 | The sensor fault detection function shall address a detectable-fault inventory TBD, including bias, drift, freeze, and loss aspects TBD. | REQ-HFPX-SYS-004, FUN-003, VFD/VHM hooks TBD | Analysis + Test (details TBD) |
| REQ-HFPX-NFD-002 | The sensor fault detection function shall implement detection methods TBD, including thresholds and latency aspects TBD. | REQ-HFPX-SYS-004, FUN-003 | Analysis + Test (details TBD) |
| REQ-HFPX-NFD-003 | The sensor fault detection function shall provide annunciation TBD. | REQ-HFPX-SYS-004, FUN-003, VFD/VHM hooks TBD | Test / Demonstration (details TBD) |
| REQ-HFPX-NFD-004 | The sensor fault detection function shall implement handover to FTC TBD, consistent with Vol 07.18 hooks TBD. | REQ-HFPX-SYS-004, FUN-003 | Analysis + Test (details TBD) |

No quantitative values are stated. All faults, thresholds, latencies, and test conditions are TBD.

## 7. Architecture

_TBD_

Detector placement, partitioning, and data flow TBD. Relationship to sensor architecture (09.1), fusion (09.13), and Vol 07.18 TBD. Structure only at this revision.

## 8. Detailed Design

_TBD_

No detailed design is defined. No detection algorithm or implementation is selected. No parts are selected at this revision.

## 9. Interfaces

_TBD_

Interfaces to sensors, fusion, annunciation consumers, VFD/VHM, and Vol 07.18 FTC TBD. ICD details TBD.

## 10. Operational Concept

_TBD_

Detection behaviour across flight phases and fault conditions TBD, including annunciation use TBD.

## 11. Safety

_TBD_

Safety relevance TBD. Hooks to SFA/CCA, FTA/FMEA, and VFD/VHM TBD. No safety claim is made at this revision.

## 12. Performance

_TBD_

All performance values including thresholds and latency TBD. No value in this document is approved.

## 13. Verification & Validation

_TBD_

Verification for REQ-HFPX-NFD-001..004 TBD, including fault injection and end-to-end handover demonstration TBD. Cases and acceptance criteria TBD in the V&V Plan.

## 14. Risks

- TBD density high: fault inventory and detection methods undefined; mitigation: placeholders established
- Handover to FTC undefined; mitigation: Vol 07.18 hook TBD

## 15. Open Issues

- Detectable-fault inventory TBD (bias / drift / freeze / loss)
- Detection methods TBD (thresholds / latency TBD)
- Annunciation TBD
- Detection-to-FTC handover TBD (Vol 07.18)

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on: functional tier FUN-003; sensor definitions (09.2 through 09.14); Vol 07.18 FTC definition; VFD/VHM definitions; V&V fault-injection capability; safety analyses Vol 13 outputs.

## 18. Traceability

Parents: REQ-HFPX-SYS-004, FUN-003. Hooks: VFD/VHM, SFA/CCA. Handover: Vol 07.18 TBD. Children: TBD (design, V&V cases, RTM rows). RTM seed for REQ-HFPX-NFD-001..004 is added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0. Tranche 5 draft, CONCEPT, not baselined. Changes require change control in later revisions.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 draft (Chapter 09.16) |
