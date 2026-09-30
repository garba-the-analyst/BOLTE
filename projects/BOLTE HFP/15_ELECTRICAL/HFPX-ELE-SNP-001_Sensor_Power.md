# Sensor Power

**Document ID:** HFPX-ELE-SNP-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the sensor power feed structure (Chapter 15.11): feeds, segregation, and interfaces to sensor loads. Structure only; no ratings or load values are stated.

## 2. Scope

Covers power feeds to sensor loads (details TBD). Excludes load values, ratings, schematics, and power-quality values (all TBD).

## 3. Applicable Documents

- HFPX-ELE-ARC-001 Electrical Architecture (parent structure)
- HFPX-ARC-PWR-001 Power Architecture (SAD PWR view parent)
- HFPX-SYS-REQ-001 SyRS (SYS tier parent)
- Vol 08 Chapter 08.7 (sensor load hook, TBD)
- Vol 13 Chapter 13.16 (safety hook, TBD)

## 4. Definitions & Acronyms

- Sensor feed: structured power path to sensor loads (rating TBD).
- Quiet feed: segregation provision for noise-sensitive paths (details TBD).

## 5. System Context

Sensor feeds interface with distribution, conversion, protection, grounding, and EMI/EMC zoning. They support normal, degraded, and emergency states where designated, including noise-sensitive provisions.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-ESP-001 | The sensor power structure shall define sensor feed structure from distribution (details TBD). | HFPX-ELE-ARC-001; SAD PWR view; SYS tier | Inspection |
| REQ-HFPX-ESP-002 | The sensor power structure shall define segregation provisions for designated sensor paths (details TBD). | HFPX-ELE-ARC-001; SAD PWR view | Analysis |
| REQ-HFPX-ESP-003 | The sensor power structure shall define sensor load-interface boundaries (definitions TBD). | HFPX-ELE-ARC-001; Vol 08.7 hook | Inspection |
| REQ-HFPX-ESP-004 | The sensor power structure shall define sensor-feed monitoring and protection provisions structure (details TBD). | HFPX-ELE-ARC-001; Vol 13.16 hook | Analysis |

## 7. Architecture

Distribution buses (TBD) → conversion where applicable (TBD) → protection (TBD) → sensor feeders (TBD) → load interfaces (TBD), with quiet-feed and segregation provisions (TBD) coordinated with EMI/EMC zoning. No ratings, load values, or schematics stated.

## 8. Detailed Design

Not applicable at this revision. Feeder sizing, filtering provisions, and schematics deferred. No electrical values stated.

## 9. Interfaces

Feeds to sensors, monitoring / control to power management, grounding / bonding and shielding provisions. Definitions TBD in ICDs.

## 10. Operational Concept

Sensor feeds support defined power states; shedding and prioritisation concepts (TBD) preserve designated sensing functions in degraded states.

## 11. Safety

Loss-of-sensor-feed and segregation-failure cases feed Vol 13.16 analyses. No safety values stated.

## 12. Performance

Load and power-quality budgets are TBD. No values stated.

## 13. Verification & Validation

Verified by inspection (feed coverage) and analysis (segregation concepts). Validated later by load analysis and integration test. Pass/fail criteria TBD.

## 14. Risks

- Noise coupling into sensor paths; mitigation: quiet-feed provisions with EMC zoning (TBD).
- Sensor load growth; mitigation: margin policy with load inventory completion (TBD).

## 15. Open Issues

Feed topology, load list, quiet-feed implementation, segregation, and power-quality limits TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on HFPX-ELE-ARC-001, SAD PWR view, distribution / conversion / protection structures, EMI/EMC structure (Chapter 15.13), and Vol 08.7 / 13.16 inputs.

## 18. Traceability

Parents: SYS tier; SAD PWR view (HFPX-ARC-PWR-001); HFPX-ELE-ARC-001; Vol 08.7 / 13.16 hooks (TBD). Children: ICDs, V&V cases. RTM: REQ-HFPX-ESP-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Chapter 15.11.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 15.11) |
