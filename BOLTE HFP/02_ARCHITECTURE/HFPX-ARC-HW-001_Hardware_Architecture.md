# Hardware Architecture

**Document ID:** HFPX-ARC-HW-001  
**Revision:** B (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 2 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X hardware architecture (Chapter 02.5): computing separation, hardware classes, redundancy and built-in-test principles, and the hardware assurance approach. No components selected.

## 2. Scope

Covers flight computer and independent safety computer separation, sensor/actuator hardware classes, redundancy/BIT principles, and assurance structured according to DO-254 concepts. Excludes part numbers, quantities and quantitative reliability values (all TBD).

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parent requirements REQ-HFPX-SYS-001..008)
- HFPX-SYS-ARC-001 SAD (parent requirements REQ-HFPX-ARC-001..005)
- DO-254 concepts (structured-according-to only, no compliance claimed); Vol 08/13/15/16

## 4. Definitions & Acronyms

- Flight computer: primary control computing path. Safety computer: independent monitoring/stabilisation/recovery path.
- BIT: built-in test (power-up, continuous, initiated). Redundancy: duplication or segregation to tolerate defined faults (scope TBD).

## 5. System Context

Hardware architecture hosts logical functions in physical enclosures, powered by the electrical architecture and connected via avionics data/power interfaces. It operates across all flight and ground states within environmental conditions TBD.

## 6. Requirements

| ID | Requirement (shall) | Verification |
| --- | --- | --- |
| REQ-HFPX-HWA-001 | The hardware architecture shall separate the flight computer from an independent safety computer. | Analysis |
| REQ-HFPX-HWA-002 | The hardware architecture shall define sensor and actuator hardware classes (types TBD). | Inspection |
| REQ-HFPX-HWA-003 | The hardware architecture shall define redundancy and built-in-test principles (scope TBD). | Analysis |
| REQ-HFPX-HWA-004 | Hardware assurance shall be structured according to DO-254 concepts (no compliance claimed at this stage). | Inspection |

## 7. Architecture

Dual-path computing structure (starter; parts, counts and topologies TBD): primary path (sensors → flight computer → mixing/allocation → actuators) operates in parallel with an independent safety path (separate sensing/compute → stabilisation/recovery commanding). Sensor/actuator classes named by function only (inertial, air-data, position, actuator-drive classes TBD). Redundancy and BIT principles (coverage, independence, segregation) are defined as policy; implementation scope TBD. Assurance artefacts and lifecycle data items follow DO-254 structure without claiming compliance or DAL assignment.

## 8. Detailed Design

Not applicable at this level. Schematics, parts, pin-outs and enclosure designs are deferred to Vol 08 and subsystem docs. No components selected.

## 9. Interfaces

Hardware interfaces: compute power feeds (Vol 15), sensor/actuator electrical I/O, data-bus physical layers (Vol 08), mechanical mounting/thermal interfaces (Vol 03/17). Connector and signal definitions TBD in ICDs (02.17).

## 10. Operational Concept

Hardware supports all flight modes plus power-up BIT, continuous BIT and maintenance BIT states. Safety computer remains capable of independent stabilisation/recovery commanding whenever the system is powered in flight modes.

## 11. Safety

Independence of the safety computer from the primary path is a hardware-architecture constraint (ARC-003). Common-cause and common-mode considerations feed Vol 13 analyses. No reliability values stated.

## 12. Performance

Compute throughput, I/O capacity and BIT-coverage budgets are TBD. Budget holders: embedded computing/avionics (Vol 08), control (Vol 07). No values stated.

## 13. Verification & Validation

Verified by analysis (separation, redundancy/BIT principles) and inspection (class definitions, DO-254-structures artefacts list). Validated later by hardware test, SIL/HIL and environmental test (Vol 19).

## 14. Risks

- Independence claims undermined by shared power, clock or enclosure; mitigation: segregation analysis via Vol 13/15.
- BIT burden on availability misunderstood; mitigation: BIT policy tied to CONOPS and maintenance concept.

## 15. Open Issues

Sensor/actuator classes, redundancy scope, BIT coverage, segregation criteria and DAL-equivalent targets all TBD. Shared-resource independence analysis not started.

## 16. Assumptions


_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on LOG flows, avionics/power design (Vol 08/15), safety analyses (Vol 13), and software architecture (SW view). Subsystem sensor/actuator inputs from Vol 03–18.

## 18. Traceability

Parents: SyRS REQ-HFPX-SYS-001..008; SAD REQ-HFPX-ARC-001..005 (notably ARC-002/003/005). Children: Vol 03–18 subsystem docs, ICDs, V&V cases. RTM: REQ-HFPX-HWA-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 2 draft, not baselined. Chapter 02.5.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 2 draft (Chapter 02.5) |
| B | 2026-09-29 | Assumptions removed; all unknowns recorded as TBD (no assumptions raised or relied upon). |
