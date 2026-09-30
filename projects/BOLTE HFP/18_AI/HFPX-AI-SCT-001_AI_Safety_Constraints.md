# AI Safety Constraints — Chapter 18.10

**Document ID:** HFPX-AI-SCT-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define safety constraints governing all HFP-X AI functions (Volume 18, Chapter 18.10). This revision fixes the constraint inventory framework and enforcement/verification intent; constraint values and ownership remain TBD.

## 2. Scope

Covers AI safety constraints for containment, authority limits, monitoring, disengagement and auditability. Applies to all AI functions in Chapters 18.3–18.9. Excludes primary-control and safety-system design and any baselined value.

## 3. Applicable Documents

- HFPX-AI-REQ-001 AI System Requirements (Chapter 18.1)
- HFPX-AI-ARC-001 AI Architecture (Chapter 18.2)
- HFPX-AI-HOV-001 Human Override (Chapter 18.11); HFPX-AI-VAV-001 AI Verification & Validation (Chapter 18.12)
- SFA tier documents (parent tier, TBD reference)

## 4. Definitions & Acronyms

- Containment: prevention of AI outputs commanding control or safety action (means TBD).
- Disengagement: removal or isolation of AI function output from consumers (mechanism TBD).
- Auditability: ability to record and review AI inputs, outputs and dispositions (means TBD).
- TBD / TBC: unknown data; no value is stated or implied at this revision.

## 5. System Context

Safety constraints bound every AI function inside the AI partition, spanning inputs, processing, outputs and consumer disposition.

> **IRON POLICY.** AI is monitoring/advisory ONLY; primary safety-critical flight control remains deterministic/bounded/verifiable; AI shall never silently override pilot or safety-system authority (human override preserved).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-ISC-001|AI functions shall be subject to defined containment constraints preventing any AI output from commanding primary control or safety action (constraint definition TBD).|SYS-002, REQ-HFPX-ARC-002|Inspection|
|REQ-HFPX-ISC-002|AI functions shall be subject to defined authority limits preserving pilot and safety-system authority over all AI outputs (limits TBD).|SYS-002, REQ-HFPX-ARC-002|Inspection|
|REQ-HFPX-ISC-003|AI functions shall be subject to defined monitoring and disengagement constraints governing detection of misbehaviour and removal of AI outputs (definitions TBD).|SFA tier|Inspection|
|REQ-HFPX-ISC-004|AI functions shall be subject to defined auditability constraints governing recording and review of AI inputs, outputs and dispositions (definitions TBD).|SFA tier|Inspection|
|REQ-HFPX-ISC-005|Verification of each AI safety constraint, including enforcement ownership, shall be by a defined method (enforcement owner and method per constraint TBD).|SFA tier|Inspection|

Constraint inventory at this revision is TBD: containment, authority limits, monitoring, disengagement, auditability. No model architecture or algorithm is selected. No accuracies, thresholds or latencies are stated.

## 7. Architecture

Constraints apply at the boundaries defined in HFPX-AI-ARC-001 (detail TBD): input gating (TBD), output containment (TBD), monitoring/disengagement paths (TBD) and audit recording (TBD). Enforcement allocation TBD. No component selected.

## 8. Detailed Design

Not applicable at this revision. Constraint mechanisms, monitors and record formats are TBD; no selection is made.

## 9. Interfaces

Monitoring, disengagement and audit interfaces are TBD. ICD capture TBD.

## 10. Operational Concept

Constraints hold in all operating conditions and phases (detail TBD). Disengaged AI provides no advisories; primary control and safety functions continue unaffected.

## 11. Safety

> **IRON POLICY.** AI is monitoring/advisory ONLY; primary safety-critical flight control remains deterministic/bounded/verifiable; AI shall never silently override pilot or safety-system authority (human override preserved).

This document is the safety-constraint holder for Volume 18; enforcement ownership and means are TBD per REQ-HFPX-ISC-005. No safety claim is made.

## 12. Performance

Performance characteristics of constraint mechanisms (including any monitoring latencies) are TBD. No value is stated or baselined at this revision.

## 13. Verification & Validation

Verification method per constraint TBD, including enforcement-ownership verification; cases and regression TBD in HFPX-AI-VAV-001 (Chapter 18.12). No verification is claimed at this revision.

## 14. Risks

- Unenforced constraints → advisory path influencing control; mitigation: enforcement ownership TBD
- Unauditable AI behaviour blocking assurance; mitigation: auditability constraints TBD

## 15. Open Issues

Constraint inventory detail TBD; enforcement ownership TBD; monitoring/disengagement mechanisms TBD; audit means TBD; verification cases TBD.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on HFPX-AI-REQ-001, HFPX-AI-ARC-001, function definitions (18.3–18.9), override (18.11) and V&V (18.12).

## 18. Traceability

Parents: SYS-002, REQ-HFPX-ARC-002, SFA tier. Children: enforcement allocations (TBD), verification cases (18.12). RTM: REQ-HFPX-ISC-001..005 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. CONCEPT, Rev A (draft).

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 18.10) |
