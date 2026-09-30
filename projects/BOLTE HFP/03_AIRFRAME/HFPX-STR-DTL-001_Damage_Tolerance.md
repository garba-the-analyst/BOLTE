# Damage Tolerance

**Document ID:** HFPX-STR-DTL-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the damage-tolerance discipline for HFP-X (Chapter 03.16): damage-scenario inventory, residual-strength practice, detectability discipline, and verification thread. This revision fixes structure only; all scenarios, strengths, and intervals are TBD and no tolerance claim is made.

## 2. Scope

Covers damage scenarios, residual-strength analysis practice, detectability rules linking damage to inspection, and verification per VVP hooks. Excludes loads definition (03.13), static-strength and fatigue execution (03.14–03.15), and test execution (03.20, Vol 22/23).

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (SYS tier allocation TBD)
- HFPX-SYS-ARC-001 SAD (system architecture views and SYS-01 allocation)
- Structural architecture and design-philosophy tier — SAR/SDP tier (IDs TBD)
- HFPX-STR-LOD-001 Structural Loads (loads feed; REQ-HFPX-SLD-001..005)
- Vol 19 Modelling & Simulation (damage-tolerance model hooks; IDs TBD)
- HFPX-VV-PLN-001 V&V Plan (VVP thread; method and gate discipline)
- HFPX-STR-TST-001 Structural Testing (03.20 test-methodology owner)

## 4. Definitions & Acronyms

- Damage scenarios: enumerated discrete damage states including manufacturing and service-induced damage; entries TBD.
- Residual strength: retained capability with prescribed damage present; methods and values TBD.
- Detectability: likelihood and means of finding damage before loss of required capability; criteria TBD.
- TBD: to be defined; TBC: to be confirmed.

## 5. System Context

Damage tolerance consumes verified loads (03.13), material data (03.10–03.12), and fatigue findings (03.15) through Vol 19 models under SYS-01, producing residual-strength and detectability records consumed by inspection provisions and VVP gates. All records are TBD-valued in this revision and gain authority only through verified evidence.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-SDT-001 | The programme shall define damage scenarios as an enumerated list, with each scenario definition recorded as TBD. | SYS-001; SAR tier (IDs TBD) | Inspection |
| REQ-HFPX-SDT-002 | The programme shall define residual-strength analysis practice for prescribed damage, with methods and results recorded as TBD. | SDP tier (IDs TBD); Vol 19 hooks (IDs TBD) | Analysis |
| REQ-HFPX-SDT-003 | The programme shall define the detectability rule linking each damage scenario to its detection means and timing, with criteria and provisions recorded as TBD. | SAR tier (IDs TBD); SDP tier (IDs TBD) | Inspection |
| REQ-HFPX-SDT-004 | Damage-tolerance findings shall be verified by defined analysis and test threads, with methods, cases, and status recorded as TBD per the VVP thread. | VVP-001; VVP-004 | Analysis + Test |

## 7. Architecture

Damage-tolerance architecture (structure only): scenario layer (REQ-HFPX-SDT-001) enumerating damage states TBD; residual-strength layer (REQ-HFPX-SDT-002) analysing retained capability TBD; detectability layer (REQ-HFPX-SDT-003) linking damage to detection TBD; verification layer (REQ-HFPX-SDT-004) linking models and tests per VVP TBD. Scenarios, strengths, and criteria TBD throughout.

## 8. Detailed Design

Scenario record TBD: manufacturing-damage entries TBD, service-damage entries TBD, threat definitions TBD, excluded scenarios TBD. Residual-strength record TBD: analytical methods TBD, damage sizes TBD, strength results TBD throughout. Detectability record TBD: detection means TBD, detection timing TBD, linkage to inspection provisions TBD. Verification record TBD: analysis cases TBD, test cases TBD, correlation method TBD.

## 9. Interfaces

- Damage tolerance ↔ 03.13 loads: damage-case loads inputs (definitions TBD).
- Damage tolerance ↔ 03.10–03.12 materials: damage-tolerance material data (values TBD).
- Damage tolerance ↔ 03.15 fatigue: crack-growth and life inputs (IDs TBD).
- Damage tolerance ↔ Vol 19: residual-strength model hooks (IDs TBD).
- Damage tolerance ↔ 03.20 / VVP thread: verification case and evidence hooks (IDs TBD).

## 10. Operational Concept

Operates scenario-first: enumerate damage TBD → analyse residual strength TBD → assign detectability TBD → submit for verification per VVP gates TBD. No damage-tolerance finding is offered as airworthiness evidence until verified. Cadence TBD.

## 11. Safety

No safety-related claim (including residual strength or detectability adequacy) is made in this revision. Safety-significant damage scenarios and their treatment in safety analyses are TBD (Vol 13/24 mapping TBD).

## 12. Performance

Damage-tolerance performance indicators TBD (no thresholds baselined): scenario-inventory completeness TBD, residual-strength maturity TBD, detectability-rule definition status TBD, verification closure TBD. Measurement method and reporting cadence TBD.

## 13. Verification & Validation

This document is verified by Inspection against template, header, and requirement discipline. REQ-HFPX-SDT-001..004 are verified by their stated methods applied to the scenario, residual-strength, detectability, and verification records. Test methodology is owned by HFPX-STR-TST-001 (03.20); this document defines no test procedure. Validation is programme-authority approval at a gated review (review TBD).

## 14. Risks

- Damage scenarios assumed complete without basis; mitigation: REQ-HFPX-SDT-001 enumerated-list rule with entries TBD.
- Residual strength cited without prescribed damage; mitigation: REQ-HFPX-SDT-002 practice rule (methods TBD).
- Undetectable damage credited with tolerance; mitigation: REQ-HFPX-SDT-003 detectability rule (criteria TBD).

## 15. Open Issues

Damage scenarios TBD. Residual-strength methods and results TBD. Detectability criteria and provisions TBD. Verification methods, cases, and status TBD per VVP and Vol 19 hooks.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SAR/SDP tier allocation (IDs TBD), loads inputs from 03.13 (TBD), material data from 03.10–03.12 (TBD), fatigue inputs from 03.15 (TBD), Vol 19 damage-tolerance methodology (TBD), VVP method and gate discipline, and 03.20 test-methodology ownership.

## 18. Traceability

Parents: SYS tier (SYS-001 allocation TBD); SAR/SDP tier (IDs TBD); Vol 06 hooks (IDs TBD); Vol 19 hooks (IDs TBD); VVP thread (VVP-001, VVP-004). Children: scenario records, residual-strength records, detectability records, verification cases (IDs TBD; rows TBD). RTM: REQ-HFPX-SDT-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records; any change re-validates affected traceability before gate claims.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (03.16 damage tolerance; requirements REQ-HFPX-SDT-001..004) |
