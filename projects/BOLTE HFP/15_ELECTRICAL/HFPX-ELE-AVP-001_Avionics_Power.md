# Avionics Power

**Document ID:** HFPX-ELE-AVP-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the avionics power feed structure (Chapter 15.9): feeds, segregation, and interfaces to avionics loads. Structure only; no ratings or load values are stated.

## 2. Scope

Covers power feeds to avionics and compute loads per Vol 08 Chapter 08.7 hook (TBD). Excludes load values, ratings, schematics, and power-quality values (all TBD).

## 3. Applicable Documents

- HFPX-ELE-ARC-001 Electrical Architecture (parent structure)
- HFPX-ARC-PWR-001 Power Architecture (SAD PWR view parent)
- HFPX-SYS-REQ-001 SyRS (SYS tier parent)
- Vol 08 Chapter 08.7 (avionics load hook, TBD)
- Vol 13 Chapter 13.16 (safety hook, TBD)

## 4. Definitions & Acronyms

- Avionics feed: structured power path to avionics loads (rating TBD).
- E-LOAD: load-feed boundary to avionics domain (definition TBD).

## 5. System Context

Avionics feeds interface with distribution, conversion, protection, grounding, and avionics equipment. They support normal, degraded, and emergency states, including segregated safety-path feeds where designated.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-EAV-001 | The avionics power structure shall define avionics feed structure from distribution (details TBD). | HFPX-ELE-ARC-001; SAD PWR view; SYS tier | Inspection |
| REQ-HFPX-EAV-002 | The avionics power structure shall define segregation provisions for designated avionics paths (details TBD). | HFPX-ELE-ARC-001; Vol 13.16 hook | Analysis |
| REQ-HFPX-EAV-003 | The avionics power structure shall define avionics load-interface boundaries per Vol 08.7 hook (definitions TBD). | HFPX-ELE-ARC-001; Vol 08.7 hook | Inspection |
| REQ-HFPX-EAV-004 | The avionics power structure shall define avionics-feed monitoring and control interface structure (details TBD). | HFPX-ELE-ARC-001; SYS tier | Inspection |

## 7. Architecture

Distribution buses (TBD) → conversion where applicable (TBD) → protection (TBD) → avionics feeders (TBD) → E-LOAD boundaries (TBD), with segregation provisions (TBD). No ratings, load values, or schematics stated.

## 8. Detailed Design

Not applicable at this revision. Feeder sizing, connector selection, and schematics deferred to later tranches and ICDs. No electrical values stated.

## 9. Interfaces

E-LOAD (feeds to avionics), monitoring / control to power management, grounding / bonding provisions. Definitions TBD in ICDs and Vol 08.

## 10. Operational Concept

Avionics feeds support all power states; shedding and prioritisation concepts (TBD) preserve designated functions in degraded states.

## 11. Safety

Loss-of-avionics-feed and segregation-failure cases feed Vol 13.16 analyses. No safety values stated.

## 12. Performance

Load and power-quality budgets are TBD with Vol 08 inputs. No values stated.

## 13. Verification & Validation

Verified by inspection (feed coverage) and analysis (segregation concepts). Validated later by load analysis and integration test. Pass/fail criteria TBD.

## 14. Risks

- Avionics load growth exceeding TBD feed structure; mitigation: margin policy with Vol 08 inputs (TBD).
- Coupling across avionics paths; mitigation: segregation and EMC provisions (TBD).

## 15. Open Issues

Feed topology, load list, segregation implementation, shedding priorities, and power-quality limits TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on HFPX-ELE-ARC-001, SAD PWR view, distribution / conversion / protection structures, Vol 08.7 load inputs, and Vol 13.16 safety inputs.

## 18. Traceability

Parents: SYS tier; SAD PWR view (HFPX-ARC-PWR-001); HFPX-ELE-ARC-001; Vol 08.7 / 13.16 hooks (TBD). Children: ICDs, V&V cases. RTM: REQ-HFPX-EAV-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Chapter 15.9.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 15.9) |
