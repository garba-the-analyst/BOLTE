# System Integration

**Document ID:** HFPX-INT-SYI-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X system integration view (Chapter 21.12): the specification structure for integrating installed systems, including integration order, interface verification, and non-conformance flow.

## 2. Scope

Covers system-level integration sequencing and specification structure for the production-aircraft concept, following airframe assembly and system installation (21.2–21.11). Integration order is TBD; interface verification is TBD; non-conformance flow is TBD (Vol 28.6 hooks). Integration test procedures are covered in 21.13. Methodology and sequencing only.

## 3. Applicable Documents

- HFPX-ARC-IFR-001 System Interfaces (interface register and ICD rule); HFPX-INT-STR-001 Assembly Strategy (Chapter 21.1)
- ICD tier (documents TBD)
- Subsystem installation inputs (Vol 03–18, details TBD); Vol 28.6 non-conformance hooks (TBD)
- VVP thread (documents TBD)

## 4. Definitions & Acronyms

- System integration: ordered mating and verification of installed systems against their interface definitions (scope TBD).
- Integration order: sequence in which installed systems are mated and checked (order TBD).
- Non-conformance flow: defined routing for recording and dispositioning integration discrepancies (details TBD, Vol 28.6 hooks).

## 5. System Context

System integration consolidates the installed systems from Chapters 21.2–21.11 into a verified as-built configuration, feeding integration test procedures (21.13) and the VVP thread.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-KSY-001 | The system integration specification shall define the integration order and stage gates (order and criteria TBD). | IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD); subsystem installation inputs (TBD); VVP thread (TBD) | Inspection |
| REQ-HFPX-KSY-002 | The system integration specification shall define interface-verification provisions for each integrated interface (provisions TBD). | IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD); subsystem installation inputs (TBD); VVP thread (TBD) | Inspection |
| REQ-HFPX-KSY-003 | The system integration specification shall define non-conformance flow hooks for integration discrepancies (details TBD, Vol 28.6 hooks). | IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD); subsystem installation inputs (TBD); VVP thread (TBD) | Inspection |
| REQ-HFPX-KSY-004 | The system integration specification shall define integration records, including as-built configuration capture (records TBD). | IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD); subsystem installation inputs (TBD); VVP thread (TBD) | Inspection |

## 7. Architecture

Integration framework: ordered integration stages (TBD), interface-verification provisions per mated interface (TBD), non-conformance hooks (TBD, Vol 28.6), and gate reviews with integration records (TBD), feeding test procedures (21.13).

## 8. Detailed Design

Not applicable at Tranche 6 draft level. Integration-order definitions, verification provisions, and record formats are TBD.

## 9. Interfaces

Each integrated interface points to its interface definition in the IFR/ICD tier (TBD). Non-conformance hooks point to Vol 28.6 provisions (TBD). Sequencing aligns with the build strategy (21.1).

## 10. Operational Concept

Integration methodology and sequencing only: ordered mating and checking under configuration control with gate reviews (flow TBD). No operation, servicing, or handling instructions are stated.

## 11. Safety

No integration-safety claim is made. Handling precautions and controlled-condition provisions are TBD. Fuel handling and propulsion handling outside controlled conditions are excluded from these documents. No hazardous instructions are stated.

## 12. Performance

Integration capacities, tolerances, and environmental ratings are TBD per subsystem input and ICD. No allocation value is stated.

## 13. Verification & Validation

Verified by inspection (integration-order completeness, interface-verification coverage, non-conformance hooks, integration records). Later validated by integration testing (Vol 22/23.2 hooks TBD). Methods TBD in detail.

## 14. Risks

- Undefined integration order forcing rework; mitigation: order stub now, trade-driven updates by change record.
- Uncontrolled discrepancies escaping into test; mitigation: non-conformance hooks stubbed now (Vol 28.6).

## 15. Open Issues

Integration order TBD; interface verification TBD; non-conformance flow TBD (Vol 28.6 hooks TBD); integration records TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on the IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD), subsystem installation inputs and as-built records from 21.2–21.11 (TBD), Vol 28.6 non-conformance provisions (TBD), and the VVP thread (TBD).

## 18. Traceability

Parents: IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD); subsystem installation inputs (TBD); VVP thread (TBD). Children: integration test procedures (21.13) and integration V&V (TBD). RTM: REQ-HFPX-KSY-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 21.12) |
