# Hover Controller

**Document ID:** HFPX-FCS-HOV-001  
**Revision:** B (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 3 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X hover controller (Chapter 07.11): hover stabilisation on distributed thrust, hover-manoeuvre bounds, entry/exit criteria, abort-to-landing path, and unmanned-first verification. All laws, gains, bounds, and criteria are TBD.

## 2. Scope

Covers the hover-regime law set at structure-only level, including stabilisation, bounded manoeuvring, transitions into/out of hover, and abort to landing. Excludes law selection, gain values, manoeuvre-box values, entry/exit threshold values, and abort-sequence detail — all TBD. No component selected.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (REQ-HFPX-SYS-001); HFPX-CONOPS-001 (CON-001/003); HFPX-ARC-CTL-001 (CTL-001/003/004); HFPX-MIS-REQ-001/002 (MIS-001/002)
- FCR/FCL tier requirements (as allocated, TBD)
- Vol 07 (flight control laws); Vol 13 (safety); Vol 19 (modelling/SIL/HIL); Vol 33 (flight test); ISS-006 (control authority)

## 4. Definitions & Acronyms

- Hover: sustained flight with near-zero translational velocity supported by distributed thrust (bounds TBD).
- Manoeuvre box: bounded volume/attitude/velocity region for hover manoeuvring (values TBD).
- Entry/exit criteria: conditions for engaging or leaving hover control (thresholds TBD).
- Abort to landing: commanded transition from hover to vertical landing (sequence TBD).
- FCR/FCL: flight-control-related requirement tiers (allocation TBD).

## 5. System Context

The hover controller is one of three regime law sets (hover/transition/cruise, all TBD) under the switching supervisor (CTL-001). It takes pilot/operator or guidance hover commands plus navigation estimates, computes attitude/vertical/yaw demand, and distributes via thrust allocation/mixing to propulsion modules (owner TBD). The safety computer monitors hover margins in parallel with independent stabilisation authority (TBD).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-FHV-001 | The FCS shall provide hover stabilisation on distributed thrust across TBD conditions (laws and gains TBD). | SYS-001, CTL-001, CTL-003, FCR-xxx (TBD) | Analysis + SIL/HIL + Test (unmanned) |
| REQ-HFPX-FHV-002 | The FCS shall constrain hover manoeuvring within a defined hover-manoeuvre box (bounds TBD). | SYS-001, CON-001, CTL-003, MIS-001 | Analysis + SIL/HIL + Test (unmanned) |
| REQ-HFPX-FHV-003 | The FCS shall enforce hover entry and exit criteria including regime, health, and margin gates (criteria TBD). | SYS-001, CON-001, CTL-001, MIS-001 | Analysis + SIL/HIL + Test (unmanned) |
| REQ-HFPX-FHV-004 | The FCS shall provide a hover abort-to-landing path with defined sequencing and safety handover (sequence TBD). | SYS-001, CON-003, CTL-004, MIS-002 | Analysis + SIL/HIL + Test (unmanned) |
| REQ-HFPX-FHV-005 | The hover controller shall be verified by analysis and SIL/HIL and validated by unmanned flight test before any human exposure (methods TBD). | SYS-001, CON-003, CTL-004, MIS-002 | Analysis + SIL/HIL + Test (unmanned) |

## 7. Architecture

Hover law set (structure TBD) with inner attitude/vertical/yaw channels and outer position/velocity loops (all TBD), bounded by the manoeuvre box and authority limits (TBD, ISS-006). Entry/exit gates feed the switching supervisor; abort-to-landing hands over to the landing controller (Ch 07.14) or safety path. Fault inputs from health monitoring trigger reconfiguration or degraded hover modes (TBD) per CTL-004.

## 8. Detailed Design

Not applicable at Tranche 3 draft level. Control laws, gains, filters, box bounds, gate thresholds, abort sequences, and allocation matrices are TBD (Vol 07, Vol 19).

## 9. Interfaces

Interfaces to navigation estimates, pilot/operator controls, guidance, transition controller (entry/exit), landing controller (abort), thrust allocation/mixing, propulsion effectors, and safety monitoring are TBD. Each shall be captured in an ICD (02.17) before CDR per ARC-005.

## 10. Operational Concept

Hover supports takeoff, station-keeping, low-speed manoeuvre, hover-to-transition departure, and abort to landing (profiles TBD). Normal operation stays within the manoeuvre box and entry/exit gates; off-nominal operation aborts to landing or hands over to the safety path per CON-003. All hover validation is unmanned first (Vol 33).

## 11. Safety

Loss of hover stabilisation, box exceedance, or failed abort is hazardous: stabilisation (FHV-001), bounded manoeuvring (FHV-002), gated entry/exit (FHV-003), abort path with handover (FHV-004), and unmanned-first validation (FHV-005) plus the independent safety path (ARC-003) mitigate it. No controllability claim is made; all bounds TBD pending Vol 07/13 analysis and unmanned test.

## 12. Performance

Hover tracking accuracy, disturbance rejection, box-conformance residuals, switching transients, and compute-load budgets are TBD. No gains, rates, or margin values are stated.

## 13. Verification & Validation

Verified by analysis (stability, margin budgets, gate logic) and SIL/HIL (methods TBD); validated by unmanned flight test before any human exposure (Vol 19/33). Abort and fault cases tested by fault injection (methods TBD).

## 14. Risks

- ISS-006: hover authority margins unknown until aero/propulsion trades close — hover is the limiting regime; mitigation: margin budget holders assigned, stub status explicit.
- Distributed-thrust failure reducing hover controllability; mitigation: fault-tolerant hooks and abort path, laws TBD.

## 15. Open Issues

Hover laws and gains TBD; manoeuvre-box bounds TBD; entry/exit criteria TBD; abort-to-landing sequence TBD; distributed-thrust failure responses TBD; unmanned test scope/methods TBD.

## 16. Assumptions


_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SAD (ARC-002/003/004), CTL-001/003/004, yaw/altitude/velocity channels (Ch 07.8–07.10), transition/cruise/landing controllers (Ch 07.12–07.14), Vol 03–06 (aero/propulsion trades, ISS-003/004/007), Vol 07 law sets, Vol 08/16 (compute/sensing), safety view (02.10), Vol 19/33 (SIL/HIL/test).

## 18. Traceability

Parents: SYS-001; CON-001/003; CTL-001/003/004; MIS-001/002; FCR/FCL tier (allocation TBD). Children: Vol 07 detailed hover design, V&V cases. RTM: REQ-HFPX-FHV-001..005 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 3 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 3 draft (Chapter 07.11) |
| B | 2026-09-29 | Assumptions removed; all unknowns recorded as TBD (no assumptions raised or relied upon). |
