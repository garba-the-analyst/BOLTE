# Prototype Propulsion

**Document ID:** HFPX-MVP-PPN-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined; Vol 33 separate from production  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the prototype propulsion installation and chain boundaries for controlled testing, and the gating that confines all prototype propulsion activity to controlled conditions. Owns Chapter 33.6.

## 2. Scope

Covers prototype propulsion installation definition; propulsion-chain boundary definition (ISS-003); the controlled-conditions rule for staged testing; and the documentation boundary for this volume. Test methodology and gating only — no build/ignition/operation instructions for high-energy propulsion outside controlled conditions are given in this document.

Vol 33 is SEPARATE from production baselines. No prototype propulsion choice constrains production design; reuse is governed by the 33.20 transition gate only.

## 3. Applicable Documents

- HFPX-MVP-OBJ-001 MVP Objectives (MVP-001..005, DDR-001 risk note)
- HFPX-MVP-REQ-001 MVP System Requirements (Chapter 33.2; REQ-HFPX-MRQ-001..006)
- HFPX-MVP-ARC-001 MVP Architecture (Chapter 33.3; MAR-002 propulsion installation)
- HFPX-MVP-CFG-001 Prototype Configuration (Chapter 33.4; propulsion modules under index control)
- Future: 33.5 experimental components, 33.11 safety system, 33.12 instrumentation, 33.13/33.14 test programmes, 33.19 exit criteria, 33.20 transition; Vol 13 safety; Vol 19 modelling; Vol 23 test programme

## 4. Definitions & Acronyms

- MPP: MVP Prototype-Propulsion Requirement — prototype propulsion obligation in this document (does not set production propulsion requirements)
- Prototype propulsion installation: non-certified arrangement of propulsion modules, mounts, and interfaces for controlled testing only (boundaries TBD)
- Propulsion chain: end-to-end energy-to-thrust path under test including control and safety interfaces (chain TBD; ISS-003 risk)
- Controlled conditions: defined test stages, ranges, authorisations, and abort rules under engineering, test, safety, and regulatory controls (criteria TBD)
- 33.20 transition gate: sole route for propulsion lessons to inform production; no auto-promotion

## 5. System Context

Prototype propulsion hosts unmanned hover, transition, and cruise methodology within staged gates:

```text
MRQ-001..003 + MAR-002 ── allocation ──► MPP-001..004 (this document, Ch 33.6)
        │                                          │
        ▼                                          ▼
  33.13 ground tests ──► 33.14 unmanned flights ──► 33.19 exit / 33.20 gate (data only)
```

> This volume is SEPARATE from the production-aircraft documentation. Production-design transition is governed by 33.20.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-MPP-001 | The MVP prototype propulsion installation shall be defined with installation boundaries, mounting interfaces, and test-article integration limits for controlled testing (boundaries and limits TBD). | MVP-001, MRQ-001, MAR-002, DDR-001 | Inspection |
| REQ-HFPX-MPP-002 | The MVP prototype propulsion chain shall be defined end-to-end with chain boundaries, control interfaces, and safety interfaces identified (chain TBD; ISS-003 propulsion-chain risk). | MVP-001, MRQ-001, MAR-002 | Inspection |
| REQ-HFPX-MPP-003 | Prototype propulsion testing shall progress only through controlled ground stages to unmanned flight stages under defined engineering, test, safety, and regulatory controls with entrance criteria and abort rules (stages, criteria, and authority TBD). | MVP-001, MVP-004, MRQ-006 | Demonstration |
| REQ-HFPX-MPP-004 | Prototype propulsion documentation in this volume shall be limited to test methodology and gating and shall contain no build, ignition, or operation instructions for high-energy propulsion outside controlled conditions. | MVP-004 | Inspection |

All thrust, energy, mass, thermal, endurance, and envelope values are TBD. No performance figure is set.

## 7. Architecture

Installation architecture (placeholder): propulsion modules hosted in the representative airframe per MAR-002 with defined chain interfaces to prototype avionics/compute (33.7/33.8), safety chain (33.11), and instrumentation hooks (33.12). Layouts, schematics, setpoints, and redundancy provisions TBD.

## 8. Detailed Design

Not applicable — no propulsion sizing, layout, schematic, material, or setpoint is baselined here. All design values TBD in later tranches, if at all, and remain prototype-only.

## 9. Interfaces

Propulsion interfaces: airframe mounts and integration limits (33.3/33.4), avionics/compute command paths (33.7/33.8), safety-chain inhibit/abort paths (33.11), instrumentation taps (33.12), range/test infrastructure (Vol 23). Production propulsion interface is data/decision handover via the 33.20 transition gate only.

## 10. Operational Concept

Test methodology and gating only. Each propulsion test stage is attempted only when its entrance criteria are met and within its abort rules (TBD in 33.13/33.14); unmanned stages precede any human-proximate activity per MRQ-006. No build/ignition/operation instructions for high-energy propulsion outside controlled conditions are given.

## 11. Safety

Propulsion safety is governed by the prototype safety system (33.11) + Vol 13 analyses + range safety (Vol 23). Recovery-system limits (ISS-008) constrain propulsion test envelopes from the first run. Hazardous-subsystem boundary: requirements, installation boundaries, chain definition, methodology, and gating only.

## 12. Performance

No propulsion performance targets are set. Demonstration success is meeting gated evidence thresholds (TBD in 33.19), not achieving numeric thrust, energy, or endurance values. All values TBD.

## 13. Verification & Validation

- MPP-001: Inspection (installation boundaries and integration limits defined — TBD)
- MPP-002: Inspection (chain defined end-to-end with control/safety interfaces — TBD, ISS-003)
- MPP-003: Demonstration (stage progression with entrance-criteria and abort-rule records under controls — TBD)
- MPP-004: Inspection (document contains methodology and gating only; no build/ignition/operation instructions)
- MVP propulsion verification does not constitute production propulsion verification (separate baseline).

## 14. Risks

- Undefined installation boundaries → uncontrolled integration changes between tests; mitigation: MPP-001 boundaries TBD before gated runs
- Undefined chain (ISS-003) → untested interactions across the energy-to-thrust path; mitigation: MPP-002 chain definition TBD before gated runs
- Pressure to test outside controlled conditions or skip stages; mitigation: MPP-003 gate rule — skipping is prohibited
- Prototype propulsion values mistaken for production requirements; mitigation: 33.20 transition gate, no auto-promotion per MVP-005

## 15. Open Issues

- Installation boundaries, mounting interfaces, and integration limits for MPP-001: TBD
- Propulsion-chain definition, control interfaces, and safety interfaces for MPP-002 (ISS-003): TBD
- Controlled stages, entrance criteria, abort rules, and authorising authority for MPP-003: TBD
- Methodology-only documentation standard enforcing MPP-004: TBD

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on 33.3 installation allocation, 33.4 configuration control, 33.5 component instances, 33.11 safety-chain definition, 33.12 instrumentation taps, 33.13/33.14 stage definitions, 33.19 exit criteria, Vol 13 safety analyses, Vol 23 range capability.

## 18. Traceability

Parents: MVP-001 (gated demonstration), MVP-004 (controlled safety progression), MRQ-001/MRQ-006 (unmanned demonstration and gating), MAR-002 (propulsion installation), DDR-001. Children: 33.13 ground-test instances, 33.14 unmanned-test instances, 33.19 exit evidence, 33.20 handover dispositions. RTM: REQ-HFPX-MPP-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined; Vol 33 separate from production baselines. Prototype propulsion definitions never auto-promote; production effect only via the 33.20 transition gate.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 33.6) |
