# Fuel Tank Architecture

**Document ID:** HFPX-FUEL-TNK-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the fuel-tank architecture requirements for HFP-X (Chapter 05.3): tank functions, crashworthiness and venting principles, quantity-sensing interface, and structural integration. All capacities, loads, pressures, and dimensions are TBD. Fuel type is not selected (see 05.2).

## 2. Scope

Covers tank-level functions and capacity provisioning (values TBD), crashworthiness/venting design principles (details TBD), quantity-sensing interface (accuracies TBD), and structural-integration requirements with Vol 03. Excludes fuel selection (05.2), storage operations (05.4), distribution/pumps/filtering/metering/injection internals (05.5–05.9), detailed sensing implementations (05.10–05.12), and test execution (05.16).

> **Hazardous-subsystem boundary.** Content in this document is limited to requirements, architecture, interfaces, test methodology and safety analysis. It shall not contain instructions for constructing, igniting, or operating human-carrying high-energy propulsion outside appropriate engineering, test, safety and regulatory controls. No fuel-handling or operation instructions are provided herein.

## 3. Applicable Documents

- HFPX-FUEL-REQ-001 (parents FRQ-001/003/004); HFPX-FUEL-SEL-001 (fuel-agnostic constraint)
- Vol 03 airframe/structure (integration); Vol 07 control/monitoring (sensing interface); Vol 13 safety analyses (TBD)
- HFP prompt §§14, 34 (hazardous-subsystem boundary)

## 4. Definitions & Acronyms

- FTK: tank-architecture ID prefix `REQ-HFPX-FTK-NNN`
- Crashworthiness: tank behaviour under crash/impact loads per Vol 03/Vol 13 principles (values TBD)
- Venting: pressure-management and vent-path provisions (pressures TBD)
- Quantity-sensing interface: data boundary between tank/gauging and control/monitoring (accuracies TBD)

## 5. System Context

Tanks sit at the head of the fuel chain, inside Vol 03 structure, feeding distribution and reporting to Vol 07:

```text
STRUCTURE (Vol 03) → TANKS (this doc) → DISTRIBUTION (05.5) → ENGINES (Vol 04)
                          ↕ quantity-sensing → CONTROL/MONITORING (Vol 07)
```

Tank count, arrangement, and capacities are TBD pending ISS-003 trade and Vol 03/04 budgets.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-FTK-001 | The fuel tank subsystem shall provide containment and supply functions for the usable-fuel capacity, with capacity, compartmentalisation, and feed provisions TBD. | REQ-HFPX-FRQ-001 | Analysis + Inspection |
| REQ-HFPX-FTK-002 | The fuel tank subsystem shall implement crashworthiness and venting principles (impact behaviour, vent paths, over-pressure provisions — details and values TBD) per Vol 03/Vol 13 inputs. | REQ-HFPX-FRQ-004 | Analysis |
| REQ-HFPX-FTK-003 | The fuel tank subsystem shall provide a quantity-sensing interface delivering tank-quantity data to the control/monitoring system, with accuracy, resolution, and update provisions TBD. | REQ-HFPX-FRQ-003 | Analysis + Demonstration |
| REQ-HFPX-FTK-004 | The fuel tank subsystem shall integrate with the airframe structure (mounting, loads, access, fire-zone provisions — details TBD) per Vol 03 allocation. | REQ-HFPX-FRQ-001, REQ-HFPX-FRQ-004 | Analysis + Inspection |

No tank capacity, pressure, load, or dimension in this document is approved.

## 7. Architecture

Notional tank-architecture views (all TBD): containment vessels/compartments (count TBD); vent system (routing TBD); gauging pickups (technology TBD, see 05.10); structural mounts and access panels (Vol 03). No geometry, material, or arrangement is selected in this revision; views exist to bound interfaces and safety analysis, not to authorise construction.

## 8. Detailed Design

Not applicable — CONCEPT architecture only. Materials, wall construction, baffling, vent-valve selection, gauging technology, and fastening are TBD after fuel selection and structural allocation.

## 9. Interfaces

Interface placeholders: tank-to-distribution feed interface (line count/size TBD, 05.5); tank-to-structure mechanical interface (loads/envelope TBD, Vol 03); tank-to-sensing interface (signals/formats TBD, Vol 07 / 05.10); tank-to-vent interface (paths/pressures TBD). Formal ICDs TBD.

## 10. Operational Concept

Architecture analysis under controlled engineering conditions only. No tank filling, draining, venting operations, maintenance procedures, or flight operations are defined herein. All future handling/operation is restricted to appropriate engineering, test, safety, and regulatory controls.

## 11. Safety

FTK-002 and FTK-004 carry the tank safety provisions (crashworthiness, venting, structural/fire-zone integration). Detailed hazard analysis (crash, over-pressure, leak/fire — TBD, Vol 13) generates derived requirements by change record. Hazardous-subsystem boundary applies: safety analysis and test methodology only.

## 12. Performance

Intentionally TBD. No capacity, usable/unusable-fuel split, feed rate, venting pressure, crash load, or mass figure is stated. Performance sizing awaits fuel selection (05.2), propulsion demands (Vol 04), and structural budgets (Vol 03).

## 13. Verification & Validation

Methods stated in §6 table. Means TBD: structural/vent analysis (models), interface inspection, sensing demonstration on rigs, progressing to controlled tank tests (05.16, Vol 22). Verification IDs and pass criteria TBD; no test execution is authorised by this document.

## 14. Risks

- Tank arrangement assumed before Vol 03 allocation → rework; mitigation: keep arrangement TBD, interface placeholders only
- Fuel-agnostic venting/material assumptions invalidated by DDR choice; mitigation: principles-only requirements, re-verification gate after DDR
- Quantity-sensing accuracy without Vol 07 budget; mitigation: joint ICD action with Vol 07

## 15. Open Issues

- Tank count/arrangement/capacity (TBD, blocked by ISS-003 + Vol 03/04)
- Crashworthiness/venting criteria and values (TBD, Vol 03/13)
- Quantity-sensing accuracy/resolution (TBD, Vol 07 / 05.10)
- Structural/fire-zone allocation (TBD, Vol 03)

## 16. Assumptions

- A-FTK-001: Principles-level tank requirements can precede fuel selection and structural allocation; validation: SRR review
- A-FTK-002: Vol 03 will own crash/fire-zone structural criteria consumed by FTK-002/004; validation: Vol 03 allocation review

## 17. Dependencies

Depends on 05.1 parents, 05.2 fuel-agnostic constraint + future DDR, Vol 03 structural/fire-zone allocation, Vol 04 feed demands, Vol 07 sensing interface, Vol 13 safety inputs, V&V methodology (Vol 22, 05.16).

## 18. Traceability

Parents: REQ-HFPX-FRQ-001/003/004 (table above). Children: tank arrangement views, Vol 03 integration artefacts, quantity-sensing ICD (Vol 07 / 05.10), V&V cases, RTM rows. RTM seed for FTK-001..004 added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0 (structure only) — Tranche 4 draft, not baselined. Geometry, material, or capacity selection requires a new revision via change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (Chapter 05.3, 4 requirements) |
