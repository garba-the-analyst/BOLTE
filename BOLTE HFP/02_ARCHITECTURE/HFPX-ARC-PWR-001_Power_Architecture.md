# Power Architecture

**Document ID:** HFPX-ARC-PWR-001  
**Revision:** B (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 2 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X power (electrical) architecture (Chapter 02.9): source classes, distribution/protection/grounding concepts, load feeds and EMI/EMC principles. Establishes structure only; no sources, ratings or topologies selected.

## 2. Scope

Covers primary, auxiliary, battery and emergency source classes (TBD), distribution/protection/grounding concepts (TBD), avionics/helmet/sensor feeds, and EMI/EMC principles per Vol 15. Excludes voltages, capacities, wire sizing and schematics (all TBD).

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parent requirements REQ-HFPX-SYS-001..008)
- HFPX-SYS-ARC-001 SAD (parent requirements REQ-HFPX-ARC-001..005)
- Vol 15 (electrical detail), Vol 08 (avionics loads), Vol 10 (helmet loads), HFP prompt §§11–13

## 4. Definitions & Acronyms

- Primary/auxiliary/battery/emergency: source roles by mission phase and failure state (ratings TBD).
- Distribution/protection/grounding: network, fault-interruption and reference-potential concepts (topology TBD).
- EMI/EMC: electromagnetic interference/compatibility principles governing emissions and susceptibility (limits TBD).

## 5. System Context

Power architecture energises all flight, ground and maintenance states, interfacing with propulsion energy (ISS-003), avionics/HMI/sensor loads, and the airframe grounding/thermal environment. It bounds normal, degraded and emergency power states.

## 6. Requirements

| ID | Requirement (shall) | Verification |
| --- | --- | --- |
| REQ-HFPX-PWR-001 | The power architecture shall define primary, auxiliary, battery, and emergency sources (ratings TBD). | Inspection |
| REQ-HFPX-PWR-002 | The power architecture shall define distribution, protection, and grounding concepts (topology TBD). | Analysis |
| REQ-HFPX-PWR-003 | The power architecture shall define avionics, helmet, and sensor power feeds (details TBD). | Inspection |
| REQ-HFPX-PWR-004 | The power architecture shall define EMI/EMC principles per Vol 15 (limits TBD). | Analysis |

## 7. Architecture

Power structure (starter; ratings, topologies and schematics TBD): source layer (primary/auxiliary/battery/emergency classes) → distribution layer (buses, protection, segregation of flight-critical vs mission loads) → load layer (avionics/compute, helmet/pilot interface, sensors, actuators, comms, ground interfaces). Safety-path loads receive independent or segregated feeds supporting ARC-003. Emergency source covers defined degraded states (scope TBD). Grounding and protection concepts ensure fault containment; EMI/EMC zoning and bonding principles per Vol 15.

## 8. Detailed Design

Not applicable at this level. Single-line diagrams, wire sizing, connector selection and load analysis are deferred to Vol 15 and ICDs. No electrical values stated.

## 9. Interfaces

Power interfaces: E-SRC (source outputs), E-DIST (bus/protection boundaries), E-LOAD (avionics/helmet/sensor/actuator feeds), E-GND (grounding/bonding), E-EMC (zoning/shielding). Definitions TBD in ICDs (02.17) and Vol 15.

## 10. Operational Concept

Power states track CONOPS modes plus ground servicing, BIT and emergency states. Source prioritisation and load-shedding concepts (TBD) preserve flight-critical and safety-path functions in degraded states.

## 11. Safety

Segregated safety-path feeds, protection selectivity and emergency-source availability support ARC-002/003. Electrical hazards and loss-of-power cases feed Vol 13/15 safety analyses. No safety values stated.

## 12. Performance

Capacity, load, transient and power-quality budgets are TBD. Budget holder: Vol 15 with load inputs from Vol 08/10/11. No values stated.

## 13. Verification & Validation

Verified by inspection (source/load coverage) and analysis (distribution/protection/grounding concepts, EMI/EMC principles). Validated later by load analysis, integration test and EMI/EMC test (Vol 15/19).

## 14. Risks

- Load growth exceeding TBD source capacity; mitigation: margin policy owned by Vol 15 from Tranche 2.
- EMI/EMC coupling across segregated paths; mitigation: zoning/bonding principles with test gating.

## 15. Open Issues

Source ratings, distribution topology, protection selectivity, load-shed priorities, grounding scheme and EMC limits all TBD. Load inventory incomplete.

## 16. Assumptions


_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on load inputs (Vol 08/10/11), propulsion energy trade (ISS-003), avionics interconnect (AVN view), safety analyses (Vol 13), and detailed electrical design (Vol 15).

## 18. Traceability

Parents: SyRS REQ-HFPX-SYS-001..008; SAD REQ-HFPX-ARC-001..005 (notably ARC-001/003/005). Children: Vol 03–18 subsystem docs (esp. Vol 15), ICDs, V&V cases. RTM: REQ-HFPX-PWR-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 2 draft, not baselined. Chapter 02.9.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 2 draft (Chapter 02.9) |
| B | 2026-09-29 | Assumptions removed; all unknowns recorded as TBD (no assumptions raised or relied upon). |
