# Predictive Maintenance — Chapter 18.4

**Document ID:** HFPX-AI-PDM-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define requirements for AI-assisted predictive-maintenance functions (Volume 18, Chapter 18.4). This revision fixes advisory scope, authority limits and verification intent; prediction logic and values remain TBD.

## 2. Scope

Covers predictions and maintenance advisories produced by AI for maintenance planning. Applies to the production-aircraft concept. Excludes maintenance-action authority, which stays human, and any baselined value.

## 3. Applicable Documents

- HFPX-AI-REQ-001 AI System Requirements (Chapter 18.1)
- HFPX-AI-ARC-001 AI Architecture (Chapter 18.2)
- HFPX-AI-VAV-001 AI Verification & Validation (Chapter 18.12)
- Maintenance data hooks (Vol 27.14 TBD reference)

## 4. Definitions & Acronyms

- Prediction: AI advisory output concerning future maintenance need (semantics TBD).
- Maintenance-action authority: authority to order or perform maintenance action; stays human (detail TBD).
- TBD / TBC: unknown data; no value is stated or implied at this revision.

## 5. System Context

Predictive maintenance operates inside the AI partition, consuming health/usage data via Vol 27.14 hooks (TBD) and emitting advisories to maintenance consumers (TBD).

> **IRON POLICY.** AI is monitoring/advisory ONLY; primary safety-critical flight control remains deterministic/bounded/verifiable; AI shall never silently override pilot or safety-system authority (human override preserved).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-IPM-001 | Predictive-maintenance predictions shall be advisory only (prediction inventory and semantics TBD) and shall not direct maintenance action by themselves. | SYS-002, REQ-HFPX-ARC-002 | Analysis |
| REQ-HFPX-IPM-002 | Maintenance-action authority shall remain with human roles (roles and disposition workflow TBD); AI shall not authorise or execute maintenance actions. | SYS-002, REQ-HFPX-ARC-002 | Test |
| REQ-HFPX-IPM-003 | Predictive-maintenance functions shall define their data hooks to maintenance data sources (hooks TBD, Vol 27.14 reference). | SFA tier | Analysis |
| REQ-HFPX-IPM-004 | Verification of predictive-maintenance requirements shall be by a defined method (method per requirement TBD). | SFA tier | Analysis |

No accuracies, thresholds or latencies are stated. No model architecture or algorithm is selected at this revision.

## 7. Architecture

Position within AI architecture per HFPX-AI-ARC-001 (detail TBD): data hooks (TBD) → prediction functions (TBD) → maintenance advisories (TBD) → human disposition (TBD). No component selected.

## 8. Detailed Design

Not applicable at this revision. Prediction logic, models, features and parameters are TBD; no selection is made.

## 9. Interfaces

Data hooks to Vol 27.14 sources and interfaces to maintenance consumers are TBD. ICD capture TBD.

## 10. Operational Concept

Predictions support maintenance planning across applicable phases (detail TBD). Human disposition of every advisory is required; no autonomous maintenance action is authorised.

## 11. Safety

> **IRON POLICY.** AI is monitoring/advisory ONLY; primary safety-critical flight control remains deterministic/bounded/verifiable; AI shall never silently override pilot or safety-system authority (human override preserved).

Misleading-prediction handling and authority limits TBD (enforcement in Chapter 18.10). No safety claim is made.

## 12. Performance

Performance characteristics (including any prediction horizons, accuracies and latencies) are TBD. No value is stated or baselined at this revision.

## 13. Verification & Validation

Verification method per requirement TBD; cases, datasets and regression TBD in HFPX-AI-VAV-001 (Chapter 18.12). No verification is claimed at this revision.

## 14. Risks

- Misleading predictions driving unnecessary or missed maintenance; mitigation: human-authority rule plus verification cases TBD
- Data-hook gaps or poor data quality; mitigation: Vol 27.14 hook definition TBD

## 15. Open Issues

Prediction inventory TBD; human disposition workflow TBD; Vol 27.14 data hooks TBD; datasets and verification cases TBD.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on HFPX-AI-REQ-001, HFPX-AI-ARC-001, Vol 27.14 maintenance data definition, safety constraints (18.10) and V&V (18.12).

## 18. Traceability

Parents: SYS-002, REQ-HFPX-ARC-002, SFA tier. Children: verification cases (18.12), data-hook ICDs (TBD). RTM: REQ-HFPX-IPM-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. CONCEPT, Rev A (draft).

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 18.4) |
