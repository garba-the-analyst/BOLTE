# Control Architecture

**Document ID:** HFPX-ARC-CTL-001  
**Revision:** B (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 2 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X control architecture view (Chapter 02.12): flight-regime law sets and switching, thrust-allocation/mixing ownership, control-authority margins, and fault-tolerant control hooks.

## 2. Scope

Covers hover, transition, and cruise control structure for the production-aircraft concept. Control laws, gains, and margin values are TBD (Vol 07). No component selected.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (REQ-HFPX-SYS-001..008); HFPX-SYS-ARC-001 SAD (REQ-HFPX-ARC-001..005)
- Vol 07 (flight control laws); Vol 19 (modelling/SIL/HIL); ISS-006 (control authority)
- HFP prompt §§11–13 (control view, flight modes)

## 4. Definitions & Acronyms

- Law set: controller structure per flight regime (hover/transition/cruise), all TBD.
- Mixing/allocation: mapping FCS commands to propulsion effectors (owner TBD).
- Authority margin: remaining control capability above trim/manoeuvre demand (values TBD, ISS-006).

## 5. System Context

Control architecture takes pilot/operator commands plus navigation estimates, computes effector commands through regime-specific laws, and distributes them via mixing to propulsion modules. Safety computer monitors in parallel with independent stabilisation authority.

## 6. Requirements

| ID | Requirement (shall) | Verification |
| --- | --- | --- |
| REQ-HFPX-CTL-001 | Hover, transition, and cruise shall use distinct control-law sets with defined switching logic and abort criteria (laws and criteria TBD, Vol 07). | Analysis + Test |
| REQ-HFPX-CTL-002 | Thrust-allocation/mixing ownership and authority limits shall be defined (owner TBD, limits TBD). | Analysis |
| REQ-HFPX-CTL-003 | Control-authority margins for each regime and failure case shall be defined (values TBD, ISS-006). | Analysis |
| REQ-HFPX-CTL-004 | Fault-tolerant control hooks (detection input, reconfiguration, degraded modes — TBD) shall be provided to the safety architecture. | Analysis + Test |

## 7. Architecture

Three law sets (hover / transition / cruise, all TBD per Vol 07) with a switching supervisor: regime detection, hysteresis, and abort-to-hover/safety criteria (all TBD). FCS owns mixing/thrust allocation unless reallocated by trade (owner TBD); allocation maps generalised forces/moments to module commands within authority limits (TBD). Authority margins (ISS-006) are budgeted per regime and failure case (values TBD). Fault-tolerant hooks take health/fault inputs from monitoring, trigger reconfiguration or degraded modes, and hand over to the safety path when margins are exceeded. Primary control remains deterministic and bounded per ARC-002.

## 8. Detailed Design

Not applicable at Tranche 2 draft level. Laws, gains, switching thresholds, and allocation matrices are TBD (Vol 07, Vol 19).

## 9. Interfaces

Interfaces to sensors/fusion, propulsion effectors, safety computer, and pilot controls are TBD. Each shall be captured in an ICD (02.17) before CDR per ARC-005.

## 10. Operational Concept

Control view supports all 15 flight modes; hover stresses authority margins, transition stresses switching/abort logic, cruise stresses efficiency/stability. Degraded control hands over to safety/recovery per CONOPS.

## 11. Safety

Loss of control authority or uncommanded switching is hazardous: distinct law sets with defined switching (CTL-001), enforced margins (CTL-003), and fault-tolerant handover (CTL-004) plus the independent safety path (ARC-003) mitigate it. No controllability claim is made; all margins TBD pending ISS-006 and Vol 07/13 analysis.

## 12. Performance

Handling qualities, tracking error, switching transients, and compute-load budgets are TBD. No allocation value is stated.

## 13. Verification & Validation

Verified by analysis (stability, switching logic) and SIL/HIL; later validated by unmanned flight (Vol 19/33). Switching and reconfiguration tested by fault injection (methods TBD).

## 14. Risks

- ISS-006: authority margins unknown until aero/propulsion trades close; mitigation: margin budget holders assigned, stub status explicit.
- Switching transients destabilising transition; mitigation: abort criteria and safety-path backstop, laws TBD.

## 15. Open Issues

ISS-006 (authority margins); control laws TBD; switching/abort criteria TBD; mixing ownership TBD; fault-tolerant scheme TBD.

## 16. Assumptions


_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SAD (ARC-001..005), Vol 07 (laws), Vol 03–06 (aero/propulsion trades, ISS-003/004/007), Vol 08/16 (compute), safety view (02.10), data view (02.11).

## 18. Traceability

Parents: SyRS REQ-HFPX-SYS-001..008; SAD REQ-HFPX-ARC-001..005 (esp. ARC-002, ARC-003, ARC-004); tier inputs FUN/SAF as allocated. Children: Vol 07 designs, V&V cases. RTM: REQ-HFPX-CTL-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 2 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 2 draft (Chapter 02.12) |
| B | 2026-09-29 | Assumptions removed; all unknowns recorded as TBD (no assumptions raised or relied upon). |
