# Cruise Controller

**Document ID:** HFPX-FCS-CRZ-001  
**Revision:** B (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 3 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X cruise controller (Chapter 07.13): cruise stabilisation with aerodynamic plus propulsion lift sharing, command tracking, energy-efficient allocation hooks, envelope protection, and cruise-fault response. All laws, gains, allocations, and limits are TBD.

## 2. Scope

Covers the cruise-regime law set at structure-only level, including stabilisation, commanded manoeuvring, allocation hooks, envelope protection, and fault response. Excludes law selection, gain values, allocation-schedule values, envelope-limit values, and efficiency-metric values — all TBD. No component selected.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (REQ-HFPX-SYS-001); HFPX-CONOPS-001 (CON-001/003); HFPX-ARC-CTL-001 (CTL-001/003/004); HFPX-MIS-REQ-001/002 (MIS-001/002)
- FCR/FCL tier requirements (as allocated, TBD)
- Vol 07 (flight control laws); Vol 13 (safety); Vol 19 (modelling/SIL/HIL); Vol 33 (flight test); ISS-006 (control authority)

## 4. Definitions & Acronyms

- Cruise: wing-borne or partially wing-borne forward flight with aero plus propulsion lift sharing (split TBD).
- Energy-efficient allocation: distribution of lift/thrust demand to minimise energy use within handling/margin constraints (metric TBD).
- Envelope protection: prevention of exceedance of cruise flight-envelope limits (limits TBD).
- FCR/FCL: flight-control-related requirement tiers (allocation TBD).

## 5. System Context

The cruise controller is one of three regime law sets (hover/transition/cruise, all TBD) under the switching supervisor (CTL-001). It takes cruise commands from pilot/operator or guidance plus navigation/airspeed estimates, computes aero-surface and propulsion demand, and distributes via thrust allocation/mixing (owner TBD). The safety computer monitors envelope and margins in parallel with independent stabilisation authority (TBD).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-FCZ-001 | The FCS shall provide cruise stabilisation with aerodynamic plus propulsion lift sharing (split and laws TBD). | SYS-001, CTL-001, CTL-003, FCR-xxx (TBD) | Analysis + SIL/HIL + Test (unmanned) |
| REQ-HFPX-FCZ-002 | The FCS shall provide cruise-command tracking within TBD characteristics (commands and tolerances TBD). | SYS-001, CON-001, CTL-003, MIS-001 | Analysis + SIL/HIL + Test (unmanned) |
| REQ-HFPX-FCZ-003 | The FCS shall provide energy-efficient allocation hooks for cruise lift/thrust distribution (metric and method TBD). | SYS-001, CTL-003, FCL-xxx (TBD) | Analysis + SIL/HIL |
| REQ-HFPX-FCZ-004 | The FCS shall provide cruise-envelope protection preventing exceedance of defined limits (limits TBD). | SYS-001, CON-003, CTL-003, MIS-002 | Analysis + SIL/HIL + Test (unmanned) |
| REQ-HFPX-FCZ-005 | The FCS shall provide a defined cruise-fault response including detection input, reconfiguration or degraded mode, and handover to the safety path (logic TBD). | SYS-001, CON-003, CTL-004, MIS-002 | Analysis + SIL/HIL + Test (unmanned) |

## 7. Architecture

Cruise law set (structure TBD) with inner attitude/yaw channels and outer altitude/velocity loops (all TBD), lift-sharing allocator splitting demand between aero surfaces and propulsion (split TBD), efficiency hooks biasing allocation within margin/handling constraints (TBD), and envelope-protection monitor bounding commands (limits TBD). Fault inputs trigger reconfiguration or degraded cruise modes (TBD) per CTL-004.

## 8. Detailed Design

Not applicable at Tranche 3 draft level. Control laws, gains, filters, allocation schedules, efficiency metrics, protection limits, and allocation matrices are TBD (Vol 07, Vol 19).

## 9. Interfaces

Interfaces to navigation/airspeed estimation, guidance/pilot controls, transition controller (entry/exit), aero-surface and propulsion effectors, thrust allocation/mixing, and safety monitoring are TBD. Each shall be captured in an ICD (02.17) before CDR per ARC-005.

## 10. Operational Concept

Cruise supports en-route flight, commanded manoeuvres, and transition entry/exit (profiles TBD). Normal operation tracks cruise commands within TBD characteristics with efficiency-biased allocation and envelope protection; degraded operation reconfigures or hands over to the safety path per CON-003. No human exposure beyond unmanned test until verified.

## 11. Safety

Loss of cruise stabilisation, envelope exceedance, or mis-allocation between aero and propulsion lift is hazardous: stabilisation with defined lift sharing (FCZ-001), bounded tracking (FCZ-002), constrained efficiency hooks (FCZ-003), envelope protection (FCZ-004), and defined fault response with handover (FCZ-005) plus the independent safety path (ARC-003) mitigate it. No controllability claim is made; all limits TBD pending Vol 07/13 analysis and unmanned test.

## 12. Performance

Cruise tracking accuracy, lift-sharing residuals, efficiency-metric outcomes, protection-conformance residuals, and compute-load budgets are TBD. No speeds, altitudes, rates, or margin values are stated.

## 13. Verification & Validation

Verified by analysis (stability, allocation, protection logic) and SIL/HIL (methods TBD); later validated by unmanned flight test (Vol 19/33). Cruise-fault and envelope-protection cases tested by fault injection (methods TBD).

## 14. Risks

- Lift-sharing split unknown until aero/propulsion trades close; mitigation: explicit allocation hooks with TBD split, verification by analysis/SIL/HIL.
- ISS-006: cruise authority margins unknown, limiting manoeuvre and failure tolerance; mitigation: margin budget holders assigned, stub status explicit.

## 15. Open Issues

Cruise laws and gains TBD; lift-sharing split TBD; efficiency metric and method TBD; envelope limits TBD; cruise-fault thresholds and reconfiguration logic TBD.

## 16. Assumptions


_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SAD (ARC-002/003/004), CTL-001/003/004, yaw/altitude/velocity channels (Ch 07.8–07.10), transition controller (Ch 07.12), Vol 03–06 (aero/propulsion trades, ISS-003/004/007), Vol 07 law sets, Vol 08/16 (compute/sensing), safety view (02.10), Vol 19/33 (SIL/HIL/test).

## 18. Traceability

Parents: SYS-001; CON-001/003; CTL-001/003/004; MIS-001/002; FCR/FCL tier (allocation TBD). Children: Vol 07 detailed cruise design, V&V cases. RTM: REQ-HFPX-FCZ-001..005 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 3 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 3 draft (Chapter 07.13) |
| B | 2026-09-29 | Assumptions removed; all unknowns recorded as TBD (no assumptions raised or relied upon). |
