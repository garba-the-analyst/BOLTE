# MVP Architecture

**Document ID:** HFPX-MVP-ARC-001  
**Revision:** B (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 3 draft, not baselined; Vol 33 separate from production  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the prototype-level architecture that hosts the MVP system requirements (33.2): which prototype segments exist, how they allocate MRQ evidence obligations, and where representativeness explicitly does not hold. Owns Chapter 33.3.

## 2. Scope

Covers representative airframe; prototype propulsion installation; prototype avionics/compute/sensors/ground-station chain; prototype safety-chain independence; and instrumentation architecture with 33.12 hooks. Test methodology and gating only — no build/ignition/operation instructions for high-energy propulsion outside controlled conditions.

Vol 33 is SEPARATE from production baselines. No architectural choice here constrains production design; reuse is governed by the 33.20 transition gate only.

## 3. Applicable Documents

- HFPX-MVP-OBJ-001 MVP Objectives (MVP-001..005, DDR-001 risk note)
- HFPX-MVP-REQ-001 MVP System Requirements (Chapter 33.2; REQ-HFPX-MRQ-001..006)
- DDR-001 (unmanned-first, representativeness risk); ISS-003 (propulsion chain risk)
- Future: 33.4 prototype configuration, 33.6 propulsion prototype, 33.7–33.10 avionics/compute/sensors/ground-station, 33.11 safety system, 33.12 instrumentation, 33.19 exit criteria, 33.20 transition; Vol 13 safety; Vol 19 modelling

## 4. Definitions & Acronyms

- MAR: MVP Architecture Requirement — prototype architecture obligation in this document (does not set production architecture)
- Representative airframe: geometry/mass/inertia sufficiently like the concept to validate first-order models; method and tolerances TBC (DDR-001 risk note)
- Prototype propulsion installation: non-certified arrangement for controlled testing only; chain details TBD (33.6, ISS-003)
- Safety-chain independence: prototype safety functions separable from nominal control/data paths to defined methodology (criteria TBD, 33.11)
- 33.12 hooks: structural, power, data, and software provisions reserved for test instrumentation (list TBD)
- 33.20 transition gate: sole route for architectural lessons to inform production; no auto-promotion

## 5. System Context

The MVP architecture is a scaffolding for evidence, not a production precursor:

```text
MRQ-001..006 (33.2) ── allocation ──► MAR-001..005 (this document, Ch 33.3)
        │                                    │
        │                              ┌────┼────┐
        ▼                              ▼    ▼    ▼
  33.19 exit / 33.20 gate       33.4 config  33.6–33.12 segments  Vol 19 models
```

> This volume is SEPARATE from the production-aircraft documentation. Production-design transition is governed by 33.20.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-MAR-001 | The MVP architecture shall provide a representative airframe whose mass, inertia, and interface properties are characterised by a defined method (method and tolerances TBC) with documented representativeness limits. | MRQ-001, MRQ-002, MRQ-003, DDR-001 | Inspection |
| REQ-HFPX-MAR-002 | The MVP architecture shall provide a prototype propulsion installation that hosts controlled ground and unmanned test methodology with defined chain boundaries (chain TBD in 33.6, ISS-003). | MRQ-001, MRQ-002, MRQ-003 | Inspection |
| REQ-HFPX-MAR-003 | The MVP architecture shall provide prototype avionics, compute, sensors, and ground-station segments that host command, telemetry, and data-capture methodology (allocation and performance TBD in 33.7–33.10). | MRQ-004, MRQ-001 | Inspection |
| REQ-HFPX-MAR-004 | The MVP architecture shall provide a prototype safety chain with defined independence from nominal control and data paths (independence criteria and logic TBD in 33.11). | MRQ-005, DDR-001 | Analysis |
| REQ-HFPX-MAR-005 | The MVP architecture shall provide instrumentation provisions with hooks to the 33.12 dataset including power, mounting, data-bus, and software interfaces (list TBD). | MRQ-004 | Inspection |

Representativeness limits: the airframe is representative only to the characterised method (TBC); prototype propulsion, avionics, compute, and software are explicitly non-representative of production and carry no certification or production-design claim. All values TBD.

## 7. Architecture

Segments (all prototype, all TBD in detail): (a) representative airframe structure + interfaces; (b) prototype propulsion installation (33.6); (c) prototype avionics/compute/sensors (33.7–33.9); (d) prototype ground station (33.10); (e) prototype safety chain, independent per MAR-004 (33.11); (f) instrumentation layer with 33.12 hooks per MAR-005. Allocation: MAR-001→MRQ-001..003 evidence; MAR-002→MRQ-001..003 testability; MAR-003→MRQ-001/004 command and capture; MAR-004→MRQ-005 protection; MAR-005→MRQ-004 validation data.

## 8. Detailed Design

Not applicable — no segment sizing, selection, or setpoint is defined here. Mass, inertia, power, data-rate, and threshold values are TBD in 33.4–33.12.

## 9. Interfaces

Internal: airframe ↔ propulsion installation (mechanical/interface methodology TBD); avionics/compute ↔ sensors ↔ ground station (protocol methodology TBD); safety chain ↔ all segments (trigger/override methodology TBD); all segments ↔ instrumentation hooks (33.12). External: range/test infrastructure (Vol 23), models (Vol 19), production baseline via 33.20 data/decision handover only.

## 10. Operational Concept

Test methodology and gating only. Architecture enables staged progression: ground → SIL/HIL → subsystem → integrated propulsion → unmanned hover → transition → cruise (gates TBD in 33.13/33.14). Safety-chain independence (MAR-004) and instrumentation hooks (MAR-005) shall be in place before gated flight. No build/ignition/operation instructions outside controlled conditions.

## 11. Safety

Architecture supports safety analysis but grants no clearance. Safety-chain independence is a design-methodology obligation verified by analysis against 33.11 criteria (TBD); hazard analyses remain Vol 13; range safety remains Vol 23; ISS-008 recovery limits constrain envelopes. Hazardous-subsystem boundary: architecture and methodology only.

## 12. Performance

No architectural performance figure is set. Throughput, latency, accuracy, and margin values for avionics, compute, sensors, links, and propulsion installation are TBD in 33.6–33.10. Success is allocation coverage of MRQ evidence, not numeric performance.

## 13. Verification & Validation

- MAR-001: Inspection (representativeness method record + limits statement, TBC)
- MAR-002: Inspection (installation boundary and test-methodology coverage vs 33.6, chain TBD)
- MAR-003: Inspection (segment allocation matrix vs 33.7–33.10, TBD)
- MAR-004: Analysis (independence argument vs 33.11 criteria, TBD)
- MAR-005: Inspection (hook list vs 33.12 dataset, TBD)
- MVP architecture verification does not verify production architecture (separate SAD baseline).

## 14. Risks

- DDR-001 risk realised: non-representative airframe yields false model validation → mitigation: MAR-001 method TBC + documented limits before first flight
- ISS-003 propulsion-chain risk carried into prototype installation → mitigation: chain TBD bounded by 33.6 methodology and 33.13 gating
- Safety chain insufficiently independent (common-cause with nominal path) → mitigation: MAR-004 independence criteria + Vol 13 review
- Instrumentation hooks omitted from early builds → MRQ-004 evidence lost; mitigation: MAR-005 hook list frozen before gated testing
- Architecture mistaken for production precedent; mitigation: 33.20 transition gate, no auto-promotion per MVP-005

## 15. Open Issues

- Representativeness method, tolerances, and measurement standard for MAR-001: TBC
- Propulsion installation chain boundaries and test interfaces for MAR-002: TBD (33.6, ISS-003)
- Avionics/compute/sensor/ground-station allocation for MAR-003: TBD (33.7–33.10)
- Safety-chain independence criteria for MAR-004: TBD (33.11)
- Instrumentation hook list for MAR-005: TBD (33.12)

## 16. Assumptions


_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on MRQ allocation (33.2), 33.4 configuration control, 33.6–33.12 segment definitions, 33.13/33.14 test programmes, 33.19 exit criteria, Vol 13 safety, Vol 19 modelling needs, Vol 23 range interfaces.

## 18. Traceability

Parents: MRQ-001..006 allocation from 33.2; DDR-001 risk note (representativeness); ISS-003 (propulsion chain). Children: 33.4 configuration items, 33.6–33.12 segment design, 33.13/33.14 test implementation, 33.19 exit evidence, 33.20 transition dispositions. RTM: REQ-HFPX-MAR-001..005 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 3 draft, CONCEPT, not baselined; Vol 33 separate from production baselines. No architectural element promotes to production except via the 33.20 transition gate (per MVP-005).

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 3 draft (Chapter 33.3) |
| B | 2026-09-29 | Assumptions removed; all unknowns recorded as TBD (no assumptions raised or relied upon). |
