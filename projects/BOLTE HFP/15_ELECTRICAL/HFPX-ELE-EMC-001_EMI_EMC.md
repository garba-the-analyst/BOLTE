# EMI/EMC

**Document ID:** HFPX-ELE-EMC-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the EMI/EMC structure (Chapter 15.13): zoning, bonding, shielding, and verification provisions structured according to established aerospace practice concepts. Structure only; no emission or susceptibility limits or practice selections are made.

## 2. Scope

Covers emission and susceptibility control provisions at structural level, structured according to DO-160 concepts only (application TBD). Excludes limits, test levels, design details, and schematics (all TBD).

## 3. Applicable Documents

- HFPX-ELE-ARC-001 Electrical Architecture (parent structure)
- HFPX-ARC-PWR-001 Power Architecture (SAD PWR view parent)
- HFPX-SYS-REQ-001 SyRS (SYS tier parent)
- Vol 13 Chapter 13.16 (safety hook, TBD)
- DO-160 concepts (structured-according-to only; applicability and levels TBD)

## 4. Definitions & Acronyms

- EMI: electromagnetic interference control provisions (limits TBD).
- EMC: electromagnetic compatibility assurance provisions (levels TBD).
- Zoning: structural allocation of emission and susceptibility provisions (details TBD).

## 5. System Context

EMI/EMC provisions interface with sources, distribution, conversion, grounding, avionics / helmet / sensor feeds, and airframe structure. They apply across all power states and installation states.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-EMC-001 | The EMI/EMC structure shall define emission control provisions structure (practice and limits TBD). | HFPX-ELE-ARC-001; SAD PWR view; SYS tier | Inspection |
| REQ-HFPX-EMC-002 | The EMI/EMC structure shall define susceptibility control provisions structure (practice and levels TBD). | HFPX-ELE-ARC-001; SAD PWR view; SYS tier | Inspection |
| REQ-HFPX-EMC-003 | The EMI/EMC structure shall define zoning, bonding, and shielding provisions structure (details TBD). | HFPX-ELE-ARC-001; SAD PWR view | Analysis |
| REQ-HFPX-EMC-004 | The EMI/EMC structure shall define EMI/EMC verification provisions structured according to DO-160 concepts only (applicability TBD). | HFPX-ELE-ARC-001; SYS tier | Inspection |

## 7. Architecture

Source and load equipment (TBD) → zoning allocations (TBD) → bonding and shielding provisions (TBD) → verification provisions (TBD), coordinated with grounding and segregation structures. No limits, levels, or design details stated.

## 8. Detailed Design

Not applicable at this revision. Filter, shield, routing, and installation design deferred. No electrical values stated.

## 9. Interfaces

E-EMC (zoning / shielding boundaries), interfaces to grounding / bonding, harness routing, and enclosure provisions. Definitions TBD in ICDs.

## 10. Operational Concept

EMI/EMC provisions apply in all operating states; degradation and maintenance provisions (TBD) preserve compatibility without defining measured values.

## 11. Safety

EMI-induced upset and susceptibility-failure cases feed Vol 13.16 analyses. No safety values stated.

## 12. Performance

Emission and susceptibility performance allocations are TBD. No values stated.

## 13. Verification & Validation

Verified by inspection (provision coverage) and analysis (zoning concepts). Validated later by EMI/EMC test structured according to DO-160 concepts only. Pass/fail criteria TBD.

## 14. Risks

- Coupling across segregated and sensor paths; mitigation: zoning and shielding concepts with test gating (TBD).
- Practice and limit uncertainty; mitigation: practice selection deferred with structured-according-to framing (TBD).

## 15. Open Issues

Emission practice, susceptibility practice, limits, zoning implementation, shielding design, and test applicability TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on HFPX-ELE-ARC-001, SAD PWR view, grounding structure (Chapter 15.12), distribution and feed structures, and Vol 13.16 safety inputs.

## 18. Traceability

Parents: SYS tier; SAD PWR view (HFPX-ARC-PWR-001); HFPX-ELE-ARC-001; Vol 13.16 hook (TBD). Children: ICDs, V&V cases. RTM: REQ-HFPX-EMC-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Chapter 15.13.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 15.13) |
