# Vibration

**Document ID:** HFPX-STR-VIB-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the vibration discipline for HFP-X (Chapter 03.17): vibration-source inventory, avoidance criteria, sensor-performance interface, and verification thread. This revision fixes structure only; all sources, criteria, and levels are TBD and no vibration claim is made.

## 2. Scope

Covers structural vibration sources including propulsion-induced vibration, vibration-avoidance criteria, the interface to sensor performance per Vol 09 hooks, and verification per VVP hooks. Excludes structural-dynamics modal ownership (03.18), FCS-coupling treatment (03.18, Vol 07), and test execution (03.20, Vol 22/23).

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (SYS tier allocation TBD)
- HFPX-SYS-ARC-001 SAD (system architecture views and SYS-01 allocation)
- Structural architecture and design-philosophy tier — SAR/SDP tier (IDs TBD)
- Vol 19 Modelling & Simulation (vibration model hooks; IDs TBD)
- HFPX-VV-PLN-001 V&V Plan (VVP thread; method and gate discipline)
- Vol 09 Sensors (sensor-performance interface; IDs TBD)
- Vol 07 Flight Control (control-response interface; IDs TBD)
- HFPX-STR-TST-001 Structural Testing (03.20 test-methodology owner)

## 4. Definitions & Acronyms

- Vibration sources: enumerated excitation mechanisms including propulsion and aero-mechanical sources; entries TBD.
- Avoidance criteria: rules keeping structural response clear of adverse regimes; criteria TBD.
- Sensor-performance interface: allowable vibration at sensor locations preserving sensor function; limits TBD.
- TBD: to be defined; TBC: to be confirmed.

## 5. System Context

Vibration sits within SYS-01 airframe, excited by propulsion, aero-mechanical, and ground-handling sources TBD, affecting structure, equipment, and sensor performance (Vol 09). All source levels, criteria, and interface limits are TBD-valued in this revision and gain authority only through verified evidence per VVP gates.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-SVB-001 | The programme shall define vibration sources as an enumerated list including propulsion-induced sources, with each source definition recorded as TBD. | SYS-001; SAR tier (IDs TBD) | Inspection |
| REQ-HFPX-SVB-002 | The programme shall define vibration-avoidance criteria, with criteria, applicable regimes, and margins recorded as TBD. | SDP tier (IDs TBD); VVP-001 | Analysis |
| REQ-HFPX-SVB-003 | The programme shall define the sensor-performance vibration interface per Vol 09 hooks, with allowable levels and locations recorded as TBD. | SYS-008; Vol 09 (IDs TBD) | Analysis |
| REQ-HFPX-SVB-004 | Vibration behaviour shall be verified by defined analysis and test threads, with methods, cases, and status recorded as TBD per the VVP thread and Vol 19 model hooks. | VVP-001; VVP-004; Vol 19 hooks (IDs TBD) | Analysis + Test |

## 7. Architecture

Vibration architecture (structure only): source layer (REQ-HFPX-SVB-001) enumerating excitations TBD; avoidance layer (REQ-HFPX-SVB-002) governing criteria TBD; sensor-interface layer (REQ-HFPX-SVB-003) governing allowable levels at sensor locations TBD; verification layer (REQ-HFPX-SVB-004) linking models and tests per VVP TBD. Sources, criteria, and levels TBD throughout.

## 8. Detailed Design

Source record TBD: propulsion-induced entries TBD, aero-mechanical entries TBD, ground-handling entries TBD, levels TBD throughout. Avoidance record TBD: criterion definitions TBD, applicable regimes TBD, treatment of resonances TBD, values TBD throughout. Sensor-interface record TBD: sensor locations TBD, allowable levels TBD, Vol 09 interface reference TBD. Verification record TBD: analysis cases TBD, test cases TBD, correlation method TBD.

## 9. Interfaces

- Vibration ↔ propulsion and aero-mechanical sources: excitation inputs (definitions TBD).
- Vibration ↔ Vol 09: sensor-performance interface (allowable levels TBD).
- Vibration ↔ Vol 07: control-response coordination (IDs TBD).
- Vibration ↔ Vol 19: vibration model hooks (IDs TBD).
- Vibration ↔ 03.20 / VVP thread: verification case and evidence hooks (IDs TBD).

## 10. Operational Concept

Operates source-first: enumerate sources TBD → apply avoidance criteria TBD → protect sensor performance TBD → submit for verification per VVP gates TBD. No vibration environment is offered as equipment-qualification evidence until verified. Cadence TBD.

## 11. Safety

No safety-related claim (including vibration adequacy for structure, equipment, or sensors) is made in this revision. Safety-significant vibration regimes and their treatment in safety analyses are TBD (Vol 13/24 mapping TBD).

## 12. Performance

Vibration performance indicators TBD (no thresholds baselined): source-inventory completeness TBD, avoidance-criteria definition status TBD, sensor-interface definition status TBD, verification closure TBD. Measurement method and reporting cadence TBD.

## 13. Verification & Validation

This document is verified by Inspection against template, header, and requirement discipline. REQ-HFPX-SVB-001..004 are verified by their stated methods applied to the source, avoidance-criteria, sensor-interface, and verification records. Test methodology is owned by HFPX-STR-TST-001 (03.20); this document defines no test procedure. Validation is programme-authority approval at a gated review (review TBD).

## 14. Risks

- Vibration sources incompletely enumerated; mitigation: REQ-HFPX-SVB-001 enumerated-list rule including propulsion (entries TBD).
- Adverse response accepted without criteria; mitigation: REQ-HFPX-SVB-002 avoidance-criteria rule (criteria TBD).
- Sensor degradation from unbudgeted vibration; mitigation: REQ-HFPX-SVB-003 Vol 09 interface rule (levels TBD).

## 15. Open Issues

Vibration sources TBD including propulsion contributions. Avoidance criteria TBD. Vol 09 sensor-performance interface levels and locations TBD. Verification methods, cases, and status TBD per VVP and Vol 19 hooks.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SAR/SDP tier allocation (IDs TBD), propulsion and aero-mechanical source definitions (TBD), Vol 09 sensor limits (TBD), Vol 07 control-response coordination (TBD), Vol 19 vibration-model methodology (TBD), VVP method and gate discipline, and 03.20 test-methodology ownership.

## 18. Traceability

Parents: SYS tier (SYS-001, SYS-008 allocation TBD); SAR/SDP tier (IDs TBD); Vol 06 hooks (IDs TBD); Vol 19 hooks (IDs TBD); VVP thread (VVP-001, VVP-004). Children: source records, avoidance-criteria records, sensor-interface records, verification cases (IDs TBD; rows TBD). RTM: REQ-HFPX-SVB-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records; any change re-validates affected traceability before gate claims.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (03.17 vibration; requirements REQ-HFPX-SVB-001..004) |
