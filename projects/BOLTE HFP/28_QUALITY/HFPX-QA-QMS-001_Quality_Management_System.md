# Quality Management System

**Document ID:** HFPX-QA-QMS-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the structure-only Quality Management System for HFP-X production: scope, policy intent, management review intent, document control linkage, and audit-based verification intent. This document owns Chapter 28.1 and does not set technical values.

## 2. Scope

Covers the QMS framework applicable to HFP-X manufacturing and quality activities linked to Vol 20 (Manufacturing), Vol 21 (support and sustainment interfaces where applicable), and Vol 25.8 (quality and certification liaison). Excludes detailed procedures, forms, and quantitative controls, all of which remain TBD. Quantitative scope boundaries, exclusions, and applicability per site or phase remain TBD.

## 3. Applicable Documents

- HFPX-PGM-CHR-001 Programme Charter (authority, TBD)
- HFPX-PGM-SEM-001 SEMP (systems engineering process)
- Vol 00.8 Document and Data Control interfaces (details TBD)
- Vol 20 Manufacturing (production system definition, TBD)
- Vol 21 Sustainment interfaces (TBD)
- Vol 25.8 Certification and quality liaison (TBD)
- Standards structured according to: ISO 9001 quality management concepts, ISO/IEC/IEEE 15288 lifecycle concepts; aerospace quality concepts per AS9100 family where applicable (applicability TBD, no clauses baselined)

## 4. Definitions & Acronyms

- QMS: Quality Management System
- QR: Quality Record; QMS scope, policy, objectives, review as used in this volume
- MRB: Material Review Board (governed in HFPX-QA-NCM-001, not here)
- TBD/TBC: unknown data markers; unknowns are never presented as facts
- Audit: independent examination against defined criteria (criteria TBD)

## 5. System Context

The QMS sits above production quality activities and connects programme governance to shop-floor control:

```text
PROGRAMME GOVERNANCE (Vol 00) → QMS (Vol 28.1) → INSPECTION / NCM / SUPPLIER / CONFIG / TRACEABILITY (Vol 28.2–28.12)
        ↑                                   ↑                                    ↑
   CERTIFICATION LIAISON (Vol 25.8) ───────┴── MANUFACTURING SYSTEM (Vol 20) ─────┴── SUSTAINMENT (Vol 21)
```

The QMS does not itself perform inspection or disposition; it defines how those activities are planned, controlled, reviewed, and audited.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-ZQS-001 | The QMS shall define its scope, including covered activities, organisations, lifecycle phases, and interfaces to Vol 20, Vol 21, and Vol 25.8. Scope details remain TBD. | Vol 20 Manufacturing system / Vol 25.8 quality liaison | Inspection |
| REQ-HFPX-ZQS-002 | The programme shall define a quality policy that states quality intent, commitment to compliance, and commitment to continual improvement. Policy text remains TBD. | Programme quality classification / Vol 25.8 | Inspection |
| REQ-HFPX-ZQS-003 | The programme shall conduct management review of the QMS, addressing suitability, adequacy, and improvement needs. Review inputs, cadence, participants, and outputs remain TBD. | Programme governance / Vol 00 management review interfaces | Inspection |
| REQ-HFPX-ZQS-004 | The QMS shall control documents and records through hooks to Vol 00.8 document and data control, including identification, review, approval, distribution, revision, and retention linkage. Control details remain TBD. | Vol 00.8 Document control | Inspection |
|REQ-HFPX-ZQS-005|The QMS shall be verified by audit against defined QMS criteria. Audit scope, criteria, auditor independence, and cadence remain TBD.|Vol 25.8 assurance / Vol 22 V&V interfaces|Inspection|

## 7. Architecture

QMS structure (all details TBD): quality manual intent (this volume set), procedure layer (inspection, non-conformance, corrective action, supplier, configuration, serialisation, traceability, acceptance), record layer (quality records defined in each child document). Roles — Quality owner, production owner, independent audit function — remain TBD. No organisational values baselined.

## 8. Detailed Design

To be defined. Intended elements include: QMS scope statement (TBD), quality policy statement (TBD), quality objectives framework (TBD, no targets baselined), process interaction description (TBD), documented-information structure linked to Vol 00.8 (TBD), management-review agenda and record structure (TBD), internal audit structure (TBD). No sampling rates, acceptance thresholds, or performance targets are set in this revision.

## 9. Interfaces

- QMS ↔ Vol 00.8: document control, record retention, approval workflows (details TBD)
- QMS ↔ Vol 20: manufacturing processes subject to QMS control (details TBD)
- QMS ↔ Vol 28.2–28.12: child procedures implementing QMS intent (inspection, NCM, corrective action, supplier, configuration, serialisation, traceability, acceptance)
- QMS ↔ Vol 25.8: certification liaison and regulatory quality expectations (TBD)
- QMS ↔ Vol 22: V&V independence interfaces where applicable (TBD)

## 10. Operational Concept

The QMS operates as a governance loop: define scope and policy → plan quality activities in child documents → execute production under control → inspect and record → manage non-conformances and corrective actions → review suitability → audit → improve. Review and audit cadence, escalation paths, and meeting structures remain TBD.

## 11. Safety

The QMS supports safety by ensuring production conforms to defined configuration and that non-conformances affecting safety are identified, segregated, and dispositioned through defined channels (see HFPX-QA-NCM-001). Safety classification of quality escapes and liaison to the safety programme remain TBD. No safety values set in this document.

## 12. Performance

QMS performance indicators remain TBD (candidate areas: audit finding closure, document control health, management-review action closure — all without targets or thresholds in this revision). No targets, thresholds, or baselines are established.

## 13. Verification & Validation

This document is verified by inspection against the document template checklist (header, full sections, requirement IDs, traceability). QMS implementation is verified by audit per REQ-HFPX-ZQS-005 (criteria and scope TBD). Validation is programme authority approval of scope and policy (path TBD).

## 14. Risks

- Scope ambiguity: undefined QMS boundaries → gaps or overlap with Vol 20/21; mitigation: scope definition tied to REQ-HFPX-ZQS-001 (TBD)
- Policy without deployment: policy statement not reflected in procedures; mitigation: traceability from policy to child documents (TBD)
- Document control divergence from Vol 00.8 → uncontrolled production information; mitigation: explicit hooks per REQ-HFPX-ZQS-004 (TBD)
- Audit without independence or criteria → ineffective verification; mitigation: audit charter TBD

## 15. Open Issues

- QMS scope statement content and exclusions (TBD)
- Quality policy text and approval path (TBD)
- Management-review inputs, participants, and records (TBD)
- Document control hook details to Vol 00.8 (TBD)
- Audit scope, criteria, independence, and records (TBD)

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on Vol 00.8 (document control), Vol 20 (manufacturing system definition), Vol 25.8 (certification and quality expectations), and programme governance for policy ownership and review authority. Child dependencies: all Vol 28.2–28.12 documents implement QMS intent.

## 18. Traceability

Parent: manufacturing and quality classification; Vol 20 Manufacturing, Vol 21 sustainment interfaces, Vol 25.8 quality liaison. Children: HFPX-QA-INP-001, HFPX-QA-INC-001, HFPX-QA-IPP-001, HFPX-QA-FIN-001, HFPX-QA-NCM-001, HFPX-QA-CRA-001, HFPX-QA-SUQ-001, HFPX-QA-CCB-001, HFPX-QA-SER-001, HFPX-QA-TRC-001, HFPX-QA-PAC-001. RTM: REQ-HFPX-ZQS-001..005 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 28.1) |
