# Computer Vision — Chapter 18.8

**Document ID:** HFPX-AI-CVS-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define requirements for AI-assisted computer-vision functions (Volume 18, Chapter 18.8). This revision fixes advisory scope, function inventory intent and verification intent; vision logic remains TBD.

## 2. Scope

Covers computer-vision advisory functions and their data hooks. Applies to the production-aircraft concept. Excludes control or safety authority based on vision outputs and any baselined value.

## 3. Applicable Documents

- HFPX-AI-REQ-001 AI System Requirements (Chapter 18.1)
- HFPX-AI-ARC-001 AI Architecture (Chapter 18.2)
- HFPX-AI-SCT-001 AI Safety Constraints (Chapter 18.10); HFPX-AI-VAV-001 AI Verification & Validation (Chapter 18.12)

## 4. Definitions & Acronyms

- Vision function: AI function consuming image or vision-sensor data to produce advisories (inventory TBD).
- TBD / TBC: unknown data; no value is stated or implied at this revision.

## 5. System Context

Computer vision operates inside the AI partition, consuming vision-sensor data (sources TBD) and emitting advisory outputs to pilot/system consumers (TBD).

> **IRON POLICY.** AI is monitoring/advisory ONLY; primary safety-critical flight control remains deterministic/bounded/verifiable; AI shall never silently override pilot or safety-system authority (human override preserved).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-ICV-001|Computer-vision functions shall be limited to a defined inventory (inventory and semantics TBD) and shall produce advisory outputs only.|SYS-002, REQ-HFPX-ARC-002|Analysis|
|REQ-HFPX-ICV-002|Computer-vision outputs shall be advisory only and shall not command control or safety action nor silently override pilot or safety-system authority.|SYS-002, REQ-HFPX-ARC-002|Analysis|
|REQ-HFPX-ICV-003|Verification of computer-vision requirements shall be by a defined method (method per requirement TBD).|SFA tier|Analysis|
|REQ-HFPX-ICV-004|Computer-vision functions shall define their data hooks, including vision sources and consumers (hooks TBD).|SFA tier|Analysis|

No accuracies, thresholds or latencies are stated. No model architecture or algorithm is selected at this revision.

## 7. Architecture

Position within AI architecture per HFPX-AI-ARC-001 (detail TBD): vision sources (TBD) → vision functions (TBD) → advisory outputs (TBD) → consumers (TBD). No component or sensor selected.

## 8. Detailed Design

Not applicable at this revision. Vision models, features and parameters are TBD; no selection is made.

## 9. Interfaces

Vision-source interfaces and advisory-output consumer interfaces are TBD. ICD capture TBD.

## 10. Operational Concept

Vision advisories support applicable phases (detail TBD). Human or deterministic-system disposition is required; no autonomous action on vision outputs is authorised.

## 11. Safety

> **IRON POLICY.** AI is monitoring/advisory ONLY; primary safety-critical flight control remains deterministic/bounded/verifiable; AI shall never silently override pilot or safety-system authority (human override preserved).

Misleading-vision-output handling and authority limits TBD (enforcement in Chapter 18.10). No safety claim is made.

## 12. Performance

Performance characteristics (including any detection accuracies and latencies) are TBD. No value is stated or baselined at this revision.

## 13. Verification & Validation

Verification method per requirement TBD; cases, datasets and regression TBD in HFPX-AI-VAV-001 (Chapter 18.12). No verification is claimed at this revision.

## 14. Risks

- Misleading vision advisories in degraded visual conditions; mitigation: data-hook definition and verification cases TBD
- Scope creep into guidance or control; mitigation: advisory-only rule plus containment TBD

## 15. Open Issues

Vision-function inventory TBD; vision sources TBD; data hooks TBD; datasets and verification cases TBD.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on HFPX-AI-REQ-001, HFPX-AI-ARC-001, sensor/vision-source definitions, safety constraints (18.10) and V&V (18.12).

## 18. Traceability

Parents: SYS-002, REQ-HFPX-ARC-002, SFA tier. Children: verification cases (18.12), data-hook ICDs (TBD). RTM: REQ-HFPX-ICV-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. CONCEPT, Rev A (draft).

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 18.8) |
