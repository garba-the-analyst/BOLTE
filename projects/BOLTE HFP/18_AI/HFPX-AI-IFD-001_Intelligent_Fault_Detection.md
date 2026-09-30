# Intelligent Fault Detection — Chapter 18.3

**Document ID:** HFPX-AI-IFD-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define requirements for intelligent fault-detection functions (Volume 18, Chapter 18.3). This revision fixes advisory scope, authority limits and verification intent; detection logic and values remain TBD.

## 2. Scope

Covers AI-assisted fault detection producing advisory flags only. Applies to the production-aircraft concept. Excludes automatic reconfiguration, primary fault-detection authority and any baselined value.

## 3. Applicable Documents

- HFPX-AI-REQ-001 AI System Requirements (Chapter 18.1)
- HFPX-AI-ARC-001 AI Architecture (Chapter 18.2)
- HFPX-AI-SCT-001 AI Safety Constraints (Chapter 18.10); HFPX-AI-HOV-001 Human Override (Chapter 18.11); HFPX-AI-VAV-001 AI Verification & Validation (Chapter 18.12)
- Deterministic fault-detection definition (Vol 09.16 TBD reference, handover target)

## 4. Definitions & Acronyms

- Advisory flag: AI fault-detection output informing pilot or deterministic systems; no command authority.
- False-alarm policy: rules governing handling of incorrect advisory flags (policy TBD).
- TBD / TBC: unknown data; no value is stated or implied at this revision.

## 5. System Context

Intelligent fault detection operates inside the AI partition, consuming system/health data (sources TBD) and emitting advisory flags to pilot/maintenance/deterministic fault-detection consumers (TBD).

> **IRON POLICY.** AI is monitoring/advisory ONLY; primary safety-critical flight control remains deterministic/bounded/verifiable; AI shall never silently override pilot or safety-system authority (human override preserved).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-IFD-001 | Intelligent fault detection shall produce advisory flags only (flag inventory and semantics TBD) and shall not command any control or reconfiguration action. | SYS-002, REQ-HFPX-ARC-002 | Test |
| REQ-HFPX-IFD-002 | Intelligent fault detection shall have no automatic reconfiguration authority; disposition of advisory flags shall rest with the pilot or deterministic systems (handover definition TBD). | SYS-002, REQ-HFPX-ARC-002 | Inspection |
| REQ-HFPX-IFD-003 | Verification of intelligent fault-detection requirements shall be by a defined method (method per requirement TBD). | SFA tier | Inspection |
| REQ-HFPX-IFD-004 | Handling of false advisory flags, including annunciation and suppression rules, shall follow a defined false-alarm policy (policy TBD). | SFA tier | Demonstration |

No accuracies, thresholds or latencies are stated. No model architecture or algorithm is selected at this revision.

## 7. Architecture

Position within AI architecture per HFPX-AI-ARC-001 (detail TBD): inputs (TBD) → intelligent fault-detection functions (TBD) → advisory flags (TBD) → consumers (TBD). No component selected.

## 8. Detailed Design

Not applicable at this revision. Detection logic, models, features and parameters are TBD; no selection is made.

## 9. Interfaces

Input data sources and advisory-flag consumer interfaces are TBD. ICD capture TBD.

## 10. Operational Concept

Advisory flags support monitoring across applicable phases (detail TBD). Pilot or deterministic-system disposition is required; no autonomous response is authorised.

## 11. Safety

> **IRON POLICY.** AI is monitoring/advisory ONLY; primary safety-critical flight control remains deterministic/bounded/verifiable; AI shall never silently override pilot or safety-system authority (human override preserved).

Misleading-flag hazard, authority limits and containment are TBD (enforcement in Chapter 18.10). No safety claim is made.

## 12. Performance

Performance characteristics (including any detection rates, accuracies and latencies) are TBD. No value is stated or baselined at this revision.

## 13. Verification & Validation

Verification method per requirement TBD; cases, datasets and regression TBD in HFPX-AI-VAV-001 (Chapter 18.12). No verification is claimed at this revision.

## 14. Risks

- Nuisance advisories eroding trust or masking real faults; mitigation: false-alarm policy TBD
- Confusion with deterministic fault-detection authority; mitigation: handover definition TBD

## 15. Open Issues

Flag inventory TBD; handover to deterministic detection TBD; false-alarm policy TBD; datasets and verification cases TBD.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on HFPX-AI-REQ-001, HFPX-AI-ARC-001, deterministic fault-detection definition, safety constraints (18.10), override (18.11) and V&V (18.12).

## 18. Traceability

Parents: SYS-002, REQ-HFPX-ARC-002, SFA tier. Children: verification cases (18.12), safety-constraint enforcement (18.10). RTM: REQ-HFPX-IFD-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. CONCEPT, Rev A (draft).

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 18.3) |
