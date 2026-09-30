# Propulsion Architecture

**Document ID:** HFPX-PROP-ARC-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X propulsion architecture (Chapter 04.2): arm/rear/ankle module partition, energy→thrust chain structure, control/monitoring interfaces, thermal/fuel interfaces, and architecture verification approach. Structure only; chain selection and all values TBD.

## 2. Scope

Covers propulsion architecture requirements, module partition, chain structure, and interface ownership for the distributed thrust system. Child of propulsion system requirements (Ch 04.1).

> **Hazardous-subsystem boundary.** Content in this volume is limited to requirements, architecture, modelling, simulation, interfaces, test methodology and safety analysis ONLY. It contains NO instructions for constructing, igniting, testing with fuel, or operating high-energy propulsion outside controlled conditions.

## 3. Applicable Documents

- HFPX-PROP-REQ-001 Propulsion System Requirements (Ch 04.1, REQ-HFPX-PRQ-001..006)
- HFPX-ARC-PRP-001 Propulsion Architecture (Vol 02)
- Vol 07 (control/allocation), Vol 08 (monitoring), Vol 05 (fuel), Vol 14 (thermal), Vol 03 (airframe), Vol 13 (safety)

## 4. Definitions & Acronyms

- Module partition: functional grouping into arm, rear and ankle propulsion modules (counts, positions and ratings TBD).
- Energy→thrust chain: stored energy → conditioning/distribution → effectors → thrust + moments (chain type TBD, ISS-003).
- ISS-003: energy-source trade, NOT started — no selection made.

## 5. System Context

Propulsion architecture converts stored energy into controlled distributed thrust within airframe, thermal, fuel and control constraints. It receives allocation commands from Vol 07, produces lift, attitude moments and health status, and exposes thermal/fuel interfaces to Vol 05/14. Chain selection is pending ISS-003.

> **Hazardous-subsystem boundary.** This document addresses requirements, architecture, interfaces and safety-analysis inputs only. It contains no build, ignition, fuelled-test, or operational procedures.

Energy-source candidates under ISS-003 (trade NOT started, no selection): jet-fuel / ethanol / hydrogen turbine, hydrogen-electric, battery-electric. All chain details and performance figures TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-PAR-001 | The propulsion architecture shall partition thrust functions into arm, rear and ankle modules (counts, positions and ratings TBD). | REQ-HFPX-PRQ-001 | Inspection |
| REQ-HFPX-PAR-002 | The propulsion architecture shall define the energy→thrust chain structure with chain type, conditioning and distribution TBD pending ISS-003 trade. | REQ-HFPX-PRQ-001, REQ-HFPX-PRQ-003 | Inspection |
| REQ-HFPX-PAR-003 | The propulsion architecture shall define control and monitoring interfaces to Vol 07 and Vol 08 (signals, ownership and thresholds TBD). | REQ-HFPX-PRQ-002, REQ-HFPX-PRQ-004 | Inspection |
| REQ-HFPX-PAR-004 | The propulsion architecture shall define thermal and fuel interfaces to Vol 05 and Vol 14 (flows, loads and limits TBD). | REQ-HFPX-PRQ-003, REQ-HFPX-PRQ-004 | Inspection |
| REQ-HFPX-PAR-005 | The propulsion architecture shall be verified by review and simulation with controlled test methodology (no fuelled or high-energy operation outside controlled conditions). | REQ-HFPX-PRQ-006 | Inspection, Simulation |

## 7. Architecture

Energy→thrust chain (structure only; chain type, counts and values TBD):

```text
STORED ENERGY (TBD, ISS-003) → CONDITIONING/DISTRIBUTION (TBD) → EFFECTORS [arm | rear | ankle] (TBD)
  → THRUST + MOMENTS (hover/transition/cruise demands from Vol 07 allocation)
  → MONITORING (health/thermal hooks → Vol 08 / fault logic) → FAULT RESPONSE (Vol 13)
```

Allocation/mixing is owned by Vol 07; propulsion executes demands and reports capability/health. Thermal hooks feed Vol 14; fuel interfaces feed Vol 05. Redundancy and degraded-mode behaviour await ISS-003 trade and Vol 13 analysis.

## 8. Detailed Design

Not applicable at this level. Module designs, plumbing/routing, mounts and controller implementations are deferred to Ch 04.3–04.9 with Vol 03/05/07/14 inputs. No design values stated.

## 9. Interfaces

Propulsion interfaces: P-CMD (allocation demands from Vol 07), P-HLTH (health/thermal status to Vol 08 and fault logic), P-FUEL (energy interfaces, Vol 05), P-MECH (mounts/loads, Vol 03), P-THM (thermal interfaces, Vol 14). Definitions TBD in ICDs.

> **Hazardous-subsystem boundary.** Interface definitions here describe architectural boundaries and analysis inputs only, not build/ignition/fuelled-test/operation procedures.

## 10. Operational Concept

Architecture functions execute across hover, transition and cruise. Hover stresses vertical thrust and control margins, transition stresses re-allocation dynamics, cruise stresses efficiency and thermal behaviour. Start-up/shutdown and emergency sequencing concepts are TBD under Ch 04.9 / Vol 07 / Vol 13 control.

## 11. Safety

Architecture fault detection, redundancy and abort/recovery commanding feed Vol 13 FHA/FMEA/FTA. Independent safety-path authority over propulsion limits and shutdown is preserved. Analysis only; no operating instructions.

> **Hazardous-subsystem boundary.** Safety content is limited to requirements, architecture and safety-analysis inputs. No instructions for constructing, igniting, testing with fuel, or operating high-energy propulsion outside controlled conditions.

## 12. Performance

Thrust allocation, efficiency, thermal loads and control-authority contributions are TBD. Budget holders: propulsion (this volume), control authority (Vol 07, ISS-006), thermal (Vol 14). No values stated.

## 13. Verification & Validation

Verified by review (partition, ownership, interfaces) and simulation (chain behaviour, allocation response, monitoring hooks). Validated later via modelling, rig test methodology, SIL/HIL and unmanned flight (Vol 19). Test methodology only; no operational procedures.

## 14. Risks

- ISS-003 trade delay stalls chain-dependent design; mitigation: structure-only architecture with explicit TBDs.
- Interface ownership ambiguity across Vol 05/07/08/14; mitigation: ownership table fixed here with ICD review.

## 15. Open Issues

ISS-003 (energy-source trade NOT started; candidates: jet-fuel/ethanol/hydrogen turbine, hydrogen-electric, battery-electric — no selection). Module counts/positions/ratings, conditioning/distribution details, interface signal definitions, and redundancy scope all TBD.

## 16. Assumptions

- A-PAR-001: Arm/rear/ankle partition is stable scaffolding pending ISS-003; validation: trade review.
- A-PAR-002: Vol 07/08 interface ownership can be fixed independent of chain selection; validation: Vol 07/08 review.

## 17. Dependencies

Depends on Ch 04.1 requirements, ISS-003 trade, control allocation/monitoring (Vol 07/08), fuel/thermal inputs (Vol 05/14), airframe mounts (Vol 03), and safety analyses (Vol 13).

## 18. Traceability

Parents: REQ-HFPX-PRQ-001..006 (notably PRQ-001/002/003/004/006). Children: Ch 04.3–04.9 module/vectoring/control docs, ICDs, Vol 05/07/08/14 subsystem docs. RTM: REQ-HFPX-PAR-001..005 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 4 draft, not baselined. Chapter 04.2.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (Chapter 04.2) |
