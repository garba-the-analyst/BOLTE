# Fuel Injection

**Document ID:** HFPX-FUEL-INJ-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the fuel-injection requirements for HFP-X (Chapter 05.9): injection interface to engines, operability across the flight envelope, and injection verification. All flow rates, pressures, patterns, and limits are TBD. Fuel type is not selected (see 05.2).

## 2. Scope

Covers injection-to-engine interface provisions (Vol 04, details TBD), envelope operability provisions (regimes TBD), and injection verification approach. Excludes injector technology selection, engine internal design (Vol 04), metering/distribution/pump/filter internals (05.5–05.8), and test execution (05.16).

> **Hazardous-subsystem boundary.** Content in this document is limited to requirements, architecture, interfaces, test methodology and safety analysis. It shall not contain instructions for constructing, igniting, or operating human-carrying high-energy propulsion outside appropriate engineering, test, safety and regulatory controls. No fuel-handling or operation instructions are provided herein.

## 3. Applicable Documents

- HFPX-FUEL-REQ-001 (parents FRQ-001/005); HFPX-FUEL-SEL-001 (fuel-agnostic constraint)
- HFPX-FUEL-MTR-001 (metered-flow input); Vol 04 propulsion/engines (interface); Vol 13 safety inputs (TBD)

## 4. Definitions & Acronyms

- FNJ: injection ID prefix `REQ-HFPX-FNJ-NNN`
- Injection interface: hydraulic/mechanical/thermal boundary between fuel injection hardware and engines (details TBD)
- Operability: satisfactory injection behaviour across defined envelope regimes and transients under controlled conditions (limits TBD)

## 5. System Context

Injection is the terminal fuel-system stage, delivering metered fuel to engines:

```text
METERING (05.8) → INJECTION (this doc) → ENGINES (Vol 04: combustion/power)
                      ↕ monitoring/faults → Vol 07 (provisions TBD)
```

Injection demands, patterns, and limits derive from Vol 04 engine needs (TBD) and remain fuel-agnostic until the DDR.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-FNJ-001 | The injection subsystem shall implement the injection interface to engines (flows, pressures, mechanical/thermal provisions — all TBD) per Vol 04 allocation. | REQ-HFPX-FRQ-001 | Analysis + Inspection |
| REQ-HFPX-FNJ-002 | The injection subsystem shall provide operability across the defined flight envelope and transients (regimes, margins, relight/turndown provisions — TBD) under controlled conditions. | REQ-HFPX-FRQ-001 | Analysis + Test |
| REQ-HFPX-FNJ-003 | The injection subsystem shall be verifiable by defined injection-verification means (analysis, inspection, spray/flow-test methodology — cases TBD) under controlled conditions. | REQ-HFPX-FRQ-005 | Analysis + Demonstration |

No injection flow, pressure, pattern, or limit value in this document is approved.

## 7. Architecture

Notional injection views (all TBD): injector placement/count per engine; manifold-to-injector routing; monitoring pickups (TBD, Vol 07). Views bound interface and safety analysis only; no injector type, nozzle geometry, or material selection is made herein.

## 8. Detailed Design

Not applicable — CONCEPT requirements only. Injector technology, nozzle design, materials, and thermal management are TBD after fuel selection and Vol 04 engine definition.

## 9. Interfaces

Interface placeholders: injection-to-metering hydraulic interface (05.8, TBD); injection-to-engine interface (Vol 04: flows/pressures/mounting/thermal TBD); injection-to-monitoring interface (Vol 07, TBD). Formal ICDs TBD.

## 10. Operational Concept

Injection analysis (interface budgets, operability regimes, transient logic) under controlled engineering conditions only. No injection-operation, engine-start/combustion, maintenance, or flight procedures are defined herein. All future handling/operation is restricted to appropriate engineering, test, safety, and regulatory controls.

## 11. Safety

Injection-interface and operability provisions (FNJ-001/002) feed Vol 13/Vol 04 safety analysis (mal-distribution, leak/fire, operability-loss hazards — TBD) by change record. Hazardous-subsystem boundary applies: safety analysis and test methodology only.

## 12. Performance

Intentionally TBD. No flow rate, pressure, spray characteristic, turndown, transient, or operability-margin figure is stated. Quantification awaits fuel selection (05.2) and engine definition (Vol 04).

## 13. Verification & Validation

Methods stated in §6 table. Means TBD: interface analysis/inspection, operability analysis, controlled spray/flow tests (05.16, Vol 22). Verification IDs and pass criteria TBD; no test execution is authorised by this document. No ignition or engine-operation testing is authorised by this document.

## 14. Risks

- Interface assumed before Vol 04 engine definition → rework; mitigation: interface-TBD requirement, placeholder ICD only
- Operability required before envelope/fuel known; mitigation: regime-TBD requirement + post-DDR re-verification gate
- Combustion coupling outside fuel-volume scope; mitigation: explicit Vol 04 ownership of combustion behaviour

## 15. Open Issues

- Injection-to-engine interface provisions (TBD, Vol 04)
- Operability regimes, transients, margins (TBD, Vol 04 + envelope)
- Fuel-dependent injection effects (TBD, post-DDR)
- Injection-verification cases (TBD, 05.16 / Vol 22)

## 16. Assumptions

- A-FNJ-001: Injection interface/operability can be required fuel-agnostically as TBD provisions; validation: SRR review
- A-FNJ-002: Vol 04 will own engine-side operability criteria consumed by FNJ-001/002; validation: Vol 04 allocation review

## 17. Dependencies

Depends on 05.1 parents, 05.2 fuel-agnostic constraint, 05.8 metered-flow input, Vol 04 engine definition, Vol 07 monitoring, Vol 13 safety inputs, V&V methodology (Vol 22, 05.16).

## 18. Traceability

Parents: REQ-HFPX-FRQ-001/005 (table above). Children: injection-interface ICD (Vol 04), operability analysis, V&V cases, RTM rows. RTM seed for FNJ-001..003 added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0 (structure only) — Tranche 4 draft, not baselined. Interface quantification or injector selection requires a new revision via change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (Chapter 05.9, 3 requirements) |
