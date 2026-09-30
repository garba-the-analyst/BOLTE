# Assembly Strategy

**Document ID:** HFPX-INT-STR-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X assembly strategy view (Chapter 21.1): the build-sequence framework, workstation ownership, configuration control during build, and assembly completion criteria.

## 2. Scope

Covers the strategy-level sequencing of airframe assembly and system installation for the production-aircraft concept. Detailed installation provisions are covered in Chapters 21.2–21.11, system integration order in 21.12, and integration test procedures in 21.13. Fuel handling and propulsion handling outside controlled conditions are outside the scope of these documents; methodology and sequencing only. All sequence details, workstation assignments, and control provisions TBD.

## 3. Applicable Documents

- HFPX-ARC-IFR-001 System Interfaces (interface register and ICD rule)
- ICD tier (documents TBD)
- Subsystem installation inputs (Vol 03–18, details TBD)
- VVP thread (documents TBD)
- Vol 28.6 non-conformance flow (hooks TBD)

## 4. Definitions & Acronyms

- Build sequence: ordered stages of assembly and installation (stages TBD).
- Workstation: allocated build location or team scope for a defined work package (allocation TBD).
- Configuration control during build: recording of as-designed versus as-built state throughout assembly (method TBD).
- Assembly gate: defined completion checkpoint between build stages (criteria TBD).

## 5. System Context

Assembly strategy governs the order in which the airframe is assembled and systems are installed, under configuration control, before system integration (21.12) and integration testing (21.13). Every installation step traces to its interface definition (IFR/ICD tier) and subsystem input.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-KAS-001|The assembly strategy shall define the build sequence from airframe assembly through system installation to integration handover (sequence TBD).|IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD); subsystem installation inputs (TBD); VVP thread (TBD)|Inspection|
|REQ-HFPX-KAS-002|The assembly strategy shall define workstation ownership for each build work package (ownership TBD).|IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD); subsystem installation inputs (TBD); VVP thread (TBD)|Inspection|
|REQ-HFPX-KAS-003|The assembly strategy shall define configuration control during build, including as-designed versus as-built recording (method TBD).|IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD); subsystem installation inputs (TBD); VVP thread (TBD)|Inspection|
|REQ-HFPX-KAS-004|The assembly strategy shall define assembly-gate completion criteria for each build stage (criteria TBD).|IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD); subsystem installation inputs (TBD); VVP thread (TBD)|Inspection|
|REQ-HFPX-KAS-005|The assembly strategy shall define installation records retained through build (records TBD).|IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD); subsystem installation inputs (TBD); VVP thread (TBD)|Inspection|

## 7. Architecture

Strategy framework: staged build sequence (stages TBD), workstation allocation against work packages (TBD), gate structure between stages (TBD), and configuration-control spine linking each step to its interface and subsystem input (method TBD). Detailed provisions live in Chapters 21.2–21.13.

## 8. Detailed Design

Not applicable at Tranche 6 draft level. Stage definitions, workstation assignments, and control records are TBD.

## 9. Interfaces

This document frames build interfaces to the IFR register and ICD tier (HFPX-ARC-IFR-001; ICDs TBD), subsystem installation inputs (TBD), and the VVP thread (TBD). Each build step points to its governing interface definition.

## 10. Operational Concept

Build-flow methodology only: staged assembly and installation under configuration control, with gate reviews before progression (flow TBD). No operation, handling, or servicing instructions are stated.

## 11. Safety

No installation-safety claim is made. Handling precautions and controlled-condition provisions are TBD and belong to the detailed installation documents (21.2–21.11). Fuel handling and propulsion handling outside controlled conditions are excluded from these documents.

## 12. Performance

Not applicable at strategy level. Build durations, capacities, and resource allocations are TBD.

## 13. Verification & Validation

Verified by review (sequence completeness, workstation coverage, configuration-control definition, gate criteria). Later validated through build execution and integration testing (Vol 22/23.2 hooks TBD). Methods TBD in detail.

## 14. Risks

- Undefined build sequence forcing out-of-order installation and rework; mitigation: stub sequence now, trade-driven updates by change record.
- Unowned work packages causing gaps or duplication; mitigation: workstation ownership register (TBD).

## 15. Open Issues

Build sequence TBD; workstation ownership TBD; configuration control during build TBD; gate criteria TBD; installation records TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on the IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD) for interface definitions, subsystem installation inputs (TBD) for step content, and the VVP thread (TBD) for verification routing.

## 18. Traceability

Parents: IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD); subsystem installation inputs (TBD); VVP thread (TBD). Children: Chapters 21.2–21.13 installation and integration documents. RTM: REQ-HFPX-KAS-001..005 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 21.1) |
