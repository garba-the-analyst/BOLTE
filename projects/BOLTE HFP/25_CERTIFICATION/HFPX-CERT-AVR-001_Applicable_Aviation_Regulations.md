# Applicable Aviation Regulations

**Document ID:** HFPX-CERT-AVR-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define how applicable aviation regulations are inventoried, assessed for applicability, and kept current. Owns Chapter 25.3.

## 2. Scope

Covers the regulation inventory, applicability assessment, and update rule. Contains no regulation list, cites no paragraph from memory, and claims no compliance with any regulation or standard. All content TBD pending authoritative-source research under ISS-001.

## 3. Applicable Documents

- HFPX-CERT-STR-001 Certification Strategy, HFPX-CERT-RGB-001 Regulatory Basis (this volume)
- STK-003, SYS tier certification classification (details TBD)
- ISS-001 (regulatory research — details TBD)
- The inventory of national regulations, international provisions, and authority guidance itself — to be verified from authoritative sources. This document is structured according to general regulatory-inventory practice; no compliance with any regulation or standard is claimed at this revision.

## 4. Definitions & Acronyms

- Regulation inventory: the controlled list of candidate regulations and guidance with source, version, and status (content TBD).
- Applicability assessment: the recorded determination of whether each inventoried item applies, with rationale (method TBD).
- Update rule: the defined handling of new, amended, or superseded regulatory material.
- TBD/TBC: unknown-data markers only.

## 5. System Context

The inventory is the working store between basis research and compliance:

```text
REGULATORY BASIS (25.2) → INVENTORY + APPLICABILITY (25.3)
  → AIRWORTHINESS REQUIREMENTS (25.4) + COMPLIANCE MATRIX (25.10)
  → AUTHORITY ENGAGEMENT (25.11) + EVIDENCE (25.12)
```

Inventory entries feed requirements derivation and the compliance matrix; updates propagate by change control.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-QAR-001 | The programme shall maintain a controlled inventory of candidate aviation regulations and guidance, populated solely from authoritative sources, with each entry to be verified from authoritative sources. | STK-003, ISS-001 | Inspection |
| REQ-HFPX-QAR-002 | The programme shall assess and record the applicability of each inventoried regulation, with method and rationale TBD. | STK-003, ISS-001 | Inspection |
| REQ-HFPX-QAR-003 | The programme shall define and follow an update rule for incorporating new or amended regulatory material obtained from authoritative sources, with detail to be verified from authoritative sources. | STK-003, ISS-001 | Inspection |
| REQ-HFPX-QAR-004 | The programme shall cite no regulation paragraph from memory; every regulatory reference shall trace to a captured authoritative source. | STK-003, ISS-001 | Inspection |

Structured according to general requirements practice; no compliance with any regulation or standard is claimed.

## 7. Architecture

Inventory architecture (structure only): source capture → inventory record (source, version, date, status) → applicability disposition → linkage to airworthiness requirements and compliance-matrix rows → change-driven update cycle. Schema and tooling TBD. All regulatory entries TBD — to be verified from authoritative sources.

## 8. Detailed Design

Detail TBD, including: inventory fields and status values; applicability categories and rationale format; review and approval workflow; update-check cadence and responsibility (TBD); and linkage mechanics to Vol 25.4 and Vol 25.10. No regulation names, numbers, or paragraphs are stated at this revision.

## 9. Interfaces

- Certification ↔ authority (TBD — to be verified from authoritative sources) for clarification of applicability.
- Certification ↔ SE/RTM, Safety, V&V, Test, Quality for disposition impacts.
- Records/configuration interfaces per programme practice (TBD).

## 10. Operational Concept

Operate the inventory as a living controlled list: add only from authoritative sources → assess applicability → link to requirements and matrix → review at gates → apply update rule when sources change → re-assess affected items. Memory-based or secondary-source entries are never added.

## 11. Safety

Mis-inventoried or stale regulations risk missed safety obligations. Control: source-only capture plus update rule and gate review; flight safety itself remains under Vol 13/24 and FRR. Any safety-related regulation or standard is TBD — to be verified from authoritative sources. Structured according to general safety-governance practice; no compliance claimed.

## 12. Performance

Inventory health measures TBD (examples: source-capture completeness, applicability-disposition closure — thresholds TBD, none baselined).

## 13. Verification & Validation

This document is verified by inspection against the template and review checklist (criteria TBD). Validation is programme-authority approval. Inventory correctness is verified later by audit of each entry against its authoritative source (to be verified from authoritative sources); not claimed here. Structured according to general V&V practice; no compliance claimed.

## 14. Risks

- Inventory built from memory or secondary summaries → wrong applicability; mitigation: authoritative-source-only rule.
- Update lag after authority amendment (amendment content TBD — to be verified from authoritative sources) → stale basis; mitigation: update rule with ownership.
- Applicability rationale unrecorded → untraceable decisions; mitigation: recorded-rationale requirement.

## 15. Open Issues

ISS-001 (source research). TBD: inventory schema, applicability method, update cadence and ownership, review gates. No paragraph citations appear in this document.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on STK-003 / SYS tier (TBD); ISS-001; HFPX-CERT-RGB-001 (basis research and evidence practice); HFPX-CERT-ATE-001 (authority clarification); programme records/configuration practice.

## 18. Traceability

Parents: STK-003, SYS tier (certification classification), ISS-001. Children: regulation inventory, applicability records, update-rule record; downstream Vol 25.4 requirements and Vol 25.10 matrix rows. RTM: REQ-HFPX-QAR-001..004 → CONCEPT. Regulatory endpoints TBD pending research to be verified from authoritative sources. Structured according to traceability practice; no compliance claimed.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via programme change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 25.3) |
