# Metallic Structures

**Document ID:** HFPX-STR-MET-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the metallic-structures discipline for HFP-X (Chapter 03.12): application scope, metallic allowables, corrosion-protection discipline, and verification thread. This revision fixes structure only; all applications, methods, and values are TBD and no strength or life claim is made.

## 2. Scope

Covers metallic-structure applications across airframe structure, metallic allowables practice, corrosion-protection discipline, and the verification thread per VVP hooks. Excludes composite structures (03.11), loads definition (03.13), strength/fatigue/damage-tolerance analysis execution (03.14–03.16), and test execution (03.20, Vol 22/23).

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (SYS tier allocation TBD)
- HFPX-SYS-ARC-001 SAD (system architecture views and SYS-01 allocation)
- Structural architecture and design-philosophy tier — SAR/SDP tier (IDs TBD)
- Vol 06 Aerodynamics (aero-load inputs to metallic sizing; IDs TBD)
- Vol 19 Modelling & Simulation (structural model hooks; IDs TBD)
- HFPX-VV-PLN-001 V&V Plan (VVP thread; method and gate discipline)
- HFPX-STR-TST-001 Structural Testing (03.20 test-methodology owner)

## 4. Definitions & Acronyms

- Metallic applications: enumerated airframe uses of metallic material systems; list TBD.
- Metallic allowables: design-permitted metallic material values; values TBD.
- Corrosion protection: treatments, coatings, and maintenance provisions preserving metallic integrity; scope TBD.
- TBD: to be defined; TBC: to be confirmed.

## 5. System Context

Metallic structures form part of SYS-01 airframe within the HFP-X system architecture. Application selection, allowables, and corrosion-protection provisions feed strength, fatigue, and damage-tolerance analyses (03.14–03.16) and test articles (03.20). All feeds are TBD-valued in this revision and gain authority only through verified evidence per VVP gates.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-SMD-001 | The programme shall define metallic-structure applications as an enumerated list, with each entry and its allocation recorded as TBD. | SYS-001; SAR tier (IDs TBD) | Inspection |
| REQ-HFPX-SMD-002 | The programme shall define metallic allowables, with test basis, statistical treatment, and values recorded as TBD. | SDP tier (IDs TBD); VVP-001 | Analysis |
| REQ-HFPX-SMD-003 | The programme shall define corrosion-protection provisions for metallic structure, with treatments, interfaces, and maintenance provisions recorded as TBD. | SAR tier (IDs TBD); SDP tier (IDs TBD) | Inspection |
| REQ-HFPX-SMD-004 | Metallic structures shall be verified by defined analysis and test threads, with methods, cases, and correlation discipline recorded as TBD per the VVP thread and Vol 19 model hooks. | VVP-001; VVP-004; Vol 19 hooks (IDs TBD) | Analysis + Test |

## 7. Architecture

Metallic discipline architecture (structure only): application layer (REQ-HFPX-SMD-001) enumerating candidate uses TBD; allowables layer (REQ-HFPX-SMD-002) governing test basis and values TBD; corrosion-protection layer (REQ-HFPX-SMD-003) governing treatments and provisions TBD; verification layer (REQ-HFPX-SMD-004) linking models and tests per VVP TBD. Alloy systems, tempers, and extents TBD throughout.

## 8. Detailed Design

Application record TBD: candidate metallic zones TBD, allocation rationale TBD, excluded zones TBD. Allowables record TBD: test basis TBD, specimen scope TBD, statistical treatment TBD, values TBD throughout. Corrosion-protection record TBD: treatment types TBD, application zones TBD, interface with coatings and sealants TBD, maintenance provisions TBD. Verification record TBD: analysis cases TBD, test cases TBD, correlation method TBD.

## 9. Interfaces

- Metallic discipline ↔ SAR/SDP tier: application and philosophy allocation (IDs TBD).
- Metallic discipline ↔ Vol 06 / Vol 19: aero inputs and structural model hooks (IDs TBD).
- Metallic discipline ↔ corrosion/maintenance provisions: treatment and sustainment interface (Vol 27 hooks TBD).
- Metallic discipline ↔ 03.14–03.16: allowables feed to strength/fatigue/damage-tolerance analyses.
- Metallic discipline ↔ 03.20 / VVP thread: verification case and evidence hooks (IDs TBD).

## 10. Operational Concept

Operates as definition-before-use: declare applications TBD → establish allowables TBD → define corrosion protection TBD → feed analyses TBD → submit for verification per VVP gates TBD. No metallic part is offered as strength evidence until verified. Cadence TBD.

## 11. Safety

No safety-related claim (including strength, fatigue life, or damage tolerance of metallic structure) is made in this revision. Safety-significant metallic items and their treatment in safety analyses are TBD (Vol 13/24 mapping TBD).

## 12. Performance

Metallic discipline performance indicators TBD (no thresholds baselined): application-list completeness TBD, allowables maturity TBD, corrosion-protection definition status TBD, verification closure TBD. Measurement method and reporting cadence TBD.

## 13. Verification & Validation

This document is verified by Inspection against template, header, and requirement discipline. REQ-HFPX-SMD-001..004 are verified by their stated methods applied to the application, allowables, corrosion-protection, and verification records. Test methodology is owned by HFPX-STR-TST-001 (03.20); this document defines no test procedure. Validation is programme-authority approval at a gated review (review TBD).

## 14. Risks

- Metallic applications assumed before allowables exist; mitigation: REQ-HFPX-SMD-001 enumerated-list rule with TBD status explicit.
- Allowables cited without pedigree; mitigation: REQ-HFPX-SMD-002 basis rule with values TBD.
- Corrosion provisions deferred until detail design; mitigation: REQ-HFPX-SMD-003 provision rule raised at CONCEPT (details TBD).

## 15. Open Issues

Metallic applications TBD. Allowables basis and values TBD. Corrosion-protection treatments, zones, and maintenance provisions TBD. Verification methods, cases, and correlation discipline TBD per VVP and Vol 19 hooks.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SAR/SDP tier allocation (IDs TBD), SYS tier stability, Vol 06 aero inputs (TBD), Vol 19 model-hook methodology (TBD), corrosion and sustainment provisions (TBD), VVP method and gate discipline, and 03.20 test-methodology ownership.

## 18. Traceability

Parents: SYS tier (SYS-001 allocation TBD); SAR/SDP tier (IDs TBD); Vol 06 hooks (IDs TBD); Vol 19 hooks (IDs TBD); VVP thread (VVP-001, VVP-004). Children: application records, allowables records, corrosion-protection records, verification cases (IDs TBD; rows TBD). RTM: REQ-HFPX-SMD-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records; any change re-validates affected traceability before gate claims.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (03.12 metallic structures; requirements REQ-HFPX-SMD-001..004) |
