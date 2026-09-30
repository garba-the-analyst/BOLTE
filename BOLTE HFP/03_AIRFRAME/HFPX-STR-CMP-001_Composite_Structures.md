# Composite Structures

**Document ID:** HFPX-STR-CMP-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the composite-structures discipline for HFP-X (Chapter 03.11): application scope, allowables and building-block practice, manufacturing interface, and verification thread. This revision fixes structure only; all applications, methods, and values are TBD and no strength or life claim is made.

## 2. Scope

Covers composite-structure applications across airframe structure, composite allowables and building-block practice, the manufacturing interface per Vol 20.5 hooks, and the verification thread per VVP hooks. Excludes metallic structures (03.12), loads definition (03.13), strength/fatigue/damage-tolerance analysis execution (03.14–03.16), and test execution (03.20, Vol 22/23).

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (SYS tier allocation TBD)
- HFPX-SYS-ARC-001 SAD (system architecture views and SYS-01 allocation)
- Structural architecture and design-philosophy tier — SAR/SDP tier (IDs TBD)
- Vol 06 Aerodynamics (aero-load inputs to composite sizing; IDs TBD)
- Vol 19 Modelling & Simulation (structural model hooks; IDs TBD)
- HFPX-VV-PLN-001 V&V Plan (VVP thread; method and gate discipline)
- Vol 20.5 Manufacturing interface (details TBD)
- HFPX-STR-TST-001 Structural Testing (03.20 test-methodology owner)

## 4. Definitions & Acronyms

- Composite applications: enumerated airframe uses of composite material systems; list TBD.
- Allowables: design-permitted composite material values; values TBD.
- Building-block practice: coupon-to-element-to-subcomponent-to-component verification progression; levels and methods TBD.
- TBD: to be defined; TBC: to be confirmed.

## 5. System Context

Composite structures form part of SYS-01 airframe within the HFP-X system architecture. Application selection, allowables development, and manufacturing discipline feed strength, fatigue, and damage-tolerance analyses (03.14–03.16) and test articles (03.20). All feeds are TBD-valued in this revision and gain authority only through verified evidence per VVP gates.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-SCP-001 | The programme shall define composite-structure applications as an enumerated list, with each entry and its allocation recorded as TBD. | SYS-001; SAR tier (IDs TBD) | Inspection |
| REQ-HFPX-SCP-002 | The programme shall define composite allowables and building-block practice, with test levels, methods, and values recorded as TBD. | SDP tier (IDs TBD); VVP-001 | Analysis |
| REQ-HFPX-SCP-003 | The programme shall define the composite manufacturing interface per Vol 20.5 hooks, with process controls, interfaces, and acceptance discipline recorded as TBD. | SAR tier (IDs TBD); Vol 20.5 (IDs TBD) | Inspection |
| REQ-HFPX-SCP-004 | Composite structures shall be verified by defined analysis and test threads, with methods, cases, and correlation discipline recorded as TBD per the VVP thread and Vol 19 model hooks. | VVP-001; VVP-004; Vol 19 hooks (IDs TBD) | Analysis + Test |

## 7. Architecture

Composite discipline architecture (structure only): application layer (REQ-HFPX-SCP-001) enumerating candidate uses TBD; allowables layer (REQ-HFPX-SCP-002) governing coupon-to-component progression TBD; manufacturing-interface layer (REQ-HFPX-SCP-003) linking design to Vol 20.5 TBD; verification layer (REQ-HFPX-SCP-004) linking models and tests per VVP TBD. Material systems, layups, and extents TBD throughout.

## 8. Detailed Design

Application record TBD: candidate composite zones TBD, allocation rationale TBD, excluded zones TBD. Allowables record TBD: coupon scope TBD, element and subcomponent scope TBD, environmental conditioning TBD, statistical treatment TBD, values TBD throughout. Manufacturing-interface record TBD: process specification TBD, control parameters TBD, interface ownership TBD per Vol 20.5. Verification record TBD: analysis cases TBD, test cases TBD, correlation method TBD.

## 9. Interfaces

- Composite discipline ↔ SAR/SDP tier: application and philosophy allocation (IDs TBD).
- Composite discipline ↔ Vol 06 / Vol 19: aero inputs and structural model hooks (IDs TBD).
- Composite discipline ↔ Vol 20.5: manufacturing process and control interface (details TBD).
- Composite discipline ↔ 03.14–03.16: allowables feed to strength/fatigue/damage-tolerance analyses.
- Composite discipline ↔ 03.20 / VVP thread: verification case and evidence hooks (IDs TBD).

## 10. Operational Concept

Operates as definition-before-use: declare applications TBD → develop allowables per building-block practice TBD → control manufacturing interface TBD → feed analyses TBD → submit for verification per VVP gates TBD. No composite part is offered as strength evidence until verified. Cadence TBD.

## 11. Safety

No safety-related claim (including strength, fatigue life, or damage tolerance of composite structure) is made in this revision. Safety-significant composite items and their treatment in safety analyses are TBD (Vol 13/24 mapping TBD).

## 12. Performance

Composite discipline performance indicators TBD (no thresholds baselined): application-list completeness TBD, allowables maturity TBD, manufacturing-interface definition status TBD, verification closure TBD. Measurement method and reporting cadence TBD.

## 13. Verification & Validation

This document is verified by Inspection against template, header, and requirement discipline. REQ-HFPX-SCP-001..004 are verified by their stated methods applied to the application, allowables, manufacturing-interface, and verification records. Test methodology is owned by HFPX-STR-TST-001 (03.20); this document defines no test procedure. Validation is programme-authority approval at a gated review (review TBD).

## 14. Risks

- Composite applications assumed before allowables exist; mitigation: REQ-HFPX-SCP-001 enumerated-list rule with TBD status explicit.
- Allowables cited without building-block pedigree; mitigation: REQ-HFPX-SCP-002 practice rule with levels and values TBD.
- Manufacturing variation unlinked from design; mitigation: REQ-HFPX-SCP-003 Vol 20.5 interface rule (details TBD).

## 15. Open Issues

Composite applications TBD. Allowables and building-block levels, methods, and values TBD. Vol 20.5 manufacturing-interface details TBD. Verification methods, cases, and correlation discipline TBD per VVP and Vol 19 hooks.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SAR/SDP tier allocation (IDs TBD), SYS tier stability, Vol 06 aero inputs (TBD), Vol 19 model-hook methodology (TBD), Vol 20.5 manufacturing definition (TBD), VVP method and gate discipline, and 03.20 test-methodology ownership.

## 18. Traceability

Parents: SYS tier (SYS-001 allocation TBD); SAR/SDP tier (IDs TBD); Vol 06 hooks (IDs TBD); Vol 19 hooks (IDs TBD); VVP thread (VVP-001, VVP-004). Children: application records, allowables records, manufacturing-interface records, verification cases (IDs TBD; rows TBD). RTM: REQ-HFPX-SCP-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records; any change re-validates affected traceability before gate claims.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (03.11 composite structures; requirements REQ-HFPX-SCP-001..004) |
