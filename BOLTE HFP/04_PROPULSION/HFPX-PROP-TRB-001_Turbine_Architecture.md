# Turbine Architecture

**Document ID:** HFPX-PROP-TRB-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X turbine architecture (Chapter 04.3): turbine-module classes, start/shutdown sequencing ownership, operating-limits protection, and the trade-study input rule pending ISS-003. Structure only; no selection or values stated.

## 2. Scope

Covers turbine-architecture requirements and ownership for turbine-based propulsion options, as one candidate branch of the ISS-003 trade. Does not select the energy source and does not authorise any fuelled activity.

> **Hazardous-subsystem boundary.** Content in this volume is limited to requirements, architecture, modelling, simulation, interfaces, test methodology and safety analysis ONLY. It contains NO instructions for constructing, igniting, testing with fuel, or operating high-energy propulsion outside controlled conditions.

## 3. Applicable Documents

- HFPX-PROP-REQ-001 Propulsion System Requirements (Ch 04.1)
- HFPX-PROP-ARC-001 Propulsion Architecture (Ch 04.2)
- Vol 07 (control), Vol 08 (monitoring), Vol 05 (fuel), Vol 14 (thermal), Vol 13 (safety)

## 4. Definitions & Acronyms

- Turbine-module class: functional category of turbine-based thrust unit (classes, ratings and fuels TBD).
- Start/shutdown sequencing: ordered logic for enabling and disabling turbine modules (ownership and sequences TBD).
- Operating-limits protection: limit monitoring and protective response preserving module and system integrity (limits and thresholds TBD).
- ISS-003: energy-source trade, NOT started — no selection made.

## 5. System Context

Turbine architecture defines one candidate energy→thrust branch within the propulsion architecture. If selected by the ISS-003 trade, turbine modules would convert chemical energy into thrust within control, fuel, thermal and safety constraints. Until the trade completes, this document defines structure, ownership and analysis inputs only.

> **Hazardous-subsystem boundary.** This document addresses requirements, architecture, interfaces and safety-analysis inputs only. It contains no build, ignition, fuelled-test, or operational procedures.

Energy-source candidates under ISS-003 (trade NOT started, no selection): jet-fuel / ethanol / hydrogen turbine, hydrogen-electric, battery-electric. Turbine classes, fuels, counts and all performance figures TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-PTB-001 | The turbine architecture shall define turbine-module classes with ratings, fuels and integration roles TBD. | REQ-HFPX-PRQ-001, REQ-HFPX-PAR-002 | Inspection |
| REQ-HFPX-PTB-002 | The turbine architecture shall define start/shutdown sequencing ownership with sequences and authority TBD. | REQ-HFPX-PRQ-002, REQ-HFPX-PRQ-003 | Inspection |
| REQ-HFPX-PTB-003 | The turbine architecture shall define operating-limits protection with limits, thresholds and protective responses TBD. | REQ-HFPX-PRQ-004 | Analysis |
|REQ-HFPX-PTB-004|The turbine architecture shall provide trade-study inputs per the ISS-003 input rule without selecting the energy source.|REQ-HFPX-PRQ-006, REQ-HFPX-PAR-002|Inspection|

## 7. Architecture

Turbine branch (structure only; selection, counts and values TBD):

```text
FUEL/ENERGY (TBD, ISS-003) → TURBINE MODULES [classes TBD] → THRUST (arm/rear/ankle allocation TBD)
  → MONITORING/LIMITS (hooks → Vol 08 / fault logic) → PROTECTION/RESPONSE (ownership TBD, Vol 13)
```

Start/shutdown sequencing ownership is TBD between module controllers and Vol 07 (see Ch 04.9). Operating-limits protection interfaces with monitoring (Vol 08) and thermal/fuel constraints (Vol 05/14). No fuels, ratings or sequences selected.

## 8. Detailed Design

Not applicable at this level. Turbine internal design, combustor/flow-path details, materials and ratings are deferred pending ISS-003 and module documents (Ch 04.4). No design values stated.

## 9. Interfaces

Turbine interfaces: T-CMD (start/stop and demand inputs, Vol 07 / Ch 04.9), T-HLTH (health/limit status to Vol 08 and fault logic), T-FUEL (fuel interfaces, Vol 05), T-THM (thermal/exhaust interfaces, Vol 14). Definitions TBD in ICDs.

> **Hazardous-subsystem boundary.** Interface definitions here describe architectural boundaries and analysis inputs only, not build/ignition/fuelled-test/operation procedures.

## 10. Operational Concept

Turbine sequencing concepts (start, shutdown, relight policy, emergency shutdown authority) are TBD under Ch 04.9 / Vol 07 / Vol 13 control. Operational behaviour is described for modelling and simulation only; no operating procedures stated.

## 11. Safety

Turbine hazards (loss of thrust, uncommanded thrust, limit exceedance, common-cause faults) feed Vol 13 FHA/FMEA/FTA. Independent safety-path authority over limits and shutdown is preserved. Analysis only; no operating instructions.

> **Hazardous-subsystem boundary.** Safety content is limited to requirements, architecture and safety-analysis inputs. No instructions for constructing, igniting, testing with fuel, or operating high-energy propulsion outside controlled conditions.

## 12. Performance

Turbine ratings, response characteristics, efficiency, operability limits and thermal behaviour are TBD. Budget holders: propulsion (this volume), control authority (Vol 07, ISS-006), thermal (Vol 14). No values stated.

## 13. Verification & Validation

Verified by inspection (class definitions, ownership) and analysis/simulation (sequencing concepts, limit-protection logic). Validated later via modelling, controlled rig test methodology, SIL/HIL and unmanned flight (Vol 19). Test methodology only; no fuelled or high-energy operation outside controlled conditions.

## 14. Risks

- ISS-003 trade delay stalls turbine-dependent design; mitigation: structure-only architecture with explicit TBDs and input rule.
- Sequencing/protection ownership ambiguity; mitigation: ownership fixed via Ch 04.9 and Vol 07/13 review.

## 15. Open Issues

ISS-003 (energy-source trade NOT started; candidates: jet-fuel/ethanol/hydrogen turbine, hydrogen-electric, battery-electric — no selection). Turbine classes, ratings, fuels, sequencing, limits and protection details all TBD.

## 16. Assumptions

- A-PTB-001: Turbine-branch scaffolding can proceed in parallel with ISS-003 without presuming selection; validation: trade review.
- A-PTB-002: Start/shutdown and protection ownership can be allocated between module controllers and Vol 07; validation: Ch 04.9 / Vol 07 review.

## 17. Dependencies

Depends on Ch 04.1/04.2 requirements, ISS-003 trade, propulsion control (Ch 04.9), monitoring (Vol 08), fuel/thermal inputs (Vol 05/14), and safety analyses (Vol 13).

## 18. Traceability

Parents: REQ-HFPX-PRQ-001..006, REQ-HFPX-PAR-002. Children: HFPX-PROP-MIC-001 (Ch 04.4), HFPX-PROP-CTL-001 (Ch 04.9), ICDs, Vol 05/07/08/14 docs. RTM: REQ-HFPX-PTB-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 4 draft, not baselined. Chapter 04.3.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (Chapter 04.3) |
