# Fleet Management

**Document ID:** HFPX-SUS-FLM-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X fleet management framework for tracking, allocating and sustaining the fielded fleet within the product lifecycle. Owns Chapter 32.3.

## 2. Scope

Covers fleet composition tracking, fleet status, allocation governance and sustainment coordination. Does not set technical values, fleet size or availability figures. Maintenance execution detail is owned elsewhere (Vol 27 hooks).

## 3. Applicable Documents

- HFPX-SUS-PLC-001 Product Lifecycle
- HFPX-SUS-CBL-001 Configuration Baselines
- Vol 24 safety assurance concepts (details TBD)
- Vol 27 support and operations concepts (details TBD)
- Vol 28 configuration and records concepts (details TBD)

## 4. Definitions & Acronyms

- Fleet: the set of fielded product instances under sustainment responsibility
- Fleet status: the recorded configuration and serviceability state of fleet instances
- TBD/TBC: unknown data markers; unknown values are never invented

## 5. System Context

Fleet management links the fielded product to its baselines and records:

```text
FIELDED INSTANCES → FLEET STATUS RECORD → ALLOCATION DECISIONS → SUSTAINMENT ACTIONS
         ↑________ CONFIGURATION BASELINES (32.2) ________↑
         ↑________ SAFETY ASSURANCE (Vol 24) _____________↑
```

Fleet data remains under configuration control and supports safety and support decisions.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-UFM-001 | The fleet management framework shall track the configuration and status of fielded product instances. | Lifecycle phase definition (TBD) | Demonstration |
| REQ-HFPX-UFM-002 | Fleet allocation and rotation decisions shall follow defined governance with recorded rationale. | Vol 27 hooks (TBD) | Inspection |
| REQ-HFPX-UFM-003 | Fleet status records shall be maintained under configuration control with traceability to baselines. | Vol 28 hooks (TBD) | Demonstration |
| REQ-HFPX-UFM-004 | Fleet management actions with safety relevance shall retain alignment with safety assurance. | Vol 24 hooks (TBD) | Inspection |

## 7. Architecture

Fleet management organisation (roles TBD): fleet manager, configuration authority and safety liaison with responsibilities TBD. Tooling and data systems TBD.

## 8. Detailed Design

Fleet tracking data model, status categories, allocation workflow and reporting outputs to be defined (TBD). No categories, criteria or values are baselined at this revision.

## 9. Interfaces

- Fleet ↔ configuration baselines (32.2) for authorised configuration reference
- Fleet ↔ operational data (32.4) for status inputs
- Fleet ↔ safety (Vol 24) and support (Vol 27) for constrained decisions
- Fleet ↔ records (Vol 28) for retention and audit

## 10. Operational Concept

Fleet management operates as a control loop: record status → assess needs → allocate → direct sustainment → update records. Forums and cadence TBD.

## 11. Safety

Fleet decisions affecting airworthiness or safety status require defined safety concurrence (mechanisms TBD, Vol 24 hooks). No safety thresholds are set in this document.

## 12. Performance

Fleet management indicators TBD (record currency criteria TBD, allocation traceability criteria TBD). No thresholds baselined.

## 13. Verification & Validation

This document is verified by inspection against the document template checklist (header, 20 sections, IDs, traceability). Requirements REQ-HFPX-UFM-001..004 verified per §6. Validation: programme authority approval (TBD).

## 14. Risks

- Stale fleet status → misinformed allocation; mitigation: record currency controls (TBD)
- Baseline/fleet divergence → unsupported configurations; mitigation: baseline traceability (TBD)
- Uncoordinated sustainment tasking → fleet disruption; mitigation: governance workflow (TBD)

## 15. Open Issues

Fleet data model, governance workflow, tooling and Vol 27 execution interfaces to be defined. All open details recorded as TBD.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on product lifecycle (32.1), configuration baselines (32.2), operational data (32.4), Vol 24 safety assurance, Vol 27 support concepts and Vol 28 records.

## 18. Traceability

Parent: lifecycle phase definition, Vol 24 / Vol 27 / Vol 28 hooks. Children: sustainment tasking fed by fleet status (TBD). RTM: REQ-HFPX-UFM-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 32.3) |
