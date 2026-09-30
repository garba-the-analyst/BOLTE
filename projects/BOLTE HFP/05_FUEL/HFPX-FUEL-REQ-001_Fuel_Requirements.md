# Fuel Requirements

**Document ID:** HFPX-FUEL-REQ-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the top-level fuel-system requirements for HFP-X (Chapter 05.1). This document establishes what the fuel system shall deliver — fuel delivery across the flight envelope, fuel quality/conditioning, quantity/pressure/temperature knowledge, safety primacy, and the verification thread — without selecting a fuel type and without quantifying any capacity, pressure, flow rate, or temperature value. All quantitative values are TBD.

## 2. Scope

Covers fuel-system requirements allocated from system requirements SYS-001 (controlled flight) and SYS-003 (independent safety path), as refined by HFPX-SYS-REQ-001 SyRS. Includes delivery, quality, sensing, safety, and verification requirements. Excludes fuel-type selection (Chapter 05.2), tank/storage/distribution/pump/filter/metering/injection detailed design (Chapters 05.3–05.9), quantity/pressure/temperature/leak/isolation detailed implementations (Chapters 05.10–05.15), test execution (05.16), and refuelling/defuelling procedures (05.17).

> **Hazardous-subsystem boundary.** Content in this document is limited to requirements, architecture, interfaces, test methodology and safety analysis. It shall not contain instructions for constructing, igniting, or operating human-carrying high-energy propulsion outside appropriate engineering, test, safety and regulatory controls. No fuel-handling or operation instructions are provided herein.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parents SYS-001, SYS-003)
- HFPX-FUEL-SEL-001 Fuel Selection (Chapter 05.2 — criteria only, no fuel chosen)
- HFPX-FUEL-TNK-001, -STO-001, -DIS-001, -PMP-001, -FLT-001, -MTR-001, -INJ-001 (Chapters 05.3–05.9, this tranche)
- HFP prompt §§8–10 (requirements format, classification, traceability); §§14, 34 (hazardous-subsystem boundary); §§19, 32 (TBD handling)
- ISS-003 energy trade (fuel-type decision deferred to trade study + DDR)

## 4. Definitions & Acronyms

- FRQ: fuel requirements ID prefix `REQ-HFPX-FRQ-NNN`
- Verification: Analysis / Inspection / Demonstration / Test (per SyRS)
- TBD/TBC/A-XXX: unknown-data handling; no invented values
- Envelope: hover, transition, cruise, landing flight regimes (limits TBD)
- Fuel quality/conditioning: cleanliness, contamination control, and conditioning state suitable for the selected fuel (properties TBD, fuel type not selected)

## 5. System Context

The fuel system (SYS-04) stores, conditions, distributes, meters, and injects fuel to the propulsion system (SYS-03) under control/monitoring interfaces (Vol 07), within airframe structural constraints (Vol 03):

```text
FUEL SELECTION (05.2, criteria) → STORAGE/TANK (05.3/05.4) → DISTRIBUTION (05.5)
  → PUMPS (05.6) → FILTRATION (05.7) → METERING (05.8) → INJECTION (05.9)
  → ENGINES (Vol 04) | monitored via Vol 07 | housed in Vol 03 structure
```

This document (05.1) owns the parent fuel requirements; Chapters 05.3–05.9 derive subsystem requirements from it.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-FRQ-001 | The fuel system shall deliver fuel to the propulsion system across the defined flight envelope (hover, transition, cruise, landing), with flow rates and pressures TBD. | SYS-001, SYS-003 | Analysis + Test |
| REQ-HFPX-FRQ-002 | The fuel system shall deliver fuel meeting defined quality and conditioning criteria (filtration, contamination limits, conditioning state — values TBD) for the selected fuel type. | SYS-001 | Analysis + Test |
| REQ-HFPX-FRQ-003 | The fuel system shall provide knowledge of fuel quantity, pressure, and temperature to the control/monitoring system, with accuracies, ranges, and update rates TBD. | SYS-001, SYS-003 | Analysis + Demonstration |
| REQ-HFPX-FRQ-004 | The fuel system shall implement safety primacy by means of isolability and leak detection/containment provisions, independent of the primary delivery path (thresholds and times TBD). | SYS-003 | Analysis + Test |
| REQ-HFPX-FRQ-005 | Each fuel requirement in this specification shall be traceable to a verification case in the V&V Plan, with verification method and success criteria defined before detailed design approval. | SYS-003 | Inspection |

No capacity, pressure, flow-rate, or temperature value in this document is approved; all are TBD.

