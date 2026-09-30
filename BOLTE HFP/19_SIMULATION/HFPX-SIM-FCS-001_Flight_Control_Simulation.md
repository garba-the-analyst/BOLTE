# Flight-Control Simulation

**Document ID:** HFPX-SIM-FCS-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the flight-control simulation structure and discipline (Chapter 19.8): control-law, mixing, and allocation implementation under test, fault-injection scope, switching-transient checks, sim-to-HIL promotion rule, and no-law-credit-before-sim rule. This document establishes structure only; no capability or feasibility claim rests on any unverified model in this revision.

## 2. Scope

Covers flight-control law, mixing, and allocation representations under test within the FVV thread, fault-injection scope, switching-transient check discipline, promotion discipline from simulation to HIL, and credit gating for control laws. Excludes control-law design (owner TBD), HIL execution (19.9), 6-DOF integration beyond the consumer interface (19.3), and verification execution (Vol 22/23).

## 3. Applicable Documents

- HFPX-VV-PLN-001 V&V Plan (notably REQ-HFPX-VVP-001, REQ-HFPX-VVP-004 gated sim-to-HIL progression)
- HFPX-SYS-REQ-001 SyRS (notably SYS-001, SYS-008)
- HFPX-SIM-STR-001 Digital Engineering Strategy
- HFPX-SIM-SIX-001 6-DOF Simulation (dynamics consumer/producer interface)
- FVV thread definitions (details TBD)
- ISS-006 and ISS-007 actions (details TBD)

## 4. Definitions & Acronyms

- Implementation under test: control-law, mixing, and allocation representation exercised in simulation; revision TBD.
- Fault-injection scope: defined set of injected faults exercised against the control implementation; set TBD.
- Switching-transient checks: defined checks on behaviour across mode or allocation switches; checks TBD.
- FVV: flight-control verification and validation thread (details TBD).
- TBD: to be defined; TBC: to be confirmed.

## 5. System Context

Flight-control simulation exercises the control-law, mixing, and allocation implementation under test within the FVV thread, coupled to 6-DOF dynamics (19.3), under the 19.1 hierarchy and VVP-004 gated progression. Fault injection and switching-transient checks characterise TBD-scoped behaviours. No control law gains gate credit until simulation per this chapter and verification via 19.15 hooks are recorded; promotion to HIL (19.9) is separately gated.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-MFC-001 | The flight-control simulation shall implement the control-law, mixing, and allocation implementation under test within the FVV thread, with implementation revision and configuration recorded as TBD. | SYS-001; ASX tier; ISS-006 | Analysis |
| REQ-HFPX-MFC-002 | The flight-control simulation shall define a fault-injection scope exercised against the implementation under test, with injected faults and configurations recorded as TBD. | SYS-008; VVP-001; ISS-006 | Analysis |
| REQ-HFPX-MFC-003 | The flight-control simulation shall define switching-transient checks across mode and allocation switches, with checks and acceptance treatment recorded as TBD. | SYS-008; ASX tier; ISS-006 | Analysis |
| REQ-HFPX-MFC-004 | The programme shall enforce a sim-to-HIL promotion rule stating the entrance conditions for moving a control implementation from simulation to HIL, with conditions TBD per the gated progression. | VVP-004; VVP-001; ISS-006 | Inspection |
| REQ-HFPX-MFC-005 | The programme shall enforce a no-law-credit-before-sim rule such that no control law receives gate credit until its simulation per this chapter is recorded and verified via 19.15 hooks, with credit status TBD. | VVP-004; SYS-001; ISS-006 | Analysis |

## 7. Architecture

Flight-control simulation architecture (structure only): implementation-under-test layer (REQ-HFPX-MFC-001) within the FVV thread; fault-injection layer (REQ-HFPX-MFC-002); transient-check layer (REQ-HFPX-MFC-003); promotion-gate layer (REQ-HFPX-MFC-004) to HIL (19.9); credit-gate layer (REQ-HFPX-MFC-005) routed via 19.15. Couplings to 6-DOF (19.3) and HIL interfaces TBD.

## 8. Detailed Design

