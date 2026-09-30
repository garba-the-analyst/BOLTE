# Fuel Distribution

**Document ID:** HFPX-FUEL-DIS-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the fuel-distribution requirements for HFP-X (Chapter 05.5): distribution topology, redundancy/cross-feed provisions, line-routing and fire-zone interfaces, and distribution verification. All flow rates, pressures, dimensions, and redundancies are TBD. Fuel type is not selected (see 05.2).

## 2. Scope

Covers lines, manifolds, valves (isolation/cross-feed), routing, and fire-zone interface provisions from tanks/pumps to metering/injection. Excludes tank architecture (05.3), pump internals (05.6), filtration (05.7), metering/injection (05.8/05.9), detailed isolation/leak implementations (05.13/05.14), and test execution (05.16).

> **Hazardous-subsystem boundary.** Content in this document is limited to requirements, architecture, interfaces, test methodology and safety analysis. It shall not contain instructions for constructing, igniting, or operating human-carrying high-energy propulsion outside appropriate engineering, test, safety and regulatory controls. No fuel-handling or operation instructions are provided herein.

## 3. Applicable Documents

- HFPX-FUEL-REQ-001 (parents FRQ-001/004/005); HFPX-FUEL-SEL-001 (fuel-agnostic constraint)
- HFPX-FUEL-TNK-001, -PMP-001 (neighbours); Vol 03 structure/fire zones; Vol 04 propulsion demands; Vol 07 monitoring

## 4. Definitions & Acronyms

- FDS: distribution ID prefix `REQ-HFPX-FDS-NNN`
- Cross-feed: ability to supply engines from alternate tank/line paths (topology TBD)
- Fire zone: airframe region with fire-protection provisions per Vol 03/Vol 13 (boundaries TBD)

## 5. System Context

Distribution connects tanks to consumers through pumps, filters, metering, and injection:

```text
TANKS (05.3) → [PUMPS 05.6] → DISTRIBUTION LINES/VALVES (this doc) → FILTER (05.7)
  → METERING (05.8) → INJECTION (05.9) → ENGINES (Vol 04)
```

Valve states and fault responses are monitored via Vol 07; routing is constrained by Vol 03 structure and fire zones.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-FDS-001 | The fuel distribution subsystem shall implement a defined distribution topology from tanks to consumers (line counts, branches, valve positions — TBD) meeting delivery demands (rates TBD). | REQ-HFPX-FRQ-001 | Analysis + Inspection |
| REQ-HFPX-FDS-002 | The fuel distribution subsystem shall provide redundancy and cross-feed provisions (schemes and coverage TBD) such that defined single-fault feed failures do not prevent continued delivery (cases TBD). | REQ-HFPX-FRQ-001, REQ-HFPX-FRQ-004 | Analysis + Test |
| REQ-HFPX-FDS-003 | The fuel distribution subsystem shall comply with line-routing and fire-zone interface provisions (separation, protection, shutoff placement — details TBD) per Vol 03/Vol 13 inputs. | REQ-HFPX-FRQ-004 | Analysis + Inspection |
| REQ-HFPX-FDS-004 | The fuel distribution subsystem shall be verifiable by defined distribution-verification means (analysis, inspection, flow-test methodology — cases TBD) under controlled conditions. | REQ-HFPX-FRQ-005 | Analysis + Demonstration |

No flow rate, pressure, diameter, routing, or redundancy value in this document is approved.

## 7. Architecture

Notional distribution views (all TBD): line schematic (branches TBD); isolation/cross-feed valve locations (TBD); fire-zone crossings and shutoff placement (TBD). Views bound interface and safety analysis only; no line size, material, valve selection, or routing is authorised herein.

## 8. Detailed Design

Not applicable — CONCEPT requirements only. Line sizing, materials, fittings, valve types/actuation, and supports are TBD after fuel selection, demand definition, and structural allocation.

## 9. Interfaces

Interface placeholders: distribution-to-tank feed interface (05.3); distribution-to-pump/filter/metering/injection interfaces (05.6–05.9); distribution-to-structure routing interface (Vol 03, penetrations/supports TBD); distribution-to-monitoring interface (valve/pressure status TBD, Vol 07); distribution-to-fire-protection interface (Vol 03/13). Formal ICDs TBD.

## 10. Operational Concept

Distribution analysis (nominal feed, cross-feed reconfiguration logic, shutoff demands) under controlled engineering conditions only. No valve-operation procedures, maintenance tasks, or flight operations are defined herein. All future handling/operation is restricted to appropriate engineering, test, safety, and regulatory controls.

## 11. Safety

FDS-002/003 carry distribution safety provisions (redundancy, fire-zone compliance, shutoff placement). Leak/rupture/fire hazards feed Vol 13 analysis (TBD) and Chapters 05.13–05.15 by change record. Hazardous-subsystem boundary applies: safety analysis and test methodology only.

## 12. Performance

Intentionally TBD. No flow rate, pressure drop, transient response, or redundancy-coverage figure is stated. Sizing awaits ISS-003 trade, Vol 04 demands, and Vol 03 routing constraints.

## 13. Verification & Validation

Methods stated in §6 table. Means TBD: schematic/flow analysis, routing inspection, valve-logic demonstration, controlled flow tests (05.16, Vol 22). Verification IDs and pass criteria TBD; no test execution is authorised by this document.

## 14. Risks

- Topology assumed before demands/routing known → rework; mitigation: topology-TBD requirement, placeholder schematic only
- Cross-feed complexity outpacing Vol 07 monitoring definition; mitigation: joint logic/ICD action with Vol 07
- Fire-zone boundaries unstable at CONCEPT; mitigation: interface requirement held jointly with Vol 03/13

## 15. Open Issues

- Distribution topology and valve complement (TBD)
- Redundancy/cross-feed fault coverage (TBD, Vol 13)
- Routing and fire-zone provisions (TBD, Vol 03/13)
- Distribution-verification cases (TBD, 05.16 / Vol 22)

## 16. Assumptions

- A-FDS-001: Topology/redundancy can be required as TBD provisions ahead of demands and routing; validation: SRR review
- A-FDS-002: Vol 03 will own fire-zone boundaries consumed by FDS-003; validation: Vol 03 allocation review

## 17. Dependencies

Depends on 05.1 parents, 05.2 fuel-agnostic constraint, 05.3 tank feeds, 05.6–05.9 neighbour interfaces, Vol 03 routing/fire zones, Vol 04 demands, Vol 07 monitoring, Vol 13 safety inputs, V&V methodology (Vol 22, 05.16).

## 18. Traceability

Parents: REQ-HFPX-FRQ-001/004/005 (table above). Children: distribution schematic, routing/fire-zone artefacts, valve-logic definitions, V&V cases, RTM rows. RTM seed for FDS-001..004 added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0 (structure only) — Tranche 4 draft, not baselined. Topology, routing, or redundancy selection requires a new revision via change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (Chapter 05.5, 4 requirements) |
