# Regulatory Basis

**Document ID:** HFPX-CERT-RGB-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define how the HFP-X regulatory basis is researched, proposed, recorded, and closed. Owns Chapter 25.2. This document directly works ISS-001; all regulatory content is TBD pending authoritative-source research.

## 2. Scope

Covers the regulatory-basis determination process, research-evidence records, international hooks, and ISS-001 closure criteria. Does not state a certification basis, does not cite any regulation paragraph from memory, and does not claim compliance with any regulation or standard.

## 3. Applicable Documents

- HFPX-CERT-STR-001 Certification Strategy (this volume, TBD)
- HFPX-CERT-AVR-001 Applicable Aviation Regulations (this volume, TBD)
- STK-003, SYS tier certification classification (details TBD)
- ISS-001 (regulatory research issue — details TBD)
- National regulations, international provisions including ICAO-related material, and authority guidance — to be verified from authoritative sources. This document is structured according to general regulatory-planning practice; no compliance with any regulation or standard is claimed at this revision.

## 4. Definitions & Acronyms

- Regulatory basis: the agreed set of applicable regulations, standards, and guidance (content TBD — to be verified from authoritative sources) against which future compliance would be shown.
- Authoritative source: the issuing authority or standards body publication (identity TBD) from which regulatory text is directly obtained and cited.
- ISS-001: the programme open issue governing authoritative regulatory research.
- TBD/TBC: unknown-data markers; no values are invented.

## 5. System Context

Regulatory-basis work converts ISS-001 research into a proposed, approved basis that downstream chapters (airworthiness, experimental, type, production, compliance matrix) can trace to:

```text
ISS-001 RESEARCH → REGULATORY BASIS (25.2) → APPLICABLE REGULATIONS (25.3)
  → AIRWORTHINESS REQUIREMENTS (25.4) + COMPLIANCE MATRIX (25.10)
  → AUTHORITY ENGAGEMENT (25.11) FOR BASIS AGREEMENT
```

No downstream compliance activity starts from an unapproved basis.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-QRB-001 | The programme shall research the applicable national regulatory framework, including NCAA-related regulations and guidance, solely from authoritative sources, with citations to be verified from authoritative sources. | STK-003, ISS-001 | Inspection |
| REQ-HFPX-QRB-002 | The programme shall research applicable international hooks, including ICAO-related provisions, solely from authoritative sources, with content to be verified from authoritative sources. | STK-003, ISS-001 | Inspection |
| REQ-HFPX-QRB-003 | The programme shall define a basis-determination rule stating how the regulatory basis is proposed, reviewed, agreed with the authority, and recorded before use. | STK-003, ISS-001 | Inspection |
| REQ-HFPX-QRB-004 | The programme shall maintain research-evidence records showing source, version, date accessed, and excerpt or reference for every regulatory assertion, with practice TBD. | STK-003, ISS-001 | Inspection |
| REQ-HFPX-QRB-005 | The programme shall define ISS-001 closure criteria requiring that every regulatory statement traces to an authoritative source verified from authoritative sources, with no paragraph cited from memory. | STK-003, ISS-001 | Inspection |

This requirements set is structured according to general requirements practice; no compliance with any regulation or standard is claimed.

## 7. Architecture

Basis architecture (structure only): research tasks (national + international) → source-capture records → applicability assessment (Vol 25.3) → basis proposal → authority agreement (Vol 25.11) → recorded basis → compliance matrix instantiation (Vol 25.10). Each element's regulatory content is TBD — to be verified from authoritative sources.

## 8. Detailed Design

Detail TBD, including: research task breakdown for NCAA-related and ICAO-related sources (to be verified from authoritative sources); source-capture template (source, version, date, reference); basis-proposal contents (TBD); authority-agreement record (TBD, Vol 25.11); and handling of regulatory updates after basis agreement (TBD, with Vol 25.3). No regulation paragraph is cited in this design section.

## 9. Interfaces

- Certification ↔ authority (TBD — to be verified from authoritative sources) for basis discussion and agreement.
- Certification ↔ SE/requirements management for RTM and VCRM hooks (details TBD).
- Certification ↔ Safety/V&V/Test/Quality for basis implications (details TBD).
- Records and configuration interfaces per programme data-management practice (TBD).

## 10. Operational Concept

Basis work proceeds as: open ISS-001 research tasks → collect authoritative sources → record research evidence → assess applicability → draft basis proposal → engage authority → record agreement → freeze basis under change control. Any later regulatory change re-enters through the update rule; unapproved basis material is never used for compliance claims.

## 11. Safety

An incorrect or premature basis creates safety-assurance risk. Mitigation is procedural: no safety credit is taken from an unapproved basis, and flight readiness remains governed by Vol 13/24 and FRR (Vol 23.13). Any safety-related regulation or standard is TBD — to be verified from authoritative sources. Structured according to general safety-governance practice; no compliance claimed.

## 12. Performance

Basis-progress measures TBD (examples: research-task closure, source-capture completeness — thresholds TBD, none baselined). No values set at this revision.

## 13. Verification & Validation

This document is verified by inspection against the template and review checklist (criteria TBD). Validation is programme-authority approval. Substantive verification of the basis itself requires direct comparison of every regulatory assertion against its authoritative source (to be verified from authoritative sources); that verification is TBD and not claimed here. Structured according to general V&V practice; no compliance claimed.

## 14. Risks

- Research from non-authoritative or remembered sources → wrong basis; mitigation: authoritative-source-only rule with source-capture records.
- ICAO/international hooks missed (provisions TBD — to be verified from authoritative sources) → late basis change; mitigation: explicit international research task.
- Basis used before agreement → invalid compliance work; mitigation: basis-determination rule.
- ISS-001 closed prematurely → TBD content treated as fact; mitigation: explicit closure criteria.

## 15. Open Issues

ISS-001 (owns all regulatory research for this basis). TBD: NCAA source list, ICAO/international source list, basis-proposal format, authority-agreement mechanics, update handling. No regulation paragraph is cited from memory in this document.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on STK-003 / SYS-tier classification (TBD); ISS-001; HFPX-CERT-STR-001 (strategy); HFPX-CERT-AVR-001 (regulation inventory); HFPX-CERT-ATE-001 (authority engagement); programme records and configuration practice.

## 18. Traceability

Parents: STK-003, SYS tier (certification classification), ISS-001. Children: basis proposal, research-evidence records, ISS-001 closure record; downstream basis consumers (Vol 25.3/25.4/25.10). RTM: REQ-HFPX-QRB-001..005 → CONCEPT. All regulatory trace endpoints TBD pending research to be verified from authoritative sources. Structured according to traceability practice; no compliance claimed.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via programme change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 25.2) |
