# Avionics Architecture

**Document ID:** HFPX-ARC-AVN-001  
**Revision:** B (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 2 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X avionics architecture (Chapter 02.7): modular avionics organisation, health monitoring, data/power/time interfaces and logging principles. No buses, parts or topologies selected.

## 2. Scope

Covers avionics modularity, health-monitoring concept, data-bus classes, power I/O, time-sync and logging principles. Excludes bus selection, wiring design and quantitative availability values (all TBD).

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parent requirements REQ-HFPX-SYS-001..008)
- HFPX-SYS-ARC-001 SAD (parent requirements REQ-HFPX-ARC-001..005)
- Vol 08 (avionics detail), Vol 11 (comms), Vol 13 (safety), Vol 15 (power)

## 4. Definitions & Acronyms

- Avionics: sensing, computing, communication and display electronics plus interconnect.
- Health monitoring: continuous assessment of avionics and linked-subsystem health feeding fault logic.
- Time sync: common time reference across avionics nodes for correlation and logging.

## 5. System Context

Avionics architecture interconnects sensors, computers, actuators, HMI and ground interfaces. It operates across all flight and maintenance states, interfacing with power distribution, structure/thermal environments and RF links (details TBD).

## 6. Requirements

| ID | Requirement (shall) | Verification |
| --- | --- | --- |
| REQ-HFPX-AVN-001 | The avionics architecture shall be modular with health monitoring of avionics nodes and linked subsystems. | Analysis |
| REQ-HFPX-AVN-002 | The avionics architecture shall define data-bus classes (selections TBD). | Inspection |
| REQ-HFPX-AVN-003 | The avionics architecture shall define power input/output interfaces (details TBD). | Inspection |
| REQ-HFPX-AVN-004 | The avionics architecture shall define time-synchronisation and logging principles. | Analysis |

## 7. Architecture

Modular avionics concept (starter; selections TBD): sensing nodes, compute nodes (flight + independent safety), HMI nodes (helmet/pilot interface), comms/telemetry nodes and ground-interface nodes. Health monitoring at node and network level feeds LOG-view fault logic (thresholds TBD Vol 13). Data-bus classes named by role (flight-critical, mission/telemetry, maintenance) with protocols and redundancy TBD. Power I/O classes feed from Vol 15 distribution (details TBD). Time-sync and logging principles ensure correlated fault/event records across nodes (mechanisms TBD Vol 08).

## 8. Detailed Design

Not applicable at this level. Node designs, bus topologies, wiring and packaging are deferred to Vol 08 and ICDs. No parts selected.

## 9. Interfaces

Avionics interfaces: data (bus physical/logical, TBD), power (feeds/returns/grounding, Vol 15), RF (Vol 11), mechanical/thermal (Vol 03/17), ground test/servicing (Vol 21/23). Definitions TBD in ICDs (02.17).

## 10. Operational Concept

Avionics supports all flight modes plus BIT, degraded/redundant, and maintenance download states. Health and logging functions remain available in degraded modes to support fault response and post-flight analysis.

## 11. Safety

Health monitoring and independent safety-node paths support ARC-003. Failure annunciation and recording feed Vol 13 safety analyses. AI-related avionics functions are advisory only (ARC-002). No safety values stated.

## 12. Performance

Bandwidth, latency, availability and power-draw budgets are TBD. Budget holders: avionics/data (Vol 08/16), power (Vol 15), safety (Vol 13). No values stated.

## 13. Verification & Validation

Verified by analysis (modularity/health-coverage argument, time-sync/logging principles) and inspection (bus/power interface definitions). Validated later by integration test, SIL/HIL and EMI/EMC test (Vol 19, Vol 15).

## 14. Risks

- Bus/protocol proliferation across nodes; mitigation: class discipline with selection gate at PDR.
- Health-monitoring gaps masking faults; mitigation: coverage analysis tied to Vol 13 FMEA.

## 15. Open Issues

Bus selections, redundancy topology, power I/O details, time-sync mechanism and log formats all TBD. Node inventory incomplete.

## 16. Assumptions


_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on HW/SW views, LOG flows, power design (Vol 15), comms design (Vol 11), safety analyses (Vol 13), and subsystem node inputs (Vol 03–18).

## 18. Traceability

Parents: SyRS REQ-HFPX-SYS-001..008; SAD REQ-HFPX-ARC-001..005 (notably ARC-002/003/005). Children: Vol 03–18 subsystem docs (esp. Vol 08/11/13/15), ICDs. RTM: REQ-HFPX-AVN-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 2 draft, not baselined. Chapter 02.7.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 2 draft (Chapter 02.7) |
| B | 2026-09-29 | Assumptions removed; all unknowns recorded as TBD (no assumptions raised or relied upon). |
