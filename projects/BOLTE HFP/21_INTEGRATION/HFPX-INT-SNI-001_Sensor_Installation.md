# Sensor Installation

**Document ID:** HFPX-INT-SNI-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X sensor installation view (Chapter 21.7): the installation-specification structure for sensors, including sequencing, mounting provisions, and alignment and calibration hooks.

## 2. Scope

Covers sensor installation sequencing and specification structure for the production-aircraft concept. Alignment and calibration hooks are TBD (Vol 09.17). All aperture provisions, mounting specifications, connector specifications, and verification methods TBD. Methodology and sequencing only.

## 3. Applicable Documents

- HFPX-ARC-IFR-001 System Interfaces (interface register and ICD rule); HFPX-INT-STR-001 Assembly Strategy (Chapter 21.1)
- ICD tier (documents TBD)
- Sensor subsystem inputs (Vol 09, including 09.17, details TBD)
- VVP thread (documents TBD)

## 4. Definitions & Acronyms

- Sensor installation: placement, mounting, and connection of sensors including aperture provisions (scope TBD).
- Alignment hook: defined interface to sensor alignment provisions (details TBD, Vol 09.17).
- Calibration hook: defined interface to sensor calibration provisions (details TBD, Vol 09.17).

## 5. System Context

Sensor installation integrates sensing apertures, mounts, power, and data interfaces with structure, avionics, and ground-service interfaces, within the build sequence (21.1), prior to system integration (21.12) and integration testing (21.13).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-KSI-001 | The sensor installation specification shall define the installation sequence and stage gates (sequence and criteria TBD). | IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD); sensor inputs including Vol 09.17 (TBD); VVP thread (TBD) | Inspection |
| REQ-HFPX-KSI-002 | The sensor installation specification shall capture each sensor mounting and aperture provision and its governing interface definition (details TBD). | IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD); sensor inputs including Vol 09.17 (TBD); VVP thread (TBD) | Inspection |
| REQ-HFPX-KSI-003 | The sensor installation specification shall capture each sensor connector and data interface and its governing interface definition (details TBD). | IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD); sensor inputs including Vol 09.17 (TBD); VVP thread (TBD) | Inspection |
| REQ-HFPX-KSI-004 | The sensor installation specification shall define alignment and calibration hooks for each applicable sensor (details TBD, Vol 09.17 hooks). | IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD); sensor inputs including Vol 09.17 (TBD); VVP thread (TBD) | Inspection |

## 7. Architecture

Installation framework: staged sensor installation (stages TBD), mounting and aperture register (TBD), connector and data interface register (TBD), and alignment/calibration hooks (TBD, Vol 09.17), with gate reviews and as-built recording (TBD).

## 8. Detailed Design

Not applicable at Tranche 6 draft level. Mounting definitions, aperture definitions, and alignment and calibration specifications are TBD in subsystem inputs and ICDs.

## 9. Interfaces

Each sensor installation interface points to its interface definition in the IFR/ICD tier (TBD). Alignment and calibration hooks point to Vol 09.17 provisions (TBD). Sequencing aligns with the build strategy (21.1).

## 10. Operational Concept

Installation methodology and sequencing only: staged mounting and connection under configuration control with gate reviews (flow TBD). No power-on, alignment, calibration, or handling instructions are stated.

## 11. Safety

No installation-safety claim is made. Handling precautions and controlled-condition provisions are TBD. No hazardous instructions are stated.

## 12. Performance

Sensor capabilities, tolerances, and environmental ratings are TBD per subsystem input and ICD. No allocation value is stated.

## 13. Verification & Validation

Verified by inspection (sequence completeness, mounting and interface coverage, alignment and calibration hooks, as-built recording). Later validated by integration testing (Vol 22/23.2 hooks TBD). Methods TBD in detail.

## 14. Risks

- Undefined aperture provisions forcing rework; mitigation: mounting and aperture register stub now, trade-driven updates by change record.
- Late-defined alignment and calibration interfaces delaying verification; mitigation: Vol 09.17 hooks stubbed now.

## 15. Open Issues

Installation sequence TBD; mounting and aperture provisions TBD; connector and data interfaces TBD; alignment and calibration hooks TBD (Vol 09.17).

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on the IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD), sensor subsystem inputs including Vol 09.17 (TBD), the assembly strategy (21.1), and the VVP thread (TBD).

## 18. Traceability

Parents: IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD); sensor installation inputs including Vol 09.17 (TBD); VVP thread (TBD). Children: as-built records and integration V&V (TBD). RTM: REQ-HFPX-KSI-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 21.7) |
