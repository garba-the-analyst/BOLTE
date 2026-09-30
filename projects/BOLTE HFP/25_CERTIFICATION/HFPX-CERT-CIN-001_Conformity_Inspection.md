# Conformity Inspection

**Document ID:** HFPX-CERT-CIN-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define how conformity of articles, processes, and records is scoped, inspected, dispositioned, and recorded. Owns Chapter 25.13.

## 2. Scope

Covers conformity scope, inspection practice, non-conformity flow, and records. Inspects nothing, dispositions nothing, and claims no compliance with any regulation or standard. All regulatory content TBD pending authoritative-source research under ISS-001.

## 3. Applicable Documents

- HFPX-CERT-EVD-001 Certification Evidence, HFPX-CERT-CCM-001 Certification Compliance Matrix (this volume)
- Vol 28 Quality, including non-conformity handling (Vol 28.6, details TBD)
- Vol 22 V&V, Vol 23 Flight Test (hooks TBD)
- Conformity-inspection regulations, standards, and guidance — to be verified from authoritative sources. This document is structured according to general conformity-assurance practice; no compliance with any regulation or standard is claimed at this revision.

## 4. Definitions & Acronyms

- Conformity: correspondence of an article, process, installation, or record to its approved definition (scope TBD).
- Conformity inspection: the planned check establishing conformity (practice TBD).
- Non-conformity: a departure from definition, handled through a controlled flow (detail TBD, Vol 28.6 hook).
- TBD/TBC: unknown-data markers only.

## 5. System Context

Conformity gates the credibility of test and evidence:

```text
DESIGN DEFINITION → CONFORMITY SCOPE (25.13) → INSPECTION → CONFORMED ARTICLE
  → TEST (Vol 23) / V&V (Vol 22) → EVIDENCE (25.12) → MATRIX (25.10)
  → NON-CONFORMITY FLOW (Vol 28.6 linkage) ON DEPARTURE
```

Only conformed configurations (or explicitly dispositioned departures) feed authorised test and evidence.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-QCI-001 | The programme shall define conformity scope for articles, installations, processes, and records, with scope TBD pending material to be verified from authoritative sources. | STK-003, ISS-001 | Inspection |
| REQ-HFPX-QCI-002 | The programme shall define conformity-inspection practice, including planning, execution, and sign-off, with detail TBD. | STK-003, ISS-001 | Inspection |
| REQ-HFPX-QCI-003 | The programme shall define the non-conformity flow with hooks to Vol 28.6, with detail TBD. | STK-003, ISS-001 | Inspection |
| REQ-HFPX-QCI-004 | The programme shall define conformity records practice, with formats and retention TBD pending material to be verified from authoritative sources. | STK-003, ISS-001 | Inspection |

Structured according to general requirements practice; no compliance with any regulation or standard is claimed.

## 7. Architecture

Conformity architecture (structure only): scope definition → inspection planning → execution and sign-off → records → non-conformity disposition loop (Vol 28.6) → re-inspection → release to test/evidence. Regulatory criteria at each step TBD — to be verified from authoritative sources.

## 8. Detailed Design

Detail TBD, including: scope categories; inspection-plan and checklist templates; inspector roles and independence (TBD); sign-off workflow; non-conformity categories, containment, root-cause, corrective-action, and closure linkage to Vol 28.6; and re-inspection rules. No inspections are planned or recorded at this revision.

## 9. Interfaces

- Certification/conformity ↔ design owners, Manufacturing/Build, V&V (Vol 22), Flight Test (Vol 23), Quality (Vol 28, including 28.6), Safety (Vol 13/24), Authority (TBD — to be verified from authoritative sources, via Vol 25.11).
- Records interface to Vol 25.12 evidence practice (TBD).

## 10. Operational Concept

Scope → plan → inspect → record → release conformed configuration to test → contain and disposition any departure through the Vol 28.6-linked flow → re-inspect before release. Test on a non-conformed, non-dispositioned configuration is not authorised.

## 11. Safety

Uncontrolled departures risk invalid tests and unsafe flight. Control is procedural via scope, inspection, and non-conformity flow; flight safety itself remains under Vol 13/24 and FRR. Any safety-related conformity regulation or standard is TBD — to be verified from authoritative sources. Structured according to general safety-governance practice; no compliance claimed.

## 12. Performance

Conformity-process measures TBD (thresholds TBD, none baselined).

## 13. Verification & Validation

This document is verified by inspection against the template and review checklist (criteria TBD). Validation is programme-authority approval. Conformity itself is later verified by inspection of articles and records against their definitions, with regulatory correctness resting on authoritative sources (to be verified from authoritative sources); not claimed here. Structured according to general V&V practice; no compliance claimed.

## 14. Risks

- Scope undefined → uninspected departures; mitigation: scope-definition rule.
- Inspection without independence or records → untrustworthy conformity; mitigation: practice-and-records rules.
- Non-conformity bypassed to hold schedule → invalid evidence; mitigation: Vol 28.6-linked flow rule.

## 15. Open Issues

ISS-001 (conformity-regulation research). TBD: scope, practice, Vol 28.6 flow mechanics, records and roles. No paragraph citations from memory.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on STK-003 / SYS tier (TBD); ISS-001; HFPX-CERT-EVD-001/CCM-001; Vol 28 (including 28.6); Vol 22/23; design-definition owners (TBD).

## 18. Traceability

Parents: STK-003, SYS tier (certification classification), ISS-001. Children: conformity-scope record, inspection-practice record, non-conformity-flow record, conformity-records set (all TBD). RTM: REQ-HFPX-QCI-001..004 → CONCEPT. Regulatory endpoints TBD pending research to be verified from authoritative sources. Structured according to traceability practice; no compliance claimed.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via programme change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 25.13) |
