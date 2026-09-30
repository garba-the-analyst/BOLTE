# In-Process Inspection

**Document ID:** HFPX-QA-IPP-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the structure-only in-process inspection approach for HFP-X: how conformance is verified during production, how inspection integrates with the manufacturing flow, and how records support control and traceability. This document owns Chapter 28.4 and does not set technical values.

## 2. Scope

Covers verification performed between operations and at defined points within the Vol 20 production flow. Includes coordination with inspection plans, work instructions, configuration control, and non-conformance routing. Detailed methods, acceptance criteria values, and process controls remain TBD.

## 3. Applicable Documents

- HFPX-QA-QMS-001 Quality Management System
- HFPX-QA-INP-001 Inspection Plans
- HFPX-QA-NCM-001 Non-Conformance Management (TBD)
- HFPX-QA-CCB-001 Configuration Control (TBD)
- Vol 20 Manufacturing (process flow and work instructions, TBD)
- Vol 25.8 Certification and quality liaison (TBD)

## 4. Definitions & Acronyms

- In-process inspection: verification performed during production, between or within operations
- Hold and witness points: flow positions where production pauses or proceeds under observation as defined (details TBD)
- Work instruction: production instruction governing an operation (content TBD)
- TBD/TBC: unknown data markers

## 5. System Context

In-process inspection is embedded in the manufacturing flow:

```text
OPERATION → IN-PROCESS INSPECTION (28.4) → NEXT OPERATION / FINAL INSPECTION (28.5)
                    ↓
         NON-CONFORMANCE (28.6) / RECORDS + TRACEABILITY (28.11)
```

Inspection planning (28.2) defines what is verified; this document governs how in-process verification is executed and controlled.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-ZPI-001 | The programme shall define in-process inspection scope, responsibilities, and placement relative to the Vol 20 production flow. Details remain TBD. | Vol 20 production flow / manufacturing quality classification | Inspection |
| REQ-HFPX-ZPI-002 | In-process inspection shall be performed per inspection plans and applicable work instructions, with defined handling of holds and progression. Details remain TBD. | HFPX-QA-INP-001 / Vol 20 work instructions | Inspection |
| REQ-HFPX-ZPI-003 | In-process inspection shall control progression of non-conforming work, routing affected articles to non-conformance management without uncontrolled continuation. Routing details remain TBD. | Quality classification / HFPX-QA-NCM-001 | Demonstration |
| REQ-HFPX-ZPI-004 | In-process inspection shall generate records supporting traceability, configuration status, and acceptance evidence. Record types and retention linkage remain TBD. | Quality records classification / Vol 28.11 Traceability | Inspection |

## 7. Architecture

In-process inspection structure (TBD): flow-integrated inspection points, responsibility assignments per operation, status identification, hold and progression control, record capture. Independence of inspection personnel where required remains TBD.

## 8. Detailed Design

To be defined. Intended elements include: point placement logic (TBD, qualitative), hold and witness definitions (TBD), operator and inspector responsibility split (TBD), status marking approach (TBD), linkage to configuration status (TBD), rework and re-inspection routing (TBD). No sampling provisions, thresholds, or process values are set in this revision.

## 9. Interfaces

- In-process ↔ Vol 20: flow, operations, work instructions, tooling (TBD)
- In-process ↔ HFPX-QA-INP-001: plan content executed at each point (TBD)
- In-process ↔ HFPX-QA-NCM-001: non-conforming work routing (TBD)
- In-process ↔ HFPX-QA-CCB-001: configuration alignment of inspected state (TBD)
- In-process ↔ HFPX-QA-TRC-001: operation-to-record linkage (TBD)

## 10. Operational Concept

Articles progress operation by operation with verification at defined points; conforming work proceeds, non-conforming work is identified and routed without uncontrolled progression. Bypass, rework, and re-inspection provisions, if any, remain TBD and are defined only through controlled documentation.

## 11. Safety

In-process inspection supports safety by detecting non-conformance before further value is added or concealment occurs. Safety-relevant operations requiring additional control or independence remain TBD in liaison with the safety programme. No safety values set in this document.

## 12. Performance

Measures of in-process detection effectiveness and record completeness remain TBD, without targets or thresholds in this revision. No performance values baselined.

## 13. Verification & Validation

This document is verified by inspection against the template checklist. In-process inspection implementation is verified by inspection and audit of flow compliance and records (criteria TBD). Validation is programme authority approval (path TBD).

## 14. Risks

- Inspection points misaligned to flow → bypass or concealment; mitigation: placement linkage per REQ-HFPX-ZPI-001 (TBD)
- Uncontrolled progression of suspect work → expanded impact; mitigation: routing control per REQ-HFPX-ZPI-003 (TBD)
- Records disconnected from operations → unverifiable build state; mitigation: record linkage per REQ-HFPX-ZPI-004 (TBD)

## 15. Open Issues

- Scope, responsibilities, and flow placement (TBD)
- Hold and progression rules (TBD)
- Non-conforming work routing details (TBD)
- Record set and retention linkage (TBD)

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on Vol 20 (flow and work instructions), HFPX-QA-INP-001 (plans), HFPX-QA-QMS-001 (framework). Supports HFPX-QA-FIN-001, HFPX-QA-NCM-001, HFPX-QA-TRC-001, and HFPX-QA-PAC-001.

## 18. Traceability

Parent: manufacturing and quality classification; Vol 20 Manufacturing, Vol 25.8 quality liaison. Children: findings to HFPX-QA-NCM-001; records to HFPX-QA-TRC-001; evidence to HFPX-QA-PAC-001. RTM: REQ-HFPX-ZPI-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 28.4) |
