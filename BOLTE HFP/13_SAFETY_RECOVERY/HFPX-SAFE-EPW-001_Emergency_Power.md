# Emergency Power

**Document ID:** HFPX-SAFE-EPW-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X emergency-power direction (Chapter 13.16): which safety loads must be powered, how source/switch-over is organised, what endurance is required, and how it is verified by test.
Sets requirements, architecture, and verification direction only; it specifies no voltages, capacities, or hardware selections.

## 2. Scope

Covers emergency power loads, emergency source and switch-over behaviour, and endurance for safety functions across applicable flight and ground-contingency regimes (regimes TBD, with Vol 15.8 inputs).
In scope: emergency-power functional requirements, architectural allocation direction, interface requirements, and test-methodology direction.
Out of scope: primary power detailed design (Vol 15), source hardware selection, and any build or operation instructions.

## 3. Applicable Documents

- Programme Charter STK-001; SyRS SYS-002/003, parent SYS-003; power tier PWR-001..004 (all stubs, values TBD)
- HFPX-SAFE-CAS-001 Safety Case; hazard log (`13_SAFETY_RECOVERY/hazard_log.csv`); HFPX-VV-PLN-001 V&V Plan
- Vol 15 power architecture, §15.8 emergency provisions; Vol 11 operations concept; Vol 13.17 emergency communications (companion load)
- Standards (structured according to): SAE ARP4754A, ARP4761/4761A concepts — no compliance claimed in this revision

## 4. Definitions & Acronyms

- Emergency power: power provided to safety loads upon loss or degradation of primary power, source and capacity TBD
- Safety loads: functions that must remain powered in an emergency, list TBD (includes safety computer, recovery triggers, comms)
- Switch-over: transition from primary to emergency source, logic and timing TBD (Vol 15.8)
- Endurance: duration over which emergency power sustains safety loads, value TBD

## 5. System Context

Emergency power underpins the independent safety path: without it, safety computer, recovery triggers, and emergency comms cannot execute their contingency functions.
Load list, source selection, and switch-over design depend on Vol 15.8 inputs, all TBD; no source or capacity is baselined in this revision.
Endurance must bound the longest contingency sequence requiring powered safety action (sequences TBD); no endurance value is set here.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-EPW-001 | The system shall sustain emergency power to safety loads, with load list TBD (safety computer, recovery triggers, comms). | SYS-003, PWR-001..004 | Test |
| REQ-HFPX-EPW-002 | The system shall provide an emergency source and switch-over behaviour, with source, logic, and timing TBD (Vol 15.8). | SYS-003, PWR-001..004 | Test |
| REQ-HFPX-EPW-003 | The system shall sustain emergency power for a defined endurance, with duration and load profile TBD. | SYS-003, PWR-001..004 | Test |
| REQ-HFPX-EPW-004 | Emergency-power performance shall be verified by test, with test scope, conditions, and acceptance criteria TBD. | SYS-003, PWR-001..004 | Test |

All voltages, currents, capacities, timings, and endurance values: TBD. No emergency-power capability is asserted until demonstrated by test.

## 7. Architecture

Emergency-power allocation TBD across source (TBD), distribution, switch-over logic, load shedding/prioritisation (TBD), and monitoring/annunciation; SAD to allocate with Vol 15.
Safety loads are architecturally identified as a protected load group segregated from non-essential loads to a degree TBD.
Switch-over logic is architecturally segregated from primary power control to a degree TBD; failure annunciation routes to crew/ground via Vol 13.17 paths (details TBD).
> Hazardous-subsystem boundary: architecture here addresses functional allocation and interfaces only; it contains no build or operation instructions.

## 8. Detailed Design

No detailed design in this revision — loads, source, switch-over, and endurance TBD.
Design direction (methodology only): per-load decomposition into power demand (TBD), priority (TBD), and verification case (TBD); switch-over decomposition into detection → transfer → stabilisation → annunciation, each with criteria TBD.
Load-measurement and endurance-analysis methodology TBD with Vol 15.8 and Vol 19 modelling support before any sizing claim.

## 9. Interfaces

