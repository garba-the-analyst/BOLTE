# Prototype Configuration

**Document ID:** HFPX-MVP-CFG-001  
**Revision:** B (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 3 draft, not baselined; Vol 33 separate from production  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define how the MVP demonstrator is configuration-controlled so that every test result traces to a known prototype state — while keeping prototype states rigorously separate from the production baseline. Owns Chapter 33.4.

## 2. Scope

Covers configuration-index ownership; MVP-vs-production parts control (no auto-promotion); configuration-change rules for the prototype; and as-built/as-tested record standards. Test methodology and gating only — no build/ignition/operation instructions for high-energy propulsion outside controlled conditions.

Vol 33 is SEPARATE from production baselines. Any movement of data, lessons, or hardware toward production is governed by the 33.20 transition gate only.

## 3. Applicable Documents

- HFPX-MVP-OBJ-001 MVP Objectives (MVP-005 no-auto-promotion rule)
- HFPX-MVP-REQ-001 MVP System Requirements (MRQ-001..006 evidence obligation)
- HFPX-MVP-ARC-001 MVP Architecture (MAR-001..005 segments under control)
- Future: 33.5 experimental components list, 33.11–33.14 safety/test volumes, 33.17 lessons learned, 33.19 exit criteria, 33.20 transition; Vol 13 safety; Vol 23 test programme

## 4. Definitions & Acronyms

- MCF: MVP Configuration Requirement — prototype configuration-control obligation in this document (does not set production CM rules)
- Configuration index: the controlled list of prototype config items and their revisions for each test article and test event (contents TBD)
- Config item: any tracked prototype element (see starter list, §7); revisions TBD
- As-built / as-tested: the recorded state of the article before and during a test, including deviations and non-conformances (standard TBD)
- No auto-promotion: per MVP-005, no prototype part, value, or revision enters production except via 33.20 transition
- 33.20 transition gate: sole route for prototype-to-production handover; requires requirements, verification, and safety review

## 5. System Context

Configuration control binds evidence to state for the demonstrator only:

```text
MAR segments (33.3) ── placed under control ──► MCF-001..004 (this document, Ch 33.4)
        │                                              │
        ▼                                              ▼
  test events (33.13/33.14) ◄── as-built/as-tested ──► 33.19 exit / 33.20 gate (data + disposition only)
```

> This volume is SEPARATE from the production-aircraft documentation. Production-design transition is governed by 33.20.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-MCF-001 | The MVP programme shall maintain a configuration index owning the identity and revision of each prototype config item for each test article and test event (items and index format TBD). | MVP-002, MRQ-004 | Inspection |
| REQ-HFPX-MCF-002 | The MVP programme shall control MVP parts separately from production parts such that no prototype component, value, or revision enters the production baseline except via the 33.20 transition gate (per MVP-005). | MVP-005 | Inspection |
| REQ-HFPX-MCF-003 | The MVP programme shall apply a defined configuration-change rule to the prototype such that changes, deviations, and non-conformances are recorded, reviewed, and re-gated before further testing (rule and authority TBD). | MVP-001, MRQ-006 | Inspection |
| REQ-HFPX-MCF-004 | The MVP programme shall record as-built and as-tested states for each gated test to a defined record standard including deviations (standard and retention TBD). | MVP-002, MRQ-004 | Inspection |

All part numbers, revisions, quantities, dates beyond 2026-09-29, and record-field values are TBD.

## 7. Architecture

Configuration-index structure (placeholder, format TBD): one index entry per test article per test event, referencing the starter config-item list below with revisions TBD. Index owns traceability from MRQ evidence (33.2) through MAR segments (33.3) to test records (33.13/33.14) and exit dispositions (33.19).

Starter config-item list (revisions TBD):

- Airframe (structure, interfaces, mass/inertia characterisation record) — revision TBD
- Propulsion modules (installation boundaries per 33.6, chain TBD) — revision TBD
- Avionics (units, harness, interface definitions per 33.7–33.9) — revision TBD
- Software build (flight, ground-station, and instrumentation software identifiers) — revision TBD
- Ground station (hardware and software configuration) — revision TBD
- Safety-system configuration (33.11 logic/threshold revision) — revision TBD
- Instrumentation fit (33.12 sensor/hook fit and calibration record) — revision TBD

## 8. Detailed Design

Not applicable — no index schema, part-numbering scheme, or record template is baselined here. All formats, fields, and numbering TBD.

## 9. Interfaces

Index interfaces: 33.5 experimental components list (source of tracked items), 33.11–33.14 (consumers of as-built state for safety/test gating), 33.17/33.19 (consumers of as-tested records for lessons/exit), production CM via 33.20 handover package only (no shared part numbering).

## 10. Operational Concept

Test methodology and gating only. No gated test proceeds without its configuration index entry and as-built record at the required standard (TBD); any change, deviation, or non-conformance invokes the MCF-003 change rule and may require re-gating (authority TBD). No build/ignition/operation instructions outside controlled conditions.

## 11. Safety

Configuration control supports safety gating (correct safety-system revision present, deviations reviewed) but grants no clearance. Safety-significant changes require review per 33.11/Vol 13 methodology (criteria TBD). Hazardous-subsystem boundary: control, records, and methodology only.

## 12. Performance

No performance figure is set. Index completeness, record latency, and retention values are TBD. Success is traceability coverage (every gated result maps to a recorded state), not numeric performance.

## 13. Verification & Validation

- MCF-001: Inspection (index exists, owns all starter items, revisions recorded — TBD standard)
- MCF-002: Inspection (MVP/production parts separation demonstrated; no shared promotion path except 33.20 record)
- MCF-003: Inspection (change/deviation/non-conformance records with review and re-gating evidence — rule TBD)
- MCF-004: Inspection (as-built/as-tested records present for each gated test — standard TBD)
- MVP configuration verification does not verify production CM (separate baseline).

## 14. Risks

- Unrecorded prototype changes between tests → evidence uninterpretable; mitigation: MCF-001/MCF-004 records required for gating
- Prototype part or value leaks into production documentation; mitigation: MCF-002 separation + 33.20 gate per MVP-005
- Change rule too heavy (slows testing) or too light (loses control); mitigation: rule TBD calibrated in 33.13 before gated flights
- As-tested records incomplete (missing deviations) → false exit claim in 33.19; mitigation: record standard TBD + gate inspection

## 15. Open Issues

- Configuration-index owner, format, and tooling: TBD
- MVP-vs-production numbering and segregation method for MCF-002: TBD
- Change-rule thresholds, review authority, and re-gating criteria for MCF-003: TBD
- As-built/as-tested record standard, fields, and retention for MCF-004: TBD

## 16. Assumptions


_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on 33.3 segment definitions (what is controlled), 33.5 experimental components list, 33.11–33.14 safety/test gating needs, 33.17/33.19 record consumers, 33.20 handover requirements.

## 18. Traceability

Parents: MVP-005 (no auto-promotion), MVP-001/MVP-002 (gating/evidence), MRQ-004/MRQ-006 (data capture and gating). Children: 33.5 item instances, 33.13/33.14 gate records, 33.19 exit evidence, 33.20 handover packages. RTM: REQ-HFPX-MCF-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 3 draft, CONCEPT, not baselined; Vol 33 separate from production baselines. Prototype revisions never auto-promote; production effect only via the 33.20 transition gate.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 3 draft (Chapter 33.4) |
| B | 2026-09-29 | Assumptions removed; all unknowns recorded as TBD (no assumptions raised or relied upon). |
