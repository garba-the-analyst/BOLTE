# Avionics Architecture

**Document ID:** HFPX-AVN-ARC-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X avionics architecture (Chapter 08.1): modular partition, flight/safety computer separation, sensor/actuator interface classes, and health-monitoring concept. No selections, topologies, or values stated.

## 2. Scope

Covers avionics modularity, separation principles, interface classes, health-monitoring concept, and architecture verification approach. Excludes computer design, hardware selection, scheduling, bus selection, and quantitative budgets (all TBD, deferred to Chapters 08.2–08.6 and linked volumes).

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parent requirements REQ-HFPX-SYS-002, REQ-HFPX-SYS-003, REQ-HFPX-SYS-005)
- HFPX-SYS-ARC-001 SAD (AVN, HWA, SWA, DAT views)
- HFPX-ARC-AVN-001 Avionics Architecture (Chapter 02.7 context)
- Vol 08 Chapters 08.2–08.6 (computer, hardware, real-time, bus detail)

## 4. Definitions & Acronyms

- Avionics partition: bounded grouping of avionics functions and interfaces defined by role.
- Separation: organisational and design independence between flight and safety computing paths.
- Interface class: role-based category of sensor/actuator interfaces without protocol selection.
- Health monitoring: continuous assessment of avionics health feeding fault logic.

## 5. System Context

The avionics architecture organises sensing, computing, actuation interfaces, and health monitoring across flight and maintenance states. It interfaces with power, structure/thermal environments, and RF links. All allocations, topologies, and mechanisms are TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-VAA-001|The avionics architecture shall define a modular partition of avionics functions (partition details TBD).|REQ-HFPX-SYS-002; SAD AVN view|Inspection|
|REQ-HFPX-VAA-002|The avionics architecture shall define separation between flight computing and safety computing paths (ownership of independence TBD).|REQ-HFPX-SYS-003; SAD AVN view|Inspection|
| REQ-HFPX-VAA-003 | The avionics architecture shall define sensor interface classes and actuator interface classes (selections TBD). | REQ-HFPX-SYS-002; SAD HWA view | Inspection |
| REQ-HFPX-VAA-004 | The avionics architecture shall define a health-monitoring concept for avionics nodes and linked subsystems (thresholds and mechanisms TBD). | REQ-HFPX-SYS-005; SAD AVN view | Analysis |
|REQ-HFPX-VAA-005|The avionics architecture shall be verified by review against parent requirements (evidence TBD).|REQ-HFPX-SYS-002; SAD AVN view|Inspection|

## 7. Architecture

Modular avionics organisation (details TBD): sensing, compute (flight plus safety), interface, and monitoring groupings. Flight/safety separation is stated as a principle with ownership of independence TBD. Sensor/actuator interfaces are named by class only. Health-monitoring concept links node and network health to fault logic. No topologies, parts, protocols, or values selected.

## 8. Detailed Design

Not applicable at this revision. Node designs, allocations, wiring, and packaging are deferred to Vol 08 detail chapters and ICDs.

## 9. Interfaces

Avionics interfaces by class: sensor inputs, actuator outputs, data exchanges, power feeds, and ground/test exchanges. Physical definitions, protocols, and connector details are TBD in ICDs.

## 10. Operational Concept

Avionics supports flight modes plus built-in test, degraded, and maintenance states. Health-monitoring functions remain available to support fault response and post-flight analysis (mechanisms TBD).

## 11. Safety

Separation and health-monitoring principles support parent safety intent. Failure annunciation and recording feed safety analyses. No safety values stated.

## 12. Performance

Budgets for capacity, timing, and availability are TBD. Budget holders are identified in linked Vol 08 chapters. No values stated.

## 13. Verification & Validation

Verified by review of architecture definitions against parent requirements, supported by analysis of health-monitoring coverage and inspection of interface classes. Integration test and SIL/HIL validation are deferred to later tranches.

## 14. Risks

- Partition instability as detail matures; mitigation: review gate before allocation.
- Health-monitoring gaps masking faults; mitigation: coverage analysis tied to safety analyses.

## 15. Open Issues

Partition details, separation ownership, interface selections, health-monitoring mechanisms, and verification evidence are all TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SyRS, SAD AVN/HWA/SWA/DAT views, Chapter 02.7 context, and Vol 08 detail chapters.

## 18. Traceability

Parents: REQ-HFPX-SYS-002, REQ-HFPX-SYS-003, REQ-HFPX-SYS-005; SAD AVN/HWA/SWA/DAT views. Children: Vol 08 Chapters 08.2–08.6 and ICDs. RTM: REQ-HFPX-VAA-001..005 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 5 draft, not baselined. Chapter 08.1.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 draft (Chapter 08.1) |
