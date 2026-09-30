# Primary Power

**Document ID:** HFPX-ELE-PRP-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the primary power structure (Chapter 15.2): role, boundaries, operating states, and interfaces. Structure only; no source selection or ratings are made.

## 2. Scope

Covers primary source role and its connection to distribution. Excludes ratings, machine types, drive arrangements, schematics, and power-quality values (all TBD).

## 3. Applicable Documents

- HFPX-ELE-ARC-001 Electrical Architecture (parent structure)
- HFPX-ARC-PWR-001 Power Architecture (SAD PWR view parent)
- HFPX-SYS-REQ-001 SyRS (SYS tier parent)
- Vol 13 Chapter 13.16 (safety hook, TBD)

## 4. Definitions & Acronyms

- Primary power: source role for normal operating states (rating TBD).
- E-SRC: primary source output boundary (definition TBD).

## 5. System Context

Primary power energises the distribution structure during normal states and interfaces with propulsion energy, distribution buses, protection, and control. Degraded and emergency states are covered by auxiliary, battery, and emergency structures.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-EPP-001 | The primary power structure shall define the primary source role and operating-state coverage (ratings TBD). | HFPX-ELE-ARC-001; SAD PWR view; SYS tier | Inspection |
| REQ-HFPX-EPP-002 | The primary power structure shall define the primary source output boundary to distribution (definition TBD). | HFPX-ELE-ARC-001; SAD PWR view | Inspection |
| REQ-HFPX-EPP-003 | The primary power structure shall define primary-source fault and disconnect behaviour structure (details TBD). | HFPX-ELE-ARC-001; Vol 13.16 hook | Analysis |
| REQ-HFPX-EPP-004 | The primary power structure shall define primary-source status and control interface structure (details TBD). | HFPX-ELE-ARC-001; SYS tier | Inspection |

## 7. Architecture

Primary source block (TBD) → E-SRC boundary (TBD) → distribution buses (TBD). Control and status paths to power management (TBD). Redundancy and segregation provisions are TBD. No ratings or topologies stated.

## 8. Detailed Design

Not applicable at this revision. Source selection, sizing, and schematics deferred to later tranches and ICDs. No electrical values stated.

## 9. Interfaces

E-SRC (primary output to distribution), control / status to power management, mechanical / thermal interfaces to host platform. Definitions TBD in ICDs.

## 10. Operational Concept

Primary power supports normal flight and ground states; loss or degradation triggers defined transfer to auxiliary, battery, or emergency structures (logic TBD).

## 11. Safety

Loss-of-primary-power cases and disconnect behaviour feed Vol 13.16 analyses. No safety values stated.

## 12. Performance

Output characteristics, transients, and power-quality budgets are TBD. No values stated.

## 13. Verification & Validation

Verified by inspection (role and boundary coverage) and analysis (fault and transfer concepts). Validated later by integration test. Pass/fail criteria TBD.

## 14. Risks

- Primary-source loss in critical phases; mitigation: transfer and segregation concepts (TBD).
- Interface mismatch to distribution; mitigation: ICD definition (TBD).

## 15. Open Issues

Source selection, ratings, redundancy, transfer logic, and power-quality limits TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on HFPX-ELE-ARC-001, SAD PWR view, propulsion energy trade, distribution structure (Chapter 15.5), and Vol 13.16 safety inputs.

## 18. Traceability

Parents: SYS tier; SAD PWR view (HFPX-ARC-PWR-001); HFPX-ELE-ARC-001. Children: ICDs, V&V cases. RTM: REQ-HFPX-EPP-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Chapter 15.2.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 15.2) |
