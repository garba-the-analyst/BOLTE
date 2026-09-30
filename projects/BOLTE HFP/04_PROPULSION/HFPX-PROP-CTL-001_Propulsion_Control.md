# Propulsion Control

**Document ID:** HFPX-PROP-CTL-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X propulsion control requirements (Chapter 04.9): engine-control ownership split, start/stop logic, limit protection, and control verification thread. Structure only; ownership boundaries, sequences and thresholds TBD.

## 2. Scope

Covers propulsion-control requirements spanning Vol 07 allocation, module controllers, monitoring, and safety-path authority. Does not select the energy source and does not authorise any fuelled activity.

> **Hazardous-subsystem boundary.** Content in this volume is limited to requirements, architecture, modelling, simulation, interfaces, test methodology and safety analysis ONLY. It contains NO instructions for constructing, igniting, testing with fuel, or operating high-energy propulsion outside controlled conditions.

## 3. Applicable Documents

- HFPX-PROP-REQ-001 Propulsion System Requirements (Ch 04.1)
- HFPX-PROP-ARC-001 Propulsion Architecture (Ch 04.2)
- HFPX-PROP-TRB-001 Turbine Architecture (Ch 04.3)
- Vol 07 (control/allocation), Vol 08 (monitoring), Vol 13 (safety), Vol 19 (verification)

## 4. Definitions & Acronyms

- Engine control: demand execution, sequencing and limit protection within propulsion modules and Vol 07 (ownership split TBD).
- Start/stop logic: ordered enabling and disabling of propulsion effectors (sequences and authority TBD).
- Limit protection: monitoring-driven protective response preserving module and system integrity (limits and thresholds TBD).
- ISS-003: energy-source trade, NOT started — no selection made.

## 5. System Context

Propulsion control executes allocation demands from Vol 07 across distributed arm/rear/ankle effectors, manages start/stop sequencing, enforces operating limits, and reports health/capability to monitoring and fault logic. Ownership is split between Vol 07 and module controllers (boundary TBD), with independent safety-path authority preserved per Vol 13. Chain selection is pending ISS-003.

> **Hazardous-subsystem boundary.** This document addresses requirements, architecture, interfaces and safety-analysis inputs only. It contains no build, ignition, fuelled-test, or operational procedures.

Energy-source candidates under ISS-003 (trade NOT started, no selection): jet-fuel / ethanol / hydrogen turbine, hydrogen-electric, battery-electric. Control laws, sequences, limits and all performance figures TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-PCT-001 | The propulsion control architecture shall define the engine-control ownership split between Vol 07 and module controllers with boundaries TBD. | REQ-HFPX-PRQ-002, REQ-HFPX-PAR-003 | Inspection |
| REQ-HFPX-PCT-002 | The propulsion control system shall define start/stop logic with sequences and authority TBD. | REQ-HFPX-PRQ-002, REQ-HFPX-PRQ-003 | Analysis, Simulation |
| REQ-HFPX-PCT-003 | The propulsion control system shall define limit protection with limits, thresholds and protective responses TBD. | REQ-HFPX-PRQ-004 | Analysis |
| REQ-HFPX-PCT-004 | The propulsion control system shall be verified by review, analysis, simulation, SIL/HIL and controlled test methodology with scope and criteria TBD. | REQ-HFPX-PRQ-006 | Inspection, Simulation, SIL/HIL |

## 7. Architecture

Control structure (ownership, laws and values TBD): Vol 07 allocation → propulsion control [Vol 07 functions | module controllers] → effectors [arm | rear | ankle] → thrust + health/limit feedback → monitoring (Vol 08) → fault response (Vol 13, independent safety path). Start/stop and limit-protection ownership boundaries are TBD and fixed here once agreed with Vol 07/13.

## 8. Detailed Design

Not applicable at this level. Control laws, gains, sequences, software/hardware implementation and limits are deferred to Vol 07 and module controller design. No design values stated.

## 9. Interfaces

Control interfaces: C-CMD (allocation demands from Vol 07), C-SEQ (start/stop commands, ownership TBD), C-LIM (limit/protection signals to/from Vol 08 and safety path), C-HLTH (health/capability to fault logic). Definitions TBD in ICDs.

> **Hazardous-subsystem boundary.** Interface definitions here describe architectural boundaries and analysis inputs only, not build/ignition/fuelled-test/operation procedures.

## 10. Operational Concept

Control behaviour is described for hover, transition and cruise modelling and simulation, including sequencing, derating and emergency shutdown concepts. Authority and sequences are TBD under Vol 07 / Vol 13 control. Analysis and simulation only.

## 11. Safety

Control hazards (loss of control, uncommanded thrust, sequencing faults, limit-protection failure, common-cause faults) feed Vol 13 FHA/FMEA/FTA. Independent safety-path authority over limits, shutdown and recovery is preserved. Analysis only; no operating instructions.

> **Hazardous-subsystem boundary.** Safety content is limited to requirements, architecture, test methodology and safety-analysis inputs. No instructions for constructing, igniting, testing with fuel, or operating high-energy propulsion outside controlled conditions.

## 12. Performance

Control response, sequencing timing, limit thresholds and protection dynamics are TBD. Budget holders: propulsion control (this volume / Vol 07), control authority (Vol 07, ISS-006). No values stated.

## 13. Verification & Validation

Verified by review (ownership split), analysis/simulation (start/stop logic, limit protection), SIL/HIL and review of controlled test methodology. Validated later via controlled rig testing and unmanned flight (Vol 19). Test methodology only; no fuelled or high-energy operation outside controlled conditions.

## 14. Risks

- Ownership-split ambiguity between Vol 07 and module controllers; mitigation: ownership table fixed here with Vol 07/13 review.
- ISS-003 trade delay stalls control-dependent design; mitigation: chain-agnostic control structure with explicit TBDs.

## 15. Open Issues

ISS-003 (energy-source trade NOT started; candidates: jet-fuel/ethanol/hydrogen turbine, hydrogen-electric, battery-electric — no selection). Ownership split, start/stop sequences, limit thresholds, protective responses and SIL/HIL/test details all TBD.

## 16. Assumptions

- A-PCT-001: Chain-agnostic control structure is stable scaffolding pending ISS-003; validation: trade review.
- A-PCT-002: Ownership split can be fixed between Vol 07 and module controllers independent of chain selection; validation: Vol 07 review.

## 17. Dependencies

Depends on Ch 04.1–04.3 requirements, ISS-003 trade, control allocation (Vol 07), monitoring (Vol 08), and safety/verification inputs (Vol 13/19).

## 18. Traceability

Parents: REQ-HFPX-PRQ-001..006, REQ-HFPX-PAR-003, REQ-HFPX-PTB-002/003. Children: ICDs, Vol 07/08/13 docs, Ch 04.4–04.8 companion docs. RTM: REQ-HFPX-PCT-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 4 draft, not baselined. Chapter 04.9.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (Chapter 04.9) |
