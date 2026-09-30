# Sensor Anomaly Detection — Chapter 18.5

**Document ID:** HFPX-AI-SAD-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define requirements for AI-assisted sensor-anomaly-detection functions (Volume 18, Chapter 18.5). This revision fixes advisory scope, handover intent and verification intent; detection logic and values remain TBD.

## 2. Scope

Covers AI sensor-anomaly flags and handover to deterministic fault detection. Applies to the production-aircraft concept. Excludes sensor-override authority and any baselined value.

## 3. Applicable Documents

- HFPX-AI-REQ-001 AI System Requirements (Chapter 18.1)
- HFPX-AI-ARC-001 AI Architecture (Chapter 18.2)
- HFPX-AI-VAV-001 AI Verification & Validation (Chapter 18.12)
- Deterministic fault-detection definition (Vol 09.16 TBD reference, handover target)

## 4. Definitions & Acronyms

- Anomaly flag: AI advisory output indicating a suspected sensor anomaly (semantics TBD).
- Handover: passing a suspected anomaly to deterministic fault detection for disposition (definition TBD).
- TBD / TBC: unknown data; no value is stated or implied at this revision.

## 5. System Context

Sensor-anomaly detection operates inside the AI partition, consuming sensor data (sources TBD) and emitting anomaly flags to pilot/deterministic-system consumers (TBD).

> **IRON POLICY.** AI is monitoring/advisory ONLY; primary safety-critical flight control remains deterministic/bounded/verifiable; AI shall never silently override pilot or safety-system authority (human override preserved).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-IAD-001 | Sensor-anomaly detection shall produce anomaly flags only (flag inventory and semantics TBD) and shall not command any sensor, control or reconfiguration action. | SYS-002, REQ-HFPX-ARC-002 | Test |
| REQ-HFPX-IAD-002 | Disposition of sensor anomalies shall hand over to deterministic fault detection (handover definition TBD, Vol 09.16 reference); AI shall have no sensor-override authority. | SYS-002, REQ-HFPX-ARC-002 | Inspection |
| REQ-HFPX-IAD-003 | Verification of sensor-anomaly-detection requirements shall be by a defined method (method per requirement TBD). | SFA tier | Inspection |
| REQ-HFPX-IAD-004 | The AI function shall have no authority to override, substitute or mask sensor outputs consumed by primary control or safety systems (override prohibition). | SYS-002, REQ-HFPX-ARC-002 | Test |

No accuracies, thresholds or latencies are stated. No model architecture or algorithm is selected at this revision.

## 7. Architecture

Position within AI architecture per HFPX-AI-ARC-001 (detail TBD): sensor inputs (TBD) → anomaly-detection functions (TBD) → anomaly flags (TBD) → deterministic handover (TBD). No component selected.

## 8. Detailed Design

Not applicable at this revision. Detection logic, models, features and parameters are TBD; no selection is made.

## 9. Interfaces

Sensor input interfaces and anomaly-flag consumer interfaces are TBD. ICD capture TBD.

## 10. Operational Concept

Anomaly flags support monitoring across applicable phases (detail TBD). Deterministic-system disposition following handover is required; no autonomous sensor action is authorised.

## 11. Safety

> **IRON POLICY.** AI is monitoring/advisory ONLY; primary safety-critical flight control remains deterministic/bounded/verifiable; AI shall never silently override pilot or safety-system authority (human override preserved).

Misleading-flag handling, handover integrity and override prohibition enforcement TBD (Chapter 18.10). No safety claim is made.

## 12. Performance

Performance characteristics (including any detection rates, accuracies and latencies) are TBD. No value is stated or baselined at this revision.

## 13. Verification & Validation

Verification method per requirement TBD; cases, datasets and regression TBD in HFPX-AI-VAV-001 (Chapter 18.12). No verification is claimed at this revision.

## 14. Risks

- False or missed anomaly flags confusing downstream disposition; mitigation: handover definition and verification cases TBD
- Coupling into sensor paths used by control; mitigation: no-override rule plus containment TBD

## 15. Open Issues

Flag inventory TBD; Vol 09.16 handover definition TBD; datasets and verification cases TBD.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on HFPX-AI-REQ-001, HFPX-AI-ARC-001, sensor definitions, Vol 09.16 deterministic detection, safety constraints (18.10) and V&V (18.12).

## 18. Traceability

Parents: SYS-002, REQ-HFPX-ARC-002, SFA tier. Children: verification cases (18.12), handover ICDs (TBD). RTM: REQ-HFPX-IAD-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. CONCEPT, Rev A (draft).

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 18.5) |
