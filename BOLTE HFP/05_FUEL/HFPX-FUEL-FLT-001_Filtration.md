# Filtration

**Document ID:** HFPX-FUEL-FLT-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the fuel-filtration requirements for HFP-X (Chapter 05.7): filtration function and rating provisions, bypass/clogging annunciation, and maintenance hooks. All ratings, contamination limits, and intervals are TBD. Fuel type is not selected (see 05.2).

## 2. Scope

Covers filter function/placement (TBD), rating and contamination-limit provisions (values TBD), bypass and clogging annunciation, and maintenance hooks (access/replacement provisions TBD). Excludes fuel selection (05.2), pump/distribution/metering/injection internals (05.5/05.6/05.8/05.9), and test execution (05.16).

> **Hazardous-subsystem boundary.** Content in this document is limited to requirements, architecture, interfaces, test methodology and safety analysis. It shall not contain instructions for constructing, igniting, or operating human-carrying high-energy propulsion outside appropriate engineering, test, safety and regulatory controls. No fuel-handling or operation instructions are provided herein.

## 3. Applicable Documents

- HFPX-FUEL-REQ-001 (parents FRQ-002/003/005); HFPX-FUEL-SEL-001 (fuel-agnostic constraint)
- HFPX-FUEL-DIS-001 (placement in chain); Vol 07 monitoring (annunciation); Vol 13 safety inputs (TBD)

## 4. Definitions & Acronyms

- FFL: filtration ID prefix `REQ-HFPX-FFL-NNN`
- Rating: filter retention/capacity provisions (micron rating, efficiency, life — all TBD, fuel-dependent)
- Bypass/clogging annunciation: detection and signalling of filter clogging or bypass state (thresholds TBD)

## 5. System Context

Filters protect metering/injection and engines from contamination, placed in the feed chain and monitored via Vol 07:

```text
PUMPS/DISTRIBUTION (05.5/05.6) → FILTER (this doc) → METERING (05.8) → INJECTION (05.9)
                                          ↕ clogging/bypass annunciation → Vol 07
```

Filter count, placement, and ratings are TBD pending fuel selection and engine-suitability inputs (Vol 04).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-FFL-001 | The filtration subsystem shall remove contaminants to defined rating provisions (rating, efficiency, capacity — values TBD) for the selected fuel. | REQ-HFPX-FRQ-002 | Analysis + Test |
| REQ-HFPX-FFL-002 | The filtration subsystem shall provide bypass and clogging annunciation provisions (detection, thresholds, signals — TBD) to the control/monitoring system. | REQ-HFPX-FRQ-003 | Analysis + Demonstration |
| REQ-HFPX-FFL-003 | The filtration subsystem shall provide maintenance hooks (access, replacement, condition-indication provisions — details TBD) enabling future servicing tasks. | REQ-HFPX-FRQ-005 | Inspection |

No filtration rating, limit, or interval in this document is approved.

## 7. Architecture

Notional filtration views (all TBD): filter locations in feed paths; bypass routing; differential-pressure sensing points. Views bound interface and safety analysis only; no filter element, housing, or sensor selection is made herein.

## 8. Detailed Design

Not applicable — CONCEPT requirements only. Media, housings, seals, bypass valves, and clogging sensors are TBD after fuel selection and contamination-limit definition.

## 9. Interfaces

Interface placeholders: filter-to-distribution hydraulic interface (05.5, TBD); filter-to-metering/injection cleanliness interface (05.8/05.9, limits TBD); filter-to-monitoring interface (annunciation signals TBD, Vol 07); filter-to-maintenance access interface (TBD). Formal ICDs TBD.

## 10. Operational Concept

Filtration analysis (contamination scenarios, bypass/annunciation logic) under controlled engineering conditions only. No filter-servicing, replacement, or operational procedures are defined herein. All future handling/operation is restricted to appropriate engineering, test, safety, and regulatory controls.

## 11. Safety

FFL-002 carries the clogging/bypass annunciation safety provision; contamination-induced engine-effect hazards feed Vol 13/Vol 04 analysis (TBD) by change record. Hazardous-subsystem boundary applies: safety analysis and test methodology only.

## 12. Performance

Intentionally TBD. No micron rating, efficiency, dirt-holding capacity, pressure drop, bypass threshold, or service interval is stated. Quantification awaits fuel selection and engine contamination limits (Vol 04).

## 13. Verification & Validation

Methods stated in §6 table (analysis, demonstration, inspection; test methodology via 05.16/Vol 22 under controlled conditions). Contamination-test media, rigs, IDs, and pass criteria are TBD; no test execution is authorised by this document.

## 14. Risks

- Rating assumed before fuel/contamination limits known → rework; mitigation: rating-TBD requirement, no element selected
- Bypass logic without Vol 07 annunciation budget; mitigation: placeholder ICD + Vol 07 action
- Maintenance access omitted from early routing; mitigation: FFL-003 hook held jointly with 05.5/Vol 03

## 15. Open Issues

- Filtration ratings and contamination limits (TBD, fuel + Vol 04)
- Bypass/clogging thresholds and signals (TBD, Vol 07)
- Servicing task set and intervals (TBD, maintenance system)
- Filtration-verification cases (TBD, 05.16 / Vol 22)

## 16. Assumptions

- A-FFL-001: Filtration can be required fuel-agnostically as rating-TBD provisions; validation: SRR review
- A-FFL-002: Engine contamination limits will be supplied by Vol 04 when defined; validation: Vol 04 interface review

## 17. Dependencies

Depends on 05.1 parents, 05.2 fuel-agnostic constraint, 05.5 placement, Vol 04 contamination limits, Vol 07 annunciation interface, Vol 13 safety inputs, V&V methodology (Vol 22, 05.16).

## 18. Traceability

Parents: REQ-HFPX-FRQ-002/003/005 (table above). Children: filter placement views, annunciation ICD (Vol 07), servicing provisions, V&V cases, RTM rows. RTM seed for FFL-001..003 added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0 (structure only) — Tranche 4 draft, not baselined. Rating or element selection requires a new revision via change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (Chapter 05.7, 3 requirements) |
