# Fuel Storage

**Document ID:** HFPX-FUEL-STO-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the fuel-storage requirements for HFP-X (Chapter 05.4): storage integrity, thermal/environmental limits, inspection/maintenance hooks, and storage verification. All limits, durations, and values are TBD. Fuel type is not selected (see 05.2).

## 2. Scope

Covers fuel-at-rest integrity (containment over storage durations TBD), thermal/environmental limit compliance (values TBD), inspection/maintenance provisions, and storage verification approach. Excludes fuel selection (05.2), tank architecture geometry (05.3), distribution/pumps/filtering/metering/injection (05.5–05.9), and refuelling/defuelling operations (05.17).

> **Hazardous-subsystem boundary.** Content in this document is limited to requirements, architecture, interfaces, test methodology and safety analysis. It shall not contain instructions for constructing, igniting, or operating human-carrying high-energy propulsion outside appropriate engineering, test, safety and regulatory controls. No fuel-handling or operation instructions are provided herein.

## 3. Applicable Documents

- HFPX-FUEL-REQ-001 (parents FRQ-002/004/005); HFPX-FUEL-SEL-001 (fuel-agnostic constraint)
- HFPX-FUEL-TNK-001 (tank architecture); Vol 13 safety analyses (TBD); Vol 22 V&V Plan (TBD)

## 4. Definitions & Acronyms

- FSR: storage ID prefix `REQ-HFPX-FSR-NNN`
- Storage integrity: ability to contain fuel within limits over defined storage durations and environments (values TBD)
- Inspection/maintenance hooks: access, sampling, drain, and NDT provisions enabling future inspection/maintenance (details TBD)

## 5. System Context

Storage is the at-rest state of the tank subsystem, exposed to ambient/thermal environments and ageing, feeding distribution on demand:

```text
AMBIENT/THERMAL ENV → STORAGE (tanks at rest, this doc) → DISTRIBUTION ON DEMAND (05.5)
                           ↕ inspection/maintenance provisions → MAINTENANCE SYSTEM (Vol TBD)
```

Durations, environments, and fuel-stability data are TBD pending selection and envelope definition.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-FSR-001 | The fuel storage subsystem shall maintain storage integrity (containment, leakage, permeation provisions — limits and durations TBD) in defined storage environments. | REQ-HFPX-FRQ-004 | Analysis + Test |
| REQ-HFPX-FSR-002 | The fuel storage subsystem shall remain within defined thermal and environmental limits (temperature, humidity, contaminants — values TBD) for the selected fuel. | REQ-HFPX-FRQ-002 | Analysis |
| REQ-HFPX-FSR-003 | The fuel storage subsystem shall provide inspection and maintenance hooks (access, sampling, drain, NDT provisions — details TBD) enabling future inspection and maintenance tasks. | REQ-HFPX-FRQ-005 | Inspection |
| REQ-HFPX-FSR-004 | The fuel storage subsystem shall be verifiable by defined storage-verification means (analysis, inspection, endurance/ageing test methodology — cases TBD) under controlled conditions. | REQ-HFPX-FRQ-005 | Analysis + Inspection |

No duration, limit, or material-compatibility value in this document is approved.

## 7. Architecture

Storage-architecture views (all TBD): containment boundary (tank + seals/closures); thermal exposure paths (ambient, solar, propulsion/airframe heat — TBD); inspection access points (TBD). Views bound analysis and verification planning only; no material, seal, coating, or insulation selection is made herein.

## 8. Detailed Design

Not applicable — CONCEPT requirements only. Materials, seals, coatings, insulation, sampling/drain hardware, and storage-life substantiation are TBD after fuel selection.

## 9. Interfaces

Interface placeholders: storage-to-environment interface (envelope TBD); storage-to-maintenance interface (access/tooling TBD); storage-to-sensing interface (condition monitoring TBD, Vol 07). Formal ICDs TBD.

## 10. Operational Concept

Storage analysis under controlled engineering conditions only. No storage operations, sampling procedures, maintenance tasks, or handling instructions are defined herein. All future storage/handling activity is restricted to appropriate engineering, test, safety, and regulatory controls.

## 11. Safety

FSR-001/002 carry storage safety provisions (containment, environmental limits). Ageing, permeation, and contamination hazards feed Vol 13 analysis (TBD) and derive future requirements by change record. Hazardous-subsystem boundary applies: safety analysis and test methodology only.

## 12. Performance

Intentionally TBD. No storage duration, leakage/permeation rate, temperature limit, or shelf-life figure is stated. Sizing awaits fuel selection (05.2) and environmental-envelope definition.

## 13. Verification & Validation

Methods stated in §6 table. Storage verification methodology TBD: analysis (thermal/ageing models), inspection (integrity/access), and controlled endurance/ageing tests (05.16, Vol 22). Verification IDs and pass criteria TBD; no test execution is authorised by this document.

## 14. Risks

- Fuel-agnostic storage limits invalidated by DDR choice; mitigation: limits TBD + re-verification gate after DDR
- Ageing/compatibility data unavailable at CONCEPT; mitigation: methodology-first approach, data actions on trade study
- Inspection hooks omitted from early tank geometry; mitigation: FSR-003 hook requirement held jointly with 05.3/Vol 03

## 15. Open Issues

- Storage durations and environments (TBD)
- Thermal/environmental limits (TBD, fuel-dependent)
- Inspection/maintenance task set (TBD, maintenance system)
- Storage-verification cases (TBD, 05.16 / Vol 22)

## 16. Assumptions

- A-FSR-001: Storage requirements can be stated fuel-agnostically as limits-TBD provisions; validation: SRR review
- A-FSR-002: Maintenance-system task definition will consume FSR-003 hooks when defined; validation: maintenance allocation review

## 17. Dependencies

Depends on 05.1 parents, 05.2 fuel-agnostic constraint + future DDR, 05.3 tank architecture, environmental-envelope definition, Vol 13 safety inputs, maintenance-system definition, V&V methodology (Vol 22, 05.16).

## 18. Traceability

Parents: REQ-HFPX-FRQ-002/004/005 (table above). Children: storage analysis views, inspection/maintenance provisions, storage-verification cases, RTM rows. RTM seed for FSR-001..004 added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0 (structure only) — Tranche 4 draft, not baselined. Limit or duration quantification requires a new revision via change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (Chapter 05.4, 4 requirements) |