Implementation record TBD: law revision TBD, mixing definition TBD, allocation definition TBD, FVV thread reference TBD, configuration TBD. Fault-injection record TBD: fault list TBD, injection points TBD, configurations TBD, results TBD. Transient-check record TBD: switch definitions TBD, check procedures TBD, acceptance treatment TBD per check, results TBD. Promotion record TBD: entrance conditions TBD, evidence references TBD, gate decision record TBD. Credit record TBD: credit status TBD, verification references TBD.

## 9. Interfaces

- Flight-control sim ↔ FVV thread: implementation and check definitions exchanged (details TBD).
- Flight-control sim ↔ 19.3 6-DOF: dynamics coupling exchanged (interface TBD).
- Flight-control sim ↔ 19.9 HIL: promotion interface governed by REQ-HFPX-MFC-004 (conditions TBD).
- Flight-control sim ↔ 19.13 failure simulation: fault-scope coordination (scope TBD).
- Flight-control sim ↔ 19.15 Model Verification: verification methodology and status for laws, injections, and transient checks.

## 10. Operational Concept

Operates check-ordered: register implementation under test TBD → exercise nominal cases TBD → inject faults per scope TBD → execute switching-transient checks TBD → record results TBD → satisfy promotion rule TBD before HIL → satisfy credit rule TBD before any gate credit. No law is credited before REQ-HFPX-MFC-005 is satisfied. Cadence TBD.

## 11. Safety

No safety-related claim (including handling, failure response, or switch safety) is made from flight-control simulation until verification per 19.15 with independence per VVP-006 (degree TBD). Safety-significant faults and switches are TBD (Vol 13/24 mapping TBD). AI-influenced threads, if any, identify the deterministic bounded function actually exercised (identification TBD).

## 12. Performance

Flight-control simulation performance indicators TBD (no thresholds baselined): implementation-registration completeness TBD, fault-scope definition status TBD, transient-check definition status TBD, promotion-gate compliance TBD, verification closure TBD. Measurement method and reporting cadence TBD.

## 13. Verification & Validation

This document is verified by Inspection against template, header, and requirement discipline. REQ-HFPX-MFC-001..005 are verified by their stated methods applied to the implementation, fault-injection, transient-check, promotion, and credit records. Verification methodology for the simulation is owned by 19.15; execution evidence is owned by Vol 22/23. Validation is programme-authority approval at a gated review (review TBD).

## 14. Risks

- Control implementation cited as proven before simulation is recorded (credit-before-evidence); mitigation: REQ-HFPX-MFC-005 no-law-credit-before-sim rule with 19.15 hooks.
- Promotion to HIL without closing simulation entrance conditions; mitigation: REQ-HFPX-MFC-004 promotion rule under VVP-004 no-skipping posture.
- Switching transients unexamined while mode logic is credited; mitigation: REQ-HFPX-MFC-003 explicit transient checks (checks TBD).

## 15. Open Issues

Implementation under test TBD (revision, configuration, FVV reference). Fault-injection scope TBD. Switching-transient checks and acceptance treatment TBD. Sim-to-HIL promotion conditions TBD. Law-credit status and verification status TBD via 19.15.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on FVV thread definitions (TBD), control-law/mixing/allocation design inputs (TBD), 19.3 dynamics interface (TBD), 19.9 HIL entrance process (TBD), 19.13 fault-scope coordination (TBD), 19.1 authority rule, 19.15 verification methodology, ISS-006 scope, and Vol 22/23 execution.

## 18. Traceability

Parents: VVP-001, VVP-004; SYS-001, SYS-008; ASX tier (details TBD); ISS-006, ISS-007 actions. Children: implementation records, fault-injection records, transient-check records, promotion records, verification cases (IDs TBD; rows TBD). RTM: REQ-HFPX-MFC-001..005 → CONCEPT. No capability or feasibility claim in this document rests on an unverified model; authority for any such future claim routes via 19.15.

## 19. Configuration

BL-0.0. Tranche 5 draft, CONCEPT, not baselined. Future changes via change records; any change re-validates affected traceability before gate claims.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 draft (19.8 flight-control structure; requirements REQ-HFPX-MFC-001..005) |
