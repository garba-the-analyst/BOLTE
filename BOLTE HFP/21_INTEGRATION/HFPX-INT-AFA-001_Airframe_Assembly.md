# Airframe Assembly

**Document ID:** HFPX-INT-AFA-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X airframe assembly view (Chapter 21.2): the installation-specification structure for airframe assembly, including sequencing, join interfaces, and assembly verification.

## 2. Scope

Covers airframe assembly sequencing and specification structure for the production-aircraft concept. Subsystem installation provisions are covered in Chapters 21.3–21.11; strategy in 21.1; system integration in 21.12. All join details, fastening specifications, and tooling provisions TBD. Methodology and sequencing only.

## 3. Applicable Documents

- HFPX-ARC-IFR-001 System Interfaces (interface register and ICD rule); HFPX-INT-STR-001 Assembly Strategy (Chapter 21.1)
- ICD tier (documents TBD)
- Airframe subsystem inputs (Vol 03, details TBD)
- VVP thread (documents TBD)

## 4. Definitions & Acronyms

- Airframe assembly: joining of structural elements into the as-built airframe (scope TBD).
- Join interface: structural mating boundary governed by its interface definition (details TBD).
- Assembly gate: completion checkpoint for an airframe assembly stage (criteria TBD).

## 5. System Context

Airframe assembly provides the structural baseline into which propulsion, fuel, electrical, avionics, sensor, helmet, and recovery systems are installed (Chapters 21.3–21.9) with wiring, harnessing, grounding, and bonding (21.10–21.11), prior to system integration (21.12).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-KAA-001 | The airframe assembly specification shall define the airframe build sequence and stage gates (sequence and criteria TBD). | IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD); airframe inputs (TBD); VVP thread (TBD) | Inspection |
| REQ-HFPX-KAA-002 | The airframe assembly specification shall capture each structural join interface and its governing interface definition (details TBD). | IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD); airframe inputs (TBD); VVP thread (TBD) | Inspection |
| REQ-HFPX-KAA-003 | The airframe assembly specification shall define fastening and joining specification hooks for each joint (specifications TBD). | IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD); airframe inputs (TBD); VVP thread (TBD) | Inspection |
| REQ-HFPX-KAA-004 | The airframe assembly specification shall define assembly verification provisions, including as-built recording (methods TBD). | IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD); airframe inputs (TBD); VVP thread (TBD) | Inspection |

## 7. Architecture

Assembly framework: staged airframe build (stages TBD), join-interface register per stage (TBD), fastening-specification hooks per joint (TBD), and gate reviews with as-built recording (TBD).

## 8. Detailed Design

Not applicable at Tranche 6 draft level. Joint definitions, fastening specifications, and tooling provisions are TBD.

## 9. Interfaces

Each structural join points to its interface definition in the IFR/ICD tier (TBD). Assembly sequencing aligns with the build strategy (21.1) and provides the baseline for system installation (21.3–21.11).

## 10. Operational Concept

Assembly methodology and sequencing only: staged joining under configuration control with gate reviews (flow TBD). No fabrication or handling instructions are stated.

## 11. Safety

No assembly-safety claim is made. Structural handling precautions and controlled-condition provisions are TBD. No hazardous instructions are stated.

## 12. Performance

Structural capabilities, tolerances, and environmental ratings are TBD per subsystem input and ICD. No allocation value is stated.

## 13. Verification & Validation

Verified by inspection (sequence completeness, join-interface coverage, specification hooks, as-built recording). Later validated by integration testing (Vol 22/23.2 hooks TBD). Methods TBD in detail.

## 14. Risks

- Undefined join interfaces forcing rework; mitigation: join-interface register stub now, trade-driven updates by change record.
- Out-of-sequence assembly blocking later installation; mitigation: strategy alignment (21.1) at each gate.

## 15. Open Issues

Build sequence TBD; join interfaces TBD; fastening specifications TBD; assembly verification methods TBD; as-built recording TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on the IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD), airframe subsystem inputs (TBD), the assembly strategy (21.1), and the VVP thread (TBD).

## 18. Traceability

Parents: IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD); airframe installation inputs (TBD); VVP thread (TBD). Children: as-built records and integration V&V (TBD). RTM: REQ-HFPX-KAA-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 21.2) |
