# Intelligent Emergency Detection — Chapter 18.9

**Document ID:** HFPX-AI-IED-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define requirements for AI-assisted emergency-detection functions (Volume 18, Chapter 18.9). This revision fixes advisory scope, trigger-authority rules and verification intent; detection logic remains TBD.

## 2. Scope

Covers AI emergency cues, missed-detection handling and the boundary with deterministic emergency triggers. Applies to the production-aircraft concept. Excludes emergency-trigger authority and any baselined value.

## 3. Applicable Documents

- HFPX-AI-REQ-001 AI System Requirements (Chapter 18.1)
- HFPX-AI-ARC-001 AI Architecture (Chapter 18.2)
- HFPX-AI-SCT-001 AI Safety Constraints (Chapter 18.10); HFPX-AI-VAV-001 AI Verification & Validation (Chapter 18.12)
- Deterministic emergency-trigger definition (TBD reference)

## 4. Definitions & Acronyms

- Emergency cue: AI advisory output suggesting a possible emergency condition (cue set and semantics TBD).
- Trigger authority: authority to declare an emergency or initiate emergency action; stays deterministic (detail TBD).
- TBD / TBC: unknown data; no value is stated or implied at this revision.

## 5. System Context

Intelligent emergency detection operates inside the AI partition, consuming system/sensor data (sources TBD) and emitting advisory cues to pilot/deterministic-system consumers (TBD).

> **IRON POLICY.** AI is monitoring/advisory ONLY; primary safety-critical flight control remains deterministic/bounded/verifiable; AI shall never silently override pilot or safety-system authority (human override preserved).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-IED-001 | Intelligent emergency detection shall produce emergency cues that are advisory only (cue set and semantics TBD) and shall not declare emergencies or initiate emergency action. | SYS-002, REQ-HFPX-ARC-002 | Test |
| REQ-HFPX-IED-002 | Emergency-trigger authority shall remain with deterministic logic (definition TBD); AI cues shall require pilot or deterministic-system disposition. | SYS-002, REQ-HFPX-ARC-002 | Inspection |
| REQ-HFPX-IED-003 | Verification of intelligent emergency-detection requirements shall be by a defined method (method per requirement TBD). | SFA tier | Inspection |
| REQ-HFPX-IED-004 | Handling of missed or incorrect emergency cues, including annunciation limits and downstream-use limits, shall follow a defined rule set (rule set TBD). | SFA tier | Demonstration |

No accuracies, thresholds or latencies are stated. No model architecture or algorithm is selected at this revision.

## 7. Architecture

Position within AI architecture per HFPX-AI-ARC-001 (detail TBD): inputs (TBD) → emergency-detection functions (TBD) → advisory cues (TBD) → deterministic disposition (TBD). No component selected.

## 8. Detailed Design

Not applicable at this revision. Detection logic, models, features and parameters are TBD; no selection is made.

## 9. Interfaces

Input data interfaces and emergency-cue consumer interfaces are TBD. ICD capture TBD.

## 10. Operational Concept

Emergency cues support monitoring across applicable phases (detail TBD). Deterministic triggers remain authoritative; no autonomous emergency action on AI cues is authorised.

## 11. Safety

> **IRON POLICY.** AI is monitoring/advisory ONLY; primary safety-critical flight control remains deterministic/bounded/verifiable; AI shall never silently override pilot or safety-system authority (human override preserved).

False-cue and missed-cue handling plus authority limits TBD (enforcement in Chapter 18.10). No safety claim is made.

## 12. Performance

Performance characteristics (including any detection rates, accuracies and latencies) are TBD. No value is stated or baselined at this revision.

## 13. Verification & Validation

Verification method per requirement TBD; cases, datasets and regression TBD in HFPX-AI-VAV-001 (Chapter 18.12). No verification is claimed at this revision.

## 14. Risks

- False cues causing inappropriate pilot action; mitigation: advisory labelling and disposition rules TBD
- Missed cues creating false confidence; mitigation: missed-detection-handling rules TBD plus deterministic triggers unaffected

## 15. Open Issues

Cue set TBD; deterministic trigger boundary TBD; missed-detection-handling rules TBD; datasets and verification cases TBD.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on HFPX-AI-REQ-001, HFPX-AI-ARC-001, deterministic emergency-trigger definitions, safety constraints (18.10) and V&V (18.12).

## 18. Traceability

Parents: SYS-002, REQ-HFPX-ARC-002, SFA tier. Children: verification cases (18.12), safety-constraint enforcement (18.10). RTM: REQ-HFPX-IED-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. CONCEPT, Rev A (draft).

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 18.9) |
