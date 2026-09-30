# Fuel Metering

**Document ID:** HFPX-FUEL-MTR-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the fuel-metering requirements for HFP-X (Chapter 05.8): metering accuracy provisions, metering-to-control interface, and metering verification. All accuracies, ranges, dynamics, and values are TBD. Fuel type is not selected (see 05.2).

## 2. Scope

Covers metered-flow accuracy and range provisions (values TBD), command/feedback interface to the control system (Vol 07, details TBD), and metering verification approach. Excludes metering technology selection, distribution/pump/filter/injection internals (05.5–05.7, 05.9), control-law design (Vol 07), and test execution (05.16).

> **Hazardous-subsystem boundary.** Content in this document is limited to requirements, architecture, interfaces, test methodology and safety analysis. It shall not contain instructions for constructing, igniting, or operating human-carrying high-energy propulsion outside appropriate engineering, test, safety and regulatory controls. No fuel-handling or operation instructions are provided herein.

## 3. Applicable Documents

- HFPX-FUEL-REQ-001 (parents FRQ-001/003/005); HFPX-FUEL-SEL-001 (fuel-agnostic constraint)
- HFPX-FUEL-FLT-001, -INJ-001 (neighbours); Vol 07 control/monitoring (interface); Vol 04 engine demands (TBD)

## 4. Definitions & Acronyms

- FMT: metering ID prefix `REQ-HFPX-FMT-NNN`
- Metering: controlled apportioning of fuel flow to injection/engines per control commands (accuracies TBD)
- Control interface: command, feedback, and fault-signal boundary between metering hardware and Vol 07 (formats TBD)

## 5. System Context

Metering sits between filtration and injection, closing the loop with the control system and engines:

```text
FILTER (05.7) → METERING (this doc) → INJECTION (05.9) → ENGINES (Vol 04)
                    ↕ commands/feedback/faults → CONTROL (Vol 07)
```

Metering authority, range, and dynamics are TBD pending Vol 04/Vol 07 definition.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-FMT-001 | The metering subsystem shall meter fuel flow within defined accuracy, range, and dynamic provisions (values TBD) across the flight envelope. | REQ-HFPX-FRQ-001 | Analysis + Test |
| REQ-HFPX-FMT-002 | The metering subsystem shall implement the metering-to-control interface (commands, feedback, fault signals — details TBD) per Vol 07 allocation. | REQ-HFPX-FRQ-003 | Analysis + Demonstration |
| REQ-HFPX-FMT-003 | The metering subsystem shall be verifiable by defined metering-verification means (analysis, inspection, flow-test methodology — cases TBD) under controlled conditions. | REQ-HFPX-FRQ-005 | Analysis + Demonstration |

No metering accuracy, range, or dynamic value in this document is approved.

## 7. Architecture

Notional metering views (all TBD): metering-unit placement; command/feedback signal paths; fault-state behaviour (fail-safe provisions TBD, Vol 07/13). Views bound interface and safety analysis only; no valve, sensor, or actuator selection is made herein.

## 8. Detailed Design

Not applicable — CONCEPT requirements only. Metering mechanisms, actuators, sensors, and controllers are TBD after fuel selection and Vol 04/07 demand definition.

## 9. Interfaces

Interface placeholders: metering-to-filtration/injection hydraulic interfaces (05.7/05.9, TBD); metering-to-control interface (Vol 07: commands/feedback/faults, formats TBD); metering-to-power interface (TBD). Formal ICDs TBD.

## 10. Operational Concept

Metering analysis (accuracy budgets, command/response logic, fault states) under controlled engineering conditions only. No metering-operation, calibration, maintenance, or flight procedures are defined herein. All future handling/operation is restricted to appropriate engineering, test, safety, and regulatory controls.

## 11. Safety

Fault-state and annunciation provisions (via FMT-002) feed Vol 13/Vol 07 safety analysis (metering-error, fail-state hazards — TBD) by change record. Hazardous-subsystem boundary applies: safety analysis and test methodology only.

## 12. Performance

Intentionally TBD. No accuracy, turndown, hysteresis, response-time, or drift figure is stated. Quantification awaits fuel selection, engine demands (Vol 04), and control budgets (Vol 07).

## 13. Verification & Validation

Methods stated in §6 table. Means TBD: accuracy-budget analysis, interface demonstration, controlled flow tests (05.16, Vol 22). Verification IDs and pass criteria TBD; no test execution is authorised by this document.

## 14. Risks

- Accuracy required before engine/control budgets exist → rework; mitigation: accuracy-TBD requirement, budget action on Vol 04/07
- Interface assumed before Vol 07 allocation; mitigation: placeholder ICD + joint Vol 07 action
- Fuel-dependent metering behaviour unknown pre-DDR; mitigation: re-verification gate after DDR

## 15. Open Issues

- Metering accuracy/range/dynamics (TBD, Vol 04/07)
- Control-interface signal set and fault states (TBD, Vol 07)
- Fuel-dependent metering effects (TBD, post-DDR)
- Metering-verification cases (TBD, 05.16 / Vol 22)

## 16. Assumptions

- A-FMT-001: Metering can be required fuel-agnostically as accuracy-TBD provisions; validation: SRR review
- A-FMT-002: Vol 07 will own command/fault-state allocation consumed by FMT-002; validation: Vol 07 allocation review

## 17. Dependencies

Depends on 05.1 parents, 05.2 fuel-agnostic constraint, 05.7/05.9 neighbour interfaces, Vol 04 engine demands, Vol 07 control allocation, Vol 13 safety inputs, V&V methodology (Vol 22, 05.16).

## 18. Traceability

Parents: REQ-HFPX-FRQ-001/003/005 (table above). Children: metering accuracy budgets, control ICD (Vol 07), V&V cases, RTM rows. RTM seed for FMT-001..003 added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0 (structure only) — Tranche 4 draft, not baselined. Accuracy quantification or technology selection requires a new revision via change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (Chapter 05.8, 3 requirements) |
