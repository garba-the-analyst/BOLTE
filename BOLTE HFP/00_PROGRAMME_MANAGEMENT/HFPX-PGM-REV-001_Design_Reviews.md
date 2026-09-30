# Design Reviews

**Document ID:** HFPX-PGM-REV-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define design reviews and gate control for HFP-X: per-gate entrance and exit structure, required documents, action closure and waiver provisions. Owns Chapter 00.14.

## 2. Scope

Covers gates SRR, PDR, CDR, TRR, FCA, PCA, FRR, PRR and ORR. Covers entrance criteria, objectives, decision criteria, actions, exit criteria and baselines per gate. Does not set technical values.

## 3. Applicable Documents

- HFPX-PGM-CHR-001 Programme Charter
- HFPX-PGM-SEM-001 SEMP
- HFPX-PGM-GAT-001 Development Phases and Gates (gate sequence)
- HFPX-PGM-LIF-001 Development Lifecycle (lifecycle context)
- HFPX-PGM-CFG-001 Configuration Management (gate baselines)

## 4. Definitions & Acronyms

- Entrance criteria: conditions required before a review may convene
- Exit criteria: conditions required before a gate may be passed
- Gate action: recorded task arising from a review requiring closure
- Gate waiver: purported exemption from gate provisions
- TBD / TBC: to be determined / to be confirmed

## 5. System Context

Reviews gate lifecycle progression:

```text
ENTRY CONDITIONS → REVIEW → DECISION → ACTIONS → EXIT → BASELINE
     ↑________________ REQUIRED DOCUMENTS ________________↑
```

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-GRV-001 | The programme shall define entrance and exit criteria structure for each gate among SRR, PDR, CDR, TRR, FCA, PCA, FRR, PRR and ORR, with criteria values recorded as TBD at this revision. | REQ-HFPX-PGM-013 | Inspection |
| REQ-HFPX-GRV-002 | The programme shall define required documents for each gate, with document lists recorded as TBD at this revision. | REQ-HFPX-PGM-013 | Inspection |
| REQ-HFPX-GRV-003 | The programme shall record gate objectives, decision criteria and resulting actions for each gate held. | REQ-HFPX-PGM-003 | Inspection |
| REQ-HFPX-GRV-004 | The programme shall close gate actions through defined action-closure provisions before the dependent phase proceeds, with provisions recorded as TBD at this revision. | REQ-HFPX-PGM-003 | Demonstration |
| REQ-HFPX-GRV-005 | The programme shall prohibit gate waivers; any proposal to bypass a gate or its criteria shall be treated as a change requiring full assessment and authority decision. | REQ-HFPX-PGM-003 | Demonstration |

## 7. Architecture

Review architecture TBD. Elements per gate: entrance criteria, required documents, objectives, decision criteria, actions, exit criteria, baseline. Convening authority and participation TBD.

## 8. Detailed Design

Per-gate provisions TBD, structured uniformly:

- SRR: entrance criteria TBD; required documents TBD; exit criteria TBD
- PDR: entrance criteria TBD; required documents TBD; exit criteria TBD
- CDR: entrance criteria TBD; required documents TBD; exit criteria TBD
- TRR: entrance criteria TBD; required documents TBD; exit criteria TBD
- FCA: entrance criteria TBD; required documents TBD; exit criteria TBD
- PCA: entrance criteria TBD; required documents TBD; exit criteria TBD
- FRR: entrance criteria TBD; required documents TBD; exit criteria TBD
- PRR: entrance criteria TBD; required documents TBD; exit criteria TBD
- ORR: entrance criteria TBD; required documents TBD; exit criteria TBD

Action-closure tracking and waiver-prohibition enforcement TBD. No criterion values are stated at this revision.

## 9. Interfaces

- To phases and gates (00.6): gate sequence and phase-entry linkage
- To configuration (00.7): baseline captured at each gate
- To requirements (00.9): RTM coverage presented at each gate
- To risk (00.12): risk posture presented at each gate
- To safety and V&V: safety and test evidence presented at applicable gates

## 10. Operational Concept

Each review convenes against entrance criteria with required documents available, records objectives, decisions and actions, and exits only when exit criteria and action provisions are satisfied. Scheduling and chairing TBD.

## 11. Safety

Safety evidence and safety authority concurrence form part of applicable gate decisions. Safety gate provisions TBD.

## 12. Performance

Review performance indicators TBD. No thresholds are baselined at this revision.

## 13. Verification & Validation

This document is verified by inspection against the document template checklist at the applicable gate. Validation is by programme authority approval (approver TBD).

## 14. Risks

- Reviews convened without entrance conditions met; mitigation TBD
- Actions left open while phases proceed; mitigation TBD
- Waiver pressure under schedule stress; mitigation TBD

## 15. Open Issues

_TBD_

All open issues are recorded in the issue register. No issue is closed by this revision.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on gate sequence (00.6), lifecycle definition (00.5), baseline provisions (00.7), RTM discipline (00.9) and safety concurrence provisions.

## 18. Traceability

Parent: HFPX-PGM-SEM-001 (REQ-HFPX-PGM-013) and HFPX-PGM-CHR-001 (REQ-HFPX-PGM-003). Children: per-gate review plans, gate decisions, action-closure records (all TBD). RTM: REQ-HFPX-GRV-001..005 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 00.14) |
