# Development Lifecycle

**Document ID:** HFPX-PGM-LIF-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X development lifecycle: V-model phases, parallel demonstrator lifecycle, tailoring rules and phase-exit rules. Owns Chapter 00.5.

## 2. Scope

Covers the end-to-end lifecycle from stakeholder needs through operation and sustainment, including the relationship between the production path and the demonstrator path. Does not set technical values or schedule dates.

## 3. Applicable Documents

- HFPX-PGM-CHR-001 Programme Charter
- HFPX-PGM-SEM-001 SEMP
- HFPX-PGM-GAT-001 Development Phases and Gates (phase and gate definitions)
- HFPX-PGM-REV-001 Design Reviews (gate criteria)

## 4. Definitions & Acronyms

- V-model: needs-to-evidence lifecycle with matching specification and verification levels
- MVP: minimum viable::* unmanned demonstrator path, kept separate from production baselines
- Tailoring: controlled adaptation of lifecycle application to scope
- TBD / TBC: to be determined / to be confirmed

## 5. System Context

Lifecycle binds needs, design, build, verification and gates:

```text
STAKEHOLDER NEEDS → REQUIREMENTS → ARCHITECTURE → DESIGN
    → BUILD → INTEGRATE → VERIFY → VALIDATE → OPERATE
    ↑_______________ GATES AND TRACEABILITY _______________↑
    MVP PARALLEL PATH (separate baselines, same discipline)
```

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-GLF-001 | The programme shall implement a V-model lifecycle covering needs, requirements, architecture, design, implementation, integration, verification, validation, certification, production, operation and sustainment. | REQ-HFPX-PGM-003 | Inspection |
| REQ-HFPX-GLF-002 | The programme shall maintain a parallel demonstrator lifecycle that follows the same V-model discipline while keeping demonstrator baselines separate from production baselines. | REQ-HFPX-PGM-005 | Inspection |
| REQ-HFPX-GLF-003 | The programme shall define a lifecycle-tailoring rule governing how lifecycle application may be adapted without weakening gates, traceability or safety independence. | REQ-HFPX-PGM-004 | Inspection |
| REQ-HFPX-GLF-004 | The programme shall enforce a phase-exit rule such that a phase is exited only when its exit conditions and gate actions are satisfied. | REQ-HFPX-PGM-003 | Inspection |

## 7. Architecture

Lifecycle architecture TBD in detail. Production path and demonstrator path run in parallel under common governance, with separate baselines and evidence chains. Phase structure and tailoring authority TBD.

## 8. Detailed Design

V-model phase descriptions, demonstrator-path provisions, tailoring procedure and phase-exit conditions TBD. Tailoring shall not permit gate skipping. No schedule values are stated at this revision.

## 9. Interfaces

- To phases and gates (00.6): phase definitions and gate sequence
- To SEMP (00.4): SE processes applied at each lifecycle stage
- To V&V: verification alignment to lifecycle levels
- To safety: safety analyses aligned to lifecycle stages
- To demonstrator path: separation and promotion rules for evidence reuse

## 10. Operational Concept

The programme advances through lifecycle phases under gate control, applying tailoring only through the defined rule and recording phase exit at gates. Lifecycle reviews and reporting cadence TBD.

## 11. Safety

Safety analyses and safety evidence mature with the lifecycle and gate independently of schedule pressure. Lifecycle tailoring shall not reduce safety activity.

## 12. Performance

Lifecycle performance indicators TBD. No thresholds are baselined at this revision.

## 13. Verification & Validation

This document is verified by inspection against the document template checklist at the applicable gate. Validation is by programme authority approval (approver TBD).

## 14. Risks

- Lifecycle tailoring applied informally, weakening verification; mitigation TBD
- Demonstrator and production baselines confused; mitigation TBD
- Phase exit granted without closure of exit conditions; mitigation TBD

## 15. Open Issues

_TBD_

All open issues are recorded in the issue register. No issue is closed by this revision.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on Charter gated-flight policy, SEMP lifecycle definition, phase and gate definitions (00.6) and gate criteria (00.14).

## 18. Traceability

Parent: HFPX-PGM-CHR-001 (REQ-HFPX-PGM-003/004/005). Children: phase procedures, tailoring records, phase-exit records (all TBD). RTM: REQ-HFPX-GLF-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 00.5) |
