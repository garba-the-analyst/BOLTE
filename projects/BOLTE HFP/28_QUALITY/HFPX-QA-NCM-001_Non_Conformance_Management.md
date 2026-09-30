# Non-Conformance Management

**Document ID:** HFPX-QA-NCM-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the structure-only non-conformance management approach for HFP-X: how non-conforming articles are identified, segregated, dispositioned, and recorded without uncontrolled use or escape. This document owns Chapter 28.6 and does not set technical values.

## 2. Scope

Covers identification and segregation of suspected and confirmed non-conformances, disposition governance including Material Review Board intent where applicable, and non-conformance records. Includes linkage to corrective actions (HFPX-QA-CRA-001) and to Vol 20 production control. Detailed criteria, board charters, and disposition authorities remain TBD.

## 3. Applicable Documents

- HFPX-QA-QMS-001 Quality Management System
- HFPX-QA-CRA-001 Corrective Actions (TBD)
- HFPX-QA-INP-001 Inspection Plans; HFPX-QA-INC-001, HFPX-QA-IPP-001, HFPX-QA-FIN-001 execution stages (TBD)
- Vol 20 Manufacturing (production control interfaces, TBD)
- Vol 25.8 Certification and quality liaison (TBD)

## 4. Definitions & Acronyms

- Non-conformance: failure to meet defined requirements as established (criteria TBD)
- Segregation: physical or administrative separation preventing uncontrolled use (method TBD)
- MRB: Material Review Board — disposition authority structure (charter TBD)
- Disposition: decision on non-conforming articles such as rework, repair, scrap, or use-as-is equivalents (categories and authorities TBD)
- TBD/TBC: unknown data markers

## 5. System Context

Non-conformance management contains and resolves departures from definition:

```text
DETECTION (28.3 / 28.4 / 28.5) → IDENTIFY + SEGREGATE (28.6) → DISPOSITION (MRB / AUTHORISED PATH, TBD) → RECORDS + CORRECTIVE ACTION LINK (28.7)
```

Containment is immediate; disposition is authorised; recurrence control is handled through corrective actions.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-ZNC-001 | The programme shall define identification and segregation provisions for suspected and confirmed non-conformances, preventing uncontrolled use or progression. Methods remain TBD. | Manufacturing quality classification / Vol 20 control | Demonstration |
| REQ-HFPX-ZNC-002 | The programme shall define disposition governance, including Material Review Board intent, disposition categories, and authorisation. Charter and authorities remain TBD. | Quality classification / Vol 25.8 liaison | Inspection |
| REQ-HFPX-ZNC-003 | Non-conformance management shall maintain linkage to corrective actions so that systemic issues transfer to root-cause and action handling. Linkage criteria remain TBD. | HFPX-QA-CRA-001 / quality improvement classification | Inspection |
| REQ-HFPX-ZNC-004 | Non-conformance management shall generate and retain non-conformance records supporting traceability, disposition evidence, and acceptance linkage. Record content and retention linkage remain TBD. | Quality records classification / Vol 28.11 Traceability | Inspection |

## 7. Architecture

Non-conformance structure (TBD): detection reporting, identification marking, segregation control, disposition review path, rework and re-inspection loop, scrap control, record file. MRB membership, quorum, and authority boundaries remain TBD.

## 8. Detailed Design

To be defined. Intended elements include: reporting form structure (TBD), identification and status marking (TBD), segregation arrangements for each production stage (TBD), disposition category definitions without presupposing outcomes (TBD), authorisation matrix (TBD), re-inspection provisions (TBD), record closure rules (TBD). No thresholds, time values, or acceptance concessions are set in this revision.

## 9. Interfaces

- NCM ↔ detection stages (28.3/28.4/28.5): intake of findings (TBD)
- NCM ↔ HFPX-QA-CRA-001: transfer to corrective action (TBD)
- NCM ↔ Vol 20: production hold, rework execution, scrap handling (TBD)
- NCM ↔ HFPX-QA-TRC-001: affected article and batch linkage (TBD)
- NCM ↔ HFPX-QA-PAC-001: unresolved-item visibility at acceptance (TBD)
- NCM ↔ safety programme: safety-relevant non-conformance escalation (path TBD)

## 10. Operational Concept

Findings are reported, identified, and segregated; contained articles await authorised disposition; dispositioned articles follow the authorised path with re-inspection where applicable; records close only through defined authority. Concession or waiver handling, if any, remains TBD and is not assumed.

## 11. Safety

Non-conformance management protects safety by containing suspect articles and escalating safety-relevant departures through defined channels. Safety classification of non-conformances and containment expectations for safety-critical articles remain TBD. No safety values set in this document.

## 12. Performance

Measures of containment effectiveness and disposition timeliness remain TBD in qualitative form, without targets or thresholds in this revision. No performance values baselined.

## 13. Verification & Validation

This document is verified by inspection against the template checklist. Non-conformance implementation is verified by demonstration of segregation control and by inspection and audit of disposition records (criteria TBD). Validation is programme authority approval (path TBD).

## 14. Risks

- Delayed segregation → inadvertent use or progression; mitigation: identification and segregation provisions per REQ-HFPX-ZNC-001 (TBD)
- Unauthorised disposition → uncontrolled configuration; mitigation: governance per REQ-HFPX-ZNC-002 (TBD)
- NCM disconnected from corrective action → recurrence; mitigation: linkage per REQ-HFPX-ZNC-003 (TBD)
- Incomplete records → unverifiable disposition; mitigation: records per REQ-HFPX-ZNC-004 (TBD)

## 15. Open Issues

- Identification and segregation methods per stage (TBD)
- MRB charter, categories, and authorities (TBD)
- Transfer criteria to corrective actions (TBD)
- Record content and retention linkage (TBD)

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on HFPX-QA-QMS-001, detection stages (28.3/28.4/28.5), Vol 20 production control, and safety input for escalation. Supports HFPX-QA-CRA-001, HFPX-QA-TRC-001, and HFPX-QA-PAC-001.

## 18. Traceability

Parent: manufacturing and quality classification; Vol 20 Manufacturing, Vol 21 interfaces where applicable, Vol 25.8 quality liaison. Children: systemic transfer to HFPX-QA-CRA-001; records to HFPX-QA-TRC-001; visibility to HFPX-QA-PAC-001. RTM: REQ-HFPX-ZNC-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 28.6) |
