# Certification Strategy

**Document ID:** HFPX-CERT-STR-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X certification strategy: pathway options, authority engagement sequence, and evidence-buildup logic from demonstrator to any future certified product. Owns Chapter 25.1.

## 2. Scope

Covers certification pathway selection, phasing of evidence, and relationship to flight-test authorisation, type-certification strategy, and production certification. Does not select a pathway, does not name a certification basis, and does not claim compliance with any regulation or standard. All regulatory content is TBD pending authoritative-source research undertaken under ISS-001.

## 3. Applicable Documents

- HFPX-PGM-CHR-001 Programme Charter (authority TBD)
- HFPX-SYS-REQ-001 SyRS (stub), HFPX-SYS-ARC-001 SAD (stub)
- HFPX-CERT-RGB-001 Regulatory Basis, HFPX-CERT-AVR-001 Applicable Aviation Regulations (both TBD, this volume)
- Stakeholder requirement STK-003 (certification classification, SYS tier — details TBD)
- Open issue ISS-001 (regulatory research — details TBD)
- All aviation regulations, standards, and authority guidance referenced in this volume — to be verified from authoritative sources. This document is structured according to general certification-planning practice; no compliance with any regulation or standard is claimed at this revision.

## 4. Definitions & Acronyms

- Certification pathway: the regulatory route (options TBD, including experimental where applicable — to be verified from authoritative sources) by which flight activity or a product is authorised.
- Authority: the responsible aviation authority (TBD — to be verified from authoritative sources).
- Evidence buildup: ordered accumulation of design, analysis, test, and conformity records supporting successive authorisations.
- TBD: to be determined; TBC: to be confirmed. Unknowns are recorded as TBD/TBC only.

## 5. System Context

Certification strategy sits above the Vol 25 chapter documents and connects programme gates to external authorisation:

```text
STK-003 / SYS TIER → CERTIFICATION STRATEGY (25.1)
  → REGULATORY BASIS (25.2) + APPLICABLE REGULATIONS (25.3)
  → EXPERIMENTAL (25.5) / FLIGHT-TEST AUTHORISATION (25.6)
  → TYPE-CERT STRATEGY (25.7, long-term) + PRODUCTION (25.8, long-term)
  → CONTINUING AIRWORTHINESS (25.9) + EVIDENCE / CONFORMITY (25.12 / 25.13)
```

Unmanned-first sequencing (prompt DDR-001 logic) is preserved: early learning under experimental / flight-test authorisation precedes any long-term certified-product ambition.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-QCS-001 | The programme shall define and maintain certification pathway options, including experimental-category routes where applicable, with each option TBD pending research to be verified from authoritative sources. | STK-003, ISS-001 | Inspection |
| REQ-HFPX-QCS-002 | The programme shall identify the responsible authority and applicable authorisation routes, TBD pending research to be verified from authoritative sources. | STK-003, ISS-001 | Inspection |
| REQ-HFPX-QCS-003 | The certification strategy shall require recorded strategy approval at a defined programme gate before any compliance claim or external commitment is made. | STK-003, ISS-001 | Inspection |
| REQ-HFPX-QCS-004 | The programme shall define an evidence-buildup sequence linking design, verification, conformity, and operational records to successive authorisations, with detail TBD. | STK-003, ISS-001 | Inspection |
| REQ-HFPX-QCS-005 | The programme shall make no claim of compliance with any aviation regulation or standard until the regulatory basis is established from authoritative sources and formally approved. | STK-003, ISS-001 | Inspection |

All regulatory content supporting these requirements is TBD pending authoritative-source research under ISS-001. This requirements set is structured according to general certification-planning practice; no compliance is claimed.

## 7. Architecture

Strategy architecture (structure only): pathway-options register (TBD) → authority-engagement plan (Vol 25.11) → regulatory basis (Vol 25.2) → authorisation phasing (experimental 25.5, flight-test 25.6) → long-term branches (type 25.7, production 25.8) → continuing airworthiness (25.9). Compliance matrix (25.10) and evidence/conformity (25.12/25.13) provide trace and records. All regulatory selections within this architecture are TBD — to be verified from authoritative sources.

