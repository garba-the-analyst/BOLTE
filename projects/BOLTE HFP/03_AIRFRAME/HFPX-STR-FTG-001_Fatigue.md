# Fatigue

**Document ID:** HFPX-STR-FTG-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the fatigue discipline for HFP-X (Chapter 03.15): spectra definition, life-analysis practice, inspection-interval hooks, and verification thread. This revision fixes structure only; all spectra, lives, and intervals are TBD and no life claim is made.

## 2. Scope

Covers fatigue spectra, fatigue life-analysis practice, hooks to inspection intervals per Vol 27.9, and verification per VVP hooks. Excludes loads definition (03.13), static-strength and damage-tolerance execution (03.14, 03.16), and test execution (03.20, Vol 22/23).

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (SYS tier allocation TBD)
- HFPX-SYS-ARC-001 SAD (system architecture views and SYS-01 allocation)
- Structural architecture and design-philosophy tier — SAR/SDP tier (IDs TBD)
- HFPX-STR-LOD-001 Structural Loads (loads feed; REQ-HFPX-SLD-001..005)
- Vol 19 Modelling & Simulation (fatigue model hooks; IDs TBD)
- HFPX-VV-PLN-001 V&V Plan (VVP thread; method and gate discipline)
- Vol 27.9 Maintenance/inspection intervals (hooks TBD)
- HFPX-STR-TST-001 Structural Testing (03.20 test-methodology owner)

## 4. Definitions & Acronyms

- Fatigue spectra: repeated-load sequences applied to life analysis; definitions TBD.
- Life-analysis practice: methods predicting fatigue lives and scatter treatment; methods TBD.
- Inspection-interval hooks: links from fatigue findings to Vol 27.9 intervals; intervals TBD.
- TBD: to be defined; TBC: to be confirmed.

## 5. System Context

Fatigue consumes verified loads spectra (03.13) and material data (03.10–03.12) through Vol 19 models under SYS-01, producing life records that inform inspection intervals (Vol 27.9) and VVP gates. All lives and intervals are TBD-valued in this revision and gain authority only through verified evidence.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-SFT-001 | The programme shall define fatigue spectra, with spectrum definitions, sources, and values recorded as TBD. | SYS-001; Vol 19 hooks (IDs TBD) | Analysis |
| REQ-HFPX-SFT-002 | The programme shall define fatigue life-analysis practice, with methods, scatter treatment, and results recorded as TBD. | SDP tier (IDs TBD); VVP-001 | Analysis |
| REQ-HFPX-SFT-003 | The programme shall define inspection-interval hooks to Vol 27.9 arising from fatigue findings, with hook definitions and intervals recorded as TBD. | SAR tier (IDs TBD); Vol 27.9 (IDs TBD) | Inspection |
| REQ-HFPX-SFT-004 | Fatigue lives and intervals shall be verified by defined analysis and test threads, with methods, cases, and status recorded as TBD per the VVP thread. | VVP-001; VVP-004 | Analysis + Test |

## 7. Architecture

Fatigue architecture (structure only): spectra layer (REQ-HFPX-SFT-001) defining repeated-load inputs TBD; life-analysis layer (REQ-HFPX-SFT-002) predicting lives TBD; interval-hook layer (REQ-HFPX-SFT-003) linking to Vol 27.9 TBD; verification layer (REQ-HFPX-SFT-004) linking models and tests per VVP TBD. Spectra, lives, and intervals TBD throughout.

## 8. Detailed Design

Spectra record TBD: spectrum families TBD, mission-mix inputs TBD, derivation method TBD, values TBD throughout. Life-analysis record TBD: analytical methods TBD, material-data references TBD, scatter treatment TBD, life results TBD. Interval-hook record TBD: hook criteria TBD, Vol 27.9 interface TBD, interval values TBD. Verification record TBD: analysis cases TBD, test cases TBD, correlation method TBD.

## 9. Interfaces

- Fatigue ↔ 03.13 loads: spectra inputs (definitions TBD).
- Fatigue ↔ 03.10–03.12 materials: fatigue material data (values TBD).
- Fatigue ↔ Vol 19: fatigue model hooks (IDs TBD).
- Fatigue ↔ Vol 27.9: inspection-interval hooks (IDs TBD).
- Fatigue ↔ 03.20 / VVP thread: verification case and evidence hooks (IDs TBD).

## 10. Operational Concept

Operates spectra-first: define spectra TBD → analyse lives TBD → derive interval hooks TBD → submit for verification per VVP gates TBD. No life or interval is offered as sustainment evidence until verified. Cadence TBD.

## 11. Safety

No safety-related claim (including fatigue life or inspection adequacy) is made in this revision. Safety-significant fatigue items and their treatment in safety analyses are TBD (Vol 13/24 mapping TBD).

## 12. Performance

Fatigue performance indicators TBD (no thresholds baselined): spectra-definition completeness TBD, life-analysis maturity TBD, interval-hook definition status TBD, verification closure TBD. Measurement method and reporting cadence TBD.

## 13. Verification & Validation

This document is verified by Inspection against template, header, and requirement discipline. REQ-HFPX-SFT-001..004 are verified by their stated methods applied to the spectra, life-analysis, interval-hook, and verification records. Test methodology is owned by HFPX-STR-TST-001 (03.20); this document defines no test procedure. Validation is programme-authority approval at a gated review (review TBD).

## 14. Risks

- Spectra assumed without mission basis; mitigation: REQ-HFPX-SFT-001 definition rule with sources TBD.
- Lives cited without scatter treatment; mitigation: REQ-HFPX-SFT-002 practice rule (methods TBD).
- Intervals decoupled from fatigue findings; mitigation: REQ-HFPX-SFT-003 Vol 27.9 hook rule (intervals TBD).

## 15. Open Issues

Fatigue spectra TBD. Life-analysis methods and results TBD. Vol 27.9 inspection-interval hooks and intervals TBD. Verification methods, cases, and status TBD per VVP hooks.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SAR/SDP tier allocation (IDs TBD), loads spectra from 03.13 (TBD), material data from 03.10–03.12 (TBD), Vol 19 fatigue-model methodology (TBD), Vol 27.9 interval ownership (TBD), VVP method and gate discipline, and 03.20 test-methodology ownership.

## 18. Traceability

Parents: SYS tier (SYS-001 allocation TBD); SAR/SDP tier (IDs TBD); Vol 06 hooks (IDs TBD); Vol 19 hooks (IDs TBD); VVP thread (VVP-001, VVP-004). Children: spectra records, life-analysis records, interval-hook records, verification cases (IDs TBD; rows TBD). RTM: REQ-HFPX-SFT-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records; any change re-validates affected traceability before gate claims.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (03.15 fatigue; requirements REQ-HFPX-SFT-001..004) |
