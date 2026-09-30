# Human Override — Chapter 18.11

**Document ID:** HFPX-AI-HOV-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define human-override requirements over all HFP-X AI functions (Volume 18, Chapter 18.11). This revision fixes override paths, no-override-failure intent and verification intent; mechanisms and values remain TBD.

## 2. Scope

Covers pilot and safety-system override paths over AI outputs, override-latency definition and override verification. Applies to all AI functions in Chapters 18.3–18.9. Excludes primary-control design and any baselined value.

## 3. Applicable Documents

- HFPX-AI-REQ-001 AI System Requirements (Chapter 18.1)
- HFPX-AI-ARC-001 AI Architecture (Chapter 18.2)
- HFPX-AI-SCT-001 AI Safety Constraints (Chapter 18.10); HFPX-AI-VAV-001 AI Verification & Validation (Chapter 18.12)

## 4. Definitions & Acronyms

- Override path: means by which pilot or safety system negates, ignores or isolates an AI output (paths TBD).
- No-override-failure rule: prohibition on AI behaviour that prevents or delays override (rule TBD).
- TBD / TBC: unknown data; no value is stated or implied at this revision.

## 5. System Context

Override sits outside the AI partition: pilot and safety-system paths can negate or isolate any AI output before it influences decisions or actions.

> **IRON POLICY.** AI is monitoring/advisory ONLY; primary safety-critical flight control remains deterministic/bounded/verifiable; AI shall never silently override pilot or safety-system authority (human override preserved).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-IHO-001 | Defined pilot override paths over all AI outputs shall be provided (paths TBD), allowing the pilot to negate, ignore or isolate any AI advisory. | SYS-002, REQ-HFPX-ARC-002 | Test |
| REQ-HFPX-IHO-002 | Defined safety-system override paths over all AI outputs shall be provided (paths TBD), allowing the safety system to negate or isolate AI advisories independently of the pilot. | SYS-002, REQ-HFPX-ARC-002 | Test |
| REQ-HFPX-IHO-003 | Override latency characteristics shall be defined (values TBD; no value stated at this revision) and verified by test. | SFA tier | Test |
| REQ-HFPX-IHO-004 | AI functions shall be subject to a no-override-failure rule: no AI output or behaviour shall prevent, delay or obscure pilot or safety-system override (rule TBD). | SYS-002, REQ-HFPX-ARC-002 | Test |

No accuracies, thresholds or latencies are stated — override latency is TBD. No model architecture or algorithm is selected at this revision.

## 7. Architecture

Override architecture overlays HFPX-AI-ARC-001 boundaries (detail TBD): pilot path (TBD), safety-system path (TBD), isolation points (TBD). No component selected.

## 8. Detailed Design

Not applicable at this revision. Override mechanisms, controls and indications are TBD; no selection is made.

## 9. Interfaces

Pilot-override and safety-system-override interfaces are TBD. ICD capture TBD.

## 10. Operational Concept

Override is available in all operating conditions and phases (detail TBD). Overridden AI provides no effective advisory; primary control and safety functions continue unaffected.

## 11. Safety

> **IRON POLICY.** AI is monitoring/advisory ONLY; primary safety-critical flight control remains deterministic/bounded/verifiable; AI shall never silently override pilot or safety-system authority (human override preserved).

Override preservation is the primary safety control for Volume 18; enforcement TBD in Chapter 18.10. No safety claim is made.

## 12. Performance

Override performance characteristics (including override latency) are TBD. No value is stated or baselined at this revision.

## 13. Verification & Validation

Override paths and latency verified by test per REQ-HFPX-IHO-001..003 (test cases TBD); no-override-failure rule verification TBD. Cases TBD in HFPX-AI-VAV-001 (Chapter 18.12). No verification is claimed at this revision.

## 14. Risks

- Override path unavailable or ineffective when needed; mitigation: independent pilot + safety-system paths TBD, verified by test
- AI presentation obscuring override need; mitigation: no-override-failure rule TBD

## 15. Open Issues

Pilot override paths TBD; safety-system override paths TBD; override latency values TBD; test cases TBD.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on HFPX-AI-REQ-001, HFPX-AI-ARC-001, pilot-interface and safety-system definitions, safety constraints (18.10) and V&V (18.12).

## 18. Traceability

Parents: SYS-002, REQ-HFPX-ARC-002, SFA tier. Children: override test cases (18.12), interface definitions (TBD). RTM: REQ-HFPX-IHO-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. CONCEPT, Rev A (draft).

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 18.11) |
