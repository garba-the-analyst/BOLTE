# Wiring & Harnessing

**Document ID:** HFPX-INT-WRH-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X wiring and harnessing view (Chapter 21.10): the installation-specification structure for wiring and harnesses, including routing, separation, support, protection, and installation verification.

## 2. Scope

Covers wiring and harness installation sequencing and specification structure for the production-aircraft concept. Routing and separation provisions are TBD, with hooks TBD (Vol 29.5). All harness definitions, connector specifications, support provisions, and verification methods TBD. Methodology and sequencing only.

## 3. Applicable Documents

- HFPX-ARC-IFR-001 System Interfaces (interface register and ICD rule); HFPX-INT-STR-001 Assembly Strategy (Chapter 21.1)
- ICD tier (documents TBD)
- Electrical and avionics inputs (Vol 15, Vol 08, details TBD); Vol 29.5 hooks (TBD)
- VVP thread (documents TBD)

## 4. Definitions & Acronyms

- Harness: routed group of wires with connectors, supports, and protection (definition TBD).
- Routing and separation: pathing and segregation provisions for wiring and harnesses (details TBD, Vol 29.5 hooks).
- Support and protection: clamping, chafing protection, and environmental safeguarding provisions (details TBD).

## 5. System Context

Wiring and harnessing realises the power and data interfaces registered in the IFR/ICD tier across electrical (21.5), avionics (21.6), sensor (21.7), and helmet (21.8) installations, within the build sequence (21.1), prior to system integration (21.12) and integration testing (21.13).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-KWH-001 | The wiring and harnessing specification shall define the installation sequence and stage gates (sequence and criteria TBD). | IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD); wiring inputs including Vol 29.5 (TBD); VVP thread (TBD) | Inspection |
| REQ-HFPX-KWH-002 | The wiring and harnessing specification shall define routing and separation specification hooks for wiring and harnesses (details TBD, Vol 29.5 hooks). | IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD); wiring inputs including Vol 29.5 (TBD); VVP thread (TBD) | Inspection |
| REQ-HFPX-KWH-003 | The wiring and harnessing specification shall define support, protection, and connection specification hooks for wiring and harnesses (specifications TBD). | IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD); wiring inputs including Vol 29.5 (TBD); VVP thread (TBD) | Inspection |
| REQ-HFPX-KWH-004 | The wiring and harnessing specification shall define installation verification provisions, including as-built recording (methods TBD). | IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD); wiring inputs including Vol 29.5 (TBD); VVP thread (TBD) | Inspection |

## 7. Architecture

Installation framework: staged wiring and harness installation (stages TBD), routing and separation hooks (TBD, Vol 29.5), support/protection/connection hooks (TBD), and gate reviews with as-built recording (TBD).

## 8. Detailed Design

Not applicable at Tranche 6 draft level. Harness definitions, routing definitions, and separation specifications are TBD in subsystem inputs and ICDs.

## 9. Interfaces

Each wiring and harness interface points to its interface definition in the IFR/ICD tier (TBD), with routing and separation hooks to Vol 29.5 provisions (TBD). Sequencing aligns with the build strategy (21.1).

## 10. Operational Concept

Installation methodology and sequencing only: staged routing, support, and connection under configuration control with gate reviews (flow TBD). No energisation, servicing, or handling instructions are stated.

## 11. Safety

No installation-safety claim is made. Handling precautions and controlled-condition provisions are TBD. No hazardous instructions are stated.

## 12. Performance

Wiring capabilities, tolerances, and environmental ratings are TBD per subsystem input and ICD. No allocation value is stated.

## 13. Verification & Validation

Verified by inspection (sequence completeness, routing and separation coverage, support and connection hooks, as-built recording). Later validated by integration testing (Vol 22/23.2 hooks TBD). Methods TBD in detail.

## 14. Risks

- Undefined routing and separation provisions forcing rework; mitigation: routing-hook stub with Vol 29.5 hooks now, trade-driven updates by change record.
- Routing conflicts across co-installed systems; mitigation: coordination through system integration (21.12).

## 15. Open Issues

Installation sequence TBD; routing and separation TBD (Vol 29.5 hooks TBD); support, protection, and connection specifications TBD; installation verification methods TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on the IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD), wiring inputs including Vol 29.5 (TBD), the assembly strategy (21.1), and the VVP thread (TBD).

## 18. Traceability

Parents: IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD); wiring installation inputs including Vol 29.5 (TBD); VVP thread (TBD). Children: as-built records and integration V&V (TBD). RTM: REQ-HFPX-KWH-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 21.10) |
