# Rear Propulsion Modules

**Document ID:** HFPX-PROP-RER-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X rear propulsion module requirements (Chapter 04.6): rear-module thrust functions, torso-mount interfaces, thermal/exhaust interfaces, and failure response. Structure only; all ratings and values TBD.

## 2. Scope

Covers torso/rear-mounted propulsion modules as part of the distributed thrust system, including functional requirements, mounting constraints, and safety-analysis inputs. Does not select the energy source and does not authorise any fuelled activity.

> **Hazardous-subsystem boundary.** Content in this volume is limited to requirements, architecture, modelling, simulation, interfaces, test methodology and safety analysis ONLY. It contains NO instructions for constructing, igniting, testing with fuel, or operating high-energy propulsion outside controlled conditions.

## 3. Applicable Documents

- HFPX-PROP-REQ-001 Propulsion System Requirements (Ch 04.1)
- HFPX-PROP-ARC-001 Propulsion Architecture (Ch 04.2)
- HFPX-PROP-MIC-001 Microturbine Modules (Ch 04.4, if turbine branch selected)
- Vol 14.2/14.3 (thermal/exhaust interfaces), Vol 07 (control), Vol 08 (monitoring), Vol 03 (airframe), Vol 13 (safety), Vol 19 (verification)

## 4. Definitions & Acronyms

- Rear module: thrust unit mounted on torso/rear structure (counts, positions and ratings TBD).
- Torso-mount interface: mechanical constraints between rear modules and torso structure (loads and geometries TBD).
- Thermal/exhaust interface: heat-rejection and exhaust routing boundaries with Vol 14 (loads and routes TBD).
- ISS-003: energy-source trade, NOT started — no selection made.

## 5. System Context

Rear modules contribute distributed thrust and control moments within the arm/rear/ankle partition. They receive allocation demands from Vol 07, report health/capability, mount to torso structure, and reject heat/route exhaust via Vol 14 interfaces. Chain selection is pending ISS-003.

> **Hazardous-subsystem boundary.** This document addresses requirements, architecture, interfaces and safety-analysis inputs only. It contains no build, ignition, fuelled-test, or operational procedures.

Energy-source candidates under ISS-003 (trade NOT started, no selection): jet-fuel / ethanol / hydrogen turbine, hydrogen-electric, battery-electric. Module types, counts, ratings and all performance figures TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-PRR-001 | The rear propulsion modules shall provide thrust functions per allocated demands with ratings and characteristics TBD. | REQ-HFPX-PRQ-001, REQ-HFPX-PAR-001 | Analysis, Simulation |
| REQ-HFPX-PRR-002 | The rear propulsion modules shall define torso-mount interfaces with loads and geometries TBD. | REQ-HFPX-PRQ-003 | Inspection |
| REQ-HFPX-PRR-003 | The rear propulsion modules shall define thermal and exhaust interfaces per Vol 14.2/14.3 with loads and routes TBD. | REQ-HFPX-PRQ-003, REQ-HFPX-PRQ-004 | Inspection |
| REQ-HFPX-PRR-004 | The rear propulsion modules shall define failure responses with behaviours and authority TBD under Vol 13 fault logic. | REQ-HFPX-PRQ-004 | Analysis |

## 7. Architecture

Rear-module structure (selection, counts and values TBD): allocation demands (Vol 07) → rear modules → thrust + moments → health/capability feedback → fault response (Vol 13). Mounting interfaces feed Vol 03; thermal/exhaust interfaces feed Vol 14.2/14.3. Redundancy and degraded-mode behaviour await ISS-003 and Vol 13 analysis.

## 8. Detailed Design

Not applicable at this level. Module internal design, mount geometry, exhaust routing and ratings are deferred pending ISS-003 and Vol 03/14 inputs. No design values stated.

## 9. Interfaces

Rear-module interfaces: R-CMD (allocation demands, Vol 07), R-HLTH (health/capability to Vol 08 and fault logic), R-MECH (torso mounts/loads, Vol 03), R-THM (thermal/exhaust interfaces, Vol 14.2/14.3), R-FUEL (energy interfaces, Vol 05). Definitions TBD in ICDs.

> **Hazardous-subsystem boundary.** Interface definitions here describe architectural boundaries and analysis inputs only, not build/ignition/fuelled-test/operation procedures.

## 10. Operational Concept

Rear-module behaviour is described for hover, transition and cruise modelling and simulation, including thermal/exhaust effects on structure and pilot environment. Start, shutdown and emergency handling concepts are TBD under Ch 04.9 / Vol 07 / Vol 13 control. Analysis and simulation only.

## 11. Safety

Rear-module hazards (loss of thrust, uncommanded thrust, mount failure, thermal/exhaust exceedance) feed Vol 13 FHA/FMEA/FTA. Independent safety-path authority over limits and shutdown is preserved. Analysis only; no operating instructions.

> **Hazardous-subsystem boundary.** Safety content is limited to requirements, architecture, test methodology and safety-analysis inputs. No instructions for constructing, igniting, testing with fuel, or operating high-energy propulsion outside controlled conditions.

## 12. Performance

Rear-module thrust, response, efficiency and thermal/exhaust behaviour are TBD. Budget holders: propulsion (this volume), control authority (Vol 07, ISS-006), thermal (Vol 14). No values stated.

## 13. Verification & Validation

Verified by inspection (mount and thermal/exhaust interface definitions) and analysis/simulation (thrust functions, failure responses). Validated later via modelling, controlled rig testing, SIL/HIL and unmanned flight (Vol 19). Test methodology only; no fuelled or high-energy operation outside controlled conditions.

## 14. Risks

- Torso-mount and thermal/exhaust routing conflicts with structure and pilot environment; mitigation: early Vol 03 and Vol 14.2/14.3 interface review.
- ISS-003 trade delay stalls module-dependent design; mitigation: structure-only definitions with explicit TBDs.

## 15. Open Issues

ISS-003 (energy-source trade NOT started; candidates: jet-fuel/ethanol/hydrogen turbine, hydrogen-electric, battery-electric — no selection). Rear-module ratings, mounts, thermal/exhaust loads and routes, failure behaviours and verification details all TBD.

## 16. Assumptions

- A-PRR-001: Rear-module partition is stable scaffolding pending ISS-003; validation: trade review.
- A-PRR-002: Thermal/exhaust interfaces can be bounded by Vol 14.2/14.3 independent of module selection; validation: Vol 14 review.

## 17. Dependencies

Depends on Ch 04.1/04.2 requirements, ISS-003 trade, torso mounts (Vol 03), thermal/exhaust interfaces (Vol 14.2/14.3), control/monitoring (Vol 07/08), and safety/verification inputs (Vol 13/19).

## 18. Traceability

Parents: REQ-HFPX-PRQ-001..006, REQ-HFPX-PAR-001. Children: ICDs, Vol 03/14.2/14.3/07/13 docs, Ch 04.9 companion doc. RTM: REQ-HFPX-PRR-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 4 draft, not baselined. Chapter 04.6.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (Chapter 04.6) |
