# Altitude Control

**Document ID:** HFPX-FCS-ALT-001  
**Revision:** B (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 3 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X altitude control function (Chapter 07.9): altitude hold, climb/descent command tracking, ground-effect handling hooks, and altitude-fault response. All laws, gains, thresholds, and sensor selections are TBD.

## 2. Scope

Covers vertical-position hold and commanded climb/descent across hover, transition, and cruise at structure-only level. Excludes law selection, gain values, climb/descent-rate values, altitude-error budgets, and sensor choices — all TBD. Ground-effect modelling detail is owned by Vol 06.18. No component selected.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (REQ-HFPX-SYS-001); HFPX-CONOPS-001 (CON-001/003); HFPX-ARC-CTL-001 (CTL-003/004); HFPX-MIS-REQ-001/002 (MIS-001/002)
- FCR/FCL tier requirements (as allocated, TBD)
- Vol 06.18 (ground effect); Vol 07 (flight control laws); Vol 19 (modelling/SIL/HIL); Vol 33 (flight test); ISS-006 (control authority)

## 4. Definitions & Acronyms

- Altitude hold: active maintenance of commanded altitude/height (reference and tolerances TBD).
- Climb/descent command: outer-loop or pilot vertical-speed/altitude command path (values TBD).
- Ground effect: change in lift/thrust behaviour near the ground (model TBD, Vol 06.18).
- FCR/FCL: flight-control-related requirement tiers (allocation TBD).

## 5. System Context

Altitude control sits within the FCS vertical channel: it takes altitude/height commands plus vertical-position/velocity estimates from navigation (sensors TBD), computes collective/thrust demand, and passes it to thrust allocation/mixing (owner TBD). It interfaces with ground-effect compensation hooks (Vol 06.18) and the safety monitor with independent stabilisation authority (TBD).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-FAL-001 | The FCS shall provide an altitude-hold function using TBD sensors and estimates (sensor set and tolerances TBD). | SYS-001, CTL-003, FCR-xxx (TBD) | Analysis + SIL/HIL + Test (unmanned) |
| REQ-HFPX-FAL-002 | The FCS shall provide climb/descent command tracking within TBD response characteristics (all thresholds TBD). | SYS-001, CON-001, CTL-003, MIS-001 | Analysis + SIL/HIL + Test (unmanned) |
| REQ-HFPX-FAL-003 | The FCS shall provide ground-effect handling hooks consistent with Vol 06.18 (compensation method TBD). | SYS-001, CTL-003, FCL-xxx (TBD) | Analysis + SIL/HIL + Test (unmanned) |
| REQ-HFPX-FAL-004 | The FCS shall provide a defined altitude-fault response including detection input, reconfiguration or degraded mode, and handover to the safety path (logic TBD). | SYS-001, CON-003, CTL-004, MIS-002 | Analysis + SIL/HIL + Test (unmanned) |

## 7. Architecture

Altitude hold and climb/descent tracking are implemented as the vertical channel of each regime law set (all TBD) with a common altitude-command shaping path (TBD). Vertical demand feeds allocation/mixing within authority limits (TBD, ISS-006). Ground-effect hooks adjust vertical demand or gains per Vol 06.18 model output (method TBD). Fault inputs trigger the altitude-fault response per REQ-HFPX-FAL-004.

## 8. Detailed Design

Not applicable at Tranche 3 draft level. Control laws, gains, filters, sensor fusion, thresholds, and allocation matrices are TBD (Vol 07, Vol 19).

## 9. Interfaces

Interfaces to barometric/inertial/radio-height sensing (set TBD), navigation/fusion, pilot/operator controls, guidance, thrust allocation/mixing, propulsion effectors, and safety monitoring are TBD. Each shall be captured in an ICD (02.17) before CDR per ARC-005.

## 10. Operational Concept

Altitude control supports hover hold, climb/descent, transition profiles, cruise altitude tracking, and landing descent (profiles TBD). Normal operation tracks altitude/vertical commands within TBD characteristics including ground-effect compensation near the surface; degraded operation reconfigures or hands over to the safety path per CON-003. No human exposure beyond unmanned test until verified.

## 11. Safety

Loss of altitude hold, uncommanded climb/descent, or ground-effect-induced instability is hazardous: altitude hold (FAL-001), bounded command tracking (FAL-002), ground-effect hooks (FAL-003), and defined fault response with safety-path handover (FAL-004) plus the independent safety path (ARC-003) mitigate it. No controllability claim is made; all thresholds TBD pending Vol 06/07/13 analysis and unmanned test.

## 12. Performance

Altitude-hold accuracy, climb/descent tracking characteristics, ground-effect compensation residual, and compute-load budgets are TBD. No altitudes, rates, or margin values are stated.

## 13. Verification & Validation

Verified by analysis (stability, sensor-error sensitivity) and SIL/HIL including ground-effect models (methods TBD); later validated by unmanned flight test (Vol 19/33). Altitude-fault response tested by fault injection (methods TBD).

## 14. Risks

- Ground-effect behaviour unknown until Vol 06.18 closes; mitigation: explicit hooks with TBD compensation, verification by analysis/SIL/HIL.
- Sensor-suite uncertainty (sensors TBD) driving altitude-estimate integrity; mitigation: sensor trade and fusion design, TBD.

## 15. Open Issues

Altitude laws and gains TBD; sensor set TBD; climb/descent response characteristics TBD; ground-effect compensation method TBD (Vol 06.18); altitude-fault thresholds and reconfiguration logic TBD.

## 16. Assumptions


_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SAD (ARC-002/003/004), CTL-001/003/004, Vol 03–06 (aero/propulsion/sensing trades, ISS-003/004/007; esp. Vol 06.18), Vol 07 law sets, Vol 08/16 (compute/sensing), safety view (02.10), Vol 19/33 (SIL/HIL/test).

## 18. Traceability

Parents: SYS-001; CON-001/003; CTL-003/004; MIS-001/002; FCR/FCL tier (allocation TBD). Children: Vol 07 detailed altitude design, V&V cases. RTM: REQ-HFPX-FAL-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 3 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 3 draft (Chapter 07.9) |
| B | 2026-09-29 | Assumptions removed; all unknowns recorded as TBD (no assumptions raised or relied upon). |
