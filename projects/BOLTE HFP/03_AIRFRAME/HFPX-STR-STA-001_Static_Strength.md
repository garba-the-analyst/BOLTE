# Static Strength

**Document ID:** HFPX-STR-STA-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the static-strength discipline for HFP-X (Chapter 03.14): analysis ownership, margin policy, test-correlation discipline, and the no-claim-before-evidence rule. This revision fixes structure only; all methods, margins, and results are TBD and no strength claim is made.

## 2. Scope

Covers static-strength analysis ownership including FEA, margin policy, correlation of analysis to test, and authority for strength claims. Excludes loads definition (03.13), fatigue and damage-tolerance execution (03.15–03.16), material allowables ownership (03.10–03.12), and test execution (03.20, Vol 22/23).

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (SYS tier allocation TBD)
- HFPX-SYS-ARC-001 SAD (system architecture views and SYS-01 allocation)
- Structural architecture and design-philosophy tier — SAR/SDP tier (IDs TBD)
- HFPX-STR-LOD-001 Structural Loads (loads feed; REQ-HFPX-SLD-001..005)
- Vol 19 Modelling & Simulation (structural model and FEA hooks; IDs TBD)
- HFPX-VV-PLN-001 V&V Plan (VVP thread; method and gate discipline)
- HFPX-STR-TST-001 Structural Testing (03.20 test-methodology owner)

## 4. Definitions & Acronyms

- Static-strength analysis: demonstration that structure sustains design loads within policy; ownership and methods TBD.
- FEA: finite-element analysis; model ownership, fidelity, and status TBD.
- Margin policy: rules governing strength margins and their presentation; criteria TBD.
- Test correlation: comparison of analysis predictions to test outcomes; method TBD.
- TBD: to be defined; TBC: to be confirmed.

## 5. System Context

Static strength consumes verified loads (03.13) and allowables (03.10–03.12) through Vol 19 structural models under SYS-01, producing margin records consumed by design decisions and VVP gates. All margins are TBD-valued in this revision and gain authority solely through verified analysis-test correlation.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-SST-001 | The programme shall define static-strength analysis ownership including FEA ownership, with owners, model fidelity, and status recorded as TBD. | SAR tier (IDs TBD); Vol 19 hooks (IDs TBD) | Inspection |
| REQ-HFPX-SST-002 | The programme shall define the static-strength margin policy, with margin definitions, presentation rules, and acceptance discipline recorded as TBD. | SDP tier (IDs TBD); VVP-001 | Analysis |
| REQ-HFPX-SST-003 | The programme shall apply a test-correlation rule requiring strength analyses to be correlated to test outcomes, with correlation method and records TBD per the VVP thread. | VVP-001; VVP-004 | Analysis |
| REQ-HFPX-SST-004 | No static-strength claim shall be offered as gate evidence until supporting analysis and correlated test evidence are verified, with evidence status TBD and no strength value baselined in this revision. | VVP-004; SDP tier (IDs TBD) | Inspection |

## 7. Architecture

Strength architecture (structure only): ownership layer (REQ-HFPX-SST-001) assigning FEA and analysis responsibility TBD; margin layer (REQ-HFPX-SST-002) governing margin presentation TBD; correlation layer (REQ-HFPX-SST-003) linking predictions to tests TBD; authority layer (REQ-HFPX-SST-004) gating claims on verified evidence TBD. Methods, margins, and results TBD throughout.

## 8. Detailed Design

Ownership record TBD: analysis owners TBD, FEA model register TBD, fidelity designations TBD, configuration references TBD. Margin-policy record TBD: margin definitions TBD, presentation format TBD, acceptance discipline TBD, values TBD throughout. Correlation record TBD: correlated cases TBD, comparison method TBD, discrepancy handling TBD. Authority record TBD: evidence references TBD, gate status TBD.

## 9. Interfaces

- Strength ↔ 03.13 loads: TBD-valued loads feed (interface TBD).
- Strength ↔ 03.10–03.12 materials: allowables feed (values TBD).
- Strength ↔ Vol 19: FEA and structural-model hooks (IDs TBD).
- Strength ↔ 03.20 / VVP thread: correlation cases and evidence hooks (IDs TBD).
- Strength ↔ SAR/SDP tier: ownership and margin-policy allocation (IDs TBD).

## 10. Operational Concept

Operates claim-last: assign ownership TBD → analyse under margin policy TBD → correlate to test TBD → offer claims only on verified correlated evidence TBD. No margin is cited for decisions until authority per REQ-HFPX-SST-004 is met. Cadence TBD.

## 11. Safety

No safety-related claim (including static-strength capability or margin) is made in this revision. Safety-significant strength items and their treatment in safety analyses are TBD (Vol 13/24 mapping TBD).

## 12. Performance

Static-strength performance indicators TBD (no thresholds baselined): ownership-definition completeness TBD, margin-policy definition status TBD, correlation coverage TBD, verification closure TBD. Measurement method and reporting cadence TBD.

## 13. Verification & Validation

This document is verified by Inspection against template, header, and requirement discipline. REQ-HFPX-SST-001..004 are verified by their stated methods applied to the ownership, margin-policy, correlation, and authority records. Test methodology is owned by HFPX-STR-TST-001 (03.20); this document defines no test procedure. Validation is programme-authority approval at a gated review (review TBD).

## 14. Risks

- Analysis cited without ownership or configuration control; mitigation: REQ-HFPX-SST-001 ownership rule (assignments TBD).
- Margins presented without policy; mitigation: REQ-HFPX-SST-002 margin-policy rule (criteria TBD).
- Uncorrelated analysis offered as evidence; mitigation: REQ-HFPX-SST-003 correlation rule and REQ-HFPX-SST-004 authority rule.

## 15. Open Issues

Analysis and FEA ownership TBD. Margin policy TBD. Correlation method and records TBD. Evidence status and gate authority TBD per VVP hooks.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SAR/SDP tier allocation (IDs TBD), loads feed from 03.13 (TBD), allowables from 03.10–03.12 (TBD), Vol 19 FEA methodology (TBD), VVP method and gate discipline, and 03.20 test-methodology ownership.

## 18. Traceability

Parents: SYS tier (SYS-001 allocation TBD); SAR/SDP tier (IDs TBD); Vol 06 hooks (IDs TBD); Vol 19 hooks (IDs TBD); VVP thread (VVP-001, VVP-004). Children: ownership records, margin-policy records, correlation records, verification cases (IDs TBD; rows TBD). RTM: REQ-HFPX-SST-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records; any change re-validates affected traceability before gate claims.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (03.14 static strength; requirements REQ-HFPX-SST-001..004) |
