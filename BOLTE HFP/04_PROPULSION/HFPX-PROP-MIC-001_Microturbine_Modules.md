# Microturbine Modules

**Document ID:** HFPX-PROP-MIC-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X microturbine module requirements (Chapter 04.4): module performance structure, mounting/mechanical interfaces, service/inspection hooks, and module test methodology. Structure only; all ratings and values TBD.

## 2. Scope

Covers microturbine-module requirements, interfaces and test methodology as candidate thrust units within the turbine branch. Does not select the energy source and does not authorise any fuelled activity.

> **Hazardous-subsystem boundary.** Content in this volume is limited to requirements, architecture, modelling, simulation, interfaces, test methodology and safety analysis ONLY. It contains NO instructions for constructing, igniting, testing with fuel, or operating high-energy propulsion outside controlled conditions.

## 3. Applicable Documents

- HFPX-PROP-REQ-001 Propulsion System Requirements (Ch 04.1)
- HFPX-PROP-ARC-001 Propulsion Architecture (Ch 04.2)
- HFPX-PROP-TRB-001 Turbine Architecture (Ch 04.3)
- Vol 03.6 (mounting/mechanical interfaces), Vol 07 (control), Vol 08 (monitoring), Vol 05 (fuel), Vol 14 (thermal), Vol 13 (safety), Vol 19 (verification)

## 4. Definitions & Acronyms

- Microturbine module: small turbine-based thrust unit candidate (ratings, fuels and counts TBD).
- Bench test: controlled-condition rig evaluation of module behaviour (scope and conditions TBD, Vol 19).
- ISS-003: energy-source trade, NOT started — no selection made.

## 5. System Context

Microturbine modules are candidate effectors within the distributed arm/rear/ankle thrust system. Each module converts supplied energy into thrust under control demands, exposes health/limit status, and mounts to airframe structure within thermal and fuel constraints. Selection and sizing are pending ISS-003.

> **Hazardous-subsystem boundary.** This document addresses requirements, architecture, interfaces and safety-analysis inputs only. It contains no build, ignition, fuelled-test, or operational procedures.

Energy-source candidates under ISS-003 (trade NOT started, no selection): jet-fuel / ethanol / hydrogen turbine, hydrogen-electric, battery-electric. Module ratings, fuels, counts and all performance figures TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-PMC-001 | The microturbine modules shall provide thrust performance per allocated demands with ratings and characteristics TBD. | REQ-HFPX-PRQ-001, REQ-HFPX-PTB-001 | Analysis, Simulation |
| REQ-HFPX-PMC-002 | The microturbine modules shall define mounting and mechanical interfaces per Vol 03.6 with loads and geometries TBD. | REQ-HFPX-PRQ-003, REQ-HFPX-PAR-001 | Inspection |
| REQ-HFPX-PMC-003 | The microturbine modules shall provide service and inspection hooks with intervals and access TBD (maintenance conditions only). | REQ-HFPX-PRQ-005 | Inspection |
| REQ-HFPX-PMC-004 | The microturbine modules shall be evaluated by bench test methodology under controlled conditions with scope and pass criteria TBD. | REQ-HFPX-PRQ-006 | Inspection, Test (methodology) |

## 7. Architecture

Module structure (selection, counts and values TBD): energy inlet → microturbine module → thrust output + health/limit status → allocation feedback (Vol 07) and fault logic (Vol 13). Mounting interfaces feed Vol 03.6; thermal/fuel interfaces feed Vol 05/14. Redundancy and degraded-mode behaviour await ISS-003 and Vol 13 analysis.

## 8. Detailed Design

Not applicable at this level. Internal module design, materials, flow-path details and ratings are deferred pending ISS-003. No design values stated.

## 9. Interfaces

Module interfaces: M-CMD (demand/start-stop inputs, Vol 07 / Ch 04.9), M-HLTH (health/limit status to Vol 08 and fault logic), M-FUEL (energy interfaces, Vol 05), M-MECH (mounts/loads, Vol 03.6), M-THM (thermal interfaces, Vol 14). Definitions TBD in ICDs.

> **Hazardous-subsystem boundary.** Interface definitions here describe architectural boundaries and analysis inputs only, not build/ignition/fuelled-test/operation procedures.

## 10. Operational Concept

Module behaviour is described for hover, transition and cruise modelling and simulation. Start, shutdown, servicing and emergency handling concepts are TBD under Ch 04.9 / Vol 07 / Vol 13 control. Analysis and simulation only.

## 11. Safety

Module hazards (loss of thrust, uncommanded thrust, limit exceedance, mount failure) feed Vol 13 FHA/FMEA/FTA. Independent safety-path authority over limits and shutdown is preserved. Analysis only; no operating instructions.

> **Hazardous-subsystem boundary.** Safety content is limited to requirements, architecture, test methodology and safety-analysis inputs. No instructions for constructing, igniting, testing with fuel, or operating high-energy propulsion outside controlled conditions.

## 12. Performance

Module thrust, response, efficiency, operability and thermal behaviour are TBD. Budget holders: propulsion (this volume), control authority (Vol 07, ISS-006), thermal (Vol 14). No values stated.

## 13. Verification & Validation

Verified by inspection (interfaces, service hooks), analysis/simulation (performance structure), and review of bench test methodology (controlled conditions, scope and criteria TBD). Validated later via controlled rig testing, SIL/HIL and unmanned flight (Vol 19). Test methodology only; no fuelled or high-energy operation outside controlled conditions.

## 14. Risks

- ISS-003 trade delay stalls module-dependent design; mitigation: structure-only module definitions with explicit TBDs.
- Mounting and service-access conflicts with airframe; mitigation: early Vol 03.6 interface review.

## 15. Open Issues

ISS-003 (energy-source trade NOT started; candidates: jet-fuel/ethanol/hydrogen turbine, hydrogen-electric, battery-electric — no selection). Module ratings, mounts, service intervals, bench scope and pass criteria all TBD.

## 16. Assumptions

- A-PMC-001: Microturbine-module scaffolding can proceed without presuming ISS-003 selection; validation: trade review.
- A-PMC-002: Vol 03.6 mounting ownership can be fixed independent of module selection; validation: Vol 03 review.

## 17. Dependencies

Depends on Ch 04.1–04.3 requirements, ISS-003 trade, airframe mounts (Vol 03.6), control/monitoring (Vol 07/08), fuel/thermal inputs (Vol 05/14), and safety/verification inputs (Vol 13/19).

## 18. Traceability

Parents: REQ-HFPX-PRQ-001..006, REQ-HFPX-PTB-001. Children: Ch 04.5–04.7 placement docs, ICDs, Vol 03.6/05/07/08/14 docs. RTM: REQ-HFPX-PMC-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 4 draft, not baselined. Chapter 04.4.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (Chapter 04.4) |
