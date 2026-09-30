# Structural Loads

**Document ID:** HFPX-STR-LOD-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the structural-loads discipline for HFP-X (Chapter 03.13): load-case inventory, load-source hierarchy, loads-to-analysis feed, and loads-update discipline. This revision fixes structure only; all load cases, sources, and values are TBD and no load factor is baselined.

## 2. Scope

Covers flight, ground, pilot, propulsion, and thermal load-case inventory, the estimate-to-CFD-to-tunnel-to-flight source hierarchy, the feed from loads to structural analyses, and the update-on-evidence rule. Excludes aerodynamic table ownership (Vol 06/19), strength analysis execution (03.14), and test execution (03.20, Vol 22/23).

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (SYS tier allocation TBD)
- HFPX-SYS-ARC-001 SAD (system architecture views and SYS-01 allocation)
- Structural architecture and design-philosophy tier — SAR/SDP tier (IDs TBD)
- Vol 06 Aerodynamics (aero data-source hierarchy; IDs TBD)
- Vol 19 Modelling & Simulation (loads model hooks; IDs TBD)
- HFPX-VV-PLN-001 V&V Plan (VVP thread; method and gate discipline)
- Vol 07 Flight Control (pilot and control-induced loads; IDs TBD)
- Vol 14 Thermal (thermal-load inventory inputs; IDs TBD)

## 4. Definitions & Acronyms

- Load-case inventory: enumerated set of flight, ground, pilot, propulsion, and thermal load cases; entries TBD.
- Load-source hierarchy: ordered sources estimate, CFD, tunnel, flight; uncertainty recorded TBD per source.
- Loads-to-analysis feed: controlled transfer of loads to strength/fatigue/damage-tolerance consumers; interface TBD.
- TBD: to be defined; TBC: to be confirmed.

## 5. System Context

Structural loads sit between environment and aero/propulsion/pilot inputs and the structural analyses (03.14–03.16) under SYS-01. Source fidelity ascends from estimate through CFD and tunnel to flight, with uncertainty recorded TBD at each level. Loads outputs are consumed only as TBD-valued structures in this revision and gain gate authority solely through verification per VVP hooks.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-SLD-001 | The programme shall define the structural load-case inventory covering flight, ground, pilot, propulsion, and thermal cases, with each case definition recorded as TBD. | SYS-001; SAR tier (IDs TBD) | Inspection |
| REQ-HFPX-SLD-002 | The programme shall apply a load-source hierarchy of estimate, CFD, tunnel, and flight, with source designation and uncertainty recorded as TBD per load case. | VVP-001; Vol 06 hooks (IDs TBD) | Inspection |
| REQ-HFPX-SLD-003 | The programme shall define the loads-to-analysis feed to strength, fatigue, and damage-tolerance consumers, with interface, configuration reference, and feed status recorded as TBD. | SDP tier (IDs TBD); Vol 19 hooks (IDs TBD) | Analysis |
| REQ-HFPX-SLD-004 | The programme shall apply a loads-update rule requiring load cases and uncertainties to be revised when higher-fidelity evidence becomes available, with revision records TBD. | VVP-004; SDP tier (IDs TBD) | Inspection |
| REQ-HFPX-SLD-005 | Structural loads used for any sizing or margin claim shall rest on verified loads evidence per the VVP thread, with verification status TBD and no load factor baselined in this revision. | VVP-001; VVP-004 | Analysis |

## 7. Architecture

Loads architecture (structure only): inventory layer (REQ-HFPX-SLD-001) enumerating flight/ground/pilot/propulsion/thermal cases TBD; source-hierarchy layer (REQ-HFPX-SLD-002) annotating each case TBD; feed layer (REQ-HFPX-SLD-003) exporting TBD-valued loads to 03.14–03.16; update layer (REQ-HFPX-SLD-004) driving revisions TBD; authority layer (REQ-HFPX-SLD-005) gating claims on verification TBD. All values TBD; no load factor stated.

