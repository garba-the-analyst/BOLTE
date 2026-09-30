# Maintainability

**Document ID:** HFPX-REL-MNT-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X maintainability direction for Volume 24 (Chapter 24.7): how maintainability attributes, MTTR hooks, demonstration approach, and Vol 27 hooks will be controlled.
Sets attribute and demonstration rules only; it contains no MTTR values, task times, or availability figures beyond TBD.

## 2. Scope

Covers design-for-maintainability attributes and maintainability demonstration planning across defined maintenance levels, with levels TBD.
In scope: attribute definitions, MTTR hooks to Vol 24.9, demonstration-by-demo rules, Vol 27 hooks. Out of scope: maintenance execution owned by Vol 27, and quantitative repair data owned by Vol 24.9.
Applies to flight and ground elements as applicable, with applicability TBD.

## 3. Applicable Documents

- Programme Charter STK-001; SyRS SYS-002/003; reliability classification tier TBD; SAF tier (stubs)
- HFPX-REL-ENG-001 Reliability Engineering, HFPX-REL-MTR-001 MTTR, HFPX-SAFE-CAS-001 Safety Case
- Vol 27 maintainability/support volumes, HFPX-VV-PLN-001 V&V Plan, Vol 13 safety hooks as applicable
- Standards (structured according to): TBD — no compliance claimed in this revision

## 4. Definitions & Acronyms

- Maintainability: ability of an item to be retained in or restored to a state to perform as required under stated conditions; attributes TBD
- Maintainability attribute: design feature enabling maintenance (access, testability, interchangeability, diagnostics); list TBD
- Demonstration: verification by maintenance demo under controlled conditions; method TBD
- Maintenance level: organisational, intermediate, depot or equivalent; definitions TBD
- TBD: to be determined; TBC: to be confirmed

## 5. System Context

Maintainability constrains design so that future repair and servicing concepts remain achievable; achievability is unproven until demonstrated under V&V control.
This document governs attribute and demonstration discipline; no maintainability outcome is claimed in this revision.
Quantitative repair inputs are owned by Vol 24.9 (all values TBD).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-RMN-001 | The programme shall define maintainability attributes with applicability per indenture level, with attributes and applicability TBD. | TBD reliability classification; HFPX-REL-ENG-001 | Inspection |
| REQ-HFPX-RMN-002 | Maintainability assessment shall use MTTR inputs governed by Vol 24.9, with all values TBD and hook rules TBD. | TBD reliability classification; Vol 24.9 | Analysis |
| REQ-HFPX-RMN-003 | Maintainability shall be verified by demonstration under a defined demonstration method, with method and acceptance criteria TBD. | TBD reliability classification; V&V Plan | Demonstration |
| REQ-HFPX-RMN-004 | Maintainability shall maintain defined hooks to Vol 27 support volumes, with interface, traceability, and update rules TBD. | TBD reliability classification; Vol 27 | Inspection |

## 7. Architecture

Maintainability organisation TBD: maintainability owner, design-domain delegates, Vol 27 support owners, independent reviewer TBD.
Attribute architecture TBD: attribute list per level, with allocation to design volumes TBD.
Demonstration architecture TBD: demo articles, conditions, and recording schema TBD.

## 8. Detailed Design

Methodology only, no values:
- Attributes: candidate attributes TBD; design-guidance rules TBD; compliance-recording schema TBD.
- MTTR hooks: input qualification TBD; scope alignment with Vol 24.9 TBD; uncertainty handling TBD.
- Demonstration: demo scope TBD; conditions TBD; task selection TBD; recording and acceptance rules TBD (no times baselined).
- Vol 27 hooks: support-concept exchange TBD; spares/GSE/tooling interfaces TBD as applicable.

## 9. Interfaces

- Maintainability ↔ MTTR (Vol 24.9 quantitative inputs; values TBD)
- Maintainability ↔ Support (Vol 27 maintenance concept, spares, GSE, documentation; details TBD)
- Maintainability ↔ Design volumes (Vol 03–18 own attribute implementation; details TBD)
- Maintainability ↔ Safety (maintenance-error and access-safety hooks to Vol 13 as applicable; authority owned by safety path)
- Maintainability ↔ V&V (demo cases enter VCRM; verification returns closure TBD)

## 10. Operational Concept

Maintainability matures across the lifecycle: attributes defined at SRR/PDR as applicable → design implementation through CDR → demonstration through integration and test → gate acceptance TBD.
This concept defines attribute and demonstration discipline only, not maintenance execution or flight operations.
No maintainability outcome is asserted in this revision.

## 11. Safety

No safety claim is made in this revision; maintainability provisions take no safety credit until verified through the safety path.
Maintenance-induced hazard controls remain owned by Vol 13 with criteria TBD; no control is claimed here.

## 12. Performance

Maintainability performance indicators TBD (no thresholds baselined): attribute coverage TBD, demo completeness TBD, Vol 27 hook coverage TBD.
No MTTR values, task times, availability figures, failure rates, or life limits are set in this revision.

## 13. Verification & Validation

This document is verified at SRR/PDR against the SEMP checklist (header, 20 sections, IDs, no-values rule, hook direction).
Requirement verification follows the V&V Plan: Inspection/Analysis/Demonstration methods; acceptance criteria TBD per case; evidence TBD until closed.
Validation is programme-authority approval at gates; certification validation owned by Vol 25 with no claims here.

## 14. Risks

- Attributes stated but not implemented in design; mitigation: allocation-to-design trace TBD before CDR
- Demonstration optimism without controlled conditions; mitigation: demo method and acceptance criteria TBD before any claim
- Vol 27 concept divergence; mitigation: hook and consistency-check rules TBD

## 15. Open Issues

Attribute list TBD. Maintenance levels TBD. Demonstration method TBD. All repair values TBD. Vol 27 hook details TBD. Acceptance criteria TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on STK-001/SYS-002/003 and TBD reliability classification, HFPX-REL-ENG-001, HFPX-REL-MTR-001 (Vol 24.9), SEMP, V&V Plan, SAF tier and HFPX-SAFE-CAS-001, Vol 27 support volumes, design volumes.

## 18. Traceability

Parents: SYS-002/003, TBD reliability classification, SAF tier, Vol 27. Children: attribute records and demo cases (artefact IDs TBD).
RTM: REQ-HFPX-RMN-001..004 → CONCEPT. Each attribute traces to design implementation → MTTR input TBD → demo case → VCRM closure (all TBD except direction).

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Changes via change records with affected-attribute impact stated.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (maintainability attributes and demo direction; values TBD) |
