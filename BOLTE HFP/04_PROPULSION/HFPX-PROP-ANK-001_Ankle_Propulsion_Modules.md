# Ankle Propulsion Modules

**Document ID:** HFPX-PROP-ANK-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X ankle propulsion module requirements (Chapter 04.7): ankle-module thrust/control functions, leg-mount/mobility interfaces, failure response, and control-authority contribution. Structure only; all ratings and values TBD.

## 2. Scope

Covers leg/ankle-mounted propulsion modules as part of the distributed thrust system, including functional requirements, mobility constraints, and safety-analysis inputs. Does not select the energy source and does not authorise any fuelled activity.

> **Hazardous-subsystem boundary.** Content in this volume is limited to requirements, architecture, modelling, simulation, interfaces, test methodology and safety analysis ONLY. It contains NO instructions for constructing, igniting, testing with fuel, or operating high-energy propulsion outside controlled conditions.

## 3. Applicable Documents

- HFPX-PROP-REQ-001 Propulsion System Requirements (Ch 04.1)
- HFPX-PROP-ARC-001 Propulsion Architecture (Ch 04.2)
- HFPX-PROP-MIC-001 Microturbine Modules (Ch 04.4, if turbine branch selected)
- Vol 12.10 (leg-mount/mobility interfaces), Vol 07 (control, ISS-006), Vol 08 (monitoring), Vol 03 (airframe), Vol 13 (safety), Vol 19 (verification)

## 4. Definitions & Acronyms

- Ankle module: thrust unit mounted on leg/ankle structure (counts, positions, ratings and control contributions TBD).
- Leg-mount/mobility interface: mechanical and range-of-motion constraints between ankle modules, structure and pilot (loads and geometries TBD, Vol 12.10).
- ISS-006: control-authority allocation, pending — ankle contribution TBD.
- ISS-003: energy-source trade, NOT started — no selection made.

## 5. System Context

Ankle modules contribute distributed thrust and control moments within the arm/rear/ankle partition, with particular relevance to attitude control authority. They receive allocation demands from Vol 07, report health/capability, mount to leg structure within mobility constraints (Vol 12.10), and respond to fault logic under Vol 13 authority. Chain selection is pending ISS-003; authority allocation is pending ISS-006.

> **Hazardous-subsystem boundary.** This document addresses requirements, architecture, interfaces and safety-analysis inputs only. It contains no build, ignition, fuelled-test, or operational procedures.

Energy-source candidates under ISS-003 (trade NOT started, no selection): jet-fuel / ethanol / hydrogen turbine, hydrogen-electric, battery-electric. Module types, counts, ratings and all performance figures TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-PAN-001 | The ankle propulsion modules shall provide thrust and control functions per allocated demands with ratings and characteristics TBD. | REQ-HFPX-PRQ-001, REQ-HFPX-PAR-001 | Analysis, Simulation |
| REQ-HFPX-PAN-002 | The ankle propulsion modules shall define leg-mount and mobility interfaces per Vol 12.10 with loads and geometries TBD. | REQ-HFPX-PRQ-003 | Inspection |
| REQ-HFPX-PAN-003 | The ankle propulsion modules shall define failure responses with behaviours and authority TBD under Vol 13 fault logic. | REQ-HFPX-PRQ-004 | Analysis |
| REQ-HFPX-PAN-004 | The ankle propulsion modules shall define control-authority contributions with allocation TBD pending ISS-006. | REQ-HFPX-PRQ-001, REQ-HFPX-PRQ-002 | Analysis, Simulation |

## 7. Architecture

Ankle-module structure (selection, counts and values TBD): allocation demands (Vol 07) → ankle modules → thrust + moments → health/capability feedback → fault response (Vol 13). Control-authority contribution feeds Vol 07 allocation (ISS-006). Mounting interfaces feed Vol 03 and mobility constraints (Vol 12.10).

## 8. Detailed Design

Not applicable at this level. Module internal design, mount geometry and ratings are deferred pending ISS-003/ISS-006 and Vol 03/12 inputs. No design values stated.

## 9. Interfaces

Ankle-module interfaces: K-CMD (allocation demands, Vol 07), K-HLTH (health/capability to Vol 08 and fault logic), K-MECH (leg mounts/loads/mobility, Vol 03 and Vol 12.10), K-THM/K-FUEL (thermal/energy interfaces, Vol 14/05). Definitions TBD in ICDs.

> **Hazardous-subsystem boundary.** Interface definitions here describe architectural boundaries and analysis inputs only, not build/ignition/fuelled-test/operation procedures.

## 10. Operational Concept

Ankle-module behaviour is described for hover, transition and cruise modelling and simulation, including leg-mobility and ground-interaction considerations. Start, shutdown and emergency handling concepts are TBD under Ch 04.9 / Vol 07 / Vol 13 control. Analysis and simulation only.

## 11. Safety

Ankle-module hazards (loss of thrust, uncommanded thrust, mount failure, mobility interference, control-authority shortfall) feed Vol 13 FHA/FMEA/FTA. Independent safety-path authority over limits and shutdown is preserved. Analysis only; no operating instructions.

> **Hazardous-subsystem boundary.** Safety content is limited to requirements, architecture, test methodology and safety-analysis inputs. No instructions for constructing, igniting, testing with fuel, or operating high-energy propulsion outside controlled conditions.

## 12. Performance

Ankle-module thrust, control contributions, response and thermal behaviour are TBD (ISS-006 pending). Budget holders: propulsion (this volume), control authority (Vol 07, ISS-006), thermal (Vol 14). No values stated.

## 13. Verification & Validation

Verified by inspection (mount/mobility interface definitions) and analysis/simulation (thrust/control functions, failure responses, authority contributions). Validated later via modelling, controlled rig testing, SIL/HIL and unmanned flight (Vol 19). Test methodology only; no fuelled or high-energy operation outside controlled conditions.

## 14. Risks

- Leg-mount and mobility conflicts with pilot movement and ground interaction; mitigation: early Vol 12.10 interface review.
- ISS-003/ISS-006 trades delay authority and module-dependent design; mitigation: structure-only definitions with explicit TBDs.

## 15. Open Issues

ISS-003 (energy-source trade NOT started; candidates: jet-fuel/ethanol/hydrogen turbine, hydrogen-electric, battery-electric — no selection). ISS-006 (control-authority allocation pending; ankle contribution TBD). Ankle-module ratings, mounts, failure behaviours and verification details all TBD.

## 16. Assumptions

- A-PAN-001: Ankle-module partition is stable scaffolding pending ISS-003; validation: trade review.
- A-PAN-002: Mobility constraints can be bounded by Vol 12.10 independent of module selection; validation: Vol 12 review.

## 17. Dependencies

Depends on Ch 04.1/04.2 requirements, ISS-003 and ISS-006 trades, leg-mount/mobility interfaces (Vol 12.10), airframe mounts (Vol 03), control/monitoring (Vol 07/08), and safety/verification inputs (Vol 13/19).

## 18. Traceability

Parents: REQ-HFPX-PRQ-001..006, REQ-HFPX-PAR-001. Children: ICDs, Vol 03/12.10/07 (ISS-006)/13 docs, Ch 04.8/04.9 companion docs. RTM: REQ-HFPX-PAN-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 4 draft, not baselined. Chapter 04.7.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (Chapter 04.7) |
