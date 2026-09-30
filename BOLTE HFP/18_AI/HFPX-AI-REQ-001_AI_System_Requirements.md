# AI System Requirements — Chapter 18.1

**Document ID:** HFPX-AI-REQ-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the system-level requirements for HFP-X AI/intelligent-systems functions (Volume 18, Chapter 18.1). This revision fixes scope, authorised/prohibited function boundaries and verification intent; all values and selections remain TBD.

## 2. Scope

Covers AI system requirements for monitoring/advisory functions only, including authorised function categories, prohibitions and verification intent. Applies to the production-aircraft concept. Excludes primary flight control, safety-system authority, model selection and any baselined value.

## 3. Applicable Documents

- HFPX-SYS-ARC-001 SAD (SYS-21 AI monitoring allocation; REQ-HFPX-ARC-002 advisory-only rule)
- HFPX-SYS-REQ-001 SyRS (SYS-002 — source parent, TBD detail)
- HFPX-AI-ARC-001 AI Architecture (Chapter 18.2, companion)
- HFPX-AI-SCT-001 AI Safety Constraints (Chapter 18.10); HFPX-AI-HOV-001 Human Override (Chapter 18.11); HFPX-AI-VAV-001 AI Verification & Validation (Chapter 18.12)
- SFA tier documents (parent tier, TBD reference)

## 4. Definitions & Acronyms

- Advisory-only: AI outputs inform pilot or maintenance decisions; AI does not command control or safety action.
- Authorised functions: AI function categories permitted within advisory scope (inventory TBD).
- Prohibited functions: functions AI shall not perform, including primary control (inventory TBD).
- TBD / TBC: unknown data; no value is stated or implied at this revision.
- SFA: safety-related function/application tier (parent tier reference, TBD).

## 5. System Context

AI is a monitoring/advisory layer within SYS-21, separate from the primary flight-control path and the independent safety path.

> **IRON POLICY.** AI is monitoring/advisory ONLY; primary safety-critical flight control remains deterministic/bounded/verifiable; AI shall never silently override pilot or safety-system authority (human override preserved).

Context (starter): sensors/avionics data (sources TBD) → AI functions (inventory TBD) → advisory outputs to pilot/maintenance/analysis consumers (TBD) → human or deterministic-system decision. No AI output commands primary control or safety action.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-IRQ-001 | The AI system shall operate as monitoring/advisory only and shall not perform primary safety-critical flight control, which shall remain deterministic, bounded and verifiable. | SYS-002, REQ-HFPX-ARC-002 | Test |
| REQ-HFPX-IRQ-002 | The authorised AI functions shall be limited to a defined inventory (TBD), covering only: anomaly detection, maintenance prediction, diagnostics, pilot assistance and analysis support. | SYS-002, REQ-HFPX-ARC-002 | Analysis |
| REQ-HFPX-IRQ-003 | The AI system shall be prohibited from performing primary control and other prohibited functions (prohibited-function inventory TBD, including primary flight control). | SYS-002, REQ-HFPX-ARC-002 | Test |
| REQ-HFPX-IRQ-004 | The AI system shall never silently override pilot authority or safety-system authority; human override shall be preserved in all operating conditions. | SYS-002, REQ-HFPX-ARC-002 | Test |
| REQ-HFPX-IRQ-005 | Verification of each AI system requirement shall be by a defined method (verification method per requirement TBD). | SFA tier | Inspection |

No accuracies, thresholds or latencies are stated. No model architecture or algorithm is selected at this revision.

## 7. Architecture

Not allocated in this requirements document. Allocation to the AI architecture (partitioning, interfaces, containment) is TBD in HFPX-AI-ARC-001 (Chapter 18.2). No component selected.

## 8. Detailed Design

Not applicable at this revision. Model architectures, algorithms, parameters and tuning values are TBD; no selection is made.

## 9. Interfaces

AI data sources, consumers and interface definitions are TBD. Interface capture via ICD discipline (companion: HFPX-AI-ARC-001 §9). No bus, protocol or signal is selected.

## 10. Operational Concept

AI advisories support pre-flight, in-flight monitoring and post-flight analysis as applicable (detail TBD). All advisories require human or deterministic-system disposition; no autonomous operational action is authorised.

## 11. Safety

> **IRON POLICY.** AI is monitoring/advisory ONLY; primary safety-critical flight control remains deterministic/bounded/verifiable; AI shall never silently override pilot or safety-system authority (human override preserved).

Safety intent at this revision: advisory confinement, authority limits and override preservation (detail and enforcement ownership TBD in HFPX-AI-SCT-001 and HFPX-AI-HOV-001). No safety claim is made.

## 12. Performance

Performance characteristics (including any accuracies, thresholds and latencies) are TBD. No value is stated or baselined at this revision.

## 13. Verification & Validation

Verification method per requirement is TBD (see REQ-HFPX-IRQ-005). Approach, cases, datasets and regression discipline are TBD in HFPX-AI-VAV-001 (Chapter 18.12). No verification is claimed at this revision.

## 14. Risks

- Advisory-scope creep into control authority; mitigation: prohibited-function inventory and containment TBD (Chapters 18.2, 18.10)
- Requirements without data/verification basis → paper requirements; mitigation: explicit CONCEPT status, TBD verification cases (Chapter 18.12)

## 15. Open Issues

Authorised-function inventory TBD; prohibited-function inventory TBD; partition/containment TBD (Chapter 18.2); safety-constraint enforcement TBD (Chapter 18.10); override paths TBD (Chapter 18.11); verification cases and datasets TBD (Chapter 18.12).

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SyRS/SYS-002 stability, SAD REQ-HFPX-ARC-002, SFA tier definitions, AI architecture (18.2), safety constraints (18.10), human override (18.11) and V&V framework (18.12).

## 18. Traceability

Parents: SYS-002, REQ-HFPX-ARC-002, SFA tier. Children: AI architecture and function documents (Chapters 18.2–18.9), safety constraints (18.10), human override (18.11), V&V (18.12). RTM: REQ-HFPX-IRQ-001..005 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. CONCEPT, Rev A (draft).

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 18.1) |
