# Helmet Power

**Document ID:** HFPX-ELE-HMP-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the helmet power feed structure (Chapter 15.10): feeds, segregation, and interfaces to helmet loads. Structure only; no ratings or load values are stated.

## 2. Scope

Covers power feeds to helmet and pilot-interface loads per Vol 10 Chapter 10.16 hook (TBD). Excludes load values, ratings, schematics, disconnect design, and power-quality values (all TBD).

## 3. Applicable Documents

- HFPX-ELE-ARC-001 Electrical Architecture (parent structure)
- HFPX-ARC-PWR-001 Power Architecture (SAD PWR view parent)
- HFPX-SYS-REQ-001 SyRS (SYS tier parent)
- Vol 10 Chapter 10.16 (helmet load hook, TBD)
- Vol 13 Chapter 13.16 (safety hook, TBD)

## 4. Definitions & Acronyms

- Helmet feed: structured power path to helmet loads (rating TBD).
- Disconnect: structured crew-equipment separation provision (design TBD).

## 5. System Context

Helmet feeds interface with distribution, conversion, protection, grounding, and helmet equipment, including crew-worn disconnect provisions. They support normal, degraded, and emergency states.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-EHP-001 | The helmet power structure shall define helmet feed structure from distribution (details TBD). | HFPX-ELE-ARC-001; SAD PWR view; SYS tier | Inspection |
| REQ-HFPX-EHP-002 | The helmet power structure shall define disconnect and routing provisions structure for crew-worn interfaces (design TBD). | HFPX-ELE-ARC-001; Vol 10.16 hook | Inspection |
| REQ-HFPX-EHP-003 | The helmet power structure shall define helmet load-interface boundaries per Vol 10.16 hook (definitions TBD). | HFPX-ELE-ARC-001; Vol 10.16 hook | Inspection |
| REQ-HFPX-EHP-004 | The helmet power structure shall define helmet-feed monitoring and protection provisions structure (details TBD). | HFPX-ELE-ARC-001; Vol 13.16 hook | Analysis |

## 7. Architecture

Distribution buses (TBD) → protection (TBD) → helmet feeders and disconnect provisions (TBD) → helmet load interfaces (TBD), with segregation where designated (TBD). No ratings, load values, or schematics stated.

## 8. Detailed Design

Not applicable at this revision. Feeder sizing, disconnect selection, and schematics deferred to later tranches and ICDs. No electrical values stated.

## 9. Interfaces

Feeds to helmet equipment, disconnect interfaces, monitoring / control to power management, grounding / bonding provisions. Definitions TBD in ICDs and Vol 10.

## 10. Operational Concept

Helmet feeds support all power states including emergency states where designated; disconnect and shedding concepts (TBD) align with crew operations and CONOPS.

## 11. Safety

Loss-of-helmet-feed, disconnect-fault, and segregation cases feed Vol 13.16 analyses. No safety values stated.

## 12. Performance

Load and power-quality budgets are TBD with Vol 10 inputs. No values stated.

## 13. Verification & Validation

Verified by inspection (feed and disconnect coverage) and analysis (protection provisions). Validated later by load analysis and integration test. Pass/fail criteria TBD.

## 14. Risks

- Disconnect wear and fault exposure at crew interface; mitigation: disconnect provision review with Vol 10 (TBD).
- Helmet load growth; mitigation: margin policy with Vol 10 inputs (TBD).

## 15. Open Issues

Feed topology, load list, disconnect design, segregation, and power-quality limits TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on HFPX-ELE-ARC-001, SAD PWR view, distribution / protection structures, Vol 10.16 load inputs, and Vol 13.16 safety inputs.

## 18. Traceability

Parents: SYS tier; SAD PWR view (HFPX-ARC-PWR-001); HFPX-ELE-ARC-001; Vol 10.16 / 13.16 hooks (TBD). Children: ICDs, V&V cases. RTM: REQ-HFPX-EHP-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Chapter 15.10.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 15.10) |
