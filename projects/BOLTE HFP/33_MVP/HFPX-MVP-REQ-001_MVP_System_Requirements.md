# MVP System Requirements

**Document ID:** HFPX-MVP-REQ-001  
**Revision:** B (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 3 draft, not baselined; Vol 33 separate from production  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the system-level requirements for the Minimum Viable Prototype (MVP) demonstrator: what it shall prove, under what gating, and what evidence it shall produce — without setting production design values. Owns Chapter 33.2.

## 2. Scope

Covers unmanned hover, transition, and cruise demonstration; telemetry/instrumentation data capture; prototype safety-system functions; and the gate for any human-proximate testing. Excludes production requirements (Vol 00–32 baselines) and excludes build/ignition/operation instructions for high-energy propulsion outside controlled conditions — test methodology and gating only.

Vol 33 is SEPARATE from production baselines. Transition of any requirement, value, or component to production is governed by the 33.20 transition gate only.

## 3. Applicable Documents

- HFPX-MVP-OBJ-001 MVP Objectives (Chapter 33.1; REQ-HFPX-MVP-001..005)
- DDR-001 (unmanned-first); HFPX-SYS-MIS-001 mission sources (MIS-001..006)
- HFPX-SYS-REQ-001 SyRS (stub); HFPX-SYS-ARC-001 SAD (stub)
- Future: 33.3 MVP architecture, 33.4 prototype configuration, 33.11 prototype safety system, 33.12 instrumentation, 33.13/33.14 test programmes, 33.19 exit criteria, 33.20 transition; Vol 13 safety; Vol 22 V&V; Vol 23 test programme; Vol 25 regulatory

## 4. Definitions & Acronyms

- MVP: Minimum Viable Prototype — unmanned-first demonstrator that retires load-bearing risks (ISS-006/007/008)
- MRQ: MVP Requirement — system-level prototype requirement in this document (does not set production values)
- Unmanned hover / transition / cruise: prototype flight phases demonstrated without crew or passengers aboard; performance figures TBD
- Human-proximate testing: tethered-human or controlled-human flight; permitted only after unmanned evidence and FRR-level authorisation (criteria TBD)
- 33.20 transition gate: sole route by which prototype data or components may inform the production baseline; no auto-promotion

## 5. System Context

The MVP requirements constrain only the Vol 33 demonstrator and its evidence chain:

```text
MVP-001..004 + MIS-001..006
        │ allocation
        ▼
REQ-HFPX-MRQ-001..006 (this document, Ch 33.2)
        │ allocation
        ▼
33.3 architecture (MAR) → 33.4 configuration → 33.11/33.12/33.13/33.14 → 33.19 exit → 33.20 transition gate → production baseline
```

> This volume is SEPARATE from the production-aircraft documentation. Production-design transition is governed by 33.20.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-MRQ-001 | The MVP system shall demonstrate unmanned hover capability under controlled test conditions with defined entrance criteria, abort rules, and evidence capture (envelope and thresholds TBD). | MVP-001, MIS-001 | Test |
| REQ-HFPX-MRQ-002 | The MVP system shall demonstrate unmanned transition capability between hover and horizontal flight under controlled test conditions with defined entrance criteria, abort rules, and evidence capture (envelope and thresholds TBD). | MVP-001, MIS-002 | Test |
| REQ-HFPX-MRQ-003 | The MVP system shall demonstrate unmanned cruise (horizontal flight) capability under controlled test conditions with defined entrance criteria, abort rules, and evidence capture (envelope and thresholds TBD). | MVP-001, MIS-003 | Test |
| REQ-HFPX-MRQ-004 | The MVP system shall capture telemetry and instrumentation data for each test sufficient to validate first-order models (dataset, sampling, and retention TBD in 33.12). | MVP-002, MIS-006 | Inspection |
| REQ-HFPX-MRQ-005 | The MVP system shall provide prototype safety-system functions including abort, stabilisation, and recovery-trigger functions (logic, thresholds, and independence TBD in 33.11). | MVP-004, MIS-004 | Demonstration |
| REQ-HFPX-MRQ-006 | The MVP system shall permit gated human-proximate testing only after unmanned hover, transition, and cruise evidence has met defined exit criteria and received authorisation (criteria and authority TBD in 33.19/33.14). | MVP-001, MVP-004, MIS-005 | Inspection |

No speed, range, endurance, mass, thrust, or energy figure is set in this document — all values TBD.

## 7. Architecture

Requirements allocate to the MVP architecture (33.3): MRQ-001..003 to representative airframe + prototype propulsion + prototype avionics/compute; MRQ-004 to instrumentation architecture (33.12 hooks); MRQ-005 to prototype safety chain (33.11); MRQ-006 to test programme gating (33.13/33.14) and exit criteria (33.19).

## 8. Detailed Design

Not applicable — no prototype detailed design is defined here. Sizing, layouts, and setpoints are TBD in 33.4–33.10 volumes.

## 9. Interfaces

MRQ interfaces: 33.3 architecture allocation, 33.10 ground station (command/telemetry methodology), 33.12 instrumentation (dataset methodology), Vol 23 range/test infrastructure, Vol 25 regulatory authorisation. Production baseline interface is data/decision handover via the 33.20 transition gate only.

## 10. Operational Concept

Test methodology and gating only. Each of MRQ-001..003 is attempted only when its stage entrance criteria are met and within abort rules (TBD in 33.13/33.14). MRQ-006 prohibits skipping unmanned stages. No build/ignition/operation instructions for high-energy propulsion outside controlled conditions are given.

## 11. Safety

MRQ-005 and MRQ-006 are safety-gating requirements, not safety clearances. Prototype safety-system design is 33.11; hazard analysis is Vol 13; range safety is Vol 23. Recovery-system limits (ISS-008) constrain MVP envelopes from the first flight. Hazardous-subsystem boundary: requirements, gating, and methodology only.

## 12. Performance

No MVP performance targets are set. Demonstration success is defined as meeting gated evidence thresholds (TBD in 33.19), not achieving numeric speed/range/endurance values. All values TBD.

## 13. Verification & Validation

- MRQ-001..003: Test (controlled unmanned flights with evidence review)
- MRQ-004: Inspection (dataset completeness against 33.12 list, TBD)
- MRQ-005: Demonstration (safety-function response in ground/SIL/HIL and unmanned tests, thresholds TBD)
- MRQ-006: Inspection (gate record showing unmanned evidence + authorisation before any human-proximate test)
- MVP verification does not constitute production verification (Vol 22 separate).

## 14. Risks

- Demonstrator envelopes defined before representativeness criteria agreed (DDR-001) → false confidence; mitigation: 33.3 representativeness limits + 33.19 exit criteria TBD
- Instrumentation dataset defined late (33.12) → MRQ-004 unverifiable; mitigation: dataset TBD resolved before first gated flight
- Schedule pressure to invoke MRQ-006 early; mitigation: MRQ-006 is a programme gate — skipping is prohibited
- Prototype values mistaken for production requirements; mitigation: 33.20 transition gate, no auto-promotion per MVP-005

## 15. Open Issues

- Flight envelopes, thresholds, and tolerances for MRQ-001..003: TBD
- Telemetry/instrumentation dataset, sampling, and retention for MRQ-004: TBD (33.12)
- Abort/stabilisation/recovery-trigger logic and thresholds for MRQ-005: TBD (33.11)
- Unmanned-evidence exit criteria and authorisation authority for MRQ-006: TBD (33.19/33.14)
- ISS-006/007/008 retirement mapping to MRQ evidence: TBD

## 16. Assumptions


_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on 33.3 architecture allocation, 33.4 configuration control, 33.11 safety-system definition, 33.12 instrumentation definition, 33.13/33.14 test programmes, 33.19 exit criteria, Vol 13 safety analyses, Vol 23 range capability, Vol 25 authorisation.

## 18. Traceability

Parents: REQ-HFPX-MVP-001..004 (OBJ-001), MIS-001..006 (mission sources). Children: MAR allocation in 33.3, MCF configuration in 33.4, 33.11/33.12/33.13/33.14 implementation, 33.19 exit criteria, 33.20 transition dispositions. RTM: REQ-HFPX-MRQ-001..006 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 3 draft, CONCEPT, not baselined; Vol 33 separate from production baselines. No MRQ value or component promotes to production except via the 33.20 transition gate (per MVP-005).

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 3 draft (Chapter 33.2) |
| B | 2026-09-29 | Assumptions removed; all unknowns recorded as TBD (no assumptions raised or relied upon). |
