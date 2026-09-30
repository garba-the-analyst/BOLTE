# Power Distribution

**Document ID:** HFPX-ELE-DST-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the power distribution structure (Chapter 15.5): buses, feeders, segregation, and load-connection provisions. Structure only; no topology selection or sizing is made.

## 2. Scope

Covers distribution network structure from source boundaries to load feeds. Excludes bus ratings, wire sizing, connector selection, schematics, and load values (all TBD).

## 3. Applicable Documents

- HFPX-ELE-ARC-001 Electrical Architecture (parent structure)
- HFPX-ARC-PWR-001 Power Architecture (SAD PWR view parent)
- HFPX-SYS-REQ-001 SyRS (SYS tier parent)
- Vol 08 Chapter 08.7 / Vol 10 Chapter 10.16 (load hooks, TBD)
- Vol 13 Chapter 13.16 (safety hook, TBD)

## 4. Definitions & Acronyms

- Bus: distribution node structure aggregating sources and loads (rating TBD).
- Feeder: structured connection from bus to load or sub-bus (sizing TBD).
- Segregation: structural separation of designated load paths (topology TBD).

## 5. System Context

Distribution interfaces with all source classes, conversion, protection, grounding, and avionics / helmet / sensor / actuator loads. It spans normal, degraded, and emergency states.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-EPD-001 | The distribution structure shall define bus and feeder structure from sources to loads (topology TBD). | HFPX-ELE-ARC-001; SAD PWR view; SYS tier | Inspection |
| REQ-HFPX-EPD-002 | The distribution structure shall define segregation structure for designated load paths (details TBD). | HFPX-ELE-ARC-001; Vol 13.16 hook | Analysis |
| REQ-HFPX-EPD-003 | The distribution structure shall define load-connection provisions for avionics, helmet, and sensor feeds (details TBD). | HFPX-ELE-ARC-001; Vol 08.7 / 10.16 hooks | Inspection |
| REQ-HFPX-EPD-004 | The distribution structure shall define distribution control and status interface structure (details TBD). | HFPX-ELE-ARC-001; SYS tier | Inspection |

## 7. Architecture

Source boundaries (TBD) → buses (TBD) → feeders (TBD) → load interfaces (TBD), with segregation provisions (TBD) and control / status paths (TBD). No ratings, sizing, or schematics stated.

## 8. Detailed Design

Not applicable at this revision. Single-line diagrams, wire sizing, and connector selection deferred to later tranches and ICDs. No electrical values stated.

## 9. Interfaces

E-DIST (bus boundaries), E-LOAD (feeds to avionics / helmet / sensor / actuator domains), control / status to power management. Definitions TBD in ICDs.

## 10. Operational Concept

Distribution supports source selection, load prioritisation, and shedding concepts (TBD) across normal, degraded, and emergency states.

## 11. Safety

Segregation, fault containment, and loss-of-bus cases feed Vol 13.16 analyses. No safety values stated.

## 12. Performance

Distribution losses, transients, and power-quality allocations are TBD. No values stated.

## 13. Verification & Validation

Verified by inspection (network coverage) and analysis (segregation concepts). Validated later by load analysis and integration test. Pass/fail criteria TBD.

## 14. Risks

- Topology uncertainty with load growth; mitigation: margin policy and load inventory completion (TBD).
- Cross-coupling between segregated paths; mitigation: segregation analysis and test gating (TBD).

## 15. Open Issues

Bus topology, feeder routing, segregation implementation, shedding priorities, and sizing TBD. Load inventory incomplete.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on HFPX-ELE-ARC-001, SAD PWR view, source structures (Chapters 15.2–15.4, 15.8), load inputs (Vol 08.7 / 10.16), and Vol 13.16 safety inputs.

## 18. Traceability

Parents: SYS tier; SAD PWR view (HFPX-ARC-PWR-001); HFPX-ELE-ARC-001; Vol 08.7 / 10.16 / 13.16 hooks (TBD). Children: ICDs, V&V cases. RTM: REQ-HFPX-EPD-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Chapter 15.5.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 15.5) |
