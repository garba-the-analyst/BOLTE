# Grounding & Bonding

**Document ID:** HFPX-INT-GDB-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X grounding and bonding view (Chapter 21.11): the installation-specification structure for grounding and bonding, including classes, measurement hooks, and installation verification.

## 2. Scope

Covers grounding and bonding installation sequencing and specification structure for the production-aircraft concept. Bonding classes are TBD; measurement provisions are TBD, with hooks TBD (Vol 15.12). All joint preparations, connection specifications, and verification methods TBD. Methodology and sequencing only.

## 3. Applicable Documents

- HFPX-ARC-IFR-001 System Interfaces (interface register and ICD rule); HFPX-INT-STR-001 Assembly Strategy (Chapter 21.1)
- ICD tier (documents TBD)
- Electrical inputs including Vol 15.12 (details TBD)
- VVP thread (documents TBD)

## 4. Definitions & Acronyms

- Grounding: defined reference provisions for the electrical system (details TBD, Vol 15.12 hooks).
- Bonding: defined continuity provisions between conductive elements (classes TBD, Vol 15.12 hooks).
- Measurement hook: defined verification interface to bonding and grounding test provisions (details TBD).

## 5. System Context

Grounding and bonding provisions underpin electrical (21.5), avionics (21.6), sensor (21.7), and wiring and harnessing (21.10) installations, within the build sequence (21.1), prior to system integration (21.12) and integration testing (21.13).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-KGB-001 | The grounding and bonding specification shall define the installation sequence and stage gates (sequence and criteria TBD). | IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD); grounding inputs including Vol 15.12 (TBD); VVP thread (TBD) | Inspection |
| REQ-HFPX-KGB-002 | The grounding and bonding specification shall define bonding-class hooks for each applicable joint and interface (classes TBD, Vol 15.12 hooks). | IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD); grounding inputs including Vol 15.12 (TBD); VVP thread (TBD) | Inspection |
| REQ-HFPX-KGB-003 | The grounding and bonding specification shall define joint-preparation and connection specification hooks for grounding and bonding (specifications TBD). | IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD); grounding inputs including Vol 15.12 (TBD); VVP thread (TBD) | Inspection |
| REQ-HFPX-KGB-004 | The grounding and bonding specification shall define measurement and installation verification hooks, including as-built recording (methods TBD, Vol 15.12 hooks). | IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD); grounding inputs including Vol 15.12 (TBD); VVP thread (TBD) | Inspection |

## 7. Architecture

Installation framework: staged grounding and bonding installation (stages TBD), bonding-class hooks (TBD, Vol 15.12), preparation and connection hooks (TBD), and measurement hooks with gate reviews and as-built recording (TBD).

## 8. Detailed Design

Not applicable at Tranche 6 draft level. Class definitions, preparation definitions, and measurement specifications are TBD in subsystem inputs and ICDs.

## 9. Interfaces

Each grounding and bonding provision points to its interface definition in the IFR/ICD tier (TBD), with measurement hooks to Vol 15.12 provisions (TBD). Sequencing aligns with the build strategy (21.1).

## 10. Operational Concept

Installation methodology and sequencing only: staged preparation, connection, and measurement under configuration control with gate reviews (flow TBD). No energisation, servicing, or handling instructions are stated.

## 11. Safety

No installation-safety claim is made. Handling precautions and controlled-condition provisions are TBD. No hazardous instructions are stated.

## 12. Performance

Grounding and bonding capabilities, tolerances, and environmental ratings are TBD per subsystem input and ICD. No allocation value is stated.

## 13. Verification & Validation

Verified by inspection (sequence completeness, bonding-class coverage, measurement hooks, as-built recording). Later validated by integration testing (Vol 22/23.2 hooks TBD). Methods TBD in detail.

## 14. Risks

- Undefined bonding classes forcing rework; mitigation: class-hook stub with Vol 15.12 hooks now, trade-driven updates by change record.
- Late-defined measurement provisions delaying verification; mitigation: measurement hooks stubbed now.

## 15. Open Issues

Installation sequence TBD; bonding classes TBD (Vol 15.12 hooks TBD); preparation and connection specifications TBD; measurement provisions TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on the IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD), grounding inputs including Vol 15.12 (TBD), the assembly strategy (21.1), and the VVP thread (TBD).

## 18. Traceability

Parents: IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD); grounding installation inputs including Vol 15.12 (TBD); VVP thread (TBD). Children: as-built records and integration V&V (TBD). RTM: REQ-HFPX-KGB-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 21.11) |
