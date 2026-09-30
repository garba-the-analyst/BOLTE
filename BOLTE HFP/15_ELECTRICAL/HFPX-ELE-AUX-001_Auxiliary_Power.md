# Auxiliary Power

**Document ID:** HFPX-ELE-AUX-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the auxiliary power structure (Chapter 15.3): role, boundaries, operating states, and interfaces. Structure only; no source selection or ratings are made.

## 2. Scope

Covers auxiliary source role and its connection to distribution. Excludes ratings, source types, schematics, and power-quality values (all TBD).

## 3. Applicable Documents

- HFPX-ELE-ARC-001 Electrical Architecture (parent structure)
- HFPX-ARC-PWR-001 Power Architecture (SAD PWR view parent)
- HFPX-SYS-REQ-001 SyRS (SYS tier parent)
- Vol 13 Chapter 13.16 (safety hook, TBD)

## 4. Definitions & Acronyms

- Auxiliary power: source role supplementing or backing primary power in defined states (rating TBD).
- Transfer: structured change of source feeding distribution (logic TBD).

## 5. System Context

Auxiliary power interfaces with distribution buses, protection, control, and ground servicing. It supports defined normal, degraded, and ground states where primary power alone is not the designated source.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-EAP-001 | The auxiliary power structure shall define the auxiliary source role and operating-state coverage (ratings TBD). | HFPX-ELE-ARC-001; SAD PWR view; SYS tier | Inspection |
| REQ-HFPX-EAP-002 | The auxiliary power structure shall define the auxiliary source output boundary to distribution (definition TBD). | HFPX-ELE-ARC-001; SAD PWR view | Inspection |
| REQ-HFPX-EAP-003 | The auxiliary power structure shall define transfer structure between primary, auxiliary, battery, and emergency sources (logic TBD). | HFPX-ELE-ARC-001; Vol 13.16 hook | Analysis |
| REQ-HFPX-EAP-004 | The auxiliary power structure shall define auxiliary-source status and control interface structure (details TBD). | HFPX-ELE-ARC-001; SYS tier | Inspection |

## 7. Architecture

Auxiliary source block (TBD) → output boundary (TBD) → distribution buses (TBD). Transfer and prioritisation concepts (TBD) coordinate with primary, battery, and emergency structures. No ratings or topologies stated.

## 8. Detailed Design

Not applicable at this revision. Source selection, sizing, and schematics deferred. No electrical values stated.

## 9. Interfaces

Auxiliary output to distribution, control / status to power management, ground-service interfaces. Definitions TBD in ICDs.

## 10. Operational Concept

Auxiliary power supports defined ground, backup, and degraded states; transfer logic (TBD) preserves designated functions without defining timing values.

## 11. Safety

Transfer failure and loss-of-auxiliary cases feed Vol 13.16 analyses. No safety values stated.

## 12. Performance

Output characteristics and power-quality budgets are TBD. No values stated.

## 13. Verification & Validation

Verified by inspection (role and boundary coverage) and analysis (transfer concepts). Validated later by integration test. Pass/fail criteria TBD.

## 14. Risks

- Transfer conflict or gap in coverage; mitigation: transfer concept analysis and test gating (TBD).
- Interface mismatch to distribution; mitigation: ICD definition (TBD).

## 15. Open Issues

Source selection, ratings, transfer logic, and ground-service provisions TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on HFPX-ELE-ARC-001, SAD PWR view, distribution structure (Chapter 15.5), and Vol 13.16 safety inputs.

## 18. Traceability

Parents: SYS tier; SAD PWR view (HFPX-ARC-PWR-001); HFPX-ELE-ARC-001. Children: ICDs, V&V cases. RTM: REQ-HFPX-EAP-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Chapter 15.3.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 15.3) |
