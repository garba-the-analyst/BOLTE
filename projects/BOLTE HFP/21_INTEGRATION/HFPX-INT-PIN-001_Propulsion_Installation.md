# Propulsion Installation

**Document ID:** HFPX-INT-PIN-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X propulsion installation view (Chapter 21.3): the installation-specification structure for propulsion, including sequencing, interface capture, and installation verification.

## 2. Scope

Covers propulsion installation sequencing and specification structure for the production-aircraft concept. Mechanical, electrical, and data interfaces are captured as hooks TBD (Vol 04.16). Sequencing only; no operation, running, servicing, or handling instructions are stated. Propulsion handling outside controlled conditions is excluded. All mounting details, connection details, and verification methods TBD.

## 3. Applicable Documents

- HFPX-ARC-IFR-001 System Interfaces (interface register and ICD rule); HFPX-INT-STR-001 Assembly Strategy (Chapter 21.1)
- ICD tier (documents TBD)
- Propulsion subsystem inputs (Vol 04, including 04.16, details TBD)
- VVP thread (documents TBD)

## 4. Definitions & Acronyms

- Propulsion installation: placement, mounting, and connection of the propulsion system into the airframe (scope TBD).
- Installation interface: mechanical, electrical, or data mating boundary governed by its interface definition (details TBD).
- Installation gate: completion checkpoint for a propulsion installation stage (criteria TBD).

## 5. System Context

Propulsion installation integrates the propulsion system with structure, fuel, electrical, data, and ground-service interfaces, within the build sequence (21.1), prior to system integration (21.12) and integration testing (21.13).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-KPI-001 | The propulsion installation specification shall define the installation sequence and stage gates (sequence and criteria TBD). | IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD); propulsion inputs including Vol 04.16 (TBD); VVP thread (TBD) | Inspection |
| REQ-HFPX-KPI-002 | The propulsion installation specification shall capture each mechanical, electrical, and data installation interface and its governing interface definition (details TBD, Vol 04.16 hooks). | IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD); propulsion inputs including Vol 04.16 (TBD); VVP thread (TBD) | Inspection |
| REQ-HFPX-KPI-003 | The propulsion installation specification shall define mounting and connection specification hooks for each propulsion interface (specifications TBD). | IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD); propulsion inputs including Vol 04.16 (TBD); VVP thread (TBD) | Inspection |
| REQ-HFPX-KPI-004 | The propulsion installation specification shall define installation verification provisions, including as-built recording (methods TBD). | IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD); propulsion inputs including Vol 04.16 (TBD); VVP thread (TBD) | Inspection |

## 7. Architecture

Installation framework: staged propulsion installation (stages TBD), interface register across mechanical/electrical/data flows (TBD, Vol 04.16 hooks), mounting and connection specification hooks (TBD), and gate reviews with as-built recording (TBD).

## 8. Detailed Design

Not applicable at Tranche 6 draft level. Mounting definitions, connection definitions, and routing details are TBD in subsystem inputs and ICDs.

## 9. Interfaces

Each propulsion installation interface points to its interface definition in the IFR/ICD tier (TBD) with Vol 04.16 hooks (TBD). Sequencing aligns with the build strategy (21.1).

## 10. Operational Concept

Installation methodology and sequencing only: staged mounting and connection under configuration control with gate reviews (flow TBD). No operation, running, servicing, or handling instructions are stated.

## 11. Safety

No installation-safety claim is made. Handling precautions and controlled-condition provisions are TBD. Propulsion handling outside controlled conditions is excluded from these documents. No hazardous instructions are stated.

## 12. Performance

Propulsion capabilities, tolerances, and environmental ratings are TBD per subsystem input and ICD. No allocation value is stated.

## 13. Verification & Validation

Verified by inspection (sequence completeness, interface coverage, specification hooks, as-built recording). Later validated by integration testing (Vol 22/23.2 hooks TBD). Methods TBD in detail.

## 14. Risks

- Undefined propulsion interfaces forcing rework; mitigation: interface register stub with Vol 04.16 hooks now, trade-driven updates by change record.
- Out-of-sequence installation blocking mating systems; mitigation: strategy alignment (21.1) at each gate.

## 15. Open Issues

Installation sequence TBD; mechanical/electrical/data interfaces TBD (Vol 04.16 hooks TBD); mounting and connection specifications TBD; installation verification methods TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on the IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD), propulsion subsystem inputs including Vol 04.16 (TBD), the assembly strategy (21.1), and the VVP thread (TBD).

## 18. Traceability

Parents: IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD); propulsion installation inputs including Vol 04.16 (TBD); VVP thread (TBD). Children: as-built records and integration V&V (TBD). RTM: REQ-HFPX-KPI-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 21.3) |
