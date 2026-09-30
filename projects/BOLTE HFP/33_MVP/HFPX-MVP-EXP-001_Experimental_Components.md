# Experimental Components

**Document ID:** HFPX-MVP-EXP-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined; Vol 33 separate from production  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define how experimental (prototype-only) components are inventoried, marked, and controlled so that prototype shortcuts never leak into the production baseline. Owns Chapter 33.5.

## 2. Scope

Covers the experimental-component inventory; prototype-vs-production marking; no-auto-promotion control; and traceability of each experimental component to its configuration-index entry and as-tested record. Excludes production parts control (production CM baselines) and excludes build/ignition/operation instructions for high-energy propulsion outside controlled conditions — test methodology and gating only.

Vol 33 is SEPARATE from production baselines. Any movement of data, lessons, or hardware toward production is governed by the 33.20 transition gate only.

## 3. Applicable Documents

- HFPX-MVP-OBJ-001 MVP Objectives (MVP-001..005, DDR-001 risk note)
- HFPX-MVP-REQ-001 MVP System Requirements (Chapter 33.2; REQ-HFPX-MRQ-001..006)
- HFPX-MVP-ARC-001 MVP Architecture (Chapter 33.3; REQ-HFPX-MAR-001..005)
- HFPX-MVP-CFG-001 Prototype Configuration (Chapter 33.4; configuration index, as-built/as-tested records)
- Future: 33.6–33.12 prototype segment volumes, 33.13/33.14 test programmes, 33.19 exit criteria, 33.20 transition; Vol 13 safety; Vol 23 test programme

## 4. Definitions & Acronyms

- MEC: MVP Experimental-Component Requirement — prototype component-control obligation in this document (does not set production CM rules)
- Experimental component: any prototype-only part, assembly, software build, or value tracked for controlled testing (inventory TBD)
- Prototype marking: defined identification distinguishing experimental components from production parts (method TBD)
- No auto-promotion: per MVP-005, no prototype component, value, or revision enters production except via 33.20 transition
- 33.20 transition gate: sole route for prototype-to-production handover; requires requirements, verification, and safety review

## 5. System Context

The experimental-components list is the source of tracked prototype items placed under configuration control:

```text
MEC-001..004 (this document, Ch 33.5) ── items placed under control ──► MCF index (33.4)
        │                                                                       │
        ▼                                                                       ▼
  33.6–33.12 segment instances ◄── prototype marking ──► 33.13/33.14 gate records → 33.19 exit / 33.20 gate
```

> This volume is SEPARATE from the production-aircraft documentation. Production-design transition is governed by 33.20.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-MEC-001 | The MVP programme shall maintain an experimental-component inventory identifying each prototype component and its revision for each test article and test event (inventory contents and format TBD). | MVP-002, MRQ-004, MAR-001, DDR-001 | Inspection |
| REQ-HFPX-MEC-002 | The MVP programme shall mark each experimental component as prototype with defined prototype-vs-production identification that prevents confusion with production parts (marking method TBD). | MVP-005, MRQ-004 | Inspection |
| REQ-HFPX-MEC-003 | The MVP programme shall prevent auto-promotion such that no experimental component, value, or revision enters the production baseline except via the 33.20 transition gate with requirements, verification, and safety review (per MVP-005). | MVP-005 | Inspection |
| REQ-HFPX-MEC-004 | The MVP programme shall trace each experimental component to its configuration-index entry and as-tested record for each gated test in which it participates (trace method and record standard TBD in 33.4). | MVP-002, MRQ-004, MAR-005 | Inspection |

All component identities, revisions, quantities, and record-field values are TBD.

## 7. Architecture

Inventory structure (placeholder, format TBD): one inventory entry per experimental component per test article per test event, carrying prototype marking and a pointer to its configuration-index entry (33.4). Inventory feeds the 33.6–33.12 segment instances and the 33.13/33.14 gate records. Schema, fields, and tooling TBD.

## 8. Detailed Design

Not applicable — no inventory schema, marking artwork, part-numbering scheme, or record template is baselined here. All formats, fields, and numbering TBD.

## 9. Interfaces

Inventory interfaces: 33.4 configuration index (controlled state), 33.6–33.12 segments (item instances), 33.11–33.14 (safety/test gating consumers), 33.17/33.19 (lessons/exit consumers), production CM via 33.20 handover package only (no shared promotion path).

## 10. Operational Concept

Test methodology and gating only. No gated test proceeds with unlisted or unmarked experimental components; any inventory change invokes the 33.4 change rule and may require re-gating (authority TBD). No build/ignition/operation instructions for high-energy propulsion outside controlled conditions are given.

## 11. Safety

Component control supports safety gating (correct prototype revision present, deviations reviewed) but grants no clearance. Safety-significant component changes require review per 33.11/Vol 13 methodology (criteria TBD). Hazardous-subsystem boundary: inventory, marking, and methodology only.

## 12. Performance

No performance figure is set. Inventory completeness, marking durability, and record latency values are TBD. Success is control coverage (every experimental component listed, marked, and traced), not numeric performance.

## 13. Verification & Validation

- MEC-001: Inspection (inventory exists, owns each experimental component and revision — standard TBD)
- MEC-002: Inspection (prototype marking present and unambiguous against production parts — method TBD)
- MEC-003: Inspection (MVP/production separation demonstrated; no shared promotion path except 33.20 record)
- MEC-004: Inspection (each experimental component traces to index entry and as-tested record for each gated test — standard TBD)
- MVP component verification does not verify production CM (separate baseline).

## 14. Risks

- Unlisted prototype component flies in a gated test → evidence uninterpretable; mitigation: MEC-001 inventory required for gating
- Prototype part mistaken for production part; mitigation: MEC-002 marking + MEC-003 separation per MVP-005
- Informal promotion of prototype values into production documents; mitigation: 33.20 gate as sole route
- Trace gaps between inventory, index, and as-tested records → false exit claim in 33.19; mitigation: MEC-004 trace inspection

## 15. Open Issues

- Experimental-component inventory contents, format, owner, and tooling: TBD
- Prototype-vs-production marking method for MEC-002: TBD
- Promotion-review inputs and authority at the 33.20 gate for MEC-003: TBD
- Trace method and record standard linking inventory to 33.4 index for MEC-004: TBD

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on 33.3 segment definitions (what is inventoried), 33.4 configuration-index and record standards, 33.6–33.12 segment instances, 33.11–33.14 safety/test gating needs, 33.19 exit evidence needs, 33.20 handover requirements.

## 18. Traceability

Parents: MVP-002 (evidence), MVP-005 (no auto-promotion), MRQ-004 (data capture), MAR-001/MAR-005 (segments and instrumentation provisions), DDR-001. Children: 33.6–33.12 item instances, 33.4 index entries, 33.13/33.14 gate records, 33.19 exit evidence, 33.20 handover packages. RTM: REQ-HFPX-MEC-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined; Vol 33 separate from production baselines. Prototype components never auto-promote; production effect only via the 33.20 transition gate.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 33.5) |
