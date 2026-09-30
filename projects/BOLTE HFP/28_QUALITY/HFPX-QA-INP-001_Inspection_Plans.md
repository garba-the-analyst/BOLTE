# Inspection Plans

**Document ID:** HFPX-QA-INP-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define how HFP-X inspection activities are planned across incoming, in-process, and final stages so that inspection coverage, sequencing, responsibilities, and records are defined before production. This document owns Chapter 28.2 and does not set technical values.

## 2. Scope

Covers inspection planning structure, linkage from design and manufacturing definition to inspection points, and coordination with HFPX-QA-INC-001, HFPX-QA-IPP-001, and HFPX-QA-FIN-001. Excludes detailed inspection methods, acceptance criteria values, and sampling provisions, all of which remain TBD. Applies to production articles governed by Vol 20; interfaces to Vol 21 and Vol 25.8 where applicable (details TBD).

## 3. Applicable Documents

- HFPX-QA-QMS-001 Quality Management System
- HFPX-QA-INC-001 Incoming Inspection, HFPX-QA-IPP-001 In-Process Inspection, HFPX-QA-FIN-001 Final Inspection (all structure-only, TBD)
- Vol 20 Manufacturing (process and work-instruction interfaces, TBD)
- Vol 22 V&V interfaces (independence and evidence linkage, TBD)
- Vol 25.8 Certification and quality liaison (TBD)

## 4. Definitions & Acronyms

- Inspection plan: defined set of inspection points, characteristics, methods, responsibilities, and records for an article or process
- Inspection point: planned hold, witness, or verification step within the production flow (details TBD)
- Characteristic: feature or attribute subject to inspection (list TBD)
- TBD/TBC: unknown data markers

## 5. System Context

Inspection planning translates design and process definition into verifiable production control:

```text
DESIGN / MANUFACTURING DEFINITION (Vol 20) → INSPECTION PLANS (28.2) → EXECUTION (28.3 / 28.4 / 28.5)
                                                        ↓
                                              RECORDS + TRACEABILITY (28.11) + ACCEPTANCE (28.12)
```

Plans do not themselves accept hardware; acceptance is governed in HFPX-QA-PAC-001.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-ZIP-001 | The programme shall define inspection plans that identify inspection points, characteristics to be inspected, methods, responsibilities, and required records. Plan contents remain TBD. | Vol 20 Manufacturing definition / manufacturing quality classification | Inspection |
| REQ-HFPX-ZIP-002 | Inspection plans shall maintain traceability from design and manufacturing definition to inspection points, so that coverage can be assessed. Traceability mechanism remains TBD. | Vol 20 design-to-production linkage | Inspection |
| REQ-HFPX-ZIP-003 | Inspection plans shall define sequencing relative to the production flow, including coordination of incoming, in-process, and final inspection. Sequencing details remain TBD. | Vol 20 production flow | Inspection |
| REQ-HFPX-ZIP-004 | Inspection plans shall define inspection records to be retained and their linkage to traceability and acceptance. Record types and retention linkage remain TBD. | Vol 28.11 Traceability / quality records classification | Inspection |

## 7. Architecture

Inspection planning hierarchy (TBD): plan header and approval, article and revision applicability, characteristic list linkage, method references, responsibility assignments, record references. Ownership of plan authorship, review, and approval remains TBD. No methods or coverage values baselined.

## 8. Detailed Design

To be defined. Intended elements include: plan template structure (TBD), characteristic selection logic (TBD, qualitative only), method assignment approach without prescribing values (TBD), responsibility matrix (TBD), linkage to work instructions (TBD), change control for plans (TBD). No sampling rates, coverage percentages, or acceptance thresholds are set in this revision.

## 9. Interfaces

- Plans ↔ Vol 20: source design characteristics, process steps, work instructions (TBD)
- Plans ↔ HFPX-QA-INC-001 / IPP-001 / FIN-001: execution procedures for each stage (TBD)
- Plans ↔ HFPX-QA-TRC-001: record-to-article linkage (TBD)
- Plans ↔ HFPX-QA-PAC-001: evidence supporting acceptance (TBD)
- Plans ↔ HFPX-QA-CCB-001: control of plan revisions with production configuration (TBD)

## 10. Operational Concept

Plans are authored from released design and process definition, reviewed and approved, released to production, executed at defined points, and revised only through configuration control. Planning cadence relative to design release and production readiness remains TBD.

## 11. Safety

Inspection planning supports safety by ensuring safety-relevant characteristics are identified for inspection through liaison with the safety programme. Classification of safety-relevant characteristics and any independent inspection provisions remain TBD. No safety values set in this document.

## 12. Performance

Measures of planning completeness and coverage assessment remain TBD, without targets or thresholds in this revision. No performance values baselined.

## 13. Verification & Validation

This document is verified by inspection against the template checklist. Inspection plans are verified by inspection for completeness and traceability (criteria TBD). Validation that plans reflect design intent follows programme approval (path TBD).

## 14. Risks

- Incomplete traceability from design to inspection → unverified characteristics; mitigation: traceability structure per REQ-HFPX-ZIP-002 (TBD)
- Plan-to-flow mismatch → inspection points unreachable or bypassed; mitigation: sequencing linkage per REQ-HFPX-ZIP-003 (TBD)
- Records disconnected from plans → unverifiable execution; mitigation: record linkage per REQ-HFPX-ZIP-004 (TBD)

## 15. Open Issues

- Plan template and approval path (TBD)
- Characteristic selection and traceability mechanism (TBD)
- Sequencing rules relative to Vol 20 flow (TBD)
- Record set and retention linkage (TBD)

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on Vol 20 (design and process definition, flow), HFPX-QA-QMS-001 (QMS framework), and safety input for safety-relevant characteristics. Supports HFPX-QA-INC-001, HFPX-QA-IPP-001, HFPX-QA-FIN-001, HFPX-QA-TRC-001, and HFPX-QA-PAC-001.

## 18. Traceability

Parent: manufacturing and quality classification; Vol 20 Manufacturing, Vol 25.8 quality liaison. Children: execution in HFPX-QA-INC-001, HFPX-QA-IPP-001, HFPX-QA-FIN-001; evidence to HFPX-QA-TRC-001 and HFPX-QA-PAC-001. RTM: REQ-HFPX-ZIP-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 28.2) |
