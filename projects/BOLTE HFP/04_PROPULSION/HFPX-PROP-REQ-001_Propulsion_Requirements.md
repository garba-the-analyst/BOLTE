# Propulsion System Requirements

**Document ID:** HFPX-PROP-REQ-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X propulsion system requirements (Chapter 04.1): distributed thrust functions for hover, transition and cruise, throttle/modulation behaviour, envelope operability, monitoring/protection hooks, maintainability hooks, and the verification thread. Structure only; all magnitudes and dynamic values TBD.

## 2. Scope

Covers propulsion system-level requirements, parents, and verification methods for the distributed arm/rear/ankle thrust system. Applies to all propulsion architecture and module documents in this volume (Ch 04.2–04.9).

> **Hazardous-subsystem boundary.** Content in this volume is limited to requirements, architecture, modelling, simulation, interfaces, test methodology and safety analysis ONLY. It contains NO instructions for constructing, igniting, testing with fuel, or operating high-energy propulsion outside controlled conditions.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parent requirements SYS-001, MIS-001..003)
- HFPX-ARC-PRP-001 Propulsion Architecture / HFPX-SYS-ARC-001 SAD (parent PRP-001)
- HFPX-PROP-ARC-001 Propulsion Architecture (Ch 04.2)
- Vol 07 (control/allocation), Vol 08 (monitoring), Vol 05 (fuel), Vol 14 (thermal), Vol 12 (human interfaces), Vol 13 (safety), Vol 19 (verification)

## 4. Definitions & Acronyms

- Distributed thrust: lift and control force from multiple arm, rear and ankle effectors (counts, positions and magnitudes TBD).
- Throttle/modulation: commanded change in thrust output of one or more effectors (response characteristics TBD).
- ISS-003: energy-source trade, NOT started — no selection made.
- TBD / TBC: to be defined / confirmed. No values stated.

## 5. System Context

The propulsion system converts stored energy into controlled distributed thrust within airframe, control, thermal, fuel and safety constraints. It receives allocation demands from Vol 07, reports health/capability to monitoring and fault logic, and executes thrust across hover, transition and cruise modes. Energy-source selection is pending ISS-003.

> **Hazardous-subsystem boundary.** This document addresses requirements, architecture context, interfaces and safety-analysis inputs only. It contains no build, ignition, fuelled-test, or operational procedures.

Energy-source candidates under ISS-003 (trade NOT started, no selection): jet-fuel / ethanol / hydrogen turbine, hydrogen-electric, battery-electric. Chain type, counts and all performance figures TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-PRQ-001 | The propulsion system shall provide distributed thrust for hover, transition and cruise modes (magnitudes, allocation and margins TBD). | SYS-001, MIS-001..003, PRP-001 | Analysis, Simulation |
| REQ-HFPX-PRQ-002 | The propulsion system shall provide throttle/modulation response to allocation commands (response characteristics TBD). | SYS-001, PRP-001 | Analysis, Simulation |
| REQ-HFPX-PRQ-003 | The propulsion system shall be operable across the defined flight envelope (envelope limits and derating TBD). | SYS-001, MIS-001..003 | Analysis |
| REQ-HFPX-PRQ-004 | The propulsion system shall provide monitoring and protection hooks for health, limits and fault logic (thresholds and ownership TBD). | SYS-001, PRP-001 | Inspection, Analysis |
| REQ-HFPX-PRQ-005 | The propulsion system shall provide maintainability hooks for inspection, servicing and module replacement (intervals and procedures TBD, maintenance conditions only). | SYS-001 | Inspection |
| REQ-HFPX-PRQ-006 | The propulsion system requirements shall be verified by review, analysis, simulation and controlled test methodology (no fuelled or high-energy operation outside controlled conditions). | PRP-001 | Inspection |

## 7. Architecture

System requirements decompose into propulsion architecture (Ch 04.2), turbine/microturbine/module requirements (Ch 04.3–04.7), vectoring (Ch 04.8) and propulsion control (Ch 04.9). Energy→thrust chain is TBD pending ISS-003. Control allocation ownership resides with Vol 07; monitoring interfaces feed Vol 08 and fault logic. No chain selection or sizing stated.

