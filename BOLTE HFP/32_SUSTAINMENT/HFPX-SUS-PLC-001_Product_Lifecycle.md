# Product Lifecycle

**Document ID:** HFPX-SUS-PLC-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X product lifecycle framework that organises development, production, operation, sustainment and retirement into controlled phases with governed transitions. Owns Chapter 32.1.

## 2. Scope

Covers lifecycle phase definition, phase transition governance, sustainment alignment and retirement linkage for the HFP-X product. Does not set technical values, schedules or quantities. Detailed sustainment disciplines are owned by Chapters 32.2 through 32.11.

## 3. Applicable Documents

- HFPX-PGM-SEM-001 SEMP (programme lifecycle and gates)
- Vol 24 safety and assurance concepts (details TBD)
- Vol 27 support and operations concepts (details TBD)
- Vol 28 configuration and records concepts (details TBD)

## 4. Definitions & Acronyms

- Lifecycle phase: a bounded stage of the product life with defined entry and exit criteria
- Sustainment: post-delivery activities that keep the product supportable, safe and available
- TBD/TBC: unknown data markers; unknown values are never invented

## 5. System Context

The product lifecycle sits above the sustainment disciplines:

```text
DEVELOPMENT → PRODUCTION → OPERATION → SUSTAINMENT → RETIREMENT
       ↑________ TRACEABILITY AND CONFIGURATION CONTROL ________↑
       ↑________ SAFETY ASSURANCE (Vol 24) ____________________↑
```

Phase transitions are gated and recorded. Sustainment feeds operational experience back into design authority.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-UPL-001 | The product lifecycle shall define lifecycle phases spanning development, production, operation, sustainment and retirement. | Programme lifecycle, HFPX-PGM-SEM-001 | Inspection |
| REQ-HFPX-UPL-002 | Lifecycle phase transitions shall be governed by defined entry criteria, exit criteria and approval authority. | Lifecycle phase definition (TBD) | Inspection |
| REQ-HFPX-UPL-003 | Sustainment activities within the lifecycle shall remain aligned with safety assurance and support concepts. | Vol 24 / Vol 27 hooks (TBD) | Inspection |
| REQ-HFPX-UPL-004 | Lifecycle phase status and associated lifecycle records shall be maintained under configuration control. | Vol 28 hooks (TBD) | Demonstration |

## 7. Architecture

Lifecycle governance structure (roles TBD): design authority, sustainment authority and safety authority with defined responsibilities for phase ownership and transition approval. Structure aligns with programme organisation (details TBD).

## 8. Detailed Design

Lifecycle phases and transition artefacts to be defined (TBD): phase descriptions, entrance artefacts, exit evidence, decision records and linkage to programme gates. No criteria are baselined at this revision.

## 9. Interfaces

- Lifecycle ↔ configuration management (Chapters 32.2, Vol 28) for phase status and baseline linkage
- Lifecycle ↔ safety assurance (Vol 24) for continued safety across phases
- Lifecycle ↔ support and operations (Vol 27) for sustainment alignment

## 10. Operational Concept

The lifecycle operates as the product control frame: define phases → assign ownership → govern transitions → sustain the fielded product → retire. Cadence and review forums TBD.

## 11. Safety

Lifecycle transitions shall not compromise safety; safety concurrence for phase progression is required with mechanisms TBD (Vol 24 hooks). No safety thresholds are set in this document.

## 12. Performance

Lifecycle performance indicators TBD (phase transition timeliness criteria TBD, record completeness criteria TBD). No thresholds baselined.

## 13. Verification & Validation

This document is verified by inspection against the document template checklist (header, 20 sections, IDs, traceability). Requirements REQ-HFPX-UPL-001..004 verified per §6. Validation: programme authority approval (TBD).

## 14. Risks

- Undefined phase criteria → ungated transitions; mitigation: define entry/exit criteria before baselining (TBD)
- Lifecycle/sustainment disconnect → unsupported fielded product; mitigation: alignment with Vol 27 concepts (TBD)
- Record gaps across phases → loss of configuration truth; mitigation: Vol 28 records linkage (TBD)

## 15. Open Issues

Lifecycle phase criteria, ownership assignments and gate linkages to be defined. All open details recorded as TBD.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SEMP lifecycle and gate definitions, Vol 24 safety assurance concepts, Vol 27 support concepts and Vol 28 configuration and records concepts.

## 18. Traceability

Parent: programme lifecycle (HFPX-PGM-SEM-001), Vol 24 / Vol 27 / Vol 28 hooks. Children: Chapters 32.2 through 32.11 sustainment disciplines. RTM: REQ-HFPX-UPL-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 32.1) |
