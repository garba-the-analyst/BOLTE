# Logical Architecture

**Document ID:** HFPX-ARC-LOG-001  
**Revision:** B (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 2 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X logical architecture (Chapter 02.4): system interactions, signal chains and switching logic independent of hardware and software implementation. Establishes command, data-flow and fault-response behaviour.

## 2. Scope

Covers command→response chains, sensor-fusion→navigation→control/safety data flow, fault-detection→mitigation logic, and hover/transition/cruise mode-switching logic. Excludes hardware selection, software layering and quantitative timing (TBD in HW/SW/AVN views).

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parent requirements REQ-HFPX-SYS-001..008)
- HFPX-SYS-ARC-001 SAD (parent requirements REQ-HFPX-ARC-001..005)
- HFPX-SYS-CON-001 CONOPS; HFP prompt §§11–13; Vol 07 (control), Vol 08 (avionics), Vol 13 (safety)

## 4. Definitions & Acronyms

- Signal chain: ordered path from command or sensor input to actuator or display response.
- Sensor fusion: combination of sensor inputs into navigation/state estimates.
- Mode-switching logic: rules governing transitions between hover, transition and cruise control sets.

## 5. System Context

Logical architecture connects pilot/operator intent and environmental sensing to thrust and safety responses. It operates within CONOPS modes and consumes functional allocations (FUN view), producing interaction requirements for hardware, software and avionics views.

## 6. Requirements

| ID | Requirement (shall) | Verification |
| --- | --- | --- |
| REQ-HFPX-LOG-001 | The logical architecture shall define command-to-response signal chains from pilot/operator inputs to actuator outputs. | Analysis |
| REQ-HFPX-LOG-002 | The logical architecture shall define sensor-fusion-to-navigation-to-control/safety data flow. | Analysis |
| REQ-HFPX-LOG-003 | The logical architecture shall define fault-detection-to-mitigation logic. | Analysis |
| REQ-HFPX-LOG-004 | The logical architecture shall define mode-switching logic for hover, transition, and cruise modes including abort criteria. | Analysis |

## 7. Architecture

Logical flows (starter; thresholds, timings and laws TBD):

```text
PILOT/OPERATOR → [command shaping] → FCS mixing/thrust allocation → PROPULSION modules
SENSORS → [fusion] → NAVIGATION estimate → FCS (primary) + SAFETY computer (parallel)
HEALTH MONITOR → [fault detection] → MITIGATION (reconfigure / stabilise / recover / abort)
MODE MANAGER: HOVER ⇄ TRANSITION ⇄ CRUISE (entry/exit/abort criteria TBD, Vol 07)
```

Primary and safety paths run in parallel with independent detection thresholds (TBD Vol 13). AI monitoring output feeds advisory channel only and cannot silently override pilot or safety authority (ARC-002). Switching logic owns entry, exit and abort conditions; control laws TBD.

## 8. Detailed Design

Not applicable at this level. Signal definitions, message sets and statecharts are deferred to Vol 07/08/16. No timing or threshold values stated.

## 9. Interfaces

Logical interfaces: L-CMD (commands), L-NAV (estimates), L-FLT (fault flags), L-MIT (mitigation commands), L-MODE (mode state). Message content, rates and protocols TBD in ICDs (02.17) and data-bus design (Vol 08).

## 10. Operational Concept

Logical chains execute per CONOPS state machine across all 15 flight modes. Transition mode exercises switching logic most heavily; emergency modes prioritise fault→mitigation chains. Detail per CONOPS and Vol 07.

## 11. Safety

Dual-path logic (primary + independent safety) is enforced by construction (ARC-003). Fault-detection→mitigation logic feeds FHA/FMEA/FTA (Vol 13). Abort criteria are safety-owned inputs.

## 12. Performance

Latency, throughput and accuracy budgets for logical chains are TBD. Budget holders: control (Vol 07), compute/data (Vol 08/16). No values stated.

## 13. Verification & Validation

Verified by analysis (chain completeness, flow coverage, switching-logic review). Validated later via SIL/HIL and unmanned flight (Vol 19/33).

## 14. Risks

- Circular or conflicting command/safety logic; mitigation: independent-path review and Vol 13 analysis.
- Mode-switching chatter or undefined aborts; mitigation: explicit entry/exit/abort ownership in Vol 07.

## 15. Open Issues

Detection thresholds, timings, message sets and abort criteria TBD. Mode-manager ownership split between FCS and safety computer TBD.

## 16. Assumptions


_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on FUN allocations, CONOPS modes, control-law breakdown (Vol 07), avionics/data design (Vol 08/16), and safety analyses (Vol 13).

## 18. Traceability

Parents: SyRS REQ-HFPX-SYS-001..008; SAD REQ-HFPX-ARC-001..005 (notably ARC-002/003/004). Children: Vol 03–18 subsystem docs (esp. Vol 07/08/13/16), ICDs. RTM: REQ-HFPX-LOG-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 2 draft, not baselined. Chapter 02.4.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 2 draft (Chapter 02.4) |
| B | 2026-09-29 | Assumptions removed; all unknowns recorded as TBD (no assumptions raised or relied upon). |
