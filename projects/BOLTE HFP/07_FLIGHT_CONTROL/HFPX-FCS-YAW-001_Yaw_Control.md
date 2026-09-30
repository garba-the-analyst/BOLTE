# Yaw Control

**Document ID:** HFPX-FCS-YAW-001  
**Revision:** B (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 3 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X yaw-axis control function (Chapter 07.8): yaw stabilisation, yaw-command response, yaw-authority margin hooks, and yaw-fault response. All laws, gains, thresholds, and margin values are TBD.

## 2. Scope

Covers yaw-axis stabilisation and command tracking across hover, transition, and cruise regimes at structure-only level. Excludes control law selection, gain values, response-rate values, and authority-margin values — all TBD. No component selected. No controllability claim is made.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (REQ-HFPX-SYS-001); HFPX-CONOPS-001 (CON-001/003); HFPX-ARC-CTL-001 (CTL-003/004); HFPX-MIS-REQ-001/002 (MIS-001/002)
- FCR/FCL tier requirements (as allocated, TBD)
- Vol 07 (flight control laws); Vol 19 (modelling/SIL/HIL); Vol 33 (flight test); ISS-006 (control authority)
- HFP prompt §§11–13 (control view, flight modes)

## 4. Definitions & Acronyms

- Yaw axis: rotation about the vehicle vertical axis (sign convention TBD).
- Yaw stabilisation: active rejection of yaw disturbances to hold commanded heading/rate (values TBD).
- Yaw authority margin: remaining yaw control capability above trim/manoeuvre demand (values TBD, ISS-006).
- FCR/FCL: flight-control-related requirement tiers (allocation TBD).
- SIL/HIL: software/hardware-in-the-loop (methods TBD).

## 5. System Context

Yaw control sits within the FCS law set: it takes heading/yaw-rate commands from pilot/operator or outer loops plus navigation/attitude estimates, computes yaw-moment demand, and passes it to thrust allocation/mixing (owner TBD). It operates across hover, transition, and cruise law sets under the switching supervisor (CTL-001). The safety computer monitors yaw behaviour in parallel with independent stabilisation authority (TBD).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-FYW-001 | The FCS shall provide yaw-axis stabilisation across all flight regimes (method and gains TBD). | SYS-001, CTL-003, FCR-xxx (TBD) | Analysis + SIL/HIL + Test (unmanned) |
| REQ-HFPX-FYW-002 | The FCS shall provide yaw-command response to pilot/operator or outer-loop commands within TBD response characteristics (all thresholds TBD). | SYS-001, CON-001, CTL-003, MIS-001 | Analysis + SIL/HIL + Test (unmanned) |
| REQ-HFPX-FYW-003 | The FCS shall enforce yaw-authority margins for each regime and failure case (values and budgets TBD, ISS-006). | SYS-001, CTL-003, FCL-xxx (TBD) | Analysis + SIL/HIL |
| REQ-HFPX-FYW-004 | The FCS shall provide a defined yaw-fault response including detection input, reconfiguration or degraded mode, and handover to the safety path (logic TBD). | SYS-001, CON-003, CTL-004, MIS-002 | Analysis + SIL/HIL + Test (unmanned) |

## 7. Architecture

Yaw stabilisation is implemented as a yaw channel within each regime law set (hover/transition/cruise, all TBD) plus a common yaw-command shaping path (TBD). Yaw-moment demand feeds the allocation/mixing function within authority limits (TBD). Authority-margin hooks (ISS-006) expose remaining yaw capability to monitoring and the switching supervisor. Fault inputs from health monitoring trigger the yaw-fault response per REQ-HFPX-FYW-004. Switching between regime yaw structures follows CTL-001 switching logic (TBD).

## 8. Detailed Design

Not applicable at Tranche 3 draft level. Control laws, gains, filters, command shaping, thresholds, and allocation matrices are TBD (Vol 07, Vol 19).

## 9. Interfaces

Interfaces to attitude/heading estimation, pilot/operator controls, outer-loop guidance, thrust allocation/mixing, propulsion effectors, and safety monitoring are TBD. Each shall be captured in an ICD (02.17) before CDR per ARC-005.

## 10. Operational Concept

Yaw control supports all flight modes requiring heading hold, commanded turns, and crosswind/disturbance rejection (conditions TBD). Normal operation tracks yaw commands within TBD characteristics; degraded operation reconfigures or hands over to the safety path per CONOPS CON-003. No human exposure beyond unmanned test until verified (Vol 33).

## 11. Safety

Loss of yaw stabilisation, uncommanded yaw, or yaw hardover is hazardous: stabilisation (FYW-001), enforced margins (FYW-003, ISS-006), and defined fault response with safety-path handover (FYW-004) plus the independent safety path (ARC-003) mitigate it. No controllability or handling-qualities claim is made; all margins and thresholds TBD pending Vol 07/13 analysis and unmanned test.

## 12. Performance

Yaw tracking error, disturbance rejection, command-response characteristics, and compute-load budgets are TBD. No gains, rates, or margin values are stated.

## 13. Verification & Validation

Verified by analysis (stability, margin budgets) and SIL/HIL (methods TBD); later validated by unmanned flight test (Vol 19/33). Yaw-fault response tested by fault injection (methods TBD). Human-rated validation is out of scope for this draft.

## 14. Risks

- ISS-006: yaw-authority margins unknown until aero/propulsion trades close; mitigation: margin budget holders assigned, stub status explicit, verification by analysis/SIL/HIL.
- Cross-coupling between yaw and roll/pitch/thrust channels destabilising hover/transition; mitigation: integrated law design and unmanned test first, laws TBD.

## 15. Open Issues

Yaw laws and gains TBD; yaw-command response characteristics TBD; yaw-authority margin values and budgets TBD (ISS-006); yaw-fault detection thresholds and reconfiguration logic TBD; sensor allocation TBD.

## 16. Assumptions


_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SAD (ARC-002/003/004), CTL-001/003/004, Vol 03–06 (aero/propulsion trades, ISS-003/004/007), Vol 07 law sets, Vol 08/16 (compute/sensing), safety view (02.10), data view (02.11), Vol 19/33 (SIL/HIL/test).

## 18. Traceability

Parents: SYS-001; CON-001/003; CTL-003/004; MIS-001/002; FCR/FCL tier (allocation TBD). Children: Vol 07 detailed yaw design, V&V cases. RTM: REQ-HFPX-FYW-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 3 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 3 draft (Chapter 07.8) |
| B | 2026-09-29 | Assumptions removed; all unknowns recorded as TBD (no assumptions raised or relied upon). |
