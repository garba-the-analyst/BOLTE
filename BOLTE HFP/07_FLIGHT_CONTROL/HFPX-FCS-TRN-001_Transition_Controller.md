# Transition Controller

**Document ID:** HFPX-FCS-TRN-001  
**Revision:** B (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 3 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X transition controller (Chapter 07.12): hover↔cruise conversion sequencing, law-blending/switching, entry/exit/abort criteria, failed-transition safe response, and unmanned-first verification. All sequences, laws, blends, and criteria are TBD.

## 2. Scope

Covers conversion between hover and cruise regimes at structure-only level, including sequencing, blending/switching between law sets, gating criteria, abort paths, and failure responses. Excludes law selection, blend/switch threshold values, corridor values, and sequence timing — all TBD. No component selected.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (REQ-HFPX-SYS-001); HFPX-CONOPS-001 (CON-001/003); HFPX-ARC-CTL-001 (CTL-001/003/004); HFPX-MIS-REQ-001/002 (MIS-001/002)
- FCR/FCL tier requirements (as allocated, TBD)
- Vol 07 (flight control laws); Vol 13 (safety); Vol 19 (modelling/SIL/HIL); Vol 33 (flight test); ISS-006 (control authority)

## 4. Definitions & Acronyms

- Transition/conversion: flight phase converting between hover-borne and cruise-borne lift (direction and corridor TBD).
- Law blending/switching: continuous or discrete changeover between hover and cruise law sets (method TBD).
- Entry/exit/abort criteria: gated conditions for starting, completing, or aborting transition (thresholds TBD).
- Failed transition: inability to complete conversion within gates (response TBD).
- FCR/FCL: flight-control-related requirement tiers (allocation TBD).

## 5. System Context

The transition controller supervises hover and cruise law sets (both TBD) under the CTL-001 switching supervisor. It takes conversion commands plus navigation/airspeed estimates (sensors TBD), sequences effector/lift-sharing changes with propulsion and aero surfaces (TBD), and monitors corridor/margin gates. The safety computer monitors conversion in parallel with independent stabilisation authority and abort backstop (TBD).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-FTN-001 | The FCS shall provide hover↔cruise conversion sequencing covering nominal conversion in both directions (sequence TBD). | SYS-001, CON-001, CTL-001, MIS-001 | Analysis + SIL/HIL + Test (unmanned) |
| REQ-HFPX-FTN-002 | The FCS shall provide law-blending or law-switching between hover and cruise law sets with defined transients (method TBD). | SYS-001, CTL-001, CTL-003, FCR-xxx (TBD) | Analysis + SIL/HIL + Test (unmanned) |
| REQ-HFPX-FTN-003 | The FCS shall enforce transition entry, exit, and abort criteria including regime, health, and margin gates (criteria TBD). | SYS-001, CON-001, CTL-001, MIS-001 | Analysis + SIL/HIL + Test (unmanned) |
| REQ-HFPX-FTN-004 | The FCS shall provide a failed-transition safe response including revert-or-hold logic and handover to the safety path (logic TBD). | SYS-001, CON-003, CTL-004, MIS-002 | Analysis + SIL/HIL + Test (unmanned) |
| REQ-HFPX-FTN-005 | Transition shall be verified by analysis and SIL/HIL and validated by unmanned flight test before any human exposure (methods TBD). | SYS-001, CON-003, CTL-004, MIS-002 | Analysis + SIL/HIL + Test (unmanned) |

## 7. Architecture

Transition sequencer (TBD) driving staged conversion steps, law-blending/switching block between hover and cruise structures (method TBD, hysteresis TBD), gate monitor for entry/exit/abort criteria, and failed-transition handler reverting to hover/cruise hold or safety handover (logic TBD). Conversion demand feeds thrust allocation/mixing and lift-sharing effectors within authority limits (TBD, ISS-006). Fault inputs trigger reconfiguration per CTL-004.

## 8. Detailed Design

Not applicable at Tranche 3 draft level. Sequences, laws, blends, switches, thresholds, corridors, and allocation matrices are TBD (Vol 07, Vol 19).

## 9. Interfaces

Interfaces to hover/cruise controllers, navigation/airspeed estimation, guidance/pilot controls, thrust allocation/mixing, propulsion and aero effectors, and safety monitoring are TBD. Each shall be captured in an ICD (02.17) before CDR per ARC-005.

## 10. Operational Concept

Transition supports outbound (hover-to-cruise) and inbound (cruise-to-hover) conversion plus aborted conversion (profiles TBD). Normal operation sequences through gates within TBD characteristics; off-nominal operation executes the failed-transition safe response or hands over to the safety path per CON-003. All conversion validation is unmanned first (Vol 33).

## 11. Safety

Uncommanded switching, corridor exceedance, or failed conversion is hazardous: defined sequencing (FTN-001), bounded blending/switching (FTN-002), gated entry/exit/abort (FTN-003), failed-transition safe response with handover (FTN-004), and unmanned-first validation (FTN-005) plus the independent safety path (ARC-003) mitigate it. No controllability claim is made; all criteria TBD pending Vol 07/13 analysis and unmanned test.

## 12. Performance

Conversion tracking characteristics, blending/switching transients, gate-conformance residuals, and compute-load budgets are TBD. No speeds, rates, or margin values are stated.

## 13. Verification & Validation

Verified by analysis (switching stability, gate logic, margin budgets) and SIL/HIL with conversion models (methods TBD); validated by unmanned flight test before any human exposure (Vol 19/33). Failed-transition and fault cases tested by fault injection (methods TBD).

## 14. Risks

- ISS-006 (LIMITING): transition authority margins unknown until aero/propulsion trades close — insufficient margin may prevent safe conversion or failed-transition recovery; mitigation: margin budget holders assigned, conversion stub explicit, no human exposure until unmanned validation.
- Blending/switching transients destabilising conversion; mitigation: abort criteria and safety-path backstop, methods TBD.

## 15. Open Issues

Conversion sequences TBD; blending/switching method TBD; entry/exit/abort criteria TBD; failed-transition logic TBD; corridor definitions TBD; unmanned test scope/methods TBD; ISS-006 limiting.

## 16. Assumptions


_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SAD (ARC-002/003/004), CTL-001/003/004, hover/cruise controllers (Ch 07.11/07.13), velocity channel (Ch 07.10), Vol 03–06 (aero/propulsion trades, ISS-003/004/007), Vol 07 law sets, Vol 08/16 (compute/sensing), safety view (02.10), Vol 19/33 (SIL/HIL/test).

## 18. Traceability

Parents: SYS-001; CON-001/003; CTL-001/003/004; MIS-001/002; FCR/FCL tier (allocation TBD). Children: Vol 07 detailed transition design, V&V cases. RTM: REQ-HFPX-FTN-001..005 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 3 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 3 draft (Chapter 07.12) |
| B | 2026-09-29 | Assumptions removed; all unknowns recorded as TBD (no assumptions raised or relied upon). |
