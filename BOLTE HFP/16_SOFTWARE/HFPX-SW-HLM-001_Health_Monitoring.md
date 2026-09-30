# Health Monitoring

**Document ID:** HFPX-SW-HLM-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X health-monitoring software scope (Chapter 16.11): monitored-parameter inventory, threshold management, annunciation, and recording. No implementation stated.

## 2. Scope

Covers health-monitoring software requirements, architecture placement, interfaces, and verification planning. Monitored-parameter detail is TBD per Vol 08.10. Excludes sensor hardware design (Vol 08), fault-recovery authority (Vol 07/13 and Chapter 16.12), and detailed display design (Vol 10).

## 3. Applicable Documents

- Parent requirements: SYS-002 thread; WDP/WSA tier; VVP thread
- HFPX-ARC-SW-001 Software Architecture (layering, determinism policy, assurance structured according to DO-178C concepts)
- Vol 08 platform definition, notably Vol 08.10 (monitored-parameter inventory, TBD)
- Vol 10 HMI definition; Vol 16 sibling software chapters; Vol 13 safety inputs
- DO-178C concepts (structured-according-to only, no compliance claimed at this stage)

## 4. Definitions & Acronyms

- Monitored parameter: a software-observed quantity used for health assessment (inventory TBD per Vol 08.10).
- Threshold: a criterion applied to a monitored parameter to declare a health condition (values and hysteresis TBD).
- Annunciation: presentation of a health condition to crew or ground roles (mechanism and prioritisation TBD).
- Recording: capture of health data for maintenance and investigation (contents and retention TBD).

## 5. System Context

Health-monitoring software executes within the layered software architecture and interfaces with sensing, propulsion, power, communications, and display/logging services. It receives parameter inputs and produces health status, annunciation requests, and recording outputs across applicable flight and maintenance states (states and signals TBD).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-WHM-001 | The health-monitoring software shall observe a monitored-parameter inventory as defined in Vol 08.10 (inventory TBD). | SYS-002; WDP/WSA tier; VVP thread | Inspection |
| REQ-HFPX-WHM-002 | The health-monitoring software shall apply thresholds to monitored parameters to declare health conditions (thresholds TBD). | SYS-002; WDP/WSA tier; VVP thread | Analysis + Test |
| REQ-HFPX-WHM-003 | The health-monitoring software shall provide annunciation of declared health conditions (mechanism TBD). | SYS-002; WDP/WSA tier; VVP thread | Test |
| REQ-HFPX-WHM-004 | The health-monitoring software shall provide recording of health data (contents TBD). | SYS-002; WDP/WSA tier; VVP thread | Inspection + Test |

Software assurance is structured according to DO-178C concepts; no compliance is claimed at this stage and no integrity values are stated.

## 7. Architecture

Health-monitoring software resides in the application/services layers defined by HFPX-ARC-SW-001 (allocation TBD). Monitoring, threshold evaluation, annunciation generation, and recording functions are partitioned per determinism and independence policy (TBD). Languages, RTOS selection, and partitioning mechanisms are TBD.

## 8. Detailed Design

Not applicable at this revision. Software requirements, design descriptions, algorithms, and code are deferred to later Vol 16 detail. No implementation, logic, or parameter values stated.

## 9. Interfaces

Software interfaces to parameter sources, threshold-configuration services, annunciation consumers (Vol 10), and recording/logging services are TBD. Signatures, timing, and protocols are TBD and will be detailed in software ICDs and Vol 08.10.

## 10. Operational Concept

Health monitoring operates across power-up, flight-mode, degraded-mode, and maintenance states (behaviour per state TBD). Threshold application, annunciation, and recording remain available as defined per state (TBD). Nuisance-annunciation control policy is TBD.

## 11. Safety

Health-monitoring software safety inputs, hazard contributions, missed-detection and false-annunciation considerations feed Vol 13 analyses (all TBD). No integrity values stated. Determinism, boundedness, and partition independence remain architecture constraints per HFPX-ARC-SW-001.

## 12. Performance

Timing (sampling, detection latency), memory, and throughput budgets for health monitoring are TBD. Budget holders: software/compute (Vol 16/08). No values stated.

## 13. Verification & Validation

Verified by inspection (parameter inventory, recording provision) and analysis plus test (thresholds, annunciation), structured according to DO-178C concepts with no compliance claimed. Detailed verification cases, fault-injection hooks, and flight-test validation are TBD per the VVP thread and Vol 19/22/23.

## 14. Risks

- Parameter inventory incompleteness ahead of Vol 08.10 maturity; mitigation: TBD-gated requirement WHM-001.
- Threshold misclassification (missed detection or nuisance annunciation); mitigation: analysis and test requirement WHM-002 with Vol 13 review.
- Recording gaps limiting investigation; mitigation: recording requirement WHM-004 with retention policy TBD.

## 15. Open Issues

Monitored-parameter inventory per Vol 08.10 TBD. Threshold values, hysteresis, and tuning process TBD. Annunciation mechanism and prioritisation TBD. Recording contents, format, and retention TBD.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on Vol 08 platform definition (notably Vol 08.10), software architecture layering (HFPX-ARC-SW-001), HMI definition (Vol 10), fault-management coordination (Chapter 16.12), safety analyses (Vol 13), and VVP planning (Vol 22/23).

## 18. Traceability

Parents: SYS-002 thread; WDP/WSA tier; VVP thread. Children: subsystem software requirements, design descriptions, ICDs, V&V cases (all TBD). RTM: REQ-HFPX-WHM-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Chapter 16.11.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 16.11) |
