# Flight-Test Authorisation

**Document ID:** HFPX-CERT-FTA-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define how flight-test activity is authorised, coordinated, gated, and stopped. Owns Chapter 25.6.

## 2. Scope

Covers authorisation artifacts, range coordination, the Flight Readiness Review gate, and the stop-rule. Authorises no flight, states no criteria values, and claims no compliance with any regulation or standard. All regulatory and criteria content TBD pending authoritative-source research under ISS-001 and Vol 23 definition.

## 3. Applicable Documents

- HFPX-CERT-STR-001 Certification Strategy, HFPX-CERT-EXP-001 Experimental Aircraft Requirements (this volume)
- Vol 23 Flight Test, including FRR (Vol 23.13, criteria TBD)
- Range, safety (Vol 13/24), and operations (Vol 27) practices (details TBD)
- Flight-authorisation regulations, standards, and guidance — to be verified from authoritative sources. This document is structured according to general flight-test governance practice; no compliance with any regulation or standard is claimed at this revision.

## 4. Definitions & Acronyms

- Flight-test authorisation: the recorded permission set allowing defined test flights (artifacts TBD).
- Range coordination: agreement with test-range stakeholders on airspace, safety, and logistics (detail TBD).
- FRR: Flight Readiness Review (Vol 23.13 gate, criteria TBD).
- Stop-rule: the defined conditions and authority under which test activity is halted.
- TBD/TBC: unknown-data markers only.

## 5. System Context

Authorisation gates every flight-test campaign:

```text
EXPERIMENTAL (25.5) + FRR (23.13) + RANGE → FLIGHT-TEST AUTHORISATION (25.6)
  → AUTHORISED TEST EXECUTION (Vol 23) → EVIDENCE (25.12) + CONFORMITY (25.13)
```

No test proceeds without authorisation artifacts, FRR passage, and range agreement.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-QFA-001 | The programme shall define the flight-test authorisation artifacts and approval workflow, with artifact contents TBD pending material to be verified from authoritative sources. | STK-003, ISS-001 | Inspection |
| REQ-HFPX-QFA-002 | The programme shall define range-coordination requirements and records, with detail TBD. | STK-003, ISS-001 | Inspection |
| REQ-HFPX-QFA-003 | The programme shall require passage of the FRR gate (Vol 23.13) with criteria TBD before authorised flight test. | STK-003, ISS-001 | Inspection |
| REQ-HFPX-QFA-004 | The programme shall define a stop-rule stating halt conditions, halt authority, and restart conditions, with detail TBD. | STK-003, ISS-001 | Inspection |

Structured according to general requirements practice; no compliance with any regulation or standard is claimed.

## 7. Architecture

Authorisation architecture (structure only): request artifacts → safety/test review → FRR → range agreement → authorisation record → controlled execution → anomaly/stop handling → close-out records. Regulatory inputs at each step TBD — to be verified from authoritative sources.

## 8. Detailed Design

Detail TBD, including: artifact list and templates; signatory roles (TBD); FRR entrance/exit criteria linkage to Vol 23.13; range-agreement contents; envelope-expansion controls (TBD, Vol 23); and stop/restart procedures. No criteria or thresholds stated.

## 9. Interfaces

- Certification ↔ Flight Test (Vol 23), Range stakeholders (TBD), Safety (Vol 13/24), Operations (Vol 27), Authority (TBD — to be verified from authoritative sources).
- Records interface to evidence (Vol 25.12) and non-conformity flow (Vol 28.6 linkage TBD).

## 10. Operational Concept

Prepare artifacts → complete development and safety inputs → pass FRR → secure range → record authorisation → fly the authorised envelope only → invoke stop-rule on trigger → record and disposition → re-authorise only through the defined workflow.

## 11. Safety

Authorisation is a safety gate, not a safety analysis; Vol 13/24 analyses and FRR evidence remain mandatory. Any safety-related authorisation regulation or standard is TBD — to be verified from authoritative sources. Structured according to general safety-governance practice; no compliance claimed.

## 12. Performance

Authorisation-readiness measures TBD (thresholds TBD, none baselined).

## 13. Verification & Validation

This document is verified by inspection against the template and review checklist (criteria TBD). Validation is programme-authority approval. Campaign-level authorisation is verified later by inspection of artifacts, FRR records, and range agreements against their defined criteria (criteria TBD — to be verified from authoritative sources where regulatory). Structured according to general V&V practice; no compliance claimed.

## 14. Risks

- Flight without complete authorisation → unauthorised operation; mitigation: artifact-and-approval workflow.
- Range coordination gaps → conflict or abort; mitigation: range-requirements rule.
- FRR bypassed under schedule pressure → unready flight; mitigation: mandatory FRR-gate rule.
- Unclear stop authority → continued unsafe testing; mitigation: explicit stop-rule.

## 15. Open Issues

ISS-001 (authorisation-regulation research). TBD: artifact list, range requirements, FRR criteria (Vol 23.13 owner), stop/restart detail. No paragraph citations from memory.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on STK-003 / SYS tier (TBD); ISS-001; HFPX-CERT-STR-001/EXP-001; Vol 23 (including 23.13), Vol 13/24, Vol 27, Vol 25.11/25.12/25.13; range stakeholders (TBD).

## 18. Traceability

Parents: STK-003, SYS tier (certification classification), ISS-001. Children: authorisation artifacts, range agreements, FRR linkage records, stop-rule record; downstream test execution and evidence. RTM: REQ-HFPX-QFA-001..004 → CONCEPT. Regulatory endpoints TBD pending research to be verified from authoritative sources. Structured according to traceability practice; no compliance claimed.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via programme change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 25.6) |