## 8. Detailed Design

Inventory record TBD per family (flight TBD, ground TBD, pilot TBD, propulsion TBD, thermal TBD): case definitions TBD, conditions TBD, values TBD throughout. Source-hierarchy record TBD per case: source designation TBD (estimate/CFD/tunnel/flight), uncertainty TBD, pedigree reference TBD. Feed record TBD: interface format TBD, consumer list TBD, configuration reference TBD, status TBD. Update record TBD: evidence-acceptance criteria TBD, revision trigger TBD, supersession handling TBD. Authority record TBD: verification references TBD, gate status TBD.

## 9. Interfaces

- Loads ↔ source activities (estimate/CFD/tunnel/flight): evidence ingested per hierarchy (pedigree TBD).
- Loads ↔ Vol 06 / Vol 19: aero tables and loads-model hooks (IDs TBD).
- Loads ↔ Vol 07 / Vol 14: pilot/control-induced and thermal load inputs (IDs TBD).
- Loads ↔ 03.14–03.16: TBD-valued feed to strength/fatigue/damage-tolerance analyses.
- Loads ↔ 03.20 / VVP thread: loads verification methodology and status.

## 10. Operational Concept

Operates evidence-driven: declare inventory TBD → populate from lowest available source TBD → annotate uncertainty TBD → export to analyses TBD → revise on higher-fidelity evidence TBD → submit for verification before any gate use. No loads set is offered as sizing evidence until verified. Cadence TBD.

## 11. Safety

No safety-related claim (including limit or ultimate behaviour derived from loads) is made in this revision. Safety-significant load cases and uncertainty treatment for safety analyses are TBD (Vol 13/24 mapping TBD).

## 12. Performance

Loads-discipline performance indicators TBD (no thresholds baselined): inventory completeness TBD, source-hierarchy population TBD, feed definition status TBD, update-record currency TBD, verification closure TBD. Measurement method and reporting cadence TBD.

## 13. Verification & Validation

This document is verified by Inspection against template, header, and requirement discipline. REQ-HFPX-SLD-001..005 are verified by their stated methods applied to the inventory, hierarchy, feed, update, and authority records. Test methodology is owned by HFPX-STR-TST-001 (03.20); this document defines no test procedure. Validation is programme-authority approval at a gated review (review TBD).

## 14. Risks

- Placeholder loads mistaken for sized data; mitigation: REQ-HFPX-SLD-001 TBD-value rule with source annotation per REQ-HFPX-SLD-002.
- Stale low-fidelity loads retained after better evidence arrives; mitigation: REQ-HFPX-SLD-004 update rule with revision records TBD.
- Unverified loads cited for margins; mitigation: REQ-HFPX-SLD-005 authority rule with no load factor baselined.

## 15. Open Issues

Load-case inventory TBD across flight, ground, pilot, propulsion, and thermal families. Per-source uncertainty TBD. Feed interface and status TBD. Update triggers and revision records TBD. Verification status TBD per VVP and Vol 19 hooks.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SAR/SDP tier allocation (IDs TBD), source evidence from estimate/CFD/tunnel/flight activities (TBD), Vol 06 aero-table interfaces (TBD), Vol 07 and Vol 14 input definitions (TBD), Vol 19 loads-model methodology (TBD), VVP method and gate discipline, and 03.20 test-methodology ownership.

## 18. Traceability

Parents: SYS tier (SYS-001 allocation TBD); SAR/SDP tier (IDs TBD); Vol 06 hooks (IDs TBD); Vol 19 hooks (IDs TBD); VVP thread (VVP-001, VVP-004). Children: inventory records, source-hierarchy records, feed records, update records, verification cases (IDs TBD; rows TBD). RTM: REQ-HFPX-SLD-001..005 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records; any change re-validates affected traceability before gate claims.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (03.13 structural loads; requirements REQ-HFPX-SLD-001..005) |
