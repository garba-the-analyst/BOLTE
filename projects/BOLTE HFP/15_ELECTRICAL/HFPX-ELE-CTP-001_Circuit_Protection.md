# Circuit Protection

**Document ID:** HFPX-ELE-CTP-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the circuit protection structure (Chapter 15.7): fault-interruption functions, coordination provisions, and boundaries. Structure only; no device selection or settings are made.

## 2. Scope

Covers protection of sources, buses, feeders, converters, and load feeds at structural level. Excludes trip settings, device ratings, wire protection sizing, schematics, and fault-level values (all TBD).

## 3. Applicable Documents

- HFPX-ELE-ARC-001 Electrical Architecture (parent structure)
- HFPX-ARC-PWR-001 Power Architecture (SAD PWR view parent)
- HFPX-SYS-REQ-001 SyRS (SYS tier parent)
- Vol 13 Chapter 13.16 (safety hook, TBD)

## 4. Definitions & Acronyms

- Protection: structured fault detection and interruption function (setting TBD).
- Selectivity: structured coordination of protection operation order (details TBD).
- E-PROT: protection coordination boundary (definition TBD).

## 5. System Context

Protection interfaces with sources, distribution, conversion, grounding, and load feeds. It contains faults and preserves designated functions across normal, degraded, and emergency states.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-ECP-001 | The protection structure shall define fault-interruption functions for sources, buses, and feeders (settings TBD). | HFPX-ELE-ARC-001; SAD PWR view; SYS tier | Inspection |
| REQ-HFPX-ECP-002 | The protection structure shall define selectivity provisions across protection boundaries (details TBD). | HFPX-ELE-ARC-001; SAD PWR view | Analysis |
| REQ-HFPX-ECP-003 | The protection structure shall define protection status and reset behaviour structure (details TBD). | HFPX-ELE-ARC-001; SYS tier | Inspection |
| REQ-HFPX-ECP-004 | The protection structure shall define protection safety hooks to Vol 13.16 analyses (details TBD). | HFPX-ELE-ARC-001; Vol 13.16 hook | Inspection |

## 7. Architecture

Fault detection blocks (TBD) → interruption devices (TBD) coordinated across E-PROT boundaries (TBD), with status paths to power management (TBD). Placement provisions across buses, feeders, and load interfaces are TBD. No ratings, settings, or schematics stated.

## 8. Detailed Design

Not applicable at this revision. Device selection, settings, and schematics deferred. No electrical values stated.

## 9. Interfaces

E-PROT (coordination boundaries), status / reset to power management and crew interfaces, mechanical interfaces to distribution hardware. Definitions TBD in ICDs.

## 10. Operational Concept

Protection operates automatically on defined fault conditions (TBD); reset and reconfiguration concepts (TBD) align with normal, degraded, and emergency states.

## 11. Safety

Undetected faults, nuisance trips, and loss-of-protection cases feed Vol 13.16 analyses. No safety values stated.

## 12. Performance

Fault-clearing behaviour and power-quality interaction are TBD. No values stated.

## 13. Verification & Validation

Verified by inspection (function coverage) and analysis (selectivity concepts). Validated later by integration and fault test. Pass/fail criteria TBD.

## 14. Risks

- Uncoordinated trips removing designated functions; mitigation: selectivity analysis (TBD).
- Device and setting uncertainty; mitigation: selection deferred with test gating (TBD).

## 15. Open Issues

Device selection, settings, placement, selectivity implementation, and reset provisions TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on HFPX-ELE-ARC-001, SAD PWR view, distribution structure (Chapter 15.5), conversion structure (Chapter 15.6), and Vol 13.16 safety inputs.

## 18. Traceability

Parents: SYS tier; SAD PWR view (HFPX-ARC-PWR-001); HFPX-ELE-ARC-001; Vol 13.16 hook (TBD). Children: ICDs, V&V cases. RTM: REQ-HFPX-ECP-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Chapter 15.7.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 15.7) |