- Emergency power ↔ Primary power (Vol 15): source boundary, transfer points, monitoring, details TBD
- Emergency power ↔ Safety computer / recovery triggers: powered-load interfaces, sequencing, details TBD
- Emergency power ↔ Emergency comms (Vol 13.17): comms load interface, priority, details TBD
- Emergency power ↔ Operations (Vol 11): annunciation, crew/ground procedures on transfer, details TBD
- Emergency power ↔ V&V (Vol 22–24): emergency-power test cases and hooks, IDs TBD

## 10. Operational Concept

Test methodology and gating only: this concept defines readiness evidence and transfer-logic structure, not vehicle handling or flight conduct.
Lifecycle direction: load-list definition → source/switch-over definition (Vol 15.8) → analysis → ground test of transfer and endurance → integrated contingency demonstration at a fidelity TBD → Safety Review Board assessment.
No operational emergency-power procedure is authorised in this revision; procedures are TBD and gated by FRR.

## 11. Safety

Loss of emergency power is treated as a safety-path hazard input; associated causes, effects, and mitigations enter the hazard log and analyses (IDs TBD).
No compliance claimed in this revision; no transfer reliability or endurance achievability is asserted until verified by test.
Emergency power shall not take credit for retiring catastrophic hazards until mitigations are verified and retired by the Safety Review Board (criteria TBD).
> Hazardous-subsystem boundary: this section states safety-analysis and gating rules only.

## 12. Performance

Emergency-power performance indicators and thresholds TBD (no values baselined): transfer behaviour TBD, voltage/continuity bounds TBD, endurance TBD, load-priority observance TBD.
No numerical targets are set in this revision; scales and acceptance criteria TBD in later revisions with Vol 13/24 concurrence.

## 13. Verification & Validation

Verification by test for REQ-HFPX-EPW-001..004: load-sustainment tests, switch-over tests, and endurance tests at conditions TBD (bench/vehicle scope TBD per Vol 23).
Acceptance criteria TBD per case; evidence recorded as TBD/empty until closed.
Validation by Safety Review Board plus programme-authority approval at gates; certification validation owned by Vol 25 with no claims here.

## 14. Risks

- Load-list drift: safety loads grow beyond emergency-source assumptions (both TBD); mitigation: protected load list under configuration control once opened, changes via change records
- Switch-over gap: transfer transient defeats safety loads (values TBD); mitigation: no transfer claim until tested across the defined load profile (profile TBD)
- Endurance shortfall: contingency sequence outlasts emergency supply (both TBD); mitigation: endurance tied to Vol 11 contingency sequences, sequences TBD

## 15. Open Issues

Emergency load list undefined. Source and switch-over logic undefined (Vol 15.8 inputs TBD). Endurance undefined. Test scope, conditions, and acceptance criteria undefined. PWR-001..004 values TBD. All emergency-power evidence TBD/empty.

## 16. Assumptions

- Safety loads can be bounded to a protectable set within mass/power budgets TBD; validation: SAD allocation with Vol 15 (TBD)
- Switch-over can be made deterministic and testable without human-flight trials; validation: Vol 23 test methodology (TBD)
- Endurance can be derived from Vol 11 contingency sequences once defined; validation: Vol 11 operations concept (TBD)

## 17. Dependencies

Depends on STK-001/SYS-002/003/PWR-001..004 tiers (requirements basis), Safety Case and hazard analyses (hazard basis), Vol 15.8 (source/switch-over design), Vol 11 (contingency sequences), Vol 13.17 (comms load), Vol 19 (modelling), Vol 22–24 (VCRM and test verification), Vol 25 (certification basis).

## 18. Traceability

Parents: SYS-003, PWR-001..004 (values TBD).
Children: load-level power requirements, switch-over requirements, and test cases (artefact IDs TBD).
RTM: REQ-HFPX-EPW-001..004 → CONCEPT. Each safety load traces to source → switch-over → endurance → test evidence (all TBD except schema).

## 19. Configuration

BL-0.0. Tranche 4 draft, CONCEPT, not baselined. Load-list change, source change, or endurance change requires a change record with affected-requirement and hazard impact stated.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (emergency-power direction; loads/source/endurance TBD) |
