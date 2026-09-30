# Power Conversion

**Document ID:** HFPX-ELE-CNV-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the power conversion structure (Chapter 15.6): conversion functions, boundaries, and placement provisions. Structure only; no topology selection or ratings are made.

## 2. Scope

Covers conversion between source and load domains at structural level. Excludes conversion ratios, ratings, topologies, efficiencies, schematics, and power-quality values (all TBD).

## 3. Applicable Documents

- HFPX-ELE-ARC-001 Electrical Architecture (parent structure)
- HFPX-ARC-PWR-001 Power Architecture (SAD PWR view parent)
- HFPX-SYS-REQ-001 SyRS (SYS tier parent)
- Vol 08 Chapter 08.7 / Vol 10 Chapter 10.16 (load hooks, TBD)

## 4. Definitions & Acronyms

- Conversion: structured transformation between power domains (ratio TBD).
- E-CNV: conversion input / output boundary (definition TBD).

## 5. System Context

Conversion interfaces with sources, distribution buses, protection, grounding, thermal environment, and avionics / helmet / sensor loads. It applies across normal, degraded, and emergency states.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-EPC-001 | The conversion structure shall define conversion functions and placement provisions (topology TBD). | HFPX-ELE-ARC-001; SAD PWR view; SYS tier | Inspection |
| REQ-HFPX-EPC-002 | The conversion structure shall define conversion input and output boundaries to distribution and loads (definitions TBD). | HFPX-ELE-ARC-001; SAD PWR view | Inspection |
| REQ-HFPX-EPC-003 | The conversion structure shall define conversion fault and bypass behaviour structure (details TBD). | HFPX-ELE-ARC-001; Vol 13.16 hook | Analysis |
| REQ-HFPX-EPC-004 | The conversion structure shall define conversion status and control interface structure (details TBD). | HFPX-ELE-ARC-001; SYS tier | Inspection |

## 7. Architecture

Source / bus inputs (TBD) → converters (TBD) → regulated outputs to buses and loads (TBD), with bypass provisions (TBD) and control / status paths (TBD). Redundancy and segregation provisions are TBD. No ratings or topologies stated.

## 8. Detailed Design

Not applicable at this revision. Converter selection, sizing, and schematics deferred. No electrical values stated.

## 9. Interfaces

E-CNV (input / output boundaries), control / status to power management, thermal interfaces. Definitions TBD in ICDs.

## 10. Operational Concept

Conversion supports defined power states; fault, bypass, and degraded-mode concepts (TBD) preserve designated functions without defining timing values.

## 11. Safety

Loss-of-conversion and bypass cases feed Vol 13.16 analyses. No safety values stated.

## 12. Performance

Regulation, transient, and power-quality allocations are TBD. No values stated.

## 13. Verification & Validation

Verified by inspection (function and boundary coverage) and analysis (fault and bypass concepts). Validated later by integration test. Pass/fail criteria TBD.

## 14. Risks

- Conversion failure propagating to loads; mitigation: bypass and segregation concepts (TBD).
- Thermal interaction; mitigation: installation provisions with thermal review (TBD).

## 15. Open Issues

Conversion topology, ratings, placement, bypass design, and power-quality limits TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on HFPX-ELE-ARC-001, SAD PWR view, distribution structure (Chapter 15.5), load inputs (Vol 08.7 / 10.16), and Vol 13.16 safety inputs.

## 18. Traceability

Parents: SYS tier; SAD PWR view (HFPX-ARC-PWR-001); HFPX-ELE-ARC-001; Vol 08.7 / 10.16 / 13.16 hooks (TBD). Children: ICDs, V&V cases. RTM: REQ-HFPX-EPC-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Chapter 15.6.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 15.6) |
