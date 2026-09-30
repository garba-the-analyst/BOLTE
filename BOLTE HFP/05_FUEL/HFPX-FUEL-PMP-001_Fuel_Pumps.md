# Fuel Pumps

**Document ID:** HFPX-FUEL-PMP-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the fuel-pump requirements for HFP-X (Chapter 05.6): pump functions and pressure provision, redundancy, monitoring, and verification. All pressures, flow rates, powers, and redundancies are TBD. Fuel type is not selected (see 05.2).

## 2. Scope

Covers boost/transfer/feed pump functions (allocations TBD), redundancy provisions, pump monitoring provisions, and pump verification approach. Excludes pump technology selection, tank/distribution/filtering/metering/injection internals (05.3–05.5, 05.7–05.9), electrical power-system design (Vol 09 pattern), and test execution (05.16).

> **Hazardous-subsystem boundary.** Content in this document is limited to requirements, architecture, interfaces, test methodology and safety analysis. It shall not contain instructions for constructing, igniting, or operating human-carrying high-energy propulsion outside appropriate engineering, test, safety and regulatory controls. No fuel-handling or operation instructions are provided herein.

## 3. Applicable Documents

- HFPX-FUEL-REQ-001 (parents FRQ-001/003/005); HFPX-FUEL-SEL-001 (fuel-agnostic constraint)
- HFPX-FUEL-DIS-001 (distribution topology); Vol 04 propulsion demands (TBD); Vol 07 monitoring; Vol 09-pattern power interfaces

## 4. Definitions & Acronyms

- FPP: pump ID prefix `REQ-HFPX-FPP-NNN`
- Pump functions: boost, transfer, and feed roles within the distribution chain (allocations TBD)
- Pump monitoring: speed, status, pressure, fault annunciation provisions (signals TBD)

## 5. System Context

Pumps pressurise and move fuel from tanks through distribution toward metering/injection, powered electrically (or as TBD) and monitored via Vol 07:

```text
TANKS (05.3) → PUMPS (this doc) → DISTRIBUTION (05.5) → FILTER/METER/INJECT (05.7–05.9)
   ↕ power (electrical TBD)   ↕ monitoring (Vol 07: status/faults TBD)
```

Pump count, placement, and duty are TBD pending demands and topology.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-FPP-001 | The fuel pump subsystem shall provide pressurised fuel flow meeting distribution and engine-interface demands, with pressures, flow rates, and duty TBD. | REQ-HFPX-FRQ-001 | Analysis + Test |
| REQ-HFPX-FPP-002 | The fuel pump subsystem shall provide pump redundancy provisions (schemes and coverage TBD) such that defined single-pump faults do not prevent continued delivery (cases TBD). | REQ-HFPX-FRQ-001 | Analysis + Test |
| REQ-HFPX-FPP-003 | The fuel pump subsystem shall provide pump monitoring provisions (status, fault detection, annunciation signals — details TBD) to the control/monitoring system. | REQ-HFPX-FRQ-003 | Analysis + Demonstration |
| REQ-HFPX-FPP-004 | The fuel pump subsystem shall be verifiable by defined pump-verification means (analysis, inspection, bench/loop-test methodology — cases TBD) under controlled conditions. | REQ-HFPX-FRQ-005 | Analysis + Demonstration |

No pressure, flow-rate, power, or redundancy value in this document is approved.

## 7. Architecture

Notional pump-architecture views (all TBD): pump locations in feed/transfer paths; redundancy arrangement (series/parallel/standby TBD); drive power source (TBD). Views bound interface and safety analysis only; no pump type, rating, or vendor selection is made herein.

## 8. Detailed Design

Not applicable — CONCEPT requirements only. Pump technology, ratings, seals/materials, controllers, and mounting are TBD after fuel selection and demand definition.

## 9. Interfaces

Interface placeholders: pump-to-distribution hydraulic interface (pressures/flows TBD, 05.5); pump-to-power interface (voltage/power TBD); pump-to-monitoring interface (signals/formats TBD, Vol 07); pump-to-structure mounting interface (Vol 03, TBD). Formal ICDs TBD.

## 10. Operational Concept

Pump analysis (duty profiles, fault/reconfiguration logic) under controlled engineering conditions only. No pump-operation, priming, maintenance, or flight procedures are defined herein. All future handling/operation is restricted to appropriate engineering, test, safety, and regulatory controls.

## 11. Safety

FPP-002/003 carry pump safety provisions (redundancy, fault annunciation). Pump-failure, over-pressure, and leak hazards feed Vol 13 analysis (TBD) by change record. Hazardous-subsystem boundary applies: safety analysis and test methodology only.

## 12. Performance

Intentionally TBD. No discharge pressure, flow rate, efficiency, NPSH, endurance, or life figure is stated. Sizing awaits ISS-003 trade and Vol 04 demands.

## 13. Verification & Validation

Methods stated in §6 table. Means TBD: hydraulic/performance analysis, monitoring demonstration, controlled bench/loop tests (05.16, Vol 22). Verification IDs and pass criteria TBD; no test execution is authorised by this document.

## 14. Risks

- Pump duty assumed before demands known → rework; mitigation: duty-TBD requirement, no rating selected
- Redundancy scheme without Vol 13 fault coverage; mitigation: coverage TBD + joint Vol 13 action
- Monitoring signals without Vol 07 budget; mitigation: placeholder ICD + Vol 07 co-ordination action

## 15. Open Issues

- Pump functions, count, placement, duty (TBD)
- Redundancy scheme and fault coverage (TBD)
- Monitoring signal set (TBD, Vol 07)
- Pump-verification cases (TBD, 05.16 / Vol 22)

## 16. Assumptions

- A-FPP-001: Pump functions/redundancy can be required as TBD provisions ahead of demands; validation: SRR review
- A-FPP-002: Power and monitoring systems will define budgets consumed by pump ICDs when allocated; validation: interface allocation review

## 17. Dependencies

Depends on 05.1 parents, 05.2 fuel-agnostic constraint, 05.3/05.5 topology, Vol 04 demands, Vol 07 monitoring, power-system allocation, Vol 13 safety inputs, V&V methodology (Vol 22, 05.16).

## 18. Traceability

Parents: REQ-HFPX-FRQ-001/003/005 (table above). Children: pump arrangement views, power/monitoring ICDs, V&V cases, RTM rows. RTM seed for FPP-001..004 added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0 (structure only) — Tranche 4 draft, not baselined. Pump selection, rating, or redundancy commitment requires a new revision via change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (Chapter 05.6, 4 requirements) |
