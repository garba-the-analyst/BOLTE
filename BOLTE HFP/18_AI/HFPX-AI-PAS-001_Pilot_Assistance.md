# Pilot Assistance — Chapter 18.6

**Document ID:** HFPX-AI-PAS-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define requirements for AI-assisted pilot-assistance functions (Volume 18, Chapter 18.6). This revision fixes advisory scope, pilot-authority rules and verification intent; assistance logic remains TBD.

## 2. Scope

Covers AI pilot-assistance advisories and pilot accept/reject authority. Applies to the production-aircraft concept. Excludes primary control authority, workload-design decisions and any baselined value.

## 3. Applicable Documents

- HFPX-AI-REQ-001 AI System Requirements (Chapter 18.1)
- HFPX-AI-ARC-001 AI Architecture (Chapter 18.2)
- HFPX-AI-VAV-001 AI Verification & Validation (Chapter 18.12)
- Workload hooks (Vol 30.7 TBD reference)

## 4. Definitions & Acronyms

- Assistance function: AI advisory supporting pilot decision or awareness (inventory TBD).
- Accept/reject authority: pilot authority to accept or reject any AI assistance output (mechanism TBD).
- TBD / TBC: unknown data; no value is stated or implied at this revision.

## 5. System Context

Pilot assistance operates inside the AI partition, presenting advisories via pilot-interface paths (TBD) without commanding control or safety action.

> **IRON POLICY.** AI is monitoring/advisory ONLY; primary safety-critical flight control remains deterministic/bounded/verifiable; AI shall never silently override pilot or safety-system authority (human override preserved).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-IPA-001 | Pilot-assistance functions shall be advisory only (assistance-function inventory and semantics TBD) and shall not command control or safety action. | SYS-002, REQ-HFPX-ARC-002 | Test |
| REQ-HFPX-IPA-002 | The pilot shall retain authority to accept or reject any pilot-assistance output (accept/reject mechanism TBD); no assistance output shall execute without pilot disposition. | SYS-002, REQ-HFPX-ARC-002 | Inspection |
| REQ-HFPX-IPA-003 | Pilot-assistance functions shall define their workload hooks (hooks TBD, Vol 30.7 reference) without altering pilot-authority rules. | SFA tier | Inspection |
| REQ-HFPX-IPA-004 | Verification of pilot-assistance requirements shall be by a defined method (method per requirement TBD). | SFA tier | Inspection |

No accuracies, thresholds or latencies are stated. No model architecture or algorithm is selected at this revision.

## 7. Architecture

Position within AI architecture per HFPX-AI-ARC-001 (detail TBD): inputs (TBD) → assistance functions (TBD) → pilot-interface presentation (TBD) → pilot disposition (TBD). No component selected.

## 8. Detailed Design

Not applicable at this revision. Assistance logic, models and presentation details are TBD; no selection is made.

## 9. Interfaces

Input interfaces and pilot-interface presentation paths are TBD. ICD capture TBD.

## 10. Operational Concept

Assistance advisories support applicable phases (detail TBD). Pilot accept/reject governs every advisory; silent execution is prohibited.

## 11. Safety

> **IRON POLICY.** AI is monitoring/advisory ONLY; primary safety-critical flight control remains deterministic/bounded/verifiable; AI shall never silently override pilot or safety-system authority (human override preserved).

Distraction, over-reliance and authority-bypass handling TBD (enforcement in Chapters 18.10–18.11). No safety claim is made.

## 12. Performance

Performance characteristics (including any latencies and presentation timing) are TBD. No value is stated or baselined at this revision.

## 13. Verification & Validation

Verification method per requirement TBD; cases, datasets and human-in-the-loop aspects TBD in HFPX-AI-VAV-001 (Chapter 18.12). No verification is claimed at this revision.

## 14. Risks

- Pilot over-reliance on advisories; mitigation: accept/reject authority plus presentation rules TBD
- Workload interference; mitigation: Vol 30.7 hooks TBD

## 15. Open Issues

Assistance-function inventory TBD; accept/reject mechanism TBD; Vol 30.7 workload hooks TBD; verification cases TBD.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on HFPX-AI-REQ-001, HFPX-AI-ARC-001, pilot-interface definitions, Vol 30.7 workload work, safety constraints (18.10), override (18.11) and V&V (18.12).

## 18. Traceability

Parents: SYS-002, REQ-HFPX-ARC-002, SFA tier. Children: verification cases (18.12), interface definitions (TBD). RTM: REQ-HFPX-IPA-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. CONCEPT, Rev A (draft).

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 18.6) |
