# Thermal Model

**Document ID:** HFPX-SIM-THM-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the thermal model structure and discipline (Chapter 19.6): heat-source and sink inventory, limit-checking function, and feeds to Volume 14 and system-level simulation (19.2). This document establishes structure only; no capability or feasibility claim rests on any unverified model in this revision.

## 2. Scope

Covers thermal source/sink inventory discipline, limit-checking logic, and consumer feeds to Vol 14 and 19.2. Excludes thermal hardware design (Vol 14 owner), propulsion coupling internals beyond the hook interface (19.5), and verification execution (Vol 22/23).

## 3. Applicable Documents

- HFPX-VV-PLN-001 V&V Plan (notably REQ-HFPX-VVP-001, REQ-HFPX-VVP-004)
- HFPX-SYS-REQ-001 SyRS (notably SYS-001, SYS-008)
- HFPX-SIM-STR-001 Digital Engineering Strategy
- HFPX-SIM-SYS-001 System-Level Simulation (consumer)
- Volume 14 thermal design inputs (details TBD)
- ISS-006 and ISS-007 actions (details TBD)

## 4. Definitions & Acronyms

- Heat-source/sink inventory: enumerated set of thermal sources and sinks represented in the model; entries TBD.
- Limit-checking function: comparison of modelled temperatures against TBD limits with TBD disposition.
- TBD: to be defined; TBC: to be confirmed.

## 5. System Context

The thermal model represents heat sources and sinks with TBD parameters under the 19.1 hierarchy, checks modelled states against TBD limits, and feeds Vol 14 design assessment and the 19.2 system-level simulation. Outputs are TBD-valued structures in this revision and gain gate authority solely through verification via 19.15 hooks.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-MTM-001 | The thermal model shall define a heat-source and sink inventory, with entries, groupings, and values recorded as TBD. | SYS-008; ASX tier; ISS-006 | Inspection |
| REQ-HFPX-MTM-002 | The thermal model shall implement a limit-checking function comparing modelled states against TBD limits with TBD disposition logic. | SYS-001; VVP-001; ISS-007 | Analysis |
| REQ-HFPX-MTM-003 | The thermal model shall feed Volume 14 and system-level simulation (19.2) as its TBD-valued supplier, with interfaces and feed status TBD, such that no capability or feasibility claim rests on unverified thermal data. | SYS-008; VVP-004; ISS-006 | Analysis |

## 7. Architecture

Thermal model architecture (structure only): inventory layer (REQ-HFPX-MTM-001); limit-checking layer (REQ-HFPX-MTM-002); feed layer (REQ-HFPX-MTM-003) exporting to Vol 14 and 19.2. Couplings to propulsion (19.5) hooks TBD. Representation fidelities TBD.

## 8. Detailed Design

Inventory record TBD: source entries TBD, sink entries TBD, grouping rationale TBD, values TBD throughout. Limit-checking record TBD: limit set TBD, comparison logic TBD, exceedance disposition TBD, recording format TBD. Feed record TBD: Vol 14 interface TBD, 19.2 interface TBD, configuration reference TBD, status TBD.

## 9. Interfaces

- Thermal model ↔ Vol 14: design-assessment feed (interface TBD).
- Thermal model ↔ 19.2 system-level sim: thermal states and limit flags supplied (format TBD).
- Thermal model ↔ 19.5 propulsion: coupling hooks consumed (treatment TBD).
- Thermal model ↔ 19.1 strategy: registration, ownership, and gate authority (assignments TBD).
- Thermal model ↔ 19.15 Model Verification: verification methodology and status.

## 10. Operational Concept

Operates inventory-driven: declare sources/sinks TBD → populate values TBD → check against limits TBD → disposition exceedances TBD → export to Vol 14 and 19.2 TBD → submit for verification per 19.15 before any gate use. No thermal-margin finding is offered as evidence until verified. Cadence TBD.

## 11. Safety

No safety-related claim (including over-temperature margin or thermal-limit compliance) is made from thermal-model output until verification per 19.15 with independence per VVP-006 (degree TBD). Safety-significant limits and disposition paths are TBD (Vol 13/24 mapping TBD).

## 12. Performance

Thermal model performance indicators TBD (no thresholds baselined): inventory completeness TBD, limit-set definition status TBD, feed-interface definition status TBD, verification closure TBD. Measurement method and reporting cadence TBD.

## 13. Verification & Validation

This document is verified by Inspection against template, header, and requirement discipline. REQ-HFPX-MTM-001..003 are verified by their stated methods applied to the inventory, limit-checking, and feed records. Verification methodology for the model is owned by 19.15; execution evidence is owned by Vol 22/23. Validation is programme-authority approval at a gated review (review TBD).

## 14. Risks

- Incomplete inventory cited as bounding thermal case; mitigation: REQ-HFPX-MTM-001 explicit inventory with TBD entries blocking closure until populated.
- Limit exceedances handled informally; mitigation: REQ-HFPX-MTM-002 explicit disposition logic (logic TBD).
- Unverified thermal states consumed by Vol 14 or 19.2 as margins; mitigation: REQ-HFPX-MTM-003 no-claim rule with 19.15 hooks.

## 15. Open Issues

Inventory entries and values TBD. Limit set, comparison logic, and disposition TBD. Feed interfaces and verification status TBD via 19.15.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on Vol 14 thermal inputs (TBD), propulsion coupling hooks (19.5, TBD), 19.2 consumer interface (TBD), 19.1 authority rule, 19.15 verification methodology, ISS-006/ISS-007 scope, and Vol 22/23 execution.

## 18. Traceability

Parents: VVP-001, VVP-004; SYS-001, SYS-008; ASX tier (details TBD); ISS-006, ISS-007 actions. Children: inventory records, limit-checking records, feed records, verification cases (IDs TBD; rows TBD). RTM: REQ-HFPX-MTM-001..003 → CONCEPT. No capability or feasibility claim in this document rests on an unverified model; authority for any such future claim routes via 19.15.

## 19. Configuration

BL-0.0. Tranche 5 draft, CONCEPT, not baselined. Future changes via change records; any change re-validates affected traceability before gate claims.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 draft (19.6 thermal structure; requirements REQ-HFPX-MTM-001..003) |