## 8. Detailed Design

Not applicable at this level. Effector designs, routing, mounts, sizing and controller implementations are deferred to Ch 04.2–04.9 and interfacing volumes. No design values stated.

## 9. Interfaces

Requirements interfaces: R-CMD (allocation demands, Vol 07), R-HLTH (health/status to Vol 08 and fault logic), R-FUEL (energy interfaces, Vol 05), R-THM (thermal interfaces, Vol 14), R-MECH (mounts/loads, Vol 03). Definitions TBD in ICDs.

> **Hazardous-subsystem boundary.** Interface requirements describe architectural boundaries and analysis inputs only, not build/ignition/fuelled-test/operation procedures.

## 10. Operational Concept

Propulsion requirements apply across all flight modes: hover (vertical thrust and control margins), transition (re-allocation dynamics) and cruise (efficiency and thermal behaviour). Start-up, shutdown and emergency sequencing concepts are TBD under Vol 07 / Ch 04.9 / Vol 13 control. Analysis and simulation only.

## 11. Safety

Propulsion requirements feed Vol 13 FHA/FMEA/FTA for loss of thrust, uncommanded thrust, and common-cause faults. Independent safety-path authority over propulsion limits and shutdown is preserved. Safety analysis only; no operating instructions.

> **Hazardous-subsystem boundary.** Safety content is limited to requirements and safety-analysis inputs. No instructions for constructing, igniting, testing with fuel, or operating high-energy propulsion outside controlled conditions.

## 12. Performance

Thrust magnitudes, throttle response, efficiency, operability limits and thermal budgets are TBD. Budget holders: propulsion (this volume, ISS-003/ISS-007 inputs), control authority (Vol 07, ISS-006), thermal (Vol 14). No values stated.

## 13. Verification & Validation

Verified by inspection (requirement definition, traceability), analysis and simulation (thrust functions, modulation, operability, monitoring hooks). Validated later via modelling, rig test methodology, SIL/HIL and unmanned flight (Vol 19). Test methodology only; no fuelled or high-energy operation outside controlled conditions.

## 14. Risks

- ISS-003 trade delay stalls propulsion-dependent requirements; mitigation: structure-only requirements with explicit TBDs.
- Envelope and allocation ownership ambiguity; mitigation: ownership fixed to Vol 07 with Vol 13 fault-response review.

## 15. Open Issues

ISS-003 (energy-source trade NOT started; candidates: jet-fuel/ethanol/hydrogen turbine, hydrogen-electric, battery-electric — no selection). Thrust magnitudes, modulation characteristics, envelope limits, monitoring thresholds, maintainability intervals and verification details all TBD.

## 16. Assumptions

- A-PRQ-001: Distributed arm/rear/ankle thrust partition is stable scaffolding pending ISS-003; validation: trade review.
- A-PRQ-002: Vol 07 can own allocation/mixing independent of chain selection; validation: Vol 07 review.

## 17. Dependencies

Depends on ISS-003 trade, SyRS/MIS parents, propulsion architecture (PRP-001), control allocation (Vol 07), monitoring (Vol 08), fuel/thermal inputs (Vol 05/14), airframe mounts (Vol 03), and safety analyses (Vol 13).

## 18. Traceability

Parents: SYS-001, MIS-001..003, PRP-001. Children: HFPX-PROP-ARC-001 (Ch 04.2), HFPX-PROP-TRB-001 (Ch 04.3), HFPX-PROP-MIC-001 (Ch 04.4), HFPX-PROP-ARM-001 (Ch 04.5), HFPX-PROP-RER-001 (Ch 04.6), HFPX-PROP-ANK-001 (Ch 04.7), HFPX-PROP-VEC-001 (Ch 04.8), HFPX-PROP-CTL-001 (Ch 04.9). RTM: REQ-HFPX-PRQ-001..006 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 4 draft, not baselined. Chapter 04.1.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (Chapter 04.1) |
