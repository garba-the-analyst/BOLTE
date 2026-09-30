# Velocity Control

**Document ID:** HFPX-FCS-VEL-001  
**Revision:** B (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 3 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X velocity control function (Chapter 07.10): velocity hold/tracking, hover-drift limiting, transition airspeed management hooks, and velocity-fault response. All laws, gains, and thresholds are TBD.

## 2. Scope

Covers horizontal and vertical velocity regulation across hover, transition, and cruise at structure-only level. Excludes law selection, gain values, velocity-error budgets, drift-limit values, and airspeed-schedule values — all TBD. No component selected. No performance claim is made.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (REQ-HFPX-SYS-001); HFPX-CONOPS-001 (CON-001/003); HFPX-ARC-CTL-001 (CTL-003/004); HFPX-MIS-REQ-001/002 (MIS-001/002)
- FCR/FCL tier requirements (as allocated, TBD)
- Vol 07 (flight control laws); Vol 19 (modelling/SIL/HIL); Vol 33 (flight test); ISS-006 (control authority)

## 4. Definitions & Acronyms

- Velocity hold/tracking: regulation of vehicle velocity vector to commanded values (axes and tolerances TBD).
- Hover drift: unintended horizontal displacement in hover (limit values TBD).
- Transition airspeed management: scheduling of velocity commands/limits through conversion (schedule TBD).
- FCR/FCL: flight-control-related requirement tiers (allocation TBD).

## 5. System Context

Velocity control sits within the FCS translational channels: it takes velocity commands from pilot/operator or guidance plus navigation velocity estimates (sensors TBD), computes attitude/thrust-vector demand, and passes it to inner attitude loops and thrust allocation/mixing (owner TBD). It spans hover, transition, and cruise law sets under the switching supervisor (CTL-001), with parallel safety monitoring (TBD).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-FVL-001 | The FCS shall provide velocity-hold and velocity-tracking functions within TBD characteristics (axes, tolerances, and gains TBD). | SYS-001, CTL-003, FCR-xxx (TBD) | Analysis + SIL/HIL + Test (unmanned) |
| REQ-HFPX-FVL-002 | The FCS shall limit hover drift within TBD bounds (limit values and method TBD). | SYS-001, CON-001, CTL-003, MIS-001 | Analysis + SIL/HIL + Test (unmanned) |
| REQ-HFPX-FVL-003 | The FCS shall provide transition airspeed management hooks including command scheduling and limits (schedule TBD). | SYS-001, CON-001, CTL-003, MIS-001 | Analysis + SIL/HIL + Test (unmanned) |
| REQ-HFPX-FVL-004 | The FCS shall provide a defined velocity-fault response including detection input, reconfiguration or degraded mode, and handover to the safety path (logic TBD). | SYS-001, CON-003, CTL-004, MIS-002 | Analysis + SIL/HIL + Test (unmanned) |

## 7. Architecture

Velocity hold/tracking is implemented as outer translational loops feeding inner attitude/vertical channels per regime (all TBD). Hover-drift limiting is a hover-regime subfunction (method TBD). Transition airspeed management interfaces with the transition controller sequencing and law-blending logic (TBD, Ch 07.12). Velocity demand is bounded by authority limits (TBD, ISS-006). Fault inputs trigger the velocity-fault response per REQ-HFPX-FVL-004.

## 8. Detailed Design

Not applicable at Tranche 3 draft level. Control laws, gains, filters, estimators, schedules, thresholds, and allocation matrices are TBD (Vol 07, Vol 19).

## 9. Interfaces

Interfaces to navigation velocity estimates, guidance/pilot controls, attitude/altitude inner loops, transition controller, thrust allocation/mixing, and safety monitoring are TBD. Each shall be captured in an ICD (02.17) before CDR per ARC-005.

## 10. Operational Concept

Velocity control supports station-keeping/drift limiting in hover, commanded translation, conversion-corridor tracking in transition, and speed tracking in cruise (envelopes TBD). Normal operation tracks velocity commands within TBD characteristics; degraded operation reconfigures or hands over to the safety path per CON-003. No human exposure beyond unmanned test until verified.

## 11. Safety

Loss of velocity regulation, uncommanded translation, or transition-corridor exceedance is hazardous: velocity hold/tracking (FVL-001), drift limiting (FVL-002), airspeed management hooks (FVL-003), and defined fault response with safety-path handover (FVL-004) plus the independent safety path (ARC-003) mitigate it. No controllability claim is made; all bounds TBD pending Vol 07/13 analysis and unmanned test.

## 12. Performance

Velocity-tracking accuracy, drift bounds, transition-schedule residuals, and compute-load budgets are TBD. No speeds, rates, or margin values are stated.

## 13. Verification & Validation

Verified by analysis (stability, wind/disturbance sensitivity) and SIL/HIL (methods TBD); later validated by unmanned flight test (Vol 19/33). Velocity-fault response tested by fault injection (methods TBD).

## 14. Risks

- Velocity-estimate integrity dependent on TBD sensor/fusion trade; mitigation: sensing trade and estimator design, TBD.
- ISS-006: authority margins unknown, limiting aggressive velocity manoeuvres; mitigation: margin budget holders assigned, stub status explicit.

## 15. Open Issues

Velocity laws and gains TBD; drift-limit values and method TBD; transition airspeed schedule TBD; velocity-fault thresholds and reconfiguration logic TBD; sensor/fusion allocation TBD.

## 16. Assumptions


_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SAD (ARC-002/003/004), CTL-001/003/004, hover/transition/cruise controllers (Ch 07.11–07.13), Vol 03–06 (aero/propulsion trades, ISS-003/004/007), Vol 07 law sets, Vol 08/16 (compute/sensing), safety view (02.10), Vol 19/33 (SIL/HIL/test).

## 18. Traceability

Parents: SYS-001; CON-001/003; CTL-003/004; MIS-001/002; FCR/FCL tier (allocation TBD). Children: Vol 07 detailed velocity design, V&V cases. RTM: REQ-HFPX-FVL-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 3 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 3 draft (Chapter 07.10) |
| B | 2026-09-29 | Assumptions removed; all unknowns recorded as TBD (no assumptions raised or relied upon). |
