# Experimental Data

**Document ID:** HFPX-MVP-EXD-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined; Vol 33 separate from production  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the planning framework for MVP experimental data, including how data inventory, quality/retention methodology, and model-validation feed are specified and controlled. Owns Chapter 33.16.

This document is planning/methodology only. It does not contain test-execution or flight-execution instructions.

## 2. Scope

Covers planning for identification, quality assessment, retention, and downstream use of data produced by ground-test (33.13), unmanned-test (33.14), and transition-demonstration (33.15) activities. Excludes execution-level acquisition procedures, instrumentation build (33.12), and production data-system decisions (governed by 33.20 transition).

Gated progression is mandatory (DDR-001): no stage shall be skipped; human-proximate stages require prior unmanned evidence plus authorisation TBD; data gaps do not justify gate bypass.

## 3. Applicable Documents

- DDR-001 (unmanned-first); HFPX-MVP-OBJ-001 (Chapter 33.1, MVP-001..MVP-005, including MVP-002 data objective)
- Future: 33.2 MVP requirements, 33.3 MVP architecture, 33.12 test instrumentation, 33.13/33.14/33.15 evidence sources, 33.19 exit criteria, 33.20 transition
- Vol 19 modelling, including Vol 19.15 validation-feed hooks (TBD); Vol 23 test programme, including Vol 23.17 hooks (TBD); Vol 13 safety; Vol 22 V&V (production, separate)

## 4. Definitions & Acronyms

- MVP: Minimum Viable Prototype — smallest system that retires the load-bearing risks (ISS-006/007/008)
- Experimental data: planned data sets produced by MVP ground and unmanned activities for model validation, exit evidence, and lessons inputs
- Data inventory: planned catalogue of data sets, sources, and ownership (details TBD)
- Vol 19.15 hooks: defined interfaces feeding model-validation activities (details TBD)
- Vol 23.17 hooks: defined interfaces to the referenced test-programme volume (details TBD)

## 5. System Context

Experimental data is the evidence backbone linking MVP activities to model validation, exit decisions, and controlled transition:

```text
33.13 GROUND + 33.14 UNMANNED + 33.15 DEMO ── evidence ──► EXPERIMENTAL DATA (33.16) ── feed ──► Vol 19 VALIDATION / 33.19 EXIT / 33.17 LESSONS
                                                              │
                                                              └──── lessons/data only ──► PRODUCTION BASELINE via 33.20 gate ──► (no auto-promotion per MVP-005)
```

> This volume is SEPARATE from the production-aircraft documentation. Production-design transition is governed by 33.20.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-MED-001 | The experimental-data plan shall define the data inventory covering scoped ground and unmanned sources (inventory TBD). | MVP-002; MRQ/MAR tier; VVP thread | Inspection |
|REQ-HFPX-MED-002|The experimental-data plan shall define data quality and retention methodology (methodology TBD).|MVP-002; MRQ/MAR tier; VVP thread|Inspection|
|REQ-HFPX-MED-003|The experimental-data plan shall define the model-validation feed methodology with hooks to Vol 19.15 (feed TBD).|MVP-002; MRQ/MAR tier; VVP thread|Inspection|
|REQ-HFPX-MED-004|The experimental-data plan shall define interface hooks to Vol 23.17 for applicable evidence exchange (hooks TBD).|MVP-004; MRQ/MAR tier; VVP thread|Inspection|

Gated progression applies to all requirements above: no stage skipped; human-proximate stages require prior unmanned evidence plus authorisation TBD.

## 7. Architecture

Experimental-data architecture (planning view, TBD): inventory structure, quality/retention framework, validation-feed chain, storage and access methodology. Instrumentation sourcing is 33.12 (TBD). No acquisition hardware configuration or execution-level handling is defined in this document.

## 8. Detailed Design

Not applicable — instrumentation detail is 33.12 (TBD); prototype configuration is 33.4 (TBD). This document defines only the planning artefacts and methodology to be produced.

## 9. Interfaces

Planning interfaces: MVP requirements (33.2), test instrumentation planning (33.12), ground/unmanned/demonstration planning (33.13/33.14/33.15), lessons-learned planning (33.17), exit-criteria planning (33.19), Vol 19.15 validation-feed interfaces (TBD), Vol 23.17 test-programme interfaces (TBD), production baseline via 33.20 data/decision handover only.

## 10. Operational Concept

Gated progression governs data use: each gate consumes defined data sets with defined quality attributes (all TBD in the data plan); incomplete or unqualified data does not advance a gate. Human-proximate stages require prior unmanned evidence plus authorisation TBD. Execution-level acquisition, handling, and processing instructions are excluded.

## 11. Safety

Experimental-data planning supports safety assessment by providing defined evidence inputs to prototype safety planning (33.11) and Vol 13 analyses; it does not itself authorise activity progression. Hazardous-subsystem boundary applies: this document covers requirements, planning methodology, interfaces, and safety-analysis inputs only — no build, operation, test-execution, or flight-execution instructions.

## 12. Performance

No performance targets are set in this document. Data-completeness and data-quality thresholds are TBD and linked to MVP exit criteria (33.19, TBD). No quantitative completeness, rate, resolution, or retention figure is stated.

## 13. Verification & Validation

This planning document is verified by inspection/review of the data-plan artefacts (inventory, quality/retention methodology, Vol 19.15 feed definition, Vol 23.17 hook definitions). Fitness of delivered data sets for validation and exit purposes is assessed separately under the defined methodology; MVP data does not equal production verification evidence (Vol 22, separate).

## 14. Risks

- Undefined inventory → missing evidence at gates; mitigation: inventory-definition requirement (REQ-HFPX-MED-001)
- Undefined quality/retention → unusable or lost evidence; mitigation: quality/retention methodology (REQ-HFPX-MED-002)
- Undefined validation feed → models remain unvalidated; mitigation: explicit Vol 19.15 feed methodology (REQ-HFPX-MED-003)
- Unmanaged Vol 23.17 dependencies → evidence-exchange gaps; mitigation: explicit hook definitions (REQ-HFPX-MED-004)

## 15. Open Issues

Data inventory TBD; quality/retention methodology TBD; model-validation feed TBD (Vol 19.15 hooks TBD); Vol 23.17 hooks TBD. Linked TBDs: instrumentation coverage (33.12), gate evidence needs (33.13/33.14/33.15), exit-evidence needs (33.19).

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on MVP requirements (33.2), test instrumentation planning (33.12), ground/unmanned/demonstration evidence planning (33.13/33.14/33.15), Vol 19 modelling needs (including Vol 19.15), Vol 23 test-programme capability (including Vol 23.17), and data-governance inputs (TBD).

## 18. Traceability

Parent: MVP-001..MVP-005 (HFPX-MVP-OBJ-001, principally MVP-002); MRQ/MAR tier; VVP thread. Children: experimental-data plan artefacts, validation-feed inputs to Vol 19, exit-evidence inputs to 33.19, lessons inputs to 33.17, handover inputs to 33.20. RTM: REQ-HFPX-MED-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined; Vol 33 items never auto-promote to production baselines (MVP-005, 33.20 gate applies).

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 33.16) |
