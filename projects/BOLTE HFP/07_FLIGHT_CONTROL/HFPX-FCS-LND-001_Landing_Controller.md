# Landing Controller

**Document ID:** HFPX-FCS-LND-001  
**Revision:** B (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 3 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X landing controller (Chapter 07.14): vertical-landing sequencing, touchdown detection and thrust cutoff, landing-abort/go-around hooks, and unmanned-first verification. All sequences, thresholds, and capabilities are TBD.

## 2. Scope

Covers vertical landing from hover/descent through touchdown and shutdown at structure-only level, including sequencing, detection/cutoff, abort/go-around hooks, and verification approach. Excludes law selection, gain values, descent-profile values, detection-threshold values, and abort-capability values — all TBD. No component selected.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (REQ-HFPX-SYS-001); HFPX-CONOPS-001 (CON-001/003); HFPX-ARC-CTL-001 (CTL-001/003/004); HFPX-MIS-REQ-001/002 (MIS-001/002)
- FCR/FCL tier requirements (as allocated, TBD)
- Vol 06.18 (ground effect); Vol 07 (flight control laws); Vol 13 (safety); Vol 19 (modelling/SIL/HIL); Vol 33 (flight test); ISS-006 (control authority)

## 4. Definitions & Acronyms

- Vertical landing: controlled descent to touchdown on distributed thrust (profile TBD).
- Touchdown detection/cutoff: sensing of ground contact and subsequent thrust reduction/shutdown (thresholds and sequence TBD).
- Landing abort/go-around: discontinuation of landing and return to hover/hold (capability and sequence TBD).
- FCR/FCL: flight-control-related requirement tiers (allocation TBD).

## 5. System Context

The landing controller operates as a terminal-phase law set closely coupled to the hover controller (Ch 07.11) and altitude/velocity channels (Ch 07.9–07.10). It takes landing commands plus navigation/height estimates (sensors TBD), sequences descent to touchdown, detects contact, commands cutoff, and offers abort hooks. The safety computer monitors descent and margins in parallel with independent stabilisation authority (TBD).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-FLD-001 | The FCS shall provide vertical-landing sequencing from descent through touchdown and shutdown (sequence TBD). | SYS-001, CON-001, CTL-001, MIS-001 | Analysis + SIL/HIL + Test (unmanned) |
| REQ-HFPX-FLD-002 | The FCS shall provide touchdown detection and thrust cutoff with defined thresholds and sequencing (thresholds TBD). | SYS-001, CTL-003, FCR-xxx (TBD) | Analysis + SIL/HIL + Test (unmanned) |
| REQ-HFPX-FLD-003 | The FCS shall provide landing-abort/go-around hooks with defined capability and sequencing (capability TBD). | SYS-001, CON-003, CTL-004, MIS-002 | Analysis + SIL/HIL + Test (unmanned) |
| REQ-HFPX-FLD-004 | Landing shall be verified by analysis and SIL/HIL and validated by unmanned flight test before any human exposure (methods TBD). | SYS-001, CON-003, CTL-004, MIS-002 | Analysis + SIL/HIL + Test (unmanned) |

## 7. Architecture

Landing sequencer (TBD) with descent, flare/touchdown, and shutdown phases (all TBD), touchdown-detection block fusing contact/height/load inputs (sensors and logic TBD) driving thrust cutoff, and abort/go-around branch returning to hover hold or safety handover (capability TBD). Descent demand feeds thrust allocation/mixing within authority limits (TBD, ISS-006) with ground-effect hooks per Vol 06.18 (TBD).

## 8. Detailed Design

Not applicable at Tranche 3 draft level. Control laws, gains, profiles, detection thresholds, cutoff sequences, abort sequences, and allocation matrices are TBD (Vol 07, Vol 19).

## 9. Interfaces

Interfaces to hover controller, altitude/velocity channels, navigation/height sensing, landing-gear/contact sensing (set TBD), pilot/operator controls, thrust allocation/mixing, propulsion effectors, and safety monitoring are TBD. Each shall be captured in an ICD (02.17) before CDR per ARC-005.

## 10. Operational Concept

Landing supports nominal vertical landing, off-nominal touchdown handling, and aborted landing (profiles TBD). Normal operation sequences descent to detected touchdown and cutoff; off-nominal operation executes abort/go-around within TBD capability or hands over to the safety path per CON-003. All landing validation is unmanned first (Vol 33).

## 11. Safety

Hard touchdown, tip-over, thrust-cutoff failure, or failed abort is hazardous: defined sequencing (FLD-001), bounded detection/cutoff (FLD-002), abort hooks with handover (FLD-003), and unmanned-first validation (FLD-004) plus the independent safety path (ARC-003) mitigate it. No controllability claim is made; all thresholds TBD pending Vol 06/07/13 analysis and unmanned test.

## 12. Performance

Descent-profile tracking characteristics, touchdown-detection performance, cutoff transients, abort capability bounds, and compute-load budgets are TBD. No altitudes, rates, or margin values are stated.

## 13. Verification & Validation

Verified by analysis (stability, detection logic, margin budgets) and SIL/HIL including ground-effect and contact models (methods TBD); validated by unmanned flight test before any human exposure (Vol 19/33). Abort and cutoff-failure cases tested by fault injection (methods TBD).

## 14. Risks

- Ground-effect and contact-dynamics uncertainty (Vol 06.18 TBD) affecting touchdown behaviour; mitigation: explicit hooks and contact-model SIL/HIL, TBD.
- Landing-abort capability TBD — go-around may not be achievable in all states; mitigation: capability stub explicit, verification unmanned first.

## 15. Open Issues

Landing sequences TBD; touchdown-detection thresholds and sensor set TBD; thrust-cutoff sequence TBD; abort/go-around capability and sequence TBD; unmanned test scope/methods TBD.

## 16. Assumptions


_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SAD (ARC-002/003/004), CTL-001/003/004, hover controller (Ch 07.11), altitude/velocity channels (Ch 07.9–07.10), Vol 03–06 (aero/propulsion/gear trades, ISS-003/004/007; esp. Vol 06.18), Vol 07 law sets, Vol 08/16 (compute/sensing), safety view (02.10), Vol 19/33 (SIL/HIL/test).

## 18. Traceability

Parents: SYS-001; CON-001/003; CTL-001/003/004; MIS-001/002; FCR/FCL tier (allocation TBD). Children: Vol 07 detailed landing design, V&V cases. RTM: REQ-HFPX-FLD-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 3 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 3 draft (Chapter 07.14) |
| B | 2026-09-29 | Assumptions removed; all unknowns recorded as TBD (no assumptions raised or relied upon). |
