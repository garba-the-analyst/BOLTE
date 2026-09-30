# Electrical Grounding

**Document ID:** HFPX-ELE-GND-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the electrical grounding structure (Chapter 15.12): reference, bonding, and segregation provisions. Structure only; no scheme selection or resistance values are stated.

## 2. Scope

Covers grounding and bonding concepts for sources, distribution, conversion, and load feeds, including EMI/EMC coordination. Excludes scheme selection, resistance values, joint details, and schematics (all TBD).

## 3. Applicable Documents

- HFPX-ELE-ARC-001 Electrical Architecture (parent structure)
- HFPX-ARC-PWR-001 Power Architecture (SAD PWR view parent)
- HFPX-SYS-REQ-001 SyRS (SYS tier parent)
- Vol 13 Chapter 13.16 (safety hook, TBD)

## 4. Definitions & Acronyms

- Grounding: structured reference-potential provisions (scheme TBD).
- Bonding: structured conductive joining provisions (details TBD).
- E-GND: grounding / bonding boundary (definition TBD).

## 5. System Context

Grounding interfaces with airframe structure, all power equipment, avionics / helmet / sensor feeds, and EMI/EMC zoning. It applies across all power states and maintenance states.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-EGR-001 | The grounding structure shall define reference and return provisions structure (scheme TBD). | HFPX-ELE-ARC-001; SAD PWR view; SYS tier | Inspection |
| REQ-HFPX-EGR-002 | The grounding structure shall define bonding provisions structure for equipment and structure (details TBD). | HFPX-ELE-ARC-001; SAD PWR view | Inspection |
| REQ-HFPX-EGR-003 | The grounding structure shall define segregation provisions for designated ground paths (details TBD). | HFPX-ELE-ARC-001; SAD PWR view | Analysis |
| REQ-HFPX-EGR-004 | The grounding structure shall define grounding safety hooks to Vol 13.16 analyses (details TBD). | HFPX-ELE-ARC-001; Vol 13.16 hook | Inspection |

## 7. Architecture

Equipment grounds (TBD) → bonding network (TBD) → structural reference (TBD), with segregated paths where designated (TBD) and coordination with protection and EMI/EMC zoning (TBD). No scheme selection, values, or schematics stated.

## 8. Detailed Design

Not applicable at this revision. Scheme selection, joint design, and schematics deferred to later tranches and ICDs. No electrical values stated.

## 9. Interfaces

E-GND (grounding / bonding boundaries), interfaces to airframe structure, equipment enclosures, and shields. Definitions TBD in ICDs.

## 10. Operational Concept

Grounding provisions apply in all operating and maintenance states; inspection and continuity verification concepts (TBD) align with maintenance states.

## 11. Safety

Ground faults, bonding failures, and fault-return integrity cases feed Vol 13.16 analyses. No safety values stated.

## 12. Performance

Ground-path performance allocations are TBD. No values stated.

## 13. Verification & Validation

Verified by inspection (provision coverage) and analysis (segregation and return concepts). Validated later by continuity and integration test. Pass/fail criteria TBD.

## 14. Risks

- Ground loops and shared-path coupling; mitigation: segregation and zoning concepts (TBD).
- Bonding degradation; mitigation: maintenance verification provisions (TBD).

## 15. Open Issues

Grounding scheme, bonding implementation, segregated-path design, and verification provisions TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on HFPX-ELE-ARC-001, SAD PWR view, distribution / protection structures, airframe structural interfaces, EMI/EMC structure (Chapter 15.13), and Vol 13.16 safety inputs.

## 18. Traceability

Parents: SYS tier; SAD PWR view (HFPX-ARC-PWR-001); HFPX-ELE-ARC-001; Vol 13.16 hook (TBD). Children: ICDs, V&V cases. RTM: REQ-HFPX-EGR-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Chapter 15.12.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 15.12) |
