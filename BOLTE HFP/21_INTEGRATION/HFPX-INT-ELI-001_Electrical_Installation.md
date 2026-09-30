# Electrical Installation

**Document ID:** HFPX-INT-ELI-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X electrical installation view (Chapter 21.5): the installation-specification structure for the electrical system, including sequencing, distribution interfaces, and installation verification.

## 2. Scope

Covers electrical installation sequencing and specification structure for the production-aircraft concept, excluding avionics boxes (21.6), harnessing detail (21.10), and grounding and bonding detail (21.11). All routing details, support provisions, connector specifications, and verification methods TBD. Methodology and sequencing only.

## 3. Applicable Documents

- HFPX-ARC-IFR-001 System Interfaces (interface register and ICD rule); HFPX-INT-STR-001 Assembly Strategy (Chapter 21.1)
- ICD tier (documents TBD)
- Electrical subsystem inputs (Vol 15, details TBD)
- VVP thread (documents TBD)

## 4. Definitions & Acronyms

- Electrical installation: placement, routing support, and connection of the electrical distribution system (scope TBD).
- Distribution interface: power mating boundary governed by its interface definition (details TBD).
- Installation gate: completion checkpoint for an electrical installation stage (criteria TBD).

## 5. System Context

Electrical installation integrates power generation, distribution, and servicing interfaces with structure, propulsion, avionics, and ground-service interfaces, within the build sequence (21.1), prior to system integration (21.12) and integration testing (21.13).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-KEI-001 | The electrical installation specification shall define the installation sequence and stage gates (sequence and criteria TBD). | IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD); electrical inputs (TBD); VVP thread (TBD) | Inspection |
| REQ-HFPX-KEI-002 | The electrical installation specification shall capture each power distribution interface and its governing interface definition (details TBD). | IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD); electrical inputs (TBD); VVP thread (TBD) | Inspection |
| REQ-HFPX-KEI-003 | The electrical installation specification shall define routing, support, and connection specification hooks for electrical equipment (specifications TBD). | IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD); electrical inputs (TBD); VVP thread (TBD) | Inspection |
| REQ-HFPX-KEI-004 | The electrical installation specification shall define installation verification provisions, including connection and continuity checks (methods TBD). | IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD); electrical inputs (TBD); VVP thread (TBD) | Inspection |

## 7. Architecture

Installation framework: staged electrical installation (stages TBD), distribution-interface register (TBD), routing/support/connection hooks (TBD), and gate reviews with as-built recording (TBD). Harnessing detail routes to 21.10; grounding and bonding detail routes to 21.11.

## 8. Detailed Design

Not applicable at Tranche 6 draft level. Routing definitions, support definitions, and connector specifications are TBD in subsystem inputs and ICDs.

## 9. Interfaces

Each electrical installation interface points to its interface definition in the IFR/ICD tier (TBD). Detail hooks point to wiring and harnessing (21.10) and grounding and bonding (21.11). Sequencing aligns with the build strategy (21.1).

## 10. Operational Concept

Installation methodology and sequencing only: staged placement and connection under configuration control with gate reviews (flow TBD). No energisation, servicing, or handling instructions are stated.

## 11. Safety

No installation-safety claim is made. Electrical handling precautions and controlled-condition provisions are TBD. No hazardous instructions are stated.

## 12. Performance

Electrical capacities, tolerances, and environmental ratings are TBD per subsystem input and ICD. No allocation value is stated.

## 13. Verification & Validation

Verified by inspection (sequence completeness, interface coverage, specification hooks, as-built recording). Later validated by integration testing (Vol 22/23.2 hooks TBD). Methods TBD in detail.

## 14. Risks

- Undefined distribution interfaces forcing rework; mitigation: interface register stub now, trade-driven updates by change record.
- Routing conflicts with co-installed systems; mitigation: coordination through system integration (21.12).

## 15. Open Issues

Installation sequence TBD; distribution interfaces TBD; routing, support, and connection specifications TBD; installation verification methods TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on the IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD), electrical subsystem inputs (TBD), the assembly strategy (21.1), and the VVP thread (TBD).

## 18. Traceability

Parents: IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD); electrical installation inputs (TBD); VVP thread (TBD). Children: as-built records and integration V&V (TBD). RTM: REQ-HFPX-KEI-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 21.5) |
