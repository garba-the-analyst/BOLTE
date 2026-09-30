# Integration Test Procedures

**Document ID:** HFPX-INT-ITP-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X integration test procedures view (Chapter 21.13): the specification structure for integration-level test procedures, including procedure inventory, pass/fail hooks, and records.

## 2. Scope

Covers integration test procedure structure for the production-aircraft concept, following system integration (21.12). Procedure inventory is TBD; pass/fail provisions are TBD; records provisions are TBD, with hooks to Vol 22/23.2 (TBD). Test execution, operation, servicing, and handling instructions are excluded. Methodology and sequencing only.

## 3. Applicable Documents

- HFPX-ARC-IFR-001 System Interfaces (interface register and ICD rule); HFPX-INT-STR-001 Assembly Strategy (Chapter 21.1); HFPX-INT-SYI-001 System Integration (Chapter 21.12)
- ICD tier (documents TBD)
- Subsystem installation inputs (Vol 03–18, details TBD); Vol 22/23.2 hooks (TBD)
- VVP thread (documents TBD)

## 4. Definitions & Acronyms

- Integration test procedure: defined check confirming an integrated interface or installed system against its specification (inventory TBD).
- Pass/fail provision: defined criterion structure for recording procedure outcomes (details TBD).
- Test record: retained evidence of procedure execution and outcome (format TBD).

## 5. System Context

Integration test procedures verify the as-built configuration produced by Chapters 21.2–21.12 against interface definitions (IFR/ICD tier) and subsystem inputs, feeding the VVP thread and Vol 22/23.2 test provisions.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-KTP-001 | The integration test procedures specification shall define the procedure inventory and its mapping to integrated interfaces (inventory TBD). | IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD); subsystem installation inputs (TBD); VVP thread including Vol 22/23.2 (TBD) | Inspection |
| REQ-HFPX-KTP-002 | The integration test procedures specification shall define pass/fail provision hooks for each procedure (provisions TBD). | IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD); subsystem installation inputs (TBD); VVP thread including Vol 22/23.2 (TBD) | Inspection |
| REQ-HFPX-KTP-003 | The integration test procedures specification shall define test-record provisions for procedure execution and outcomes (records TBD). | IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD); subsystem installation inputs (TBD); VVP thread including Vol 22/23.2 (TBD) | Inspection |
| REQ-HFPX-KTP-004 | The integration test procedures specification shall define hooks to Vol 22/23.2 test provisions for each applicable procedure (hooks TBD). | IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD); subsystem installation inputs (TBD); VVP thread including Vol 22/23.2 (TBD) | Inspection |

## 7. Architecture

Procedure framework: inventory mapped to integrated interfaces (TBD), pass/fail hooks per procedure (TBD), record provisions (TBD), and Vol 22/23.2 hooks (TBD), sequenced after system integration (21.12) with gate reviews (TBD).

## 8. Detailed Design

Not applicable at Tranche 6 draft level. Procedure definitions, criterion values, and record formats are TBD.

## 9. Interfaces

Each procedure points to its integrated interface definition in the IFR/ICD tier (TBD). Test-provision hooks point to Vol 22/23.2 (TBD). Sequencing aligns with the build strategy (21.1) and system integration (21.12).

## 10. Operational Concept

Test-specification methodology and sequencing only: ordered procedure structure under configuration control (flow TBD). No test execution, operation, servicing, or handling instructions are stated.

## 11. Safety

No test-safety claim is made. Handling precautions and controlled-condition provisions are TBD. Fuel handling and propulsion handling outside controlled conditions are excluded from these documents. No hazardous instructions are stated.

## 12. Performance

Test capabilities, tolerances, and environmental ratings are TBD per subsystem input and ICD. No allocation value is stated.

## 13. Verification & Validation

Verified by inspection (inventory completeness, interface mapping, pass/fail hooks, record provisions, Vol 22/23.2 hooks). Test methods TBD in detail in the VVP thread.

## 14. Risks

- Undefined procedure inventory leaving interfaces unverified; mitigation: inventory stub now, trade-driven updates by change record.
- Late-defined pass/fail provisions delaying acceptance; mitigation: pass/fail hooks stubbed now.

## 15. Open Issues

Procedure inventory TBD; interface mapping TBD; pass/fail provisions TBD; test records TBD; Vol 22/23.2 hooks TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on the IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD), as-built configuration from 21.2–21.12 (TBD), Vol 22/23.2 test provisions (TBD), and the VVP thread (TBD).

## 18. Traceability

Parents: IFR/ICD tier (HFPX-ARC-IFR-001; ICDs TBD); subsystem installation inputs (TBD); VVP thread including Vol 22/23.2 (TBD). Children: integration test execution and V&V records (TBD). RTM: REQ-HFPX-KTP-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 21.13) |
