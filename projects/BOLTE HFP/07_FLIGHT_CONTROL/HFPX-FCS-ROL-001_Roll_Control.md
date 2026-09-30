# Roll Control

**Document ID:** HFPX-FCS-ROL-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 3 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the roll-axis control function for HFP-X (Chapter 07.6): stabilisation, command response, authority margins, and fault response. No control-law values are defined.

## 2. Scope

Covers roll-axis behaviour within the attitude/law framework. Effector mechanisms, gains, responses, margins, and fault logic are TBD. Authority values are TBD (ISS-006).

## 3. Applicable Documents

- HFPX-FCS-REQ-001 (FCR-001); HFPX-FCS-LAW-001; HFPX-FCS-ATT-001; HFPX-FCS-ARC-001
- HFPX-ARC-CTL-001 (CTL-001/003); ISS-006 (control authority); Vol 19 (SIL/HIL)

## 4. Definitions & Acronyms

- Roll-axis stabilisation: regulation of roll orientation/motion (mechanisation TBD).
- Differential/allocation: generation of roll moments via differential effectors/allocation (TBD).
- Roll-authority margin: remaining roll capability above demand (values TBD, ISS-006).
- Roll-fault response: defined behaviour on roll-path faults (TBD).

## 5. System Context

Roll control implements the roll component of attitude laws, fed by roll commands and lateral/roll estimates, outputting roll-moment demands to allocation/mixing. Authority budgeting and fault handling coordinate with supervisor and safety path.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-FRO-001 | The FCS shall provide roll-axis stabilisation via defined differential/allocation means (means and criteria TBD). | FCR-001 | Analysis + SIL + HIL (TBD) |
| REQ-HFPX-FRO-002 | The FCS shall provide a defined roll-command response (commands, responses, and conditions TBD). | FCR-001 | Analysis + SIL + Test (TBD) |
| REQ-HFPX-FRO-003 | Roll-authority margins for nominal and failure cases shall be defined (values TBD, ISS-006). | FCR-001, ISS-006 | Analysis (TBD) |
| REQ-HFPX-FRO-004 | The FCS shall execute a defined roll-fault response with annunciation and handover as needed (behaviour TBD). | FCR-004 | Analysis + SIL + HIL (TBD) |

No gains, bandwidths, margins, rates, or limits are stated. All quantitative content is TBD.

## 7. Architecture

Text block diagram:

```
[Roll Commands + Roll Estimates] --> [Roll Laws per Regime (TBD)] --> [Roll-Moment Demand] --> [Differential / Allocation to Effectors (FRO-001, TBD)]
                                                                                                            |
                                              [Authority Margin Budget (FRO-003, TBD, ISS-006)] <---> [Supervisor / Safety] <---> [Roll-Fault Response (FRO-004, TBD)]
```

Mechanisation, allocation mapping, and fault states are TBD.

## 8. Detailed Design

Not applicable at Tranche 3 draft level. Roll law realisation, parameters, and margin budgets are TBD.

## 9. Interfaces

- Roll command/estimate input ICD: TBD.
- Roll-moment to allocation ICD: TBD.
- Authority/fault interface to supervisor/safety ICD: TBD.

## 10. Operational Concept

Roll control operates in all regimes; hover/transition stress differential authority; cruise stresses coordinated response (all TBD). Faults trigger defined degraded response and handover (TBD).

## 11. Safety

Loss of roll stabilisation, inadequate authority, or mishandled roll faults are hazardous. Mitigations required (all TBD): stabilisation (FRO-001), defined response (FRO-002), enforced margins (FRO-003, ISS-006), fault response plus handover (FRO-004). No roll controllability claim is made.

## 12. Performance

Roll response, error, and margin values are TBD. No performance value is stated.

## 13. Verification & Validation

Verified by analysis, SIL/HIL (Vol 19), and test; margin verification by analysis per ISS-006; fault cases by injection (methods and criteria TBD).

## 14. Risks

- Roll effector/authority solution unknown; mitigation: TBD margin budget holders, stub status explicit (ISS-006).
- Fault-response undefined; mitigation: explicit TBD with SIL/HIL validation planned.

## 15. Open Issues

- Mechanisation TBD; response criteria TBD; authority values TBD (ISS-006); fault behaviour TBD.

## 16. Assumptions

- A-FRO-001: Roll moments are generated via allocation to distributed effectors (validation: propulsion/aero trade, TBD).

## 17. Dependencies

Depends on FCR-001/004, law/attitude framework, allocation/mixing, ISS-006, supervisor/safety, Vol 19 rigs.

## 18. Traceability

Parents: FCR-001 (via HFPX-FCS-REQ-001), ISS-006, CTL-003. Children: roll detailed design, SIL/HIL cases, V&V cases. RTM: REQ-HFPX-FRO-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 3 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 3 draft (Chapter 07.6) |
