# AI Architecture — Chapter 18.2

**Document ID:** HFPX-AI-ARC-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Describe the architecture for HFP-X AI/intelligent-systems functions (Volume 18, Chapter 18.2). This revision fixes the architectural framework — partitioning, data interfaces and containment — with all selections TBD.

## 2. Scope

Covers AI architectural partitioning from the primary path, data interfaces and containment. Applies to the production-aircraft concept. Excludes primary flight-control design, safety-computer design, model selection and any baselined value.

## 3. Applicable Documents

- HFPX-SYS-ARC-001 SAD (REQ-HFPX-ARC-002 advisory-only rule; independent safety path)
- HFPX-AI-REQ-001 AI System Requirements (Chapter 18.1, parent requirements)
- HFPX-AI-SCT-001 AI Safety Constraints (Chapter 18.10); HFPX-AI-HOV-001 Human Override (Chapter 18.11)
- SFA tier documents (parent tier, TBD reference)

## 4. Definitions & Acronyms

- Partition: separation between AI functions and the primary control/safety paths (mechanism TBD).
- Containment: architectural means preventing AI outputs from commanding control or safety action (means TBD).
- TBD / TBC: unknown data; no value is stated or implied at this revision.

## 5. System Context

AI architecture sits in SYS-21 as a monitoring/advisory layer alongside, but partitioned from, the primary flight-control path and the independent safety path.

> **IRON POLICY.** AI is monitoring/advisory ONLY; primary safety-critical flight control remains deterministic/bounded/verifiable; AI shall never silently override pilot or safety-system authority (human override preserved).

Context (starter): data sources (TBD) → AI partition (TBD) → advisory outputs (TBD) → pilot/maintenance consumers (TBD). No path from AI to primary control or safety actuation is authorised.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-IAR-001 | The AI architecture shall partition AI functions from the primary flight-control path by a defined partitioning scheme (scheme TBD), preserving deterministic/bounded/verifiable primary control and advisory-only AI. | SYS-002, REQ-HFPX-ARC-002 | Inspection |
| REQ-HFPX-IAR-002 | The AI architecture shall define all AI data interfaces, including sources, consumers and direction (interface inventory TBD). | SYS-002, REQ-HFPX-ARC-002 | Inspection |
| REQ-HFPX-IAR-003 | The AI architecture shall contain AI outputs so that no AI output commands primary control or safety action and no silent override of pilot or safety-system authority is possible (containment means TBD). | SYS-002, REQ-HFPX-ARC-002 | Test |
| REQ-HFPX-IAR-004 | Verification of each AI architectural requirement shall be by review of the architecture description against its parent requirements (artefacts TBD). | SFA tier | Inspection |

No accuracies, thresholds or latencies are stated. No model architecture or algorithm is selected at this revision.

## 7. Architecture

Framework (starter, all TBD): AI input conditioning (TBD) → AI function set (Chapters 18.3–18.9, TBD) → advisory output management (TBD) → containment boundary (TBD) → consumers (TBD). Partitioning mechanism, redundancy, hosting and resource allocation are TBD. No component selected.

## 8. Detailed Design

Not applicable at this revision. Model architectures, algorithms, parameters and hosting selections are TBD; no selection is made.

## 9. Interfaces

AI data interfaces (sources, consumers, formats, direction, criticality) are TBD. Each interface will be captured under ICD discipline before CDR (companion detail TBD). No bus, protocol or signal is selected.

## 10. Operational Concept

Architecture supports advisory operation across applicable phases (detail TBD). Partitioning and containment hold in all modes; degraded-data behaviour is TBD.

## 11. Safety

> **IRON POLICY.** AI is monitoring/advisory ONLY; primary safety-critical flight control remains deterministic/bounded/verifiable; AI shall never silently override pilot or safety-system authority (human override preserved).

Safety intent: partitioning plus containment plus override preservation (enforcement ownership and means TBD in Chapter 18.10). No safety claim is made.

## 12. Performance

Architectural performance characteristics (including any data rates, latencies and resource budgets) are TBD. No value is stated or baselined at this revision.

## 13. Verification & Validation

Verified by review per REQ-HFPX-IAR-004 (review artefacts and criteria TBD). Later validation hooks to HFPX-AI-VAV-001 (Chapter 18.12). No verification is claimed at this revision.

## 14. Risks

- Partition leakage allowing advisory path to influence control; mitigation: containment definition TBD (Chapter 18.10)
- Interface sprawl across data sources; mitigation: interface inventory and ICD discipline TBD

## 15. Open Issues

Partitioning scheme TBD; interface inventory TBD; containment means TBD; hosting/compute allocation TBD; review artefacts TBD.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on HFPX-AI-REQ-001, SAD partitioning/independence criteria, compute/avionics architectures (Vol 08/16 TBD), safety constraints (18.10) and V&V framework (18.12).

## 18. Traceability

Parents: SYS-002, REQ-HFPX-ARC-002, SFA tier. Children: function architectures (Chapters 18.3–18.9), safety constraints (18.10), override (18.11). RTM: REQ-HFPX-IAR-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. CONCEPT, Rev A (draft).

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 18.2) |
