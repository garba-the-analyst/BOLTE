# FCS Requirements

**Document ID:** HFPX-FCS-REQ-001  
**Revision:** B (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 3 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the top-level Flight Control System (FCS) requirements for HFP-X (Chapter 07.1): stabilisation and control across the flight envelope including transition, determinism, regime law sets, fault annunciation, and external interfaces. No control-law values are defined in this document.

## 2. Scope

Covers primary FCS functional requirements for hover, transition, and cruise, including determinism, mode law sets, health annunciation, and interfaces to propulsion, navigation, and HMI. Control-law forms, gains, bandwidths, margins, rates, and limits are TBD (detailed in HFPX-FCS-LAW-001, HFPX-FCS-ATT-001, HFPX-FCS-ROL-001, HFPX-FCS-PIT-001). No component selected. No verification claim made.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (REQ-HFPX-SYS-001, SYS-002); stakeholder needs STK-002
- HFPX-ARC-CTL-001 Control Architecture (REQ-HFPX-CTL-001); HFPX-SYS-ARC-001 SAD (ARC-004)
- Vol 07 companion docs: HFPX-FCS-ARC-001, HFPX-FCS-INP-001, HFPX-FCS-LAW-001, HFPX-FCS-ATT-001, HFPX-FCS-ROL-001, HFPX-FCS-PIT-001
- Vol 08/16 (compute allocation); Vol 10/12 (HMI/operator input); Vol 19 (modelling/SIL/HIL); ISS-006 (control authority)

## 4. Definitions & Acronyms

- FCS: Flight Control System — computes effector commands from pilot/operator commands and navigation estimates.
- Envelope: hover, transition, and cruise regimes, including transition ingress/egress (boundaries TBD).
- Deterministic bounded control: primary control executes with bounded timing and bounded outputs (values TBD).
- Law set: controller structure per flight regime (forms and values TBD).
- Health/fault annunciation: reporting of FCS health and fault status to safety/HMI (mechanism TBD).
- TBD / TBC: to be defined / to be confirmed. No values stated.

## 5. System Context

FCS sits between command/navigation sources and propulsion effectors. It receives pilot/operator commands (via HFPX-FCS-INP-001) and navigation/fusion estimates, executes regime-appropriate control laws under a mode supervisor (per HFPX-FCS-ARC-001 / HFPX-ARC-CTL-001), distributes commands via thrust allocation/mixing, and annunciates health/faults to the safety computer and HMI. The safety computer provides an independent monitoring path.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-FCR-001 | The FCS shall stabilise and control the aircraft across the defined flight envelope, including hover, transition, and cruise (envelope boundaries and criteria TBD). | SYS-001, SYS-002 | Analysis + SIL + HIL + Test (TBD) |
| REQ-HFPX-FCR-002 | The primary FCS control path shall be deterministic and bounded in execution and output (timing, bounds, and methods TBD). | SYS-002, CTL-001 | Analysis + SIL + HIL (TBD) |
| REQ-HFPX-FCR-003 | The FCS shall provide distinct hover, transition, and cruise control-law sets with defined switching logic (laws, thresholds, and abort criteria TBD, Vol 07). | CTL-001, SYS-002 | Analysis + SIL + Test (TBD) |
| REQ-HFPX-FCR-004 | The FCS shall annunciate its health and fault status to the safety system and HMI (signals, latencies, and integrity TBD). | SYS-002, STK-002 | Analysis + SIL + HIL (TBD) |
| REQ-HFPX-FCR-005 | The FCS shall interface to propulsion (effector commands), navigation/fusion (estimates), and HMI/operator (commands/status) via defined ICDs (all ICDs TBD). | SYS-001, SYS-002 | Analysis + Test (TBD) |
| REQ-HFPX-FCR-006 | Each FCS requirement in this document shall have a defined verification method and pass criteria (methods and criteria TBD per requirement). | SYS-002 | Analysis (TBD) |

No gains, bandwidths, margins, rates, or limits are stated. All quantitative content is TBD.

## 7. Architecture

Top-level FCS partition (text block diagram):

```
[Pilot/Operator Input] --> [Command Shaping/Limiting (TBD)] --\
[Nav / Sensor Fusion] --> [Input Interface (TBD)] -------------> [Mode Supervisor + Law Sets: Hover / Transition / Cruise (TBD)] --> [Allocation/Mixing (TBD)] --> [Propulsion Effectors]
                                                                                                                                    |
                                                                 [Health/Fault Annunciation (TBD)] --> [Safety Computer / HMI]
[Monitoring Path (TBD)] <--> [Safety Computer] (independent path, TBD)
```

FCS requirements allocate to architecture (HFPX-FCS-ARC-001), input system (HFPX-FCS-INP-001), laws (HFPX-FCS-LAW-001), and axis functions (ATT/ROL/PIT). Software/hardware allocation is TBD (Vol 08/16).

## 8. Detailed Design

Not applicable at Tranche 3 draft level. Law structures, parameters, thresholds, ICD signals, and annunciation implementations are TBD.

## 9. Interfaces

- Pilot/operator command input: TBD (devices TBD, Vol 10/12; see HFPX-FCS-INP-001).
- Navigation/fusion input: TBD (see HFPX-FCS-ARC-001).
- Propulsion effector output via allocation/mixing: TBD (owner TBD per CTL-002).
- Safety computer monitoring/annunciation: TBD.
- HMI status display: TBD.
- Each interface shall be captured in an ICD before CDR (ICDs TBD).

## 10. Operational Concept

FCS requirements support all flight modes; hover stresses stabilisation authority, transition stresses law-set switching/abort, cruise stresses tracking/stability. Degraded operation hands over to safety/recovery per CONOPS (details TBD).

## 11. Safety

Loss of stabilisation/control or undetected FCS fault is hazardous. Mitigations required (all TBD): deterministic bounded primary path (FCR-002), distinct law sets with switching/abort (FCR-003), health/fault annunciation plus independent monitoring (FCR-004). No controllability or integrity claim is made at this revision.

## 12. Performance

Stabilisation accuracy, tracking error, switching transients, timing budgets, and compute-load budgets are TBD. No performance value is stated. No gains, bandwidths, margins, rates, or limits are stated.

## 13. Verification & Validation

Verification methods are TBD per requirement (see table). Intended strategy: analysis (stability, logic), SIL/HIL (Vol 19), and test including fault injection (methods, rigs, and pass criteria TBD). No V&V complete at this revision.

## 14. Risks

- Envelope/control requirements unstable until aero/propulsion trades close; mitigation: requirements held as TBD with explicit parents, refined in Vol 07.
- ISS-006: authority margins unknown; mitigation: margin requirements deferred to axis docs with TBD values, stub status explicit.
- Determinism/bounding unproven without compute allocation (Vol 08/16); mitigation: allocation TBD, verification by SIL/HIL TBD.

## 15. Open Issues

- Envelope boundaries TBD; law forms and all quantitative values TBD; switching/abort criteria TBD.
- ICDs TBD; annunciation signals/latencies TBD; verification methods and pass criteria TBD per requirement.
- ISS-006 (authority margins) open.

## 16. Assumptions


_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SyRS (SYS-001/002), STK-002, CTL-001, SAD ARC-004, Vol 03–06 trades, Vol 08/16 compute, Vol 10/12 HMI, Vol 19 V&V, and safety view.

## 18. Traceability

Parents: SYS-001, SYS-002, STK-002, CTL-001. Children: HFPX-FCS-ARC-001, HFPX-FCS-INP-001, HFPX-FCS-LAW-001, HFPX-FCS-ATT-001, HFPX-FCS-ROL-001, HFPX-FCS-PIT-001; V&V cases (TBD). RTM: REQ-HFPX-FCR-001..006 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 3 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 3 draft (Chapter 07.1) |
| B | 2026-09-29 | Assumptions removed; all unknowns recorded as TBD (no assumptions raised or relied upon). |