## 7. Architecture

Parent allocation: FRQ-001 → distribution/pumps/injection chain (05.5/05.6/05.9); FRQ-002 → filtration/conditioning (05.7) plus selection constraints (05.2); FRQ-003 → quantity/pressure/temperature sensing (05.10–05.12) and metering (05.8); FRQ-004 → leak detection/isolation/safety (05.13–05.15); FRQ-005 → V&V thread (05.16, Vol 22). Authoritative subsystem allocation lives in subsystem documents; this section states derivation intent only.

## 8. Detailed Design

Not applicable — requirements level only. No tank geometry, line sizing, pump selection, filter rating, metering technology, or injector design is specified herein. Detailed design is TBD in Chapters 05.3–05.9 after fuel selection and envelope/budget definition.

## 9. Interfaces

Interface placeholders derived from these requirements: fuel-to-propulsion delivery interface (Vol 04, flow/pressure TBD); fuel-to-control/monitoring data interface (Vol 07: quantity, pressure, temperature, valve/pump status — formats TBD); fuel-to-structure installation interface (Vol 03); fuel-to-electrical power interface (pump/valve/sensor power TBD). Formal ICDs are TBD (Vol 02 pattern).

## 10. Operational Concept

Requirements are exercised through analysis of nominal and off-nominal threads (e.g., normal feed across envelope; degraded feed; leak/isolation demand) under controlled engineering and test conditions only. No operating, handling, refuelling, or ignition procedures are defined in this document. Operational use outside appropriate test, safety, and regulatory controls is out of scope.

## 11. Safety

FRQ-004 encodes safety primacy at requirements level. Further safety requirements derive from Vol 13 analyses (FHA/FMEA/FTA — TBD) and feed Chapters 05.13–05.15. Hazardous-subsystem boundary applies: safety analysis and test methodology only; no fuel-handling or operation instructions outside controlled conditions.

## 12. Performance

Intentionally TBD. No usable-fuel capacity, endurance contribution, flow rate, pressure, temperature limit, or delivery margin is quantified until the ISS-003 energy trade, envelope definition, and propulsion demands (Vol 04) exist. Future revisions reference budgets and models, never invented figures.

## 13. Verification & Validation

FRQ-005 establishes the thread: each FRQ requirement maps to ≥1 V&V case (method stated in §6 table). Strategy: analysis (models) → inspection/demonstration (ground, unmanned) → test (unmanned, controlled range). Verification IDs, rigs, and pass criteria are TBD in the V&V Plan (Vol 22) and Fuel System Testing (05.16). Requirements without a verification method are rejected at SRR.

## 14. Risks

- Requirements written before fuel selection and envelope/budgets exist → high TBD density; mitigation: explicit stub/CONCEPT status, trade-study gate before quantification
- Over-constraining a future fuel choice via implicit assumptions; mitigation: 05.2 owns selection criteria, this document stays fuel-agnostic
- Sensing without accuracy budgets (FRQ-003) delaying control-interface definition; mitigation: placeholder ICD + Vol 07 co-ordination action

## 15. Open Issues

- ISS-003 (energy/fuel trade — blocks quantification of FRQ-001/FRQ-002 and all downstream sizing)
- Envelope definition (blocks FRQ-001 verification envelope)
- V&V Plan cases for FRQ-001..005 (TBD, Vol 22 / 05.16)
- Thresholds/times for isolation and leak response (TBD, Vol 13 → 05.13–05.15)

## 16. Assumptions

- A-FRQ-001: SYS-001/SYS-003 allocation to fuel is stable enough to hold these five parent requirements; validation: SRR review
- A-FRQ-002: Fuel-agnostic requirements can precede fuel selection without rework beyond quantification; validation: DDR review of 05.2 decision

## 17. Dependencies

Depends on SyRS stability (SYS-001/003), ISS-003 trade outcome, propulsion demand definition (Vol 04), control/monitoring interface definition (Vol 07), structural constraints (Vol 03), safety analyses (Vol 13), V&V Plan (Vol 22).

## 18. Traceability

Parents: SYS-001, SYS-003 (table above). Children: HFPX-FUEL-SEL-001 (constrained by, not selected by), HFPX-FUEL-TNK/STO/DIS/PMP/FLT/MTR/INJ-001 subsystem requirements, sensing/safety chapters (05.10–05.15), V&V cases, RTM rows. RTM seed for FRQ-001..005 is added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0 (structure only) — Tranche 4 draft, not baselined. Quantification or fuel selection requires a new revision via change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (Chapter 05.1, 5 requirements) |
