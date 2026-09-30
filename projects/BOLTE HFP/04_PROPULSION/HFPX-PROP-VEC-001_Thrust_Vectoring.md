# Thrust Vectoring

**Document ID:** HFPX-PROP-VEC-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X thrust-vectoring requirements (Chapter 04.8): vectoring functions and ranges, vectoring-command interfaces, fault response, and verification thread. Structure only; all ranges and values TBD.

## 2. Scope

Covers thrust-vectoring functions across arm, rear and ankle modules, including command ownership, fault handling, and safety-analysis inputs. Does not select the energy source and does not authorise any fuelled activity.

> **Hazardous-subsystem boundary.** Content in this volume is limited to requirements, architecture, modelling, simulation, interfaces, test methodology and safety analysis ONLY. It contains NO instructions for constructing, igniting, testing with fuel, or operating high-energy propulsion outside controlled conditions.

## 3. Applicable Documents

- HFPX-PROP-REQ-001 Propulsion System Requirements (Ch 04.1)
- HFPX-PROP-ARC-001 Propulsion Architecture (Ch 04.2)
- HFPX-PROP-ARM-001 / RER-001 / ANK-001 (Ch 04.5–04.7 placement docs)
- Vol 07.15/07.16 (vectoring-command interfaces), Vol 08 (monitoring), Vol 13 (safety), Vol 19 (verification)

## 4. Definitions & Acronyms

- Thrust vectoring: directed change of thrust orientation per effector (functions, axes and ranges TBD).
- Vectoring-command interface: allocation-to-effector command path for vectoring demands (signals and ownership TBD, Vol 07.15/07.16).
- ISS-003: energy-source trade, NOT started — no selection made.

## 5. System Context

Thrust vectoring converts allocation commands into oriented thrust across distributed effectors, producing lift and attitude moments in hover, transition and cruise. Vectoring demands originate from Vol 07 allocation, execute in arm/rear/ankle modules, and report position/health to monitoring and fault logic. Mechanism selection is pending ISS-003 and module trades.

> **Hazardous-subsystem boundary.** This document addresses requirements, architecture, interfaces and safety-analysis inputs only. It contains no build, ignition, fuelled-test, or operational procedures.

Energy-source candidates under ISS-003 (trade NOT started, no selection): jet-fuel / ethanol / hydrogen turbine, hydrogen-electric, battery-electric. Vectoring mechanisms, ranges and all performance figures TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-PVC-001 | The thrust-vectoring functions shall provide directed thrust per allocated demands with functions and ranges TBD. | REQ-HFPX-PRQ-001, REQ-HFPX-PRQ-002 | Analysis, Simulation |
| REQ-HFPX-PVC-002 | The thrust-vectoring system shall implement vectoring-command interfaces per Vol 07.15/07.16 with signals and ownership TBD. | REQ-HFPX-PRQ-002 | Inspection |
| REQ-HFPX-PVC-003 | The thrust-vectoring system shall define vectoring-fault responses with behaviours and authority TBD under Vol 13 fault logic. | REQ-HFPX-PRQ-004 | Analysis |
| REQ-HFPX-PVC-004 | The thrust-vectoring system shall be verified by SIL/HIL and controlled test methodology with scope and criteria TBD. | REQ-HFPX-PRQ-006 | SIL/HIL, Test (methodology) |

## 7. Architecture

Vectoring structure (mechanisms, counts and values TBD): allocation commands (Vol 07) → vectoring actuation per effector [arm | rear | ankle] → oriented thrust + moments → position/health feedback → fault response (Vol 13). Command ownership resides with Vol 07.15/07.16; execution and position reporting reside with propulsion modules.

## 8. Detailed Design

Not applicable at this level. Vectoring mechanisms, actuators, geometries and ratings are deferred pending ISS-003 and module trades. No design values stated.

## 9. Interfaces

Vectoring interfaces: V-CMD (vectoring demands, Vol 07.15/07.16), V-FB (position/health feedback to Vol 08 and fault logic), V-MECH (actuation mounts/loads, Vol 03), V-PWR (actuation power, as applicable, TBD). Definitions TBD in ICDs.

> **Hazardous-subsystem boundary.** Interface definitions here describe architectural boundaries and analysis inputs only, not build/ignition/fuelled-test/operation procedures.

## 10. Operational Concept

Vectoring behaviour is described for hover (attitude and translation control), transition (re-orientation dynamics) and cruise (trim and efficiency) modelling and simulation. Faulted-vectoring concepts (freeze, centre, shutdown) are TBD under Vol 13 authority. Analysis and simulation only.

## 11. Safety

Vectoring hazards (loss of vectoring, uncommanded vectoring, jam, hardover, common-cause faults) feed Vol 13 FHA/FMEA/FTA. Independent safety-path authority over vectoring limits and protective response is preserved. Analysis only; no operating instructions.

> **Hazardous-subsystem boundary.** Safety content is limited to requirements, architecture, test methodology and safety-analysis inputs. No instructions for constructing, igniting, testing with fuel, or operating high-energy propulsion outside controlled conditions.

## 12. Performance

Vectoring functions, ranges, rates, accuracy and thermal behaviour are TBD. Budget holders: propulsion (this volume), control authority (Vol 07, ISS-006). No values stated.

## 13. Verification & Validation

Verified by analysis/simulation (vectoring functions, fault responses) and SIL/HIL plus review of controlled test methodology (scope and criteria TBD). Validated later via controlled rig testing and unmanned flight (Vol 19). Test methodology only; no fuelled or high-energy operation outside controlled conditions.

## 14. Risks

- Vectoring-mechanism selection delay stalls control-dependent design; mitigation: structure-only definitions with explicit TBDs and Vol 07 interface review.
- Jam/hardover fault criticality; mitigation: early Vol 13 fault-response analysis.

## 15. Open Issues

ISS-003 (energy-source trade NOT started; candidates: jet-fuel/ethanol/hydrogen turbine, hydrogen-electric, battery-electric — no selection). Vectoring functions/ranges, command signal definitions, fault behaviours and SIL/HIL/test details all TBD.

## 16. Assumptions

- A-PVC-001: Vectoring-command ownership can reside with Vol 07.15/07.16 independent of mechanism selection; validation: Vol 07 review.
- A-PVC-002: SIL/HIL verification scaffolding can proceed before mechanism selection; validation: Vol 19 review.

## 17. Dependencies

Depends on Ch 04.1/04.2/04.5–04.7 requirements, ISS-003 trade, vectoring commands (Vol 07.15/07.16), monitoring (Vol 08), and safety/verification inputs (Vol 13/19).

## 18. Traceability

Parents: REQ-HFPX-PRQ-001..006. Children: ICDs, Vol 07.15/07.16/08/13 docs, Ch 04.5–04.7/04.9 companion docs. RTM: REQ-HFPX-PVC-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 4 draft, not baselined. Chapter 04.8.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (Chapter 04.8) |
