# Pitch Control

**Document ID:** HFPX-FCS-PIT-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 3 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the pitch-axis control function for HFP-X (Chapter 07.7): stabilisation (transition-critical), command response, authority margins, and fault response. No control-law values are defined.

## 2. Scope

Covers pitch-axis behaviour within the attitude/law framework, with emphasis on transition. Effector mechanisms, gains, responses, margins, and fault logic are TBD. Authority values are TBD (ISS-006).

## 3. Applicable Documents

- HFPX-FCS-REQ-001 (FCR-001); HFPX-FCS-LAW-001; HFPX-FCS-ATT-001; HFPX-FCS-ARC-001
- HFPX-ARC-CTL-001 (CTL-001/003); ISS-006 (control authority); Vol 19 (SIL/HIL)

## 4. Definitions & Acronyms

- Pitch-axis stabilisation: regulation of pitch orientation/motion, transition-critical (mechanisation TBD).
- Pitch-command response: following of pitch commands (criteria TBD).
- Pitch-authority margin: remaining pitch capability above demand (values TBD, ISS-006).
- Pitch-fault response: defined behaviour on pitch-path faults (TBD).

## 5. System Context

Pitch control implements the pitch component of attitude laws, fed by pitch commands and longitudinal/pitch estimates, outputting pitch-moment demands to allocation/mixing. Transition switching and authority budgeting are coordinated with the supervisor and safety path.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-FPI-001 | The FCS shall provide pitch-axis stabilisation across hover, transition, and cruise, with transition behaviour explicitly addressed (means and criteria TBD). | FCR-001 | Analysis + SIL + HIL (TBD) |
| REQ-HFPX-FPI-002 | The FCS shall provide a defined pitch-command response (commands, responses, and conditions TBD). | FCR-001 | Analysis + SIL + Test (TBD) |
| REQ-HFPX-FPI-003 | Pitch-authority margins for nominal and failure cases, including transition, shall be defined (values TBD, ISS-006). | FCR-001, ISS-006 | Analysis (TBD) |
| REQ-HFPX-FPI-004 | The FCS shall execute a defined pitch-fault response with annunciation and handover as needed (behaviour TBD). | FCR-004 | Analysis + SIL + HIL (TBD) |

No gains, bandwidths, margins, rates, or limits are stated. All quantitative content is TBD.

## 7. Architecture

Text block diagram:

```
[Pitch Commands + Pitch Estimates] --> [Pitch Laws per Regime incl. Transition (TBD)] --> [Pitch-Moment Demand] --> [Allocation to Effectors (TBD)]
                                                                                                                  |
                                              [Authority Margin Budget incl. Transition (FPI-003, TBD, ISS-006)] <---> [Supervisor / Safety] <---> [Pitch-Fault Response (FPI-004, TBD)]
```

Mechanisation, transition blending, and fault states are TBD.

## 8. Detailed Design

Not applicable at Tranche 3 draft level. Pitch law realisation, parameters, and margin budgets are TBD.

## 9. Interfaces

- Pitch command/estimate input ICD: TBD.
- Pitch-moment to allocation ICD: TBD.
- Authority/fault interface to supervisor/safety ICD: TBD.

## 10. Operational Concept

Pitch control operates in all regimes with transition as the sizing case for switching and authority (criteria TBD). Faults trigger defined degraded response and handover (TBD).

## 11. Safety

Loss of pitch stabilisation (especially in transition), inadequate authority, or mishandled pitch faults are hazardous. Mitigations required (all TBD): stabilisation (FPI-001), defined response (FPI-002), enforced margins incl. transition (FPI-003, ISS-006), fault response plus handover (FPI-004). No pitch controllability claim is made.

## 12. Performance

Pitch response, error, and margin values are TBD. No performance value is stated.

## 13. Verification & Validation

Verified by analysis, SIL/HIL (Vol 19) with transition cases, and test; margin verification by analysis per ISS-006; fault cases by injection (methods and criteria TBD).

## 14. Risks

- Transition pitch authority/stability unknown; mitigation: TBD margin budgets and transition-specific SIL/HIL planned (ISS-006).
- Fault-response undefined; mitigation: explicit TBD with validation planned.

## 15. Open Issues

- Mechanisation TBD; response criteria TBD; authority values incl. transition TBD (ISS-006); fault behaviour TBD.

## 16. Assumptions

- A-FPI-001: Transition is the sizing case for pitch authority and switching (validation: aero/propulsion trade + Vol 19, TBD).

## 17. Dependencies

Depends on FCR-001/004, law/attitude framework, allocation/mixing, ISS-006, supervisor/safety, Vol 19 rigs.

## 18. Traceability

Parents: FCR-001 (via HFPX-FCS-REQ-001), ISS-006, CTL-003. Children: pitch detailed design, SIL/HIL cases, V&V cases. RTM: REQ-HFPX-FPI-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 3 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 3 draft (Chapter 07.7) |
