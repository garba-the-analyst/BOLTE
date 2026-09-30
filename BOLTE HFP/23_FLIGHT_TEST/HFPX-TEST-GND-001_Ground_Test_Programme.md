# Ground Test Programme

**Document ID:** HFPX-TEST-GND-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the ground-test programme methodology (Chapter 23.2): scope structure, rig/fixture ownership, pass/fail discipline, ground-to-flight credit rule, and safety/range-control hooks.
This document sets methodology and gating only; it contains no propulsion build, fuel, ignition, or flight-execution instructions.

## 2. Scope

Covers all ground verification: simulation, SIL, HIL, subsystem rigs, and integrated ground testing supporting Vol 23.3–23.9 domain threads.
Excludes flight execution (Vol 23.10–23.14), detailed procedures (child documents, TBD), and range conduct (Vol 25 hooks, TBD).

## 3. Applicable Documents

- HFPX-TEST-STR-001 Test & Evaluation Strategy (gated thread, no-skipping rule)
- HFPX-VV-PLN-001 V&V Plan (REQ-HFPX-VVP-001..006)
- HFPX-PGM-SEM-001 SEMP (DDR-001 gate discipline)
- HFPX-SYS-REQ-001 SyRS (tier allocation TBD)
- Vol 13 / Vol 24 (hazard-derived ground-test obligations, TBD); Vol 25 (range-safety, authorisation — TBD)

## 4. Definitions & Acronyms

- Ground test: any verification executed without free flight, including sim, SIL, HIL, rig, and integrated ground configurations.
- Rig/fixture: ground support equipment, mounts, harnesses, and simulators hosting the article under test.
- Ground-to-flight credit: the documented claim that a ground result satisfies a flight-verification obligation.
- TBD: threshold, list, or assignment not yet defined; no values baselined.

## 5. System Context

Ground testing is the pre-flight portion of the gated thread, feeding unmanned, tethered, human, and expansion stages only through closed gates:

```text
SIM → SIL → HIL → SUBSYSTEM RIGS → INTEGRATED GROUND → [GATE] → FLIGHT STAGES
```

VCRM (Vol 22.3) traces each ground case to its parent requirement, method, level, and credit claim.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-TGD-001 | The ground-test programme shall define its verification scope as an enumerated list of ground-test objectives and threads, with the list recorded as TBD in this revision. | VVP-001 | Inspection |
| REQ-HFPX-TGD-002 | Each ground rig and fixture shall have defined ownership, configuration control, and calibration/adequacy status, with assignments recorded as TBD in this revision. | VVP-003 | Inspection |
| REQ-HFPX-TGD-003 | Every ground-test case shall define pass/fail criteria before execution, with all threshold values recorded as TBD in this revision. | VVP-005 | Test |
| REQ-HFPX-TGD-004 | Ground results claimed as flight-verification credit shall satisfy a documented ground-to-flight credit rule including representativeness, environment coverage, and gate approval, with rule details TBD per claim. | VVP-004 | Analysis |
| REQ-HFPX-TGD-005 | Ground testing involving hazardous energy or constrained operations shall be subject to defined safety and range controls and authorisation, with control details TBD via Vol 25 hooks. | VVP-006 | Demonstration |

All pass/fail thresholds: TBD. No quantitative acceptance values are baselined in this revision.

## 7. Architecture

Ground-test levels: sim environments (TBD), SIL (TBD), HIL (TBD), subsystem rigs per domain (propulsion, fuel, structures, thermal, avionics, software, control — details in 23.3–23.9), integrated ground configuration (TBD).
Organisation and rig ownership TBD. Data/instrumentation interfaces feed Vol 23.16–23.17 (TBD).

## 8. Detailed Design

Scope-list structure (list TBD): per-thread objective, parent requirement(s), article configuration, environment, method (A/I/D/T), entrance/exit criteria, and credit sought.
Rig/fixture record structure (values TBD): owner, configuration baseline, calibration/adequacy status, interface definition, maintenance responsibility.
Credit-rule structure: representativeness argument + environment-coverage mapping + independent review (where safety-relevant) + gate decision; no credit is claimed in this revision.
No procedure in this document directs hazardous operations; controlled-conditions constraints are defined per child document.

## 9. Interfaces

- Ground ↔ VCRM (Vol 22.3: case IDs, methods, levels — TBD).
- Ground ↔ Domain volumes (Vol 03–18: articles, models, ICDs).
- Ground ↔ Flight stages (Vol 23.10–23.14: only via closed gates, no skipping per DDR-001 / VVP-004).
- Ground ↔ Safety/authorisation (Vol 13/24/25: hazard controls, range-safety, authorisation — TBD).

## 10. Operational Concept

Operate lowest-adequate-stage-first: define case and TBD criteria → confirm entrance criteria and article configuration → execute on rig/ground configuration → capture data per data plan → review → gate decision → advance or remediate.
No ground case authorises flight; flight progression requires separate gate and Vol 25 authorisation (TBD).

## 11. Safety

Hazardous ground configurations are subject to safety review and independent verification per VVP-006 (degree TBD). Safety/range controls, abort logic, and authorisation are TBD via Vol 25 hooks. This document contains no hazardous test-execution instructions.

## 12. Performance

Ground-programme indicators TBD (no thresholds baselined): case-definition completeness (TBD), rig-adequacy closure (TBD), first-pass rate (TBD), credit-claim acceptance rate (TBD). Method and cadence TBD.

## 13. Verification & Validation

This document is verified at SRR/PDR against the SEMP checklist (header, 20 sections, IDs, shall-statements, A/I/D/T allocation, credit rule, no-skipping alignment).
Validation is programme-authority approval at gated reviews. Certification validation owned by Vol 25 (no claims here).

## 14. Risks

- Rig/fixture ownership left TBD causing configuration drift; mitigation: REQ-HFPX-TGD-002 ownership rule with gate check (threshold TBD).
- Ground-to-flight over-claim; mitigation: REQ-HFPX-TGD-004 credit rule with representativeness and gate approval.
- Criteria left TBD blocking closure; mitigation: per-case TBD tracking with due gate (assignments TBD).

## 15. Open Issues

Ground-test scope list TBD. Rig/fixture ownership, calibration, and adequacy TBD. All pass/fail thresholds TBD. Credit-rule details TBD per claim. Safety/range controls and authorisation TBD (Vol 25).

## 16. Assumptions

- A-TGD-001: Ground environments can be shown representative for defined credit claims via arguments TBD per claim; validation: independent review.
- A-TGD-002: A single ground-test scope list can span all domain threads; validation: PDR review.

## 17. Dependencies

Depends on HFPX-TEST-STR-001 (thread, gates), V&V Plan (methods, VCRM, independence), SEMP gates, SyRS tier allocation, domain volumes (articles), Vol 23.16–23.17 (instrumentation/data), Vol 25 (safety/authorisation).

## 18. Traceability

Parents: REQ-HFPX-VVP-001..006; HFPX-SYS-REQ-001 (tier allocation TBD); HFPX-TEST-STR-001 (thread). Children: domain ground-test cases in 23.3–23.9 and VCRM rows (IDs TBD).
RTM: REQ-HFPX-TGD-001..005 → CONCEPT. No orphaned requirements in this document.

## 19. Configuration

BL-0.0 (structure only) — Tranche 4 draft, not baselined. CONCEPT. Future changes via change records; changes re-validate affected VCRM rows before gate claims.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (Ch 23.2 Ground Test Programme) |
