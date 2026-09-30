# System Requirements Specification (SyRS) — Stub

**Document ID:** HFPX-SYS-REQ-001  
**Revision:** B (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 1 stub, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Hold the system-level requirements for HFP-X in one specification. This Tranche 1 version is a **stub**: it establishes the requirement set structure, the top-level system requirements and the derivation path; detailed sub-tiers (01.7–01.17) follow in later tranches. Backbone document 2 of 5.

## 2. Scope

Covers system requirements derived from Mission (01.1), Operational Concept (01.2), CONOPS (01.3) and Stakeholder Requirements (01.4). Classifications per prompt §9: mission, stakeholder, operational, functional, performance, interface, safety, environmental, structural, software, hardware, human factors, reliability, maintainability, manufacturing, certification, security, cybersecurity, verification. All quantitative values TBD.

## 3. Applicable Documents

- HFPX-SYS-MIS-001, HFPX-SYS-OPC-001, HFPX-SYS-CON-001, HFPX-SYS-STK-001 (parents)
- HFPX-SYS-ARC-001 SAD (stub, allocates these requirements to SYS-01..SYS-23)
- HFPX-VV-PLN-001 V&V Plan (not written); HFPX-SAFE-CAS-001 Safety Case (not written)
- HFP prompt §§8–10 (requirements format, classification, traceability)

## 4. Definitions & Acronyms

- SyRS: this specification; requirement ID `REQ-HFPX-[DOMAIN]-[NNN]`; verification: Analysis / Inspection / Demonstration / Test
- TBD/TBC/A-XXX: unknown data handling; no invented values (prompt §§19, 32)
- SYS-01..SYS-23: system breakdown (prompt §12): airframe, aerodynamic/lifting, propulsion, fuel, FCS, avionics, navigation, sensors, electrical, embedded computing, comms, helmet, pilot interface, suit, impact protection, recovery, thermal, ground station, software, cybersecurity, AI monitoring, maintenance, training

## 5. System Context

SyRS is the bridge between needs and architecture:

```text
MISSION (MIS) → STAKEHOLDER (STK) → SYSTEM (this SyRS) → SUBSYSTEM (Vol 03–18) → DESIGN → TEST → EVIDENCE
```

Detailed tiers map to chapters: 01.7 functional, 01.8 performance, 01.9 environmental, 01.10 safety, 01.11 human factors, 01.12 reliability, 01.13 maintainability, 01.14 security, 01.15 regulatory, 01.16 interface, 01.17 derived. RTM (01.18) is the law.

## 6. Requirements

Top-level system requirements (detailed tiers TBD in later tranches):

| ID | Requirement (shall) | Parent | Subsystem | Verification |
| --- | --- | --- | --- | --- |
| REQ-HFPX-SYS-001 | The system shall provide controlled VTOL hover, transition, horizontal cruise and landing per CONOPS threads. | MIS-001..003, CON-001 | SYS-05 + SYS-03 + SYS-02 | Test |
| REQ-HFPX-SYS-002 | The system shall implement deterministic, bounded, independently verifiable primary flight control; AI shall operate as monitoring/advisory layer only. | STK-001/002 | SYS-05, SYS-21 | Analysis + Test |
| REQ-HFPX-SYS-003 | The system shall provide an independent safety path (detection → stabilisation → recovery/safe state) separate from the primary control path. | STK-001, MIS-005 | SYS-16 + safety computer | Analysis + Test |
| REQ-HFPX-SYS-004 | The system shall provide navigation (inertial, GNSS, barometric altitude, air data) sufficient for controlled flight in the defined envelope (accuracies TBD). | MIS-001..003 | SYS-07/08 | Analysis + Test |
| REQ-HFPX-SYS-005 | The system shall provide pilot/operator status, warning and emergency guidance via helmet/HMI and ground-station telemetry. | STK-007 | SYS-12/13/18, SYS-11 | Demonstration |
| REQ-HFPX-SYS-006 | The system shall operate within defined environmental limits (temperature, humidity, rain, dust, wind — values TBD). | REQ-HFPX-MIS-001 | All | Analysis + Test |
| REQ-HFPX-SYS-007 | The system shall meet defined interface requirements for propulsion, fuel, power, data and human-system boundaries (details TBD, Vol 02 ICDs). | STK-006 | SYS-01..23 | Inspection |
| REQ-HFPX-SYS-008 | Quantitative performance (mass, thrust, endurance, speed, range, altitude) shall remain TBD until budgets and models exist; no value in this SyRS is approved. | MIS-007 | SYS-03/04 | Inspection |

## 7. Architecture

Allocation (starter — SAD owns the authoritative allocation): SYS-001 → FCS/propulsion/aero; SYS-002 → FCS + AI monitoring; SYS-003 → safety computer + recovery; SYS-004 → nav/sensors; SYS-005 → helmet/HMI/comms/ground station; SYS-006 → thermal/environmental; SYS-007 → ICDs (02.16/02.17); SYS-008 → budgets (Vol 06/19 actions).

## 8. Detailed Design

Not applicable — system level only. Subsystem requirements live in Vol 03–18 and are TBD.

## 9. Interfaces

Interface requirements chapter is 01.16 (TBD). External interface placeholders: airspace/range, GNSS, spectrum, ground support equipment, fuel/power servicing. Internal interfaces controlled via SAD §9/ICDs.

## 10. Operational Concept

System requirements are exercised through CONOPS threads: each SYS requirement maps to ≥1 nominal/off-nominal scenario (mapping table TBD in V&V Plan).

## 11. Safety

System safety requirements chapter is 01.10 (TBD, feeds Safety Case). SYS-002/SYS-003 encode the two load-bearing safety policies: deterministic primary control and independent safety path. FHA/FMEA/FTA (Vol 13) will generate further system safety requirements by change record. Hazardous-subsystem boundary applies (prompt §§14, 34).

## 12. Performance

Intentionally TBD (SYS-008). No mass, thrust, thrust-to-weight, endurance, range, speed or altitude requirement is quantified until ISS-007 actions complete. Future performance tier (01.8) will reference budgets and 6-DOF results, never invented figures.

## 13. Verification & Validation

Each requirement states its method above; verification IDs and cases are TBD in the V&V Plan (Vol 22). Strategy: analysis (models, Vol 19) → inspection/demonstration (ground) → test (unmanned, Vol 33/23). Requirements without a verification method are rejected at SRR.

## 14. Risks

- SyRS written before envelopes/budgets exist → high TBD density; mitigation: stub status is explicit, SRR exit requires only structure + top-level set, not quantified tiers
- Orphaned requirements as Vol 03–18 grow; mitigation: RTM coverage gate per review (SEMP)

## 15. Open Issues

ISS-002 (SyRS completeness — this stub partially addresses; stays OPEN), ISS-003/004 (trades shape subsystem reqs), ISS-006/007/008 (feasibility unknowns propagate into 01.8/01.10).

## 16. Assumptions


_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on stakeholder approval (STK), CONOPS stability, SAD allocation feedback, safety analyses (Vol 13), models/budgets (Vol 06/19), V&V Plan cases.

## 18. Traceability

Parents: MIS / OPC / CON / STK (table above). Children: SAD views, subsystem requirements (Vol 03–18), V&V cases, RTM rows. RTM seed for SYS-001..008 is added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0. Tranche 1 stub, CONCEPT, not baselined. Quantified tiers require new revisions via change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 1 stub (Chapter 01.6; backbone 2/5) |
| B | 2026-09-29 | Assumptions removed; all unknowns recorded as TBD (no assumptions raised or relied upon). |
