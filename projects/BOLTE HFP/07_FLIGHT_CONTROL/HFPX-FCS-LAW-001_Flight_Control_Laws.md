# Flight Control Laws

**Document ID:** HFPX-FCS-LAW-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 3 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the flight control law framework for HFP-X (Chapter 07.4): per-mode law structure, gain-scheduling/interpolation, anti-windup/saturation handling, switching-transient bounds, identification/versioning, and the no-AI primary-path constraint. No law values are defined.

## 2. Scope

Covers law architecture and constraints for hover/transition/cruise. Law forms, gains, schedules, bandwidths, margins, rates, limits, and transient bounds are TBD. Axis implementations are in ATT/ROL/PIT docs. No AI in the primary control path.

## 3. Applicable Documents

- HFPX-FCS-REQ-001 (FCR-001..003); HFPX-ARC-CTL-001 (CTL-001); SAD ARC-004; SyRS SYS-002
- Companion: HFPX-FCS-ARC-001, HFPX-FCS-ATT-001, HFPX-FCS-ROL-001, HFPX-FCS-PIT-001
- Vol 19 (modelling/SIL/HIL); ISS-006 (authority)

## 4. Definitions & Acronyms

- Control law: algorithm mapping commands/estimates to generalised force/moment demands (forms TBD).
- Gain-scheduling/interpolation: blending of law parameters across regimes (schedules TBD).
- Anti-windup/saturation: handling of actuator/effector saturation (scheme TBD).
- Switching transient: response during law-set changeover (bounds TBD).
- Law identification/versioning: unique ID and version for each law build (scheme TBD).
- AI: artificial-intelligence/machine-learned components — excluded from primary path.

## 5. System Context

Laws execute within the FCS architecture under the mode supervisor, fed by shaped commands and fusion estimates, outputting to allocation/mixing. Law versions are configuration-controlled and verified by analysis/SIL/HIL/test.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-FCL-001 | The FCS shall implement a defined control-law structure for each of hover, transition, and cruise modes (structures/forms TBD). | ARC-004, SYS-002 | Analysis + SIL (TBD) |
| REQ-HFPX-FCL-002 | Gain-scheduling and interpolation between law sets shall be defined (schedules, breakpoints, and blending TBD). | ARC-004, SYS-002 | Analysis + SIL (TBD) |
| REQ-HFPX-FCL-003 | Anti-windup and saturation handling for effector/actuator limits shall be defined (scheme and limits TBD). | ARC-004 | Analysis + SIL + HIL (TBD) |
| REQ-HFPX-FCL-004 | Law-switching transients shall be bounded with defined criteria (bounds and criteria TBD). | ARC-004, SYS-002 | Analysis + SIL + HIL (TBD) |
| REQ-HFPX-FCL-005 | Each control law shall carry a unique identification and version under configuration control (scheme TBD). | SYS-002 | Analysis (TBD) |
| REQ-HFPX-FCL-006 | The primary control path shall contain no AI/machine-learned components (verification by design inspection and analysis, TBD). | SYS-002, ARC-004 | Analysis (TBD) |

No gains, bandwidths, margins, rates, or limits are stated. All quantitative content is TBD.

## 7. Architecture

Text block diagram:

```
[Shaped Commands + Estimates] --> [Hover Laws (TBD)] --\
                              --> [Transition Laws (TBD)] --> [Gain Schedule / Interpolation (FCL-002, TBD)] --> [Anti-Windup/Saturation (FCL-003, TBD)] --> [Switching-Transient Management (FCL-004, TBD)] --> [Allocation]
                              --> [Cruise Laws (TBD)] --/
[Law ID / Version Registry (FCL-005, TBD)] governs all law builds; [No-AI Primary Path (FCL-006)] constrains implementation.
```

Law forms (e.g., TBD — no PID/state-space or other form claimed), schedules, and transient managers are TBD.

## 8. Detailed Design

Not applicable at Tranche 3 draft level. All law equations, coefficients, tables, and code are TBD.

## 9. Interfaces

- Command/estimate input ICD: TBD.
- Law-output to allocation ICD: TBD.
- Law ID/version registry interface: TBD.
- SIL/HIL law-model interface (Vol 19): TBD.

## 10. Operational Concept

Laws support hover/transition/cruise operations with scheduled blending and bounded changeover; saturation handling preserves stability pending safety handover (all behaviours TBD).

## 11. Safety

Unbounded switching transients, windup-induced divergence, unscheduled gains, or unverified law versions are hazardous. Mitigations required (all TBD): defined structures (FCL-001), verified scheduling (FCL-002), anti-windup (FCL-003), bounded transients (FCL-004), version control (FCL-005), and deterministic non-AI primary path (FCL-006). No stability claim is made.

## 12. Performance

Law accuracy, robustness, transient bounds, and compute budgets are TBD. No performance value is stated.

## 13. Verification & Validation

Verified by analysis (stability/robustness, TBD methods), SIL/HIL (Vol 19), and test; switching/saturation cases by fault injection (criteria TBD). Law versions tracked for V&V traceability.

## 14. Risks

- Law design entirely TBD; mitigation: framework requirements held explicit, detailed design deferred to later tranche with Vol 19 modelling.
- Scheduling/anti-windup/transient unknowns; mitigation: bounded-transient requirement with TBD criteria, validated by SIL/HIL.

## 15. Open Issues

- Law forms TBD; schedules TBD; anti-windup scheme TBD; transient bounds TBD; ID/version scheme TBD; no-AI verification method TBD.

## 16. Assumptions

- A-FCL-001: Regime-specific laws with scheduled interpolation are required (validation: Vol 07/19 trade, TBD).

## 17. Dependencies

Depends on ARC-004, SYS-002, CTL-001, FCS architecture/input, aero/propulsion models, ISS-006, Vol 19 rigs, configuration management.

## 18. Traceability

Parents: ARC-004, SYS-002. Children: axis law implementations (ATT/ROL/PIT), SIL/HIL models, V&V cases. RTM: REQ-HFPX-FCL-001..006 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 3 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 3 draft (Chapter 07.4) |
