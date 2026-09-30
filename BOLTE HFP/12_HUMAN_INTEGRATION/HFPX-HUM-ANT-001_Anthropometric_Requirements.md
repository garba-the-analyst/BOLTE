# Anthropometric Requirements

**Document ID:** HFPX-HUM-ANT-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define anthropometric requirements for HFP-X pilot accommodation (Chapter 12.2). This Tranche 6 draft establishes population-coverage, accommodation-range, and adjustability placeholders; all values are TBD.

## 2. Scope

Covers intended-user population coverage, accommodation range, and adjustability provisions for the pilot station and suit interfaces. Excludes restraint design (12.3), load distribution (12.4), ergonomics detail (12.5), and mobility detail (12.10).

## 3. Applicable Documents

- HFPX-SYS-HUM-001 Human Factors Requirements (parent HUM tier)
- Stakeholder need STK-002 (human involvement)
- HSA tier (ID TBD — allocation to follow)
- Vol 30 hooks (TBD — population and evaluation inputs to follow)
- HFPX-HUM-ARC-001 Pilot Integration Architecture (Chapter 12.1, to be read jointly)

## 4. Definitions & Acronyms

- HUM: human-factors requirement tier; IDs `REQ-HFPX-HUM-NNN`.
- UAT: anthropometric requirement tier; IDs `REQ-HFPX-UAT-NNN`; verification TBD.
- TBD/TBC: unknown data; no values invented.

## 5. System Context

Anthropometry refines system-level accommodation needs into testable placeholders:

```text
STK-002 + HUM tier → UAT-001..004 → suit / station / restraint sizing → V&V cases
```

No population, percentile, or dimension is approved at this revision.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-UAT-001|The system shall define the intended-user population coverage for pilot accommodation (population coverage TBD).|STK-002, REQ-HFPX-HUM-003, HSA tier (ID TBD)|Test|
|REQ-HFPX-UAT-002|The system shall accommodate the defined anthropometric range across the pilot station and suit interfaces (accommodation range TBD).|STK-002, REQ-HFPX-HUM-003, HSA tier (ID TBD)|Inspection|
|REQ-HFPX-UAT-003|The system shall provide adjustability provisions to cover the defined accommodation range (adjustability provisions TBD).|STK-002, REQ-HFPX-HUM-003, HSA tier (ID TBD)|Inspection|
|REQ-HFPX-UAT-004|Anthropometric accommodation shall be verified against defined criteria and participant sampling (criteria and sampling TBD; Vol 30 hook TBD).|STK-002, REQ-HFPX-HUM-003, HSA tier (ID TBD)|Inspection|

All populations, ranges, provisions, and criteria are TBD. No value is approved.

## 7. Architecture

Starter allocation (SAD owns authoritative mapping): UAT-001/002 → pilot station, suit sizing, and restraint interfaces; UAT-003 → adjustment mechanisms; UAT-004 → V&V framework with Vol 30 hooks. All TBC.

## 8. Detailed Design

Not applicable — requirements level only. Sizing tables, adjustment ranges, and hardware selection are TBD in follow-on revisions.

## 9. Interfaces

Anthropometric interfaces (station geometry, suit sizing interfaces, adjustment linkages) are TBD in Vol 02 ICDs and Chapter 12.1 register. No interface value or layout is approved.

## 10. Operational Concept

Accommodation requirements apply across donning, ingress, flight, egress, and doffing phases; phase-specific applicability is TBD. Unmanned demonstration precedes any crewed evaluation per safety gating.

## 11. Safety

Accommodation shortfalls and adjustability failures feed Vol 13 safety analyses (to follow). No UAT requirement confers flight approval; human flight remains gated by tier 01.10 and the Safety Case.

## 12. Performance

No UAT requirement quantifies performance. All coverage bounds and accommodation measures are TBD pending follow-on studies.

## 13. Verification & Validation

Each requirement states its method above as TBD; verification IDs, measurement protocols, participant criteria, and pass thresholds are TBD in the V&V Plan (Vol 22) with Vol 12/30 inputs. No accommodation credit is claimed at this revision.

## 14. Risks

- Population coverage undefined → exclusion or misfit discovered late; mitigation: early UAT placeholders plus review gates.
- Adjustability scope undefined → sizing rework; mitigation: UAT-003 placeholder plus architecture review.

## 15. Open Issues

TBD: population coverage, accommodation range, adjustability provisions, and verification criteria/sampling pending Vol 30 and HSA-tier inputs.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on STK-002 stability, HUM-tier stability (HFPX-SYS-HUM-001), HSA-tier allocation (TBD), Vol 30 hooks (TBD), Chapter 12.1 architecture, and V&V Plan cases. Changes propagate by change record.

## 18. Traceability

Parents: STK-002, HUM tier (REQ-HFPX-HUM-003), HSA tier (ID TBD), Vol 30 hooks (TBD) — see table. Children: sizing specs, adjustment specs, V&V cases, RTM rows. RTM seed for UAT-001..004 added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Additions or range changes require new revisions via change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 12.2) |
