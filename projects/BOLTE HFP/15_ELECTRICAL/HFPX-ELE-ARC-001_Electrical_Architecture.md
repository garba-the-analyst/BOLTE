# Electrical Architecture

**Document ID:** HFPX-ELE-ARC-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X electrical architecture structure (Chapter 15.1): source classes, distribution, conversion, protection, grounding, load-feed allocation, and EMI/EMC principles. Structure only; no ratings, topologies, or selections are made.

## 2. Scope

Covers the end-to-end electrical structure spanning Chapters 15.2–15.14. Excludes source ratings, distribution topology, wire sizing, schematics, and limit values (all TBD). Detail is deferred to Chapters 15.2–15.14.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (SYS tier parent)
- HFPX-SYS-ARC-001 SAD (SYS tier parent)
- HFPX-ARC-PWR-001 Power Architecture (SAD PWR view parent)
- Vol 08 Chapter 08.7 (avionics load hook, TBD)
- Vol 10 Chapter 10.16 (helmet load hook, TBD)
- Vol 13 Chapter 13.16 (safety hook, TBD)

## 4. Definitions & Acronyms

- Electrical architecture: structure of sources, distribution, conversion, protection, grounding, and load feeds (details TBD).
- Source class: primary, auxiliary, battery, or emergency role (ratings TBD).
- Segregation: structural separation of flight-critical and mission load paths (topology TBD).

## 5. System Context

Electrical architecture energises all flight, ground, and maintenance states. It interfaces with propulsion energy, avionics, helmet, and sensor loads, and with the airframe grounding and thermal environment. It bounds normal, degraded, and emergency power states.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-EAR-001 | The electrical architecture shall define the source, distribution, conversion, protection, and grounding structure (details TBD). | SAD PWR view (HFPX-ARC-PWR-001); SYS tier | Inspection |
| REQ-HFPX-EAR-002 | The electrical architecture shall define bus segregation structure for flight-critical and mission load paths (topology TBD). | SAD PWR view (HFPX-ARC-PWR-001); SYS tier | Analysis |
| REQ-HFPX-EAR-003 | The electrical architecture shall define power-state structure across normal, degraded, and emergency states (definitions TBD). | SAD PWR view (HFPX-ARC-PWR-001); SYS tier | Analysis |
| REQ-HFPX-EAR-004 | The electrical architecture shall allocate load-feed structures to avionics, helmet, and sensor domains (details TBD). | SAD PWR view (HFPX-ARC-PWR-001); Vol 08.7 / 10.16 hooks | Inspection |
| REQ-HFPX-EAR-005 | The electrical architecture shall define grounding and EMI/EMC structural principles (limits TBD). | SAD PWR view (HFPX-ARC-PWR-001); SYS tier | Analysis |

## 7. Architecture

Source layer (primary / auxiliary / battery / emergency classes, TBD) → distribution and conversion layer (buses, converters, protection, segregation, TBD) → load layer (avionics, helmet, sensor, actuator, ground-interface feeds, TBD). Grounding and EMI/EMC zoning principles apply across layers. No ratings, topologies, or schematics stated.

## 8. Detailed Design

Not applicable at this revision. Single-line diagrams, sizing, and selections are deferred to Chapters 15.2–15.14 and ICDs. No electrical values stated.

## 9. Interfaces

Structural boundaries: E-SRC (source outputs), E-DIST (distribution buses), E-CNV (conversion boundaries), E-PROT (protection coordination boundaries), E-LOAD (avionics / helmet / sensor feeds), E-GND (grounding / bonding), E-EMC (zoning / shielding). Definitions TBD.

## 10. Operational Concept

Power-state structure tracks CONOPS modes plus ground servicing, BIT, and emergency states. Source prioritisation and load-shedding concepts (TBD) preserve defined functions in degraded states.

## 11. Safety

Segregated safety-path feed structure and emergency-source availability structure support Vol 13.16 safety analyses. Hazards and loss-of-power cases are TBD inputs to Vol 13. No safety values stated.

## 12. Performance

Capacity, load, transient, and power-quality budgets are TBD. Budget holder: Vol 15 with load inputs from Vol 08 / 10. No values stated.

## 13. Verification & Validation

Verified by inspection (structural coverage) and analysis (segregation and state concepts). Validated later by load analysis, integration test, and EMI/EMC test. Pass/fail criteria TBD.

## 14. Risks

- Load growth exceeding TBD source structure; mitigation: margin policy owned by Vol 15 (TBD).
- Coupling across segregated paths; mitigation: zoning and bonding principles with test gating (TBD).

## 15. Open Issues

Source ratings, distribution topology, conversion topology, protection selectivity, load-shed priorities, grounding scheme, and EMC limits all TBD. Load inventory incomplete.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on load inputs (Vol 08.7 / 10.16), safety analyses (Vol 13.16), SAD PWR view, and detailed design in Chapters 15.2–15.14.

## 18. Traceability

Parents: SYS tier (SyRS / SAD); SAD PWR view (HFPX-ARC-PWR-001); Vol 08.7 / 10.16 / 13.16 hooks (TBD). Children: Chapters 15.2–15.14, ICDs, V&V cases. RTM: REQ-HFPX-EAR-001..005 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Chapter 15.1.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 15.1) |
