# Arm Propulsion Modules

**Document ID:** HFPX-PROP-ARM-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X arm propulsion module requirements (Chapter 04.5): arm-module thrust/vectoring functions, pilot-load interfaces, failure response, and verification approach. Structure only; all ratings and values TBD.

## 2. Scope

Covers arm-mounted propulsion modules as part of the distributed thrust system, including functional requirements, human-interface constraints, and safety-analysis inputs. Does not select the energy source and does not authorise any fuelled activity.

> **Hazardous-subsystem boundary.** Content in this volume is limited to requirements, architecture, modelling, simulation, interfaces, test methodology and safety analysis ONLY. It contains NO instructions for constructing, igniting, testing with fuel, or operating high-energy propulsion outside controlled conditions.

## 3. Applicable Documents

- HFPX-PROP-REQ-001 Propulsion System Requirements (Ch 04.1)
- HFPX-PROP-ARC-001 Propulsion Architecture (Ch 04.2)
- HFPX-PROP-MIC-001 Microturbine Modules (Ch 04.4, if turbine branch selected)
- Vol 12.4 (pilot-load interfaces), Vol 07 (control), Vol 08 (monitoring), Vol 03 (airframe), Vol 13 (safety), Vol 19 (verification)

## 4. Definitions & Acronyms

- Arm module: thrust unit mounted on arm structure (counts, positions, ratings and vectoring ranges TBD).
- Pilot-load interface: mechanical/ergonomic constraints between arm modules, structure and pilot (loads and geometries TBD, Vol 12.4).
- ISS-003: energy-source trade, NOT started — no selection made.

## 5. System Context

Arm modules contribute distributed thrust and control moments within the arm/rear/ankle partition. They receive allocation demands from Vol 07, report health/capability, mount to arm structure within pilot-load constraints (Vol 12.4), and respond to fault logic under Vol 13 authority. Chain selection is pending ISS-003.

> **Hazardous-subsystem boundary.** This document addresses requirements, architecture, interfaces and safety-analysis inputs only. It contains no build, ignition, fuelled-test, or operational procedures.

Energy-source candidates under ISS-003 (trade NOT started, no selection): jet-fuel / ethanol / hydrogen turbine, hydrogen-electric, battery-electric. Module types, counts, ratings and all performance figures TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-PAM-001 | The arm propulsion modules shall provide thrust and vectoring functions per allocated demands with ratings and ranges TBD. | REQ-HFPX-PRQ-001, REQ-HFPX-PAR-001 | Analysis, Simulation |
| REQ-HFPX-PAM-002 | The arm propulsion modules shall define pilot-load interfaces per Vol 12.4 with loads and geometries TBD. | REQ-HFPX-PRQ-003 | Inspection |
| REQ-HFPX-PAM-003 | The arm propulsion modules shall define failure responses with behaviours and authority TBD under Vol 13 fault logic. | REQ-HFPX-PRQ-004 | Analysis |
| REQ-HFPX-PAM-004 | The arm propulsion modules shall be verified by analysis and controlled test methodology with scope and criteria TBD. | REQ-HFPX-PRQ-006 | Analysis, Test (methodology) |

## 7. Architecture

Arm-module structure (selection, counts and values TBD): allocation demands (Vol 07) → arm modules → thrust + moments → health/capability feedback → fault response (Vol 13). Vectoring commands interface via Ch 04.8 / Vol 07. Mounting interfaces feed Vol 03 and pilot-load constraints (Vol 12.4).

## 8. Detailed Design

Not applicable at this level. Module internal design, mount geometry, vectoring mechanisms and ratings are deferred pending ISS-003 and Vol 03/12 inputs. No design values stated.

## 9. Interfaces

Arm-module interfaces: A-CMD (allocation/vectoring demands, Vol 07 / Ch 04.8), A-HLTH (health/capability to Vol 08 and fault logic), A-MECH (mounts/loads, Vol 03 and Vol 12.4), A-THM/A-FUEL (thermal/energy interfaces, Vol 14/05). Definitions TBD in ICDs.

> **Hazardous-subsystem boundary.** Interface definitions here describe architectural boundaries and analysis inputs only, not build/ignition/fuelled-test/operation procedures.

## 10. Operational Concept

Arm-module behaviour is described for hover, transition and cruise modelling and simulation, including pilot-load and mobility considerations. Start, shutdown and emergency handling concepts are TBD under Ch 04.9 / Vol 07 / Vol 13 control. Analysis and simulation only.

## 11. Safety

Arm-module hazards (loss of thrust, uncommanded thrust/vectoring, mount failure, pilot-load exceedance) feed Vol 13 FHA/FMEA/FTA. Independent safety-path authority over limits and shutdown is preserved. Analysis only; no operating instructions.

> **Hazardous-subsystem boundary.** Safety content is limited to requirements, architecture, test methodology and safety-analysis inputs. No instructions for constructing, igniting, testing with fuel, or operating high-energy propulsion outside controlled conditions.

## 12. Performance

Arm-module thrust, vectoring ranges, response and thermal behaviour are TBD. Budget holders: propulsion (this volume), control authority (Vol 07, ISS-006), thermal (Vol 14). No values stated.

## 13. Verification & Validation

Verified by analysis (thrust/vectoring functions, failure responses) and review of controlled test methodology (scope and criteria TBD). Validated later via modelling, controlled rig testing, SIL/HIL and unmanned flight (Vol 19). Test methodology only; no fuelled or high-energy operation outside controlled conditions.

## 14. Risks

- Arm-module loads conflict with pilot ergonomics and mobility; mitigation: early Vol 12.4 interface review.
- ISS-003 trade delay stalls module-dependent design; mitigation: structure-only definitions with explicit TBDs.

## 15. Open Issues

ISS-003 (energy-source trade NOT started; candidates: jet-fuel/ethanol/hydrogen turbine, hydrogen-electric, battery-electric — no selection). Arm-module ratings, vectoring ranges, pilot-load limits, failure behaviours and verification details all TBD.

## 16. Assumptions

- A-PAM-001: Arm-module partition is stable scaffolding pending ISS-003; validation: trade review.
- A-PAM-002: Pilot-load constraints can be bounded by Vol 12.4 independent of module selection; validation: Vol 12 review.

## 17. Dependencies

Depends on Ch 04.1/04.2 requirements, ISS-003 trade, pilot-load interfaces (Vol 12.4), airframe mounts (Vol 03), control/vectoring (Vol 07 / Ch 04.8), monitoring (Vol 08), and safety/verification inputs (Vol 13/19).

## 18. Traceability

Parents: REQ-HFPX-PRQ-001..006, REQ-HFPX-PAR-001. Children: ICDs, Vol 03/12.4/07/13 docs, Ch 04.8/04.9 companion docs. RTM: REQ-HFPX-PAM-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 4 draft, not baselined. Chapter 04.5.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (Chapter 04.5) |
