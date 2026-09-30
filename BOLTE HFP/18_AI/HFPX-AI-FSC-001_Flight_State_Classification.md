# Flight-State Classification — Chapter 18.7

**Document ID:** HFPX-AI-FSC-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define requirements for AI-assisted flight-state-classification functions (Volume 18, Chapter 18.7). This revision fixes advisory scope, authority limits and verification intent; classification logic remains TBD.

## 2. Scope

Covers AI flight-state classification outputs, misclassification handling and mode-switch authority prohibition. Applies to the production-aircraft concept. Excludes control-law switching authority and any baselined value.

## 3. Applicable Documents

- HFPX-AI-REQ-001 AI System Requirements (Chapter 18.1)
- HFPX-AI-ARC-001 AI Architecture (Chapter 18.2)
- HFPX-AI-SCT-001 AI Safety Constraints (Chapter 18.10); HFPX-AI-VAV-001 AI Verification & Validation (Chapter 18.12)

## 4. Definitions & Acronyms

- Classification output: AI advisory indicating an inferred flight state (state set and semantics TBD).
- Misclassification handling: defined response to incorrect classification outputs (handling TBD).
- TBD / TBC: unknown data; no value is stated or implied at this revision.

## 5. System Context

Flight-state classification operates inside the AI partition, consuming flight/system data (sources TBD) and emitting advisory classification outputs to pilot/deterministic-system consumers (TBD).

> **IRON POLICY.** AI is monitoring/advisory ONLY; primary safety-critical flight control remains deterministic/bounded/verifiable; AI shall never silently override pilot or safety-system authority (human override preserved).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-IFC-001|Flight-state-classification outputs shall be advisory only (state set and semantics TBD) and shall inform but not determine flight-state decisions.|SYS-002, REQ-HFPX-ARC-002|Test|
|REQ-HFPX-IFC-002|AI flight-state classification shall have no mode-switch authority; control-law set selection and switching shall remain with deterministic logic (definition TBD).|SYS-002, REQ-HFPX-ARC-002|Test|
|REQ-HFPX-IFC-003|Verification of flight-state-classification requirements shall be by a defined method (method per requirement TBD).|SFA tier|Test|
|REQ-HFPX-IFC-004|Handling of misclassified flight states, including annunciation and downstream-use limits, shall follow a defined rule set (rule set TBD).|SFA tier|Test|

No accuracies, thresholds or latencies are stated. No model architecture or algorithm is selected at this revision.

## 7. Architecture

Position within AI architecture per HFPX-AI-ARC-001 (detail TBD): inputs (TBD) → classification functions (TBD) → advisory outputs (TBD) → consumers (TBD). No component selected.

## 8. Detailed Design

Not applicable at this revision. Classification logic, models, features and parameters are TBD; no selection is made.

## 9. Interfaces

Input data interfaces and classification-output consumer interfaces are TBD. ICD capture TBD.

## 10. Operational Concept

Classification advisories support monitoring across applicable flight modes (detail TBD). Deterministic mode logic remains authoritative; no autonomous mode switch is authorised.

## 11. Safety

> **IRON POLICY.** AI is monitoring/advisory ONLY; primary safety-critical flight control remains deterministic/bounded/verifiable; AI shall never silently override pilot or safety-system authority (human override preserved).

Misclassification hazard and authority limits TBD (enforcement in Chapter 18.10). No safety claim is made.

## 12. Performance

Performance characteristics (including any classification accuracies and latencies) are TBD. No value is stated or baselined at this revision.

## 13. Verification & Validation

Verification method per requirement TBD; cases, datasets and regression TBD in HFPX-AI-VAV-001 (Chapter 18.12). No verification is claimed at this revision.

## 14. Risks

- Misclassification misleading pilot or downstream logic; mitigation: misclassification-handling rules plus no-mode-switch rule TBD
- Confusion with authoritative mode logic; mitigation: advisory labelling TBD

## 15. Open Issues

Flight-state set TBD; misclassification-handling rules TBD; deterministic mode-logic boundary TBD; datasets and verification cases TBD.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on HFPX-AI-REQ-001, HFPX-AI-ARC-001, flight-mode definitions, control-law architecture, safety constraints (18.10) and V&V (18.12).

## 18. Traceability

Parents: SYS-002, REQ-HFPX-ARC-002, SFA tier. Children: verification cases (18.12), safety-constraint enforcement (18.10). RTM: REQ-HFPX-IFC-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. CONCEPT, Rev A (draft).

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 18.7) |
