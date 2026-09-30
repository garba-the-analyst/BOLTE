# Airworthiness Requirements

**Document ID:** HFPX-CERT-AWR-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define how HFP-X airworthiness requirements are derived, recorded, and verified. Owns Chapter 25.4.

## 2. Scope

Covers airworthiness-criteria derivation, basis linkage, and verification approach. States no airworthiness criteria, cites no regulation paragraph, and claims no compliance with any regulation or standard. All criteria TBD pending authoritative-source research under ISS-001.

## 3. Applicable Documents

- HFPX-CERT-RGB-001 Regulatory Basis, HFPX-CERT-AVR-001 Applicable Aviation Regulations (this volume)
- STK-003 (certification-related stakeholder need, SYS tier — details TBD)
- HFPX-SYS-REQ-001 SyRS (stub), safety programme Vol 13/24 (details TBD)
- Airworthiness regulations, standards, and guidance — to be verified from authoritative sources. This document is structured according to general airworthiness-planning practice; no compliance with any regulation or standard is claimed at this revision.

## 4. Definitions & Acronyms

- Airworthiness requirement: a requirement expressing a condition for safe design, construction, and operation (content TBD).
- Derivation: the recorded reasoning from regulatory basis and stakeholder need to airworthiness requirement (method TBD).
- Verification: the Analysis, Inspection, Demonstration, or Test activity showing a requirement is met (plan TBD).
- TBD/TBC: unknown-data markers only.

## 5. System Context

Airworthiness requirements bridge the regulatory basis to engineering and safety work:

```text
STK-003 + REGULATORY BASIS (25.2/25.3) → AIRWORTHINESS REQUIREMENTS (25.4)
  → DESIGN VOLUMES (03–18) + SAFETY (13/24) + V&V (22) + COMPLIANCE MATRIX (25.10)
```

Derivation inputs include STK-003 hooks; verification executes through Vol 22 and test volumes.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-QAW-001 | The programme shall derive airworthiness requirements from the approved regulatory basis and STK-003, with derivation method and criteria TBD pending research to be verified from authoritative sources. | STK-003, ISS-001 | Inspection |
| REQ-HFPX-QAW-002 | Each airworthiness requirement shall record its regulatory basis linkage, with basis content to be verified from authoritative sources. | STK-003, ISS-001 | Inspection |
| REQ-HFPX-QAW-003 | Each airworthiness requirement shall state its verification method and success criteria, with detail TBD. | STK-003, ISS-001 | Inspection |
| REQ-HFPX-QAW-004 | The programme shall maintain STK-003 traceability for airworthiness requirements within the SYS-tier structure, with classification detail TBD. | STK-003, ISS-001 | Inspection |

Structured according to general requirements practice; no compliance with any regulation or standard is claimed.

## 7. Architecture

Requirements architecture (structure only): basis inputs → derivation records → airworthiness requirement set → allocation to design/safety owners → verification tasks → compliance-matrix linkage. Tooling and allocation tables TBD. All regulatory content TBD — to be verified from authoritative sources.

## 8. Detailed Design

Detail TBD, including: derivation procedure; requirement-writing rules; allocation to subsystems; verification planning with Vol 22; and handling of special conditions or equivalent-safety findings if the authority process provides for them (concepts TBD — to be verified from authoritative sources). No criteria values stated.

## 9. Interfaces

- Certification ↔ design-volume owners, Safety, V&V/Test, Quality.
- Certification ↔ authority (TBD — to be verified from authoritative sources) on basis interpretation (via Vol 25.11).
- RTM/VCRM interfaces (details TBD, hooks to Vol 25.10).

## 10. Operational Concept

Derive once the basis is approved → allocate → design to requirements → verify per plan → record in compliance matrix → change only by formal process. No design proceeds on assumed airworthiness criteria; unknowns remain TBD until researched.

## 11. Safety

Airworthiness requirements carry safety intent but do not replace independent safety assessment (Vol 13/24). Any safety-related regulation or standard invoked here is TBD — to be verified from authoritative sources. Structured according to general safety-governance practice; no compliance claimed.

## 12. Performance

Derivation/verification progress measures TBD (thresholds TBD, none baselined).

## 13. Verification & Validation

This document is verified by inspection against the template and review checklist (criteria TBD). Validation is programme-authority approval. Requirement-level verification executes later per stated methods; regulatory correctness depends on authoritative sources (to be verified from authoritative sources) and is not claimed here. Structured according to general V&V practice; no compliance claimed.

## 14. Risks

- Criteria derived before basis approval → rework; mitigation: basis-linkage gate.
- STK-003 misinterpreted → misallocated requirements; mitigation: explicit STK-003 trace rule.
- Verification methods undefined → unverifiable requirements; mitigation: method-and-criteria rule.

## 15. Open Issues

ISS-001 (basis research). TBD: derivation method, allocation, verification plans, special-condition handling. No paragraph citations from memory.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on STK-003 / SYS tier (TBD); ISS-001; HFPX-CERT-RGB-001/AVR-001; SyRS/SAD; Vol 13/24 (safety), Vol 22 (V&V), Vol 25.10/25.11.

## 18. Traceability

Parents: STK-003, SYS tier (certification classification), ISS-001. Children: airworthiness requirement set, derivation records, verification plans; downstream design, safety, V&V, and matrix artifacts. RTM: REQ-HFPX-QAW-001..004 → CONCEPT. Regulatory endpoints TBD pending research to be verified from authoritative sources. Structured according to traceability practice; no compliance claimed.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via programme change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 25.4) |