## 8. Detailed Design

Detailed strategy content TBD, including: pathway-option descriptions (including experimental — to be verified from authoritative sources); entry/exit criteria per authorisation stage (TBD); evidence expectations per stage (TBD, hooks to Vol 22/23); decision records for pathway selection (TBD); and alignment with MVP/demonstrator sequencing (Vol 33, TBD). No pathway is selected at this revision.

## 9. Interfaces

- SE ↔ Certification (Vol 25 chapter owners, TBD) via requirements and RTM discipline.
- Certification ↔ Safety (Vol 13/24), V&V (Vol 22), Flight Test (Vol 23), Quality (Vol 28), Operations/Sustainment (Vol 27/32).
- Certification ↔ external authority (TBD — to be verified from authoritative sources) via engagement plan (Vol 25.11).
- Tooling and change control per programme configuration practice (details TBD).

## 10. Operational Concept

Strategy operates as the programme's certification control loop: research regulatory options (ISS-001) → propose pathways → approve strategy at a gate → build evidence in order → seek staged authorisations → record outcomes → revisit strategy only by formal change. Early operation is demonstrator-focused; certified-product routes remain long-term options only.

## 11. Safety

Certification strategy does not substitute for the safety programme. Flight safety is governed by Vol 13/24 and gated readiness (including FRR, Vol 23.13); no flight is authorised by strategy alone. Any safety-related regulatory expectation is TBD — to be verified from authoritative sources. This section is structured according to general safety-governance practice; no compliance is claimed.

## 12. Performance

Strategy effectiveness measures TBD (examples: pathway-option closure, ISS-001 research progress, evidence-trace coverage — targets and thresholds TBD, none baselined). No performance values are set at this revision.

## 13. Verification & Validation

This document is verified by inspection against the document template (header, full sections, requirement IDs, traceability) at the applicable programme review (criteria TBD). Validation is programme-authority approval of the strategy. Any claim that a pathway satisfies a regulation or standard requires evidence verified from authoritative sources; no such claim is made at this revision. Structured according to general V&V practice; no compliance claimed.

## 14. Risks

- Pathway assumed before research completes → rework or unauthorised operation; mitigation: ISS-001 research gate and strategy-approval rule (REQ-HFPX-QCS-003).
- Experimental route misunderstood (rules, limitations — to be verified from authoritative sources) → schedule delay; mitigation: Vol 25.5 research actions.
- Evidence built out of sequence → gaps at authorisation; mitigation: evidence-buildup sequence (REQ-HFPX-QCS-004) with hooks to Vol 22/23.
- Premature compliance language → false assurance; mitigation: no-compliance-claimed rule (REQ-HFPX-QCS-005).

## 15. Open Issues

ISS-001 (authoritative regulatory research — the direct driver of all TBD regulatory content in this document). Further TBD issues: authority identity, pathway-option viability, strategy-approval gate placement, evidence-buildup detail. No regulation or standard is cited from memory; all such content awaits research to be verified from authoritative sources.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on STK-003 and SYS-tier certification classification (details TBD); ISS-001 regulatory research; SyRS/SAD stubs; Vol 25.2/25.3 (basis and regulation inventory); Vol 25.11 (authority engagement); Vol 22/23 (V&V and test readiness); Vol 33 (MVP/demonstrator scope).

## 18. Traceability

Parents: STK-003, SYS tier (certification classification), ISS-001. Children: pathway-option records, strategy-approval record, evidence-buildup plan; downstream Vol 25.5/25.6 authorisation work and long-term Vol 25.7/25.8 strategies. RTM: REQ-HFPX-QCS-001..005 → CONCEPT. All regulatory trace targets TBD pending research to be verified from authoritative sources. Structured according to traceability practice; no compliance claimed.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via programme change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 25.1) |
