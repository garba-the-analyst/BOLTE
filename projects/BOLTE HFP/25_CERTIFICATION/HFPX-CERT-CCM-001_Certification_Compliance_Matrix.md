# Certification Compliance Matrix

**Document ID:** HFPX-CERT-CCM-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the schema, trace practice, and coverage governance for the certification compliance matrix. Owns Chapter 25.10.

## 2. Scope

Covers matrix schema, requirement-to-evidence trace, coverage-gate rule, and hooks to the programme RTM/VCRM. Contains no matrix rows, states no coverage values, and claims no compliance with any regulation or standard. All regulatory content TBD pending authoritative-source research under ISS-001.

## 3. Applicable Documents

- HFPX-CERT-RGB-001 Regulatory Basis, HFPX-CERT-AVR-001 Applicable Aviation Regulations, HFPX-CERT-AWR-001 Airworthiness Requirements (this volume)
- Requirements-management and V&V planning (Vol 00.9, Vol 22 — details TBD)
- Matrix and traceability regulations, standards, and guidance — to be verified from authoritative sources. This document is structured according to general traceability-matrix practice; no compliance with any regulation or standard is claimed at this revision.

## 4. Definitions & Acronyms

- Compliance matrix: the controlled mapping from certification requirements to compliance evidence (schema TBD).
- RTM: Requirements Traceability Matrix; VCRM: Verification Cross-Reference Matrix (programme implementations TBD).
- Coverage gate: the review rule requiring defined trace completeness before proceeding (rule TBD).
- TBD/TBC: unknown-data markers only.

## 5. System Context

The matrix is the certification trace hub:

```text
BASIS (25.2/25.3) + AIRWORTHINESS REQS (25.4) → COMPLIANCE MATRIX (25.10)
  ↔ RTM / VCRM ↔ EVIDENCE (25.12) + CONFORMITY (25.13) + V&V (Vol 22)
  → AUTHORITY REVIEW (25.11)
```

Every certification requirement traces to evidence; every evidence item traces back to its requirement.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-QCM-001 | The programme shall define the compliance-matrix schema, with fields and status values TBD. | STK-003, ISS-001 | Inspection |
| REQ-HFPX-QCM-002 | The programme shall trace each certification requirement to its compliance evidence, with regulatory endpoints to be verified from authoritative sources. | STK-003, ISS-001 | Inspection |
| REQ-HFPX-QCM-003 | The programme shall define a coverage-gate rule governing required trace completeness before each review or authorisation, with thresholds TBD and none baselined. | STK-003, ISS-001 | Inspection |
| REQ-HFPX-QCM-004 | The programme shall define hooks between the compliance matrix and the programme RTM/VCRM, with mechanics TBD. | STK-003, ISS-001 | Inspection |

Structured according to general requirements practice; no compliance with any regulation or standard is claimed.

## 7. Architecture

Matrix architecture (structure only): requirement entries → compliance-method records → evidence links → verification-status fields → RTM/VCRM synchronisation → coverage reporting → gate control. Tooling TBD. Regulatory row content TBD — to be verified from authoritative sources.

## 8. Detailed Design

Detail TBD, including: column definitions; compliance-method taxonomy; evidence-link mechanics; status lifecycle; coverage computation and reporting; and RTM/VCRM synchronisation procedure. No fields are populated and no rows are instantiated at this revision.

## 9. Interfaces

- Certification ↔ SE/requirements management (RTM owner, TBD), V&V (VCRM, Vol 22), Safety, Test, Quality, Authority (TBD — to be verified from authoritative sources, via Vol 25.11).
- Tooling/configuration interfaces per programme practice (TBD).

## 10. Operational Concept

Define schema → instantiate rows only from the approved basis → link evidence as it is produced → report coverage → enforce the coverage gate at reviews and authorisations → change rows only by formal process with impact assessment.

## 11. Safety

Trace gaps risk unshown compliance. Control is procedural via the coverage-gate rule; flight safety itself remains under Vol 13/24 and FRR. Any safety-related matrix regulation or standard is TBD — to be verified from authoritative sources. Structured according to general safety-governance practice; no compliance claimed.

## 12. Performance

Matrix-health measures TBD (thresholds TBD, none baselined).

## 13. Verification & Validation

This document is verified by inspection against the template and review checklist (criteria TBD). Validation is programme-authority approval. Matrix correctness is later verified by audit of traces against authoritative sources (to be verified from authoritative sources) and evidence records; not claimed here. Structured according to general V&V practice; no compliance claimed.

## 14. Risks

- Schema defined late → ad-hoc tracing; mitigation: schema-first rule.
- Evidence linked to unapproved requirements → false coverage; mitigation: basis-gated instantiation.
- RTM/VCRM divergence → inconsistent status; mitigation: explicit hook rule.

## 15. Open Issues

ISS-001 (regulatory row content research). TBD: schema, trace mechanics, coverage-gate placement, RTM/VCRM synchronisation. No paragraph citations from memory.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on STK-003 / SYS tier (TBD); ISS-001; HFPX-CERT-RGB-001/AVR-001/AWR-001/EVD-001; Vol 00.9 requirements practice; Vol 22 V&V; Vol 25.11.

## 18. Traceability

Parents: STK-003, SYS tier (certification classification), ISS-001. Children: matrix schema, coverage-gate rule, RTM/VCRM hook records; downstream matrix rows and coverage reports. RTM: REQ-HFPX-QCM-001..004 → CONCEPT. Regulatory endpoints TBD pending research to be verified from authoritative sources. Structured according to traceability practice; no compliance claimed.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via programme change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 25.10) |
