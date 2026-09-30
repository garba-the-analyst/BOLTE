# Fuel System Installation

**Document ID:** HFPX-INT-FSI-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X fuel system installation view (Chapter 21.4): the installation-specification structure for the fuel system, including sequencing, routing and protection hooks, and installation verification.

## 2. Scope

Covers fuel system installation sequencing and specification structure for the production-aircraft concept. Routing and protection provisions are TBD; leak-check hooks are TBD (Vol 05.13/05.16). Sequencing only; no fuelling, draining, pressurisation, servicing, or handling instructions are stated. Fuel handling outside controlled conditions is excluded. All connection details, sealing specifications, and verification methods TBD.

## 3. Applicable Documents

- HFPX-ARC-IFR-001 System Interfaces (interface register and ICD rule); HFPX-INT-STR-001 Assembly Strategy (Chapter 21.1)
- ICD tier (documents TBD)
- Fuel subsystem inputs (Vol 05, including 05.13/05.16, details TBD)
- VVP thread (documents TBD)

## 4. Definitions & Acronyms

- Fuel system installation: placement, routing, and connection of the fuel system into the airframe (scope TBD).
- Routing and protection: pathing and safeguarding provisions for fuel lines and components (details TBD).
- Leak-check hook: defined verification interface to fuel-system test provisions (details TBD, Vol 05.13/05.16).

## 5. System Context

Fuel system installation integrates fuel storage, distribution, and metering interfaces with structure, propulsion, and ground-service interfaces, within the build sequence (21.1), prior to system integration (21.12) and integration testing (21.13).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-KFI-001 | The fuel system installation specification shall define the installation sequence and stage gates (sequence and criteria TBD). | IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD); fuel inputs (TBD); VVP thread (TBD) | Inspection |
| REQ-HFPX-KFI-002 | The fuel system installation specification shall define routing and protection specification hooks for fuel lines and components (details TBD). | IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD); fuel inputs (TBD); VVP thread (TBD) | Inspection |
| REQ-HFPX-KFI-003 | The fuel system installation specification shall define connection and sealing specification hooks for each fuel interface (specifications TBD). | IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD); fuel inputs (TBD); VVP thread (TBD) | Inspection |
| REQ-HFPX-KFI-004 | The fuel system installation specification shall define installation verification hooks, including leak-check provisions (details TBD, Vol 05.13/05.16 hooks). | IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD); fuel inputs (TBD); VVP thread (TBD) | Inspection |

## 7. Architecture

Installation framework: staged fuel system installation (stages TBD), routing and protection hooks (TBD), connection and sealing hooks per fuel interface (TBD), and leak-check verification hooks (TBD, Vol 05.13/05.16), with gate reviews and as-built recording (TBD).

## 8. Detailed Design

Not applicable at Tranche 6 draft level. Routing definitions, protection definitions, connection definitions, and sealing specifications are TBD in subsystem inputs and ICDs.

## 9. Interfaces

Each fuel installation interface points to its interface definition in the IFR/ICD tier (TBD). Verification hooks point to Vol 05.13/05.16 provisions (TBD). Sequencing aligns with the build strategy (21.1).

## 10. Operational Concept

Installation methodology and sequencing only: staged routing and connection under configuration control with gate reviews (flow TBD). No fuelling, servicing, or handling instructions are stated.

## 11. Safety

No installation-safety claim is made. Handling precautions and controlled-condition provisions are TBD. Fuel handling outside controlled conditions is excluded from these documents. No hazardous instructions are stated.

## 12. Performance

Fuel system capacities, tolerances, and environmental ratings are TBD per subsystem input and ICD. No allocation value is stated.

## 13. Verification & Validation

Verified by inspection (sequence completeness, routing and connection coverage, leak-check hooks, as-built recording). Later validated by integration testing (Vol 22/23.2 hooks TBD). Methods TBD in detail.

## 14. Risks

- Undefined routing and protection provisions forcing rework; mitigation: routing-hook stub now, trade-driven updates by change record.
- Late-defined leak-check interfaces delaying verification; mitigation: Vol 05.13/05.16 hooks stubbed now.

## 15. Open Issues

Installation sequence TBD; routing and protection TBD; connection and sealing specifications TBD; leak-check hooks TBD (Vol 05.13/05.16).

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on the IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD), fuel subsystem inputs including Vol 05.13/05.16 (TBD), the assembly strategy (21.1), and the VVP thread (TBD).

## 18. Traceability

Parents: IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD); fuel installation inputs (TBD); VVP thread (TBD). Children: as-built records and integration V&V (TBD). RTM: REQ-HFPX-KFI-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 21.4) |
