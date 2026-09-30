# Safety-Critical Components

**Document ID:** HFPX-REL-SCC-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X safety-critical components direction for Volume 24 (Chapter 24.13): how identification criteria, component list control, special controls, and verification will be governed.
Sets identification and control rules only; it contains no component ratings, failure rates, or life limits beyond TBD.

## 2. Scope

Covers identification and special-control governance for safety-critical components across flight and ground elements as applicable, with applicability TBD.
In scope: identification criteria, list control, special controls, verification approach. Out of scope: hazard retirement owned by Vol 13, life-limit values owned by Vol 24.10, and design implementation owned by design volumes.
Supports the safety path without taking safety credit in this revision.

## 3. Applicable Documents

- Programme Charter STK-001; SyRS SYS-002/003; reliability classification tier TBD; SAF-001..006 tier (stubs, values TBD)
- HFPX-REL-ENG-001 Reliability Engineering, HFPX-REL-LLC-001 Life-Limited Components, HFPX-SAFE-CAS-001 Safety Case
- Vol 13 hazard log and Vol 13.5/13.6 analyses, Vol 27 support controls, HFPX-VV-PLN-001 V&V Plan
- Standards (structured according to): TBD — no compliance claimed in this revision

## 4. Definitions & Acronyms

- Safety-critical component: item whose failure could contribute to a hazard above criteria TBD; list TBD
- Identification criteria: rules determining safety-critical status; criteria TBD
- Special controls: additional design, manufacturing, maintenance, or tracking controls applied to listed items; controls TBD
- List control: configuration-controlled record of safety-critical components; schema TBD
- TBD: to be determined; TBC: to be confirmed

## 5. System Context

Safety-critical component control constrains design and support by ensuring candidate items receive special attention before any safety conclusion.
This document governs identification and control discipline; no item is claimed as adequately controlled in this revision.
Hazard severity and probability scales feeding criteria are TBD in Vol 13.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-RSC-001 | The programme shall define safety-critical identification criteria, with criteria and applicability TBD. | TBD reliability classification; SAF tier; REQ-HFPX-SCA-001 | Inspection |
| REQ-HFPX-RSC-002 | The programme shall maintain a configuration-controlled safety-critical components list, with list TBD and schema TBD. | TBD reliability classification; Vol 13 hazard log | Inspection |
| REQ-HFPX-RSC-003 | The programme shall define special controls for listed components, with controls and ownership TBD. | TBD reliability classification; Vol 27; Vol 24.10 | Inspection |
| REQ-HFPX-RSC-004 | Identification, listing, and special controls shall be verified under a defined verification approach, with method and criteria TBD. | TBD reliability classification; REQ-HFPX-SCA-004 | Analysis |

## 7. Architecture

Control organisation TBD: safety-critical owner, Vol 13 safety owners, design-domain owners, Vol 27 support owners, independent reviewer TBD.
Record architecture TBD: list schema TBD (component, criterion TBD, controls TBD, status).
Control architecture TBD: design, manufacturing, maintenance, and tracking control threads TBD.

## 8. Detailed Design

Methodology only, no values:
- Criteria: hazard-contribution rules TBD; severity/probability inputs TBD (scales TBD in Vol 13); single-failure treatment TBD.
- List: schema TBD; entry/exit rules TBD; all entries TBD.
- Special controls: design controls TBD; manufacturing controls TBD; maintenance and tracking controls TBD with Vol 24.10/27 hooks TBD.
- Change control: re-identification triggers TBD; propagation to design and support TBD.

## 9. Interfaces

- Safety-critical ↔ Hazard log and Vol 13.5/13.6 (hazard-contribution inputs; hazard authority owned by Vol 13)
- Safety-critical ↔ Life-limited components (Vol 24.10 determination and tracking exchange as applicable)
- Safety-critical ↔ Support (Vol 27 special handling, tracking, and documentation; details TBD)
- Safety-critical ↔ Design/manufacturing volumes (control implementation; details TBD)
- Safety-critical ↔ V&V (identification and control cases enter VCRM; verification returns closure TBD)

## 10. Operational Concept

Safety-critical control matures across the lifecycle: criteria at SRR → candidate list through PDR/CDR as applicable → special controls through design and support → gate acceptance TBD.
This concept defines identification and control discipline only, not hazard retirement, operation, or flight conduct.
No adequacy of control is claimed in this revision.

## 11. Safety

No safety claim is made in this revision; safety-critical listing and controls take no safety credit until verified through the safety path.
Hazard retirement remains owned by Vol 13 and HFPX-SAFE-CAS-001; no retirement is claimed here.

## 12. Performance

Safety-critical performance indicators TBD (no thresholds baselined): identification coverage TBD, list completeness TBD, special-control implementation TBD.
No failure rates, MTBF/MTTR values, availability figures, life limits, or hazard probabilities are set in this revision.

## 13. Verification & Validation

This document is verified at SRR/PDR against the SEMP checklist (header, 20 sections, IDs, criteria direction, no-values rule).
Requirement verification follows the V&V Plan: Inspection/Analysis methods with independent review as applicable; acceptance criteria TBD per case; evidence TBD until closed.
Validation is programme-authority plus Safety Review Board acceptance at gates as applicable; certification validation owned by Vol 25 with no claims here.

## 14. Risks

- Late identification leaving controls unimplemented; mitigation: criteria and candidate review TBD before PDR/CDR as applicable
- Listed items treated as controlled without verified controls; mitigation: TBD-only adequacy enforced at gates
- List divergence from Vol 13 hazard log; mitigation: trace and consistency checks TBD

## 15. Open Issues

Identification criteria TBD. Component list TBD. Special controls TBD. Ownership TBD. Verification criteria TBD. Vol 13/24.10/27 hook details TBD. Severity/probability scales TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on STK-001/SYS-002/003 and TBD reliability classification, SAF tier and HFPX-SAFE-CAS-001, HFPX-REL-ENG-001, HFPX-REL-LLC-001 (Vol 24.10), SEMP, V&V Plan, Vol 13 hazard log and Vol 13.5/13.6, Vol 27 support.

## 18. Traceability

Parents: SYS-002/003, TBD reliability classification, SAF tier, REQ-HFPX-SCA-001/002, Vol 13. Children: safety-critical list and control records (artefact IDs TBD).
RTM: REQ-HFPX-RSC-001..004 → CONCEPT. Each listed item traces to criterion TBD → hazard input → special controls TBD → VCRM closure (all TBD except direction).

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Safety-critical list under reliability configuration control once opened; changes via change records with affected-component impact stated.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (safety-critical identification and control direction; list and controls TBD) |
