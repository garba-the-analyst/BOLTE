# Development Phases & Gates

**Document ID:** HFPX-PGM-GAT-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define HFP-X development phases and the gated review sequence controlling programme progression. Owns Chapter 00.6.

## 2. Scope

Covers phase definitions, gate sequence, gate-skipping prohibition and phase-entry rules. Detailed entrance and exit criteria are owned by design reviews (00.14). Does not set technical values or schedule dates.

## 3. Applicable Documents

- HFPX-PGM-CHR-001 Programme Charter
- HFPX-PGM-SEM-001 SEMP
- HFPX-PGM-LIF-001 Development Lifecycle (lifecycle context)
- HFPX-PGM-REV-001 Design Reviews (entrance and exit criteria)

## 4. Definitions & Acronyms

- Phase: bounded lifecycle stage with defined purpose and artefacts
- Gate: formal decision point controlling entry to the next phase
- Gates: SRR, PDR, CDR, TRR, FCA, PCA, FRR, PRR, ORR
- TBD / TBC: to be determined / to be confirmed

## 5. System Context

Phases and gates sequence the lifecycle:

```text
PHASE → GATE → NEXT PHASE → GATE → …
  ↑       ↑________ ENTRY / EXIT CRITERIA (Vol 00.14) __↑
  ↑_______________ BASELINE AT EACH GATE _______________↑
```

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-GAT-001 | The programme shall define each development phase, with purpose and expected artefacts recorded as TBD at this revision. | REQ-HFPX-PGM-003 | Inspection |
| REQ-HFPX-GAT-002 | The programme shall sequence formal gates as SRR, PDR, CDR, TRR, FCA, PCA, FRR, PRR, ORR. | REQ-HFPX-PGM-003 | Inspection |
| REQ-HFPX-GAT-003 | The programme shall prohibit gate skipping; progression to human-carrying flight activity shall pass through each applicable gate in sequence. | REQ-HFPX-PGM-003 | Demonstration |
| REQ-HFPX-GAT-004 | The programme shall enforce a phase-entry rule such that a phase is entered only when the preceding gate decision and entry conditions are satisfied. | REQ-HFPX-PGM-003 | Inspection |

## 7. Architecture

Phase and gate architecture TBD in detail. Gate chain SRR through ORR structures progression from requirements review to operational readiness. Phase artefacts and baselines per gate TBD.

## 8. Detailed Design

Phase definitions, gate objectives, entry and exit provisions TBD (criteria detail in 00.14). Gate-skipping prohibition and phase-entry enforcement mechanisms TBD. No schedule values are stated at this revision.

## 9. Interfaces

- To lifecycle (00.5): phases placed in V-model context
- To reviews (00.14): entrance criteria, required documents, exit criteria per gate
- To configuration (00.7): baseline captured at each gate
- To safety and V&V: gate evidence from safety and test activity

## 10. Operational Concept

The programme proceeds phase by phase, holding each gate, recording the gate decision and capturing the baseline before entering the next phase. Gate scheduling and convening arrangements TBD.

## 11. Safety

Gate decisions shall consider safety evidence and safety authority concurrence. Safety gate provisions TBD.

## 12. Performance

Phase and gate performance indicators TBD. No thresholds are baselined at this revision.

## 13. Verification & Validation

This document is verified by inspection against the document template checklist at the applicable gate. Validation is by programme authority approval (approver TBD).

## 14. Risks

- Gates treated as informational rather than decisional; mitigation TBD
- Pressure to skip gates to recover schedule; mitigation TBD
- Entry conditions waived without record; mitigation TBD

## 15. Open Issues

_TBD_

All open issues are recorded in the issue register. No issue is closed by this revision.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on lifecycle definition (00.5), gate criteria (00.14), configuration baselines (00.7) and safety concurrence provisions.

## 18. Traceability

Parent: HFPX-PGM-CHR-001 (REQ-HFPX-PGM-003) and HFPX-PGM-SEM-001 (REQ-HFPX-PGM-013). Children: gate plans, gate decisions, phase-entry records (all TBD). RTM: REQ-HFPX-GAT-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 00.6) |
