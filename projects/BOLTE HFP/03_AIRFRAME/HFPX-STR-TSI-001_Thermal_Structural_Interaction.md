# Thermal-Structural Interaction

**Document ID:** HFPX-STR-TSI-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the thermal-structural interaction discipline for HFP-X (Chapter 03.19): thermal-load inventory, material-knockdown practice, verification thread, and update discipline. This revision fixes structure only; all thermal loads, knockdowns, and results are TBD and no thermal-structural claim is made.

## 2. Scope

Covers thermal-load inventory per Vol 14 hooks, material-knockdown practice for elevated-temperature effects, verification per VVP hooks, and the update-on-evidence rule. Excludes thermal-system ownership (Vol 14), loads inventory ownership outside thermal cases (03.13), and test execution (03.20, Vol 22/23).

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (SYS tier allocation TBD)
- HFPX-SYS-ARC-001 SAD (system architecture views and SYS-01 allocation)
- Structural architecture and design-philosophy tier — SAR/SDP tier (IDs TBD)
- Vol 14 Thermal (thermal-load and temperature-field inputs; IDs TBD)
- HFPX-STR-LOD-001 Structural Loads (thermal load-case feed; REQ-HFPX-SLD-001..005)
- Vol 19 Modelling & Simulation (thermal-structural model hooks; IDs TBD)
- HFPX-VV-PLN-001 V&V Plan (VVP thread; method and gate discipline)
- HFPX-STR-TST-001 Structural Testing (03.20 test-methodology owner)

## 4. Definitions & Acronyms

- Thermal-load inventory: enumerated temperature fields and thermally induced loads; entries TBD.
- Material knockdown: reduction of material capability with temperature or thermal exposure; practice and values TBD.
- Update rule: revision of thermal-structural inputs and knockdowns on higher-fidelity evidence; triggers TBD.
- TBD: to be defined; TBC: to be confirmed.

## 5. System Context

Thermal-structural interaction couples Vol 14 temperature fields to SYS-01 airframe response through Vol 19 models, feeding strength, fatigue, and damage-tolerance consumers (03.14–03.16). All temperature fields, knockdowns, and interaction results are TBD-valued in this revision and gain authority only through verified evidence per VVP gates.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-STS-001 | The programme shall define the thermal-load inventory per Vol 14 hooks, with temperature fields and thermally induced loads recorded as TBD. | SYS-001; Vol 14 (IDs TBD) | Analysis |
| REQ-HFPX-STS-002 | The programme shall define material-knockdown practice for thermal effects, with methods, conditioning, and values recorded as TBD. | SDP tier (IDs TBD); VVP-001 | Analysis |
| REQ-HFPX-STS-003 | Thermal-structural interaction shall be verified by defined analysis and test threads, with methods, cases, and status recorded as TBD per the VVP thread and Vol 19 model hooks. | VVP-001; VVP-004; Vol 19 hooks (IDs TBD) | Analysis + Test |
| REQ-HFPX-STS-004 | The programme shall apply a thermal-structural update rule requiring inventory and knockdowns to be revised when higher-fidelity thermal evidence becomes available, with revision records TBD. | VVP-004; SDP tier (IDs TBD) | Inspection |

## 7. Architecture

Thermal-structural architecture (structure only): inventory layer (REQ-HFPX-STS-001) enumerating temperature fields and thermal loads TBD; knockdown layer (REQ-HFPX-STS-002) governing material-capability treatment TBD; verification layer (REQ-HFPX-STS-003) linking models and tests per VVP TBD; update layer (REQ-HFPX-STS-004) driving revisions TBD. Fields, knockdowns, and results TBD throughout.

## 8. Detailed Design

Inventory record TBD: temperature-field definitions TBD, thermally induced load entries TBD, Vol 14 source references TBD, values TBD throughout. Knockdown record TBD: applicable material systems TBD, conditioning definitions TBD, statistical treatment TBD, knockdown values TBD. Verification record TBD: analysis cases TBD, test cases TBD, correlation method TBD. Update record TBD: evidence-acceptance criteria TBD, revision trigger TBD, supersession handling TBD.

## 9. Interfaces

- Thermal-structural ↔ Vol 14: temperature-field and thermal-load inputs (IDs TBD).
- Thermal-structural ↔ 03.10–03.12 materials: knockdown material-data interface (values TBD).
- Thermal-structural ↔ 03.13 loads: thermal load-case coordination (IDs TBD).
- Thermal-structural ↔ Vol 19: coupled-model hooks (IDs TBD).
- Thermal-structural ↔ 03.20 / VVP thread: verification case and evidence hooks (IDs TBD).

## 10. Operational Concept

Operates evidence-driven: declare thermal inventory TBD → apply knockdown practice TBD → feed strength/fatigue/damage-tolerance consumers TBD → revise on higher-fidelity thermal evidence TBD → submit for verification before any gate use. No thermally affected margin is offered as evidence until verified. Cadence TBD.

## 11. Safety

No safety-related claim (including thermally affected strength or life) is made in this revision. Safety-significant thermal-structural states and their treatment in safety analyses are TBD (Vol 13/24 mapping TBD).

## 12. Performance

Thermal-structural performance indicators TBD (no thresholds baselined): inventory completeness TBD, knockdown-practice maturity TBD, verification closure TBD, update-record currency TBD. Measurement method and reporting cadence TBD.

## 13. Verification & Validation

This document is verified by Inspection against template, header, and requirement discipline. REQ-HFPX-STS-001..004 are verified by their stated methods applied to the inventory, knockdown, verification, and update records. Test methodology is owned by HFPX-STR-TST-001 (03.20); this document defines no test procedure. Validation is programme-authority approval at a gated review (review TBD).

## 14. Risks

- Thermal fields assumed without Vol 14 pedigree; mitigation: REQ-HFPX-STS-001 Vol 14 hook rule with values TBD.
- Full-temperature capability credited without knockdown; mitigation: REQ-HFPX-STS-002 knockdown-practice rule (values TBD).
- Stale thermal inputs retained after better evidence arrives; mitigation: REQ-HFPX-STS-004 update rule with revision records TBD.

## 15. Open Issues

Thermal-load inventory TBD per Vol 14. Material-knockdown methods, conditioning, and values TBD. Verification methods, cases, and status TBD per VVP and Vol 19 hooks. Update triggers and revision records TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SAR/SDP tier allocation (IDs TBD), Vol 14 temperature-field definitions (TBD), material data from 03.10–03.12 (TBD), loads coordination via 03.13 (TBD), Vol 19 coupled-model methodology (TBD), VVP method and gate discipline, and 03.20 test-methodology ownership.

## 18. Traceability

Parents: SYS tier (SYS-001 allocation TBD); SAR/SDP tier (IDs TBD); Vol 06 hooks (IDs TBD); Vol 19 hooks (IDs TBD); VVP thread (VVP-001, VVP-004). Children: inventory records, knockdown records, verification cases, update records (IDs TBD; rows TBD). RTM: REQ-HFPX-STS-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records; any change re-validates affected traceability before gate claims.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (03.19 thermal-structural interaction; requirements REQ-HFPX-STS-001..004) |
